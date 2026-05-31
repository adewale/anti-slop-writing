#!/usr/bin/env python3
"""Execution runner for anti-slop-writing evals.

The repo is instruction-only: the skill is doctrine, not code, so this runner
does not call a model itself. It orchestrates a loop that sub-agents (or a
human) carry out. See docs/judge-protocol.md for the sub-agent steps and
runbooks/hillclimb-skill.md for where this fits.

Subcommands:

  prepare  Build a worklist of per-case run units (a skill-apply prompt and a
           judge prompt) from one or more eval files, filtered by split.

  grade    Turn per-assertion judgments (emitted by judge sub-agents) into
           per-case scores plus a summary table. A case score is the fraction
           of its assertions that passed, so small movements show up as small
           numbers rather than a censored 0/1. With --include-graded, optional
           1-5 graded_dimensions are normalized and averaged into the score.

  join     Merge a before-scores file and an after-scores file into the
           {id, split, before, after} JSONL that scripts/score_delta.py reads.

Examples:

  python3 scripts/run_evals.py prepare evals/evals.json --split holdout --out work.json
  python3 scripts/run_evals.py grade judgments/*.jsonl --out scores.jsonl
  python3 scripts/run_evals.py join --before base.jsonl --after round2.jsonl --out delta.jsonl
"""
from __future__ import annotations

import argparse
import glob
import json
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SKILL = ROOT / "skills" / "anti-slop-writing" / "SKILL.md"
VALID_SPLITS = {"tune", "holdout"}


def die(msg: str) -> None:
    print(f"FAIL: {msg}", file=sys.stderr)
    raise SystemExit(1)


def load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        die(f"no such file: {path}")
    except json.JSONDecodeError as exc:
        die(f"invalid JSON in {path}: {exc}")


def iter_lines(paths: list[Path]):
    for path in paths:
        with path.open(encoding="utf-8") as fh:
            for line_no, raw in enumerate(fh, start=1):
                line = raw.strip()
                if not line or line.startswith("#"):
                    continue
                try:
                    yield path, line_no, json.loads(line)
                except json.JSONDecodeError as exc:
                    die(f"{path}:{line_no}: invalid JSON: {exc}")


def select(cases: list[dict], split: str) -> list[dict]:
    if split == "all":
        return cases
    return [c for c in cases if c.get("split") == split]


# --- prepare -----------------------------------------------------------------

APPLY_TEMPLATE = (
    "Read {skill} and apply it to the TASK below. Produce exactly the critique "
    "and/or rewrite the skill prescribes — no preamble, no meta-commentary.\n\n"
    "TASK:\n{prompt}"
)

JUDGE_TEMPLATE = (
    "You are grading one eval case for the anti-slop-writing skill. Be skeptical: "
    "an assertion passes only if the OUTPUT clearly satisfies it, with quoted "
    "evidence. Do not give credit for keyword presence alone.\n\n"
    "CASE PROMPT:\n{prompt}\n\n"
    "EXPECTED:\n{expected}\n\n"
    "ASSERTIONS (judge each independently):\n{assertions}\n\n"
    "GRADED DIMENSIONS (score 1-5 when present):\n{graded_dimensions}\n\n"
    "Emit one JSON object: "
    '{{"id": "{id}", "suite": "{suite}", "split": "{split}", '
    '"assertions": [{{"index": 1, "pass": true, "evidence": "<quote>"}}, ...], '
    '"graded_dimensions": [{{"name": "<name>", "score": 5, "evidence": "<quote>"}}, ...]}}'
)


def format_graded_dimensions(case: dict) -> str:
    dims = case.get("graded_dimensions")
    if not dims:
        return "(none)"
    lines = []
    for i, dim in enumerate(dims, start=1):
        lines.append(f"{i}. {dim['name']} ({dim['scale']}): {dim['rubric']}")
    return "\n".join(lines)


