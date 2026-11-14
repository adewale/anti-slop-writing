#!/usr/bin/env python3
"""Repo-only, frozen candidate screening. Never edits or promotes installed doctrine.

Uses the baseline's audited subscription transports, blind/judge protocol and statistics.
Only `apply` and `judge` call models. `prepare`, `analyze` and tests are model-free.
"""
from __future__ import annotations

import argparse
import difflib
import json
import random
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import subscription_baseline as base
from run_evals import case_prompt, load_judge_worklist, validate_judgment

SEED = 261115
REFS = {
    "compound": "origin/claude/gpt6-astra-personality-guide-zrkwcv",
    "twitter": "origin/claude/twitter-thread-eval-b3mxxi",
    "highlighter": "origin/claude/llm-cliche-highlighter-c2qqq8",
    "teaser": "origin/claude/cataphoric-teasers-handling-sele9m",
}
COMPOUND = (
    "Support must be resolvable by the reader. An undefined coined label does not earn a "
    "claim merely by naming a check or process. Ask for its definition or cut the "
    "unsupported claim; keep standard domain terms and coinages defined in the passage. "
    "Do not invent a definition."
)
TEASER = (
    "Forward-pointing teasers: identify the promised payload and check whether the next "
    "sentences supply it. Cut an undischarged or merely restated promise; ask for missing "
    "content rather than inventing it. Keep labels, questions, and roadmaps that deliver "
    "specific content. A discharged frame can still make an unsupported rarity claim or "
    "redundantly announce significance; judge those separately."
)
GUARDS = {
    "earned-domain-compound", "coined-label-defined-in-place",
    "holdout-coined-label-defined-in-place", "holdout-earned-domain-compound",
    "substantive-actual-measured-vs-advertised", "negation-answers-the-users-hypothesis",
    "key-issue-earned-by-stated-ranking", "earned-negation-chain-changelog",
    "earned-turns-out-with-trace", "earned-anaphora-invariant-chain",
    "holdout-earned-honesty-clarification", "earned-cataphoric-enumeration-label",
    "earned-cataphoric-question-discharged", "back-pointing-label-not-cataphoric",
    "earned-discourse-deixis-roadmap",
}
# New same-split, source-backed tune twins; never counted as extra independent units.
SUPPLIED = {
    "coined-compound-label": [
        "In this paragraph, an exact-head check compares each replica's last merged commit ID with the incoming merge's parent commit ID and stops the merge if they differ.",
        "Editorial-row layout is this team's name for the stored column order and field types; the check compares their hashes across replicas before allowing a merge.",
        "A mismatch is reported during the merge; a matching comparison does not establish that every possible consistency failure is prevented.",
    ],
    "cataphoric-teaser-undischarged": [
        "The missing retry failure is a payment worker submitting the same charge twice after an acknowledgement is lost.",
        "This worker does not record an idempotency key. These are facts about this worker, not evidence about what most teams know.",
    ],
    "cataphoric-teaser-self-posed-question": [
        "The Tuesday indexer deployment skipped records whose update timestamp was exactly equal to the saved checkpoint.",
        "The team spent Wednesday through Friday replaying the skipped records. No count or customer-impact measurement is available.",
    ],
    "new-register-significance-compression": [
        "The new sync engine saves its checkpoint only after the destination acknowledges the batch.",
        "The chaos test killed the worker between sending a batch and receiving its acknowledgement; after restart, all test records reached the destination, with duplicates suppressed by record ID.",
        "No production measurements or user-impact study have been supplied.",
    ],
    "structural-cadence-run": [
        "The on-call roster and acknowledgement log show that the assigned responder acknowledged the page within two minutes.",
        "The responder followed a runbook link that returned HTTP 404. Alert-volume data have not been checked.",
    ],
    "strip-new-register-launch": [
        "The editor runs entirely in a browser tab and opens local plain-text files without an account or installation.",
        "Its supported actions are opening, editing, and saving a plain-text file. No bundle-size or performance measurements are supplied.",
    ],
}


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True)


def installed_files() -> dict[str, str]:
    root = ROOT / "skills/anti-slop-writing"
    return {str(p.relative_to(root)): p.read_text() for p in sorted(root.rglob("*.md"))}


