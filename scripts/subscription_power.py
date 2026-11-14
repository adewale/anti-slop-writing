#!/usr/bin/env python3
"""Outcome-free ordinal power scenarios for the subscription baseline.

Run with: uv run --no-project --with numpy==2.3.5 python scripts/subscription_power.py DEST
Uses the final family-weighted, eight-contrast conjunctive gate, 10,000 bootstrap
resamples and exact family sign flips. Scenario assumptions are not measured data.
"""

from __future__ import annotations

import json
import sys
from itertools import product
from pathlib import Path

import numpy as np


def main():
    dest = Path(sys.argv[1])
    core = [
        c
        for c in json.loads((dest / "cases.json").read_text())
        if c["group"] == "review-rewrite" and c["split"] == "holdout"
    ]
    families = sorted({c["family"] for c in core})
    labels = np.array([families.index(c["family"]) for c in core])
    n = len(families)
    signs = np.array(list(product((-1, 1), repeat=n)))
    rng = np.random.default_rng(261114)
    simulations = 500
    results = []
    scenarios = [
        ("null", 0.75, 0.0, 0.08),
        ("central", 0.75, 0.10, 0.08),
        ("small-effect", 0.75, 0.05, 0.08),
        ("near-ceiling", 0.90, 0.05, 0.08),
        ("heterogeneous", 0.75, 0.10, 0.18),
        ("large-effect", 0.50, 0.15, 0.08),
    ]
    for trials in (3, 5, 10):
        for name, baseline, effect, heterogeneity in scenarios:
            passes = 0
            for _ in range(simulations):
                # Eight correlated contrasts: two outcomes x two models x two judges.
                # Common family/case and generation effects create dependence; independent
                # contrast noise prevents the conjunction from becoming one test copied 8x.
                family_base = rng.normal(0, 0.08, n)
                family_effect = rng.normal(effect, heterogeneity, n)
                case_base = np.clip(
                    baseline + family_base[labels] + rng.normal(0, 0.05, len(core)),
                    0.01,
                    0.99,
                )
                case_effect = family_effect[labels] + rng.normal(0, 0.04, len(core))
                shared_before = rng.normal(0, 0.10, (len(core), trials))
                shared_after = rng.normal(0, 0.10, (len(core), trials))
                before = np.clip(
                    case_base[None, :, None]
                    + shared_before[None, :, :]
                    + rng.normal(0, 0.14, (8, len(core), trials)),
                    0,
                    1,
                )
                after = np.clip(
                    (case_base + case_effect)[None, :, None]
                    + shared_after[None, :, :]
                    + rng.normal(0, 0.14, (8, len(core), trials)),
                    0,
                    1,
                )
                # Actual judges return integer 1..5, normalized to 0,.25,.5,.75,1.
                delta = (np.round(after * 4) - np.round(before * 4)).mean(axis=2) / 4
                family_delta = np.stack(
                    [delta[:, labels == i].mean(axis=1) for i in range(n)], axis=1
                )
                observed = np.abs(family_delta.sum(axis=1))
                flipped = np.abs(family_delta @ signs.T)
                p = (
                    (flipped > observed[:, None])
                    | np.isclose(flipped, observed[:, None], rtol=1e-12, atol=1e-15)
                ).mean(axis=1)
                means = family_delta.mean(axis=1)
                # Early rejection is algebraically identical to the final conjunctive gate.
                if np.any(p >= 0.05) or np.any(means < 0.05):
                    continue
                indices = rng.integers(0, n, (10000, n))
                bootstrap = family_delta[:, indices].mean(axis=2)
                low = np.partition(bootstrap, 250, axis=1)[:, 250]
                if np.all(low > 0):
                    passes += 1
            estimate = passes / simulations
            result = {
                "scenario": name,
                "trials": trials,
                "baseline": baseline,
                "latent_effect": effect,
                "family_effect_sd": heterogeneity,
                "joint_success": estimate,
                "mc_se": (estimate * (1 - estimate) / simulations) ** 0.5,
            }
            results.append(result)
            print(json.dumps(result), flush=True)
    output = {
        "seed": 261114,
        "simulations_per_scenario": simulations,
        "families": families,
        "holdout_cases": len(core),
        "bootstrap_iters": 10000,
        "alpha": 0.05,
        "sesoi": 0.05,
        "target_joint_power": 0.80,
        "results": results,
        "decision": "Estimation/coverage study at 3 trials; no robust power guarantee or doctrine promotion.",
    }
    (dest / "power-scenarios.json").write_text(json.dumps(output, indent=2) + "\n")


if __name__ == "__main__":
    main()
