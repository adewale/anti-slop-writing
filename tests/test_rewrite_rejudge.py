"""scripts/rewrite_rejudge.py: scope, verbatim extraction, blinding, and analysis.

Model calls are replaced by a deterministic fake so the whole pipeline runs
offline. The fake judge rewards visible critique, so the expected result is a
skill advantage in the full view that disappears in the deliverable view.
"""

from __future__ import annotations

import json
import re
import tempfile
import unittest
from pathlib import Path

from _support import load_script

rr = load_script("scripts/rewrite_rejudge.py")
sb = rr.sb

REWRITE = "The job retries twice and then stops."


def case(cid: str, task: str, family: str) -> dict:
    return {"id": cid, "task": task, "group": "review-rewrite", "family": family,
            "split": "tune", "fact_condition": "no_additional_facts",
            "expected_output": "A plain rewrite.", "assertions": ["a", "b"]}


def build_baseline(root: Path, families: int = 6) -> Path:
    cases = [case(f"c{i}", f"Rewrite this sentence: The job is robust {i}.", f"fam{i}")
             for i in range(families)]
    cases.append(case("review-only", "Review this sentence: The job is robust.", "famR"))
    slots = []
    for c in cases:
        for model in sb.APPLY_MODELS:
            for arm in rr.ARMS:
                for trial in range(1, sb.TRIALS + 1):
                    sid = f"{c['id']}-{model}-{arm}-{trial}"
                    out = (f"Verdict: revise\nCRITIQUE: 'robust' names no mechanism.\n"
                           f"Concrete rewrite: {REWRITE}\nRemembered line: name it." if arm == "skill"
                           else REWRITE)
                    blinded = sb.strip_template_fields(out, ["Rewrite check", "Remembered line"])
                    path = root / "apply" / model / sid
                    path.mkdir(parents=True)
                    (path / "complete.json").write_text(json.dumps({"output": out, "blinded": blinded}))
                    slots.append({"id": sid, "case_id": c["id"], "model": model, "arm": arm,
                                  "trial": trial, "group": "review-rewrite"})
    (root / "cases.json").write_text(json.dumps(cases))
    (root / "manifest.json").write_text(json.dumps({"slots": slots}))
    return root


def fake_invoke(broken: set[str] = frozenset()):
    def invoke(model, prompt, effort, attempt):
        attempt.mkdir(parents=True, exist_ok=False)
        if prompt.startswith("You are copying text"):
            eid = re.search(r'\{"id": "([0-9a-f]{24})"', prompt)[1]
            if eid in broken:
                return json.dumps({"id": eid, "disposition": "rewrite", "spans": ["Not in the response."]}), {}
            return json.dumps({"id": eid, "disposition": "rewrite", "spans": [REWRITE]}), {}
        jid = re.search(r'with id "([0-9a-f]{24})"', prompt)[1]
        response = prompt.split("\n\nRESPONSE:\n", 1)[1]
        task = 5 if "CRITIQUE" in response else 3
        dims = [{"name": "factual_fidelity", "score": 5, "evidence": "q"},
                {"name": "task_fulfillment", "score": task, "evidence": "q"},
                {"name": "rewrite_quality", "score": 4, "evidence": "q"}]
        return json.dumps({"id": jid, "dimensions": dims}), {}
    return invoke


class Scope(unittest.TestCase):
    def test_rewrite_tasks_are_in_scope(self) -> None:
        for task in ["Rewrite this conclusion: X", "Review and rewrite this line: X",
                     "Review and tighten this passage.", "Turn this list into prose:\n\nX",
                     "Revise this sentence: X"]:
            self.assertTrue(rr.in_scope(case("x", task, "f")), task)

    def test_review_only_and_critique_format_tasks_are_out(self) -> None:
        for task in ["Review this sentence: X", "Review the cadence: X",
                     "Review this paragraph using the Critique output format. Then rewrite it.",
                     "Apply the anti-slop-writing skill to the thread, then rewrite it."]:
            self.assertFalse(rr.in_scope(case("x", task, "f")), task)

    def test_rewrite_word_after_the_instruction_does_not_count(self) -> None:
        # Near-miss: "rewrite" inside the quoted source text is not the instruction.
        self.assertFalse(rr.in_scope(case("x", "Review this line: We will rewrite the parser.", "f")))


