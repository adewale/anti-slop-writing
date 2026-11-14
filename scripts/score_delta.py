#!/usr/bin/env python3
"""Statistical gate for hillclimbing accept/reject decisions.

Compares per-case scores from two runs (before vs after a doctrine change) and
reports a 95% confidence interval on the mean per-case score delta. The
interval is computed by paired bootstrap and by a sign-flip permutation test,
because the eval suites here are small (N < ~30) and CLT-based standard errors
are dramatically too tight at that size — see Bowyer, Aitchison, Ivanova,
"Don't Use the CLT in LLM Evals" (ICML 2025, arXiv 2503.01747).

Rule of the runbook: do not accept an edit when the 95% CI on the delta
overlaps zero. Use --holdout-only to score only the held-out split. A delta
that clears the noise floor in the negative direction is a regression and is
REJECTED too: only a significant improvement exits 0. Other REJECTs exit 1;
an UNDERPOWERED REJECT (fewer than six independent units, no --allow-small)
exits 2. Treat any nonzero exit as REJECT.

A REJECT here means "no improvement was detected", which is NOT the same as
"the edit does nothing": a non-significant superiority test can also be an
underpowered one (absence of evidence is not evidence of absence). To make the
positive "it does nothing" claim, pass --sesoi S to run a two-one-sided-tests
(TOST) equivalence check against a smallest-effect-of-interest S: equivalence
is declared when the (1 - 2*alpha) CI on the delta lies entirely within
(-S, +S). See docs/eval-null-result-literature.md for why a null delta needs
this and not just a failed superiority test.

Input format: JSONL, one record per case, with fields {id, split, before, after}.
`before` and `after` may be 0/1 (binary assertion pass-rate) or any real number
(graded dimension score).

Example:

    python3 scripts/score_delta.py results/round-2.jsonl --holdout-only
    python3 scripts/score_delta.py results/round-2.jsonl --sesoi 0.05

Reads a small file; no dependencies beyond the Python stdlib.
"""

from __future__ import annotations

import argparse
import json
import math
import random
import sys
from collections import defaultdict
from itertools import product
from pathlib import Path


def load_records(path: Path, holdout_only: bool) -> list[dict]:
    records: list[dict] = []
    seen: set[str] = set()
    with path.open(encoding="utf-8") as f:
        for line_no, raw in enumerate(f, start=1):
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            try:
                record = json.loads(line)
            except json.JSONDecodeError as exc:
                sys.exit(f"FAIL: {path}:{line_no}: invalid JSON: {exc}")
            if not isinstance(record, dict):
                sys.exit(f"FAIL: {path}:{line_no}: record must be an object")
            for field in ("id", "split", "before", "after"):
                if field not in record:
                    sys.exit(f"FAIL: {path}:{line_no}: missing field {field}")
            if record["split"] not in ("tune", "holdout"):
                sys.exit(f"FAIL: {path}:{line_no}: split must be tune or holdout")
            cid = record["id"]
            if not isinstance(cid, str) or not cid.strip():
                sys.exit(f"FAIL: {path}:{line_no}: id must be a non-empty string")
            if cid in seen:
                sys.exit(f"FAIL: {path}:{line_no}: duplicate id: {cid}")
            seen.add(cid)
            for field in ("before", "after"):
                value = record[field]
                if (
                    isinstance(value, bool)
                    or not isinstance(value, (int, float))
                    or not math.isfinite(value)
                ):
                    sys.exit(f"FAIL: {path}:{line_no}: {field} must be a finite number")
            if holdout_only and record["split"] != "holdout":
                continue
            records.append(record)
    return records


def paired_bootstrap_ci(
    deltas: list[float], iters: int, alpha: float, rng: random.Random
) -> tuple[float, float, float]:
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
    # Enumerate small studies so a random draw cannot move the six-unit floor.
    if len(deltas) <= 16:
        extreme = sum(
            abs(total := sum(d * s for d, s in zip(deltas, signs))) >= observed
            or math.isclose(abs(total), observed, rel_tol=1e-12, abs_tol=1e-15)
            for signs in product((-1, 1), repeat=len(deltas))
        )
        return extreme / (2 ** len(deltas))
    extreme = 0
    for _ in range(iters):
        flipped = sum(d if rng.random() < 0.5 else -d for d in deltas)
        if abs(flipped) >= observed:
            extreme += 1
    return (extreme + 1) / (iters + 1)


