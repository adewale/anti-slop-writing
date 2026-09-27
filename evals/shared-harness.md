# Shared benchmark evals

This repo participates in the shared Skill Eval Harness:

- Repo: https://github.com/adewale/skill-eval-harness
- Version: `==0.6.0` (PyPI; the manifest's `harness.version` says the same)
- Manifest: `evals/shared-benchmark.json`

Install the pinned harness with [uv](https://docs.astral.sh/uv/):

```sh
uv tool install skill-eval-harness==0.6.0
```

CI runs the model-free gate against that pin, and grades the checked-in example
outputs in `evals/assertion-examples.json` with the harness's own assertion evaluator:

```sh
uvx --from skill-eval-harness==0.6.0 skill-benchmark validate --strict-leakage --check-ablations evals/shared-benchmark.json
uvx --from skill-eval-harness==0.6.0 skill-benchmark audit-manifest --fail-on-blockers evals/shared-benchmark.json
uvx --from skill-eval-harness==0.6.0 python scripts/check_assertion_examples.py
```

## Over-application probe: earned antithesis

The harness's pinned ablation study
([`docs/ablation-study-walkthrough.md`](https://github.com/adewale/skill-eval-harness/blob/main/docs/ablation-study-walkthrough.md))
found this skill directionally over-applies: on `neg-human-antithesis`, without the skill
the model kept an earned antithesis 5/5, and with it the model flagged it as slop and
rewrote it about 4/5 times (with 0.2 vs without 1.0, n=5). Five pairs sit below the
two-sided sign-flip floor, so the finding is unconfirmed. That case's objective check,
`contains_any ["earned", "antithesis", "do not"]`, also passes the harmful answer
(`evals/examples/earned-antithesis/revise-earned.md` contains "antithesis").

The replication family is deterministic:

- `neg-earned-antithesis-{archive,bridge,growth,syllabus,translation,fence}`: six different
  earned contrasts. The context evidences both sides, which is the `SKILL.md` definition of
  an earned antithesis. The answer must open with `VERDICT: KEEP` and must not also vote
  `REVISE`.
- `pos-decorative-antithesis-{readme,changelog}`: controls where neither side is evidenced;
  `VERDICT: REVISE` is right. They stop a "keep everything" fix from passing the probe.
- `evals/assertion-examples.json` lists pass and fail example outputs for every case in
  the family, and CI grades them with the pinned harness.

To decide whether the doctrine over-applies, run the family with at least three runs per
arm. That gives 18 earned-case pairs, above the six informative pairs the sign-flip gate
needs:

```sh
skill-benchmark prepare evals/shared-benchmark.json --split tune --runs-per-variant 3 --out /tmp/anti-slop-tasks.jsonl
python3 -c "import json,sys; [print(l, end='') for l in open('/tmp/anti-slop-tasks.jsonl') if json.loads(l)['case_id'].startswith(('neg-earned-antithesis-', 'pos-decorative-antithesis-'))]" > /tmp/antithesis-tasks.jsonl
# run /tmp/antithesis-tasks.jsonl with your runner (run-claude, run-codex, run-agent), then:
skill-benchmark benchmark evals/shared-benchmark.json --runs eval-runs/antithesis --out /tmp/antithesis-benchmark.json
```

The doctrine over-applies if the with-skill keep rate on the six earned cases is below
the without-skill rate, the paired sign-flip gate agrees, and the decorative controls
are still revised with the skill. If so, follow `runbooks/hillclimb-skill.md`: record the
failure, make the smallest doctrine change, and re-run the family and the holdout gate.
If the paired gate does not agree, record the null result in `evals/results/`.

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

Script assertions are deterministic repo-owned oracles and require `--allow-scripts` during grading.
