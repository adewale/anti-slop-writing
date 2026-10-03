"""scripts/score_delta.py is the accept/reject gate for doctrine edits.

The runbook says "require ACCEPT before promoting the change", so the exit
code is the contract: 0 only for an improvement that clears the noise floor.
"""
from __future__ import annotations

import random
import tempfile
import unittest
from pathlib import Path

from _support import load_script, run_script, write_jsonl

score_delta = load_script("scripts/score_delta.py")


def rows(deltas: list[float], split: str = "holdout", prefix: str = "c") -> list[dict]:
    return [{"id": f"{prefix}{i}", "split": split, "before": 0.5, "after": 0.5 + d} for i, d in enumerate(deltas)]


class GateVerdicts(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = Path(tempfile.mkdtemp())

    def gate(self, records: list[dict], *flags: str):
        path = write_jsonl(self.tmp / "delta.jsonl", records)
        return run_script("scripts/score_delta.py", path, *flags)

    def test_consistent_improvement_is_accepted(self) -> None:
        result = self.gate(rows([0.25] * 10))
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("ACCEPT", result.stdout)

    def test_consistent_regression_is_rejected(self) -> None:
        # Mirror image of the improvement above: same magnitude, opposite sign.
        result = self.gate(rows([-0.25] * 10))
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("REJECT", result.stdout)
        self.assertNotIn("ACCEPT", result.stdout)

    def test_three_cases_cannot_clear_the_permutation_test(self) -> None:
        # The bootstrap CI of three equal deltas is a point above zero, but the
        # exact sign-flip p is 2 / 2**3 = 0.25, so the gate must still reject.
        result = self.gate(rows([0.25] * 3))
        self.assertEqual(result.returncode, 1, result.stdout)
        self.assertIn("sign-flip p >=", result.stdout)

    def test_zero_delta_is_rejected(self) -> None:
        result = self.gate(rows([0.0] * 10))
        self.assertEqual(result.returncode, 1, result.stdout)

    def test_symmetric_noise_is_rejected(self) -> None:
        result = self.gate(rows([0.25, -0.25] * 5))
        self.assertEqual(result.returncode, 1, result.stdout)

    def test_holdout_only_ignores_tune_gains(self) -> None:
        records = rows([0.25] * 10, split="tune", prefix="t") + rows([0.0] * 10, split="holdout", prefix="h")
        self.assertEqual(self.gate(records).returncode, 0)
        held = self.gate(records, "--holdout-only")
        self.assertEqual(held.returncode, 1, held.stdout)
        self.assertIn("Cases:         10", held.stdout)

    def test_rejects_unknown_split(self) -> None:
        result = self.gate([{"id": "x", "split": "unknown", "before": 0, "after": 1}])
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("split must be tune or holdout", result.stderr)

    def test_no_holdout_records_is_an_error_not_a_pass(self) -> None:
        result = self.gate(rows([0.25] * 10, split="tune"), "--holdout-only")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("no records", result.stderr)

    def test_sesoi_reports_equivalence_only_inside_bounds(self) -> None:
        tiny = self.gate(rows([0.01, -0.01] * 10), "--sesoi", "0.05")
        self.assertIn("Equivalence:   EQUIVALENT", tiny.stdout)
        large = self.gate(rows([0.2, -0.1] * 10), "--sesoi", "0.05")
        self.assertIn("Equivalence:   NOT SHOWN", large.stdout)


class Statistics(unittest.TestCase):
    def test_bootstrap_of_constant_deltas_is_a_point(self) -> None:
        mean, low, high = score_delta.paired_bootstrap_ci([0.3] * 8, 500, 0.05, random.Random(0))
        self.assertAlmostEqual(mean, 0.3)
        self.assertAlmostEqual(low, 0.3)
        self.assertAlmostEqual(high, 0.3)

    def test_bootstrap_interval_brackets_the_mean(self) -> None:
        deltas = [0.0, 0.1, 0.2, 0.3, 0.4]
        mean, low, high = score_delta.paired_bootstrap_ci(deltas, 2000, 0.05, random.Random(1))
        self.assertAlmostEqual(mean, 0.2)
        self.assertLess(low, mean)
        self.assertGreater(high, mean)
        self.assertGreaterEqual(low, 0.0)
        self.assertLessEqual(high, 0.4)

    def test_sign_flip_p_value_matches_exact_tail(self) -> None:
        # Ten same-signed equal deltas: only the two all-same-sign flips are as
        # extreme, so the exact two-sided p is 2 / 2**10 ~= 0.00195.
        p = score_delta.sign_flip_p_value([0.1] * 10, 20000, random.Random(2))
        self.assertLess(p, 0.006)
        # One nonzero delta among zeros: every flip is as extreme, p ~= 1.
        p_one = score_delta.sign_flip_p_value([0.1] + [0.0] * 9, 2000, random.Random(3))
        self.assertGreater(p_one, 0.99)


if __name__ == "__main__":
    unittest.main()