def independent_deltas(records: list[dict], cluster_field: str | None) -> list[float]:
    """Equal-weight cluster means; trials and near-copy cases are not extra N."""
    pair_units: dict[str, str] = {}
    for record in records:
        if "pair_id" not in record:
            continue
        pair_id = record["pair_id"]
        if not isinstance(pair_id, str) or not pair_id.strip():
            sys.exit(f"FAIL: {record['id']}: pair_id must be a non-empty string")
        unit = record.get(cluster_field) if cluster_field else record["id"]
        if pair_id in pair_units and pair_units[pair_id] != unit:
            sys.exit(
                f"FAIL: pair_id {pair_id} spans independent units; aggregate first or "
                "use --cluster-field pair_id (or a broader family)"
            )
        pair_units[pair_id] = unit
    if cluster_field is None:
        return [r["after"] - r["before"] for r in records]
    groups: dict[str, list[float]] = defaultdict(list)
    for record in records:
        label = record.get(cluster_field)
        if not isinstance(label, str) or not label.strip():
            sys.exit(
                f"FAIL: {record['id']}: missing non-empty cluster field {cluster_field}"
            )
        groups[label].append(record["after"] - record["before"])
    return [sum(values) / len(values) for values in groups.values()]


def main() -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "results",
        type=Path,
        help="JSONL with one record per case: {id, split, before, after}",
    )
    parser.add_argument(
        "--holdout-only", action="store_true", help="Score only the held-out split."
    )
    parser.add_argument(
        "--iters",
        type=int,
        default=10_000,
        help="Bootstrap and permutation iterations (default 10000).",
    )
    parser.add_argument(
        "--alpha",
        type=float,
        default=0.05,
        help="Two-sided alpha for CI (default 0.05).",
    )
    parser.add_argument(
        "--seed", type=int, default=0, help="RNG seed for reproducibility (default 0)."
    )
    parser.add_argument(
        "--allow-small",
        action="store_true",
        help="Report an UNDERPOWERED study with fewer than six independent units.",
    )
    parser.add_argument(
        "--cluster-field",
        help="Resample equal-weight means of this field (e.g. family), rather than rows.",
    )
    parser.add_argument(
        "--sesoi",
        type=float,
        default=None,
        help="Smallest effect size of interest. When set, also run a TOST equivalence check: equivalence is declared when the (1 - 2*alpha) CI on the delta lies within (-SESOI, +SESOI).",
    )
    args = parser.parse_args()
    if args.iters < 1 or not 0 < args.alpha < 0.5:
        parser.error("--iters must be positive and --alpha must be between 0 and 0.5")
    if args.sesoi is not None and (not math.isfinite(args.sesoi) or args.sesoi <= 0):
        sys.exit("FAIL: --sesoi must be positive")

    records = load_records(args.results, args.holdout_only)
    if not records:
        sys.exit("FAIL: no records to score")

    rng = random.Random(args.seed)
    deltas = independent_deltas(records, args.cluster_field)
    n_clusters = len(deltas)
    print(f"Split:         {'holdout-only' if args.holdout_only else 'all-cases'}")
    print(f"Cases:         {len(records)}")
    print(f"Clusters:      {n_clusters} ({args.cluster_field or 'one per case'})")
    if n_clusters < 6:
        print("Power:         UNDERPOWERED (fewer than 6 independent units).")
        if not args.allow_small:
            print(
                f"Verdict:       REJECT (UNDERPOWERED; N={len(records)}, clusters={n_clusters}; use --allow-small to inspect)."
            )
            return 2

    mean, low, high = paired_bootstrap_ci(deltas, args.iters, args.alpha, rng)
    p_value = sign_flip_p_value(deltas, args.iters, rng)

    print(f"Mean delta:    {mean:+.4f}")
    print(f"{(1 - args.alpha) * 100:g}% CI:        [{low:+.4f}, {high:+.4f}]")
    print(f"Sign-flip p:   {p_value:.4f}")

    if args.sesoi is not None:
        # TOST: a two-one-sided-tests equivalence decision at level alpha is the
        # (1 - 2*alpha) CI lying inside the equivalence bounds. Reuse the paired
        # bootstrap at the widened alpha so the interval matches the convention.
        _, eq_low, eq_high = paired_bootstrap_ci(
            deltas, args.iters, 2 * args.alpha, rng
        )
        within = -args.sesoi < eq_low and eq_high < args.sesoi
        conf = round((1 - 2 * args.alpha) * 100)
        print(f"SESOI:         +/-{args.sesoi:.4f}")
        print(f"TOST {conf}% CI:   [{eq_low:+.4f}, {eq_high:+.4f}]")
        if within:
            print(
                f"Equivalence:   EQUIVALENT (CI within +/-{args.sesoi:.4f}; no effect of practical size)."
            )
        else:
            print(
                f"Equivalence:   NOT SHOWN (CI exceeds +/-{args.sesoi:.4f}; cannot rule out an effect this large)."
            )

    ci_overlaps_zero = low <= 0 <= high
    if ci_overlaps_zero:
        print("Verdict:       REJECT (CI overlaps zero; delta is within noise).")
        return 1
    if p_value >= args.alpha:
        print(f"Verdict:       REJECT (sign-flip p >= {args.alpha}).")
        return 1
    if mean < 0:
        print("Verdict:       REJECT (regression clears the noise floor).")
        return 1
    print("Verdict:       ACCEPT (improvement clears the noise floor).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
