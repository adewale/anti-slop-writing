#!/usr/bin/env python3
"""Saturation / discrimination check for an eval scores file.

A case is *saturated* (at the ceiling) when every run scores it the same — most
often a perfect 1.0 — across the axis you varied (models, judges, conditions).
Saturated cases can no longer separate a good doctrine from a bad one, so a
zero delta on them is only weak "no regression" evidence, not "no effect". This
is the loss-of-discriminative-power problem from the benchmark-saturation
literature (see docs/eval-null-result-literature.md, section 4). The fix is to
retire or harden saturated cases and add discriminating ones.

Input: JSONL from `run_evals.py grade` (records with {id, score, split}). The
`id` is expected to encode the varied axis as a prefix, e.g. "opus__case-id";
everything after the first SEP is the case key, so all runs of one case group
together. Pass --sep to change the separator (default "__").

Output: per-case spread (n, min, max, mean) with a CEILING / spread flag, and an
overall saturation index = fraction of cases at the ceiling.

Example:

    python3 scripts/run_evals.py grade judgments/*.jsonl --include-graded --out scores.jsonl
    python3 scripts/saturation_index.py scores.jsonl
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path
from statistics import pstdev


def load_scores(path: Path, sep: str) -> dict[str, list[float]]:
    groups: dict[str, list[float]] = defaultdict(list)
    with path.open(encoding="utf-8") as fh:
        for line_no, raw in enumerate(fh, start=1):
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            try:
                rec = json.loads(line)
            except json.JSONDecodeError as exc:
                sys.exit(f"FAIL: {path}:{line_no}: invalid JSON: {exc}")
            if "id" not in rec or "score" not in rec:
                sys.exit(f"FAIL: {path}:{line_no}: record needs 'id' and 'score'")
            case = rec["id"].split(sep, 1)[1] if sep in rec["id"] else rec["id"]
            groups[case].append(float(rec["score"]))
    return groups


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("scores", type=Path, help="JSONL of {id, score, split} from run_evals.py grade.")
    parser.add_argument("--sep", default="__", help="Separator splitting the varied-axis prefix from the case key (default '__').")
    parser.add_argument("--ceiling", type=float, default=1.0, help="Score treated as the ceiling (default 1.0).")
    parser.add_argument("--eps", type=float, default=1e-9, help="Spread below this counts as no spread.")
    args = parser.parse_args()

    groups = load_scores(args.scores, args.sep)
    if not groups:
        sys.exit("FAIL: no scores to check")

    print(f"{'case':40} {'n':>2} {'min':>5} {'max':>5} {'mean':>5}  flag")
    ceiling_cases = 0
    for case in sorted(groups):
        vals = groups[case]
        lo, hi = min(vals), max(vals)
        mean = sum(vals) / len(vals)
        at_ceiling = hi - lo < args.eps and abs(hi - args.ceiling) < args.eps
        flat = hi - lo < args.eps
        flag = "CEILING" if at_ceiling else ("flat" if flat else "spread")
        if at_ceiling:
            ceiling_cases += 1
        print(f"{case:40} {len(vals):>2} {lo:5.2f} {hi:5.2f} {mean:5.2f}  {flag}")

    n = len(groups)
    index = ceiling_cases / n
    print()
    print(f"Cases:             {n}")
    print(f"At ceiling:        {ceiling_cases}")
    print(f"Saturation index:  {index:.3f}  (fraction of cases with no spread at the ceiling)")
    print("Note: a zero delta on CEILING cases is only no-regression evidence; harden or retire them.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
