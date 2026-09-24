# TODO

Tracked work for the `anti-slop-writing` hillclimb loop. Done items stay listed for one cycle so the next contributor sees what changed.

## Blocked — needs a human

- [ ] **Real discourse-layer failure examples.** 3–5 pieces of multi-paragraph prose (~500+ words) that use no banned phrases and read fine at the sentence level but are still slop: over-explained takeaway, flat paragraph escalation (siblings at the same altitude), or single-track structure with no counter-evidence. These cannot be synthesized here without circularity (drafting the rule then writing examples to fit it) or contamination (public long-form may be in training data). See `Lessons_learned.md` → "Doctrine reaches the surface layer." Until these land, the discourse-layer doctrine work in `SKILL.md` stays blocked.
  - Acceptance: each example added to `evals/failures/`, plus `tune` cases in an eval file and at least one `holdout` case in the same vein.

## Done — 2026-09-24

- [x] **Run the pre-registered coined-compound-label re-run** (`evals/results/2026-09-23-coined-label-rerun/`). All 176 slots were filled with audited trials. Three of 179 attempts were excluded and replaced, and nine of 85 judgment files were re-judged under the judge audit. Both gates accepted under both judges: +0.93 on the tune case and +0.92 on the holdout case, with the candidate naming the coinage in 80 of 80 trials against 5 of 80 for the baseline. No guard over-flagged beyond the allowance. The frozen `candidate-v3.patch` is now in `SKILL.md`.

## Done — 2026-05-29

- [x] **Execution runner** (`scripts/run_evals.py`): prepare/grade/join over the eval suites, filtered by split. Orchestration only — the repo is instruction-only, so model calls are done by sub-agents per `docs/judge-protocol.md`.
- [x] **Judge implementation using sub-agents** (`docs/judge-protocol.md`): file-based apply → judge → grade protocol, with the strict judgment-line format the runner consumes.
- [x] **Clean baseline** (`evals/results/2026-05-29-baseline.md` + `evals/results/baseline-2026-05-29/`): current skill scored on every tune and holdout case, recorded as the comparison point future rounds join against.

## Open — buildable without the blocked item

- [ ] **Cross-family judge.** The baseline judges are Claude grading Claude output (same-family, self-preference risk per `Lessons_learned.md`). A non-Claude judge is not available in the current harness. Wire one in when a second model family is reachable.
- [ ] **Fix the `earned-domain-compound` guard sentence.** It says "a crash between the enqueue and the fsync replays from the last checkpoint", which claims recovery for the one window a write-ahead log does not yet cover. In the 2026-09-23 re-run, careful critiques in both arms said so and returned `revise` or `ask-author`, and the case's first assertion ("Returns a keep verdict and does not flag ...") counts that as an over-flag: 5 of 8 baseline and 3 of 8 candidate trials. None of the 16 critiques flagged the standard terms as coined. Either move the crash after the fsync so the sentence earns `keep`, or split the first assertion so it checks only that the terms are not flagged as coined. Re-baseline the guard afterwards; the recorded runs used the current text.
  - Acceptance: a revised sentence or assertion, a note in the case's `split_note` or source field, and one fresh run on both doctrines showing the guard now separates coinage flags from other findings.
- [ ] **`scripts/score_delta.py` prints `ACCEPT` for a significant regression.** Its verdict means "the delta clears the noise floor" in either direction (`ACCEPT (regression clears the noise floor)`), while `runbooks/hillclimb-skill.md` and `AGENTS.md` say to "require ACCEPT". A regressing edit would pass that wording. The 2026-09-23 re-run guards against it in `score_rerun.py`; the shared tool should too, for example with a distinct `REJECT (regression)` verdict and a nonzero exit.
  - Acceptance: a regression returns a non-ACCEPT verdict and exit code, a test covers it, and the runbook wording matches.
- [ ] **Instruction-precedence behaviour on a non-Claude model.** The GPT-6 Astra guide warns that a skill file "may cause the model to pause and block work early" and recommends an explicit precedence line; `SKILL.md` has none. The risk did not reproduce on Claude Sonnet 5 (`evals/results/2026-09-05-astra-compound-labels/outputs/precedence-sonnet.md`: the skill shipped the line when asked and waived the mandatory `Rewrite check` when asked, one trial each), but the warning is about a model not reachable from this harness. Re-probe when a GPT-family or other non-Claude runner is available, and only then decide whether a precedence line earns its words. Shares a blocker with the cross-family judge item above.
  - Acceptance: `probe-precedence.md` re-run on a non-Claude model, result recorded, and either a precedence line added with eval coverage or a note that the skill already complies.
- [ ] **Test the GPT-6 Astra guide items no round has tested.** The coverage map in `evals/results/2026-09-05-astra-compound-labels/README.md` lists them: the stock words "leverage", "importantly", and "genuinely" (which `SKILL.md` itself uses once); the closers "Bottom Line:", "In short:", and "The simplest mental model is:"; the "Question? Answer." rhythm; padding that says what will not change or how results will be grouped; and a positive rule for when a list beats prose.
  - Acceptance: for each item, a failing case showing the current doctrine misses it, or a note that an existing mechanism test already catches it. Borrowed surface rules are often inert (`Lessons_learned.md`, 2026-06-14), so no item earns doctrine without a failing case.
- [ ] **Observed multi-run trigger rates** in Pi, Claude Code, Codex, and OpenCode. The baseline records a single routing-decision pass, not live multi-run activation rates.
