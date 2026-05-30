# Judge protocol (sub-agent implementation)

The repo is instruction-only. Nothing in it calls a model, so evals run through sub-agents driven by `scripts/run_evals.py`. This doc is the implementation those sub-agents follow.

The loop has three phases — apply, judge, grade — and is file-based so a parent agent's context stays small and the run is reproducible.

## Layout

One run writes under `evals/results/baseline-YYYY-MM-DD/` (or an iteration dir):

```
outputs/<suite>/<id>.md       one skill-applied output per case
judgments/<suite>.jsonl       one judgment line per case
scores.jsonl                  grade output, the recorded score
```

## Phase 1 — apply

Spawn one apply sub-agent per suite. Each one:

1. Reads `skills/anti-slop-writing/SKILL.md`.
2. Reads the suite file (e.g. `evals/evals.json`).
3. For each case in the requested split, applies the skill to `prompt` and writes the result to `outputs/<suite>/<id>.md`.
4. Returns only a short confirmation and the list of files written — never the full outputs, to keep the parent context small.

The apply agent must not see the assertions. It produces the output the skill prescribes; it does not optimize toward the grader.

## Phase 2 — judge

Spawn one judge sub-agent per suite, distinct from the apply agent that produced the outputs. Each one:

1. Reads the suite file and the matching `outputs/<suite>/<id>.md`.
2. Judges each assertion independently. An assertion passes only when the output clearly satisfies it, with a quoted snippet as evidence. Keyword presence alone is not a pass (see `evals/meta-evals.json` → `metric-artifact-check`).
3. Writes one JSON object per line to `judgments/<suite>.jsonl`:

```json
{"id": "generic-importance", "suite": "evals.json", "split": "tune", "assertions": [{"index": 1, "pass": true, "evidence": "flags 'underscores the importance'"}, {"index": 2, "pass": true, "evidence": "names retry/checkpoint"}, {"index": 3, "pass": false, "evidence": "no concrete rewrite given"}]}
```

`run_evals.py grade` reads exactly this format. The `assertions` array may also be a list of bare booleans if evidence is recorded elsewhere.

## Phase 3 — grade

The parent runs:

```bash
python3 scripts/run_evals.py grade evals/results/baseline-YYYY-MM-DD/judgments/*.jsonl \
  --out evals/results/baseline-YYYY-MM-DD/scores.jsonl
```

A case score is the fraction of assertions that passed, so a change that fixes one of three assertions reads as +0.33, not a censored 0/1. The summary breaks scores down by split.

To compare two runs:

```bash
python3 scripts/run_evals.py join --before baseline/scores.jsonl --after round-2/scores.jsonl --out delta.jsonl
python3 scripts/score_delta.py delta.jsonl --holdout-only
```

## Known limitation: same-family judging

When the apply and judge sub-agents are the same model family, the judge can favor outputs that look like its own (self-preference; see `Lessons_learned.md` → "Rewrite-eval grading inherited known judge biases"). The runbook requires a cross-family judge to dilute this. When only one family is reachable — as in the baseline recorded here — the result note must say so, and the score is read as a coverage signal rather than a calibrated number.

## Trigger queries

`evals/trigger-queries.json` tests activation, not output, so it skips the apply phase. A single routing sub-agent decides, per query, whether the skill's description should load it, then compares to `should_trigger`. Report accuracy split by tune/holdout and call out any `near-neg-` near-miss that fired.
