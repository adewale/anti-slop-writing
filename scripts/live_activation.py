#!/usr/bin/env python3
"""Initial-turn skill loading in controlled live Pi SDK and Claude Code sessions.

Only pilot/run call providers. Models receive verbatim task queries, never labels or
routing questions. Successful instruction delivery, not self-report, defines activation.
"""
from __future__ import annotations

import argparse
import concurrent.futures
import json
import os
import random
import re
import shutil
import subprocess
import sys
import tempfile
import threading
import time
import uuid
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import subscription_baseline as base

MODELS = {"pi": "gpt-6.1-sol", "claude": "claude-sonnet-5-5"}
SEED = 261116
# Built-in skills observed in the first native CLI pilot, not user/project resources.
CLAUDE_BUILTINS = {
    "deep-research", "design", "design-sync", "dataviz", "update-config", "verify",
    "debug", "code-review", "simplify", "batch", "fewer-permission-prompts", "doctor",
    "loop", "schedule", "claude-api", "workflow-authoring", "run", "run-skill-generator",
    "plugin-authoring",
}
CLAUDE_TARGETS = {"anti-slop-writing", "local-writing:anti-slop-writing"}


def body(text: str) -> str:
    return re.sub(r"\A---\r?\n.*?\r?\n---\r?\n", "", text, count=1, flags=re.DOTALL).strip()


def normalized(text: str) -> str:
    text = re.sub(r"(?m)^\s*\d+→", "", text)
    return " ".join(text.split())


def content_text(content) -> str:
    if isinstance(content, str):
        return content
    return "\n".join(c.get("text", "") for c in content if isinstance(c, dict) and c.get("type") == "text")


def same_file(requested: str, canonical: str, cwd: str) -> bool:
    p = Path(requested)
    return p.is_absolute() and str(p.resolve()) == canonical or str((Path(cwd) / p).resolve()) == canonical


def classify_pi(events: list[dict], skill: str, canonical: str) -> dict:
    inits = [e for e in events if e.get("type") == "init"]
    results = [e for e in events if e.get("type") == "result"]
    if len(inits) != 1 or len(results) != 1:
        raise ValueError("incomplete Pi trace")
    init, result = inits[0], results[0]
    if init.get("model") != MODELS["pi"] or result.get("model") != MODELS["pi"] or result.get("success") is not True:
        raise ValueError("Pi model/completion mismatch")
    skills = init.get("skills", [])
    if len(skills) != 1 or skills[0].get("name") != "anti-slop-writing" or skills[0].get("filePath") != canonical or init.get("tools") != ["read"]:
        raise ValueError("unexpected Pi resource inventory")
    if normalized(body(skill)) in normalized(init.get("systemPrompt", "")):
        raise ValueError("skill body preloaded before routing")
    messages = result["messages"]
    assistants = [m for m in messages if m.get("role") == "assistant"]
    if not assistants or any(m.get("model") != MODELS["pi"] for m in assistants) or assistants[-1].get("stopReason") != "stop":
        raise ValueError("incomplete Pi assistant or model drift")
    calls = {}
    for m in assistants:
        for c in m.get("content", []):
            if c.get("type") == "toolCall":
                if c.get("name") != "read":
                    raise ValueError("unexpected Pi tool")
                if same_file(c.get("arguments", {}).get("path", ""), canonical, init["cwd"]):
                    calls[c["id"]] = c
    successful, failed = [], []
    for m in messages:
        if m.get("role") == "toolResult" and m.get("toolCallId") in calls:
            if m.get("isError"):
                failed.append(m["toolCallId"])
            elif normalized(body(skill)) in normalized(content_text(m.get("content", []))):
                successful.append(m["toolCallId"])
    return {"advertised": True, "attempted": bool(calls), "activated": bool(successful),
            "valid": not failed, "successful_loads": successful, "failed_loads": failed,
            "assistant_requests": len(assistants)}


