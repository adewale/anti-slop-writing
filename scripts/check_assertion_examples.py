#!/usr/bin/env python3
"""Grade the checked-in example outputs with the pinned Skill Eval Harness.

evals/assertion-examples.json lists manifest cases with example outputs that
must pass and outputs that must fail. Each example is graded by the harness's
own assertion evaluator (not a local re-implementation), so a pattern typo or
a check that cannot tell a right answer from a wrong one fails here instead of
in a paid run:

- a pass example must satisfy every gate/critical objective assertion of every
  listed case;
- a fail example must fail at least one of them.

Judge assertions are not graded. Run it with the pinned harness on the path:

    uvx --from skill-eval-harness==0.6.0 python scripts/check_assertion_examples.py

Exit status: 0 when every example behaves as declared, 1 otherwise, 2 when
the harness is not importable or the examples file is malformed.
"""
from __future__ import annotations

import json
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVALS = ROOT / "evals"
EXAMPLES = EVALS / "assertion-examples.json"
MANIFEST = EVALS / "shared-benchmark.json"


def main() -> int:
    try:
        import skill_benchmark as sb
    except ImportError:
        print("FAIL: skill_benchmark is not importable; run with "
              "`uvx --from skill-eval-harness==0.6.0 python scripts/check_assertion_examples.py`",
              file=sys.stderr)
        return 2
    spec = json.loads(EXAMPLES.read_text(encoding="utf-8"))
    manifest = sb.validate_manifest(MANIFEST)
    cases = {case["id"]: case for case in sb.iter_cases(manifest)}
    problems: list[str] = []
    checked = 0
    for group in spec.get("groups", []):
        if not group.get("cases") or not group.get("pass") or not group.get("fail"):
            print(f"FAIL: group {group.get('name')!r} needs cases, pass and fail examples", file=sys.stderr)
            return 2
        for case_id in group["cases"]:
            case = cases.get(case_id)
            if case is None:
                problems.append(f"{case_id}: not in {MANIFEST.relative_to(ROOT)}")
                continue
            gates = [a for a in case.get("assertions", [])
                     if a.get("type") not in sb.QUALITATIVE_ASSERTIONS
                     and sb.assertion_severity(a) in {"gate", "critical"}]
            if not gates:
                problems.append(f"{case_id}: no gate/critical objective assertion to check")
                continue
            for expected, examples in (("pass", group["pass"]), ("fail", group["fail"])):
                for rel in examples:
                    example = ROOT / rel
                    text = example.read_text(encoding="utf-8")
                    with tempfile.TemporaryDirectory() as td:
                        output = Path(td) / "output.md"
                        output.write_text(text, encoding="utf-8")
                        results = {sb.assertion_label(a) if hasattr(sb, "assertion_label") else a.get("name"):
                                   bool(sb.assertion_result(a, text, output, allow_scripts=True,
                                                            manifest_dir=EVALS).get("passed"))
                                   for a in gates}
                    checked += 1
                    failed = sorted(name for name, ok in results.items() if not ok)
                    if expected == "pass" and failed:
                        problems.append(f"{case_id}: pass example {rel} fails {failed}")
                    elif expected == "fail" and not failed:
                        problems.append(f"{case_id}: fail example {rel} passes every gate {sorted(results)}")
                    else:
                        verdict = "fails " + ", ".join(failed) if failed else "passes"
                        print(f"ok   {case_id}: {expected} example {Path(rel).name} {verdict}")
    if problems:
        for problem in problems:
            print(f"FAIL {problem}")
        return 1
    print(f"OK: {checked} example gradings behaved as declared")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
