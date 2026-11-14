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


def judgment(
    case_id: str,
    passes: list[bool],
    split: str = "holdout",
    graded: list[int] | None = None,
) -> dict:
    record = {
        "id": case_id,
        "suite": "evals.json",
        "split": split,
        "assertions": [
            {"index": i, "pass": p, "evidence": "q"}
            for i, p in enumerate(passes, start=1)
        ],
    }
    if graded is not None:
        record["graded_dimensions"] = [
            {"name": f"d{i}", "score": s} for i, s in enumerate(graded)
        ]
    return record


class CaseScore(unittest.TestCase):
    def score(self, record: dict, include_graded: bool = False) -> dict:
        return run_evals.case_score(
            record, Path("j.jsonl"), 1, include_graded=include_graded
        )

    def test_score_is_fraction_of_assertions_passed(self) -> None:
        result = self.score(judgment("a", [True, False, True]))
        self.assertAlmostEqual(result["score"], 0.6667)
        self.assertEqual(
            (result["n_passed"], result["n_assertions"], result["all_pass"]),
            (2, 3, False),
        )

    def test_graded_dimensions_reported_but_not_scored_by_default(self) -> None:
        result = self.score(judgment("a", [True, False, True], graded=[5, 1]))
        self.assertAlmostEqual(result["score"], 0.6667)
        self.assertAlmostEqual(result["graded_score"], 0.6)  # (5/5 + 1/5) / 2

    def test_include_graded_averages_assertions_and_normalized_dimensions(self) -> None:
        # (1 + 0 + 1 + 5/5 + 1/5) / 5 = 0.64
        result = self.score(
            judgment("a", [True, False, True], graded=[5, 1]), include_graded=True
        )
        self.assertAlmostEqual(result["score"], 0.64)
        self.assertAlmostEqual(result["assertion_score"], 0.6667)

    def test_malformed_judgments_are_rejected(self) -> None:
        bad = {
            "string pass": {"id": "a", "assertions": [{"pass": "true"}]},
            "no assertions": {"id": "a", "assertions": []},
            "graded out of range": judgment("a", [True], graded=[6]),
            "boolean grade": judgment("a", [True], graded=[True]),
            "no id": {"assertions": [True]},
        }
        for name, record in bad.items():
            with (
                self.subTest(name),
                self.assertRaises(SystemExit),
                contextlib.redirect_stderr(io.StringIO()),
            ):
                self.score(record)


