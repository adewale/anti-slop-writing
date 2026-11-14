#!/usr/bin/env python3
"""Model-free publication/replay of the extraction-audit checkpoint, not writing scores."""
from __future__ import annotations

import argparse
import hashlib
import json
import random
import shutil
import sys
import tarfile
import tempfile
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import rewrite_rejudge as rr

BASELINE = ROOT / "evals/results/2026-11-14-subscription-baseline/trials.tar.gz"
BASELINE_SHA = "ac9a292615299cd5160a08772118f1d76a2d5b273bb5b19e18b589be2c08dd23"
GENERATED = ("checkpoint.json", "receipts.json", "reliability.json", "REVIEW-PACKET.md",
             "REVIEW-ANSWERS.template.json", "REVIEW-PRIVATE-KEY.json", "review-selection.json")


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def selected(path: Path, model: str, prompt: str, finish) -> dict:
    """Bind each selected record to its exact retained request and audited provider response."""
    complete = rr.sb.read_json(path / "complete.json")
    number = complete["attempt"]
    if type(number) is not int or not 1 <= number <= 3:
        raise ValueError("invalid selected attempt")
    attempt = path / f"attempt-{number}"
    request = rr.sb.read_json(attempt / "request.json")
    if (request["model"] != model or request["prompt_sha256"] != rr.sb.sha(prompt)
            or request["returncode"] != 0 or request["tools"] != []
            or request["effort"] != "medium" or request["system_prompt"] != "You are a helpful assistant."
            or (attempt / "prompt.txt").read_text() != prompt):
        raise ValueError("selected request differs")
    provider = "claude" if model.startswith("claude-") else "openai"
    if request["provider"] != provider:
        raise ValueError("provider differs")
    raw = (attempt / "stdout.txt").read_text()
    text, usage = rr.sb.audit_response(provider, raw, model)
    expected = finish(rr.sb.parse_object(text)) | {
        "attempt": number, "usage": usage, "input_sha256": rr.sb.sha(model + "\n" + prompt)}
    if complete != expected:
        raise ValueError("selected record differs from raw response")
    if provider == "openai":
        result = json.loads(raw)["result"]
        ids = {result["responseId"]}
        cost = result["usage"]["cost"]["total"]
    else:
        events = [json.loads(line) for line in raw.splitlines() if line.strip()]
        ids = {e["message"]["id"] for e in events if e.get("type") == "assistant"}
        cost = next(e["total_cost_usd"] for e in events if e.get("type") == "result")
    if len(ids) != 1 or not all(isinstance(x, str) and x.strip() for x in ids):
        raise ValueError("selected slot needs exactly one provider response id")
    return {"response_id": next(iter(ids)), "model": model,
            "prompt_sha256": request["prompt_sha256"], "stdout_sha256": digest(attempt / "stdout.txt"),
            "returned_list_price_equivalent_usd": cost,
            "started": request["started"], "ended": request["started"] + request["seconds"]}


def baseline_response_ids(baseline: Path) -> set[str]:
    ids = set()
    paths = list(baseline.glob("apply/*/*/complete.json")) + list(baseline.glob("judge/*/*/complete.json"))
    for path in paths:
        complete = rr.sb.read_json(path)
        if "attempt" not in complete:  # Minimal offline test fixtures have no historical provider calls.
            continue
        attempt = path.parent / f"attempt-{complete['attempt']}"
        request = rr.sb.read_json(attempt / "request.json")
        raw = (attempt / "stdout.txt").read_text()
        if request["provider"] == "openai":
            ids.add(json.loads(raw)["result"]["responseId"])
        else:
            ids.update(e["message"]["id"] for e in map(json.loads, raw.splitlines()) if e.get("type") == "assistant")
    return ids


