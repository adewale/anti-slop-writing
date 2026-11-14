"""scripts/validate.py: the repo copy passes, and each planted defect fails.

Each test copies the working tree to a scratch directory, plants one defect,
and runs the real validator there, so the copy under test is the same code CI
runs.
"""

from __future__ import annotations

import json
import shutil
import tempfile
import unittest
from pathlib import Path

from _support import ROOT, run_script


def copy_validation_fixture(source: Path, destination: Path) -> None:
    shutil.copytree(source, destination, ignore=shutil.ignore_patterns(
        ".git", "__pycache__", "eval-workspace", ".ruff_cache", ".venv",
    ))


class FixtureIsolation(unittest.TestCase):
    def test_excludes_runtime_and_caches_but_keeps_validation_inputs(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "source"
            for name in ("eval-workspace", ".ruff_cache", ".venv", "evals"):
                (source / name).mkdir(parents=True)
                (source / name / "canary").write_text(name)
            destination = Path(directory) / "copy"
            copy_validation_fixture(source, destination)
            self.assertEqual((destination / "evals/canary").read_text(), "evals")
            for name in ("eval-workspace", ".ruff_cache", ".venv"):
                with self.subTest(name=name):
                    self.assertFalse((destination / name).exists())


class Validate(unittest.TestCase):
    def setUp(self) -> None:
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name) / "repo"
        copy_validation_fixture(ROOT, self.root)

    def validate(self):
        return run_script("scripts/validate.py", cwd=self.root)

    def edit_json(self, rel: str, change) -> None:
        path = self.root / rel
        data = json.loads(path.read_text(encoding="utf-8"))
        change(data)
        path.write_text(json.dumps(data, indent=2), encoding="utf-8")

    def assert_fails_with(self, message: str) -> None:
        result = self.validate()
        self.assertEqual(result.returncode, 1, result.stdout)
        self.assertIn(message, result.stdout)

    def test_repository_copy_passes(self) -> None:
        result = self.validate()
        self.assertEqual(result.returncode, 0, result.stdout)

    def test_eval_case_without_split_fails(self) -> None:
        self.edit_json("evals/adversarial.json", lambda d: d["evals"][0].pop("split"))
        self.assert_fails_with("split must be one of")

    def test_duplicate_eval_id_fails(self) -> None:
        def dup(d):
            d["evals"][1]["id"] = d["evals"][0]["id"]

        self.edit_json("evals/rewrite-evals.json", dup)
        self.assert_fails_with("duplicate eval id")

    def test_single_assertion_case_fails(self) -> None:
        def trim(d):
            d["evals"][0]["assertions"] = d["evals"][0]["assertions"][:1]

        self.edit_json("evals/meta-evals.json", trim)
        self.assert_fails_with("must have at least 2 assertions")

    def test_missing_reference_target_fails(self) -> None:
        skill = self.root / "skills/anti-slop-writing/SKILL.md"
        skill.write_text(
            skill.read_text(encoding="utf-8") + "\nreferences/not-there.md\n",
            encoding="utf-8",
        )
        self.assert_fails_with("references missing file: references/not-there.md")

    def test_trigger_queries_without_near_miss_negatives_fail(self) -> None:
        def rename(d):
            for q in d["queries"]:
                q["id"] = q["id"].replace("near-neg-", "neg-")

        self.edit_json("evals/trigger-queries.json", rename)
        self.assert_fails_with("near-neg- near-miss negatives")

    def test_trigger_queries_without_enough_holdout_fail(self) -> None:
        def retune(d):
            for q in d["queries"]:
                q["split"] = "tune"

        self.edit_json("evals/trigger-queries.json", retune)
        self.assert_fails_with("at least 4 holdout queries")

    def test_rewrite_case_requires_facts_field(self) -> None:
        self.edit_json("evals/rewrite-evals.json", lambda d: d["evals"][0].pop("facts"))
        self.assert_fails_with("facts must be a list")

    def test_twitter_case_requires_explicit_facts(self) -> None:
        self.edit_json("evals/twitter-evals.json", lambda d: d["evals"][0].pop("facts"))
        self.assert_fails_with("facts must be a list")

    def test_twitter_case_rejects_blank_fact(self) -> None:
        self.edit_json("evals/twitter-evals.json", lambda d: d["evals"][0].update(facts=[" "]))
        self.assert_fails_with("facts must be a list")

    def test_twitter_source_in_prompt_may_have_no_additional_facts(self) -> None:
        self.edit_json("evals/twitter-evals.json", lambda d: d["evals"][0].update(facts=[]))
        result = self.validate()
        self.assertEqual(result.returncode, 0, result.stdout)

    def twin(self, data: dict) -> dict:
        return next(c for c in data["evals"] if c.get("paired_with"))

    def test_fact_twin_without_facts_fails(self) -> None:
        self.edit_json(
            "evals/rewrite-evals.json", lambda d: self.twin(d).update(facts=[])
        )
        self.assert_fails_with("must supply facts")

    def test_fact_twin_with_a_dangling_partner_fails(self) -> None:
        self.edit_json(
            "evals/evals.json",
            lambda d: self.twin(d).update(paired_with="no-such-case"),
        )
        self.assert_fails_with("paired_with names no other case")

    def test_fact_pair_split_across_tune_and_holdout_fails(self) -> None:
        def flip(d):
            t = self.twin(d)
            t["split"] = "holdout" if t["split"] == "tune" else "tune"

        self.edit_json("evals/evals.json", flip)
        self.assert_fails_with("has a different split")

    def test_fact_twin_may_reword_its_prompt(self) -> None:
        # Near-miss: a twin's prompt may differ from its partner's (for example,
        # to drop "no source notes are available"); only facts and split are tied.
        def reword(d):
            self.twin(d)["prompt"] += " Use the author's notes."

        self.edit_json("evals/rewrite-evals.json", reword)
        result = self.validate()
        self.assertEqual(result.returncode, 0, result.stdout)

    def test_required_fact_twin_cannot_be_deleted(self) -> None:
        def remove_twin(d):
            twin_id = self.twin(d)["id"]
            d["evals"] = [c for c in d["evals"] if c["id"] != twin_id]

        self.edit_json("evals/evals.json", remove_twin)
        self.assert_fails_with("requires_fact_pair but has no facts-supplied twin")

    def test_unpaired_source_sufficient_case_remains_valid(self) -> None:
        # An exporter case already supplies its mechanism and needs no ask-side twin.
        self.edit_json(
            "evals/evals.json", lambda d: d["evals"][0].update(requires_fact_pair=False)
        )
        result = self.validate()
        self.assertEqual(result.returncode, 0, result.stdout)

    def test_pair_reference_must_be_a_string(self) -> None:
        self.edit_json(
            "evals/evals.json", lambda d: self.twin(d).update(paired_with=[])
        )
        self.assert_fails_with("paired_with must be a non-empty string")

    def test_pair_requirement_is_boolean(self) -> None:
        self.edit_json(
            "evals/evals.json", lambda d: d["evals"][0].update(requires_fact_pair="yes")
        )
        self.assert_fails_with("requires_fact_pair must be boolean")

    def test_copied_eight_word_example_fails(self) -> None:
        def leak(d):
            d["evals"][0]["prompt"] = (
                "Review: The workflow can fail on step 4, retry only that step, and keep the previous outputs."
            )

        self.edit_json("evals/evals.json", leak)
        self.assert_fails_with("eval leakage")

    def test_seven_word_near_miss_does_not_fail(self) -> None:
        def short(d):
            d["evals"][0]["prompt"] = "Review: The workflow can fail on step 4."

        self.edit_json("evals/evals.json", short)
        result = self.validate()
        self.assertEqual(result.returncode, 0, result.stdout)

    def test_holdout_fixture_copy_is_checked(self) -> None:
        fixture = self.root / "evals/fixtures/alert-triage-transfer/input.md"
        fixture.write_text(
            "The workflow can fail on step 4, retry only that step, and keep the previous outputs."
        )
        self.assert_fails_with("eval leakage")

    def test_holdout_cannot_reuse_tune_fixture(self) -> None:
        def reuse(d):
            d["evals"][-1]["prompt"] = (
                "Rewrite evals/fixtures/tweet-taste-as-model/input.md"
            )

        self.edit_json("evals/rewrite-evals.json", reuse)
        self.assert_fails_with("fixture shared between tune and holdout")

    def test_word_growth_requires_consolidation_note(self) -> None:
        skill = self.root / "skills/anti-slop-writing/SKILL.md"
        skill.write_text(skill.read_text() + "\n" + "extra " * 201)
        self.assert_fails_with("budget +200")

    def test_word_growth_of_exactly_200_is_allowed(self) -> None:
        skill = self.root / "skills/anti-slop-writing/SKILL.md"
        skill.write_text(skill.read_text() + "\n" + "extra " * 200)
        result = self.validate()
        self.assertEqual(result.returncode, 0, result.stdout)

    def test_consolidation_note_records_budget_exception(self) -> None:
        skill = self.root / "skills/anti-slop-writing/SKILL.md"
        skill.write_text(skill.read_text() + "\n" + "extra " * 201)
        (self.root / "docs/consolidation.md").write_text(
            "Consolidation removed duplicate examples; remaining growth is recorded for review."
        )
        self.edit_json(
            "docs/skill-length-baseline.json",
            lambda d: d.update(consolidation_note="docs/consolidation.md"),
        )
        result = self.validate()
        self.assertEqual(result.returncode, 0, result.stdout)


if __name__ == "__main__":
    unittest.main()
