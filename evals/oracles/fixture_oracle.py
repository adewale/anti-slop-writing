#!/usr/bin/env python3
"""Fixture-backed output oracle for shared Skill Eval Harness script assertions."""
from __future__ import annotations
import json
import re
import sys
from pathlib import Path

CHECKS = {
  "round3-fixture-mechanism-copy": {
    "all": [
      "HMAC",
      "retry receipt"
    ],
    "forbid": [
      "\\b(pivotal|transformative|unlock|modern productivity|fast-moving teams|collaboration platform)\\b"
    ]
  }
}

def contains(text: str, needle: str) -> bool:
    return needle.casefold() in text.casefold()

def main() -> int:
    if len(sys.argv) != 3:
        print("usage: fixture_oracle.py OUTPUT_DIR CASE_ID", file=sys.stderr)
        return 2
    output_dir = Path(sys.argv[1])
    case_id = sys.argv[2]
    spec = CHECKS.get(case_id)
    if not spec:
        print(f"unknown case id: {case_id}", file=sys.stderr)
        return 2
    out = output_dir / "output.md"
    if not out.exists():
        print(f"missing output: {out}", file=sys.stderr)
        return 2
    text = out.read_text(encoding="utf-8", errors="replace")
    failures: list[str] = []
    for needle in spec.get("all", []):
        if not contains(text, needle):
            failures.append(f"missing required text: {needle!r}")
    for group in spec.get("any", []):
        if not any(contains(text, needle) for needle in group):
            failures.append("missing one of: " + ", ".join(repr(x) for x in group))
    for pattern in spec.get("regex", []):
        if not re.search(pattern, text, re.I | re.M | re.S):
            failures.append(f"missing regex: {pattern}")
    for pattern in spec.get("forbid", []):
        if re.search(pattern, text, re.I | re.M | re.S):
            failures.append(f"forbidden regex present: {pattern}")
    if failures:
        print("FAIL fixture oracle")
        for failure in failures:
            print("- " + failure)
        return 1
    print("OK fixture oracle: " + case_id)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
