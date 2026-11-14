#!/usr/bin/env python3
"""Model-free follow-through: branch evidence and a blind human calibration packet.

Does not merge/delete refs, score human answers, or call a model. The human packet
intentionally samples disagreement and cannot estimate a population error rate.
"""
from __future__ import annotations

import argparse
import json
import random
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BRANCHES = (
    "agent/upgrade-ruff-0.16", "ci/no-extra-cost-optimisations-20261102",
    "codex/pin-github-actions-2026-11-05", "claude/tweet-audit-l4yq2z",
    "claude/test-audit-campaign", "claude/verification-audit-fixes",
    "claude/stop-slop-review-61fuj1", "cleanup/avoid-duplicate-ci-runs",
    "dependabot/github_actions/github-actions-7840bcb697",
    "skills/curtail-maintenance-ceremony", "sol/eval-integrity",
)


def read(path: Path):
    return json.loads(path.read_text())


def write(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True)


def branches(dest: Path) -> None:
    main = git("rev-parse", "origin/main").strip()
    result = []
    for branch in BRANCHES:
        ref = f"origin/{branch}"
        head = git("rev-parse", ref).strip()
        fork = git("merge-base", "origin/main", ref).strip()
        added = git("diff", "--diff-filter=A", "--name-only", fork, ref).splitlines()
        same, different = [], []
        for name in added:
            original = subprocess.check_output(["git", "show", f"{ref}:{name}"], cwd=ROOT)
            current = subprocess.run(["git", "show", f"origin/main:{name}"], cwd=ROOT, capture_output=True)
            (same if current.returncode == 0 and original == current.stdout else different).append(name)
        cherry = git("cherry", "origin/main", ref).splitlines()
        result.append({"branch": branch, "head": head, "main": main,
                       "unreachable_commits": int(git("rev-list", "--count", f"origin/main..{ref}")),
                       "patch_equivalent": sum(line.startswith("-") for line in cherry),
                       "unmatched_patches": sum(line.startswith("+") for line in cherry),
                       "added_files": len(added), "identical_added_files": len(same), "different_added_files": different,
                       "changed_paths": git("diff", "--name-status", fork, ref).splitlines()})
    stop = next(r for r in result if r["branch"] == "claude/stop-slop-review-61fuj1")
    old = git("show", "origin/claude/stop-slop-review-61fuj1:scripts/saturation_index.py")
    current = git("show", "origin/main:scripts/saturation_index.py")
    stop["saturation_equivalent_except_unused_import"] = old.count("from statistics import pstdev\n") == 1 and old.replace("from statistics import pstdev\n", "") == current
    write(dest / "branch-audit-before.json", result)
    print(json.dumps(result, indent=2))


def select_packet(records: list[dict], per_model: int = 6, controls: int = 3) -> list[dict]:
    selected = []
    for model in sorted({r["model"] for r in records}):
        used = set()
        candidates = sorted((r for r in records if r["model"] == model and r["difference"] != 0), key=lambda r: (-abs(r["difference"]), r["slot"]))
        disagreements = []
        for row in candidates:
            if row["case_id"] not in used:
                disagreements.append({**row, "selection": "disagreement"})
                used.add(row["case_id"])
            if len(disagreements) == per_model:
                break
        if len(disagreements) != per_model:
            raise ValueError("insufficient distinct-case disagreements; do not fill with repeat trials")
        selected.extend(disagreements)
        agreement = sorted((r for r in records if r["model"] == model and r["difference"] == 0), key=lambda r: (r["opus_score"], r["slot"]))
        # Low/median/high agreement controls, always different cases within a model.
        for target in (0.0, 0.5, 1.0)[:controls]:
            available = [r for r in agreement if r["case_id"] not in used]
            if not available:
                raise ValueError("insufficient distinct-case agreement controls")
            row = available[round(target * (len(available) - 1))]
            used.add(row["case_id"])
            selected.append({**row, "selection": "agreement-control"})
    random.Random(261117).shuffle(selected)
    return selected


