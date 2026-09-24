#!/usr/bin/env python3
"""Build the re-run's judge prompts and audit the judge agents against them.

  prompt: python3 audit_judges.py prompt --batch-file F --out-file O
  audit:  python3 audit_judges.py audit --batches DIR --key KEY --judgments DIR \
              --transcripts DIR --out REPORT.json [--final]

A judgment file is accepted only if its judge's transcript shows the prompt
verbatim, the pre-registered model, reads of its own batch file and nothing
else, one Write to its own output path, and no other tool; and the file holds
one JSON line per batch item, in batch order, with every assertion judged by
index and every graded dimension scored 1-5. A rejected file is replaced by a
fresh judge on the same batch. A transcript with no hand-back is still running
and is not judged unless --final is given.
Run from the repository root.
"""
import argparse
import json
import re
from pathlib import Path

MODELS = {"sonnet": "claude-sonnet-5", "haiku": "claude-haiku-4-5-20251001"}
PROMPT = """You are an evaluation judge. Read exactly one file: {batch}. Each item in it has the request a critique responds to, a numbered list of assertions, graded dimensions, and the critique under review.

For each item, judge the critique against each assertion independently. An assertion passes only when the critique clearly satisfies it. Keyword presence alone is not a pass: a critique that mentions a term without making the judgment the assertion describes fails. A critique that criticizes the passage for a different reason than the one an assertion describes does not satisfy that assertion. Score each graded dimension 1-5 against its rubric. Judge each item on its own merits.

Keep every evidence field to a short quote of at most 15 words. Write one JSON object per line, one line per item, in the order the items appear, with a single Write call to {out} using this shape:
{{"id": "<item id>", "assertions": [{{"index": 1, "pass": true, "evidence": "<short quote>"}}], "graded_dimensions": [{{"name": "<name>", "score": 4, "evidence": "<short quote>"}}]}}
Include every assertion by index. Use an empty list for graded_dimensions when the item lists none. Escape double quotes inside evidence so every line is valid JSON. Put nothing else in the file.

Do not read, list, or search any other file or directory. Reply with only: DONE <number of lines written>"""
OUT_NAME = re.compile(r"^(sonnet|haiku)-(\d{3})(?:-r\d+)?\.jsonl$")


def text_of(content):
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        return "".join(p.get("text", "") if isinstance(p, dict) else str(p) for p in content)
    return ""


def load_transcript(path):
    prompt, models, calls = None, set(), []
    for line in path.read_text(errors="replace").splitlines():
        try:
            o = json.loads(line)
        except json.JSONDecodeError:
            continue
        m = o.get("message") or {}
        if m.get("model"):
            models.add(m["model"])
        c = m.get("content")
        if o.get("type") == "user" and prompt is None and "You are an evaluation judge." in text_of(c):
            prompt = text_of(c)
        if isinstance(c, list):
            calls += [p for p in c if isinstance(p, dict) and p.get("type") == "tool_use"]
    return prompt, models, calls


def load_cases():
    cases = {}
    for suite in ("evals.json", "adversarial.json"):
        for c in json.loads(Path("evals", suite).read_text())["evals"]:
            cases[c["id"]] = c
    return cases


def check_file(path, item_ids, key, cases):
    v = []
    if not path.is_file():
        return ["output missing"]
    lines = [x for x in path.read_text().splitlines() if x.strip()]
    recs = []
    for n, line in enumerate(lines, 1):
        try:
            recs.append(json.loads(line))
        except json.JSONDecodeError as e:
            v.append(f"line {n} is not JSON: {e.msg}")
    if v:
        return v
    if [r.get("id") for r in recs] != item_ids:
        return ["ids differ from the batch's items or their order"]
    for r in recs:
        case = cases[key[r["id"]]["case_id"]]
        a = r.get("assertions")
        if not isinstance(a, list) or [x.get("index") if isinstance(x, dict) else None for x in a] != list(
                range(1, len(case["assertions"]) + 1)):
            v.append(f"{r['id']}: assertions not indexed 1..{len(case['assertions'])}")
        elif not all(isinstance(x.get("pass"), bool) for x in a):
            v.append(f"{r['id']}: a pass value is not a boolean")
        dims = r.get("graded_dimensions", [])
        want = [d["name"] for d in case.get("graded_dimensions", [])]
        if not isinstance(dims, list) or [d.get("name") if isinstance(d, dict) else None for d in dims] != want:
            v.append(f"{r['id']}: graded dimensions differ from the case's")
        elif not all(isinstance(d.get("score"), (int, float)) and 1 <= d["score"] <= 5 for d in dims):
            v.append(f"{r['id']}: a graded score is outside 1-5")
    return v


