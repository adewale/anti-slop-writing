#!/usr/bin/env python3
"""Blind, batch, unblind, and score the 2026-09-23 re-run under its pre-registration.

  batches: python3 score_rerun.py batches --manifest M --audit A --outputs DIR --out BATCH_DIR --key KEY
  score:   python3 score_rerun.py score --key KEY --judgments DIR --judge-audit REPORT --out RESULTS_DIR

`batches` takes each slot's audited trial, splits guard trials into their four
cases, gives every critique an opaque id (seed 20260923), shuffles across arms,
and writes batches of at most six, plus the key to a path outside the batch
directory so no judge can reach it. `score` reads, for each batch and judge,
the one file that audit_judges.py marked valid, unblinds the judgments, scores them with scripts/run_evals.py grade, pairs discriminating
trials by slot, runs scripts/score_delta.py for the tune and holdout gates, and
counts guard over-flags (first assertion failed) per arm.
Run from the repository root.
"""
import argparse
import json
import random
import re
import subprocess
from collections import defaultdict
from pathlib import Path

SEED = 20260923
BATCH = 6
JUDGES = {"sonnet": "claude-sonnet-5", "haiku": "claude-haiku-4-5-20251001"}
PRIMARY = "sonnet"
GATES = [("coined-compound-label", False), ("holdout-coined-compound-label", True)]
GUARD_LIMIT = 1  # candidate over-flags may exceed baseline's by at most this many per guard


def load_case(suite, case_id):
    return next(c for c in json.loads(Path("evals", suite).read_text())["evals"] if c["id"] == case_id)


def render(item, case):
    a = "\n".join(f"{i}. {x}" for i, x in enumerate(case["assertions"], 1))
    g = "\n".join(f"- {d['name']} ({d['scale']}): {d['rubric']}" for d in case.get("graded_dimensions", [])) or "- none"
    return (f"=== ITEM {item['blind_id']} ===\nREQUEST THE CRITIQUE RESPONDS TO:\n{case['prompt']}\n\n"
            f"ASSERTIONS (judge each independently):\n{a}\n\nGRADED DIMENSIONS (score 1-5; empty list if none):\n{g}\n\n"
            f"CRITIQUE UNDER REVIEW:\n{item['text']}\n=== END ITEM {item['blind_id']} ===\n")


def cmd_batches(args):
    trials = {f"{t['kind']}:{t.get('case_id', 'guards')}:{t['arm']}:{t['slot']}": t
              for t in json.loads(args.manifest.read_text())["trials"]}
    audit = json.loads(args.audit.read_text())
    items = []
    for key, s in sorted(audit["slots"].items()):
        assert s["status"] == "valid", f"slot {key} is {s['status']}; every slot must hold a valid trial"
        t = trials[key]
        body = (args.outputs / Path(s["trial"]).name).read_text()
        base = {"arm": t["arm"], "slot": t["slot"], "trial": Path(s["trial"]).stem}
        if t["kind"] == "discriminating":
            items.append(dict(base, suite=t["suite"], case_id=t["case_id"], split=t["split"], text=body.strip()))
            continue
        parts = re.split(r"^##\s*(R[1-4])\s*$", body, flags=re.MULTILINE)
        sections = {parts[i]: parts[i + 1].strip() for i in range(1, len(parts), 2)}
        for g in t["guards"]:
            case = load_case(g["suite"], g["case_id"])
            items.append(dict(base, suite=g["suite"], case_id=g["case_id"], split=case["split"],
                              text=sections[g["heading"]]))
    rng = random.Random(SEED)
    used = set()
    for it in items:
        while True:
            b = "j" + "".join(rng.choice("abcdefghjkmnpqrstuvwxyz23456789") for _ in range(6))
            if b not in used:
                used.add(b)
                break
        it["blind_id"] = b
    rng.shuffle(items)
    args.out.mkdir(parents=True, exist_ok=True)
    for n in range(0, len(items), BATCH):
        chunk = items[n:n + BATCH]
        (args.out / f"batch-{n // BATCH + 1:03d}.md").write_text(
            "\n".join(render(it, load_case(it["suite"], it["case_id"])) for it in chunk))
    key = [{k: it[k] for k in ("blind_id", "suite", "case_id", "split", "arm", "slot", "trial")} for it in items]
    assert args.out.resolve() not in args.key.resolve().parents, "keep the key out of the batch directory"
    args.key.write_text(json.dumps(key, indent=2))
    print(f"{len(items)} items in {-(-len(items) // BATCH)} batches -> {args.out}")


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    return (r.stdout + r.stderr).strip()


