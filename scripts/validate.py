#!/usr/bin/env python3
"""Lightweight validation for the anti-slop-writing skill repo."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "anti-slop-writing" / "SKILL.md"
REQUIRED = [
    ROOT / "README.md",
    ROOT / "AGENTS.md",
    ROOT / "LICENSE",
    ROOT / ".gitignore",
    SKILL,
    ROOT / "skills" / "anti-slop-writing" / "references" / "anti-slop-writing-doctrine.md",
    ROOT / "skills" / "anti-slop-writing" / "references" / "flow-by-relation.md",
    ROOT / "skills" / "anti-slop-writing" / "references" / "rewrite-patterns.md",
    ROOT / "examples" / "pelican-conclusion-before-after.md",
    ROOT / "evals" / "cases.md",
]

REQUIRED_SKILL_PHRASES = [
    "Sharp detail beats inflated significance",
    "Flow-by-relation test",
    "Conclusion test",
    "replace rhythm with relation",
    "Flow break:",
]

REFERENCE_RE = re.compile(r"^references/[^\s]+\.md$", re.M)


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def main() -> int:
    for path in REQUIRED:
        if not path.exists():
            fail(f"missing required file: {path.relative_to(ROOT)}")

    text = SKILL.read_text(encoding="utf-8")
    for phrase in REQUIRED_SKILL_PHRASES:
        if phrase not in text:
            fail(f"SKILL.md missing required phrase: {phrase}")

    for rel in REFERENCE_RE.findall(text):
        ref = SKILL.parent / rel
        if not ref.exists():
            fail(f"SKILL.md references missing file: {rel}")

    cases = (ROOT / "evals" / "cases.md").read_text(encoding="utf-8")
    case_count = len(re.findall(r"^## Case ", cases, re.M))
    if case_count < 5:
        fail(f"expected at least 5 eval cases, found {case_count}")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    if "python3 scripts/validate.py" not in readme:
        fail("README must document validation command")

    print("OK: anti-slop-writing project validates")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
