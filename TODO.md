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

- [ ] Calibrate the subscription baseline's fidelity disagreement with human review before any promotion claim. The 18-item blinded packet and blank answers are ready in `evals/results/2026-11-14-fidelity-calibration/`; actual human scoring is pending. Keep existing holdouts frozen; later doctrine changes need tune cases and their own study.
- [ ] Run revision 2 of the pre-registered rewrite-only re-judging in `evals/results/2026-11-14-rewrite-only-rejudge/` (488 extraction, up to 444 audit and 1,776 judge calls; ~$80 list-price equivalent, authorized existing subscriptions only). Retain empty deliverables, audit extraction faithfulness before judging, and stop for review on any negative audit. Publish view sensitivity and uncertainty as registered; this is not a pure causal critique effect or human fidelity calibration.
- [ ] Complete live-client coverage for **native Codex and OpenCode**. Pi and guarded Claude Code now have 29 queries × three valid fresh sessions each. Codex's registered native model was unsupported on the subscription; a different model needs a separately fixed instrument. OpenCode was absent and was not installed. Do not invent rates or substitute the old routing classifier.

## Open — 2026-11-13 review

- [x] Land eval-integrity changes: #26 merged. The completed subscription baseline's joint criterion failed; no doctrine was promoted from isolated positive rows.
- [x] Port #17 as fresh case-only #28, now merged, and complete the bounded compound/#18 screen. All eight original Twitter records remain; compound's positive one-scaffold estimates did not clear standing or supplied-fact quality guards. The broad #18 PR was closed as not adopted; its source remains available.
- [x] Split highlighter into tested triage-only lint plus grounded coverage, and complete the cataphoric-teaser screen. Full results: `evals/results/2026-11-14-candidate-studies/`; no candidate installed.
- [ ] Repair SKILL.md's unsourced examples, mandatory aphorism field, carrier terminology, duplicated lists, and maintainer text in separately measured rounds. No doctrine was changed during instrument repair.
- [x] Complete authorized PR/branch housekeeping. #22/#25/#26/#28 merged; #21 closed as superseded. Eleven stale remote branches deleted with atomic expected-head leases. Stop-slop's only differing added script was an unused import; three archive tags retain unmatched historical source history. Audit/actions: `evals/results/2026-11-14-followthrough/`. Original stash and local branches/worktrees preserved.

## Done — 2026-11-14

- [x] Complete the frozen candidate screen: 1,122 apply outputs, 2,244 valid judgments, all raw/replacement data retained and analyses reproduced offline. Neither candidate clears its eight standing-holdout co-primary contrasts; five of 64 point guards fail. No promotion.
- [x] Measure actual initial-turn body loading: 174 valid sessions in controlled Pi and guarded Claude Code. Majority sensitivity 7/12 each; specificity 16/17 and 17/17. Material instrument amendments and excluded cohorts are disclosed, not pooled.
- [x] Prepare the 18-item blind human fidelity-calibration packet without pretending a model is a human reviewer.

- [x] Review the nineteen facts-supplied twins from `69ade5d`, including five holdout twins. Audit, validity corrections, pair-preserving scoring, and tests are in `evals/results/2026-11-14-fact-pair-review/`. That validity review itself generated no model results.
- [x] **Cross-family judging and no-skill baselines.** Completed 804 outputs and 1,608 judgments using Sonnet 5.5/GPT-6.1 Sol apply models and Opus 5.5/GPT-6.1 Sol judges. All 59 core cases and eight antithesis/control cases received three trials per arm/model. The joint criterion failed and fidelity judgments disagreed; see `evals/results/2026-11-14-subscription-baseline/README.md`.