class Extraction(unittest.TestCase):
    response = "Verdict: revise\nThe claim is vague.\nConcrete rewrite: The job retries\n  twice.\nWhy: it names the mechanism."

    def check(self, spans, disposition="rewrite", eid="e1"):
        return rr.validate_extraction({"id": eid, "disposition": disposition, "spans": spans}, self.response, "e1")

    def test_verbatim_span_passes(self) -> None:
        self.assertEqual(self.check(["The claim is vague."]), ["The claim is vague."])

    def test_whitespace_difference_passes(self) -> None:
        self.assertEqual(self.check(["The job retries twice."]), ["The job retries twice."])

    def test_paraphrase_fails(self) -> None:
        with self.assertRaisesRegex(ValueError, "verbatim"):
            self.check(["The job retries two times."])

    def test_out_of_order_spans_fail(self) -> None:
        with self.assertRaisesRegex(ValueError, "in-order"):
            self.check(["The job retries twice.", "The claim is vague."])

    def test_none_with_spans_and_wrong_id_fail(self) -> None:
        with self.assertRaisesRegex(ValueError, "no spans"):
            self.check(["The claim is vague."], disposition="none")
        with self.assertRaisesRegex(ValueError, "wrong extraction id"):
            self.check(["The claim is vague."], eid="other")

    def test_render_strips_template_labels_but_not_prose(self) -> None:
        self.assertEqual(rr.render(["Concrete rewrite: The job retries."]), "The job retries.\n")
        self.assertEqual(rr.render(["**Ask author:** Which retries?"]), "Which retries?\n")
        # Near-miss: a label word inside a sentence stays.
        self.assertEqual(rr.render(["The verdict: keep the line."]), "The verdict: keep the line.\n")


class Prompts(unittest.TestCase):
    def test_judge_prompt_carries_no_assertions_or_arm(self) -> None:
        c = case("x", "Rewrite this: X", "f")
        c["assertions"] = ["SECRET_ASSERTION"]
        prompt = rr.judge_prompt(c, "RESPONSE_TEXT", "j1")
        self.assertIn("RESPONSE_TEXT", prompt)
        self.assertNotIn("SECRET_ASSERTION", prompt)
        self.assertNotIn("no-skill", prompt)
        self.assertNotIn("SKILL PACKAGE", prompt)

    def test_judgment_validation(self) -> None:
        dims = [{"name": n, "score": 3, "evidence": "q"} for n in rr.DIMENSIONS]
        self.assertEqual(set(rr.validate_judgment({"id": "j", "dimensions": dims}, "j")), set(rr.DIMENSIONS))
        with self.assertRaises(ValueError):
            rr.validate_judgment({"id": "j", "dimensions": dims[:2]}, "j")
        with self.assertRaises(ValueError):
            rr.validate_judgment({"id": "j", "dimensions": [dims[0] | {"score": 6}, *dims[1:]]}, "j")


class Pipeline(unittest.TestCase):
    def setUp(self) -> None:
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name)
        self.baseline = build_baseline(self.root / "baseline")
        self.dest = self.root / "study"
        self.original = sb.invoke
        self.addCleanup(setattr, sb, "invoke", self.original)

    def run_all(self, broken=frozenset()):
        manifest = rr.prepare(self.baseline, self.dest)
        sb.invoke = fake_invoke(broken)
        rr.extract(self.baseline, self.dest, workers=4)
        rr.judge(self.baseline, self.dest, workers=4)
        return manifest, rr.analyze(self.baseline, self.dest)

    def test_critique_driven_advantage_is_attributed_to_the_critique(self) -> None:
        manifest, summary = self.run_all()
        self.assertNotIn("review-only", manifest["scope"])
        self.assertEqual(len(manifest["outputs"]), 6 * 2 * 2 * sb.TRIALS)
        self.assertEqual(summary["excluded_outputs"], 0)
        reports = json.loads((self.dest / "comparisons.json").read_text())
        task = next(r for r in reports if r["dimension"] == "task_fulfillment"
                    and r["split"] == "all" and r["apply_model"] == "sonnet" and r["judge"] == "opus")
        self.assertAlmostEqual(task["full"]["delta"], 0.5)
        self.assertAlmostEqual(task["deliverable"]["delta"], 0.0)
        self.assertAlmostEqual(task["critique_share"]["delta"], 0.5)
        self.assertEqual(summary["extractor_reliability"]["exact_rate"], 1.0)

    def test_failed_extraction_excludes_the_case_from_both_views(self) -> None:
        manifest = rr.prepare(self.baseline, self.dest)
        target = next(o for o in manifest["outputs"] if o["case_id"] == "c0" and o["model"] == "sol")
        (self.dest / "manifest.json").unlink()
        _, summary = self.run_all(broken={target["extraction_id"]})
        self.assertEqual(summary["excluded_outputs"], 1)
        scores = json.loads((self.dest / "scores.json").read_text())
        self.assertFalse(any(s["case_id"] == "c0" and s["model"] == "sol" for s in scores))
        self.assertTrue(any(s["case_id"] == "c0" and s["model"] == "sonnet" for s in scores))

    def test_changed_baseline_is_refused(self) -> None:
        rr.prepare(self.baseline, self.dest)
        cases = json.loads((self.baseline / "cases.json").read_text())
        cases[0]["task"] += " Edited."
        (self.baseline / "cases.json").write_text(json.dumps(cases))
        with self.assertRaisesRegex(ValueError, "cases differ"):
            rr.extract(self.baseline, self.dest, workers=1)

    def test_prepare_refuses_to_replace_a_frozen_manifest(self) -> None:
        rr.prepare(self.baseline, self.dest)
        with self.assertRaisesRegex(ValueError, "refusing"):
            rr.prepare(self.baseline, self.dest)


if __name__ == "__main__":
    unittest.main()
