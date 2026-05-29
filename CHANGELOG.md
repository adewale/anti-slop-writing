# Changelog

All notable changes to this project are recorded here. This changelog tracks doctrine, eval coverage, compatibility, and docs because a skill can change behavior without changing code.

## [Unreleased]

### Hillclimb infrastructure

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
- Added rewrite evals that score concrete output quality, not just critique labels.
- Added meta-evals for ceiling effects, metric artifacts, capability drift, trigger drift, and judge drift.
- Added a curated failure corpus under `evals/failures/`.
- Added before/after cards under `examples/cards/` for fast inspection of core patterns.

### Doctrine

- Added a final self-check and one bounded judge-refine pass for high-stakes prose.

### Docs

- Added `LESSONS.md` to record what each failure taught and what not to overgeneralize.
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
