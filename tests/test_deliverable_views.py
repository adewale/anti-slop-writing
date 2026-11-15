"""Offline structured views: exact-source spans, role preservation, and honest limits."""
from __future__ import annotations

import copy
import hashlib
import json
import tarfile
import tempfile
import unittest
from pathlib import Path

from _support import ROOT, load_script, run_script

views = load_script("scripts/deliverable_views.py")
FIXTURES = ROOT / "evals/fixtures/structured-deliverables"


def ref(source: str, text: str, start: int = 0) -> dict:
    begin = source.index(text, start)
    return {"start": begin, "end": begin + len(text), "text": text}


def annotation(source: str, items: list) -> dict:
    return {"version": 1, "source_sha256": hashlib.sha256(source.encode()).hexdigest(),
            "items": items, "unresolved": []}


def item(source: str, text: str, role="prose", identity="d1", qualifications=()) -> dict:
    return {"id": identity, "role": role, "content": ref(source, text),
            "qualifications": [ref(source, text) for text in qualifications]}


class Contract(unittest.TestCase):
    def test_roles_and_qualifications_are_not_concatenated_into_manuscript(self) -> None:
        source = "Main text.\nAsk author: Which batch?\nFallback: cut the line."
        spec = annotation(source, [item(source, "Main text."),
            item(source, "Which batch?", "author_question", "d2"),
            item(source, "cut the line.", "conditional_alternative", "d3", ["Fallback:"])])
        result = views.build_views(source, spec)
        self.assertEqual(result["status"], "unvalidated_prototype")
        self.assertEqual(result["views"]["full"]["response"], source)
        emitted = result["views"]["deliverable"]["items"]
        self.assertEqual([r["role"] for r in emitted], ["prose", "author_question", "conditional_alternative"])
        self.assertEqual(emitted[2]["qualifications"], [{"position": "before", "text": "Fallback:"}])
        self.assertEqual(emitted[0]["text"], "Main text.")
        self.assertNotIn("Which batch?", emitted[0]["text"])
        self.assertEqual(spec, annotation(source, [item(source, "Main text."),
            item(source, "Which batch?", "author_question", "d2"),
            item(source, "cut the line.", "conditional_alternative", "d3", ["Fallback:"])]))

    def test_qualification_in_a_self_check_survives_in_both_views(self) -> None:
        source = "Concrete rewrite: It resumes.\nRewrite check: Use only if confirmed."
        result = views.build_views(source, annotation(source, [
            item(source, "It resumes.", "conditional_alternative", qualifications=["Use only if confirmed."])]))
        self.assertIn("Rewrite check: Use only if confirmed.", result["views"]["full"]["response"])
        self.assertEqual(result["views"]["deliverable"]["items"][0]["qualifications"],
                         [{"position": "after", "text": "Use only if confirmed."}])

    def test_conditional_without_qualification_is_rejected(self) -> None:
        source = "It resumes."
        with self.assertRaisesRegex(ValueError, "qualification"):
            views.build_views(source, annotation(source, [item(source, source, "conditional_alternative")]))

    def test_empty_deliverable_is_an_outcome_not_a_missing_record(self) -> None:
        source = "Diagnosis only."
        result = views.build_views(source, annotation(source, []))
        self.assertEqual(result["views"]["deliverable"]["items"], [])
        self.assertEqual(result["omitted_spans"], [ref(source, source)])
        self.assertEqual(result["status"], "unvalidated_prototype")

    def test_unknown_roles_are_not_guessed(self) -> None:
        source = "Text."
        with self.assertRaisesRegex(ValueError, "role"):
            views.build_views(source, annotation(source, [item(source, source, "mixed")]))

    def test_cut_or_keep_decision_has_its_own_role(self) -> None:
        source = "Keep the sentence as it is."
        result = views.build_views(source, annotation(source, [item(source, source, "decision")]))
        self.assertEqual(result["views"]["deliverable"]["items"][0]["role"], "decision")

    def test_unresolved_material_blocks_view_construction(self) -> None:
        source = "Maybe optional."
        spec = annotation(source, []) | {"unresolved": [ref(source, source)]}
        with self.assertRaisesRegex(ValueError, "unresolved"):
            views.build_views(source, spec)

    def test_unknown_metadata_and_false_human_approval_are_rejected(self) -> None:
        source = "Text."
        for extra in ({"human_approved": True}, {"arm": "skill"}):
            with self.subTest(extra=extra), self.assertRaises(ValueError):
                views.build_views(source, annotation(source, [item(source, source)]) | extra)
        with self.assertRaises(ValueError):
            views.build_views(source, annotation(source, [item(source, source) | {"rewrite": "new words"}]))

    def test_malformed_types_and_versions_are_rejected(self) -> None:
        source = "Text."
        base = annotation(source, [item(source, source)])
        for key, value in [("version", True), ("version", 1.0), ("version", 2),
                           ("items", None), ("unresolved", None)]:
            with self.subTest(key=key, value=value), self.assertRaises((TypeError, ValueError)):
                views.build_views(source, base | {key: value})
        with self.assertRaises(TypeError):
            views.build_views(None, base)
        with self.assertRaises(ValueError):
            views.build_views(source, base | {"items": [base["items"][0] | {"content": {}}]})
        with self.assertRaises(TypeError):
            views.build_views(source, base | {"items": [base["items"][0] | {"qualifications": None}]})

    def test_changed_source_or_paraphrased_span_is_rejected(self) -> None:
        source = "The job stops."
        spec = annotation(source, [item(source, source)])
        with self.assertRaisesRegex(ValueError, "hash"):
            views.build_views(source + " Changed.", spec)
        spec["items"][0]["content"]["text"] = "The job halts."
        with self.assertRaisesRegex(ValueError, "exact"):
            views.build_views(source, spec)

    def test_invalid_ranges_and_boolean_offsets_are_rejected(self) -> None:
        source = "Text."
        for start, end in [(-1, 2), (0, 99), (2, 2), (3, 1), (False, 5), (0, True)]:
            spec = annotation(source, [item(source, source)])
            spec["items"][0]["content"].update(start=start, end=end)
            with self.subTest(start=start, end=end), self.assertRaises(ValueError):
                views.build_views(source, spec)

    def test_duplicate_ids_reordered_items_and_overlaps_are_rejected(self) -> None:
        source = "First. Second."
        good = [item(source, "First."), item(source, "Second.", identity="d2")]
        bad = [good[0], good[1] | {"id": "d1"}]
        for items in [bad, list(reversed(good)), [good[0], item(source, source, identity="d2")]]:
            with self.subTest(items=items), self.assertRaises(ValueError):
                views.build_views(source, annotation(source, items))

    def test_qualification_cannot_overlap_content(self) -> None:
        source = "If confirmed, ship."
        spec = annotation(source, [item(source, source, "conditional_alternative", qualifications=["If confirmed"])])
        with self.assertRaisesRegex(ValueError, "overlap"):
            views.build_views(source, spec)

    def test_shared_qualification_keeps_explicit_scope_on_each_item(self) -> None:
        source = "If confirmed:\nFirst.\nSecond."
        spec = annotation(source, [item(source, text, "conditional_alternative", identity=f"d{i}",
                                       qualifications=["If confirmed:"])
                                  for i, text in enumerate(["First.", "Second."], 1)])
        result = views.build_views(source, spec)
        self.assertEqual([x["qualifications"] for x in result["views"]["deliverable"]["items"]],
                         [[{"position": "before", "text": "If confirmed:"}]] * 2)

    def test_overlapping_or_reordered_qualifications_are_rejected(self) -> None:
        source = "If confirmed, if needed, ship."
        for notes in [["If confirmed", "confirmed, if needed"], ["if needed", "If confirmed"]]:
            spec = annotation(source, [item(source, "ship.", "conditional_alternative", qualifications=notes)])
            with self.subTest(notes=notes), self.assertRaisesRegex(ValueError, "overlap|source order"):
                views.build_views(source, spec)
        spec = annotation(source, [item(source, "If confirmed"),
            item(source, "ship.", "conditional_alternative", "d2", ["If confirmed"])])
        with self.assertRaisesRegex(ValueError, "another item's content"):
            views.build_views(source, spec)

    def test_label_words_and_unicode_whitespace_are_preserved(self) -> None:
        source = "🙂\r\nThe verdict: keep  café\topen.\r\n"
        body = "The verdict: keep  café\topen."
        result = views.build_views(source, annotation(source, [item(source, body)]))
        self.assertEqual(result["views"]["full"]["response"], source)
        self.assertEqual(result["views"]["deliverable"]["items"][0]["text"], body)

    def test_exact_but_misleading_annotation_never_becomes_a_faithfulness_pass(self) -> None:
        source = "Do not ship."
        result = views.build_views(source, annotation(source, [item(source, "ship.")]))
        self.assertEqual(result["views"]["deliverable"]["items"][0]["text"], "ship.")
        self.assertEqual(result["omitted_spans"], [ref(source, "Do not ")])
        self.assertEqual(result["status"], "unvalidated_prototype")
        self.assertNotIn("passed", result)
        self.assertNotIn("human_approved", result)

    def test_exhaustive_small_spans_conserve_source_and_never_claim_semantic_validation(self) -> None:
        for source in ["abc", "é🙂x", "a\r\nb", "not x"]:
            for start in range(len(source)):
                for end in range(start + 1, len(source) + 1):
                    text = source[start:end]
                    if not text.strip():
                        continue
                    spec = annotation(source, [{"id": "d1", "role": "prose", "content": {
                        "start": start, "end": end, "text": text}, "qualifications": []}])
                    result = views.build_views(source, spec)
                    pieces = [spec["items"][0]["content"], *result["omitted_spans"]]
                    self.assertEqual("".join(s["text"] for s in sorted(pieces, key=lambda s: s["start"])), source)
                    self.assertEqual(result["views"]["deliverable"]["items"][0]["text"], text)
                    self.assertEqual(result["status"], "unvalidated_prototype")


