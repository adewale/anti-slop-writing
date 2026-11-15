#!/usr/bin/env python3
"""Offline, unvalidated role-preserving views of one exact source response.

Consumes proposed annotations; does not extract, judge, call models, or change the
registered rewrite-only runner. Structural validity is not semantic faithfulness.
See docs/structured-deliverable-views.md.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from itertools import pairwise
from pathlib import Path

ROLES = ("prose", "author_question", "decision", "conditional_alternative")


def exact_keys(value, keys: set[str], name: str) -> None:
    if not isinstance(value, dict) or set(value) != keys:
        raise ValueError(f"{name} must contain exactly: {', '.join(sorted(keys))}")


def checked_span(source: str, value) -> dict:
    exact_keys(value, {"start", "end", "text"}, "span")
    start, end, text = value["start"], value["end"], value["text"]
    if type(start) is not int or type(end) is not int or not 0 <= start < end <= len(source):
        raise ValueError("span offsets must be nonempty, in-range Unicode character indices")
    if not isinstance(text, str) or not text.strip() or source[start:end] != text:
        raise ValueError("span must be an exact, nonblank source slice; no whitespace normalization")
    return {"start": start, "end": end, "text": text}


def overlaps(left: tuple[int, int], right: tuple[int, int]) -> bool:
    return left[0] < right[1] and right[0] < left[1]


def build_views(source: str, annotation: dict) -> dict:
    """Validate references and render roles without inventing or approving their assignment."""
    if not isinstance(source, str):
        raise TypeError("source must be a string")
    exact_keys(annotation, {"version", "source_sha256", "items", "unresolved"}, "annotation")
    if type(annotation["version"]) is not int or annotation["version"] != 1:
        raise ValueError("unsupported annotation version")
    checksum = hashlib.sha256(source.encode()).hexdigest()
    if annotation["source_sha256"] != checksum:
        raise ValueError("source hash differs from annotation")
    if not isinstance(annotation["unresolved"], list):
        raise TypeError("unresolved must be a list")
    if annotation["unresolved"]:
        raise ValueError("unresolved material needs review before constructing views")
    if not isinstance(annotation["items"], list):
        raise TypeError("items must be a list; [] explicitly represents no deliverable")

    emitted, bodies, qualifications, identities = [], [], [], set()
    for entry in annotation["items"]:
        exact_keys(entry, {"id", "role", "content", "qualifications"}, "item")
        identity, role = entry["id"], entry["role"]
        if (not isinstance(identity, str) or re.fullmatch(r"[A-Za-z0-9_-]{1,32}", identity) is None
                or identity in identities):
            raise ValueError("item ids must be unique short identifiers")
        identities.add(identity)
        if role not in ROLES:
            raise ValueError("unknown role; do not guess a mixed or ambiguous role")
        content = checked_span(source, entry["content"])
        body = (content["start"], content["end"])
        if bodies and body[0] < bodies[-1][1]:
            raise ValueError("content must be in source order without overlap")
        bodies.append(body)
        if not isinstance(entry["qualifications"], list):
            raise TypeError("qualifications must be a list")
        if role == "conditional_alternative" and not entry["qualifications"]:
            raise ValueError("conditional alternative requires an attached source qualification")
        notes, last_end = [], -1
        for raw in entry["qualifications"]:
            qualifier = checked_span(source, raw)
            span = (qualifier["start"], qualifier["end"])
            if span[0] < last_end:
                raise ValueError("qualifications must be in source order without overlap")
            last_end = span[1]
            if overlaps(body, span):
                raise ValueError("qualification must not overlap its content")
            qualifications.append(span)
            notes.append({"position": "before" if span[1] <= body[0] else "after", "text": qualifier["text"]})
        emitted.append({"id": identity, "role": role, "text": content["text"], "qualifications": notes})

    # The exact same qualification may explicitly apply to several items. Other
    # overlapping annotations obscure roles and are rejected, not silently merged.
    unique_notes = sorted(set(qualifications))
    if any(overlaps(a, b) for a, b in pairwise(unique_notes)):
        raise ValueError("qualification spans overlap")
    if any(overlaps(body, note) for body in bodies for note in unique_notes):
        raise ValueError("qualification must not overlap another item's content")

    # Every unselected character remains visible for audit; omissions are not
    # classified as harmless and cannot receive an automatic audit pass.
    omitted, cursor = [], 0
    for start, end in sorted(set(bodies + qualifications)):
        if cursor < start:
            omitted.append({"start": cursor, "end": start, "text": source[cursor:start]})
        cursor = end
    if cursor < len(source):
        omitted.append({"start": cursor, "end": len(source), "text": source[cursor:]})
    return {"schema_version": 1, "status": "unvalidated_prototype", "source_sha256": checksum,
            "views": {"full": {"response": source}, "deliverable": {"items": emitted}},
            "omitted_spans": omitted}


def unique_object(pairs: list) -> dict:
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="JSON with source and annotation; fixture metadata is not emitted")
    parser.add_argument("--out", type=Path, help="new output file; default stdout")
    args = parser.parse_args()
    try:
        payload = json.loads(args.input.read_text(encoding="utf-8"), object_pairs_hook=unique_object)
        if not isinstance(payload, dict) or not {"source", "annotation"} <= payload.keys():
            raise ValueError("input needs source and annotation")
        result = build_views(payload["source"], payload["annotation"])
        text = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
        if args.out is None:
            sys.stdout.write(text)
        else:
            # Exclusive creation preserves both source inputs and prior artifacts.
            with args.out.open("x", encoding="utf-8") as out:
                out.write(text)
    except (OSError, TypeError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