def candidates(files: dict[str, str]) -> dict[str, dict[str, str]]:
    variants = {"current": dict(files)}
    for arm, needle, addition in (
        ("compound", "Do not offer a synonym-only rewrite just because a watch-list word appears.", COMPOUND),
        ("teaser", "Rhetorical staccato: do not ban antithesis/parallelism;", TEASER),
    ):
        text = files["SKILL.md"]
        if text.count(needle) != 1:
            raise ValueError(f"candidate {arm} has no unique insertion point")
        variants[arm] = {**files, "SKILL.md": text.replace(needle, addition + "\n\n" + needle, 1)}
    return variants


def package(files: dict[str, str]) -> str:
    return "\n\n".join(f"FILE {p}\n{files[p]}" for p in sorted(files))


def case_record(c: dict, suite: str, panel: str, family: str) -> dict:
    pair = c.get("paired_with", c["id"])
    return {
        **c, "suite": suite, "group": panel, "pair_id": pair, "family": family,
        "facts": c.get("facts", []), "task": case_prompt({**c, "facts": c.get("facts", [])}),
        "fact_condition": "supplied" if c.get("facts") else "no_additional_facts",
        "role": "guard" if c["id"] in GUARDS else "target",
    }


def repair_highlighter_tune(c: dict) -> dict:
    """New tune versions correct fact-demand defects; original records are archived."""
    c = dict(c)
    c.pop("deterministic_checks", None)
    if c["id"] in SUPPLIED:
        c["id"] += "-grounded-v2"
        c["expected_output"] = (
            "Remove unsupported rhetorical emphasis while preserving all usable source facts. "
            "If the requested mechanism or measurement is absent, ask precisely or cut its "
            "unsupported claim; never invent one. With supplied facts, use them in a grounded "
            "rewrite rather than merely asking or discarding supported content."
        )
        c["assertions"] = [
            "Identifies the rhetorical scaffolding without treating a phrase hit alone as proof of poor writing.",
            "Preserves source-supported content and uncertainty; no fact is invented to make the rewrite concrete.",
            "Asks for precisely missing evidence or justifies a cut when necessary; when supplied facts support a rewrite, uses them instead of merely asking or cutting everything.",
        ]
        c["graded_dimensions"] = []
        c["validity_note"] = "New tune counterpart: the branch's assertions demanded absent facts. Original retained in historical-cases.json."
    return c


def build_cases() -> tuple[list[dict], list[dict], dict]:
    cases, historical, provenance = [], [], {}
    for suite in ("evals.json", "rewrite-evals.json"):
        for c in base.read_json(ROOT / "evals" / suite)["evals"]:
            pair = c.get("paired_with", c["id"])
            family = "maintenance-evidence" if pair.startswith("maintenance-") else base.FAMILIES[pair]
            cases.append(case_record(c, suite, "standing", family))
    for c in base.read_json(ROOT / "evals/shared-benchmark.json")["cases"]:
        if not c["id"].startswith(("neg-earned-antithesis-", "pos-decorative-antithesis-")):
            continue
        earned = c["id"].startswith("neg-")
        cases.append({
            **c, "suite": "shared-benchmark.json", "group": "standing",
            "pair_id": c["id"], "family": "antithesis-calibration", "task": c["prompt"],
            "facts": [], "fact_condition": "no_additional_facts", "role": "guard" if earned else "target",
            "expected_output": " ".join(c["expected_behavior"]),
            "deterministic_assertions": c["assertions"],
            "assertions": ["Keep the supported contrast without rewriting it." if earned else "Revise or cut the unsupported contrast using the source facts."],
        })
    for panel, ref in REFS.items():
        provenance[panel] = {"ref": ref, "commit": git("rev-parse", ref).strip()}
        for suite in ("evals.json", "rewrite-evals.json", "adversarial.json"):
            current = {c["id"] for c in base.read_json(ROOT / "evals" / suite)["evals"]}
            source = json.loads(git("show", f"{ref}:evals/{suite}"))
            for original in source["evals"]:
                if original["id"] in current or original["id"] == "tweet-best-rewrite-anchor":
                    continue
                historical.append({"panel": panel, "suite": suite, "case": original})
                c = dict(original)
                c.pop("deterministic_checks", None)  # triage hits are never quality verdicts
                if panel == "highlighter" and c["split"] == "tune":
                    c = repair_highlighter_tune(c)
                # Historical defective holds are retained but quarantined, not silently rescored.
                # The earned-honesty guard is factual and remains eligible.
                if panel == "highlighter" and c["split"] == "holdout" and c["id"] != "holdout-earned-honesty-clarification":
                    provenance[panel].setdefault("quarantined", []).append(c["id"])
                    continue
                # All new branch examples share their mechanism/source scaffold conservatively.
                rec = case_record(c, suite, panel, f"historical-{panel}-scaffold")
                rec["historical_case_id"] = original["id"]
                rec["historical_split"] = original["split"]
                cases.append(rec)
                supplied = SUPPLIED.get(original["id"])
                if supplied and c["split"] == "tune":
                    rec["requires_fact_pair"] = True
                    twin = {**rec, "id": rec["id"] + "-with-facts", "paired_with": rec["id"],
                            "facts": supplied, "fact_condition": "supplied", "requires_fact_pair": False,
                            "expected_output": "Use the supplied facts to complete a grounded review or rewrite; do not merely ask or cut all supported content. Preserve genuinely unspecified facts as unknown.",
                            "assertions": [
                                "Uses the supplied facts in a substantive review or rewrite rather than only asking or cutting supported content.",
                                "Preserves the source's scope and uncertainty and introduces no unsupported facts or causal conclusions.",
                                "Does not mechanically reject earned domain terms, defined labels, or a forward reference that actually delivers supported content.",
                            ], "graded_dimensions": []}
                    twin["task"] = case_prompt(twin)
                    cases.append(twin)
    if len({c["id"] for c in cases}) != len(cases):
        raise ValueError("duplicate case IDs")
    return cases, historical, provenance


