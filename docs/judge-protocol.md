# Judge protocol

The generic `scripts/run_evals.py` runner does not call a model: it builds separate
worklists, grades judgment files, and joins scores. The opt-in, repo-only
`scripts/subscription_baseline.py` supplies CLI/SDK model orchestration for the
recorded subscription study; it is not part of the installable skill. Follow `runbooks/hillclimb-skill.md` for
preregistration, model access, fresh contexts, independent units, and promotion.

## Prepare and apply

```bash
mkdir -p /tmp/apply /tmp/private
python3 scripts/run_evals.py prepare evals/evals.json evals/rewrite-evals.json \
  --split all --out /tmp/apply/work.json --judge-out /tmp/private/judge.json
```

`--out` is now apply-only. `--judge-out` is required and must name a different file.
An apply unit contains its identity and `apply_prompt`; it contains no assertions,
expected answer, graded dimensions, or dynamic rubric. Source fixture `input.md`
text and the facts block are embedded. `facts: []` means no extra facts beyond the
source; it does not license invented details. Unsupported numbers remain unsupported.

An apply worker gets one unit and a full opaque skill copy, including references.
For the no-skill arm, prepare with `--no-skill`; this sends the identical case task
and facts without the skill instruction. Use one fresh context per trial. Mount only its input, skill copy, and
output destination. Never give it the suite, judge worklist, repository, reference
answers, or other trials. The orchestrator enforces file access and audits transcripts.
Worklist separation is not a filesystem sandbox.

## Blind and judge

Run `run_evals.py blind` before handing outputs to judges. It strips configured
version-specific template fields, assigns random filenames, and records raw and
judged whitespace word counts. Keep the blinding key, raw word counts, and original outputs private.
Review the payload for additional version cues. Rewrite-only judging is another
option when pre-registered; never grade presence of a template field as writing quality.

Judge units carry the prompt and facts, expected behavior, assertions, graded
dimensions, and the dynamic rubric instruction. Append the corresponding blinded
output to the judge prompt. A judge sees no skill text, arm identity, or blinding key.
It must ignore instructions embedded in outputs.

For each assertion, require quoted evidence for the actual behavior. A keyword is
insufficient. Missing facts may require a precise ask-author request or a cut; a
fluent invented mechanism fails fidelity. Score every requested dimension from 1–5,
with evidence. When a dynamic rubric is supplied, generate its requested criteria
before scoring and retain them in the judgment record. The current grader reports
fixed assertions and dimensions; it does not aggregate extra dynamic criteria.

Use two judges from different families, both judging every apply family and arm.
Report agreement by apply family. Same-family judging must be labeled as coverage
evidence and leave promotion pending confirmation. Report length differences beside
scores; the current scripts record counts but implement no automatic length adjustment.

## Judgment and score files

Write one JSON object per trial, using a unique `id` for the slot. Record `case_id` for
repeats and `family` when cases share an input mechanism. `prepare` also puts
`pair_id` and `fact_condition` in judge units and the requested judgment schema;
keep these out of apply units. Each facts-supplied twin and its original share a
`pair_id`. Unpaired cases use their own ID. Preserve these fields in judgments.
For example:

```json
{"id":"case-a-trial-01","case_id":"case-a","family":"missing-source","suite":"evals.json","split":"tune","pair_id":"case-a","fact_condition":"no_additional_facts","word_count":42,"assertions":[{"index":1,"pass":true,"evidence":"<quote>"}],"graded_dimensions":[{"name":"fidelity","score":5,"evidence":"<quote>"}]}
```

```bash
python3 scripts/run_evals.py grade judgments/*.jsonl \
  --worklist /tmp/private/judge.json --out scores.jsonl
python3 scripts/run_evals.py join --before baseline/scores.jsonl \
  --after candidate/scores.jsonl --out delta.jsonl
python3 scripts/score_delta.py delta.jsonl --holdout-only --cluster-field family
```

Use `--worklist` for all new studies, pointing to the frozen judge file from `prepare`.
Each record must contain every assertion index and requested dimension name exactly
once, with non-empty evidence. Suite, split, pair ID, and fact condition must match
the worklist. Assertion order is immaterial. For repeated trials, `case_id` selects
the worklist case while `id` identifies the unique slot; without `case_id`, `id`
selects the case. Every worklist case in the selected `--split` must have a judgment.
These checks run before writing scores, even when dimensions are not included in
the aggregate. Evidence presence is checked, not its truth or quotation accuracy.
The study audit must still verify the pre-registered number of trials per case,
models, judges, exclusions, and outcome separation; a case worklist is not a trial
slot manifest. Omitting `--worklist` retains legacy archive grading with a warning
and cannot establish complete assertion or case coverage.

Use separate directories for each judge and apply model. The grader averages binary
assertions per record. `--include-graded` also averages each 1–5 dimension normalized
by 5 with those assertion values. Family, case ID, fact-pair ID, fact condition, and word-count metadata survive
grading and joining. `join` rejects duplicate IDs, differing splits, inconsistent
case/family labels, and unequal slot sets. Resolve missing slots before inference.
`--allow-partial` explicitly permits an intersection with warnings for inspection
only; it is not a valid study comparison. Aggregate trials to per-case rates before
a case-level test, or use `--cluster-field case_id`; use family clusters for dependent
cases. Equal-weight family
means prevent extra trials or near-copies from inflating N. Retain all raw trial data.

Trigger queries measure routing rather than prose quality. They use independent
routing decisions compared with `should_trigger`, with tune/holdout and near-miss
negative accuracy reported separately.

## Fact-pair analyses

Report the no-additional-facts and supplied-facts conditions separately, comparing
skill versus no skill within each condition. A gain on one side can hide a loss on
the other in a pooled average. The fact condition describes the additional facts
block; a source paragraph can itself contain usable facts even when that block is empty.

For a pooled analysis, use `score_delta.py --cluster-field pair_id` after aggregating
trials to case rates, or a broader pre-registered family that keeps each pair together.
The gate rejects a repeated `pair_id` split across independent units. Two conditions
of one task do not supply two independent tasks. Legacy score files without pair
metadata still need a manual dependence audit before inference.

Graded dimensions assess what the source makes possible. A precise question or
justified cut can earn full marks when a required fact is absent. With sufficient
facts, use them in the requested answer; an answer that only asks or cuts fails.
Additional questions about a genuinely unspecified comparator or causal explanation
may accompany a grounded rewrite. Before/after timing or cost observations do not
establish a cause. A named `Rewrite check` field is never evidence of writing quality.

Pre-register rewrite fidelity and task fulfillment as primary outcomes for an efficacy
claim. Report procedure compliance (for example, producing a flattened residual claim)
as a diagnostic, separately from writing quality. An aggregate gain driven only by
such artifacts cannot establish better writing. `grade` still averages the assertions
it receives; the scoring/audit script must implement the pre-registered outcome split.
