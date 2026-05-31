# Changelog

All notable changes to this project are recorded here. This changelog tracks doctrine, eval coverage, compatibility, and docs because a skill can change behavior without changing code.

## [Unreleased]

### Doctrine

- Added two procedural detectors to `skills/anti-slop-writing/SKILL.md`: the **emphasis-source test** (write the flattened version of the line in the critique; judge whether the residual claim still names actor/mechanism/limit) and the **syntax-relation test** (restate the implied relation with a connective; if no connective fits without invention, the syntax was empty). Sourced from Ruth Starkman, "Model Style Is So Cringe." Retained on qualitative behavioral evidence: under the blinded harness the procedural wording reliably produces the flatten artifact in critique text while the labeled wording does not. The +1 score delta from the worked Round 5 does not pass `scripts/score_delta.py` at N=5 (CI overlaps zero, sign-flip p=1.0); recorded honestly in `evals/results/2026-05-27-emphasis-source-experiment.md` and the gate output in `evals/results/2026-05-28-emphasis-source-procedural/`.

### Evals

- Added five eval cases for the emphasis-source diagnostic, all with proper splits: `evals/evals.json` → `borrowed-emphasis` (tune), `paragraph-scale-borrowed-emphasis` (tune); `evals/rewrite-evals.json` → `emphasis-source-flatten` (tune); `evals/adversarial.json` → `earned-emphasis-from-idea` (holdout), `earned-paragraph-escalation` (holdout). Plus `evals/failures/borrowed-emphasis.md` and `examples/cards/borrowed-emphasis.md`.
- Added `evals/blinded-eval-harness.md`: doctrine A/B comparison with anonymized labels and a rate-study procedure for behaviors that vary run-to-run. Extends the standard `docs/judge-protocol.md` apply-judge separation with the additional discipline a fair doctrine comparison requires.
- Added `evals/rejected-edits.md` entry: paragraph-scale ladder guidance on the emphasis-source test was tried and reverted as inert (rate study: 3/3 vs 3/3 on both decisive prompts).
- Ran the held-out regression check under the new protocol: this branch's doctrine scores 10/10 on the upstream's holdout cases, matching the 2026-05-29 baseline case-for-case. Per-case delta is exactly 0.0 on every joined case. The procedural emphasis-source change does not regress any upstream holdout case. Full run in `evals/results/2026-05-30-holdout-regression-check/` with outputs, judgments, scores, joined delta, and captured gate output.

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
- Added rewrite evals that score concrete output quality, not just critique labels.
- Added meta-evals for ceiling effects, metric artifacts, capability drift, trigger drift, and judge drift.
- Added a curated failure corpus under `evals/failures/`.
- Added before/after cards under `examples/cards/` for fast inspection of core patterns.

### Doctrine

- Added a final self-check and one bounded judge-refine pass for high-stakes prose.

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