class RetainedFixtures(unittest.TestCase):
    def test_sources_match_the_original_frozen_archive_not_new_generations(self) -> None:
        cases = [json.loads(p.read_text()) for p in sorted(FIXTURES.glob("*.json"))]
        self.assertEqual(len(cases), 3)
        archive_path = ROOT / cases[0]["provenance"]["archive"]
        self.assertEqual(hashlib.sha256(archive_path.read_bytes()).hexdigest(), cases[0]["provenance"]["archive_sha256"])
        with tarfile.open(archive_path) as archive:
            for case in cases:
                record = json.loads(archive.extractfile(case["provenance"]["archive_member"]).read())
                self.assertEqual(record["output"], case["source"])

    def test_proposed_annotations_match_explicit_policy_examples(self) -> None:
        paths = sorted(FIXTURES.glob("*.json"))
        self.assertEqual(len(paths), 3)
        for path in paths:
            with self.subTest(path=path):
                case = json.loads(path.read_text())
                self.assertEqual(case["split"], "tune")
                self.assertEqual(case["annotation_origin"], "model_proposed_not_human_adjudication")
                source, spec = case["source"], case["annotation"]
                result = views.build_views(source, spec)
                self.assertEqual(result["views"]["full"]["response"], source)
                self.assertEqual(result["views"]["deliverable"]["items"], case["expected_items"])
                self.assertEqual(result["status"], "unvalidated_prototype")
                if case["id"] == "conditional-remembered-line":
                    roles = [r["role"] for r in result["views"]["deliverable"]["items"]]
                    self.assertEqual(roles, ["prose", "author_question", "conditional_alternative"])
                    self.assertIn("only once the author confirms", result["views"]["deliverable"]["items"][2]["qualifications"][0]["text"])
                if case["id"] == "separate-remembered-line":
                    self.assertEqual(len(result["views"]["deliverable"]["items"]), 1)
                    omitted = "".join(s["text"] for s in result["omitted_spans"])
                    self.assertIn("Remembered line:", omitted)

    def test_cli_rejects_duplicate_keys_and_bad_types_without_output(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "bad.json"
            for text in ['{"source":"x","source":"y","annotation":{}}',
                         '{"source":null,"annotation":{}}', '[]']:
                path.write_text(text)
                result = run_script("scripts/deliverable_views.py", path)
                self.assertEqual(result.returncode, 2)
                self.assertEqual(result.stdout, "")
                self.assertIn("error:", result.stderr)

    def test_cli_builds_views_and_fails_without_writing_partial_output(self) -> None:
        fixture = FIXTURES / "conditional-remembered-line.json"
        good = run_script("scripts/deliverable_views.py", fixture)
        self.assertEqual(good.returncode, 0, good.stderr)
        result = json.loads(good.stdout)
        self.assertEqual(result["status"], "unvalidated_prototype")
        with tempfile.TemporaryDirectory() as temp:
            path, out = Path(temp) / "input.json", Path(temp) / "views.json"
            case = json.loads(fixture.read_text())
            broken = copy.deepcopy(case)
            broken["annotation"]["items"][2]["qualifications"] = []
            path.write_text(json.dumps(broken))
            bad = run_script("scripts/deliverable_views.py", path, "--out", out)
            self.assertEqual(bad.returncode, 2)
            self.assertIn("qualification", bad.stderr)
            self.assertFalse(out.exists())
            path.write_text(json.dumps(case))
            saved = run_script("scripts/deliverable_views.py", path, "--out", out)
            self.assertEqual(saved.returncode, 0, saved.stderr)
            self.assertEqual(json.loads(out.read_text()), result)
            again = run_script("scripts/deliverable_views.py", path, "--out", out)
            self.assertEqual(again.returncode, 2)
            self.assertEqual(json.loads(out.read_text()), result)


if __name__ == "__main__":
    unittest.main()
