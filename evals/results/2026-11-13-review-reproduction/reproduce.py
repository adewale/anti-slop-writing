"""Reproduce the review against the fixed pre-repair commit; no model calls."""

import collections
import importlib.util
import json
import random
import re
import subprocess
import tempfile
from pathlib import Path

ROOT = Path.cwd()
REF = "70f9803b4c717a98c713706101638f2406105a40"


def read(path):
    return subprocess.check_output(["git", "show", f"{REF}:{path}"], text=True)


def data(path):
    return json.loads(read(path))


def lines(path):
    return [json.loads(l) for l in read(path).splitlines() if l.strip()]


def grams(text, n):
    w = re.findall(r"\b\w+\b", text.casefold())
    return {tuple(w[i : i + n]) for i in range(len(w) - n + 1)}


with tempfile.TemporaryDirectory() as td:
    gate = Path(td) / "gate.py"
    gate.write_text(read("scripts/score_delta.py"))
    spec = importlib.util.spec_from_file_location("gate", gate)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    p = "evals/results/2026-05-31-stat-proof/"
    before = {r["id"]: r for r in lines(p + "judgments/before.jsonl")}
    after = {r["id"]: r for r in lines(p + "judgments/after.jsonl")}
    cases = data(p + "fresh-holdout.json")["evals"]
    ds = []
    fs = collections.defaultdict(list)
    removed = []
    for c in cases:
        keep = [i for i, a in enumerate(c["assertions"]) if "Rewrite check" not in a]
        if len(keep) < len(c["assertions"]):
            removed.append(c["id"])

        def score(r, keep=keep):
            return sum(bool(r["assertions"][i]["pass"]) for i in keep) / len(keep)

        d = score(after[c["id"]]) - score(before[c["id"]])
        ds.append(d)
        fs[c["id"].split("-")[1]].append(d)
    print(
        "STAT-PROOF corrected binary N, delta, CI, p:",
        len(ds),
        m.paired_bootstrap_ci(ds, 10000, 0.05, random.Random(0)),
        m.sign_flip_p_value(ds, 10000, random.Random(0)),
    )
    print("Template assertion removed from:", removed)
    clusters = [sum(v) / len(v) for v in fs.values()]
    print(
        "STAT-PROOF corrected family means and p:",
        dict(zip(fs, clusters)),
        m.sign_flip_p_value(clusters, 10000, random.Random(0)),
    )
    print(
        "Failed template assertions in old arm:",
        sum(not before[c]["assertions"][2]["pass"] for c in removed),
    )
    print(
        "All old-arm assertion failures:",
        sum(not a["pass"] for r in before.values() for a in r["assertions"]),
    )
    lens = [
        (
            len(read(p + "before/outputs/" + c["id"] + ".md").split()),
            len(read(p + "after/outputs/" + c["id"] + ".md").split()),
        )
        for c in cases
    ]
    print(
        "After longer by whitespace word count:",
        sum(b > a for a, b in lens),
        "/",
        len(lens),
    )
    base = lines("evals/results/baseline-2026-05-29/scores.jsonl")
    print("BASELINE cases, perfect:", len(base), sum(r["score"] == 1 for r in base))
    duplicate = Path(td) / "dup.jsonl"
    duplicate.write_text(
        "\n".join(
            json.dumps({"id": "same", "split": "holdout", "before": 0, "after": 1})
            for _ in range(8)
        )
    )
    print(
        "DUPLICATES:",
        subprocess.run(
            ["python3", str(gate), str(duplicate)], text=True, capture_output=True
        ).stdout.strip(),
    )
    five = Path(td) / "five.jsonl"
    five.write_text(
        "\n".join(
            json.dumps({"id": str(i), "split": "holdout", "before": 0, "after": 1})
            for i in range(5)
        )
    )
    print(
        "FIVE perfect gains:",
        subprocess.run(
            ["python3", str(gate), str(five)], text=True, capture_output=True
        ).stdout.strip(),
    )
    regression = Path(td) / "regression.jsonl"
    regression.write_text(
        "\n".join(
            json.dumps({"id": str(i), "split": "holdout", "before": 1, "after": 0})
            for i in range(10)
        )
    )
    print(
        "REGRESSION:",
        subprocess.run(
            ["python3", str(gate), str(regression)], text=True, capture_output=True
        ).stdout.strip(),
    )
    doctrine = "\n".join(
        read(f)
        for f in subprocess.check_output(
            ["git", "ls-tree", "-r", "--name-only", REF, "skills/"], text=True
        ).splitlines()
    )
    for n in [6, 8]:
        dg = grams(doctrine, n)
        hits = []
        for suite in ["evals", "rewrite-evals", "adversarial", "meta-evals"]:
            for c in data("evals/" + suite + ".json")["evals"]:
                overlap = grams(c["prompt"], n) & dg
                if overlap:
                    hits.append((suite, c["id"], " ".join(min(overlap))))
        print(f"PROMPT LEAKAGE {n}-grams ({len(hits)} cases):", json.dumps(hits))
    print(
        "REWRITE SPLITS:",
        collections.Counter(
            c["split"] for c in data("evals/rewrite-evals.json")["evals"]
        ),
    )
    runner = read("scripts/run_evals.py")
    print(
        "DYNAMIC RUBRIC in JUDGE_TEMPLATE:",
        "dynamic_rubric"
        in runner[
            runner.index("JUDGE_TEMPLATE =") : runner.index(
                "def format_graded_dimensions"
            )
        ],
    )
    print(
        "PREPARE combines apply and judge:",
        all(
            s in runner
            for s in ['"apply_prompt":', '"judge_prompt":', '"assertions": assertions']
        ),
    )
    for c in data("evals/shared-benchmark.json")["cases"]:
        for a in c.get("assertions", []):
            if a.get("name") in ["has-relation-hinge", "earned-appositive"]:
                text = (
                    "also" if a["name"] == "has-relation-hinge" else "Do not keep it."
                )
                print(
                    "FOOLING CHECK:",
                    a["name"],
                    repr(text),
                    any(v.casefold() in text.casefold() for v in a["values"]),
                )
    oracle = Path(td) / "oracle.py"
    oracle.write_text(read("evals/oracles/fixture_oracle.py"))
    for text in [
        "HMAC retry receipt",
        "Our groundbreaking, seamless tool checks HMAC signatures and logs a retry receipt for 99.99% reliability.",
    ]:
        (Path(td) / "output.md").write_text(text)
        r = subprocess.run(
            ["python3", str(oracle), td, "round3-fixture-mechanism-copy"],
            text=True,
            capture_output=True,
        )
        print("FOOLING ORACLE:", repr(text), r.returncode, r.stdout.strip())
    for a, b in [("de3cf59", "725d546")]:
        print(
            "COMMIT TIMES:",
            subprocess.check_output(
                ["git", "show", "-s", "--format=%h %cI", a, b], text=True
            ).strip(),
        )

for commit in ["48f29fc", "de3cf59"]:
    path = "skills/anti-slop-writing/SKILL.md"
    before = subprocess.check_output(["git", "show", commit + "^:" + path], text=True)
    after = subprocess.check_output(["git", "show", commit + ":" + path], text=True)
    print("HISTORICAL WORD GROWTH:", commit, len(after.split()) - len(before.split()))
print(
    "LAST MAIN SKILL COMMIT:",
    subprocess.check_output(
        ["git", "log", REF, "-1", "--format=%h %cI %s", "--", "skills/"], text=True
    ).strip(),
)
pairs = []
for name in subprocess.check_output(
    [
        "git",
        "ls-tree",
        "-r",
        "--name-only",
        REF,
        "evals/results/2026-06-14-stop-slop-ablation/",
    ],
    text=True,
).splitlines():
    if name.endswith("__cond_A.md"):
        other = name.replace("__cond_A.md", "__cond_B.md")
        pairs.append(read(name) == read(other))
print("STOP-SLOP IDENTICAL PAIRS:", sum(pairs), "/", len(pairs))
