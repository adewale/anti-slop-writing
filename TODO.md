# TODO

Tracked work for the `anti-slop-writing` hillclimb loop. Done items stay listed for one cycle so the next contributor sees what changed.

## Blocked — needs a human

- [ ] **Real discourse-layer failure examples.** 3–5 pieces of multi-paragraph prose (~500+ words) that use no banned phrases and read fine at the sentence level but are still slop: over-explained takeaway, flat paragraph escalation (siblings at the same altitude), or single-track structure with no counter-evidence. These cannot be synthesized here without circularity (drafting the rule then writing examples to fit it) or contamination (public long-form may be in training data). See `Lessons_learned.md` → "Doctrine reaches the surface layer." Until these land, the discourse-layer doctrine work in `SKILL.md` stays blocked.
  - Acceptance: each example added to `evals/failures/`, plus `tune` cases in an eval file and at least one `holdout` case in the same vein.

## Done — 2026-05-29

- [x] **Execution runner** (`scripts/run_evals.py`): prepare/grade/join over the eval suites, filtered by split. Orchestration only — the repo is instruction-only, so model calls are done by sub-agents per `docs/judge-protocol.md`.
- [x] **Judge implementation using sub-agents** (`docs/judge-protocol.md`): file-based apply → judge → grade protocol, with the strict judgment-line format the runner consumes.
- [x] **Clean baseline** (`evals/results/2026-05-29-baseline.md` + `evals/results/baseline-2026-05-29/`): current skill scored on every tune and holdout case, recorded as the comparison point future rounds join against.

## Open — buildable without the blocked item

- [ ] Calibrate the subscription baseline's fidelity disagreement with human review before any promotion claim. Keep existing holdouts frozen; any later doctrine change needs tune cases and its own study.
- [ ] **Observed multi-run trigger rates** in Pi, Claude Code, Codex, and OpenCode. The baseline records a single routing-decision pass, not live multi-run activation rates.

## Open — 2026-11-13 review

- [ ] Land the eval-integrity changes. The owner subsequently authorized subscription-backed baselines before merge; the preregistered run is complete in `evals/results/2026-11-14-subscription-baseline/`. Its joint improvement criterion failed; do not promote doctrine from isolated positive rows.
- [ ] Recreate or rebase #17 and #18 on fresh branches after the instrument lands; replicate without treating trials as independent cases. #18 needs an independent-case design or a bounded single-case claim.
- [ ] Prepare the highlighter split (lint and grounded examples only) and evaluate the cataphoric-teaser candidate under the repaired protocol.
- [ ] Repair SKILL.md's unsourced examples, mandatory aphorism field, carrier terminology, duplicated lists, and maintainer text in separately measured rounds. No doctrine was changed during instrument repair.
- [ ] Review the owner-only closure/merge/deletion recommendations in `evals/results/2026-11-13-eval-integrity.md`. The stop-slop branch fails the handoff's deletion test; retain it pending investigation.

## Done — 2026-11-14

- [x] Review the nineteen facts-supplied twins from `69ade5d`, including five holdout twins. Audit, validity corrections, pair-preserving scoring, and tests are in `evals/results/2026-11-14-fact-pair-review/`. That validity review itself generated no model results.
- [x] **Cross-family judging and no-skill baselines.** Completed 804 outputs and 1,608 judgments using Sonnet 5.5/GPT-6.1 Sol apply models and Opus 5.5/GPT-6.1 Sol judges. All 59 core cases and eight antithesis/control cases received three trials per arm/model. The joint criterion failed and fidelity judgments disagreed; see `evals/results/2026-11-14-subscription-baseline/README.md`.
