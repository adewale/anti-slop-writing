# Latest eval results

Date: 2026-08-29 (coverage round; statistical proof surface unchanged since 2026-05-31)

The 2026-08-29 highlighter-mining round (`evals/results/2026-08-29-highlighter-mining.md`) expanded coverage — new-register doctrine families, 13 new cases across the four suites, and the deterministic slop-lint grading layer (`docs/deterministic-graders.md`). The follow-up pre-registered scored run (`evals/results/2026-08-29-scored-run.md`) A/B-tested old vs new doctrine on the 13 new cases with a blinded Opus+Haiku panel: every mean delta is positive and both judges independently move the same three rewrite-behavior cases (deterministic checks separate the arms 3/7 vs 6/7 with no judge at all), but all four `score_delta.py` gates REJECT at N=13/5 and TOST equivalence is also not shown — so the round records coverage plus a baseline, not a measured improvement, and the run note lists the disclosed caveats (two discounted tune cases, one mis-specified assertion, an arm-B holdout miss). For statistical accept/reject evidence, the 2026-05-31 fresh-holdout run below remains the current proof surface; the old binary holdout suite is at ceiling, so zero-delta runs there remain useful only as no-regression checks.

## Current merged result notes

- `evals/results/2026-05-30-holdout-regression-check/` — procedural emphasis-source / syntax-relation doctrine: 12/12 branch-run holdout cases passed; 10/10 comparable baseline cases stayed 1.0 → 1.0.
- `evals/results/2026-05-30-rebaseline.md` and `evals/results/rebaseline-2026-05-30/` — ask-author / Rewrite check / both-sides Staccato doctrine: 15/15 holdout cases passed; 10/10 comparable baseline cases stayed 1.0 → 1.0.
- `evals/results/2026-05-27-emphasis-source-experiment.md` — blinded A/B history for procedural-vs-label wording. The qualitative artifact improved (the agent wrote the flattened sentence), while the small-N statistical gate did not accept the score delta.
- `evals/results/2026-05-30-branch-paired/` — paired pre-integration vs merged-doctrine run on harder branch-specific cases, fresh holdouts, and graded dimensions. Holdout means improved (binary 0.6042 → 0.9167; graded 0.6383 → 0.8917), but both all-case and holdout gates still REJECT because the CI overlaps zero.
- `evals/results/2026-05-31-stat-proof/` — fresh 42-case holdout run with blind A/B pair judging. Binary holdout mean improved 0.9286 → 1.0000, 95% CI [+0.0317, +0.1190], p=0.0074; graded holdout mean improved 0.9319 → 0.9988, 95% CI [+0.0245, +0.1167], p=0.0074. Both gates ACCEPT under the available blind same-family judge.

## How to read the score-delta output

Existing holdout binary assertions are saturated. For both merged doctrine branches, the joined before/after rows against `baseline-2026-05-29/scores.jsonl` have mean delta `+0.0000`; the CI overlaps zero and the sign-flip p-value is 1.0. Under the runbook, that means the change is not statistically accepted as an improvement on the old holdout surface. Improvement should instead be read from the pre-registered fresh holdout in `2026-05-31-stat-proof/`.

The safe interpretation is:

1. **No regression on existing holdouts.** The comparable holdout cases remained at 1.0.
2. **New branch cases become future regression coverage.** Branch-added cases that were introduced with their doctrine are not proof of improvement over the old baseline.
3. **Harder paired cases and/or graded dimensions are required** to make future improvements measurable above ceiling.

## Remaining measurement gaps

- Cross-family or human confirmation for the 2026-05-31 proof run. An Anthropic rerun was attempted but failed because no Anthropic API key was configured.
- Observed trigger rates in Pi, Claude Code, Codex, and OpenCode, especially for near-miss negatives.
- Future major versions still need fresh holdout refreshes from real usage traces; do not keep reusing the 2026-05-31 proof set for adaptive tuning.

## Previous results

| Date | File |
|---|---|
| 2026-05-31 | `2026-05-31-stat-proof/` |
| 2026-05-30 | `2026-05-30-holdout-regression-check/`, `2026-05-30-rebaseline.md`, `2026-05-30-branch-paired/` |
| 2026-05-29 | `2026-05-29-baseline.md`, `baseline-2026-05-29/` |
| 2026-05-25 | `2026-05-25-before.md`, `2026-05-25-after.md`, `2026-05-25-adversarial-expansion.md`, `2026-05-25-runbook-eval-drift.md` |
