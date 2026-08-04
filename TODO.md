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

- [ ] **Decide the dialogic-scope question with an A/B.** Seven cases landed on 2026-08-04 (see `Lessons_learned.md` → "The earned-contrast test is scoped to the document") without a doctrine change, because the last two imports of an outside idea both measured inert. Run the tune cases against the current `SKILL.md` first: if the doctrine already flags a self-planted strawman and repairs a hollow modifier by deletion, the cases are regression coverage and the question is closed. If it grades the strawman as earned antithesis, A/B the candidate edit — extend the staccato contrast test to ask *who introduced the opposing side*, and treat a side the writer supplied themselves as unearned regardless of local evidence.
  - Acceptance: `scripts/run_evals.py` prepare/grade/join over the seven cases per `docs/judge-protocol.md`; `scripts/saturation_index.py` before trusting any zero delta; `scripts/score_delta.py --holdout-only` ACCEPT before any `SKILL.md` edit, or an entry in `evals/rejected-edits.md` if it comes back null.
  - Watch the length-control dimension on `hollow-modifier-delete-not-expand`: the default editing pass replaces abstraction with mechanism, which adds words, and the correct repair here is deletion.


- [ ] **Cross-family judge.** The baseline judges are Claude grading Claude output (same-family, self-preference risk per `Lessons_learned.md`). A non-Claude judge is not available in the current harness. Wire one in when a second model family is reachable.
- [ ] **Observed multi-run trigger rates** in Pi, Claude Code, Codex, and OpenCode. The baseline records a single routing-decision pass, not live multi-run activation rates.
