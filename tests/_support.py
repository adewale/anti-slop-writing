"""Shared helpers: load repo scripts as modules and run them as CLIs."""
from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_script(rel: str):
    path = ROOT / rel
    spec = importlib.util.spec_from_file_location(path.stem, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def run_script(rel: str, *args: str, cwd: Path | None = None) -> subprocess.CompletedProcess:
    script = (cwd or ROOT) / rel
    return subprocess.run(
        [sys.executable, str(script), *map(str, args)],
        cwd=cwd or ROOT,
        capture_output=True,
        text=True,
        timeout=120,
    )


def write_jsonl(path: Path, records: list[dict]) -> Path:
    path.write_text("".join(json.dumps(r) + "\n" for r in records), encoding="utf-8")
    return path
