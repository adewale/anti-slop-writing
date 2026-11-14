#!/usr/bin/env python3
"""Outcome-free simulation of the registered mixed-trial candidate screening gate.

uv run --no-project --with numpy==2.3.5 python scripts/candidate_power.py DEST
Assumptions are scenarios, not pilot estimates. Target panels also have an exact
power bound: a one-family two-sided sign-flip test can never reject at alpha .05.
"""
from __future__ import annotations

import json
import sys
from itertools import product
from pathlib import Path

import numpy as np


def main() -> None:
    dest = Path(sys.argv[1])
    cases = json.loads((dest / "cases.json").read_text())
    slots = json.loads((dest / "manifest.json").read_text())["slots"]
    rng = np.random.default_rng(261115)
    simulations = 500
    results = []
    for panel in ("standing", "compound", "teaser"):
        selected = [c for c in cases if c["group"] == panel and c["split"] == "holdout"]
        families = sorted({c["family"] for c in selected})
        n = len(families)
        labels = np.array([families.index(c["family"]) for c in selected])
        trials = np.array([sum(s["case_id"] == c["id"] and s["arm"] == "current" and s["model"] == "sonnet" for s in slots) for c in selected])
        signs = np.array(list(product((-1, 1), repeat=n)))
        for effect in (0.0, 0.05, 0.10, 0.15):
            passes = 0
            for _ in range(simulations):
                family_base = rng.normal(0.75, 0.08, n)
                family_effect = rng.normal(effect, 0.08, n)
                trial_counts = int(max(trials))
                before = np.clip(family_base[labels][None, :, None] + rng.normal(0, 0.18, (8, len(selected), trial_counts)), 0, 1)
                after = np.clip((family_base + family_effect)[labels][None, :, None] + rng.normal(0, 0.18, (8, len(selected), trial_counts)), 0, 1)
                delta = np.stack([(np.round(after[:, i, :t] * 4) - np.round(before[:, i, :t] * 4)).mean(axis=1) / 4 for i, t in enumerate(trials)], axis=1)
                family_delta = np.stack([delta[:, labels == i].mean(axis=1) for i in range(n)], axis=1)
                observed = np.abs(family_delta.sum(axis=1))
                flipped = np.abs(family_delta @ signs.T)
                p = ((flipped > observed[:, None]) | np.isclose(flipped, observed[:, None], rtol=1e-12, atol=1e-15)).mean(axis=1)
                if n < 6 or np.any(p >= 0.05) or np.any(family_delta.mean(axis=1) < 0.05):
                    continue
                indices = rng.integers(0, n, (10000, n))
                boot = family_delta[:, indices].mean(axis=2)
                if np.all(np.quantile(boot, 0.025, axis=1) > 0):
                    passes += 1
            result = {"panel": panel, "holdout_cases": len(selected), "families": families,
                      "trials_per_case": trials.tolist(), "latent_effect": effect,
                      "joint_success": passes / simulations,
                      "exact_maximum_power": 0 if n < 6 else None}
            results.append(result)
            print(json.dumps(result), flush=True)
    (dest / "power-scenarios.json").write_text(json.dumps({
        "seed": 261115, "simulations": simulations, "bootstrap_iterations": 10000,
        "alpha": 0.05, "sesoi": 0.05, "target_joint_power": 0.80, "results": results,
        "decision": "Screening/coverage only. Target panels cannot pass the independent-family gate at any repeat count; no promotion authorized.",
        "limits": "Illustrative ordinal scenarios, independent contrast noise and shared family effects; not empirical pilot estimates or a proof of harm/equivalence. Fact twins and repeats share their family.",
    }, indent=2) + "\n")


if __name__ == "__main__":
    main()
