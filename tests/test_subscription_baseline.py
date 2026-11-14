"""Subscription study boundaries; all payloads here are synthetic, not model trials."""

from __future__ import annotations

import copy
import json
import unittest

from _support import load_script

study = load_script("scripts/subscription_baseline.py")


class Audit(unittest.TestCase):
    def test_accepts_complete_openai_text_and_rejects_tools_or_model_drift(self):
        good = {
            "result": {
                "model": "gpt-test",
                "stopReason": "stop",
                "usage": {},
                "content": [{"type": "text", "text": "answer"}],
            }
        }
        self.assertEqual(
            study.audit_response("openai", json.dumps(good), "gpt-test"), ("answer", {})
        )
        for change in [
            {"model": "other"},
            {"stopReason": "length"},
            {"content": [{"type": "toolCall", "name": "read"}]},
            {"content": [{"type": "text", "text": " "}]},
        ]:
            with self.subTest(change=change), self.assertRaises(ValueError):
                study.audit_response(
                    "openai",
                    json.dumps({"result": {**good["result"], **change}}),
                    "gpt-test",
                )

    def test_claude_audit_checks_init_and_complete_model_usage(self):
        events = [
            {
                "type": "system",
                "subtype": "init",
                "tools": [],
                "skills": [],
                "mcp_servers": [],
            },
            {
                "type": "result",
                "subtype": "success",
                "is_error": False,
                "result": "answer",
                "modelUsage": {"claude-test": {}},
                "permission_denials": [],
                "num_turns": 1,
            },
        ]
        encode = lambda es: "\n".join(json.dumps(e) for e in es)
        self.assertEqual(
            study.audit_response("claude", encode(events), "claude-test")[0], "answer"
        )
        for extra in [
            {"type": "system", "subtype": "init", "tools": ["Read"]},
            {
                "type": "assistant",
                "message": {"content": [{"type": "tool_use", "name": "Read"}]},
            },
            events[-1],
        ]:
            with self.subTest(extra=extra), self.assertRaises(ValueError):
                study.audit_response("claude", encode([*events, extra]), "claude-test")
        changed = copy.deepcopy(events)
        changed[-1]["modelUsage"]["fallback"] = {}
        with self.assertRaises(ValueError):
            study.audit_response("claude", encode(changed), "claude-test")

    def test_judgment_coverage_uses_exact_names_and_scores_not_labels_alone(self):
        case = {"assertions": ["fidelity", "substance"], "graded_dimensions": []}
        good = {
            "id": "opaque",
            "assertions": [
                {"index": 2, "pass": False, "evidence": "missing rewrite"},
                {"index": 1, "pass": True, "evidence": "quote"},
            ],
            "graded_dimensions": [],
            "primary_dimensions": [
                {"name": name, "score": 5, "evidence": "quote"}
                for name in study.PRIMARY
            ],
        }
        study.validate_judge(good, case, "opaque")
        bad = []
        for key in ("assertions", "primary_dimensions"):
            record = copy.deepcopy(good)
            record[key].pop()
            bad.append(record)
            record = copy.deepcopy(good)
            record[key][1] = record[key][0]
            bad.append(record)
        record = copy.deepcopy(good)
        record["primary_dimensions"][0]["score"] = True
        bad.append(record)
        record = copy.deepcopy(good)
        record["assertions"][0]["index"] = True
        bad.append(record)
        for record in bad:
            with self.subTest(record=record), self.assertRaises(ValueError):
                study.validate_judge(record, case, "opaque")

    def test_dynamic_criteria_must_be_generated_not_just_acknowledged(self):
        case = {"assertions": [], "dynamic_rubric": {"minimum_criteria": 3}}
        record = {
            "id": "x",
            "assertions": [],
            "primary_dimensions": [
                {"name": n, "score": 4, "evidence": "quote"} for n in study.PRIMARY
            ],
        }
        for criteria in [True, ["one"], ["one", "two", " "]]:
            with self.subTest(criteria=criteria), self.assertRaises(ValueError):
                study.validate_judge(
                    {**record, "dynamic_criteria": criteria}, case, "x"
                )
        study.validate_judge(
            {**record, "dynamic_criteria": ["one", "two", "three"]}, case, "x"
        )

    def test_arms_have_identical_tasks_and_no_skill_arm_has_no_package(self):
        case = {"task": "Task text with facts."}
        a = study.apply_prompt(case, "skill", "SECRET_SKILL")
        b = study.apply_prompt(case, "no-skill", "SECRET_SKILL")
        self.assertEqual(a.split("TASK:\n")[1], b.split("TASK:\n")[1])
        self.assertNotIn("SECRET_SKILL", b)
        self.assertIn("SECRET_SKILL", a)

    def test_six_case_ids_in_one_family_stay_underpowered(self):
        rows = [
            {
                "id": str(i),
                "split": "tune",
                "before": 0,
                "after": 1,
                "pair_id": str(i),
                "family": "one-template",
            }
            for i in range(6)
        ]
        result = study.stats(rows, "family")
        self.assertEqual(result["clusters"], 1)
        self.assertEqual(result["verdict"], "UNDERPOWERED")
        self.assertFalse(result["equivalence_005"])


if __name__ == "__main__":
    unittest.main()
