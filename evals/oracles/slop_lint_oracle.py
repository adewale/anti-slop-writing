#!/usr/bin/env python3
"""Slop-lint script oracle for shared Skill Eval Harness script assertions.

Bridges `slop_lint.py` (the repo's deterministic detector registry) into the
shared harness's `script` assertion contract (adewale/skill-eval-harness):
invoked as `python3 oracles/slop_lint_oracle.py {output_dir} CASE_ID` with the
manifest directory as cwd, reads `{output_dir}/output.md`, exits 0 only when
every check for CASE_ID passes, and prints the `{"score": ..., "max_score": ...}`
line the harness feeds to its graded channel. Same calling convention and
output shape as `fixture_oracle.py`.

Checks reuse the repo's `deterministic_checks` schema (see
docs/deterministic-graders.md): forbid-shaped detector checks and format-regex
checks, with optional `scope: "rewrite"`. Keep them forbid-shaped — a
deterministic require-check is a keyword-stuffing incentive.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import slop_lint  # noqa: E402

# Per-case deterministic checks, slop_lint schema. Add a table entry alongside
# any shared-benchmark case whose script assertion names this oracle.
CHECKS: dict[str, list[dict]] = {
    "pos-new-register-launch-strip": [
        {"detector": "no-chain", "max_hits": 0},
        {"detector": "devblog-boilerplate", "max_hits": 0},
        {"detector": "performative-honesty", "max_hits": 0},
        {"detector": "significance-compression", "max_hits": 0},
        {"detector": "not-just-but", "max_hits": 0},
    ],
}


def main() -> int:
    if len(sys.argv) != 3:
        print("usage: slop_lint_oracle.py OUTPUT_DIR CASE_ID", file=sys.stderr)
        return 2
    output_dir = Path(sys.argv[1])
    case_id = sys.argv[2]
    checks = CHECKS.get(case_id)
    if not checks:
        print(f"unknown case id: {case_id}", file=sys.stderr)
        return 2
    for check in checks:
        error = slop_lint.validate_check(check)
        if error:
            print(f"bad check for {case_id}: {error}", file=sys.stderr)
            return 2
    out = output_dir / "output.md"
    if not out.exists():
        print(f"missing output: {out}", file=sys.stderr)
        return 2
    text = out.read_text(encoding="utf-8", errors="replace")
    results = slop_lint.run_checks(text, checks)
    failures = [r for r in results if not r["pass"]]
    print(json.dumps({"score": len(results) - len(failures), "max_score": len(results) or 1, "case_id": case_id}))
    if failures:
        print("FAIL slop-lint oracle")
        for r in failures:
            print("- " + r["evidence"])
        return 1
    print("OK slop-lint oracle: " + case_id)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