def prepare(dest: Path) -> None:
    if dest.exists() and any(dest.iterdir()):
        raise ValueError("refusing to overwrite registered assets")
    dest.mkdir(parents=True, exist_ok=True)
    cases, historical, provenance = build_cases()
    files = installed_files()
    variants = candidates(files)
    specs = {"no-skill": None}
    for arm, material in variants.items():
        text = package(material)
        name = f"package-{arm}.txt"
        (dest / name).write_text(text)
        specs[arm] = {"file": name, "sha256": base.sha(text)}
        if arm != "current":
            patch = "".join(difflib.unified_diff(
                files["SKILL.md"].splitlines(keepends=True), material["SKILL.md"].splitlines(keepends=True),
                fromfile="a/skills/anti-slop-writing/SKILL.md", tofile="b/skills/anti-slop-writing/SKILL.md",
            ))
            (dest / f"candidate-{arm}.patch").write_text(patch)
    slots = []
    for c in cases:
        arms = ["no-skill", "current"]
        if c["group"] == "standing":
            arms += ["compound", "teaser"]
        elif c["group"] in ("compound", "teaser"):
            arms += [c["group"]]
        trials = 1 if c["group"] == "standing" else 3
        for model in base.APPLY_MODELS:
            for arm in arms:
                for trial in range(1, trials + 1):
                    key = f"candidate-screen-v1|{c['id']}|{model}|{arm}|{trial}"
                    slots.append({"id": base.sha(key)[:24], "case_id": c["id"], "model": model,
                                  "arm": arm, "trial": trial, "group": c["group"]})
    random.Random(SEED).shuffle(slots)
    base.dump(dest / "cases.json", cases)
    base.dump(dest / "historical-cases.json", historical)
    base.dump(dest / "provenance.json", provenance)
    base.dump(dest / "judge-worklist.json", {"role": "judge", "units": [
        {k: c[k] for k in ("id", "suite", "split", "pair_id", "fact_condition", "assertions")}
        | {"graded_dimensions": c.get("graded_dimensions", [])} for c in cases
    ]})
    base.dump(dest / "prompt-templates.json", {
        "skill": base.apply_prompt({"task": "{TASK}"}, "skill", "{SKILL_PACKAGE}"),
        "no-skill": base.apply_prompt({"task": "{TASK}"}, "no-skill", ""),
        "judge": base.judge_prompt({"task": "{TASK}", "assertions": ["{ASSERTION}"]}, "{BLINDED_OUTPUT}", "{OPAQUE_ID}"),
        "primary_rubric": base.PRIMARY,
    })
    base.dump(dest / "manifest.json", {
        "seed": SEED, "base_commit": git("rev-parse", "HEAD").strip(),
        "apply_models": base.APPLY_MODELS, "judges": base.JUDGES,
        "arm_packages": specs, "slots": slots,
        "cases_sha256": base.sha((dest / "cases.json").read_text()),
        "trial_allocation": {"standing": 1, "branch_panels": 3},
    })
    base.dump(dest / "frozen-sources.json", {str(p.relative_to(ROOT)): base.sha(p.read_text()) for p in [
        ROOT / "scripts/candidate_studies.py", ROOT / "scripts/candidate_power.py", ROOT / "scripts/subscription_baseline.py",
        ROOT / "scripts/subscription_model.mjs", ROOT / "scripts/run_evals.py", ROOT / "scripts/score_delta.py",
        *sorted((ROOT / "skills/anti-slop-writing").rglob("*.md")),
    ]})
    base.dump(dest / "design-summary.json", {
        "cases": len(cases), "slots": len(slots), "judgments": 2 * len(slots),
        "panels": {g: {"cases": sum(c["group"] == g for c in cases),
                       "families": sorted({c["family"] for c in cases if c["group"] == g}),
                       "slots": sum(s["group"] == g for s in slots)} for g in sorted({c["group"] for c in cases})},
        "promotion": "Not authorized: branch target panels are single-scaffold rate studies; standing holds are inspected public regressions.",
    })
    print(json.dumps(base.read_json(dest / "design-summary.json"), indent=2))


