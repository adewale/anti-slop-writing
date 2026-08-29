# Shared benchmark evals

This repo participates in the shared Skill Eval Harness:

- Repo: https://github.com/adewale/skill-eval-harness
- Version: `>=0.3.0`
- Manifest: `evals/shared-benchmark.json`

Install the harness from GitHub with [uv](https://docs.astral.sh/uv/):

```sh
uv tool install git+https://github.com/adewale/skill-eval-harness.git@v0.3.0
```

Splits:
- `tune` — visible iteration cases.
- `holdout` — hidden end-of-round / merge scoring cases.
- `holdback` — examples withheld from `SKILL.md`, references, docs, and public eval descriptions until after scoring.

Validate from this repo root:

```sh
skill-benchmark validate evals/shared-benchmark.json
```

Prepare paired run tasks:

```sh
skill-benchmark prepare evals/shared-benchmark.json --split tune --out /tmp/anti-slop-writing-tasks.jsonl
```

Include ablation variants when running a focused regression check:

```sh
skill-benchmark prepare evals/shared-benchmark.json --split tune --include-ablations --out /tmp/anti-slop-writing-ablation-tasks.jsonl
```

Run autonomous Pi trigger checks for trigger/no-trigger cases:

```sh
skill-pi-trigger-eval evals/shared-benchmark.json --split tune --out /tmp/anti-slop-writing-trigger-report.json
```

`old_skill` is optional and intentionally not emitted unless `old_skill_paths` is populated and `--include-old-skill` is passed. Hidden `holdout` / `holdback` prompt refs must be supplied privately before scoring; use `--allow-missing-prompts` only for dry-run planning.

Grade saved outputs:

```sh
skill-benchmark benchmark evals/shared-benchmark.json --runs eval-runs/latest --allow-scripts --out /tmp/anti-slop-writing-benchmark.json
```

Run optional qualitative judges through the shared `judge` backend:

```sh
skill-benchmark judge evals/shared-benchmark.json --runs eval-runs/latest --judge-cmd 'claude -p' --transcripts eval-runs/judge-transcripts --out /tmp/anti-slop-writing-judge-results.jsonl
skill-benchmark benchmark evals/shared-benchmark.json --runs eval-runs/latest --allow-scripts --judge-results /tmp/anti-slop-writing-judge-results.jsonl --out /tmp/anti-slop-writing-benchmark.json
```

Script assertions are deterministic repo-owned oracles and require `--allow-scripts` during grading. Two live in `oracles/`:

- `oracles/fixture_oracle.py` — fixture-backed content checks (case `round3-fixture-mechanism-copy`).
- `oracles/slop_lint_oracle.py` — slop-lint detector checks bridging `oracles/slop_lint.py` into the script-assertion contract (case `pos-new-register-launch-strip`); marked `"oracle": "strong"` because the detector registry is self-tested (`python3 oracles/slop_lint.py --self-test`). Add a `CHECKS` table entry alongside any new case that names it. See `../docs/deterministic-graders.md`.

Manifest maintenance note (2026-08-29): the current harness main validates this manifest (`20 cases, 4 ablations`). Getting there required stamping the five trigger cases' `should_trigger` booleans (taken verbatim from their `expected_behavior` text) and marking the two judge-only hidden cases' reviews as `"severity": "gate"` — newer harness versions require every answer variant to carry at least one gate-tier assertion. The version pins above trail the harness's main branch; revalidate after harness upgrades.