def classify_claude(events: list[dict], skill: str, canonical: str) -> dict:
    inits = [e for e in events if e.get("type") == "system" and e.get("subtype") == "init"]
    results = [e for e in events if e.get("type") == "result"]
    if len(inits) != 1 or len(results) != 1:
        raise ValueError("incomplete Claude trace")
    init, result = inits[0], results[0]
    if result.get("is_error") or result.get("subtype") != "success" or set(result.get("modelUsage", {})) != {MODELS["claude"]}:
        raise ValueError("Claude model/completion mismatch")
    inventory = set(init.get("skills", []))
    if len(inventory & CLAUDE_TARGETS) != 1 or inventory - CLAUDE_TARGETS - CLAUDE_BUILTINS or set(init.get("tools", [])) - {"Read", "Skill"} or init.get("mcp_servers"):
        raise ValueError("unexpected Claude skill/tool/MCP inventory")
    builtin_plugins = {"cc-plugin-agents-md", "cc-plugin-telemetry", "cc-plugin-privacy", "cc-plugin-plugin-authoring"}
    for plugin in init.get("plugins", []):
        name = plugin.get("name")
        builtin = name in builtin_plugins and plugin.get("path") == "builtin" and plugin.get("source") == f"{name}@builtin"
        local = name == "local-writing" and plugin.get("path") == str(Path(canonical).parents[2]) and plugin.get("source") == "local-writing@inline"
        if not (builtin or local):
            raise ValueError("unexpected external Claude plugin")
    calls, successes, failures = {}, {}, []
    delivered_context = []
    for e in events:
        role = e.get("type")
        blocks = e.get("message", {}).get("content", [])
        if role == "assistant":
            for c in blocks:
                if c.get("type") != "tool_use":
                    continue
                name, arguments = c["name"], c.get("input", {})
                if name not in ("Skill", "Read"):
                    raise ValueError("unexpected Claude tool")
                match = name == "Skill" and arguments.get("skill") in CLAUDE_TARGETS
                match |= name == "Read" and same_file(arguments.get("file_path", ""), canonical, init.get("cwd", str(Path(canonical).parent)))
                if match:
                    calls[c["id"]] = name
        if role == "user":
            for c in blocks:
                if c.get("type") == "tool_result" and c.get("tool_use_id") in calls:
                    if c.get("is_error"):
                        failures.append(c["tool_use_id"])
                    else:
                        successes[c["tool_use_id"]] = content_text(c.get("content", ""))
                if c.get("type") == "text":
                    delivered_context.append(c.get("text", ""))
    target = normalized(body(skill))
    delivered = [cid for cid, text in successes.items() if target in normalized(text)
                 or calls[cid] == "Skill" and any(target in normalized(t) for t in delivered_context)]
    return {"advertised": True, "attempted": bool(calls), "activated": bool(delivered),
            "valid": not failures, "successful_loads": delivered, "failed_loads": failures,
            "assistant_requests": result.get("num_turns")}


def prepare(dest: Path) -> None:
    if dest.exists() and any(dest.iterdir()):
        raise ValueError("refusing to overwrite frozen routing inputs")
    dest.mkdir(parents=True, exist_ok=True)
    shutil.copytree(ROOT / "skills/anti-slop-writing", dest / "frozen-skill")
    data = base.read_json(ROOT / "evals/trigger-queries.json")
    base.dump(dest / "queries.json", data)
    slots = []
    for client in MODELS:
        for q in data["queries"]:
            for trial in range(1, data["runs_per_query"] + 1):
                slots.append({"id": base.sha(f"route-v1|{client}|{q['id']}|{trial}")[:24],
                              "client": client, "query_id": q["id"], "trial": trial})
    random.Random(SEED).shuffle(slots)
    base.dump(dest / "manifest.json", {"seed": SEED, "instrument_revision": 3, "models": MODELS, "slots": slots,
        "queries_sha256": base.sha((dest / "queries.json").read_text()),
        "skill_hashes": {str(p.relative_to(dest / "frozen-skill")): base.sha(p.read_text()) for p in (dest / "frozen-skill").rglob("*.md")},
        "clients": {"pi": "Pi 1.4.0 controlled SDK AgentSession (not stock CLI/TUI)", "claude": "Claude Code 2.1.323 restricted CLI with explicit local-writing plugin"},
        "unavailable": {"codex": "0.145.0: recorded subscription probe rejects gpt-6.1-sol; no model substitution preregistered", "opencode": "Not installed on PATH or checked conventional locations; not installed by this study"}})
    base.dump(dest / "frozen-sources.json", {str(p.relative_to(ROOT)): base.sha(p.read_text()) for p in (
        ROOT / "scripts/live_activation.py", ROOT / "scripts/activation_model.mjs", ROOT / "scripts/subscription_model.mjs")})


