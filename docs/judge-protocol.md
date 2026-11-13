# Judge protocol

The repo does not call a model. `scripts/run_evals.py` builds separate worklists,
grades judgment files, and joins scores. Follow `runbooks/hillclimb-skill.md` for
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
repeats and `family` when cases share an input mechanism. For example:

```json
{"id":"case-a-trial-01","case_id":"case-a","family":"missing-source","suite":"evals.json","split":"tune","word_count":42,"assertions":[{"index":1,"pass":true,"evidence":"<quote>"}],"graded_dimensions":[{"name":"fidelity","score":5,"evidence":"<quote>"}]}
```

```bash
python3 scripts/run_evals.py grade judgments/*.jsonl --out scores.jsonl
python3 scripts/run_evals.py join --before baseline/scores.jsonl \
  --after candidate/scores.jsonl --out delta.jsonl
python3 scripts/score_delta.py delta.jsonl --holdout-only --cluster-field family
```

Use separate directories for each judge and apply model. The grader averages binary
assertions per record. `--include-graded` also averages each 1–5 dimension normalized
by 5 with those assertion values. Family, case ID, and word-count metadata survive
grading and joining. `join` rejects duplicate IDs, differing splits, and inconsistent
case/family labels; it warns about missing slots, which the audit must resolve before
any inference. Aggregate trials to per-case rates before a case-level test, or use
`--cluster-field case_id`; use family clusters for dependent cases. Equal-weight family
means prevent extra trials or near-copies from inflating N. Retain all raw trial data.

Trigger queries measure routing rather than prose quality. They use independent
routing decisions compared with `should_trigger`, with tune/holdout and near-miss
negative accuracy reported separately.