def inspect(baseline: Path, runtime: Path) -> tuple[dict, list, list]:
    manifest, cases = rr.load(baseline, runtime)
    receipts, reliability, expected_paths = [], [], set()
    if list((runtime / "judge").glob("*/*/complete.json")):
        raise ValueError("this checkpoint publication must not contain writing judgments")
    for output in manifest["outputs"]:
        original = rr.baseline_output(baseline, output)["output"]
        eid, task = output["extraction_id"], cases[output["case_id"]]["task"]
        routes = [rr.EXTRACTOR] + ([rr.RELIABILITY_EXTRACTOR]
                  if output["baseline_id"] in manifest["reliability_outputs"] else [])
        for route in routes:
            path = runtime / "extract" / route / eid
            def finish(result, original=original, eid=eid):
                spans = rr.validate_extraction(result, original, eid)
                text = rr.render(spans)
                if result["disposition"] != "none" and not text.strip():
                    raise ValueError("non-none extraction renders empty")
                return {"disposition": result["disposition"], "spans": spans,
                        "deliverable": text, "words": len(text.split())}
            receipts.append(selected(path, rr.sb.JUDGES[route], rr.extract_prompt(task, original, eid), finish)
                            | {"stage": "extract", "route": route, "id": eid})
            expected_paths.add(path / "complete.json")
        extracted = rr.deliverable(runtime, output)
        path = runtime / "audit" / eid
        def finish_audit(result, eid=eid):
            return {"checks": result["checks"], "passed": rr.validate_audit(result, eid)}
        prompt = rr.audit_prompt(task, original, {"disposition": extracted["disposition"],
                                                 "deliverable": extracted["deliverable"]}, eid)
        receipts.append(selected(path, rr.sb.JUDGES[rr.RELIABILITY_EXTRACTOR], prompt, finish_audit)
                        | {"stage": "audit", "id": eid})
        expected_paths.add(path / "complete.json")
        if len(routes) == 2:
            alternate = rr.deliverable(runtime, output, rr.RELIABILITY_EXTRACTOR)
            reliability.append({"baseline_id": output["baseline_id"], "extraction_id": eid,
                "exact": rr.normalize(extracted["deliverable"]) == rr.normalize(alternate["deliverable"]),
                "jaccard": rr.token_jaccard(extracted["deliverable"], alternate["deliverable"]),
                "same_disposition": extracted["disposition"] == alternate["disposition"]})
    actual_paths = set(runtime.glob("extract/*/*/complete.json")) | set(runtime.glob("audit/*/complete.json"))
    if actual_paths != expected_paths:
        raise ValueError("selected slot set differs")
    raw_paths = set(runtime.glob("extract/*/*/attempt-*/stdout.txt")) | set(runtime.glob("audit/*/attempt-*/stdout.txt"))
    if len(raw_paths) != len(receipts):
        raise ValueError("unselected attempts require additional usage accounting before publication")
    selected_ids = {r["response_id"] for r in receipts}
    if len(selected_ids) != len(receipts):
        raise ValueError("provider response id reused")
    historical_ids = baseline_response_ids(baseline)
    if selected_ids & historical_ids:
        raise ValueError("new provider response id overlaps baseline")
    report = rr.audit_report(manifest, runtime)
    cells = []
    for model in rr.sb.APPLY_MODELS:
        for arm in rr.ARMS:
            rows = [r for r in report["rows"] if (r["model"], r["arm"]) == (model, arm)]
            cells.append({"model": model, "arm": arm, "audited": len(rows),
                          "flagged": sum(not r["passed"] for r in rows)})
    n = len(reliability)
    summary = {
        "status": "blocked before judging" if report["failed"] or report["missing"] else "audit passed; no writing scores published",
        "registration_commit": (runtime / "registration-commit.txt").read_text().strip(),
        "baseline_archive_sha256": BASELINE_SHA,
        "primary_extractions": len(manifest["outputs"]), "reliability_extractions": n,
        "audits": report["outputs_audited"], "flagged_outputs": report["failed"],
        "missing_audits": report["missing"], "writing_judgments": 0,
        "flagged_by_model_arm": cells,
        "failed_checks": dict(sorted(Counter(c["name"] for r in report["rows"]
                                                for c in r["checks"] if not c["pass"]).items())),
        "no_deliverable_outputs": sum(rr.deliverable(runtime, o)["disposition"] == "none" for o in manifest["outputs"]),
        "reliability": {"pairs": n,
            "exact_rate": sum(r["exact"] for r in reliability) / n if n else None,
            "mean_jaccard": sum(r["jaccard"] for r in reliability) / n if n else None,
            "disposition_agreement": sum(r["same_disposition"] for r in reliability) / n if n else None},
        "selected_provider_responses": len(receipts),
        "unique_returned_provider_response_ids": len(selected_ids),
        "baseline_selected_provider_response_ids": len(historical_ids), "response_id_overlap_with_baseline": 0,
        "returned_list_price_equivalent_usd": sum(r["returned_list_price_equivalent_usd"] for r in receipts),
        "first_request_started": min(r["started"] for r in receipts),
        "last_request_ended": max(r["ended"] for r in receipts),
        "limits": "Model audit flags are not human-confirmed defects or skill outcomes. Counters are not subscription invoices. No new writing-score inference."}
    return summary, receipts, reliability