def cmd_prepare(args: argparse.Namespace) -> int:
    skill_rel = Path(args.skill)
    units: list[dict] = []
    for raw_path in args.eval_files:
        path = Path(raw_path)
        data = load_json(path)
        cases = data.get("evals")
        if not isinstance(cases, list):
            die(f"{path} has no 'evals' list (trigger-queries.json is handled separately)")
        for case in select(cases, args.split):
            assertions = case.get("assertions", [])
            numbered = "\n".join(f"{i}. {a}" for i, a in enumerate(assertions, start=1))
            graded_dimensions = case.get("graded_dimensions", [])
            units.append(
                {
                    "suite": path.name,
                    "id": case["id"],
                    "split": case.get("split", "unknown"),
                    "apply_prompt": APPLY_TEMPLATE.format(skill=skill_rel, prompt=case["prompt"]),
                    "judge_prompt": JUDGE_TEMPLATE.format(
                        prompt=case["prompt"],
                        expected=case.get("expected_output", ""),
                        assertions=numbered,
                        graded_dimensions=format_graded_dimensions(case),
                        id=case["id"],
                        suite=path.name,
                        split=case.get("split", "unknown"),
                    ),
                    "assertions": assertions,
                    "graded_dimensions": graded_dimensions,
                    "dynamic_rubric": case.get("dynamic_rubric"),
                }
            )
    worklist = {
        "skill_name": "anti-slop-writing",
        "generated": date.today().isoformat(),
        "split": args.split,
        "skill_path": str(skill_rel),
        "unit_count": len(units),
        "units": units,
    }
    out = json.dumps(worklist, indent=2, ensure_ascii=False)
    if args.out:
        Path(args.out).write_text(out + "\n", encoding="utf-8")
        print(f"wrote {len(units)} units to {args.out}", file=sys.stderr)
    else:
        print(out)
    return 0


# --- grade -------------------------------------------------------------------


def normalized_graded_scores(record: dict, path: Path, line_no: int) -> list[float]:
    dims = record.get("graded_dimensions", [])
    if dims in (None, []):
        return []
    if not isinstance(dims, list):
        die(f"{path}:{line_no}: graded_dimensions must be a list when present")
    scores: list[float] = []
    for i, dim in enumerate(dims, start=1):
        if not isinstance(dim, dict):
            die(f"{path}:{line_no}: graded_dimensions[{i}] must be an object")
        raw = dim.get("score")
        if not isinstance(raw, (int, float)) or not 1 <= float(raw) <= 5:
            die(f"{path}:{line_no}: graded_dimensions[{i}].score must be in [1,5]")
        scores.append(float(raw) / 5)
    return scores


def case_score(record: dict, path: Path, line_no: int, include_graded: bool = False) -> dict:
    assertions = record.get("assertions")
    if not isinstance(assertions, list) or not assertions:
        die(f"{path}:{line_no}: record {record.get('id')} missing non-empty 'assertions'")
    passed = 0
    assertion_values: list[float] = []
    for a in assertions:
        if isinstance(a, bool):
            value = float(a)
        elif isinstance(a, dict) and isinstance(a.get("pass"), bool):
            value = float(a["pass"])
        else:
            die(f"{path}:{line_no}: assertion must be bool or object with 'pass'")
        passed += int(value)
        assertion_values.append(value)
    n = len(assertions)
    graded_values = normalized_graded_scores(record, path, line_no)
    score_values = assertion_values + graded_values if include_graded else assertion_values
    split = record.get("split", "unknown")
    if "id" not in record:
        die(f"{path}:{line_no}: record missing 'id'")
    result = {
        "id": record["id"],
        "split": split,
        "suite": record.get("suite", path.stem),
        "score": round(sum(score_values) / len(score_values), 4),
        "all_pass": passed == n,
        "n_passed": passed,
        "n_assertions": n,
    }
    if include_graded or graded_values:
        result["assertion_score"] = round(passed / n, 4)
    if graded_values:
        result["graded_score"] = round(sum(graded_values) / len(graded_values), 4)
        result["n_graded_dimensions"] = len(graded_values)
    if include_graded:
        result["score_includes_graded"] = True
    return result


