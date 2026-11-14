"""Activation is observed instruction delivery, not model self-report. No live calls."""
from __future__ import annotations

import copy
import json
import subprocess
import tempfile
import unittest
from pathlib import Path

from _support import ROOT, load_script

study = load_script("scripts/live_activation.py")
TEXT = "---\nname: anti-slop-writing\ndescription: Edit prose.\n---\n# Instructions\nUse source facts.\n"
FILE = "/isolated/anti-slop-writing/SKILL.md"


def pi_events():
    return [
        {"type": "init", "skills": [{"name": "anti-slop-writing", "filePath": FILE}], "tools": ["read"], "systemPrompt": "Skill metadata only.", "model": "gpt-6.1-sol", "cwd": "/isolated"},
        {"type": "result", "success": True, "model": "gpt-6.1-sol", "messages": [
            {"role": "assistant", "model": "gpt-6.1-sol", "stopReason": "toolUse", "content": [{"type": "toolCall", "id": "read-1", "name": "read", "arguments": {"path": FILE}}]},
            {"role": "toolResult", "toolCallId": "read-1", "toolName": "read", "isError": False, "content": [{"type": "text", "text": TEXT}]},
            {"role": "assistant", "model": "gpt-6.1-sol", "stopReason": "stop", "content": [{"type": "text", "text": "Please paste the paragraph."}]},
        ]},
    ]