def mean_scores(slots: list[dict], records: list[dict]) -> dict:
    expected = {s["id"]: s for s in slots}
    actual = {r["id"]: r for r in records}
    if len(expected) != len(slots) or len(actual) != len(records) or actual.keys() != expected.keys():
        raise ValueError("missing, extra, or duplicate trial IDs")
    values = defaultdict(list)
    for rid, record in actual.items():
        slot = expected[rid]
        dimensions = {d["name"]: d["score"] for d in record["primary_dimensions"]}
        if set(dimensions) != set(base.PRIMARY) or len(record["primary_dimensions"]) != len(base.PRIMARY):
            raise ValueError("incomplete primary dimensions")
        if any(type(v) is not int or not 1 <= v <= 5 for v in dimensions.values()):
            raise ValueError("invalid primary score")
        row = {name: (score - 1) / 4 for name, score in dimensions.items()}
        row["unsupported"] = float(dimensions["factual_fidelity"] <= 3)
        row["diagnostic_assertions"] = sum(a["pass"] for a in record.get("assertions", [])) / max(1, len(record.get("assertions", [])))
        values[(slot["case_id"], slot["model"], slot["arm"])].append(row)
    return {key: {name: sum(r[name] for r in rows) / len(rows) for name in rows[0]} for key, rows in values.items()}


