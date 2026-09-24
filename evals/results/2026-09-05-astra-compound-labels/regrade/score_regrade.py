#!/usr/bin/env python3
"""Unblind the 2026-09-23 regrade and score it with the repo's own tools.

Reads key.json and judgments/<judge>.jsonl in this directory, writes
judgments/<judge>.unblinded.jsonl, scores/<judge>.jsonl (via scripts/run_evals.py grade),
the paired delta files, the gate outputs (via scripts/score_delta.py), and summary.md.
Run from the repository root:
  python3 evals/results/2026-09-05-astra-compound-labels/regrade/score_regrade.py
"""
import json
import subprocess
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
JUDGES = {"sonnet": "claude-sonnet-5", "haiku": "claude-haiku-4-5-20251001"}
PRIMARY = "sonnet"
# Round-1 pairing, as committed in ../delta.jsonl: baseline Sonnet run i <-> candidate run i.
PAIRS = [("baseline-sonnet.md", "cand-sonnet-c1.md"), ("rate-sonnet-r2.md", "cand-sonnet-c2.md"),
         ("rate-sonnet-r3.md", "cand-sonnet-c3.md"), ("rate-sonnet-r4.md", "cand-sonnet-c4.md")]


def uid(k):
    return f"{k['case_id']}::{k['file']}::{k['section']}"


def load_jsonl(p):
    return [json.loads(line) for line in p.read_text().splitlines() if line.strip()]


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    return r.stdout + r.stderr


def main():
    key = {k["blind_id"]: k for k in json.loads((HERE / "key.json").read_text())}
    (HERE / "scores").mkdir(exist_ok=True)
    scores = {}
    for judge in JUDGES:
        recs = load_jsonl(HERE / "judgments" / f"{judge}.jsonl")
        ids = [r["id"] for r in recs]
        assert sorted(ids) == sorted(key), f"{judge}: judged ids do not match the key"
        out = HERE / "judgments" / f"{judge}.unblinded.jsonl"
        with out.open("w") as fh:
            for r in recs:
                k = key[r["id"]]
                fh.write(json.dumps({"id": uid(k), "suite": k["suite"], "split": k["split"],
                                     "assertions": r["assertions"],
                                     "graded_dimensions": r.get("graded_dimensions", [])}) + "\n")
        sp = HERE / "scores" / f"{judge}.jsonl"
        run(["python3", "scripts/run_evals.py", "grade", str(out), "--split", "all", "--out", str(sp)])
        scores[judge] = {s["id"]: s for s in load_jsonl(sp)}
        for r in recs:
            scores[judge][uid(key[r["id"]])]["a1"] = bool(r["assertions"][0]["pass"])

    lines = ["# Regrade summary", "",
             f"Primary judge `{JUDGES[PRIMARY]}`; secondary judge `{JUDGES['haiku']}`. Case score is the",
             "fraction of the case's assertions passed. `a1` is the first assertion: for the",
             "discriminating cases, naming the coinage as coined or undefined; for the guards, keeping the text.", ""]
    rows = defaultdict(list)
    for k in key.values():
        rows[(k["fixture"], k["arm"], k["model_id"], "excluded" if k["status"].startswith("excluded") else
              ("secondary" if k["status"].startswith("secondary") else "valid"))].append(k)
    lines += ["| Case | Arm | Model | Trials | Status | Mean score, primary | a1, primary | Mean score, secondary | a1, secondary |",
              "|---|---|---|---:|---|---:|---:|---:|---:|"]
    for (fx, arm, model, status), ks in sorted(rows.items()):
        def agg(j, ks=ks):
            ss = [scores[j][uid(k)] for k in ks]
            return sum(s["score"] for s in ss) / len(ss), sum(s["a1"] for s in ss)
        pm, pa = agg(PRIMARY)
        sm, sa = agg("haiku")
        lines.append(f"| {fx} | {arm} | {model} | {len(ks)} | {status} | {pm:.2f} | {pa}/{len(ks)} | {sm:.2f} | {sa}/{len(ks)} |")

    agree_a = total_a = agree_a1 = 0
    for k in key.values():
        p, s = scores[PRIMARY][uid(k)], scores["haiku"][uid(k)]
        agree_a1 += p["a1"] == s["a1"]
    for judge_file_p, judge_file_s in [("sonnet", "haiku")]:
        rp = {r["id"]: r for r in load_jsonl(HERE / "judgments" / f"{judge_file_p}.jsonl")}
        rs = {r["id"]: r for r in load_jsonl(HERE / "judgments" / f"{judge_file_s}.jsonl")}
        for bid in key:
            for x, y in zip(rp[bid]["assertions"], rs[bid]["assertions"]):
                total_a += 1
                agree_a += bool(x["pass"]) == bool(y["pass"])
    lines += ["", f"Judge agreement: {agree_a}/{total_a} assertions, {agree_a1}/{len(key)} on the first assertion.", ""]

    by_file = defaultdict(dict)
    for k in key.values():
        by_file[k["file"]][k["fixture"]] = k
    for judge in JUDGES:
        for name, fixtures, holdout_only in [("round1-design", ["P1", "P2", "P3"], False),
                                             ("round1-p1", ["P1"], False),
                                             ("round1-design", ["P1", "P2", "P3"], True)]:
            delta = HERE / f"delta-{judge}-{name}.jsonl"
            with delta.open("w") as fh:
                for i, (b, c) in enumerate(PAIRS, 1):
                    for fx in fixtures:
                        kb, kc = by_file[b][fx], by_file[c][fx]
                        fh.write(json.dumps({"id": f"{fx}-run{i}", "split": kb["split"],
                                             "before": scores[judge][uid(kb)]["score"],
                                             "after": scores[judge][uid(kc)]["score"]}) + "\n")
            cmd = ["python3", "scripts/score_delta.py", str(delta), "--sesoi", "0.05"] + (["--holdout-only"] if holdout_only else [])
            label = f"{judge} {name}{' holdout-only' if holdout_only else ''}"
            lines += [f"### Gate: {label}", "", "```txt", run(cmd).strip(), "```", ""]
    (HERE / "summary.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
