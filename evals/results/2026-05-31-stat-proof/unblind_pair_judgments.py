#!/usr/bin/env python3
"""Unblind A/B pair judgments for the 2026-05-31 statistical-proof run.

Usage:
  python3 unblind_pair_judgments.py pair-judgments/default-*.jsonl

Reads blind/mapping.json and writes:
  judgments/before.jsonl
  judgments/after.jsonl
"""
from __future__ import annotations

import argparse
import glob
import json
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent


def die(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def iter_records(patterns: list[str]):
    paths: list[Path] = []
    for pattern in patterns:
        matches = [Path(p) for p in glob.glob(pattern)]
        paths.extend(matches or [Path(pattern)])
    if not paths:
        die("no judgment files")
    for path in paths:
        with path.open(encoding="utf-8") as fh:
            for line_no, raw in enumerate(fh, start=1):
                line = raw.strip()
                if not line:
                    continue
                try:
                    record = json.loads(line)
                except json.JSONDecodeError as exc:
                    die(f"{path}:{line_no}: invalid JSON: {exc}")
                yield path, line_no, record


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("judgments", nargs="+")
    parser.add_argument("--out-dir", default=str(BASE / "judgments"))
    args = parser.parse_args()

    mapping_path = BASE / "blind" / "mapping.json"
    mapping_data = json.loads(mapping_path.read_text(encoding="utf-8"))
    mapping = {row["id"]: {"A": row["A"], "B": row["B"]} for row in mapping_data["mapping"]}

    by_side = {"before": [], "after": []}
    seen: set[tuple[str, str]] = set()
    for path, line_no, record in iter_records(args.judgments):
        cid = record.get("id")
        candidate = record.get("candidate")
        if cid not in mapping:
            die(f"{path}:{line_no}: unknown id {cid!r}")
        if candidate not in ("A", "B"):
            die(f"{path}:{line_no}: candidate must be A or B")
        key = (cid, candidate)
        if key in seen:
            die(f"duplicate judgment for {cid} candidate {candidate}")
        seen.add(key)
        side = mapping[cid][candidate]
        out = dict(record)
        out.pop("candidate", None)
        out["blind_candidate"] = candidate
        by_side[side].append(out)

    expected = {(cid, c) for cid in mapping for c in ("A", "B")}
    missing = sorted(expected - seen)
    if missing:
        die(f"missing {len(missing)} candidate judgments: {missing[:5]}")

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    for side in ("before", "after"):
        rows = sorted(by_side[side], key=lambda r: r["id"])
        path = out_dir / f"{side}.jsonl"
        path.write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in rows) + "\n", encoding="utf-8")
        print(f"wrote {len(rows)} {side} judgments to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
