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
    return [
        {"id": f"{prefix}{i}", "split": split, "before": 0.5, "after": 0.5 + d}
        for i, d in enumerate(deltas)
    ]


class GateVerdicts(unittest.TestCase):
    def setUp(self) -> None:
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.tmp = Path(tmp.name)

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
        result = self.gate(rows([0.25] * 3), "--allow-small")
        self.assertEqual(result.returncode, 1, result.stdout)
        self.assertIn("sign-flip p >=", result.stdout)
        self.assertIn("UNDERPOWERED", result.stdout)

    def test_small_study_requires_explicit_override(self) -> None:
        result = self.gate(rows([0.25] * 5))
        self.assertEqual(result.returncode, 2)
        self.assertIn("UNDERPOWERED", result.stdout)
        self.assertIn("Clusters:      5", result.stdout)

    def test_duplicate_id_cannot_inflate_sample_size(self) -> None:
        records = [{"id": "same", "split": "holdout", "before": 0, "after": 1}] * 8
        result = self.gate(records)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("duplicate id", result.stderr)

    def test_near_miss_distinct_ids_are_valid(self) -> None:
        result = self.gate(rows([0.25] * 8))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Clusters:      8", result.stdout)

    def test_repeated_trials_in_two_clusters_cannot_pass(self) -> None:
        records = rows([0.25] * 40)
        for i, record in enumerate(records):
            record["family"] = str(i % 2)
        result = self.gate(records, "--cluster-field", "family")
        self.assertEqual(result.returncode, 2)
        self.assertIn("clusters=2", result.stdout)

    def test_cluster_means_have_equal_weight(self) -> None:
        records = rows([0.25] * 20 + [-0.25] * 5)
        for i, record in enumerate(records):
            record["family"] = "large" if i < 20 else str(i)
        result = self.gate(records, "--cluster-field", "family")
        self.assertEqual(result.returncode, 1)
        self.assertIn("Mean delta:    -0.1667", result.stdout)

    def test_missing_cluster_label_is_an_error(self) -> None:
        result = self.gate(rows([0.25] * 10), "--cluster-field", "family")
        self.assertIn("missing non-empty cluster field", result.stderr)
        self.assertNotEqual(result.returncode, 0)

    def test_six_fact_pairs_can_pass_as_six_independent_units(self) -> None:
        records = rows([0.25] * 12)
        for i, record in enumerate(records):
            record["pair_id"] = f"pair-{i // 2}"
        result = self.gate(records, "--cluster-field", "pair_id")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("Clusters:      6", result.stdout)

    def test_broader_family_must_keep_each_fact_pair_together(self) -> None:
        records = rows([0.25] * 12)
        for i, record in enumerate(records):
            record.update(pair_id=f"pair-{i // 2}", family=f"family-{i // 2}")
        self.assertEqual(self.gate(records, "--cluster-field", "family").returncode, 0)
        records[0]["family"] = "different-family"
        result = self.gate(records, "--cluster-field", "family")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("spans independent units", result.stderr)

    def test_distinct_pair_ids_allow_legacy_case_level_scoring(self) -> None:
        records = rows([0.25] * 8)
        for record in records:
            record["pair_id"] = record["id"]
        result = self.gate(records)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_non_numeric_or_nonfinite_scores_are_errors(self) -> None:
        for value in ["0.5", True, float("nan"), float("inf")]:
            records = rows([0.25] * 8)
            records[0]["after"] = value
            with self.subTest(value=value):
                result = self.gate(records)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("finite number", result.stderr)

    def test_zero_delta_is_rejected(self) -> None:
        result = self.gate(rows([0.0] * 10))
        self.assertEqual(result.returncode, 1, result.stdout)

    def test_symmetric_noise_is_rejected(self) -> None:
        result = self.gate(rows([0.25, -0.25] * 5))
        self.assertEqual(result.returncode, 1, result.stdout)

    def test_holdout_only_ignores_tune_gains(self) -> None:
        records = rows([0.25] * 10, split="tune", prefix="t") + rows(
            [0.0] * 10, split="holdout", prefix="h"
        )
        self.assertEqual(self.gate(records).returncode, 0)
        held = self.gate(records, "--holdout-only")
        self.assertEqual(held.returncode, 1, held.stdout)
        self.assertRegex(held.stdout, r"Cases:\s+10\n")

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
        mean, low, high = score_delta.paired_bootstrap_ci(
            [0.3] * 8, 500, 0.05, random.Random(0)
        )
        self.assertAlmostEqual(mean, 0.3)
        self.assertAlmostEqual(low, 0.3)
        self.assertAlmostEqual(high, 0.3)

    def test_bootstrap_interval_brackets_the_mean(self) -> None:
        deltas = [0.0, 0.1, 0.2, 0.3, 0.4]
        mean, low, high = score_delta.paired_bootstrap_ci(
            deltas, 2000, 0.05, random.Random(1)
        )
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
