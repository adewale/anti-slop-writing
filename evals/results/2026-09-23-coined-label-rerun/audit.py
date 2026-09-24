#!/usr/bin/env python3
"""Apply the pre-registered exclusion rule to the re-run's apply-agent transcripts.

A trial is valid only if its transcript shows the manifest prompt verbatim, the
pre-registered model, reads confined to its own doctrine directory, a single
write to its own output path, no listing or search that exposed another trial's
output, and a non-empty, well-formed output file. Each slot takes its first
valid attempt; later attempts in a slot exist only as replacements. A transcript
with no hand-back is still running and is not judged unless --final is given.

Run from the repository root:
  python3 evals/results/2026-09-23-coined-label-rerun/audit.py \
      --manifest M --attempts A --transcripts DIR --out REPORT.json
"""
import argparse
import json
import re
from collections import Counter
from pathlib import Path

MODEL = "claude-sonnet-5"
OPAQUE = re.compile(r"\bt[a-z2-9]{6}(?:-r\d+)?\b")
READ_ONLY_BASH = re.compile(r"^\s*(ls|mkdir -p|test -d|stat)\b")


def slot_key(t):
    return f"{t['kind']}:{t.get('case_id', 'guards')}:{t['arm']}:{t['slot']}"


def text_of(content):
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        return "".join(p.get("text", "") if isinstance(p, dict) else str(p) for p in content)
    return ""


def load_transcript(path):
    prompt, models, calls, results = None, set(), [], {}
    for line in path.read_text(errors="replace").splitlines():
        try:
            o = json.loads(line)
        except json.JSONDecodeError:
            continue
        m = o.get("message") or {}
        if m.get("model"):
            models.add(m["model"])
        c = m.get("content")
        if o.get("type") == "user" and prompt is None and "You are applying a writing-review skill" in text_of(c):
            prompt = text_of(c)
        if isinstance(c, list):
            for p in c:
                if not isinstance(p, dict):
                    continue
                if p.get("type") == "tool_use":
                    calls.append(p)
                elif p.get("type") == "tool_result":
                    results[p.get("tool_use_id")] = text_of(p.get("content"))
    return prompt, models, calls, results


def violations(att, prompt, models, calls, results):
    v = []
    if (prompt or "").strip() != att["prompt"].strip():
        v.append("prompt differs from manifest")
    if models - {MODEL}:
        v.append(f"model {sorted(models - {MODEL})}")
    d, out = att["doctrine_dir"].rstrip("/") + "/", att["output_path"]
    out_dir = str(Path(out).parent)
    own = Path(out).stem
    writes = 0
    for call in calls:
        name, inp = call.get("name"), call.get("input", {})
        if name == "SubagentHandback":
            continue
        if name == "Read":
            fp = inp.get("file_path", "")
            if not (fp == d + "SKILL.md" or fp.startswith(d + "references/")):
                v.append(f"read outside doctrine: {fp}")
        elif name == "Write":
            writes += 1
            if inp.get("file_path") != out:
                v.append(f"wrote elsewhere: {inp.get('file_path')}")
        elif name == "Bash":
            cmd = inp.get("command", "")
            paths = set(re.findall(r"/[^\s'\";|&>]+", cmd))
            allowed = [x for x in paths if x.rstrip("/") in (out_dir, out) or (x.rstrip("/") + "/").startswith(d)]
            if not READ_ONLY_BASH.match(cmd) or len(allowed) != len(paths):
                v.append(f"bash: {cmd[:80]}")
            seen = set(OPAQUE.findall(results.get(call.get("id"), ""))) - {own}
            if seen:
                v.append(f"listing exposed other outputs: {sorted(seen)[:3]}")
        else:
            v.append(f"tool {name}")
    if writes != 1:
        v.append(f"{writes} writes")
    p = Path(out)
    if not p.is_file() or not p.read_text().strip():
        v.append("output missing or empty")
    elif att["kind"] == "guard":
        body = p.read_text()
        if any(f"## R{i}" not in body for i in range(1, 5)):
            v.append("guard output missing an R heading")
    return v


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", type=Path, required=True)
    ap.add_argument("--attempts", type=Path, required=True)
    ap.add_argument("--transcripts", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--final", action="store_true", help="treat unfinished transcripts as finished")
    args = ap.parse_args()
    trials = {slot_key(t): t for t in json.loads(args.manifest.read_text())["trials"]}
    attempts = json.loads(args.attempts.read_text())
    by_output = {}
    for key, paths in attempts.items():
        t = trials[key]
        doctrine_dir = re.search(r"Read the skill file (\S+)/SKILL\.md", t["prompt"]).group(1)
        for path in paths:
            by_output[path] = {"slot": key, "kind": t["kind"], "arm": t["arm"], "output_path": path,
                               "doctrine_dir": doctrine_dir, "prompt": t["prompt"].replace(t["output_path"], path)}
    found = {}
    for tr in sorted(args.transcripts.glob("agent-*.jsonl")):
        prompt, models, calls, results = load_transcript(tr)
        if not prompt:
            continue
        hits = [o for o in by_output if o in prompt]
        if len(hits) == 1:
            found[hits[0]] = (tr.name, prompt, models, calls, results)
    report = {"model": MODEL, "attempts": {}, "slots": {}}
    for path, att in by_output.items():
        if path not in found:
            report["attempts"][path] = {"slot": att["slot"], "status": "pending"}
            continue
        tr, prompt, models, calls, results = found[path]
        if not any(c.get("name") == "SubagentHandback" for c in calls) and not args.final:
            report["attempts"][path] = {"slot": att["slot"], "transcript": tr, "status": "running"}
            continue
        v = violations(att, prompt, models, calls, results)
        report["attempts"][path] = {"slot": att["slot"], "transcript": tr, "models": sorted(models),
                                    "tool_calls": [c.get("name") for c in calls],
                                    "status": "valid" if not v else "excluded", "violations": v}
    for key, paths in attempts.items():
        states = [report["attempts"][p]["status"] for p in paths]
        valid = [p for p, s in zip(paths, states) if s == "valid"]
        waiting = "pending" in states or "running" in states
        report["slots"][key] = {"arm": trials[key]["arm"], "kind": trials[key]["kind"],
                                "status": "valid" if valid else ("pending" if waiting else "needs-replacement"),
                                "trial": valid[0] if valid else None, "attempts": len(paths)}
    args.out.write_text(json.dumps(report, indent=2))
    c = Counter((s["kind"], s["arm"], s["status"]) for s in report["slots"].values())
    ex = Counter((report["slots"][a["slot"]]["arm"]) for a in report["attempts"].values() if a["status"] == "excluded")
    print("slots:", dict(sorted(c.items())))
    print("excluded attempts by arm:", dict(ex))
    for p, a in report["attempts"].items():
        if a["status"] == "excluded":
            print("EXCLUDED", Path(p).name, a["violations"][:2])


if __name__ == "__main__":
    main()
