#!/usr/bin/env python3
"""Rebuild the blinded judge inputs for the 2026-09-23 regrade of the 2026-09-05 round.

Splits every critique in ../outputs/ into one item per case, gives each an opaque id
(seed 20260923), shuffles across arms and models, and writes:
  batch-1.md, batch-2.md    the two batches the Haiku judge graded
  small-1.md ... small-8.md the same items in eight batches for the Sonnet judge
  key.json                  opaque id -> source file, case, arm, model, status
Run from the repository root with an output directory:
  python3 evals/results/2026-09-05-astra-compound-labels/regrade/build_batches.py <out-dir>
"""
import json
import random
import re
import sys
from pathlib import Path

ROUND = Path("evals/results/2026-09-05-astra-compound-labels")
P4TEXT = ("Rollout gating relies on soft-quorum drains, so tenant-affinity pools never see a partial config. "
          "Because the drain completes before the flip, a bad config is caught in staging rather than in production.")
P4 = {
    "id": "p4-coined-compound-label (probe only, not in a suite)", "suite": "probe", "split": "probe",
    "prompt": "Review this paragraph using the Critique output format:\n\n" + P4TEXT,
    "assertions": [
        "Identifies at least one of 'soft-quorum drains' or 'tenant-affinity pools' as a coined or undefined term rather than an established one.",
        "Does not treat the coined label as the mechanism that earns the claim that the pools 'never see a partial config'.",
        "Asks the author to define the term or cuts the unsupported claim, rather than inventing a definition for it.",
    ],
    "graded_dimensions": [
        {"name": "label-resolution", "scale": "1-5", "rubric": "5 = names the coinage and says the referent is unavailable to the reader; 3 = notes vagueness without locating it in the compound; 1 = accepts the label as mechanism."},
        {"name": "non-invention", "scale": "1-5", "rubric": "5 = supplies no invented definition of 'soft-quorum' or 'tenant-affinity'; 1 = guesses a definition to make the rewrite sharper."},
    ],
}
MULTI = ["baseline-opus.md", "baseline-sonnet.md", "baseline-haiku.md", "rate-sonnet-r2.md", "rate-sonnet-r3.md",
         "rate-sonnet-r4.md", "cand-sonnet-c1.md", "cand-sonnet-c2.md", "cand-sonnet-c3.md", "cand-sonnet-c4.md"]


def load_cases():
    ev = {c["id"]: c for c in json.loads(Path("evals/evals.json").read_text())["evals"]}
    ad = {c["id"]: c for c in json.loads(Path("evals/adversarial.json").read_text())["evals"]}
    return {
        "P1": dict(ev["coined-compound-label"], suite="evals.json"),
        "P2": dict(ad["earned-domain-compound"], suite="adversarial.json"),
        # Split recorded as it was when the round ran; the case has since moved to tune.
        "P3": dict(ad["coined-label-defined-in-place"], suite="adversarial.json", split="holdout"),
        "P4": P4,
    }


def split_sections(path, pattern):
    parts = re.split(pattern, path.read_text(), flags=re.M)
    return [(parts[i], parts[i + 1].strip()) for i in range(1, len(parts), 2)]


def render(item, case):
    a = "\n".join(f"{i}. {x}" for i, x in enumerate(case["assertions"], 1))
    g = "\n".join(f"- {d['name']} ({d['scale']}): {d['rubric']}" for d in case.get("graded_dimensions", [])) or "- none"
    return (f"=== ITEM {item['blind_id']} ===\nREQUEST THE CRITIQUE RESPONDS TO:\n{case['prompt']}\n\n"
            f"ASSERTIONS (judge each independently):\n{a}\n\nGRADED DIMENSIONS (score 1-5; empty list if none):\n{g}\n\n"
            f"CRITIQUE UNDER REVIEW:\n{item['text']}\n=== END ITEM {item['blind_id']} ===\n")


def main():
    out = Path(sys.argv[1])
    out.mkdir(parents=True, exist_ok=True)
    cases = load_cases()
    meta = {a["output"].split("/")[-1]: a for a in json.loads((ROUND / "run-metadata.json").read_text())["agents"]}

    def arm_of(f):
        d = meta[f]["doctrine"]
        return "baseline" if d.startswith("baseline") else ("candidate-v2" if "v2" in d else "candidate")

    items = []
    for f in MULTI:
        for sec, body in split_sections(ROUND / "outputs" / f, r"^#{2}\s*(P[123])\s*$"):
            items.append(dict(file=f, section=sec, fixture=sec, text=body))
    for f in ["r2-baseline-b5678.md", "r2-cand-c5678.md"]:
        for sec, body in split_sections(ROUND / "outputs" / f, r"^#{2}\s*Trial\s*(\d)\s*$"):
            items.append(dict(file=f, section="Trial " + sec, fixture="P1", text=body))
    for f in ["p4-baseline.md", "p4-candidate-v2.md"]:
        for sec, body in split_sections(ROUND / "outputs" / f, r"^#{2}\s*Trial\s*(\d)\s*$"):
            items.append(dict(file=f, section="Trial " + sec, fixture="P4", text=body))
    rng = random.Random(20260923)
    used = set()
    for it in items:
        while True:
            b = "g" + "".join(rng.choice("abcdefghjkmnpqrstuvwxyz23456789") for _ in range(5))
            if b not in used:
                used.add(b)
                break
        c = cases[it["fixture"]]
        it.update(blind_id=b, case_id=c["id"], suite=c["suite"], split=c["split"], arm=arm_of(it["file"]),
                  model_id=meta[it["file"]]["model_id"], status=meta[it["file"]]["status"])
    rng.shuffle(items)
    half = (len(items) + 1) // 2
    for n, chunk in enumerate([items[:half], items[half:]], 1):
        (out / f"batch-{n}.md").write_text("\n".join(render(it, cases[it["fixture"]]) for it in chunk))
    size = -(-len(items) // 8)
    for n in range(8):
        chunk = items[n * size:(n + 1) * size]
        (out / f"small-{n + 1}.md").write_text("\n".join(render(it, cases[it["fixture"]]) for it in chunk))
    fields = ("blind_id", "file", "section", "fixture", "case_id", "suite", "split", "arm", "model_id", "status")
    (out / "key.json").write_text(json.dumps([{k: it[k] for k in fields} for it in items], indent=2))
    print(f"{len(items)} items -> {out}")


if __name__ == "__main__":
    main()
