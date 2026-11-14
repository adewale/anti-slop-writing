#!/usr/bin/env python3
"""Post-run evidence verification, not a new outcome or scoring rule.

Usage: python3 evals/results/2026-11-14-subscription-baseline/verify.py RUNTIME
Produces verification.json from actual files and set comparisons, not echoed counts.
"""

from __future__ import annotations

import json
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "scripts"))
import subscription_baseline as study


def main():
    runtime = Path(sys.argv[1]).resolve()
    manifest = study.read_json(runtime / "manifest.json")
    slots = manifest["slots"]
    ids = [s["id"] for s in slots]
    tuples = [(s["case_id"], s["model"], s["arm"], s["trial"]) for s in slots]
    assert len(ids) == len(set(ids)) == len(set(tuples)) == 804
    cases = {c["id"]: c for c in study.read_json(runtime / "cases.json")}
    assert len(cases) == 67
    expected_apply = {(s["model"], s["id"]) for s in slots}
    expected_judge = {(j, s["id"]) for s in slots for j in study.JUDGES}
    actual_apply = {
        (p.parent.parent.name, p.parent.name)
        for p in (runtime / "apply").glob("*/*/complete.json")
    }
    actual_judge = {
        (p.parent.parent.name, p.parent.name)
        for p in (runtime / "judge").glob("*/*/complete.json")
    }
    assert actual_apply == expected_apply
    assert actual_judge == expected_judge
    package = (runtime / "skill-package.txt").read_text()
    assert study.sha(package) == manifest["skill_sha256"]
    assert study.sha((runtime / "cases.json").read_text()) == manifest["cases_sha256"]
    responses = set()
    valid_counts = Counter()
    for slot in slots:
        c, opaque = cases[slot["case_id"]], slot["id"]
        applied = study.read_json(
            runtime / "apply" / slot["model"] / opaque / "complete.json"
        )
        for stage, agents in [
            ("apply", [slot["model"]]),
            ("judge", list(study.JUDGES)),
        ]:
            for agent in agents:
                path = runtime / stage / agent / opaque
                complete = study.read_json(path / "complete.json")
                model = (
                    study.APPLY_MODELS[agent]
                    if stage == "apply"
                    else study.JUDGES[agent]
                )
                provider = "claude" if model.startswith("claude-") else "openai"
                attempt = path / f"attempt-{complete['attempt']}"
                raw = (attempt / "stdout.txt").read_text()
                text, _ = study.audit_response(provider, raw, model)
                request = study.read_json(attempt / "request.json")
                assert (
                    request["model"] == model
                    and request["tools"] == []
                    and request["returncode"] == 0
                )
                assert request["effort"] == ("low" if stage == "apply" else "medium")
                expected_prompt = (
                    study.apply_prompt(c, slot["arm"], package)
                    if stage == "apply"
                    else study.judge_prompt(c, applied["blinded"], opaque)
                )
                assert (attempt / "prompt.txt").read_text() == expected_prompt
                assert request["prompt_sha256"] == study.sha(expected_prompt)
                if provider == "claude":
                    events = [
                        json.loads(line) for line in raw.splitlines() if line.strip()
                    ]
                    init = [
                        e
                        for e in events
                        if e.get("type") == "system" and e.get("subtype") == "init"
                    ]
                    assert (
                        len(init) == 1
                        and not init[0]["tools"]
                        and not init[0]["skills"]
                    )
                    assert not init[0]["mcp_servers"]
                    response_id = next(
                        e["session_id"] for e in events if e.get("type") == "result"
                    )
                else:
                    response_id = json.loads(raw)["result"]["responseId"]
                assert response_id not in responses, (
                    "duplicate provider response",
                    response_id,
                )
                responses.add(response_id)
                valid_counts[stage] += 1
                if stage == "apply":
                    assert text == complete["output"]
                    assert (
                        study.strip_template_fields(
                            text, ["Rewrite check", "Remembered line"]
                        )
                        == complete["blinded"]
                    )
                    assert len(text.split()) == complete["raw_words"]
                    assert len(complete["blinded"].split()) == complete["judged_words"]
                else:
                    j = study.parse_object(text)
                    study.validate_judge(j, c, opaque)
                    for key in (
                        "assertions",
                        "graded_dimensions",
                        "primary_dimensions",
                        "dynamic_criteria",
                    ):
                        assert j.get(key) == complete.get(key)
    pair_cases = {}
    for c in cases.values():
        if c["group"] == "review-rewrite":
            pair_cases.setdefault(c["pair_id"], []).append(c)
    assert len(pair_cases) == 40
    pairs = [cs for cs in pair_cases.values() if len(cs) == 2]
    assert len(pairs) == 19
    for pair in pairs:
        assert len({c["family"] for c in pair}) == len({c["split"] for c in pair}) == 1
        assert {c["fact_condition"] for c in pair} == {
            "supplied",
            "no_additional_facts",
        }
    infrastructure = list((runtime / "infrastructure-failures").glob("*/*/attempt-*"))
    assert len(infrastructure) == 72
    for a in infrastructure:
        assert not (a / "stdout.txt").read_text()
        assert "EAGAIN" in (a / "stderr.txt").read_text()
    exceptions = Counter()
    attempt_classification = []
    for stage in ("apply", "judge"):
        for a in (runtime / stage).glob("*/*/attempt-*"):
            status = "completed-selected"
            if (a / "failure.json").exists():
                status = "schema-invalid-returned-response"
                exceptions["schema_invalid_returned_response"] += 1
                assert (a / "audit.json").exists()
            elif not (a / "stdout.txt").exists():
                status = "host-interrupted-no-response"
                exceptions["host_interrupted_no_response"] += 1
                assert not (a / "request.json").exists()
            attempt_classification.append(
                {"path": str(a.relative_to(runtime)), "stage": stage, "status": status}
            )
    for a in infrastructure:
        attempt_classification.append(
            {
                "path": str(a.relative_to(runtime)),
                "stage": "apply",
                "status": "pre-request-infrastructure-failure",
            }
        )
    study.dump(
        runtime / "attempt-classification.json",
        {
            "counts": dict(Counter(a["status"] for a in attempt_classification)),
            "attempts": attempt_classification,
        },
    )
    assert exceptions == {
        "schema_invalid_returned_response": 5,
        "host_interrupted_no_response": 8,
    }
    result = {
        "status": "passed",
        "unique_manifest_ids": len(set(ids)),
        "unique_case_model_arm_trial_slots": len(set(tuples)),
        "expected_apply": len(expected_apply),
        "actual_apply": len(actual_apply),
        "expected_judgments": len(expected_judge),
        "actual_judgments": len(actual_judge),
        "extra_or_missing_slots": [],
        "unique_completed_provider_response_ids": len(responses),
        "duplicate_completed_provider_responses": 0,
        "validated": dict(valid_counts),
        "raw_complete_blinding_prompt_model_mismatches": 0,
        "core_pair_ids": 40,
        "complete_fact_pairs": len(pairs),
        "infrastructure_pre_request_failures": len(infrastructure),
        **exceptions,
    }
    # Report the predeclared point guards with the same family weighting as inference.
    scores = study.read_json(runtime / "scores.json")
    guards = []
    for split in ("all", "holdout"):
        for model in study.APPLY_MODELS:
            for judge in study.JUDGES:
                for condition in ("supplied", "no_additional_facts"):
                    selected = [
                        r
                        for r in scores
                        if r["group"] == "review-rewrite"
                        and r["model"] == model
                        and r["judge"] == judge
                        and r["fact_condition"] == condition
                        and (split == "all" or r["split"] == split)
                    ]
                    groups = defaultdict(list)
                    for row in selected:
                        groups[row["family"]].append(row)
                    means = {}
                    for arm in ("no-skill", "skill"):
                        means[arm] = {}
                        for metric in ("unsupported", "rewrite_quality"):
                            family_values = []
                            for values in groups.values():
                                v = [r for r in values if r["arm"] == arm]
                                family_values.append(
                                    sum(
                                        (r[metric] - 1) / 4
                                        if metric == "rewrite_quality"
                                        else r[metric]
                                        for r in v
                                    )
                                    / len(v)
                                )
                            means[arm][metric] = sum(family_values) / len(family_values)
                    unsupported = (
                        means["skill"]["unsupported"] - means["no-skill"]["unsupported"]
                    )
                    quality = (
                        means["skill"]["rewrite_quality"]
                        - means["no-skill"]["rewrite_quality"]
                    )
                    guards.append(
                        {
                            "split": split,
                            "model": model,
                            "judge": judge,
                            "condition": condition,
                            "families": len(groups),
                            "unsupported_delta": unsupported,
                            "normalized_quality_delta": quality,
                            "point_guard_failed": unsupported > 0.05 or quality < -0.05,
                        }
                    )
    study.dump(runtime / "family-weighted-guards.json", guards)
    # Independently invoke the repo's gate on each predeclared co-primary holdout contrast.
    contrasts = []
    for model in study.APPLY_MODELS:
        for judge in study.JUDGES:
            for metric in ("factual_fidelity", "task_fulfillment"):
                selected = [
                    r
                    for r in scores
                    if r["group"] == "review-rewrite"
                    and r["split"] == "holdout"
                    and r["model"] == model
                    and r["judge"] == judge
                ]
                buckets = defaultdict(list)
                for row in selected:
                    buckets[(row["case_id"], row["arm"])].append(row)
                rows = []
                for cid in sorted({r["case_id"] for r in selected}):
                    case = cases[cid]
                    row = {
                        "id": cid,
                        "split": "holdout",
                        "family": case["family"],
                        "pair_id": case["pair_id"],
                    }
                    for field, arm in (("before", "no-skill"), ("after", "skill")):
                        values = buckets[(cid, arm)]
                        assert len(values) == 3
                        row[field] = sum((r[metric] - 1) / 4 for r in values) / 3
                    rows.append(row)
                path = runtime / "primary-analysis" / f"{model}-{judge}-{metric}.jsonl"
                path.parent.mkdir(exist_ok=True)
                path.write_text("".join(json.dumps(r) + "\n" for r in rows))
                gate = subprocess.run(
                    [
                        sys.executable,
                        str(ROOT / "scripts/score_delta.py"),
                        str(path),
                        "--holdout-only",
                        "--cluster-field",
                        "family",
                        "--seed",
                        "261114",
                        "--sesoi",
                        "0.05",
                    ],
                    text=True,
                    capture_output=True,
                )
                assert gate.returncode in (0, 1), gate.stderr
                path.with_suffix(".gate.txt").write_text(gate.stdout + gate.stderr)
                calculated = study.stats(rows, "family")
                meets = gate.returncode == 0 and calculated["delta"] >= 0.05
                contrasts.append(
                    {
                        "model": model,
                        "judge": judge,
                        "outcome": metric,
                        "gate_exit": gate.returncode,
                        "meets_registered_numeric_criterion": meets,
                    }
                )
    result["holdout_co_primary_contrasts"] = contrasts
    result["joint_numeric_criterion_met"] = all(
        c["meets_registered_numeric_criterion"] for c in contrasts
    )
    result["holdout_point_guards_met"] = not any(
        g["point_guard_failed"] for g in guards if g["split"] == "holdout"
    )
    study.dump(runtime / "verification.json", result)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
