# Changelog

All notable changes to this project are recorded here. This changelog tracks doctrine, eval coverage, compatibility, and docs because a skill can change behavior without changing code.

## [Unreleased]

### Hillclimb infrastructure

- Added `scripts/run_evals.py`, an execution runner with `prepare` / `grade` / `join` subcommands over the eval suites, filtered by split. Orchestration only — the repo is instruction-only, so model calls are done by sub-agents.
- Added `docs/judge-protocol.md`, the file-based apply → judge → grade protocol that sub-agents follow, with the strict judgment-line format `run_evals.py grade` consumes.
- Added a clean scored baseline: `evals/results/2026-05-29-baseline.md` plus `evals/results/baseline-2026-05-29/` (38 skill-applied outputs, per-assertion judgments, 26 trigger decisions, `scores.jsonl`). Binary assertions are at ceiling (115/115, 26/26 trigger); the `length-control` graded dimension fails on two rewrites, which on inspection is a rubric-calibration bug (it penalizes mechanism-adding rewrites for exceeding input length), not a skill regression — recorded as the first eval-calibration item for the next round.
- Added `TODO.md` tracking the blocked discourse-layer failure-example item and the cross-family-judge follow-up.
- Added tune/holdout split to every eval file (`evals/evals.json`, `evals/adversarial.json`, `evals/rewrite-evals.json`, `evals/meta-evals.json`, `evals/trigger-queries.json`). Holdout cases are scored only at end-of-round and at merge; doctrine must not be edited in response to a holdout failure.
- Added `scripts/score_delta.py` for paired-bootstrap and sign-flip-permutation gating; the runbook now requires ACCEPT on the holdout split before merge.
- Added `dynamic_rubric` (per-instance criteria) and `graded_dimensions` (orthogonal 1-5 axes) schema fields on rewrite-eval cases.
- Added `near-neg-` near-miss negatives to `evals/trigger-queries.json` (fact-check, link-check, draft-from-bullets, storyboard, slide-export, docx-from-dataset).
- Added new holdout cases to every suite: `fake-precision-unnamed-source`, `stacked-rule-of-three`, `abstract-system-noun-stack`, `earned-importance-immediate-mechanism`, `cost-benefit-not-just-earning-the-contrast`, `research-methods-staccato`, `fake-precision-rewrite-finance`, `product-tour-rewrite-developer-tools`, `noise-vs-signal-on-small-suite`, `judge-self-preference`.
- Updated `scripts/validate.py` to enforce per-case split, minimum holdout counts per suite, and the `near-neg-` near-miss requirement on trigger queries.
- Added `evals/rejected-edits.md` graveyard so previously rejected edits are not relitigated.
- Added `docs/hillclimb-improvements.md` with sources for all thirteen changes (Dwork, Blum & Hardt, Miller, Bowyer, WritingBench, FLASK, BFCL, Panickssery, Dubois, Hamel/Shankar, GEPA, SkillOpt, Decagon, Schaeffer).

### Evals

- Added adversarial evals to prevent over-flagging earned contrast, technical use of `robust`, quoted bad phrases, useful lists, short direct answers, exact `not just` distinctions, controlled-variable staccato, concrete tables, ordered three-step sequences, direct warnings, source-backed `highlights`, and imperative runbook steps.
- Added adversarial evals from a generalization test on a Paul Graham essay: `earned-antithesis-synthesis-pg`, `cataphoric-label-defined-in-paragraph`, and `escalating-magnitude-triple` lock in false-positive resistance against dense earned human rhetoric the doctrine was not tuned on.
- Added meta-evals `single-source-overfitting` (repeated tuning against one document does not prove generalization) and `earned-rhetoric-false-positive-rate` (how to read a near-zero flag rate on clean prose honestly).
- Added rewrite evals that score concrete output quality, not just critique labels.
- Added rewrite evals covering rewrites that reuse the flagged cadence under different punctuation (`rewrite-reuses-flagged-pattern`) and rewrites that should ask the author or cut instead of inventing a specific (`rewrite-asks-or-cuts-when-fact-missing`).
- Added meta-evals for ceiling effects, metric artifacts, capability drift, trigger drift, and judge drift.
- Added a curated failure corpus under `evals/failures/`, including `rewrite-reuses-flagged-pattern.md`.
- Added before/after cards under `examples/cards/` for fast inspection of core patterns.

### Doctrine

- Added a final self-check and one bounded judge-refine pass for high-stakes prose.
- Extended the Final self-check to require running the same detectors on the rewrite and to require asking or cutting when a rewrite would need a fact not present in the source.
- Added `ask-author` as a verdict in the Critique output format, with a triggering rule in the Default editing pass: do not invent a tool, person, count, or timing to fill the Concrete rewrite slot when the source paragraph does not supply it.
- Tightened the antithesis classification rule: read the prior sentence in the paragraph before grading contrast as compressed or decorative. Anchored on a real failure from joe.dev/posts/thinking-out-loud where the skill graded earned contrast as decorative because it scored the sentence alone.
- Added a mandatory `Rewrite check` field to the Critique output format so the same detectors run against every Concrete rewrite (including ask-author fallbacks) inside the per-item loop, not at end-of-document. Added a "Rewrites must pass the same detectors as the source" section to `references/rewrite-patterns.md` with real before/after pairs from the joe.dev review.
- Clarified the Staccato contrast test in `SKILL.md` with the both-sides test: an antithesis is earned only when both sides of the contrast are evidenced in the prior prose, not when only the topic of the contrast was mentioned. Carries the joe.dev pair as the canonical compressed example. Corrected the eval assertion and failure-file claims that previously framed the model's compressed verdict on `That's not incidental. It's the design.` as a misclassification.

### Docs

- Added `Lessons_learned.md` (originally `LESSONS.md`) to record what each failure taught and what not to overgeneralize.
- Added `runbooks/hillclimb-skill.md` to keep multi-artifact skill improvements from stopping early; rewritten to include the held-out gate, statistical gating, cross-family judge protocol, length normalization, saturation stop, Pareto-front carryforward, length budget, and eval-rot refresh policy.
- Added `docs/eval-runbook-notes.md` to record the external runbook and eval-drift ideas that shaped this iteration.
- Added `docs/hillclimb-improvements.md` as the single source of truth for the thirteen hillclimb-infrastructure changes and their citations.

## [0.1.0] - 2026-05-25

### Added

- Packaged `anti-slop-writing` as an instruction-only Agent Skill.
- Added compatibility notes for Pi, Claude Code, Codex, OpenCode, claude.ai, and Claude API.
- Added machine-readable output evals, trigger-query evals, manual cases, and smoke eval results.
- Added GitHub Actions validation.
- Added contributor guidance and a validation script.

### Doctrine

- Established the core rule: sharp detail beats inflated significance.
- Added flow-by-relation and carrier-bound conclusion checks.
- Added staccato contrast handling so the skill distinguishes earned compression from decorative rhythm.