class Cli(unittest.TestCase):
    def setUp(self) -> None:
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.tmp = Path(tmp.name)

    def test_prepare_filters_split_and_shows_judge_every_assertion(self) -> None:
        out = self.tmp / "work.json"
        judge_out = self.tmp / "judge.json"
        result = run_script(
            "scripts/run_evals.py",
            "prepare",
            "evals/evals.json",
            "--split",
            "holdout",
            "--out",
            out,
            "--judge-out",
            judge_out,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        work = json.loads(out.read_text())
        source = json.loads((ROOT / "evals/evals.json").read_text())["evals"]
        holdout = {c["id"]: c for c in source if c["split"] == "holdout"}
        self.assertEqual({u["id"] for u in work["units"]}, set(holdout))
        self.assertEqual(work["unit_count"], len(holdout))
        for unit in work["units"]:
            case = holdout[unit["id"]]
            self.assertIn(case["prompt"], unit["apply_prompt"])
            self.assertEqual(set(unit), {"id", "suite", "split", "apply_prompt"})
        for unit in json.loads(judge_out.read_text())["units"]:
            case = holdout[unit["id"]]
            self.assertNotIn("apply_prompt", unit)
            for i, assertion in enumerate(case["assertions"], start=1):
                self.assertIn(f"{i}. {assertion}", unit["judge_prompt"])

    def test_prepare_keeps_rubric_secret_and_sends_facts_to_both_roles(self) -> None:
        case = {
            "id": "x",
            "split": "tune",
            "prompt": "Rewrite the draft.",
            "facts": ["The retry waits ten seconds."],
            "assertions": ["SECRET_ASSERTION"],
            "dynamic_rubric": {"instruction": "SECRET_RUBRIC", "minimum_criteria": 3},
        }
        src = self.tmp / "cases.json"
        src.write_text(json.dumps({"evals": [case]}))
        apply, judge = self.tmp / "apply.json", self.tmp / "judge.json"
        result = run_script(
            "scripts/run_evals.py", "prepare", src, "--out", apply, "--judge-out", judge
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertNotIn("SECRET", apply.read_text())
        self.assertIn(
            "SECRET_RUBRIC", json.loads(judge.read_text())["units"][0]["judge_prompt"]
        )
        for p in (apply, judge):
            self.assertIn("The retry waits ten seconds.", p.read_text())

    def test_fact_pairs_survive_prepare_grade_join_and_clustered_gate(self) -> None:
        # Five independent tasks, each asked with and without additional facts:
        # ten rows must still count as five independent units. Judgments here
        # are synthetic arithmetic fixtures, not generated model results.
        cases = []
        for i in range(5):
            base = {
                "id": f"p{i}",
                "split": "holdout",
                "prompt": "Rewrite the draft.",
                "facts": [],
                "assertions": ["fidelity", "task fulfilled"],
            }
            cases.extend(
                [
                    base,
                    {
                        **base,
                        "id": f"p{i}-facts",
                        "paired_with": f"p{i}",
                        "facts": ["The scheduler retries after ten seconds."],
                    },
                ]
            )
        src = self.tmp / "cases.json"
        src.write_text(json.dumps({"evals": cases}))
        apply, judge = self.tmp / "apply.json", self.tmp / "judge.json"
        prepared = run_script(
            "scripts/run_evals.py", "prepare", src, "--out", apply, "--judge-out", judge
        )
        self.assertEqual(prepared.returncode, 0, prepared.stderr)
        for unit in json.loads(apply.read_text())["units"]:
            self.assertNotIn("pair_id", unit)
            self.assertNotIn("fact_condition", unit)
        units = json.loads(judge.read_text())["units"]
        self.assertEqual({u["pair_id"] for u in units}, {f"p{i}" for i in range(5)})
        self.assertEqual(
            {u["fact_condition"] for u in units}, {"supplied", "no_additional_facts"}
        )
        for u in units:
            self.assertIn(f'"pair_id": "{u["pair_id"]}"', u["judge_prompt"])
        scores = []
        for arm, passes in [("before", [True, False]), ("after", [True, True])]:
            records = []
            for u in units:
                r = judgment(u["id"], passes)
                r.update(
                    suite=u["suite"],
                    pair_id=u["pair_id"],
                    fact_condition=u["fact_condition"],
                )
                records.append(r)
            judgments = write_jsonl(self.tmp / f"{arm}-judgments.jsonl", records)
            out = self.tmp / f"{arm}-scores.jsonl"
            graded = run_script(
                "scripts/run_evals.py",
                "grade",
                judgments,
                "--worklist",
                judge,
                "--out",
                out,
            )
            self.assertEqual(graded.returncode, 0, graded.stderr)
            scores.append(out)
        delta = self.tmp / "delta.jsonl"
        joined = run_script(
            "scripts/run_evals.py",
            "join",
            "--before",
            scores[0],
            "--after",
            scores[1],
            "--out",
            delta,
        )
        self.assertEqual(joined.returncode, 0, joined.stderr)
        unclustered = run_script("scripts/score_delta.py", delta)
        self.assertNotEqual(unclustered.returncode, 0)
        self.assertIn("spans independent units", unclustered.stderr)
        clustered = run_script(
            "scripts/score_delta.py", delta, "--cluster-field", "pair_id"
        )
        self.assertEqual(clustered.returncode, 2, clustered.stdout + clustered.stderr)
        self.assertIn("Cases:         10", clustered.stdout)
        self.assertIn("Clusters:      5", clustered.stdout)
        self.assertIn("UNDERPOWERED", clustered.stdout)

    def test_prepare_rejects_overlapping_role_files(self) -> None:
        dest = self.tmp / "same.json"
        result = run_script(
            "scripts/run_evals.py",
            "prepare",
            "evals/evals.json",
            "--out",
            dest,
            "--judge-out",
            dest,
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("different files", result.stderr)

    def test_no_skill_arm_has_the_identical_task_and_facts(self) -> None:
        worklists = []
        for suffix, flags in [("current", []), ("none", ["--no-skill"])]:
            apply, judge = (
                self.tmp / f"{suffix}.json",
                self.tmp / f"{suffix}-judge.json",
            )
            result = run_script(
                "scripts/run_evals.py",
                "prepare",
                "evals/evals.json",
                "--out",
                apply,
                "--judge-out",
                judge,
                *flags,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            worklists.append(json.loads(apply.read_text()))
        self.assertIsNone(worklists[1]["skill_path"])
        for a, b in zip(worklists[0]["units"], worklists[1]["units"]):
            self.assertEqual(
                a["apply_prompt"].split("TASK:\n", 1)[1],
                b["apply_prompt"].split("TASK:\n", 1)[1],
            )
            self.assertNotIn("Read skills/", b["apply_prompt"])

    def test_empty_facts_block_does_not_coach_the_expected_behavior(self) -> None:
        # The no-skill arm must not receive the skill's ask-or-cut behavior as an
        # instruction. Known-good: neutral statement. Known-bad: the old coaching
        # sentence. Near-miss: a task prompt that itself says "ask" stays intact.
        cases = [
            {
                "id": "empty",
                "split": "tune",
                "prompt": "Rewrite the draft.",
                "facts": [],
                "assertions": ["a", "b"],
            },
            {
                "id": "task-asks",
                "split": "tune",
                "prompt": "Rewrite this, or ask for the missing relation.",
                "facts": [],
                "assertions": ["a", "b"],
            },
        ]
        src = self.tmp / "cases.json"
        src.write_text(json.dumps({"evals": cases}))
        for flags in ([], ["--no-skill"]):
            apply, judge = self.tmp / "apply.json", self.tmp / "judge.json"
            result = run_script(
                "scripts/run_evals.py",
                "prepare",
                src,
                "--out",
                apply,
                "--judge-out",
                judge,
                *flags,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            units = {u["id"]: u for u in json.loads(apply.read_text())["units"]}
            for unit in units.values():
                facts_block = unit["apply_prompt"].split("Facts available:\n", 1)[1]
                self.assertEqual(
                    facts_block.strip(), "No additional facts beyond the source text."
                )
                self.assertNotIn("Ask for missing facts", unit["apply_prompt"])
                self.assertNotIn("cut unsupported", unit["apply_prompt"])
            self.assertIn(
                "or ask for the missing relation", units["task-asks"]["apply_prompt"]
            )

    def test_prepare_embeds_only_fixture_input(self) -> None:
        case = {
            "id": "x",
            "split": "tune",
            "prompt": "Read evals/fixtures/alert-triage-transfer/input.md",
            "assertions": ["SECRET"],
        }
        src = self.tmp / "cases.json"
        src.write_text(json.dumps({"evals": [case]}))
        apply, judge = self.tmp / "apply.json", self.tmp / "judge.json"
        result = run_script(
            "scripts/run_evals.py", "prepare", src, "--out", apply, "--judge-out", judge
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("The practice inbox", apply.read_text())
        self.assertNotIn("SECRET", apply.read_text())
        case["prompt"] = "Read evals/fixtures/tweet-taste-as-model/best-rewrite.md"
        src.write_text(json.dumps({"evals": [case]}))
        result = run_script(
            "scripts/run_evals.py", "prepare", src, "--out", apply, "--judge-out", judge
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("only fixture input.md", result.stderr)

    def test_blind_removes_multiline_fields_and_records_lengths(self) -> None:
        src = self.tmp / "candidate.md"
        src.write_text(
            "Verdict: revise\nConcrete rewrite: Use the queue.\nRewrite check: VERSION_SECRET\ncontinued secret\nRemembered line: SECRET\n"
        )
        dest, key, counts = (
            self.tmp / "blinded",
            self.tmp / "key.json",
            self.tmp / "counts.jsonl",
        )
        result = run_script(
            "scripts/run_evals.py",
            "blind",
            src,
            "--out-dir",
            dest,
            "--key-out",
            key,
            "--counts-out",
            counts,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        files = list(dest.glob("*.md"))
        self.assertEqual(len(files), 1)
        self.assertNotEqual(files[0].name, src.name)
        self.assertEqual(
            files[0].read_text(), "Verdict: revise\nConcrete rewrite: Use the queue.\n"
        )
        row = json.loads(counts.read_text())
        self.assertEqual(row["judged_words"], 7)
        self.assertGreater(row["raw_words"], row["judged_words"])

    def test_blind_preserves_near_miss_and_fields_after_removed_section(self) -> None:
        text = "Concrete rewrite: A remembered line is optional.\nRewrite check: secret\nSlop tells: Keep this.\n"
        self.assertEqual(
            run_evals.strip_template_fields(text, ["Rewrite check"]),
            "Concrete rewrite: A remembered line is optional.\nSlop tells: Keep this.\n",
        )

    def test_blind_rejects_key_in_judge_directory(self) -> None:
        src = self.tmp / "candidate.md"
        src.write_text("Hello")
        dest = self.tmp / "judge"
        result = run_script(
            "scripts/run_evals.py",
            "blind",
            src,
            "--out-dir",
            dest,
            "--key-out",
            dest / "key.json",
            "--counts-out",
            self.tmp / "counts.jsonl",
        )
        self.assertNotEqual(result.returncode, 0)

    def test_blind_handles_markdown_field_labels(self) -> None:
        text = "**Concrete rewrite:** Keep this.\n- **Rewrite check**: secret\n- **Remembered line:** secret\n"
        self.assertEqual(
            run_evals.strip_template_fields(text, ["Rewrite check", "Remembered line"]),
            "**Concrete rewrite:** Keep this.\n",
        )

    def test_blind_removes_labeled_bullets_inside_template_section(self) -> None:
        raw = "Concrete rewrite: Keep this.\nRewrite check:\n- Invented facts: none\n- Cadence: passes\nSlop tells: Keep this too.\n"
        self.assertEqual(
            run_evals.strip_template_fields(raw, ["Rewrite check"]),
            "Concrete rewrite: Keep this.\nSlop tells: Keep this too.\n",
        )

    def test_join_preserves_family_and_length_metadata(self) -> None:
        common = {
            "id": "x",
            "case_id": "case-x",
            "family": "family-x",
            "split": "holdout",
        }
        a = write_jsonl(
            self.tmp / "a.jsonl", [{**common, "score": 0.5, "word_count": 20}]
        )
        b = write_jsonl(
            self.tmp / "b.jsonl", [{**common, "score": 1, "word_count": 25}]
        )
        result = run_script("scripts/run_evals.py", "join", "--before", a, "--after", b)
        self.assertEqual(result.returncode, 0, result.stderr)
        row = json.loads(result.stdout)
        self.assertEqual(
            (row["family"], row["case_id"], row["before_words"], row["after_words"]),
            ("family-x", "case-x", 20, 25),
        )

    def test_join_rejects_duplicate_score_ids(self) -> None:
        row = {"id": "x", "split": "tune", "score": 1}
        a = write_jsonl(self.tmp / "a.jsonl", [row, row])
        b = write_jsonl(self.tmp / "b.jsonl", [row])
        result = run_script("scripts/run_evals.py", "join", "--before", a, "--after", b)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("duplicate id", result.stderr)

    def test_join_rejects_differing_split_or_cluster(self) -> None:
        row = {
            "id": "x",
            "split": "tune",
            "score": 1,
            "family": "a",
            "pair_id": "p",
            "fact_condition": "supplied",
        }
        a = write_jsonl(self.tmp / "a.jsonl", [row])
        for change in [
            {"split": "holdout"},
            {"family": "b"},
            {"pair_id": "other"},
            {"fact_condition": "no_additional_facts"},
        ]:
            b = write_jsonl(self.tmp / "b.jsonl", [{**row, **change}])
            with self.subTest(change=change):
                result = run_script(
                    "scripts/run_evals.py", "join", "--before", a, "--after", b
                )
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("differs", result.stderr)

    def test_grade_rejects_duplicate_ids_across_files(self) -> None:
        a = write_jsonl(self.tmp / "a.jsonl", [judgment("x", [True, True])])
        b = write_jsonl(self.tmp / "b.jsonl", [judgment("x", [False, True])])
        result = run_script("scripts/run_evals.py", "grade", a, b)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("duplicate id", result.stderr)

    def test_grade_fails_on_a_missing_judgment_file(self) -> None:
        # A typo in one path must not silently shrink the scored set.
        present = write_jsonl(self.tmp / "a.jsonl", [judgment("x", [True, True])])
        result = run_script(
            "scripts/run_evals.py", "grade", present, self.tmp / "missing.jsonl"
        )
        self.assertNotEqual(result.returncode, 0, result.stdout)
        self.assertIn("missing.jsonl", result.stderr)

    def test_grade_accepts_an_existing_path_with_glob_characters(self) -> None:
        literal = write_jsonl(self.tmp / "run[1].jsonl", [judgment("x", [True, False])])
        result = run_script("scripts/run_evals.py", "grade", literal)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)["score"], 0.5)

    def test_grade_split_filter(self) -> None:
        path = write_jsonl(
            self.tmp / "j.jsonl",
            [judgment("t", [True, True], split="tune"), judgment("h", [True, False])],
        )
        result = run_script("scripts/run_evals.py", "grade", path, "--split", "holdout")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(
            [json.loads(line)["id"] for line in result.stdout.splitlines()], ["h"]
        )

    def test_grade_expands_globs(self) -> None:
        write_jsonl(self.tmp / "j1.jsonl", [judgment("x", [True, True])])
        write_jsonl(self.tmp / "j2.jsonl", [judgment("y", [True, False])])
        result = run_script("scripts/run_evals.py", "grade", self.tmp / "j*.jsonl")
        self.assertEqual(result.returncode, 0, result.stderr)
        scores = {
            json.loads(line)["id"]: json.loads(line)["score"]
            for line in result.stdout.splitlines()
        }
        self.assertEqual(scores, {"x": 1.0, "y": 0.5})

    def test_grade_join_and_gate_round_trip(self) -> None:
        # Before: every holdout case passes 1 of 2 assertions. After: 2 of 2.
        ids = [f"case-{i}" for i in range(10)]
        before_j = write_jsonl(
            self.tmp / "before-j.jsonl", [judgment(i, [True, False]) for i in ids]
        )
        after_j = write_jsonl(
            self.tmp / "after-j.jsonl", [judgment(i, [True, True]) for i in ids]
        )
        before, after, delta = (
            self.tmp / "before.jsonl",
            self.tmp / "after.jsonl",
            self.tmp / "delta.jsonl",
        )
        for src, dst in ((before_j, before), (after_j, after)):
            graded = run_script("scripts/run_evals.py", "grade", src, "--out", dst)
            self.assertEqual(graded.returncode, 0, graded.stderr)
        joined = run_script(
            "scripts/run_evals.py",
            "join",
            "--before",
            before,
            "--after",
            after,
            "--out",
            delta,
        )
        self.assertEqual(joined.returncode, 0, joined.stderr)
        rows = [json.loads(line) for line in delta.read_text().splitlines()]
        self.assertEqual(
            {(r["id"], r["before"], r["after"]) for r in rows},
            {(i, 0.5, 1.0) for i in ids},
        )
        self.assertEqual(
            run_script("scripts/score_delta.py", delta, "--holdout-only").returncode, 0
        )
        # The same files in reverse are a regression and must not pass the gate.
        reverse = self.tmp / "reverse.jsonl"
        rejoined = run_script(
            "scripts/run_evals.py",
            "join",
            "--before",
            after,
            "--after",
            before,
            "--out",
            reverse,
        )
        self.assertEqual(rejoined.returncode, 0, rejoined.stderr)
        self.assertEqual(
            run_script("scripts/score_delta.py", reverse, "--holdout-only").returncode,
            1,
        )

    def test_join_rejects_missing_slots_unless_explicitly_inspecting(self) -> None:
        shared = {"id": "x", "split": "holdout", "score": 1}
        extra = {"id": "missing", "split": "holdout", "score": 0}
        for left, right in [([shared, extra], [shared]), ([shared], [shared, extra])]:
            with self.subTest(left=left):
                a = write_jsonl(self.tmp / "a.jsonl", left)
                b = write_jsonl(self.tmp / "b.jsonl", right)
                result = run_script(
                    "scripts/run_evals.py", "join", "--before", a, "--after", b
                )
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("case sets differ", result.stderr)
                self.assertEqual(result.stdout, "")
                inspected = run_script(
                    "scripts/run_evals.py",
                    "join",
                    "--before",
                    a,
                    "--after",
                    b,
                    "--allow-partial",
                )
                self.assertEqual(inspected.returncode, 0, inspected.stderr)
                self.assertIn("warning", inspected.stderr)
                self.assertEqual(json.loads(inspected.stdout)["id"], "x")

    def test_join_requires_shared_ids(self) -> None:
        a = write_jsonl(
            self.tmp / "a.jsonl", [{"id": "x", "split": "tune", "score": 1}]
        )
        b = write_jsonl(
            self.tmp / "b.jsonl", [{"id": "y", "split": "tune", "score": 1}]
        )
        result = run_script("scripts/run_evals.py", "join", "--before", a, "--after", b)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("no shared ids", result.stderr)


class WorklistGrade(unittest.TestCase):
    def setUp(self) -> None:
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.tmp = Path(tmp.name)
        cases = [
            {
                "id": "x",
                "split": "holdout",
                "prompt": "Rewrite the draft.",
                "facts": [],
                "assertions": ["fidelity", "task fulfilled"],
                "graded_dimensions": [
                    {"name": "fidelity", "scale": "1-5", "rubric": "Grounded."}
                ],
            },
            {
                "id": "t",
                "split": "tune",
                "prompt": "Review the draft.",
                "facts": ["The queue retries after ten seconds."],
                "assertions": ["fidelity", "task fulfilled"],
            },
        ]
        src = self.tmp / "evals.json"
        src.write_text(json.dumps({"evals": cases}))
        self.worklist = self.tmp / "judge.json"
        result = run_script(
            "scripts/run_evals.py",
            "prepare",
            src,
            "--out",
            self.tmp / "apply.json",
            "--judge-out",
            self.worklist,
        )
        self.assertEqual(result.returncode, 0, result.stderr)

    def record(self, cid: str = "x") -> dict:
        r = judgment(cid, [True, False], split="holdout" if cid == "x" else "tune")
        r.update(
            pair_id=cid,
            fact_condition="no_additional_facts" if cid == "x" else "supplied",
        )
        if cid == "x":
            r["graded_dimensions"] = [
                {"name": "fidelity", "score": 5, "evidence": "quote"}
            ]
        return r

    def grade(self, records: list, *flags):
        src = write_jsonl(self.tmp / "judgments.jsonl", records)
        return run_script(
            "scripts/run_evals.py", "grade", src, "--worklist", self.worklist, *flags
        )

    def test_complete_worklist_scores_with_reordered_assertions_and_trial_ids(
        self,
    ) -> None:
        x = self.record()
        x.update(id="x-trial-1", case_id="x")
        x["assertions"].reverse()
        result = self.grade([self.record("t"), x], "--include-graded")
        self.assertEqual(result.returncode, 0, result.stderr)
        scores = {r["id"]: r for r in map(json.loads, result.stdout.splitlines())}
        self.assertEqual(set(scores), {"t", "x-trial-1"})
        self.assertEqual(scores["x-trial-1"]["score"], 0.6667)
        self.assertEqual(scores["x-trial-1"]["pair_id"], "x")
        self.assertEqual(scores["x-trial-1"]["case_id"], "x")

    def test_incomplete_or_ambiguous_judgments_fail_before_writing_scores(self) -> None:
        changes = {
            "omitted assertion": {
                "assertions": [{"index": 1, "pass": True, "evidence": "q"}]
            },
            "duplicate index": {
                "assertions": [{"index": 1, "pass": True, "evidence": "q"}] * 2
            },
            "boolean index": {
                "assertions": [
                    {"index": True, "pass": True, "evidence": "q"},
                    {"index": 2, "pass": True, "evidence": "q"},
                ]
            },
            "no dimension": {"graded_dimensions": []},
            "wrong dimension": {
                "graded_dimensions": [{"name": "invented", "score": 5, "evidence": "q"}]
            },
            "duplicate dimension": {
                "graded_dimensions": [{"name": "fidelity", "score": 5, "evidence": "q"}]
                * 2
            },
            "blank evidence": {
                "assertions": [
                    {"index": 1, "pass": True, "evidence": " "},
                    {"index": 2, "pass": True, "evidence": "q"},
                ]
            },
            "blank dimension evidence": {
                "graded_dimensions": [{"name": "fidelity", "score": 5, "evidence": ""}]
            },
            "wrong split": {"split": "tune"},
            "wrong suite": {"suite": "other.json"},
            "wrong pair": {"pair_id": "other"},
            "wrong condition": {"fact_condition": "supplied"},
            "missing pair": {"pair_id": None},
            "unknown case": {"case_id": "unknown"},
            "invalid slot id": {"id": []},
            "null assertions": {"assertions": None},
            "null dimensions": {"graded_dimensions": None},
        }
        out = self.tmp / "scores.jsonl"
        for label, change in changes.items():
            with self.subTest(label):
                result = self.grade(
                    [self.record("t"), {**self.record(), **change}], "--out", out
                )
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("FAIL:", result.stderr)
                self.assertNotIn("Traceback", result.stderr)
                self.assertFalse(out.exists())

    def test_missing_case_fails_but_split_scoped_worklist_coverage_passes(self) -> None:
        result = self.grade([self.record()])
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("missing judgments", result.stderr)
        self.assertEqual(result.stdout, "")
        scoped = self.grade([self.record()], "--split", "holdout")
        self.assertEqual(scoped.returncode, 0, scoped.stderr)
        self.assertEqual(json.loads(scoped.stdout)["score"], 0.5)

    def test_rejects_non_object_judgments_and_unrequested_dimensions(self) -> None:
        for record in [
            [],
            None,
            {
                **self.record("t"),
                "graded_dimensions": [
                    {"name": "fidelity", "score": 5, "evidence": "quote"}
                ],
            },
        ]:
            with self.subTest(record=record):
                result = self.grade([record])
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("FAIL:", result.stderr)
                self.assertNotIn("Traceback", result.stderr)

    def test_worklist_rejects_wrong_role_duplicate_cases_and_invalid_schema(
        self,
    ) -> None:
        original = json.loads(self.worklist.read_text())
        invalid = [
            {**original, "role": "apply"},
            {**original, "units": original["units"] * 2},
            {**original, "units": []},
            {**original, "units": [{**original["units"][0], "assertions": []}]},
            {
                **original,
                "units": [
                    {**original["units"][0], "graded_dimensions": [{"name": ""}]}
                ],
            },
        ]
        for work in invalid:
            with self.subTest(work=work):
                self.worklist.write_text(json.dumps(work))
                result = self.grade([self.record()])
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("FAIL:", result.stderr)
                self.assertNotIn("Traceback", result.stderr)


if __name__ == "__main__":
    unittest.main()
