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
- [ ] **Run the pre-registered coined-compound-label re-run.** Everything is ready in `evals/results/2026-09-23-coined-label-rerun/`: the frozen candidate (`candidate-v3.patch`), fresh holdout cases, a deterministic manifest, the apply protocol, the exclusion rule, and the decision rule. The design is 40 trials per arm on each discriminating case. It passes both gates about three times in four if the rule lifts the pass rate by 0.35, and about one time in four if the lift is 0.25. It costs about 176 apply agents and 76 judge agents. Detecting a 0.25 lift reliably would take about 80 per arm; if that is chosen, amend the pre-registration before any trial runs.
  - Acceptance: every slot filled with an audited trial, both gates scored under the primary judge, and the pre-registered decision applied. The result is either the rule in `SKILL.md` or a tested entry in `evals/rejected-edits.md`.
- [ ] **Instruction-precedence behaviour on a non-Claude model.** The GPT-6 Astra guide warns that a skill file "may cause the model to pause and block work early" and recommends an explicit precedence line; `SKILL.md` has none. The risk did not reproduce on Claude Sonnet 5 (`evals/results/2026-09-05-astra-compound-labels/outputs/precedence-sonnet.md`: the skill shipped the line when asked and waived the mandatory `Rewrite check` when asked, one trial each), but the warning is about a model not reachable from this harness. Re-probe when a GPT-family or other non-Claude runner is available, and only then decide whether a precedence line earns its words. Shares a blocker with the cross-family judge item above.
  - Acceptance: `probe-precedence.md` re-run on a non-Claude model, result recorded, and either a precedence line added with eval coverage or a note that the skill already complies.
- [ ] **Test the GPT-6 Astra guide items no round has tested.** The coverage map in `evals/results/2026-09-05-astra-compound-labels/README.md` lists them: the stock words "leverage", "importantly", and "genuinely" (which `SKILL.md` itself uses once); the closers "Bottom Line:", "In short:", and "The simplest mental model is:"; the "Question? Answer." rhythm; padding that says what will not change or how results will be grouped; and a positive rule for when a list beats prose.
  - Acceptance: for each item, a failing case showing the current doctrine misses it, or a note that an existing mechanism test already catches it. Borrowed surface rules are often inert (`Lessons_learned.md`, 2026-06-14), so no item earns doctrine without a failing case.
- [ ] **Observed multi-run trigger rates** in Pi, Claude Code, Codex, and OpenCode. The baseline records a single routing-decision pass, not live multi-run activation rates.
