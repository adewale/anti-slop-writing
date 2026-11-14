"""Human packet selection preserves unique cases and never invents human scores."""
from __future__ import annotations

import unittest

from _support import load_script

review = load_script("scripts/review_followthrough.py")


class PacketSelection(unittest.TestCase):
    def test_repeated_trials_do_not_fill_distinct_case_quota(self):
        records = [{"model": "m", "slot": str(i), "case_id": "same", "difference": 2, "opus_score": 5} for i in range(20)]
        with self.assertRaisesRegex(ValueError, "distinct-case disagreements"):
            review.select_packet(records, per_model=2, controls=0)

    def test_deterministic_largest_disagreement_and_distinct_agreement_control(self):
        records = [
            {"model": "m", "slot": "a", "case_id": "first", "difference": -3, "opus_score": 1},
            {"model": "m", "slot": "b", "case_id": "first", "difference": 2, "opus_score": 5},
            {"model": "m", "slot": "c", "case_id": "second", "difference": 1, "opus_score": 4},
            {"model": "m", "slot": "d", "case_id": "first", "difference": 0, "opus_score": 2},
            {"model": "m", "slot": "e", "case_id": "control", "difference": 0, "opus_score": 3},
        ]
        selected = review.select_packet(records, per_model=2, controls=1)
        self.assertEqual(selected, review.select_packet(list(reversed(records)), per_model=2, controls=1))
        self.assertEqual({r["slot"] for r in selected}, {"a", "c", "e"})
        self.assertEqual(len({r["case_id"] for r in selected}), 3)
        self.assertEqual(sum(r["selection"] == "agreement-control" for r in selected), 1)

    def test_agreement_cannot_be_fabricated_when_no_control_exists(self):
        with self.assertRaisesRegex(ValueError, "agreement controls"):
            review.select_packet([{"model": "m", "slot": "a", "case_id": "a", "difference": 1, "opus_score": 5}], per_model=1, controls=1)


if __name__ == "__main__":
    unittest.main()