def packet(baseline: Path, runtime: Path, target: Path) -> None:
    manifest, cases = rr.load(baseline, runtime)
    audit = rr.sb.read_json(runtime / "extraction-audit.json")
    flagged = {r["baseline_id"] for r in audit["rows"] if not r["passed"]}
    controls = set(manifest["reliability_outputs"])
    outputs = sorted((o for o in manifest["outputs"] if o["baseline_id"] in flagged | controls), key=lambda o: o["extraction_id"])
    random.Random(rr.SEED + 3).shuffle(outputs)
    lines = ["# Blind extraction review — not fidelity calibration", "",
        "Review the task, original response and extracted view. For each check, record a boolean",
        "and evidence in a copy of `REVIEW-ANSWERS.template.json`. Check completeness, preserved",
        "qualifications, separation from diagnosis, and correct disposition. Necessary context",
        "may cross template fields. Decide whether removed labels carry meaning or are cosmetic.",
        "`mixed` may mean more than one deliverable kind, not necessarily different items.",
        "Do not open `REVIEW-PRIVATE-KEY.json`, the model audits or the manifest until answers",
        "are frozen and dated. Style may still reveal an arm. This enriched packet cannot",
        "estimate population error, and reviewing it does not calibrate the writing judges.", ""]
    answers, key = [], []
    def quote(text):
        return "\n".join("> " + line for line in text.splitlines()) or "> (empty)"
    for number, output in enumerate(outputs, 1):
        rid = f"R{number:03}"
        extracted = rr.deliverable(runtime, output)
        lines.extend([f"## {rid}", "", "### Task", quote(cases[output["case_id"]]["task"]), "",
                      "### Original response", quote(rr.baseline_output(baseline, output)["output"]), "",
                      f"### Extracted view (disposition: {extracted['disposition']})", quote(extracted["deliverable"]), ""])
        answers.append({"id": rid, "checks": [{"name": name, "pass": None, "evidence": ""} for name in rr.AUDIT_CHECKS]})
        key.append({"id": rid, **output, "audit_flagged": output["baseline_id"] in flagged,
                    "preselected_control": output["baseline_id"] in controls})
    target.mkdir(parents=True, exist_ok=True)
    (target / "REVIEW-PACKET.md").write_text("\n".join(lines))
    rr.sb.dump(target / "REVIEW-ANSWERS.template.json", {"reviewer": "", "frozen_at": "", "items": answers})
    rr.sb.dump(target / "REVIEW-PRIVATE-KEY.json", key)
    rr.sb.dump(target / "review-selection.json", {"seed": rr.SEED + 3,
        "rule": "all flagged outputs union the originally preregistered 44 reliability outputs, deduplicated",
        "flagged": len(flagged), "preselected_controls": len(controls), "overlap": len(flagged & controls), "items": len(outputs),
        "limits": "Enriched instrument-review sample, not a population error estimate or human writing-judge calibration."})