def run_one(dest: Path, client: str, query: str, output: Path, forced: bool = False) -> dict:
    output.mkdir(parents=True, exist_ok=False)
    with tempfile.TemporaryDirectory(prefix="r-" + uuid.uuid4().hex[:8] + "-") as directory:
        workspace = Path(directory).resolve() / "workspace"
        workspace.mkdir()
        plugin_root = workspace / "resources/local-writing"
        skill_root = plugin_root / "skills/anti-slop-writing" if client == "claude" else workspace / "resources/anti-slop-writing"
        shutil.copytree(dest / "frozen-skill", skill_root)
        if client == "claude":
            base.dump(plugin_root / ".claude-plugin/plugin.json", {"name": "local-writing", "version": "1.0.0", "description": "Local writing instructions"})
        canonical = str(skill_root / "SKILL.md")
        if forced:
            query = f"Read {canonical} in full, then state its first heading. Do not edit any file."
        request = {"model": MODELS[client], "query": query, "cwd": str(workspace),
                   "skillRoot": str(skill_root), "agentDir": str(Path(directory).resolve() / "config")}
        if client == "pi":
            command = ["node", str(ROOT / "scripts/activation_model.mjs"), os.environ["ASW_PI_SDK"]]
            stdin = json.dumps(request)
        else:
            command = ["claude", "--print", "--restricted", "--tools", "Read,Skill",
                       "--allowedTools", "Read", "Skill", "--permission-mode", "dontAsk", "--permission-prompts", "none",
                       "--setting-sources", "", "--strict-mcp-config", "--mcp-config", '{"mcpServers":{}}',
                       "--no-session-persistence", "--session-id", str(uuid.uuid4()), "--plugin-dir", str(plugin_root),
                       "--model", MODELS[client], "--effort", "low", "--output-format", "stream-json", "--verbose"]
            stdin = query
        env = os.environ.copy()
        for key in ("ANTHROPIC_API_KEY", "ANTHROPIC_AUTH_TOKEN", "ANTHROPIC_OAUTH_TOKEN"):
            env.pop(key, None)
        started = time.time()
        base.dump(output / "request.json", {**request, "canonical_skill": canonical, "command": command, "started": started, "forced_control": forced})
        try:
            result = subprocess.run(command, input=stdin, text=True, capture_output=True, cwd=workspace, env=env, timeout=240)
            stdout, stderr, code = result.stdout, result.stderr, result.returncode
        except subprocess.TimeoutExpired as exc:
            stdout = exc.stdout.decode() if isinstance(exc.stdout, bytes) else exc.stdout or ""
            stderr = exc.stderr.decode() if isinstance(exc.stderr, bytes) else exc.stderr or ""
            code = -1
        (output / "stdout.jsonl").write_text(stdout)
        (output / "stderr.txt").write_text(stderr)
        base.dump(output / "process.json", {"returncode": code, "seconds": time.time() - started})
        if code:
            raise ValueError(f"{client} process failed ({code}): {stderr[-200:]}")
        events = [json.loads(line) for line in stdout.splitlines() if line.strip()]
        text = (dest / "frozen-skill/SKILL.md").read_text()
        classify = classify_pi if client == "pi" else classify_claude
        normalized_result = classify(events, text, canonical)
        base.dump(output / "complete.json", normalized_result)
        return normalized_result


def validate_frozen(dest: Path) -> dict:
    manifest = base.read_json(dest / "manifest.json")
    if manifest["models"] != MODELS or base.sha((dest / "queries.json").read_text()) != manifest["queries_sha256"]:
        raise ValueError("frozen models/queries changed")
    for p, checksum in manifest["skill_hashes"].items():
        if base.sha((dest / "frozen-skill" / p).read_text()) != checksum:
            raise ValueError("frozen skill changed")
    return manifest


def saved_result(dest: Path, client: str, folder: Path) -> dict:
    request = base.read_json(folder / "request.json")
    if base.read_json(folder / "process.json")["returncode"] != 0:
        raise ValueError("saved client process did not complete")
    events = [json.loads(line) for line in (folder / "stdout.jsonl").read_text().splitlines() if line.strip()]
    classify = classify_pi if client == "pi" else classify_claude
    return classify(events, (dest / "frozen-skill/SKILL.md").read_text(), request["canonical_skill"])


def pilot(dest: Path) -> None:
    validate_frozen(dest)
    queries = {q["id"]: q for q in base.read_json(dest / "queries.json")["queries"]}
    summary = {}
    for client in MODELS:
        results = []
        for name, qid, forced in (("positive", "pos-readme-polish", False), ("negative", "neg-em-dash-mechanical", False), ("forced", "pos-readme-polish", True)):
            path = dest / "pilot" / client / name
            try:
                if path.exists():
                    result = saved_result(dest, client, path)
                    base.dump(path / "complete.json", result)
                else:
                    result = run_one(dest, client, queries[qid]["query"], path, forced)
                results.append({"control": name, **result})
            except (ValueError, OSError) as exc:
                base.dump(path / "failure.json", {"error": str(exc)})
                results.append({"control": name, "error": str(exc)})
                break
        summary[client] = {"results": results, "eligible": len(results) == 3 and all("error" not in r and r["valid"] for r in results) and results[-1]["activated"]}
    base.dump(dest / "pilot-summary.json", summary)
    print(json.dumps(summary, indent=2))


