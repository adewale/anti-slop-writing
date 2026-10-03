"""Known-good, known-bad and near-miss samples for evals/oracles/fixture_oracle.py.

The fixture is evals/fixtures/round3-mechanism-copy/input.md: the draft is
launch copy, and the facts are an HMAC check on webhook retries plus a retry
receipt ID. Samples below are written from that fixture, not from the regexes.
"""
from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from _support import run_script

CASE = "round3-fixture-mechanism-copy"

GOOD = (
    "The tool rejects a webhook retry unless its HMAC signature matches, "
    "and logs the retry receipt ID with the original delivery timestamp."
)


class FixtureOracle(unittest.TestCase):
    def grade(self, text: str | None, case: str = CASE):
        out_dir = Path(tempfile.mkdtemp())
        if text is not None:
            (out_dir / "output.md").write_text(text, encoding="utf-8")
        return run_script("evals/oracles/fixture_oracle.py", out_dir, case)

    def test_grounded_rewrite_passes(self) -> None:
        result = self.grade(GOOD)
        self.assertEqual(result.returncode, 0, result.stdout)
        summary = json.loads(result.stdout.splitlines()[0])
        self.assertEqual(summary["score"], summary["max_score"])

    def test_mechanism_terms_match_case_insensitively(self) -> None:
        self.assertEqual(self.grade(GOOD.replace("HMAC", "hmac").replace("retry receipt", "Retry Receipt")).returncode, 0)

    def test_draft_echo_fails(self) -> None:
        draft = (
            "Today marks a pivotal milestone for resilient collaboration. Our transformative "
            "platform unlocks modern productivity for fast-moving teams."
        )
        result = self.grade(draft)
        self.assertEqual(result.returncode, 1)
        self.assertIn("missing required text: 'HMAC'", result.stdout)
        self.assertIn("forbidden regex present", result.stdout)

    def test_missing_one_mechanism_fails(self) -> None:
        result = self.grade("The tool rejects webhook retries without a matching HMAC signature.")
        self.assertEqual(result.returncode, 1)
        self.assertIn("missing required text: 'retry receipt'", result.stdout)

    def test_grounded_rewrite_with_launch_copy_fails(self) -> None:
        for phrase in ("A pivotal release.", "It is transformative.", "Built for fast-moving teams."):
            with self.subTest(phrase=phrase):
                self.assertEqual(self.grade(GOOD + " " + phrase).returncode, 1)

    def test_inflected_unlock_is_still_generic_copy(self) -> None:
        # The fixture's own draft says "unlocks"; a rewrite that keeps that verb
        # with a new object has not removed the generic benefit claim.
        for phrase in ("It unlocks faster incident review.", "Unlocking safer retries."):
            with self.subTest(phrase=phrase):
                result = self.grade(GOOD + " " + phrase)
                self.assertEqual(result.returncode, 1, result.stdout)

    def test_near_miss_words_are_not_flagged(self) -> None:
        # Neighbouring vocabulary that is not launch copy must not fail the case.
        for phrase in (
            "The platform team owns the check.",
            "The transformation step runs before signing.",
            "Teams can unpack the receipt for audits.",
        ):
            with self.subTest(phrase=phrase):
                result = self.grade(GOOD + " " + phrase)
                self.assertEqual(result.returncode, 0, result.stdout)

    def test_missing_output_and_unknown_case_are_harness_errors(self) -> None:
        self.assertEqual(self.grade(None).returncode, 2)
        self.assertEqual(self.grade(GOOD, case="no-such-case").returncode, 2)


if __name__ == "__main__":
    unittest.main()