def cmd_score(args):
    key = {k["blind_id"]: k for k in json.loads(args.key.read_text())}
    args.out.mkdir(parents=True, exist_ok=True)
    scores, firsts, raw = {}, {}, {}
    batches = json.loads(args.judge_audit.read_text())["batches"]
    for judge in JUDGES:
        recs = []
        for name, b in sorted(batches.items()):
            if not name.startswith(f"{judge}-"):
                continue
            assert b["status"] == "valid", f"{name} is {b['status']}; every batch needs a valid judgment"
            f = args.judgments / b["file"]
            recs += [json.loads(line) for line in f.read_text().splitlines() if line.strip()]
        ids = [r["id"] for r in recs]
        assert sorted(ids) == sorted(key), f"{judge}: judged ids do not match the key"
        raw[judge] = {r["id"]: r for r in recs}
        unblinded = args.out / f"judgments-{judge}.unblinded.jsonl"
        with unblinded.open("w") as fh:
            for r in recs:
                k = key[r["id"]]
                fh.write(json.dumps({"id": f"{k['case_id']}::{k['arm']}::{k['slot']}", "suite": k["suite"],
                                     "split": k["split"], "assertions": r["assertions"],
                                     "graded_dimensions": r.get("graded_dimensions", [])}) + "\n")
        sp = args.out / f"scores-{judge}.jsonl"
        run(["python3", "scripts/run_evals.py", "grade", str(unblinded), "--split", "all", "--out", str(sp)])
        scores[judge] = {s["id"]: s for s in (json.loads(x) for x in sp.read_text().splitlines() if x.strip())}
        firsts[judge] = {f"{key[r['id']]['case_id']}::{key[r['id']]['arm']}::{key[r['id']]['slot']}":
                         bool(r["assertions"][0]["pass"]) for r in recs}
    lines = ["# Re-run results", "", f"Primary judge `{JUDGES[PRIMARY]}`, secondary judge `{JUDGES['haiku']}`.", ""]
    by_case = defaultdict(lambda: defaultdict(list))
    for k in key.values():
        by_case[k["case_id"]][k["arm"]].append(k)
    lines += ["| Case | Split | Arm | Trials | Mean score, primary | First assertion, primary | Mean score, secondary | First assertion, secondary |",
              "|---|---|---|---:|---:|---:|---:|---:|"]
    for case_id in sorted(by_case):
        for arm in ("baseline", "candidate"):
            ks = by_case[case_id][arm]
            ids = [f"{k['case_id']}::{k['arm']}::{k['slot']}" for k in ks]
            cells = []
            for j in (PRIMARY, "haiku"):
                cells += [f"{sum(scores[j][i]['score'] for i in ids) / len(ids):.3f}", f"{sum(firsts[j][i] for i in ids)}/{len(ids)}"]
            lines.append(f"| {case_id} | {ks[0]['split']} | {arm} | {len(ks)} | " + " | ".join(cells) + " |")
    agree = sum(bool(a["pass"]) == bool(b["pass"]) for bid in key
                for a, b in zip(raw[PRIMARY][bid]["assertions"], raw["haiku"][bid]["assertions"]))
    total = sum(len(raw[PRIMARY][bid]["assertions"]) for bid in key)
    lines += ["", f"Judge agreement: {agree}/{total} assertions.", ""]
    verdicts = {}
    for judge in JUDGES:
        for case_id, holdout in GATES:
            n = max(k["slot"] for k in by_case[case_id]["baseline"])
            delta = args.out / f"delta-{judge}-{case_id}.jsonl"
            with delta.open("w") as fh:
                for slot in range(1, n + 1):
                    b, c = f"{case_id}::baseline::{slot}", f"{case_id}::candidate::{slot}"
                    fh.write(json.dumps({"id": f"{case_id}-slot{slot:02d}", "split": "holdout" if holdout else "tune",
                                         "before": scores[judge][b]["score"], "after": scores[judge][c]["score"]}) + "\n")
            cmd = ["python3", "scripts/score_delta.py", str(delta), "--sesoi", "0.05"] + (["--holdout-only"] if holdout else [])
            out = run(cmd)
            # score_delta prints ACCEPT for any delta that clears the noise floor,
            # including a regression. Only an improvement passes the gate.
            verdicts[(judge, case_id)] = ("ACCEPT" if "Verdict:       ACCEPT (improvement" in out
                                          else "REJECT (regression)" if "Verdict:       ACCEPT" in out
                                          else "REJECT")
            lines += [f"### Gate: {case_id} ({'holdout' if holdout else 'tune'}), {judge} judge", "", "```txt", out, "```", ""]
    lines += ["## Guards", "", "| Guard | Baseline over-flags | Candidate over-flags | Within limit |", "|---|---:|---:|---|"]
    guard_ok = True
    for case_id in sorted(c for c in by_case if c not in dict(GATES)):
        counts = {}
        for arm in ("baseline", "candidate"):
            counts[arm] = sum(not firsts[PRIMARY][f"{case_id}::{arm}::{k['slot']}"] for k in by_case[case_id][arm])
        ok = counts["candidate"] - counts["baseline"] <= GUARD_LIMIT
        guard_ok &= ok
        n = len(by_case[case_id]["baseline"])
        lines.append(f"| {case_id} | {counts['baseline']}/{n} | {counts['candidate']}/{n} | {'yes' if ok else 'NO'} |")
    gates_primary = all(verdicts[(PRIMARY, c)] == "ACCEPT" for c, _ in GATES)
    agree_gates = all(verdicts[(PRIMARY, c)] == verdicts[("haiku", c)] for c, _ in GATES)
    ship = gates_primary and guard_ok and agree_gates
    lines += ["", "## Decision", "",
              f"- Tune gate, primary judge: {verdicts[(PRIMARY, GATES[0][0])]}",
              f"- Holdout gate, primary judge: {verdicts[(PRIMARY, GATES[1][0])]}",
              f"- Guards within limit: {'yes' if guard_ok else 'no'}",
              f"- Secondary judge's gate verdicts agree: {'yes' if agree_gates else 'no'}",
              f"- Pre-registered outcome: {'SHIP candidate-v3' if ship else ('JUDGE-SENSITIVE: human decision' if gates_primary and guard_ok else 'DO NOT SHIP')}"]
    (args.out / "summary.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    b = sub.add_parser("batches")
    b.add_argument("--manifest", type=Path, required=True)
    b.add_argument("--audit", type=Path, required=True)
    b.add_argument("--outputs", type=Path, required=True)
    b.add_argument("--out", type=Path, required=True)
    b.add_argument("--key", type=Path, required=True)
    s = sub.add_parser("score")
    s.add_argument("--key", type=Path, required=True)
    s.add_argument("--judgments", type=Path, required=True)
    s.add_argument("--judge-audit", type=Path, required=True)
    s.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()
    cmd_batches(args) if args.cmd == "batches" else cmd_score(args)


if __name__ == "__main__":
    main()
