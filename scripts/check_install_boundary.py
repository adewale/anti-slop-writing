#!/usr/bin/env python3
"""Fail if the declared installable skill directory contains repo-only artifacts."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BANNED_DIR_NAMES = {
    ".git",
    ".github",
    "__pycache__",
    "eval-runs",
    "evals",
    "node_modules",
    "research",
    "skill-development",
    "tests",
}
BANNED_FILE_SUFFIXES = {".pyc", ".pyo"}
BANNED_FILE_NAMES = {".DS_Store"}


def load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError as exc:
        print(f"FAIL: {path.relative_to(ROOT)} is not valid JSON: {exc}", file=sys.stderr)
        sys.exit(2)


def declared_skill_dirs() -> list[Path]:
    package = load_json(ROOT / "package.json")
    dirs: list[Path] = []
    entry = (package.get("skill") or {}).get("entry")
    if entry:
        dirs.append(ROOT / Path(entry).parent)
    for raw in (package.get("pi") or {}).get("skills") or []:
        path = ROOT / raw
        if path.name == "skills" and path.is_dir():
            dirs.extend(p for p in path.iterdir() if (p / "SKILL.md").is_file())
        else:
            dirs.append(path)
    marketplace = load_json(ROOT / ".claude-plugin" / "marketplace.json")
    for plugin in marketplace.get("plugins") or []:
        for raw in plugin.get("skills") or []:
            dirs.append(ROOT / raw)
    if not dirs:
        for candidate in [ROOT / "SKILL.md", *ROOT.glob("skills/*/SKILL.md"), ROOT / "swiss-poster/SKILL.md", ROOT / "testing-best-practices/SKILL.md"]:
            if candidate.is_file():
                dirs.append(candidate.parent)
    seen: set[Path] = set()
    unique: list[Path] = []
    for path in dirs:
        resolved = path.resolve()
        if resolved not in seen:
            seen.add(resolved)
            unique.append(path)
    return unique


def bad_files(skill_dir: Path) -> list[Path]:
    bad: list[Path] = []
    for path in skill_dir.rglob("*"):
        rel_parts = path.relative_to(skill_dir).parts
        if any(part in BANNED_DIR_NAMES for part in rel_parts):
            bad.append(path)
        elif path.is_file() and (path.suffix in BANNED_FILE_SUFFIXES or path.name in BANNED_FILE_NAMES):
            bad.append(path)
    return bad


def main() -> int:
    dirs = declared_skill_dirs()
    if not dirs:
        print("FAIL: no installable skill directory declared or discovered", file=sys.stderr)
        return 1
    errors: list[str] = []
    for skill_dir in dirs:
        try:
            display = skill_dir.resolve().relative_to(ROOT.resolve())
        except ValueError:
            display = skill_dir
        skill_file = skill_dir / "SKILL.md"
        if not skill_dir.is_dir():
            errors.append(f"{display}: directory does not exist")
            continue
        if not skill_file.is_file():
            errors.append(f"{display}: missing SKILL.md")
        bad = bad_files(skill_dir)
        if bad:
            sample = ", ".join(str(p.relative_to(ROOT)) for p in bad[:20])
            suffix = f"; +{len(bad) - 20} more" if len(bad) > 20 else ""
            errors.append(f"{display}: repo-only artifacts found: {sample}{suffix}")
    if errors:
        for error in errors:
            print(f"FAIL: {error}", file=sys.stderr)
        return 1
    print("OK: installable skill boundary is clean: " + ", ".join(str(d.resolve().relative_to(ROOT.resolve())) for d in dirs))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
