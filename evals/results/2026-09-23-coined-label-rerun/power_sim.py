#!/usr/bin/env python3
"""Power of scripts/score_delta.py's ACCEPT rule for this round's design.

Imports the gate's own functions. ACCEPT = paired-bootstrap 95% CI excludes 0
AND sign-flip p < 0.05. Trials are independent binary outcomes paired by slot.
Run from the repository root:  python3 evals/results/2026-09-23-coined-label-rerun/power_sim.py
Reproduces the table in PREREGISTRATION.md (600 simulated experiments per cell,
1000 bootstrap/permutation iterations, seed 300 + N + 100*before + 10*after, truncated).
"""
import random
import sys

sys.path.insert(0, "scripts")
from score_delta import paired_bootstrap_ci, sign_flip_p_value  # noqa: E402


def gate(deltas, rng, iters):
    _, low, high = paired_bootstrap_ci(deltas, iters, 0.05, rng)
    if low <= 0 <= high:
        return False
    return sign_flip_p_value(deltas, iters, rng) < 0.05


def power(n, p_before, p_after, sims, iters, seed=0):
    rng = random.Random(seed)
    accepted = 0
    for _ in range(sims):
        deltas = [float((rng.random() < p_after) - (rng.random() < p_before)) for _ in range(n)]
        accepted += gate(deltas, rng, iters)
    return accepted / sims


SCENARIOS = [(0.50, 0.75), (0.40, 0.75), (0.50, 0.85), (0.50, 0.95)]

if __name__ == "__main__":
    print("Power of one gate, by true pass rate before -> after (600 experiments per cell)")
    print("N/arm " + "".join(f"{f'{a:.2f}->{b:.2f}':>12}" for a, b in SCENARIOS))
    for n in (12, 40, 60, 80):
        cells = [power(n, a, b, 600, 1000, seed=300 + n + int(100 * a) + int(10 * b)) for a, b in SCENARIOS]
        print(f"{n:>5} " + "".join(f"{c:>12.2f}" for c in cells))