def generate(baseline: Path, runtime: Path, target: Path) -> None:
    summary, receipts, reliability = inspect(baseline, runtime)
    rr.sb.dump(target / "checkpoint.json", summary)
    rr.sb.dump(target / "receipts.json", receipts)
    rr.sb.dump(target / "reliability.json", reliability)
    packet(baseline, runtime, target)


def inventory(dest: Path) -> None:
    rr.sb.dump(dest / "checksums.json", {str(p.relative_to(dest)): digest(p) for p in sorted(dest.rglob("*"))
        if p.is_file() and p.name not in ("checksums.json", "reproduction.json")})


def publish(baseline: Path, runtime: Path, dest: Path) -> None:
    generate(baseline, runtime, runtime)
    rr.sb.dump(runtime / "publication-sources.json", {name: digest(ROOT / name)
        for name in (*rr.SOURCES, "scripts/review_rewrite_rejudge.py")})
    for name in (*GENERATED, "manifest.json", "prompt-templates.json", "publication-sources.json", "extraction-audit.json",
                 "extract-status.json", "audit-status.json", "extract.log", "audit.log", "registration-commit.txt",
                 "process-started.txt", "process-ended.txt", "process-status.json"):
        shutil.copyfile(runtime / name, dest / name)
    with tarfile.open(dest / "trials.tar.gz", "w:gz") as archive:
        archive.add(runtime, arcname="rewrite-only-rejudge")
    inventory(dest)


def verify(dest: Path) -> None:
    expected = rr.sb.read_json(dest / "checksums.json")
    for name, checksum in expected.items():
        path = (dest / name).resolve()
        if not path.is_relative_to(dest.resolve()) or digest(path) != checksum:
            raise ValueError(f"published checksum mismatch: {name}")
    if digest(BASELINE) != BASELINE_SHA:
        raise ValueError("baseline archive changed")
    for name, checksum in rr.sb.read_json(dest / "publication-sources.json").items():
        if digest(ROOT / name) != checksum:
            raise ValueError(f"publication source differs: {name}; use publication commit")
    def forbidden(*args, **kwargs):
        raise RuntimeError("offline replay must never invoke a model")
    original = rr.sb.invoke
    rr.sb.invoke = forbidden
    try:
        with tempfile.TemporaryDirectory(prefix="asw-rewrite-replay-") as temp:
            root = Path(temp)
            for archive_path in (BASELINE, dest / "trials.tar.gz"):
                with tarfile.open(archive_path) as archive:
                    archive.extractall(root, filter="data")
            baseline, runtime = root / "subscription-baseline", root / "rewrite-only-rejudge"
            target = root / "reproduced"
            target.mkdir()
            generate(baseline, runtime, target)
            for name in GENERATED:
                if (target / name).read_bytes() != (dest / name).read_bytes():
                    raise ValueError(f"offline reproduction differs: {name}")
    finally:
        rr.sb.invoke = original
    rr.sb.dump(dest / "reproduction.json", {"status": "passed", "model_calls": 0,
        "published_checksums_verified": len(expected), "byte_identical_reproduced_files": list(GENERATED)})
    print("Offline replay passed; no model calls; all selected provider receipts and review artifacts verified.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("publish", "verify", "checksums"))
    parser.add_argument("--baseline", type=Path)
    parser.add_argument("--runtime", type=Path)
    parser.add_argument("--dest", type=Path, required=True)
    args = parser.parse_args()
    if args.command == "publish":
        if args.baseline is None or args.runtime is None:
            parser.error("publish requires --baseline and --runtime")
        publish(args.baseline, args.runtime, args.dest)
    elif args.command == "verify":
        verify(args.dest)
    else:
        inventory(args.dest)


if __name__ == "__main__":
    main()