def packet(source: Path, dest: Path) -> None:
    manifest, cases = read(source / "manifest.json"), read(source / "cases.json")
    case_map = {c["id"]: c for c in cases}
    records = []
    for slot in manifest["slots"]:
        if slot["group"] != "review-rewrite":
            continue
        scores = {}
        evidence = {}
        for judge in ("opus", "sol"):
            record = read(source / "judge" / judge / slot["id"] / "complete.json")
            dimension = next(d for d in record["primary_dimensions"] if d["name"] == "factual_fidelity")
            scores[judge], evidence[judge] = dimension["score"], dimension["evidence"]
        records.append({"slot": slot["id"], "case_id": slot["case_id"], "model": slot["model"], "arm": slot["arm"],
                        "trial": slot["trial"], "difference": scores["opus"] - scores["sol"],
                        "opus_score": scores["opus"], "sol_score": scores["sol"], "judge_evidence": evidence})
    chosen = select_packet(records)
    key, answers, pages = [], [], []
    for index, selected in enumerate(chosen, 1):
        label = f"H{index:02d}"
        case = case_map[selected["case_id"]]
        applied = read(source / "apply" / selected["model"] / selected["slot"] / "complete.json")
        key.append({"human_id": label, **selected, "family": case["family"], "split": case["split"]})
        answers.append({"id": label, "factual_fidelity": None, "evidence": "", "unsupported_claims_or_lost_qualifications": []})
        pages.append(f"## {label}\n\n### Task and supplied source\n\n{case['task']}\n\n### Response to review\n\n{applied['blinded']}\n")
    dest.mkdir(parents=True, exist_ok=True)
    (dest / "PACKET.md").write_text("# Human fidelity calibration packet\n\nRead README.md before scoring. Do not open PRIVATE-KEY.json until your answers are frozen.\n\n" + "\n".join(pages))
    write(dest / "ANSWERS.template.json", {"reviewer": None, "reviewed_at": None, "answers": answers})
    write(dest / "PRIVATE-KEY.json", key)
    write(dest / "selection.json", {"seed": 261117, "baseline": "2026-11-14-subscription-baseline",
          "items": len(chosen), "disagreements_per_apply_model": 6, "agreement_controls_per_apply_model": 3,
          "rule": "Largest absolute ordinal fidelity disagreements, opaque-ID tie break, one response per case/apply model; low/median/high agreement controls from distinct cases; shuffled.",
          "status": "AWAITING HUMAN REVIEW", "limits": "Deliberately selected, not representative; families may overlap; public inspected holdouts remain frozen. Another model is not a human adjudicator."})


def twitter(dest: Path) -> None:
    original = read(ROOT / "evals/results/2026-11-14-candidate-studies/historical-cases.json")
    selected = [r for r in original if r["panel"] == "twitter"]
    if len(selected) != 8:
        raise ValueError("Twitter source panel changed")
    cases = [{**r["case"], "facts": r["case"].get("facts", []), "source_kind": "synthetic", "original_suite": r["suite"]} for r in selected]
    write(dest, {"skill_name": "anti-slop-writing", "provenance": {
        "pull_request": 17, "branch_head": "3aa3f72dcabac82873c1ecb0d972e397198d5462",
        "exposure": "Public historical cases, not fresh sealed holdout. Original splits and all behavioral fields retained.",
        "dependence": "One conservative source/scaffold family; eight cases are not eight independent replications."
    }, "evals": cases})


def tables(dest: Path) -> None:
    rows = read(dest / "comparisons.json")
    text = ["# Candidate model/judge tables\n", "Normalized after−before deltas. Full intervals, exact tests and all fact/target/guard selections remain in comparisons.json. One-family panels are UNDERPOWERED; their bootstrap intervals do not establish precision.\n"]
    groups = sorted({(r["panel"], r["before_arm"], r["after_arm"]) for r in rows})
    for panel, before, after in groups:
        for selection in ("all", "holdout"):
            chosen = [r for r in rows if (r["panel"], r["before_arm"], r["after_arm"], r["selection"]) == (panel, before, after, selection)]
            if not chosen:
                continue
            text.extend([f"## {panel}: {before} → {after}, {selection}\n", "| Apply | Judge | Cases | Families | Δ fidelity | Δ task | Δ rewrite quality | Fidelity gate | Task gate |", "|---|---|---:|---:|---:|---:|---:|---|---|"])
            for model in ("sonnet", "sol"):
                for judge in ("opus", "sol"):
                    outcomes = {r["outcome"]: r for r in chosen if r["model"] == model and r["judge"] == judge}
                    fidelity, task, quality = [outcomes[n] for n in ("factual_fidelity", "task_fulfillment", "rewrite_quality")]
                    deltas = [f"{0 if abs(r['delta']) < 0.0005 else r['delta']:+.3f}" for r in (fidelity, task, quality)]
                    text.append(f"| {model} | {judge} | {fidelity['cases']} | {fidelity['clusters']} | {' | '.join(deltas)} | {fidelity['verdict']} | {task['verdict']} |")
            text.append("")
    (dest / "MODEL-TABLES.md").write_text("\n".join(text) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("branches", "packet", "twitter", "tables"))
    parser.add_argument("--dest", type=Path, required=True)
    parser.add_argument("--baseline", type=Path, default=ROOT / "eval-workspace/subscription-baseline")
    args = parser.parse_args()
    if args.command == "branches":
        branches(args.dest)
    elif args.command == "packet":
        packet(args.baseline, args.dest)
    elif args.command == "twitter":
        twitter(args.dest)
    else:
        tables(args.dest)


if __name__ == "__main__":
    main()
