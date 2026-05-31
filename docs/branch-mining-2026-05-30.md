# Branch mining notes — 2026-05-30

These notes record what was mined from each remote branch and what was deliberately not taken. They exist so the merged `main` can be audited without reopening every branch.

## Already mined before this session

- `origin/claude/arxiv-2604-03136-eVySl` — ancestor of current `main`; no unique commits left. Its execution runner, judge protocol, and scored baseline are already present.
- `origin/claude/mechanism-meal-line-FKXYi` — ancestor of current `main`; no unique commits left. Its README doctrine-snapshot changes are already present.

## Merged as branch history

### `origin/claude/model-style-discussion-ZdILX`

Taken:

- Procedural `Emphasis-source test` and `Syntax-relation test` in `SKILL.md`.
- Five eval cases around borrowed emphasis and earned emphasis.
- `evals/blinded-eval-harness.md` for A/B doctrine comparison and rate studies.
- Historical result notes and the 2026-05-30 no-regression holdout check.

Caveat:

- The score-delta gate is zero at ceiling on comparable old holdouts. This is treated as no-regression plus new future regression coverage, not a statistically accepted improvement claim.

### `origin/claude/thinking-out-loud-feedback-acAqK`

Taken:

- `ask-author` verdict, mandatory `Rewrite check`, and both-sides Staccato contrast rule.
- Joe Beda rewrite-invention evals, failure record, card, and result notes.
- Paul Graham false-positive resistance holdouts and meta-evals.
- 2026-05-30 rebaseline artifacts.

Fixups applied during merge:

- Resolved `Lessons_learned.md`, `evals/adversarial.json`, `scripts/validate.py`, and `latest.md` by unioning branch content with the model-style branch.
- Corrected contradictory historical notes that still called the joe.dev `That's not incidental. It's the design.` verdict a misclassification after the branch itself retracted that claim.
- Kept the score-delta-at-ceiling caveat explicit.

## Ported manually, not raw-merged

### `origin/claude/score-gist-hillclimb-BI26L`

Reason not raw-merged:

- The branch predates the `Lessons_learned.md` rename, per-case `split` schema, held-out gate, `scripts/run_evals.py`, `scripts/score_delta.py`, and the 2026-05-29 baseline.
- A raw merge conflicts in `CHANGELOG.md`, `LESSONS.md`, eval JSON files, trigger queries, and `latest.md`.

Taken:

- Copula displacement, hedged symmetry, outline-shaped conclusion, and em-dash-cluster detectors.
- Earned-use boundaries for `serves`, real `Whether X or Y` branching, and em-dash parentheticals.
- Word-list drift lesson and fake-precision correction around `delve`.
- Eval coverage, manual cases, trigger queries, lessons, and historical smoke/result notes.

Adapted to current protocol:

- Branch-driving cases were marked `split: "tune"`; they were not promoted to holdout after being used to design the doctrine.
- Fresh non-adaptive holdouts were added for the integrated detector family: `holdout-borrowed-emphasis-release-safety`, `holdout-copula-hedged-outline-combo`, `holdout-earned-branching-dash-copula`, and `holdout-ask-author-ai-tooling`.
- Graded dimensions were added to the branch-specific cases so future paired runs can distinguish quality above a binary ceiling.
- The branch's stale `LESSONS.md` content was ported into `Lessons_learned.md`; `LESSONS.md` was not resurrected.
- The em-dash rule was softened from “one dash per sentence” to “one earned dash insertion/pair,” so paired parenthetical dashes remain valid.

## Final validation contract

For the integrated state:

```bash
git diff --check
python3 scripts/validate.py
python3 scripts/run_evals.py prepare evals/evals.json evals/adversarial.json evals/rewrite-evals.json evals/meta-evals.json --split holdout --out /tmp/anti-slop-holdout-worklist.json
```

The paired branch-specific run under `evals/results/2026-05-30-branch-paired/` compares the pre-integration skill snapshot against the merged candidate on harder cases and graded dimensions.
