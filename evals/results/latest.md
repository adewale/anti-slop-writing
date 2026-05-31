# Latest eval results

Date: 2026-05-30

This note supersedes the 2026-05-29 infrastructure baseline after merging the branch work on procedural emphasis-source tests and rewrite self-check doctrine. The binary holdout suite is at ceiling, so `scripts/score_delta.py` reports `REJECT` for zero-delta runs: that is evidence of no measured improvement on the saturated baseline, not evidence of a regression.

## Current merged result notes

- `evals/results/2026-05-30-holdout-regression-check/` — procedural emphasis-source / syntax-relation doctrine: 12/12 branch-run holdout cases passed; 10/10 comparable baseline cases stayed 1.0 → 1.0.
- `evals/results/2026-05-30-rebaseline.md` and `evals/results/rebaseline-2026-05-30/` — ask-author / Rewrite check / both-sides Staccato doctrine: 15/15 holdout cases passed; 10/10 comparable baseline cases stayed 1.0 → 1.0.
- `evals/results/2026-05-27-emphasis-source-experiment.md` — blinded A/B history for procedural-vs-label wording. The qualitative artifact improved (the agent wrote the flattened sentence), while the small-N statistical gate did not accept the score delta.
- `evals/results/2026-05-30-branch-paired/` — paired pre-integration vs merged-doctrine run on harder branch-specific cases, fresh holdouts, and graded dimensions. Holdout means improved (binary 0.6042 → 0.9167; graded 0.6383 → 0.8917), but both all-case and holdout gates still REJECT because the CI overlaps zero.

## How to read the score-delta output

Existing holdout binary assertions are saturated. For both merged doctrine branches, the joined before/after rows against `baseline-2026-05-29/scores.jsonl` have mean delta `+0.0000`; the CI overlaps zero and the sign-flip p-value is 1.0. Under the runbook, that means the change is not statistically accepted as an improvement on the old holdout surface.

The safe interpretation is:

1. **No regression on existing holdouts.** The comparable holdout cases remained at 1.0.
2. **New branch cases become future regression coverage.** Branch-added cases that were introduced with their doctrine are not proof of improvement over the old baseline.
3. **Harder paired cases and/or graded dimensions are required** to make future improvements measurable above ceiling.

## Remaining measurement gaps

- Cross-family or human spot-check for the same-family judge limitation noted in both 2026-05-30 result notes.
- Observed trigger rates in Pi, Claude Code, Codex, and OpenCode, especially for near-miss negatives.
- More independent branch-specific holdout cases; the first paired run moved the mean but did not clear the gate at N=4 holdouts.
- Cross-family or human judging for the branch-paired run; current apply/judge agents are same-family, so treat scores as coverage signals.

## Previous results

| Date | File |
|---|---|
| 2026-05-30 | `2026-05-30-holdout-regression-check/`, `2026-05-30-rebaseline.md`, `2026-05-30-branch-paired/` |
| 2026-05-29 | `2026-05-29-baseline.md`, `baseline-2026-05-29/` |
| 2026-05-25 | `2026-05-25-before.md`, `2026-05-25-after.md`, `2026-05-25-adversarial-expansion.md`, `2026-05-25-runbook-eval-drift.md` |
