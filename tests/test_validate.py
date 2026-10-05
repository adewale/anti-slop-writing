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


class Validate(unittest.TestCase):
    def setUp(self) -> None:
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name) / "repo"
        shutil.copytree(ROOT, self.root, ignore=shutil.ignore_patterns(".git", "__pycache__"))

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
        skill.write_text(skill.read_text(encoding="utf-8") + "\nreferences/not-there.md\n", encoding="utf-8")
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


if __name__ == "__main__":
    unittest.main()
