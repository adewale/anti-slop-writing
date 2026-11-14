"""Real filesystem and hook CLI checks, no mocks or provider calls."""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from _support import ROOT, load_script

guard = load_script("scripts/activation_guard.py")


class Guard(unittest.TestCase):
    def test_only_target_skill_and_real_in_tree_reads_are_permitted(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "skill"
            root.mkdir()
            inside = root / "SKILL.md"
            inside.write_text("instructions")
            outside = Path(directory) / "skill-sibling.md"
            outside.write_text("private")
            escape = root / "escape.md"
            escape.symlink_to(outside)
            self.assertTrue(guard.allowed({"tool_name": "Read", "tool_input": {"file_path": str(inside)}}, root))
            self.assertTrue(guard.allowed({"tool_name": "Skill", "tool_input": {"skill": "local-writing:anti-slop-writing"}}, root))
            for event in (
                {"tool_name": "Read", "tool_input": {"file_path": str(outside)}},
                {"tool_name": "Read", "tool_input": {"file_path": str(escape)}},
                {"tool_name": "Read", "tool_input": {"file_path": "SKILL.md"}},
                {"tool_name": "Skill", "tool_input": {"skill": "dataviz"}},
                *({"tool_name": name, "tool_input": {}} for name in ("Write", "Edit", "Bash", "Agent", "Task", "WebFetch", "unknown-future-tool")),
            ):
                with self.subTest(event=event):
                    self.assertFalse(guard.allowed(event, root))

    def test_real_hook_cli_records_denial_and_invalid_input_fails_closed(self):
        with tempfile.TemporaryDirectory() as directory:
            root, ledger = Path(directory), Path(directory) / "ledger.jsonl"
            cmd = [sys.executable, str(ROOT / "scripts/activation_guard.py"), "--root", str(root), "--ledger", str(ledger)]
            payload = {"hook_event_name": "PreToolUse", "tool_use_id": "toolu-1", "tool_name": "Write", "tool_input": {"file_path": str(root / "forbidden.txt"), "content": "do not write"}}
            run = subprocess.run(cmd, input=json.dumps(payload), text=True, capture_output=True, timeout=10)
            self.assertEqual(run.returncode, 0, run.stderr)
            self.assertEqual(json.loads(run.stdout)["hookSpecificOutput"]["permissionDecision"], "deny")
            self.assertFalse(json.loads(ledger.read_text())["allowed"])
            self.assertFalse((root / "forbidden.txt").exists())
            malformed = subprocess.run(cmd, input="not JSON", text=True, capture_output=True, timeout=10)
            self.assertEqual(malformed.returncode, 2)
            self.assertIn("failed closed", malformed.stderr)
            self.assertEqual(len(ledger.read_text().splitlines()), 1)


if __name__ == "__main__":
    unittest.main()
