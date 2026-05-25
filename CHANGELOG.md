# Changelog

All notable changes to this project are recorded here. This changelog tracks doctrine, eval coverage, compatibility, and docs because a skill can change behavior without changing code.

## [Unreleased]

### Evals

- Added adversarial evals to prevent over-flagging earned contrast, technical use of `robust`, quoted bad phrases, useful lists, and short direct answers.
- Added rewrite evals that score concrete output quality, not just critique labels.
- Added a curated failure corpus under `evals/failures/`.
- Added before/after cards under `examples/cards/` for fast inspection of core patterns.

### Docs

- Added `LESSONS.md` to record what each failure taught and what not to overgeneralize.

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