def audit(dest: Path) -> tuple[dict, list[dict], dict, dict]:
    manifest = base.read_json(dest / "manifest.json")
    if base.sha((dest / "cases.json").read_text()) != manifest["cases_sha256"]:
        raise ValueError("frozen cases changed")
    packages = base.load_packages(dest, manifest)
    if manifest["apply_models"] != base.APPLY_MODELS or manifest["judges"] != base.JUDGES:
        raise ValueError("registered model panel changed")
    cases = {c["id"]: c for c in base.read_json(dest / "cases.json")}
    units = load_judge_worklist(dest / "judge-worklist.json")
    if len({s["id"] for s in manifest["slots"]}) != len(manifest["slots"]):
        raise ValueError("duplicate manifest slots")
    records, outputs, attempts = defaultdict(list), {}, []
    expected_paths = {"apply": set(), "judge": set()}
    for slot in manifest["slots"]:
        opaque, cid = slot["id"], slot["case_id"]
        c = cases[cid]
        for stage, actors in (("apply", [slot["model"]]), ("judge", list(base.JUDGES))):
            for actor in actors:
                path = dest / stage / actor / opaque
                expected_paths[stage].add(path / "complete.json")
                complete = base.read_json(path / "complete.json")
                attempt = path / f"attempt-{complete['attempt']}"
                req = base.read_json(attempt / "request.json")
                model = (base.APPLY_MODELS if stage == "apply" else base.JUDGES)[actor]
                if req["model"] != model or req["returncode"] != 0 or req["tools"] != []:
                    raise ValueError("request identity/completion mismatch")
                text, _ = base.audit_response(req["provider"], (attempt / "stdout.txt").read_text(), model)
                if stage == "apply":
                    prompt = base.apply_prompt(c, "no-skill" if slot["arm"] == "no-skill" else "skill", packages[slot["arm"]])
                    blinded = base.strip_template_fields(text, ["Rewrite check", "Remembered line"])
                    if complete["output"] != text or complete["blinded"] != blinded:
                        raise ValueError("raw-to-blinded output mismatch")
                    if complete["raw_words"] != len(text.split()) or complete["judged_words"] != len(blinded.split()):
                        raise ValueError("word count mismatch")
                    outputs[opaque] = complete
                else:
                    prompt = base.judge_prompt(c, outputs[opaque]["blinded"], opaque)
                    returned = base.parse_object(text)
                    base.validate_judge(returned, c, opaque)
                    if any(complete.get(k) != v for k, v in returned.items()):
                        raise ValueError("raw-to-judgment mismatch")
                    trusted = {**complete, "case_id": cid, "suite": c["suite"], "split": c["split"],
                               "pair_id": c["pair_id"], "fact_condition": c["fact_condition"], "family": c["family"]}
                    validate_judgment(trusted, units, str(path))
                    records[(slot["model"], actor)].append(trusted)
                if req["prompt_sha256"] != base.sha(prompt) or (attempt / "prompt.txt").read_text() != prompt:
                    raise ValueError("request prompt differs from registered input")
                for p in path.glob("attempt-*/failure.json"):
                    attempts.append({"stage": stage, "actor": actor, "slot": opaque, "arm": slot["arm"], **base.read_json(p)})
    for stage in ("apply", "judge"):
        actual = set((dest / stage).glob("*/*/complete.json"))
        if actual != expected_paths[stage]:
            raise ValueError(f"missing or extra {stage} completions")
    base.dump(dest / "verification.json", {"status": "passed", "apply_slots": len(outputs),
              "valid_judgments": sum(len(r) for r in records.values()), "failed_attempts": attempts,
              "checks": ["exact slots/models/prompts", "complete tool-free provider results", "raw-to-blinded identity", "word counts", "all assertion/dimension labels/evidence", "trusted worklist metadata", "no missing/extra completions"]})
    return manifest, list(cases.values()), records, outputs