def cmd_audit(args):
    key = {k["blind_id"]: k for k in json.loads(args.key.read_text())}
    cases = load_cases()
    batches = {f.stem.split("-")[1]: f for f in sorted(args.batches.glob("batch-*.md"))}
    items = {n: re.findall(r"^=== ITEM (\S+) ===$", f.read_text(), flags=re.MULTILINE) for n, f in batches.items()}
    assert sorted(i for ids in items.values() for i in ids) == sorted(key), "batches do not cover the key"
    transcripts = []
    for tr in sorted(args.transcripts.glob("agent-*.jsonl")):
        prompt, models, calls = load_transcript(tr)
        if prompt:
            transcripts.append((tr.name, prompt, models, calls))
    report = {"models": MODELS, "files": {}, "batches": {}}
    for f in sorted(args.judgments.glob("*.jsonl")):
        m = OUT_NAME.match(f.name)
        if not m:
            continue
        judge, n = m.groups()
        hits = [t for t in transcripts if str(f) in t[1]]
        entry = {"judge": judge, "batch": n}
        if len(hits) != 1:
            entry.update(status="excluded", violations=[f"{len(hits)} transcripts name this output"])
        else:
            name, prompt, models, calls = hits[0]
            entry["transcript"] = name
            if not any(c.get("name") == "SubagentHandback" for c in calls) and not args.final:
                entry["status"] = "running"
                report["files"][f.name] = entry
                continue
            v = []
            if prompt.strip() != PROMPT.format(batch=batches[n], out=f).strip():
                v.append("prompt differs from the template")
            if models - {MODELS[judge]}:
                v.append(f"model {sorted(models - {MODELS[judge]})}")
            writes = 0
            for c in calls:
                name_, inp = c.get("name"), c.get("input", {})
                if name_ == "SubagentHandback":
                    continue
                if name_ == "Read" and inp.get("file_path") == str(batches[n]):
                    continue
                if name_ == "Write" and inp.get("file_path") == str(f):
                    writes += 1
                    continue
                v.append(f"tool {name_}: {json.dumps(inp)[:80]}")
            if writes != 1:
                v.append(f"{writes} writes")
            v += check_file(f, items[n], key, cases)
            entry.update(status="valid" if not v else "excluded", violations=v, models=sorted(models))
        report["files"][f.name] = entry
    for judge in MODELS:
        for n in batches:
            files = [e for fn, e in report["files"].items() if e["judge"] == judge and e["batch"] == n]
            valid = sorted(fn for fn, e in report["files"].items()
                           if e["judge"] == judge and e["batch"] == n and e["status"] == "valid")
            status = "valid" if valid else ("running" if any(e["status"] == "running" for e in files)
                                            else "needs-judge" if not files else "needs-replacement")
            report["batches"][f"{judge}-{n}"] = {"status": status, "file": valid[0] if valid else None,
                                                 "attempts": len(files)}
    args.out.write_text(json.dumps(report, indent=2))
    counts = {}
    for b in report["batches"].values():
        counts[b["status"]] = counts.get(b["status"], 0) + 1
    print("batches:", counts)
    for fn, e in report["files"].items():
        if e["status"] == "excluded":
            print("EXCLUDED", fn, e["violations"][:3])


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("prompt")
    p.add_argument("--batch-file", type=Path, required=True)
    p.add_argument("--out-file", type=Path, required=True)
    a = sub.add_parser("audit")
    a.add_argument("--batches", type=Path, required=True)
    a.add_argument("--key", type=Path, required=True)
    a.add_argument("--judgments", type=Path, required=True)
    a.add_argument("--transcripts", type=Path, required=True)
    a.add_argument("--out", type=Path, required=True)
    a.add_argument("--final", action="store_true", help="treat unfinished transcripts as finished")
    args = ap.parse_args()
    if args.cmd == "prompt":
        print(PROMPT.format(batch=args.batch_file, out=args.out_file))
    else:
        cmd_audit(args)


if __name__ == "__main__":
    main()