class Activation(unittest.TestCase):
    def test_successful_full_read_is_activation_but_attempt_error_or_partial_is_not(self):
        events = pi_events()
        self.assertTrue(study.classify_pi(events, TEXT, FILE)["activated"])
        for change in ({"isError": True}, {"content": [{"type": "text", "text": "# Instructions"}]}):
            bad = copy.deepcopy(events)
            bad[-1]["messages"][1].update(change)
            result = study.classify_pi(bad, TEXT, FILE)
            self.assertTrue(result["attempted"])
            self.assertFalse(result["activated"])
        self.assertTrue(study.classify_pi([events[0], {**events[-1], "messages": [events[-1]["messages"][-1]]}], TEXT, FILE)["valid"])

    def test_final_message_quoting_skill_is_not_delivery_and_model_drift_rejected(self):
        events = pi_events()
        events[-1]["messages"] = [{"role": "assistant", "model": "gpt-6.1-sol", "stopReason": "stop", "content": [{"type": "text", "text": "I loaded it. " + TEXT}]}]
        self.assertFalse(study.classify_pi(events, TEXT, FILE)["activated"])
        events[-1]["messages"][0]["model"] = "other"
        with self.assertRaises(ValueError):
            study.classify_pi(events, TEXT, FILE)

    def test_advertisement_is_not_activation_and_body_preloading_rejected(self):
        events = pi_events()
        events[-1]["messages"] = [events[-1]["messages"][-1]]
        result = study.classify_pi(events, TEXT, FILE)
        self.assertTrue(result["advertised"])
        self.assertFalse(result["attempted"])
        self.assertFalse(result["activated"])
        events[0]["systemPrompt"] = TEXT
        with self.assertRaises(ValueError):
            study.classify_pi(events, TEXT, FILE)

    def test_claude_native_skill_requires_success_and_body_delivery_not_just_launch(self):
        events = [
            {"type": "system", "subtype": "init", "skills": ["anti-slop-writing"], "tools": ["Read", "Skill"], "mcp_servers": [], "plugins": [{"name": "cc-plugin-agents-md", "path": "builtin", "source": "cc-plugin-agents-md@builtin"}]},
            {"type": "assistant", "message": {"content": [{"type": "tool_use", "id": "s1", "name": "Skill", "input": {"skill": "anti-slop-writing"}}]}},
            {"type": "user", "message": {"content": [{"type": "tool_result", "tool_use_id": "s1", "content": "Launching skill: anti-slop-writing"}]}},
            {"type": "user", "message": {"content": [{"type": "text", "text": study.body(TEXT)}]}},
            {"type": "result", "subtype": "success", "is_error": False, "modelUsage": {"claude-sonnet-5-5": {}}},
        ]
        self.assertTrue(study.classify_claude(events, TEXT, FILE)["activated"])
        with self.assertRaises(ValueError):
            study.classify_claude(events, TEXT, FILE, [])
        receipt = {"tool_use_id": "s1", "tool_name": "Skill", "allowed": True, "requested_skill": "anti-slop-writing"}
        self.assertTrue(study.classify_claude(events, TEXT, FILE, [receipt])["activated"])
        with self.assertRaises(ValueError):
            study.classify_claude(events, TEXT, FILE, [{**receipt, "allowed": False}])
        namespaced = copy.deepcopy(events)
        namespaced[0]["skills"] = [*sorted(study.CLAUDE_BUILTINS), "local-writing:anti-slop-writing"]
        namespaced[1]["message"]["content"][0]["input"]["skill"] = "local-writing:anti-slop-writing"
        self.assertTrue(study.classify_claude(namespaced, TEXT, FILE)["activated"])
        namespaced[0]["skills"].append("foreign-user-skill")
        with self.assertRaises(ValueError):
            study.classify_claude(namespaced, TEXT, FILE)
        absent = events[:3] + events[4:]
        self.assertFalse(study.classify_claude(absent, TEXT, FILE)["activated"])
        spoof = copy.deepcopy(absent)
        spoof.insert(-1, {"type": "assistant", "message": {"content": [{"type": "text", "text": study.body(TEXT)}]}})
        self.assertFalse(study.classify_claude(spoof, TEXT, FILE)["activated"])
        failed = copy.deepcopy(events)
        failed[2]["message"]["content"][0]["is_error"] = True
        self.assertFalse(study.classify_claude(failed, TEXT, FILE)["activated"])

    def test_claude_read_body_accepts_native_tab_or_arrow_line_prefixes(self):
        for separator in ("\t", "→"):
            numbered = "\n".join(f"{i}{separator}{line}" for i, line in enumerate(TEXT.splitlines(), 1))
            events = [
                {"type": "system", "subtype": "init", "skills": ["anti-slop-writing"], "tools": ["Read", "Skill"], "mcp_servers": []},
                {"type": "assistant", "message": {"content": [{"type": "tool_use", "id": "r1", "name": "Read", "input": {"file_path": FILE}}]}},
                {"type": "user", "message": {"content": [{"type": "tool_result", "tool_use_id": "r1", "content": numbered}]}},
                {"type": "result", "subtype": "success", "is_error": False, "modelUsage": {"claude-sonnet-5-5": {}}},
            ]
            with self.subTest(separator=separator):
                self.assertTrue(study.classify_claude(events, TEXT, FILE)["activated"])

    def test_native_unavailable_tool_error_is_not_an_executed_capability(self):
        events = [
            {"type": "system", "subtype": "init", "skills": ["anti-slop-writing"], "tools": ["Read", "Skill"], "mcp_servers": []},
            {"type": "assistant", "message": {"content": [{"type": "tool_use", "id": "b1", "name": "Bash", "input": {"command": "pwd"}}]}},
            {"type": "user", "message": {"content": [{"type": "tool_result", "tool_use_id": "b1", "is_error": True, "content": "<tool_use_error>Error: No such tool available: Bash. Bash is disabled for this session, in subagents as well as here.</tool_use_error>"}]}},
            {"type": "result", "subtype": "success", "is_error": False, "modelUsage": {"claude-sonnet-5-5": {}}},
        ]
        result = study.classify_claude(events, TEXT, FILE, [])
        self.assertTrue(result["valid"])
        self.assertFalse(result["activated"])
        self.assertEqual(result["client_rejected_tools"], ["Bash"])
        spawned = copy.deepcopy(events)
        spawned[-1]["subagent_stats"] = {"spawned": 1}
        with self.assertRaisesRegex(ValueError, "subagent execution"):
            study.classify_claude(spawned, TEXT, FILE, [])
        for update in ({"is_error": False}, {"content": "Command failed after running."}):
            bad = copy.deepcopy(events)
            bad[2]["message"]["content"][0].update(update)
            with self.subTest(update=update), self.assertRaises(ValueError):
                study.classify_claude(bad, TEXT, FILE, [])

    def test_guarded_read_resolves_symlink_escapes_before_opening(self):
        module = (ROOT / "scripts/activation_model.mjs").as_uri()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "root"
            root.mkdir()
            (root / "inside.md").write_text("allowed")
            outside = Path(directory) / "outside.md"
            outside.write_text("private")
            (root / "escape.md").symlink_to(outside)
            code = f"import {{ confinedPath }} from {json.dumps(module)}; for (const p of process.argv.slice(1)) {{ try {{ console.log(JSON.stringify({{ok:true,path:await confinedPath({json.dumps(str(root))},p)}})); }} catch {{ console.log(JSON.stringify({{ok:false}})); }} }}"
            run = subprocess.run(["node", "--input-type=module", "-e", code, str(root / "inside.md"), str(root / "escape.md"), str(outside)], capture_output=True, text=True, timeout=10)
            self.assertEqual(run.returncode, 0, run.stderr)
            self.assertEqual([json.loads(line)["ok"] for line in run.stdout.splitlines()], [True, False, False])


if __name__ == "__main__":
    unittest.main()
