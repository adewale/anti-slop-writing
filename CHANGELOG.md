# Changelog

All notable changes to this project are recorded here. This changelog tracks doctrine, eval coverage, compatibility, and docs because a skill can change behavior without changing code.

## [Unreleased]

### Evals

- Added adversarial evals to prevent over-flagging earned contrast, technical use of `robust`, quoted bad phrases, useful lists, short direct answers, exact `not just` distinctions, controlled-variable staccato, concrete tables, ordered three-step sequences, direct warnings, source-backed `highlights`, and imperative runbook steps.
- Added rewrite evals that score concrete output quality, not just critique labels.
- Added meta-evals for ceiling effects, metric artifacts, capability drift, trigger drift, and judge drift.
- Added a curated failure corpus under `evals/failures/`.
- Added before/after cards under `examples/cards/` for fast inspection of core patterns.
- Added evals for copula displacement (`serves as`, `stands as`), hedged symmetry (`Whether X or Y`, `While X, Y is also important`), outline-shaped conclusions (`Despite challenges, X continues to thrive`, `Looking ahead, X will play a pivotal role`), and decorative em-dash clusters; each with an adversarial counterpart where the pattern is earned.
- Added a `word-list-drift` meta-eval that treats high-risk word and phrase lists as time-dated detectors keyed to model generation.
- Added trigger queries for hedged-symmetry rewrites (positive) and mechanical em-dash replacement (negative).
- Added manual cases 6-9 in `evals/cases.md` aligned with the new JSON evals.

### Doctrine

- Added a final self-check and one bounded judge-refine pass for high-stakes prose.
- Added detectors for copula displacement, hedged symmetry, em-dash cadence, and outline-shaped conclusion templates to SKILL.md and the doctrine reference.
- Added editing-pass steps for displaced copulas, hedged symmetry, outline conclusion templates, and decorative em-dash clusters.
- Added a note that high-risk word and phrase lists are time-dated and should be re-profiled against a current human-vs-LLM corpus; `delve` is the cautionary example.

### Docs

- Added `LESSONS.md` to record what each failure taught and what not to overgeneralize.
- Added `runbooks/hillclimb-skill.md` to keep multi-artifact skill improvements from stopping early.
- Added `docs/eval-runbook-notes.md` to record the external runbook and eval-drift ideas that shaped this iteration.
- Added six lesson entries dated 2026-05-27 covering copula displacement, hedged symmetry, outline conclusions, em-dash cadence, word-list drift, and an injected-fake-precision self-correction.
- Recorded a live smoke run (`evals/results/2026-05-27-smoke-run.md`) and an independent cold-grader pass that re-judged the verdict-sensitive assertions without the doctrine loaded.

### Fixed

- Removed an unsourced "roughly 80%" drop figure for `delve` from the doctrine reference, the `word-list-drift` meta-eval, and `LESSONS.md`; the public reporting supports only a qualitative decline. Added an explicit instruction not to invent the percentage. This was the anti-slop doctrine reproducing the fake-precision failure it warns against.
- Moved the `serves as` and `stands as` entries out of the SKILL.md and doctrine-reference words lists into the dedicated copula-displacement detector sections only. They are two-word context-dependent templates, not single lexemes, and a flat words list would risk over-flagging earned uses such as `The retry policy serves three distinct failure modes: ...`.
- Fixed three trailing additive em-dashes in this session's own prose (one in `LESSONS.md`, two in `evals/results/2026-05-27-smoke-run.md`) that tripped the new em-dash detector. Replaced with commas or restructured clauses.

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
