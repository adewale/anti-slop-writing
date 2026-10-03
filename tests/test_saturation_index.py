"""scripts/saturation_index.py groups runs of one case by stripping the axis prefix."""
from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from _support import run_script, write_jsonl


class Saturation(unittest.TestCase):
    def test_flags_ceiling_flat_and_spread_cases(self) -> None:
        records = [
            {"id": "opus__easy", "split": "tune", "score": 1.0},
            {"id": "haiku__easy", "split": "tune", "score": 1.0},
            {"id": "opus__stuck", "split": "tune", "score": 0.5},
            {"id": "haiku__stuck", "split": "tune", "score": 0.5},
            {"id": "opus__useful", "split": "holdout", "score": 1.0},
            {"id": "haiku__useful", "split": "holdout", "score": 0.25},
        ]
        path = write_jsonl(Path(tempfile.mkdtemp()) / "scores.jsonl", records)
        result = run_script("scripts/saturation_index.py", path)
        self.assertEqual(result.returncode, 0, result.stderr)
        flags = {line.split()[0]: line.split()[-1] for line in result.stdout.splitlines() if line.split()[-1:] in (["CEILING"], ["flat"], ["spread"])}
        self.assertEqual(flags, {"easy": "CEILING", "stuck": "flat", "useful": "spread"})
        self.assertIn("Saturation index:  0.333", result.stdout)

    def test_separator_is_configurable(self) -> None:
        records = [{"id": "a::x", "split": "tune", "score": 1.0}, {"id": "b::x", "split": "tune", "score": 0.0}]
        path = write_jsonl(Path(tempfile.mkdtemp()) / "scores.jsonl", records)
        result = run_script("scripts/saturation_index.py", path, "--sep", "::")
        self.assertIn("Cases:             1", result.stdout)
        self.assertIn("Saturation index:  0.000", result.stdout)


if __name__ == "__main__":
    unittest.main()
