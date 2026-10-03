"""scripts/run_evals.py: prepare worklists, grade judgments, join runs.

Expected scores are hand-derived from the judgment records in each test.
"""
from __future__ import annotations

import contextlib
import io
import json
import tempfile
import unittest
from pathlib import Path

from _support import ROOT, load_script, run_script, write_jsonl

run_evals = load_script("scripts/run_evals.py")


def judgment(case_id: str, passes: list[bool], split: str = "holdout", graded: list[int] | None = None) -> dict:
    record = {
        "id": case_id,
        "suite": "evals.json",
        "split": split,
        "assertions": [{"index": i, "pass": p, "evidence": "q"} for i, p in enumerate(passes, start=1)],
    }
    if graded is not None:
        record["graded_dimensions"] = [{"name": f"d{i}", "score": s} for i, s in enumerate(graded)]
    return record


class CaseScore(unittest.TestCase):
    def score(self, record: dict, include_graded: bool = False) -> dict:
        return run_evals.case_score(record, Path("j.jsonl"), 1, include_graded=include_graded)

    def test_score_is_fraction_of_assertions_passed(self) -> None:
        result = self.score(judgment("a", [True, False, True]))
        self.assertAlmostEqual(result["score"], 0.6667)
        self.assertEqual((result["n_passed"], result["n_assertions"], result["all_pass"]), (2, 3, False))

    def test_graded_dimensions_reported_but_not_scored_by_default(self) -> None:
        result = self.score(judgment("a", [True, False, True], graded=[5, 1]))
        self.assertAlmostEqual(result["score"], 0.6667)
        self.assertAlmostEqual(result["graded_score"], 0.6)  # (5/5 + 1/5) / 2

    def test_include_graded_averages_assertions_and_normalized_dimensions(self) -> None:
        # (1 + 0 + 1 + 5/5 + 1/5) / 5 = 0.64
        result = self.score(judgment("a", [True, False, True], graded=[5, 1]), include_graded=True)
        self.assertAlmostEqual(result["score"], 0.64)
        self.assertAlmostEqual(result["assertion_score"], 0.6667)

    def test_malformed_judgments_are_rejected(self) -> None:
        bad = {
            "string pass": {"id": "a", "assertions": [{"pass": "true"}]},
            "no assertions": {"id": "a", "assertions": []},
            "graded out of range": judgment("a", [True], graded=[6]),
            "no id": {"assertions": [True]},
        }
        for name, record in bad.items():
            with self.subTest(name), self.assertRaises(SystemExit), contextlib.redirect_stderr(io.StringIO()):
                self.score(record)


class Cli(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = Path(tempfile.mkdtemp())

    def test_prepare_filters_split_and_shows_judge_every_assertion(self) -> None:
        out = self.tmp / "work.json"
        result = run_script("scripts/run_evals.py", "prepare", "evals/evals.json", "--split", "holdout", "--out", out)
        self.assertEqual(result.returncode, 0, result.stderr)
        work = json.loads(out.read_text())
        source = json.loads((ROOT / "evals/evals.json").read_text())["evals"]
        holdout = {c["id"]: c for c in source if c["split"] == "holdout"}
        self.assertEqual({u["id"] for u in work["units"]}, set(holdout))
        self.assertEqual(work["unit_count"], len(holdout))
        for unit in work["units"]:
            case = holdout[unit["id"]]
            self.assertIn(case["prompt"], unit["apply_prompt"])
            for i, assertion in enumerate(case["assertions"], start=1):
                self.assertIn(f"{i}. {assertion}", unit["judge_prompt"])

    def test_grade_rejects_duplicate_ids_across_files(self) -> None:
        a = write_jsonl(self.tmp / "a.jsonl", [judgment("x", [True, True])])
        b = write_jsonl(self.tmp / "b.jsonl", [judgment("x", [False, True])])
        result = run_script("scripts/run_evals.py", "grade", a, b)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("duplicate id", result.stderr)

    def test_grade_fails_on_a_missing_judgment_file(self) -> None:
        # A typo in one path must not silently shrink the scored set.
        present = write_jsonl(self.tmp / "a.jsonl", [judgment("x", [True, True])])
        result = run_script("scripts/run_evals.py", "grade", present, self.tmp / "missing.jsonl")
        self.assertNotEqual(result.returncode, 0, result.stdout)
        self.assertIn("missing.jsonl", result.stderr)

    def test_grade_expands_globs(self) -> None:
        write_jsonl(self.tmp / "j1.jsonl", [judgment("x", [True, True])])
        write_jsonl(self.tmp / "j2.jsonl", [judgment("y", [True, False])])
        result = run_script("scripts/run_evals.py", "grade", self.tmp / "j*.jsonl")
        self.assertEqual(result.returncode, 0, result.stderr)
        scores = {json.loads(line)["id"]: json.loads(line)["score"] for line in result.stdout.splitlines()}
        self.assertEqual(scores, {"x": 1.0, "y": 0.5})

    def test_grade_join_and_gate_round_trip(self) -> None:
        # Before: every holdout case passes 1 of 2 assertions. After: 2 of 2.
        ids = [f"case-{i}" for i in range(10)]
        before_j = write_jsonl(self.tmp / "before-j.jsonl", [judgment(i, [True, False]) for i in ids])
        after_j = write_jsonl(self.tmp / "after-j.jsonl", [judgment(i, [True, True]) for i in ids])
        before, after, delta = self.tmp / "before.jsonl", self.tmp / "after.jsonl", self.tmp / "delta.jsonl"
        for src, dst in ((before_j, before), (after_j, after)):
            graded = run_script("scripts/run_evals.py", "grade", src, "--out", dst)
            self.assertEqual(graded.returncode, 0, graded.stderr)
        joined = run_script("scripts/run_evals.py", "join", "--before", before, "--after", after, "--out", delta)
        self.assertEqual(joined.returncode, 0, joined.stderr)
        rows = [json.loads(line) for line in delta.read_text().splitlines()]
        self.assertEqual({(r["id"], r["before"], r["after"]) for r in rows}, {(i, 0.5, 1.0) for i in ids})
        self.assertEqual(run_script("scripts/score_delta.py", delta, "--holdout-only").returncode, 0)
        # The same files in reverse are a regression and must not pass the gate.
        reverse = self.tmp / "reverse.jsonl"
        run_script("scripts/run_evals.py", "join", "--before", after, "--after", before, "--out", reverse)
        self.assertEqual(run_script("scripts/score_delta.py", reverse, "--holdout-only").returncode, 1)

    def test_join_requires_shared_ids(self) -> None:
        a = write_jsonl(self.tmp / "a.jsonl", [{"id": "x", "split": "tune", "score": 1}])
        b = write_jsonl(self.tmp / "b.jsonl", [{"id": "y", "split": "tune", "score": 1}])
        result = run_script("scripts/run_evals.py", "join", "--before", a, "--after", b)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("no shared ids", result.stderr)


if __name__ == "__main__":
    unittest.main()
