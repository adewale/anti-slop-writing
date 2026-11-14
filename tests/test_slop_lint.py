"""Recall-oriented spans are not prose-quality or authorship verdicts."""
from __future__ import annotations

import json
import subprocess
import sys
import unittest

from _support import ROOT, load_script

lint = load_script("evals/oracles/slop_lint.py")


class Lint(unittest.TestCase):
    def test_each_detector_has_positive_negative_and_near_miss(self):
        cases = [
            ("significance-compression", "That's the whole point.", "The checkpoint stores the last ID.", "The whole point of the needle broke."),
            ("therapy-voice", "Sit with that for a moment.", "The job failed at step 4.", "Sit with the operator during the test."),
            ("performative-honesty", "Let's be honest: the migration failed.", "The migration failed.", "Let's test whether the log is complete."),
            ("stage-management", "Turns out the index was missing.", "The index was missing.", "The lathe turns outward."),
            ("sentence-anaphora", "Maybe the alert failed. Maybe the owner slept. Maybe the link broke.", "The alert fired. A worker acknowledged it.", "Maybe the alert failed. Maybe the link broke."),
            ("stacked-questions", "Did the alert fire? Did anyone respond?", "The alert fired. A worker responded.", "Did the alert fire? The log says yes."),
            ("no-chain", "No account, no install, no setup.", "Open a local file.", "No account, no install."),
            ("stranded-auxiliary", "The tool died; the data didn't.", "The data remained readable.", "The data didn't disappear."),
        ]
        for detector, positive, negative, near in cases:
            with self.subTest(detector=detector):
                self.assertIn(detector, {h["detector"] for h in lint.findings(positive)})
                self.assertNotIn(detector, {h["detector"] for h in lint.findings(negative)})
                self.assertNotIn(detector, {h["detector"] for h in lint.findings(near)})

    def test_cli_findings_do_not_fail_prose_but_missing_rewrite_is_an_error(self):
        command = [sys.executable, str(ROOT / "evals/oracles/slop_lint.py"), "-"]
        result = subprocess.run(command, input="Turns out it failed.", text=True, capture_output=True, timeout=10)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)["counts"], {"stage-management": 1})
        malformed = subprocess.run([*command, "--rewrite-only"], input="No rewrite field.", text=True, capture_output=True, timeout=10)
        self.assertEqual(malformed.returncode, 2)
        self.assertIn("exactly one Concrete rewrite", malformed.stderr)

    def test_offsets_slice_original_unicode_text_and_are_deterministic(self):
        text = "Résumé: That's not nothing. Café: let’s be honest, it failed."
        found = lint.findings(text)
        self.assertEqual(found, lint.findings(text))
        self.assertGreaterEqual(len(found), 2)
        for hit in found:
            self.assertEqual(text[hit["start"]:hit["end"]], hit["text"])
            self.assertLess(hit["start"], hit["end"])

    def test_maximal_anaphora_run_is_one_hit_and_paragraphs_do_not_join(self):
        text = "Maybe one. Maybe two. Maybe three. Maybe four."
        hits = [h for h in lint.findings(text) if h["detector"] == "sentence-anaphora"]
        self.assertEqual(len(hits), 1)
        self.assertEqual(hits[0]["text"], text)
        separated = "Maybe one. Maybe two.\n\nMaybe three."
        self.assertNotIn("sentence-anaphora", {h["detector"] for h in lint.findings(separated)})
        self.assertNotIn("sentence-anaphora", {h["detector"] for h in lint.findings(separated.replace("\n\n", "\n \t\n"))})
        self.assertNotIn("stacked-questions", {h["detector"] for h in lint.findings("Why A?\n \t\nWhy B?")})

    def test_earned_use_is_flagged_for_review_not_automatically_failed(self):
        text = "No allocations in the hot loop, no network calls in the transaction, no writes before validation."
        report = lint.report(text)
        self.assertEqual(report["counts"]["no-chain"], 1)
        self.assertEqual(report["mode"], "triage-only")
        self.assertNotIn("verdict", report)
        self.assertNotIn("pass", report)
        self.assertNotIn("is_ai", report)

    def test_rewrite_scope_ignores_quoted_critique_and_preserves_original_offsets(self):
        review = "Slop tells: ‘Turns out’ announces a reveal.\nConcrete rewrite:\n```txt\nThe index was missing.\n```\nRewrite check: passes self-detectors\nRemembered line: That's the whole point.\n"
        result = lint.report(review, rewrite_only=True)
        self.assertEqual(result["findings"], [])
        changed = review.replace("The index was missing.", "Turns out the index was missing.")
        hits = lint.report(changed, rewrite_only=True)["findings"]
        self.assertEqual(len(hits), 1)
        self.assertEqual(changed[hits[0]["start"]:hits[0]["end"]], "Turns out")

    def test_missing_duplicate_or_empty_rewrite_does_not_silently_pass(self):
        for text in ("A critique without its rewrite.", "Concrete rewrite:\nRewrite check: passes", "Concrete rewrite: One.\nConcrete rewrite: Two.", "Concrete rewrite:\n```txt\nunclosed"):
            with self.subTest(text=text), self.assertRaises(ValueError):
                lint.report(text, rewrite_only=True)
        plain = lint.report("**Concrete rewrite:** Turns out it failed.\n**Rewrite check:** passes", rewrite_only=True)
        self.assertEqual(plain["counts"]["stage-management"], 1)


if __name__ == "__main__":
    unittest.main()
