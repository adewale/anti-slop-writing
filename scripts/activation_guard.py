#!/usr/bin/env python3
"""Fail-closed Claude PreToolUse hook for the controlled activation study.

No model calls. Only the frozen skill's native invocation and reads inside its
real directory are permitted. All other tools/skills are denied before execution.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path


def allowed(event: dict, root: Path) -> bool:
    name, arguments = event.get("tool_name"), event.get("tool_input", {})
    if name == "Skill":
        return arguments.get("skill") in ("anti-slop-writing", "local-writing:anti-slop-writing")
    if name != "Read":
        return False
    value = arguments.get("file_path")
    if not isinstance(value, str) or not Path(value).is_absolute():
        return False
    return Path(value).resolve().is_relative_to(root.resolve())


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--ledger", type=Path, required=True)
    args = parser.parse_args()
    try:
        event = json.load(sys.stdin)
        if event.get("hook_event_name") != "PreToolUse" or not event.get("tool_use_id"):
            raise ValueError("invalid PreToolUse event")
        permit = allowed(event, args.root)
        record = {"tool_use_id": event["tool_use_id"], "tool_name": event.get("tool_name"),
                  "allowed": permit, "requested_skill": event.get("tool_input", {}).get("skill")}
        descriptor = os.open(args.ledger, os.O_WRONLY | os.O_APPEND | os.O_CREAT, 0o600)
        try:
            os.write(descriptor, (json.dumps(record) + "\n").encode())
        finally:
            os.close(descriptor)
        print(json.dumps({"hookSpecificOutput": {"hookEventName": "PreToolUse",
            "permissionDecision": "allow" if permit else "deny",
            "permissionDecisionReason": "This read-only session permits only its local writing skill and reads of its reference files."}}))
        return 0
    except (ValueError, TypeError, OSError, AttributeError) as exc:
        print(f"Read-only tool guard failed closed: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
