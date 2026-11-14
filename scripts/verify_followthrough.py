#!/usr/bin/env python3
"""Archive/reproduce candidate and activation studies without any model calls."""
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import sys
import tarfile
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import candidate_studies
import live_activation
import review_followthrough

OUTPUTS = {
    "candidate": ("verification.json", "comparisons.json", "case-scores.json", "guard-results.json", "lengths.json", "judge-agreement.json", "decision.json", "standing-regressions.json", "MODEL-TABLES.md", "normalized", "primary-analysis"),
    "activation": ("rates.json", "summary.json"),
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def dump(path: Path, value) -> None:
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n")


def forbid_models(*args, **kwargs):
    raise RuntimeError("Offline verification must never invoke a model")


def verify_sources(kind: str, runtime: Path) -> None:
    source = runtime / ("analysis-sources.json" if kind == "candidate" else "frozen-sources.json")
    expected = json.loads(source.read_text())
    for relative, checksum in expected.items():
        if digest(ROOT / relative) != checksum:
            raise ValueError(f"source differs from registered analysis: {relative}; use the publication commit")


def independent_activation(runtime: Path) -> dict:
    manifest = json.loads((runtime / "manifest.json").read_text())
    queries = {q["id"]: q for q in json.loads((runtime / "queries.json").read_text())["queries"]}
    actual_paths = set((runtime / "runs").glob("*/*/complete.json"))
    expected_paths = {runtime / "runs" / s["client"] / s["id"] / "complete.json" for s in manifest["slots"]}
    if actual_paths != expected_paths or len(expected_paths) != 174:
        raise ValueError("activation slot set differs")
    observations = {}
    for slot in manifest["slots"]:
        folder = runtime / "runs" / slot["client"] / slot["id"]
        request = json.loads((folder / "request.json").read_text())
        if request["query"] != queries[slot["query_id"]]["query"] or request["model"] != live_activation.MODELS[slot["client"]]:
            raise ValueError("activation request identity differs")
        result = live_activation.saved_result(runtime, slot["client"], folder)
        if result != json.loads((folder / "complete.json").read_text()) or not result["valid"]:
            raise ValueError("invalid activation receipt")
        observations.setdefault((slot["client"], slot["query_id"]), []).append(result["activated"])
    counts = {}
    for client in live_activation.MODELS:
        positive, negative, true_positive, true_negative = 0, 0, 0, 0
        for (actor, qid), values in observations.items():
            if actor != client:
                continue
            if len(values) != 3:
                raise ValueError("activation query lacks three valid runs")
            majority = sum(values) >= 2
            if queries[qid]["should_trigger"]:
                positive += 1
                true_positive += majority
            else:
                negative += 1
                true_negative += not majority
        counts[client] = {"positive_queries": positive, "true_positive": true_positive, "negative_queries": negative, "true_negative": true_negative}
    return counts


def usage(kind: str, runtime: Path) -> dict:
    paths = list(runtime.glob("apply/*/*/attempt-*/stdout.txt")) + list(runtime.glob("judge/*/*/attempt-*/stdout.txt")) if kind == "candidate" else list(runtime.rglob("stdout.jsonl"))
    hashes, response_ids, ids_by_hash = set(), set(), {}
    counters, missing, traces, repeated_ids = 0.0, 0, 0, []
    for path in sorted(paths):
        raw = path.read_text()
        sha = digest(path)
        if not raw.strip():
            traces += 1
            missing += 1
            continue
        if sha in hashes:
            continue  # selected-attempt/pilot copies are not extra provider usage
        hashes.add(sha)
        traces += 1
        ids, cost = set(), None
        try:
            if kind == "candidate" and json.loads((path.parent / "request.json").read_text())["provider"] == "openai":
                envelope = json.loads(raw)
                result = envelope["result"]
                ids.add(result["responseId"])
                cost = result.get("usage", {}).get("cost", {}).get("total")
            else:
                events = [json.loads(line) for line in raw.splitlines() if line.strip()]
                results = [e for e in events if e.get("type") == "result"]
                if len(results) == 1 and "messages" in results[0]:
                    messages = [m for m in results[0]["messages"] if m.get("role") == "assistant"]
                    ids = {m["responseId"] for m in messages if m.get("responseId")}
                    values = [m.get("usage", {}).get("cost", {}).get("total") for m in messages]
                    cost = sum(values) if values and all(v is not None for v in values) else None
                else:
                    ids = {e["message"]["id"] for e in events if e.get("type") == "assistant" and e.get("message", {}).get("id")}
                    cost = results[0].get("total_cost_usd") if len(results) == 1 else None
        except (ValueError, KeyError, TypeError):
            pass
        ids_by_hash[sha] = ids
        overlap = ids & response_ids
        if overlap:
            repeated_ids.extend(sorted(overlap))
        response_ids.update(ids)
        if cost is None:
            missing += 1
        else:
            counters += cost
    selected_count = None
    if kind == "candidate":
        selected = list(runtime.glob("apply/*/*/complete.json")) + list(runtime.glob("judge/*/*/complete.json"))
        selected_ids = []
        for path in selected:
            attempt = json.loads(path.read_text())["attempt"]
            ids = ids_by_hash[digest(path.parent / f"attempt-{attempt}" / "stdout.txt")]
            if len(ids) != 1 or not all(isinstance(value, str) and value.strip() for value in ids):
                raise ValueError("candidate slot lacks exactly one returned provider response")
            selected_ids.extend(ids)
        selected_count = len(set(selected_ids))
        if len(selected) != 3366 or selected_count != 3366:
            raise ValueError("candidate completed provider response receipts missing or reused")
    return {"distinct_raw_traces": traces, "unique_returned_provider_response_ids": len(response_ids), "unique_selected_candidate_responses": selected_count, "repeated_ids_across_nonidentical_trace_copies": repeated_ids,
            "returned_list_price_equivalent_usd": counters, "traces_without_complete_cost_counters": missing,
            "scope": "All retained attempts/pilots, deduplicating byte-identical copies. Counters are not subscription invoices; missing remote usage is unknown, not zero."}


def inventory(dest: Path) -> None:
    dump(dest / "checksums.json", {str(p.relative_to(dest)): digest(p) for p in sorted(dest.rglob("*")) if p.is_file() and p.name not in ("checksums.json", "reproduction.json")})


def publish(kind: str, runtime: Path, dest: Path) -> None:
    if (runtime / "process-exit-code.txt").read_text().strip() != "0":
        raise ValueError("study process did not finish successfully")
    verify_sources(kind, runtime)
    dest.mkdir(parents=True, exist_ok=True)
    for name in OUTPUTS[kind]:
        source, target = runtime / name, dest / name
        if source.is_dir():
            shutil.copytree(source, target, dirs_exist_ok=True)
        else:
            shutil.copyfile(source, target)
    dump(dest / "usage.json", usage(kind, runtime))
    for name in ("process-started.txt", "process-ended.txt", "process-exit-code.txt", "process.log", "pilot-summary.json"):
        if (runtime / name).exists():
            shutil.copyfile(runtime / name, dest / name)
    with tarfile.open(dest / "trials.tar.gz", "w:gz") as archive:
        archive.add(runtime, arcname=runtime.name)
    inventory(dest)


def verify(kind: str, dest: Path) -> None:
    expected = json.loads((dest / "checksums.json").read_text())
    for name, checksum in expected.items():
        if digest(dest / name) != checksum:
            raise ValueError(f"published checksum mismatch: {name}")
    candidate_studies.base.invoke = forbid_models
    with tempfile.TemporaryDirectory(prefix="asw-offline-replay-") as directory:
        root = Path(directory)
        with tarfile.open(dest / "trials.tar.gz") as archive:
            archive.extractall(root, filter="data")
        runtimes = [p for p in root.iterdir() if p.is_dir()]
        if len(runtimes) != 1:
            raise ValueError("unexpected archive root")
        runtime = runtimes[0]
        verify_sources(kind, runtime)
        if usage(kind, runtime) != json.loads((dest / "usage.json").read_text()):
            raise ValueError("returned usage accounting differs")
        counts = independent_activation(runtime) if kind == "activation" else None
        (candidate_studies.analyze if kind == "candidate" else live_activation.analyze)(runtime)
        if kind == "candidate":
            review_followthrough.tables(runtime)
        if counts is not None:
            summary = json.loads((runtime / "summary.json").read_text())
            for row in summary["summaries"]:
                if row["selection"] == "all":
                    values = counts[row["client"]]
                    if row["sensitivity"] != values["true_positive"] / values["positive_queries"] or row["specificity"] != values["true_negative"] / values["negative_queries"]:
                        raise ValueError("independent activation arithmetic differs")
        checked = []
        for name in OUTPUTS[kind]:
            source = runtime / name
            files = sorted(source.rglob("*")) if source.is_dir() else [source]
            for path in files:
                if path.is_file():
                    relative = path.relative_to(runtime)
                    if digest(path) != digest(dest / relative):
                        raise ValueError(f"offline reproduction differs: {relative}")
                    checked.append(str(relative))
        report = {"status": "passed", "model_calls": 0, "published_checksums_verified": len(expected), "byte_identical_reproduced_files": checked, "independent_activation_counts": counts}
        dump(dest / "reproduction.json", report)
        print(json.dumps(report, indent=2))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("publish", "verify", "checksums"))
    parser.add_argument("--kind", choices=tuple(OUTPUTS), required=True)
    parser.add_argument("--runtime", type=Path)
    parser.add_argument("--dest", type=Path, required=True)
    args = parser.parse_args()
    if args.command == "publish":
        if args.runtime is None:
            parser.error("publish requires --runtime")
        publish(args.kind, args.runtime, args.dest)
    elif args.command == "verify":
        verify(args.kind, args.dest)
    else:
        inventory(args.dest)


if __name__ == "__main__":
    main()
