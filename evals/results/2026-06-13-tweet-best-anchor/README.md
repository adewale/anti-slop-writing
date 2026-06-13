# 2026-06-13 — Tweet best-rewrite reference anchor

A new kind of test: a fixed **don't-regress ceiling** for rewriting one real piece. It
captures the original tweet and the best known rewrite, characterizes what makes that
rewrite top-scoring (six assertions + four graded dimensions), and records the score the
best rewrite achieves so future models and future skill versions can be measured against
it.

- **Case:** `tweet-best-rewrite-anchor` in `evals/rewrite-evals.json` (split `holdout`,
  `kind: reference-anchor`).
- **Original:** `evals/fixtures/tweet-taste-as-model/input.md`
- **Best known rewrite (the ceiling):** `evals/fixtures/tweet-taste-as-model/best-rewrite.md`
- **Human review (original vs best, line-level):** `evals/fixtures/tweet-taste-as-model/HUMAN-REVIEW.md`
- **Rewrite model/version:** claude-opus-4-8, 2026-06-13.

## Reference score

| Scoring | Reference (best-rewrite.md) |
|---|---:|
| Binary assertions | 1.000 (6/6) |
| With graded dimensions | 1.000 |

Scorecard: `reference-scorecard.jsonl` (per-assertion + per-dimension judgments).
Recomputed by the harness: `reference-score.jsonl`, `reference-score-graded.jsonl`.

## Regression protocol

This anchor is meant to be re-run when a model or the skill changes:

1. Apply the skill to the case `prompt` with the model/version under test. Produce a full
   rewrite (a candidate).
2. Judge the candidate against the case `assertions` and `graded_dimensions`. Record
   `candidate_score`.
3. Compare to the reference. The best rewrite is the fixed ceiling at 1.0. The gap
   `reference_score - candidate_score` is what you track over versions; a candidate score
   that **drops across skill versions** is a regression to investigate.
4. Re-judge `best-rewrite.md` itself each round (it should still score 1.0). If it does
   not, that is judge drift, not a skill change — recalibrate the judge or refresh the
   reference, do not "fix" the skill.
5. **Never edit doctrine to pass this holdout case.** If the candidate gap widens, write a
   new tune case for the next round (the standard holdout rule).

## Notes

- The ceiling is editable. If a reviewer or a future run produces a strictly better
  rewrite that scores at least as high on every assertion and dimension, replace
  `best-rewrite.md` and re-record this scorecard.
- The reference rewrite was hand-tuned by claude-opus-4-8 against the skill's own
  self-detectors, so 1.0 is expected; it represents an expert-guided ceiling, not a plain
  one-shot skill application. That is the point — it is the bar a plain application should
  approach.
- Single-judge caveat applies (the scorecard was graded by one Opus-family judge). A
  cross-family judge pass is the documented next step for any high-stakes use.
