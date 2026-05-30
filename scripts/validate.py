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
ADVERSARIAL_EVALS = ROOT / "evals" / "adversarial.json"
REWRITE_EVALS = ROOT / "evals" / "rewrite-evals.json"
META_EVALS = ROOT / "evals" / "meta-evals.json"
TRIGGER_QUERIES = ROOT / "evals" / "trigger-queries.json"
MANUAL_CASES = ROOT / "evals" / "cases.md"

REQUIRED = [
    ROOT / "README.md",
    ROOT / "AGENTS.md",
    ROOT / "CONTRIBUTING.md",
    ROOT / "CHANGELOG.md",
    ROOT / "Lessons_learned.md",
    ROOT / "LICENSE",
    ROOT / "docs" / "eval-runbook-notes.md",
    ROOT / "docs" / "hillclimb-improvements.md",
    ROOT / "docs" / "judge-protocol.md",
    ROOT / "runbooks" / "hillclimb-skill.md",
    ROOT / "scripts" / "score_delta.py",
    ROOT / "scripts" / "run_evals.py",
    ROOT / "evals" / "rejected-edits.md",
    ROOT / "evals" / "blinded-eval-harness.md",
    ROOT / "TODO.md",
    ROOT / ".gitignore",
    ROOT / ".github" / "workflows" / "validate.yml",
    SKILL,
    SKILL_DIR / "references" / "anti-slop-writing-doctrine.md",
    SKILL_DIR / "references" / "flow-by-relation.md",
    SKILL_DIR / "references" / "rewrite-patterns.md",
    SKILL_EVALS,
    ADVERSARIAL_EVALS,
    REWRITE_EVALS,
    META_EVALS,
    TRIGGER_QUERIES,
    ROOT / "examples" / "pelican-conclusion-before-after.md",
    ROOT / "examples" / "cards" / "generic-importance.md",
    ROOT / "examples" / "cards" / "decorative-contrast.md",
    ROOT / "examples" / "cards" / "weak-conclusion.md",
    ROOT / "examples" / "cards" / "product-tour-flow.md",
    ROOT / "examples" / "cards" / "safe-essay-voice.md",
    ROOT / "examples" / "cards" / "borrowed-emphasis.md",
    MANUAL_CASES,
    ROOT / "evals" / "failures" / "generic-importance.md",
    ROOT / "evals" / "failures" / "decorative-contrast.md",
    ROOT / "evals" / "failures" / "weak-conclusion.md",
    ROOT / "evals" / "failures" / "product-tour-flow.md",
    ROOT / "evals" / "failures" / "safe-essay-voice.md",
    ROOT / "evals" / "failures" / "borrowed-emphasis.md",
    ROOT / "evals" / "results" / "latest.md",
    ROOT / "evals" / "results" / "2026-05-25-before.md",
    ROOT / "evals" / "results" / "2026-05-25-after.md",
    ROOT / "evals" / "results" / "2026-05-25-runbook-eval-drift.md",
    ROOT / "evals" / "results" / "2026-05-25-adversarial-expansion.md",
    ROOT / "evals" / "results" / "2026-05-29-baseline.md",
    ROOT / "evals" / "results" / "baseline-2026-05-29" / "scores.jsonl",
    ROOT / "evals" / "results" / "2026-05-27-emphasis-source-experiment.md",
    ROOT / "evals" / "results" / "2026-05-28-emphasis-source-procedural" / "scores.jsonl",
    ROOT / "evals" / "results" / "2026-05-28-emphasis-source-procedural" / "README.md",
    ROOT / "evals" / "results" / "2026-05-30-holdout-regression-check" / "README.md",
    ROOT / "evals" / "results" / "2026-05-30-holdout-regression-check" / "scores.jsonl",
    ROOT / "evals" / "results" / "2026-05-30-holdout-regression-check" / "delta.jsonl",
    ROOT / "evals" / "results" / "2026-05-30-holdout-regression-check" / "gate-output.txt",
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


VALID_SPLITS = {"tune", "holdout"}


def validate_graded_dimensions(path: Path, case_id: str, dims: Any) -> None:
    if not isinstance(dims, list) or not dims:
        fail(f"{path.relative_to(ROOT)} eval {case_id} graded_dimensions must be a non-empty list when present")
    for i, dim in enumerate(dims, start=1):
        if not isinstance(dim, dict):
            fail(f"{path.relative_to(ROOT)} eval {case_id} graded_dimensions[{i}] must be an object")
        for field in ("name", "scale", "rubric"):
            if not isinstance(dim.get(field), str) or not dim[field].strip():
                fail(f"{path.relative_to(ROOT)} eval {case_id} graded_dimensions[{i}] missing non-empty {field}")


def validate_dynamic_rubric(path: Path, case_id: str, rubric: Any) -> None:
    if not isinstance(rubric, dict):
        fail(f"{path.relative_to(ROOT)} eval {case_id} dynamic_rubric must be an object when present")
    if not isinstance(rubric.get("instruction"), str) or not rubric["instruction"].strip():
        fail(f"{path.relative_to(ROOT)} eval {case_id} dynamic_rubric missing non-empty instruction")
    min_criteria = rubric.get("minimum_criteria")
    if not isinstance(min_criteria, int) or min_criteria < 2:
        fail(f"{path.relative_to(ROOT)} eval {case_id} dynamic_rubric.minimum_criteria must be int >= 2")


def validate_eval_file(path: Path, min_count: int = 1, min_holdout: int = 2) -> None:
    data = load_json(path)
    if data.get("skill_name") != "anti-slop-writing":
        fail(f"{path.relative_to(ROOT)} skill_name must be anti-slop-writing")
    evals = data.get("evals")
    if not isinstance(evals, list) or len(evals) < min_count:
        fail(f"{path.relative_to(ROOT)} must contain at least {min_count} evals")

    ids: set[str] = set()
    holdout_count = 0
    tune_count = 0
    for index, case in enumerate(evals, start=1):
        if not isinstance(case, dict):
            fail(f"{path.relative_to(ROOT)} eval #{index} must be an object")
        case_id = case.get("id")
        if not isinstance(case_id, str) or not case_id:
            fail(f"{path.relative_to(ROOT)} eval #{index} missing string id")
        if case_id in ids:
            fail(f"duplicate eval id in {path.relative_to(ROOT)}: {case_id}")
        ids.add(case_id)
        for field in ["prompt", "expected_output"]:
            if not isinstance(case.get(field), str) or not case[field].strip():
                fail(f"{path.relative_to(ROOT)} eval {case_id} missing non-empty {field}")
        assertions = case.get("assertions")
        if not isinstance(assertions, list) or len(assertions) < 2:
            fail(f"{path.relative_to(ROOT)} eval {case_id} must have at least 2 assertions")
        if not all(isinstance(item, str) and item.strip() for item in assertions):
            fail(f"{path.relative_to(ROOT)} eval {case_id} assertions must be non-empty strings")
        split = case.get("split")
        if split not in VALID_SPLITS:
            fail(f"{path.relative_to(ROOT)} eval {case_id} split must be one of {sorted(VALID_SPLITS)}")
        if split == "holdout":
            holdout_count += 1
        else:
            tune_count += 1
        if "graded_dimensions" in case:
            validate_graded_dimensions(path, case_id, case["graded_dimensions"])
        if "dynamic_rubric" in case:
            validate_dynamic_rubric(path, case_id, case["dynamic_rubric"])

    if holdout_count < min_holdout:
        fail(f"{path.relative_to(ROOT)} must contain at least {min_holdout} holdout cases (found {holdout_count})")
    if tune_count < 1:
        fail(f"{path.relative_to(ROOT)} must contain at least 1 tune case (found {tune_count})")


def validate_skill_evals() -> None:
    validate_eval_file(SKILL_EVALS, min_count=8, min_holdout=2)
    validate_eval_file(ADVERSARIAL_EVALS, min_count=15, min_holdout=2)
    validate_eval_file(REWRITE_EVALS, min_count=8, min_holdout=2)
    validate_eval_file(META_EVALS, min_count=7, min_holdout=2)


def validate_baseline_scores() -> None:
    path = ROOT / "evals" / "results" / "baseline-2026-05-29" / "scores.jsonl"
    seen: set[str] = set()
    count = 0
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            record = json.loads(line)
        except json.JSONDecodeError as exc:
            fail(f"invalid JSON in {path.relative_to(ROOT)}: {exc}")
        for field in ("id", "split", "score"):
            if field not in record:
                fail(f"{path.relative_to(ROOT)} record missing {field}: {record}")
        if record["split"] not in VALID_SPLITS:
            fail(f"{path.relative_to(ROOT)} record {record['id']} has invalid split")
        if not isinstance(record["score"], (int, float)) or not 0 <= record["score"] <= 1:
            fail(f"{path.relative_to(ROOT)} record {record['id']} score must be in [0,1]")
        if record["id"] in seen:
            fail(f"{path.relative_to(ROOT)} duplicate id: {record['id']}")
        seen.add(record["id"])
        count += 1
    if count < 30:
        fail(f"{path.relative_to(ROOT)} baseline must score at least 30 cases (found {count})")


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
    holdout = 0
    near_miss_negatives = 0
    for index, query in enumerate(queries, start=1):
        if not isinstance(query, dict):
            fail(f"trigger query #{index} must be an object")
        for field in ["id", "query"]:
            if not isinstance(query.get(field), str) or not query[field].strip():
                fail(f"trigger query #{index} missing non-empty {field}")
        should_trigger = query.get("should_trigger")
        if not isinstance(should_trigger, bool):
            fail(f"trigger query {query['id']} should_trigger must be boolean")
        split = query.get("split")
        if split not in VALID_SPLITS:
            fail(f"trigger query {query['id']} split must be one of {sorted(VALID_SPLITS)}")
        positives += int(should_trigger)
        negatives += int(not should_trigger)
        if split == "holdout":
            holdout += 1
        if query["id"].startswith("near-neg-"):
            near_miss_negatives += 1

    if positives < 5 or negatives < 5:
        fail("trigger queries must include at least 5 positives and 5 negatives")
    if holdout < 4:
        fail(f"trigger queries must include at least 4 holdout queries (found {holdout})")
    if near_miss_negatives < 4:
        fail(f"trigger queries must include at least 4 near-neg- near-miss negatives (found {near_miss_negatives})")


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
    validate_baseline_scores()
    validate_with_skills_ref()

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for phrase in ["python3 scripts/validate.py", "evals/evals.json", "evals/adversarial.json", "evals/rewrite-evals.json", "evals/meta-evals.json", "evals/failures/", "examples/cards/", "Lessons_learned.md", "CHANGELOG.md", "runbooks/hillclimb-skill.md", "evals/results/latest.md", "CONTRIBUTING.md", "What to install", "Claude Code", "Codex", "OpenCode", "with_skill", "old_skill"]:
        if phrase not in readme:
            fail(f"README must document {phrase}")

    print("OK: anti-slop-writing project validates")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