def analyze(dest: Path) -> None:
    manifest, cases, records, outputs = audit(dest)
    comparison, case_scores = [], []
    case_map = {c["id"]: c for c in cases}
    for (model, judge), judged in records.items():
        slots = [s for s in manifest["slots"] if s["model"] == model]
        means = mean_scores(slots, judged)
        case_scores.extend({"case_id": cid, "model": apply_model, "arm": arm, "judge": judge,
                            **{key: case_map[cid][key] for key in ("group", "split", "family", "pair_id", "fact_condition", "role")},
                            **scores} for (cid, apply_model, arm), scores in means.items())
        target = dest / "normalized" / f"{model}-{judge}.jsonl"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in judged))
        subprocess.run([sys.executable, str(ROOT / "scripts/run_evals.py"), "grade", str(target),
                        "--worklist", str(dest / "judge-worklist.json"), "--out", str(target.with_suffix(".scores.jsonl"))], check=True, capture_output=True, text=True)
        for panel in ("standing", *REFS):
            arms = [("no-skill", "current")]
            if panel in ("standing", "compound"):
                arms.append(("current", "compound"))
            if panel in ("standing", "teaser"):
                arms.append(("current", "teaser"))
            selections = [("all", lambda c: True), ("holdout", lambda c: c["split"] == "holdout"),
                          ("target", lambda c: c["role"] == "target"), ("guard", lambda c: c["role"] == "guard"),
                          ("supplied", lambda c: c["fact_condition"] == "supplied"),
                          ("no_additional_facts", lambda c: c["fact_condition"] == "no_additional_facts")]
            for before, after in arms:
                for selection, predicate in selections:
                    chosen = [c for c in cases if c["group"] == panel and predicate(c)]
                    if not chosen:
                        continue
                    for outcome in (*base.PRIMARY, "unsupported", "diagnostic_assertions"):
                        rows = [{"id": c["id"], "split": c["split"], "pair_id": c["pair_id"], "family": c["family"],
                                 "before": means[(c["id"], model, before)][outcome],
                                 "after": means[(c["id"], model, after)][outcome]} for c in chosen]
                        result = base.stats(rows, "family", SEED)
                        comparison.append({"panel": panel, "selection": selection, "model": model, "judge": judge,
                                           "before_arm": before, "after_arm": after, "outcome": outcome, **result})
                        if selection == "holdout" and before == "current" and outcome in ("factual_fidelity", "task_fulfillment"):
                            folder = dest / "primary-analysis"
                            folder.mkdir(exist_ok=True)
                            name = f"{panel}-{after}-{model}-{judge}-{outcome}"
                            path = folder / f"{name}.jsonl"
                            path.write_text("".join(json.dumps(r) + "\n" for r in rows))
                            run = subprocess.run([sys.executable, str(ROOT / "scripts/score_delta.py"), str(path), "--holdout-only", "--cluster-field", "family", "--sesoi", "0.05"], capture_output=True, text=True)
                            (folder / f"{name}.gate.txt").write_text(run.stdout + run.stderr)
    lengths = []
    for panel in sorted({c["group"] for c in cases}):
        for model in base.APPLY_MODELS:
            for arm in manifest["arm_packages"]:
                selected = [outputs[s["id"]] for s in manifest["slots"] if s["model"] == model and s["arm"] == arm and case_map[s["case_id"]]["group"] == panel]
                if selected:
                    lengths.append({"panel": panel, "model": model, "arm": arm, "outputs": len(selected),
                                    **{key: sum(r[key] for r in selected) / len(selected) for key in ("raw_words", "judged_words")}})
    agreement = []
    for model in base.APPLY_MODELS:
        by_judge = {j: {r["id"]: r for r in records[(model, j)]} for j in base.JUDGES}
        for name in base.PRIMARY:
            differences = []
            for opaque in by_judge["opus"]:
                a, b = [next(d["score"] for d in by_judge[j][opaque]["primary_dimensions"] if d["name"] == name) for j in ("opus", "sol")]
                differences.append(a - b)
            agreement.append({"model": model, "outcome": name, "n": len(differences),
                              "exact_agreement": sum(d == 0 for d in differences) / len(differences),
                              "mean_opus_minus_sol": sum(differences) / len(differences),
                              "mean_absolute_difference": sum(abs(d) for d in differences) / len(differences)})
    base.dump(dest / "comparisons.json", comparison)
    base.dump(dest / "case-scores.json", case_scores)
    guards = [dict(r, guard_pass=(r["delta"] <= 0.05 if r["outcome"] == "unsupported" else r["delta"] >= -0.05))
              for r in comparison if r["before_arm"] == "current" and r["selection"] in ("supplied", "no_additional_facts")
              and r["outcome"] in ("unsupported", "rewrite_quality")]
    base.dump(dest / "guard-results.json", guards)
    base.dump(dest / "lengths.json", lengths)
    base.dump(dest / "judge-agreement.json", agreement)
    base.dump(dest / "decision.json", {"doctrine_promoted": False,
              "reason": "Preregistered screening/rate studies cannot authorize promotion; target panels have one conservative source/scaffold family each. Standing holds are public inspected regressions, with only one trial per arm/model.",
              "completed_apply": len(outputs), "completed_judgments": sum(len(v) for v in records.values())})
    print(json.dumps(base.read_json(dest / "decision.json"), indent=2))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("stage", choices=("prepare", "apply", "judge", "analyze", "audit"))
    parser.add_argument("--dest", type=Path, required=True)
    parser.add_argument("--workers", type=int, default=8)
    args = parser.parse_args()
    if args.stage == "prepare":
        prepare(args.dest)
    elif args.stage in ("apply", "judge"):
        base.run_stage(args.dest, args.stage, "all", args.workers)
    elif args.stage == "audit":
        audit(args.dest)
    else:
        analyze(args.dest)


if __name__ == "__main__":
    main()
