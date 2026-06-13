# Reference-anchor tests

A reference-anchor is an eval case that pins a **fixed, human-reviewable floor** for a
single high-value rewrite and uses it as a don't-regress gate for future models and future
skill versions. It complements the existing assertion/graded suites: those measure whether
the skill catches a failure pattern; an anchor measures whether a rewrite of one concrete
piece still scores at least as well as the best one we have. It is a floor, not a ceiling:
a candidate must meet or beat the reference, and a future rewrite that clears every
assertion can raise the floor.

## When to add one

- You have done deep work on one real artifact (a tweet, a post, a README) and produced a
  rewrite you are willing to set as the floor (the minimum future rewrites must match).
- You want to detect regressions on that specific piece when the model or the doctrine
  changes, and you want a human to be able to review the original and the best version
  without running the harness.

## Shape

A reference-anchor case is a normal `evals/<suite>.json` case (it still has `id`, `split`,
`prompt`, `expected_output`, `assertions`, optional `graded_dimensions`) plus:

```json
"kind": "reference-anchor",
"reference": {
  "original": "evals/fixtures/<name>/input.md",
  "best_rewrite": "evals/fixtures/<name>/best-rewrite.md",
  "human_review": "evals/fixtures/<name>/HUMAN-REVIEW.md",
  "model": "<model id that produced the best rewrite>",
  "captured": "YYYY-MM-DD",
  "reference_score": 1.0,
  "reference_graded_score": 1.0,
  "scorecard": "evals/results/<date>-<name>/reference-scorecard.jsonl",
  "protocol": "one-paragraph description of how to re-run and compare"
}
```

Rules:

- **Split is `holdout`.** An anchor is a merge-time gate, never used to tune doctrine. If a
  future candidate falls short, write a new tune case; do not edit doctrine to pass it.
- The `assertions` characterize the properties a passing rewrite must have — they are the
  bar a future candidate must clear. Keep them behavioral and quote-checkable.
- `reference_score` / `reference_graded_score` are the scores the stored `best_rewrite`
  achieves against those assertions/dimensions (in [0,1]). They are the **floor**: a
  candidate must score at least this. Record the scorecard that produced them.
- The `best_rewrite` is the floor, not a one-shot skill output. It may be hand-tuned by
  an expert/model against the skill's own detectors. The floor is editable upward: replace
  it (and re-record the scorecard) only with a rewrite that scores at least as high on
  every assertion and dimension.

## How it is enforced

`scripts/validate.py` scans every eval suite for cases with a `reference` object and checks
that `original`, `best_rewrite`, `human_review`, and `scorecard` files exist and that
`reference_score` / `reference_graded_score` are floats in [0,1]. This keeps the artifacts
from rotting away from the case.

## How to run the regression check

1. Apply the skill to the case `prompt` with the model/version under test → candidate.
2. Judge the candidate against the case `assertions` and `graded_dimensions` (use
   `scripts/run_evals.py grade`) → `candidate_score`.
3. Compare `candidate_score` to `reference_score`. The reference is the floor: a candidate
   scoring at or above it passes; a candidate below it (or with any graded dimension below
   the reference) is a regression to investigate.
4. Re-judge `best_rewrite` itself each round (should still hit `reference_score`); a change
   there is judge drift, not a skill change.

## Worked example

`tweet-best-rewrite-anchor` in `evals/rewrite-evals.json`, with artifacts under
`evals/fixtures/tweet-taste-as-model/` and the reference scorecard in
`evals/results/2026-06-13-tweet-best-anchor/`.
