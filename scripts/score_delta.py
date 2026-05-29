#!/usr/bin/env python3
"""Statistical gate for hillclimbing accept/reject decisions.

Compares per-case scores from two runs (before vs after a doctrine change) and
reports a 95% confidence interval on the mean per-case score delta. The
interval is computed by paired bootstrap and by a sign-flip permutation test,
because the eval suites here are small (N < ~30) and CLT-based standard errors
are dramatically too tight at that size — see Bowyer, Aitchison, Ivanova,
"Don't Use the CLT in LLM Evals" (ICML 2025, arXiv 2503.01747).

Rule of the runbook: do not accept an edit when the 95% CI on the delta
overlaps zero. Use --holdout-only to score only the held-out split.

Input format: JSONL, one record per case, with fields {id, split, before, after}.
`before` and `after` may be 0/1 (binary assertion pass-rate) or any real number
(graded dimension score).

Example:

    python3 scripts/score_delta.py results/round-2.jsonl --holdout-only

Reads a small file; no dependencies beyond the Python stdlib.
"""
from __future__ import annotations

import argparse
import json
import random
import sys
from pathlib import Path


def load_records(path: Path, holdout_only: bool) -> list[dict]:
    records: list[dict] = []
    with path.open(encoding="utf-8") as f:
        for line_no, raw in enumerate(f, start=1):
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            try:
                record = json.loads(line)
            except json.JSONDecodeError as exc:
                sys.exit(f"FAIL: {path}:{line_no}: invalid JSON: {exc}")
            for field in ("id", "split", "before", "after"):
                if field not in record:
                    sys.exit(f"FAIL: {path}:{line_no}: missing field {field}")
            if record["split"] not in ("tune", "holdout"):
                sys.exit(f"FAIL: {path}:{line_no}: split must be tune or holdout")
            if holdout_only and record["split"] != "holdout":
                continue
            records.append(record)
    return records


def paired_bootstrap_ci(deltas: list[float], iters: int, alpha: float, rng: random.Random) -> tuple[float, float, float]:
    if not deltas:
        return 0.0, 0.0, 0.0
    n = len(deltas)
    mean = sum(deltas) / n
    samples = []
    for _ in range(iters):
        resample = [deltas[rng.randrange(n)] for _ in range(n)]
        samples.append(sum(resample) / n)
    samples.sort()
    low = samples[int(iters * (alpha / 2))]
    high = samples[int(iters * (1 - alpha / 2)) - 1]
    return mean, low, high


def sign_flip_p_value(deltas: list[float], iters: int, rng: random.Random) -> float:
    if not deltas:
        return 1.0
    observed = abs(sum(deltas))
    if observed == 0:
        return 1.0
    extreme = 0
    for _ in range(iters):
        flipped = sum(d if rng.random() < 0.5 else -d for d in deltas)
        if abs(flipped) >= observed:
            extreme += 1
    return (extreme + 1) / (iters + 1)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("results", type=Path, help="JSONL with one record per case: {id, split, before, after}")
    parser.add_argument("--holdout-only", action="store_true", help="Score only the held-out split.")
    parser.add_argument("--iters", type=int, default=10_000, help="Bootstrap and permutation iterations (default 10000).")
    parser.add_argument("--alpha", type=float, default=0.05, help="Two-sided alpha for CI (default 0.05).")
    parser.add_argument("--seed", type=int, default=0, help="RNG seed for reproducibility (default 0).")
    args = parser.parse_args()

    records = load_records(args.results, args.holdout_only)
    if not records:
        sys.exit("FAIL: no records to score")

    rng = random.Random(args.seed)
    deltas = [float(r["after"]) - float(r["before"]) for r in records]

    mean, low, high = paired_bootstrap_ci(deltas, args.iters, args.alpha, rng)
    p_value = sign_flip_p_value(deltas, args.iters, rng)

    split_label = "holdout-only" if args.holdout_only else "all-cases"
    print(f"Split:         {split_label}")
    print(f"Cases:         {len(records)}")
    print(f"Mean delta:    {mean:+.4f}")
    print(f"95% CI:        [{low:+.4f}, {high:+.4f}]")
    print(f"Sign-flip p:   {p_value:.4f}")

    ci_overlaps_zero = low <= 0 <= high
    if ci_overlaps_zero:
        print("Verdict:       REJECT (CI overlaps zero; delta is within noise).")
        return 1
    if p_value >= args.alpha:
        print(f"Verdict:       REJECT (sign-flip p >= {args.alpha}).")
        return 1
    direction = "improvement" if mean > 0 else "regression"
    print(f"Verdict:       ACCEPT ({direction} clears the noise floor).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
