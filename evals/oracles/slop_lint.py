#!/usr/bin/env python3
"""Recall-oriented prose spans; never an authorship or prose-quality verdict.

Independent small implementation, not the historical branch's 830-line registry.
See docs/slop-lint.md for provenance, scope and earned-use limitations.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

PHRASES = {
    "significance-compression": r"\b(?:that['’]s the whole (?:point|story|game)|that['’]s not nothing|the punchline is)\b",
    "therapy-voice": r"\b(?:sit with that|worth naming|you already know)\b",
    "performative-honesty": r"\b(?:let['’]s be honest|I won['’]t pretend|honestly(?=,))\b",
    "stage-management": r"\b(?:here['’]s the thing|turns out|here['’]s the kicker)\b",
    "no-chain": r"\bno\s+[^,;.!?\n]+(?:,\s*no\s+[^,;.!?\n]+){2,}",
    "stranded-auxiliary": r"\b(?:didn['’]t|doesn['’]t|isn['’]t|wasn['’]t|won['’]t|can['’]t)\s*[.!?]",
}
FIELD = re.compile(
    r"(?im)^[ \t]*(?:\#{1,6}[ \t]+)?(?:\*\*)?"
    r"(Verdict|Slop tells|Specificity missing|Inflated claim|Flow break|Concrete rewrite|Rewrite check|Remembered line)"
    r"(?:\*\*)?[ \t]*:[ \t]*(?:\*\*)?[ \t]*"
)


def rewrite_span(text: str) -> tuple[str, int]:
    """One explicit rewrite field, or an error; never silently lint an empty scope."""
    fields = list(FIELD.finditer(text))
    selected = [i for i, match in enumerate(fields) if match[1].lower() == "concrete rewrite"]
    if len(selected) != 1:
        raise ValueError("rewrite-only mode requires exactly one Concrete rewrite: field")
    i = selected[0]
    start = fields[i].end()
    end = fields[i + 1].start() if i + 1 < len(fields) else len(text)
    chunk = text[start:end]
    start += len(chunk) - len(chunk.lstrip())
    chunk = chunk.strip()
    if chunk.startswith("```"):
        lines = chunk.splitlines(keepends=True)
        if len(lines) < 3 or lines[-1].strip() != "```" or any(line.lstrip().startswith("```") for line in lines[1:-1]):
            raise ValueError("rewrite-only mode found an ambiguous or unclosed code fence")
        start += len(lines[0])
        chunk = "".join(lines[1:-1])
        start += len(chunk) - len(chunk.lstrip())
        chunk = chunk.strip()
    if not chunk:
        raise ValueError("rewrite-only mode found an empty rewrite")
    return chunk, start


def sentence_spans(text: str) -> list[tuple[int, int]]:
    """Deliberately small segmentation heuristic; abbreviations remain a limitation."""
    spans = []
    start = 0
    ends = [m.end() for m in re.finditer(r"[.!?]+[\"’”']?(?=\s|$)", text)]
    if not ends or ends[-1] != len(text):
        ends.append(len(text))
    for end in ends:
        chunk = text[start:end]
        left = start + len(chunk) - len(chunk.lstrip())
        right = start + len(chunk.rstrip())
        if left < right:
            spans.append((left, right))
        start = end
    return spans


def findings(text: str, offset: int = 0) -> list[dict]:
    hits = []

    def add(detector: str, start: int, end: int) -> None:
        hits.append({"detector": detector, "start": start + offset, "end": end + offset,
                     "text": text[start:end], "interpretation": "review in context; earned uses may be correct"})

    for detector, pattern in PHRASES.items():
        for match in re.finditer(pattern, text, re.IGNORECASE):
            add(detector, match.start(), match.end())
    sentences = sentence_spans(text)
    for detector, minimum in (("sentence-anaphora", 3), ("stacked-questions", 2)):
        run, previous = [], None
        for start, end in [*sentences, (len(text), len(text))]:
            sentence = text[start:end]
            word = re.match(r"[\"'‘“*_]*([A-Za-z]+)\b", sentence)
            key = word[1].lower() if detector == "sentence-anaphora" and word else None
            if detector == "stacked-questions":
                key = "question" if sentence.rstrip('\"’”\'').endswith("?") else None
            gap = text[run[-1][1]:start] if run else ""
            if run and (key != previous or re.search(r"\n\s*\n", gap)):
                if len(run) >= minimum:
                    add(detector, run[0][0], run[-1][1])
                run = []
            if key:
                run.append((start, end))
            previous = key
    return sorted(hits, key=lambda h: (h["start"], h["end"], h["detector"]))


def report(text: str, rewrite_only: bool = False) -> dict:
    selected, offset = rewrite_span(text) if rewrite_only else (text, 0)
    hits = findings(selected, offset)
    return {"version": 1, "mode": "triage-only", "scope": "rewrite" if rewrite_only else "whole-input",
            "findings": hits, "counts": {name: sum(h["detector"] == name for h in hits) for name in sorted({h["detector"] for h in hits})},
            "limitations": "Matches are review leads, not errors, AI-authorship evidence or quality scores. Context, quotation, domain terminology and earned repetition require judgment."}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", help="UTF-8 file, or - for stdin")
    parser.add_argument("--rewrite-only", action="store_true")
    args = parser.parse_args()
    text = sys.stdin.read() if args.input == "-" else Path(args.input).read_text()
    try:
        result = report(text, args.rewrite_only)
    except ValueError as exc:
        parser.error(str(exc))
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0  # Findings do not automatically fail prose.


if __name__ == "__main__":
    raise SystemExit(main())
