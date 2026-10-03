"""scripts/check_install_boundary.py run against a scratch copy of the installable tree."""
from __future__ import annotations

import shutil
import tempfile
import unittest
from pathlib import Path

from _support import ROOT, run_script

SKILL = Path("skills/anti-slop-writing")


class InstallBoundary(unittest.TestCase):
    def setUp(self) -> None:
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name)
        shutil.copytree(ROOT / "skills", self.root / "skills")
        shutil.copy(ROOT / "package.json", self.root / "package.json")
        (self.root / "scripts").mkdir()
        shutil.copy(ROOT / "scripts/check_install_boundary.py", self.root / "scripts")

    def check(self):
        return run_script("scripts/check_install_boundary.py", cwd=self.root)

    def plant(self, rel: str) -> None:
        path = self.root / SKILL / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("x", encoding="utf-8")

    def test_shipped_skill_tree_is_clean(self) -> None:
        result = self.check()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn(str(SKILL), result.stdout)

    def test_repo_only_artifacts_fail(self) -> None:
        for rel in ("evals/cases.json", "references/tests/case.md", "references/__pycache__/x.cpython-311.pyc", "scratch.pyc", ".DS_Store"):
            with self.subTest(rel=rel):
                self.setUp()
                self.plant(rel)
                result = self.check()
                self.assertEqual(result.returncode, 1, result.stdout)
                self.assertIn(Path(rel).parts[0], result.stderr)

    def test_near_miss_names_pass(self) -> None:
        # Files whose names merely contain a banned word are skill content.
        for rel in ("references/evals-overview.md", "references/tests.md", "references/research-notes.md"):
            self.plant(rel)
        result = self.check()
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_missing_skill_md_fails(self) -> None:
        (self.root / SKILL / "SKILL.md").unlink()
        result = self.check()
        self.assertEqual(result.returncode, 1)
        self.assertIn("missing SKILL.md", result.stderr)


if __name__ == "__main__":
    unittest.main()
