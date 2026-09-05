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

- [ ] **Cross-family judge.** The baseline judges are Claude grading Claude output (same-family, self-preference risk per `Lessons_learned.md`). A non-Claude judge is not available in the current harness. Wire one in when a second model family is reachable.
- [ ] **Re-run the coined-compound-label round with adequate power.** The 2026-09-05 round showed a consistent 4/8 -> 8/8 Sonnet flag rate with clean adversarial guards and still returned REJECT, because a two-sided sign-flip test on four discordant pairs cannot go below p=0.125. Needs roughly 12 trials per arm, a doctrine that quotes no fixture string (`candidate-v2-SKILL.md` is the decontaminated snapshot), and the fresh-coinage fixture (`probe-fixture-p4.md`) scored separately from the tuning one. Full record and the two design defects to avoid are in `evals/results/2026-09-05-astra-compound-labels/` and `Lessons_learned.md`.
  - Acceptance: `scripts/score_delta.py` ACCEPT on the discriminating fixture with the decontaminated doctrine, guards still kept in every run, or a second graveyard entry saying the rule does not generalize.
- [ ] **Instruction-precedence behaviour on a non-Claude model.** The GPT-6 Astra guide warns that a skill file "may cause the model to pause and block work early" and recommends an explicit precedence line; `SKILL.md` has none. The risk did not reproduce on Sonnet (`evals/results/2026-09-05-astra-compound-labels/outputs/precedence-sonnet.md`: the skill shipped the line when asked and waived the mandatory `Rewrite check` when asked), but the warning is about a model not reachable from this harness. Re-probe when a GPT-family or other non-Claude runner is available, and only then decide whether a precedence line earns its words. Shares a blocker with the cross-family judge item above.
  - Acceptance: `probe-precedence.md` re-run on a non-Claude model, result recorded, and either a precedence line added with eval coverage or a note that the skill already complies.
- [ ] **Observed multi-run trigger rates** in Pi, Claude Code, Codex, and OpenCode. The baseline records a single routing-decision pass, not live multi-run activation rates.
