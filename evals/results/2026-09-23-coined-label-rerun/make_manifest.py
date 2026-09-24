#!/usr/bin/env python3
"""Build the trial manifest and apply prompts for the 2026-09-23 re-run.

Deterministic given SEED, so committing this script pre-registers every slot,
its pairing index, its opaque output id, the launch order, and the guard order.
Run from the repository root:

    python3 evals/results/2026-09-23-coined-label-rerun/make_manifest.py \
        --doctrine-map <json {"baseline": dir, "candidate": dir}> --out <manifest.json>

The doctrine map is kept outside the repository until the run finishes, so no
file an apply agent could reach says which opaque directory is which arm.
"""
import argparse
import json
import random
from pathlib import Path

SEED = 20260923
N_DISCRIMINATING = 40
N_GUARD = 8
DISCRIMINATING = [("evals.json", "coined-compound-label"), ("evals.json", "holdout-coined-compound-label")]
GUARDS = [
    ("adversarial.json", "earned-domain-compound"),
    ("adversarial.json", "coined-label-defined-in-place"),
    ("adversarial.json", "holdout-coined-label-defined-in-place"),
    ("adversarial.json", "holdout-earned-domain-compound"),
]
RULES = (
    "You are applying a writing-review skill as part of an evaluation. Follow these rules exactly.\n\n"
    "1. Read the skill file {d}/SKILL.md. If the skill tells you to load one of its reference files, you may read "
    "files under {d}/references/. Do not read, list, or search any other file or directory.\n"
    "2. Carry out the {what} below exactly as the skill prescribes.\n"
    "3. Write your full response with a single Write call to {out}\n"
    "4. Reply with only the word DONE.\n\n"
)


def load_case(suite, case_id):
    cases = json.loads(Path("evals", suite).read_text(encoding="utf-8"))["evals"]
    return next(c for c in cases if c["id"] == case_id)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--doctrine-map", type=Path, required=True)
    ap.add_argument("--out-dir", type=Path, required=True, help="directory the apply agents write into")
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()
    dirs = json.loads(args.doctrine_map.read_text(encoding="utf-8"))
    rng = random.Random(SEED)
    used = set()

    def opaque():
        while True:
            tid = "t" + "".join(rng.choice("abcdefghjkmnpqrstuvwxyz23456789") for _ in range(6))
            if tid not in used:
                used.add(tid)
                return tid

    trials = []
    for suite, case_id in DISCRIMINATING:
        case = load_case(suite, case_id)
        for arm in ("baseline", "candidate"):
            for slot in range(1, N_DISCRIMINATING + 1):
                trials.append({"kind": "discriminating", "suite": suite, "case_id": case_id, "split": case["split"],
                               "arm": arm, "slot": slot, "id": opaque()})
    for arm in ("baseline", "candidate"):
        for slot in range(1, N_GUARD + 1):
            order = GUARDS[:]
            rng.shuffle(order)
            trials.append({"kind": "guard", "arm": arm, "slot": slot, "id": opaque(),
                           "guards": [{"suite": s, "case_id": c, "heading": f"R{i}"} for i, (s, c) in enumerate(order, 1)]})
    rng.shuffle(trials)
    for position, t in enumerate(trials, 1):
        t["launch_position"] = position
        d = str(Path(dirs[t["arm"]]))
        out = str(args.out_dir / f"{t['id']}.md")
        t["output_path"] = out
        if t["kind"] == "discriminating":
            t["prompt"] = RULES.format(d=d, what="user request", out=out) + "User request:\n\n" + load_case(t["suite"], t["case_id"])["prompt"]
        else:
            body = "\n\n".join(f"## {g['heading']}\n\n" + load_case(g["suite"], g["case_id"])["prompt"] for g in t["guards"])
            t["prompt"] = (RULES.format(d=d, what="four user requests", out=out)
                           + "Answer each request on its own, under the same heading it has below (## R1 to ## R4).\n\n" + body)
    args.out.write_text(json.dumps({"seed": SEED, "trials": trials}, indent=2), encoding="utf-8")
    print(f"{len(trials)} trials -> {args.out}")


if __name__ == "__main__":
    main()