def cmd_grade(args: argparse.Namespace) -> int:
    paths = [Path(p) for raw in args.judgments for p in glob.glob(raw)] or [Path(p) for p in args.judgments]
    scores: list[dict] = []
    seen: set[str] = set()
    for path, line_no, record in iter_lines(paths):
        s = case_score(record, path, line_no, include_graded=args.include_graded)
        if s["id"] in seen:
            die(f"duplicate id across judgment files: {s['id']}")
        seen.add(s["id"])
        if args.split != "all" and s["split"] != args.split:
            continue
        scores.append(s)

    if not scores:
        die("no judgments matched")

    lines = "\n".join(json.dumps(s, ensure_ascii=False) for s in scores)
    if args.out:
        Path(args.out).write_text(lines + "\n", encoding="utf-8")
        print(f"wrote {len(scores)} scores to {args.out}", file=sys.stderr)
    else:
        print(lines)

    # Summary by split.
    print("\nsummary:", file=sys.stderr)
    for split in ("tune", "holdout", "unknown"):
        bucket = [s for s in scores if s["split"] == split]
        if not bucket:
            continue
        mean = sum(s["score"] for s in bucket) / len(bucket)
        all_pass = sum(int(s["all_pass"]) for s in bucket)
        print(
            f"  {split:8} n={len(bucket):3}  mean_score={mean:.3f}  all_pass={all_pass}/{len(bucket)}",
            file=sys.stderr,
        )
    return 0


# --- join --------------------------------------------------------------------


def load_scores(path: Path) -> dict[str, dict]:
    out: dict[str, dict] = {}
    for p, line_no, record in iter_lines([path]):
        if "id" not in record or "score" not in record:
            die(f"{p}:{line_no}: scores file needs 'id' and 'score'")
        out[record["id"]] = record
    return out


def cmd_join(args: argparse.Namespace) -> int:
    before = load_scores(Path(args.before))
    after = load_scores(Path(args.after))
    ids = sorted(set(before) & set(after))
    if not ids:
        die("no shared ids between before and after scores")
    only_before = sorted(set(before) - set(after))
    only_after = sorted(set(after) - set(before))
    if only_before:
        print(f"warning: ids only in before: {only_before}", file=sys.stderr)
    if only_after:
        print(f"warning: ids only in after: {only_after}", file=sys.stderr)

    rows = []
    for cid in ids:
        b, a = before[cid], after[cid]
        split = b.get("split", a.get("split", "unknown"))
        rows.append({"id": cid, "split": split, "before": b["score"], "after": a["score"]})
    lines = "\n".join(json.dumps(r, ensure_ascii=False) for r in rows)
    if args.out:
        Path(args.out).write_text(lines + "\n", encoding="utf-8")
        print(f"wrote {len(rows)} joined rows to {args.out}", file=sys.stderr)
    else:
        print(lines)
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)

    p_prepare = sub.add_parser("prepare", help="Build a worklist of run units.")
    p_prepare.add_argument("eval_files", nargs="+")
    p_prepare.add_argument("--split", choices=["tune", "holdout", "all"], default="all")
    p_prepare.add_argument("--skill", default=str(DEFAULT_SKILL.relative_to(ROOT)))
    p_prepare.add_argument("--out")
    p_prepare.set_defaults(func=cmd_prepare)

    p_grade = sub.add_parser("grade", help="Score per-assertion judgments.")
    p_grade.add_argument("judgments", nargs="+")
    p_grade.add_argument("--split", choices=["tune", "holdout", "all"], default="all")
    p_grade.add_argument("--out")
    p_grade.add_argument("--include-graded", action="store_true", help="Include optional 1-5 graded_dimensions in the emitted score.")
    p_grade.set_defaults(func=cmd_grade)

    p_join = sub.add_parser("join", help="Merge before/after scores for score_delta.py.")
    p_join.add_argument("--before", required=True)
    p_join.add_argument("--after", required=True)
    p_join.add_argument("--out")
    p_join.set_defaults(func=cmd_join)

    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