def run(dest: Path, workers: int) -> None:
    manifest = validate_frozen(dest)
    pilots = base.read_json(dest / "pilot-summary.json")
    queries = {q["id"]: q for q in base.read_json(dest / "queries.json")["queries"]}
    slots = [s for s in manifest["slots"] if pilots[s["client"]]["eligible"]]

    stop = threading.Event()

    def worker(slot):
        if stop.is_set():
            return
        folder = dest / "runs" / slot["client"] / slot["id"]
        if (folder / "complete.json").exists():
            return
        for number in range(1, 4):
            attempt = folder / f"attempt-{number}"
            if stop.is_set():
                return
            if attempt.exists():
                continue
            try:
                result = run_one(dest, slot["client"], queries[slot["query_id"]]["query"], attempt)
                for name in ("request.json", "stdout.jsonl", "stderr.txt", "process.json", "complete.json"):
                    shutil.copyfile(attempt / name, folder / name)
                base.dump(folder / "selected-attempt.json", {"attempt": number})
                if not result["valid"]:
                    base.dump(folder / "invalid.json", {"reason": "attempted load failed; do not count as nonactivation or retry a routing outcome"})
                return
            except (ValueError, OSError) as exc:
                base.dump(attempt / "failure.json", {"error": str(exc)})
                if any(word in str(exc).lower() for word in ("model", "inventory", "authentication", "unauthorized", "401", "usage limit", "rate limit", "hit your limit")):
                    stop.set()
                    raise
        stop.set()
        raise ValueError(f"routing slot {slot['id']} exhausted three attempts")

    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as pool:
        for i, _ in enumerate(pool.map(worker, slots), 1):
            if i % 10 == 0 or i == len(slots):
                print(f"routing {i}/{len(slots)}", flush=True)


def analyze(dest: Path) -> None:
    manifest = validate_frozen(dest)
    pilots = base.read_json(dest / "pilot-summary.json")
    queries = {q["id"]: q for q in base.read_json(dest / "queries.json")["queries"]}
    grouped = defaultdict(list)
    for slot in manifest["slots"]:
        if not pilots[slot["client"]]["eligible"]:
            continue
        folder = dest / "runs" / slot["client"] / slot["id"]
        request = base.read_json(folder / "request.json")
        if request["query"] != queries[slot["query_id"]]["query"]:
            raise ValueError("query changed")
        events = [json.loads(line) for line in (folder / "stdout.jsonl").read_text().splitlines() if line.strip()]
        classify = classify_pi if slot["client"] == "pi" else classify_claude
        actual = classify(events, (dest / "frozen-skill/SKILL.md").read_text(), request["canonical_skill"])
        if actual != base.read_json(folder / "complete.json") or base.read_json(folder / "process.json")["returncode"] != 0:
            raise ValueError("raw activation receipt mismatch")
        grouped[(slot["client"], slot["query_id"])].append(actual)
    rows = []
    for (client, qid), runs in grouped.items():
        q = queries[qid]
        valid = [r for r in runs if r["valid"]]
        complete = len(valid) == 3
        count = sum(r["activated"] for r in valid)
        majority = count >= 2 if complete else None
        rows.append({"client": client, **q, "valid_runs": len(valid), "invalid_runs": len(runs) - len(valid),
                     "activations": count, "activation_rate": count / len(valid) if valid else None,
                     "majority_activation": majority, "correct": majority == q["should_trigger"] if complete else None})
    summaries = []
    for client in MODELS:
        for split in ("all", "tune", "holdout", "near-negative"):
            chosen = [r for r in rows if r["client"] == client and (split == "all" or r["split"] == split or split == "near-negative" and r["id"].startswith("near-neg-"))]
            valid = [r for r in chosen if r["correct"] is not None]
            positive = [r for r in valid if r["should_trigger"]]
            negative = [r for r in valid if not r["should_trigger"]]
            summaries.append({"client": client, "selection": split, "queries": len(chosen), "complete_queries": len(valid),
                              "sensitivity": sum(r["correct"] for r in positive) / len(positive) if positive else None,
                              "specificity": sum(r["correct"] for r in negative) / len(negative) if negative else None})
    base.dump(dest / "rates.json", rows)
    base.dump(dest / "summary.json", {"summaries": summaries, "pilot_eligibility": {c: p["eligible"] for c, p in pilots.items()},
              "unavailable": manifest["unavailable"], "interpretation": "Initial-turn activation in controlled read-only contexts, not writing efficacy, default-client behavior or complete workflows. Repeats are not independent queries."})
    print(json.dumps(base.read_json(dest / "summary.json"), indent=2))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("stage", choices=("prepare", "pilot", "run", "analyze"))
    parser.add_argument("--dest", type=Path, required=True)
    parser.add_argument("--workers", type=int, default=2)
    args = parser.parse_args()
    if args.stage == "run":
        run(args.dest, args.workers)
    else:
        {"prepare": prepare, "pilot": pilot, "analyze": analyze}[args.stage](args.dest)


if __name__ == "__main__":
    main()
