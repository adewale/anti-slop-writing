#!/usr/bin/env python3
"""Validation for the anti-slop-writing skill repo."""
from __future__ import annotations

import json
import re
import shutil
import subprocess
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "anti-slop-writing"
SKILL = SKILL_DIR / "SKILL.md"
SKILL_EVALS = ROOT / "evals" / "evals.json"
TRIGGER_QUERIES = ROOT / "evals" / "trigger-queries.json"
MANUAL_CASES = ROOT / "evals" / "cases.md"

REQUIRED = [
    ROOT / "README.md",
    ROOT / "AGENTS.md",
    ROOT / "LICENSE",
    ROOT / ".gitignore",
    ROOT / ".github" / "workflows" / "validate.yml",
    SKILL,
    SKILL_DIR / "references" / "anti-slop-writing-doctrine.md",
    SKILL_DIR / "references" / "flow-by-relation.md",
    SKILL_DIR / "references" / "rewrite-patterns.md",
    SKILL_EVALS,
    TRIGGER_QUERIES,
    ROOT / "examples" / "pelican-conclusion-before-after.md",
    MANUAL_CASES,
    ROOT / "evals" / "results" / "latest.md",
]

REQUIRED_SKILL_PHRASES = [
    "Sharp detail beats inflated significance",
    "Flow-by-relation test",
    "Conclusion test",
    "replace rhythm with relation",
    "Flow break:",
    "Load local references only when the task needs them",
]

REFERENCE_RE = re.compile(r"^references/[^\s]+\.md", re.M)
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"invalid JSON in {path.relative_to(ROOT)}: {exc}")


def parse_frontmatter(text: str) -> dict[str, str]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        fail("SKILL.md must start with YAML frontmatter")

    try:
        end = next(i for i, line in enumerate(lines[1:], start=1) if line.strip() == "---")
    except StopIteration:
        fail("SKILL.md frontmatter must end with ---")

    fields: dict[str, str] = {}
    current_key: str | None = None
    for line in lines[1:end]:
        if not line.strip():
            continue
        if not line.startswith(" ") and ":" in line:
            key, value = line.split(":", 1)
            current_key = key.strip()
            fields[current_key] = value.strip().strip('"\'')
        elif current_key and line.startswith(" "):
            fields[current_key] = (fields[current_key] + " " + line.strip()).strip()
        else:
            fail(f"unsupported frontmatter line: {line}")
    return fields


def validate_frontmatter(text: str) -> None:
    fields = parse_frontmatter(text)
    name = fields.get("name", "")
    description = fields.get("description", "")

    if not name:
        fail("SKILL.md frontmatter missing name")
    if len(name) > 64 or not NAME_RE.fullmatch(name):
        fail("SKILL.md name must be lowercase letters/numbers/hyphens, no leading/trailing/consecutive hyphens, max 64 chars")
    if name != SKILL_DIR.name:
        fail(f"SKILL.md name must match parent directory: {SKILL_DIR.name}")
    if name in {"anthropic", "claude"}:
        fail("SKILL.md name must not use Claude reserved words")
    if "<" in name or ">" in name:
        fail("SKILL.md name must not contain XML tags")

    if not description:
        fail("SKILL.md frontmatter missing description")
    if len(description) > 1024:
        fail(f"SKILL.md description exceeds 1024 chars: {len(description)}")
    if "<" in description or ">" in description:
        fail("SKILL.md description must not contain XML tags")
    if "Use" not in description and "use" not in description:
        fail("SKILL.md description should say when to use the skill")

    license_name = fields.get("license")
    if license_name != "MIT":
        fail("SKILL.md license should be MIT")

    compatibility = fields.get("compatibility")
    if not compatibility:
        fail("SKILL.md frontmatter missing compatibility")
    if compatibility and len(compatibility) > 500:
        fail(f"SKILL.md compatibility exceeds 500 chars: {len(compatibility)}")


def validate_skill_evals() -> None:
    data = load_json(SKILL_EVALS)
    if data.get("skill_name") != "anti-slop-writing":
        fail("evals/evals.json skill_name must be anti-slop-writing")
    evals = data.get("evals")
    if not isinstance(evals, list) or len(evals) < 5:
        fail("evals/evals.json must contain at least 5 evals")

    ids: set[str] = set()
    for index, case in enumerate(evals, start=1):
        if not isinstance(case, dict):
            fail(f"eval #{index} must be an object")
        case_id = case.get("id")
        if not isinstance(case_id, str) or not case_id:
            fail(f"eval #{index} missing string id")
        if case_id in ids:
            fail(f"duplicate eval id: {case_id}")
        ids.add(case_id)
        for field in ["prompt", "expected_output"]:
            if not isinstance(case.get(field), str) or not case[field].strip():
                fail(f"eval {case_id} missing non-empty {field}")
        assertions = case.get("assertions")
        if not isinstance(assertions, list) or len(assertions) < 2:
            fail(f"eval {case_id} must have at least 2 assertions")
        if not all(isinstance(item, str) and item.strip() for item in assertions):
            fail(f"eval {case_id} assertions must be non-empty strings")


def validate_with_skills_ref() -> None:
    if not shutil.which("skills-ref"):
        return
    result = subprocess.run(["skills-ref", "validate", str(SKILL_DIR)], cwd=ROOT)
    if result.returncode != 0:
        fail("skills-ref validation failed")


def validate_trigger_queries() -> None:
    data = load_json(TRIGGER_QUERIES)
    if data.get("skill_name") != "anti-slop-writing":
        fail("evals/trigger-queries.json skill_name must be anti-slop-writing")
    queries = data.get("queries")
    if not isinstance(queries, list) or len(queries) < 10:
        fail("evals/trigger-queries.json must contain at least 10 queries")

    positives = 0
    negatives = 0
    for index, query in enumerate(queries, start=1):
        if not isinstance(query, dict):
            fail(f"trigger query #{index} must be an object")
        for field in ["id", "query"]:
            if not isinstance(query.get(field), str) or not query[field].strip():
                fail(f"trigger query #{index} missing non-empty {field}")
        should_trigger = query.get("should_trigger")
        if not isinstance(should_trigger, bool):
            fail(f"trigger query {query['id']} should_trigger must be boolean")
        positives += int(should_trigger)
        negatives += int(not should_trigger)

    if positives < 5 or negatives < 5:
        fail("trigger queries must include at least 5 positives and 5 negatives")


def main() -> int:
    for path in REQUIRED:
        if not path.exists():
            fail(f"missing required file: {path.relative_to(ROOT)}")

    text = SKILL.read_text(encoding="utf-8")
    validate_frontmatter(text)

    for phrase in REQUIRED_SKILL_PHRASES:
        if phrase not in text:
            fail(f"SKILL.md missing required phrase: {phrase}")

    for rel in REFERENCE_RE.findall(text):
        ref = SKILL.parent / rel
        if not ref.exists():
            fail(f"SKILL.md references missing file: {rel}")

    cases = MANUAL_CASES.read_text(encoding="utf-8")
    case_count = len(re.findall(r"^## Case ", cases, re.M))
    if case_count < 5:
        fail(f"expected at least 5 manual eval cases, found {case_count}")

    validate_skill_evals()
    validate_trigger_queries()
    validate_with_skills_ref()

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for phrase in ["python3 scripts/validate.py", "evals/evals.json", "evals/results/latest.md", "What to install", "Claude Code", "Codex", "OpenCode", "with_skill", "old_skill"]:
        if phrase not in readme:
            fail(f"README must document {phrase}")

    print("OK: anti-slop-writing project validates")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
