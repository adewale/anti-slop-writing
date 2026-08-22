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

- [ ] **Rate study: does the doctrine steer weaker models to repair by deletion?** The one miss to survive the 2026-08-04 round. Haiku repaired `The key issue is deciding who owns the rollback` as `Deciding who owns the rollback is the remaining blocker`, substituting an adjective into the slot `key` vacated; a three-judge panel was unanimous that this fails. Opus and Sonnet both repaired cleanly.
  - This is one observation, which is exactly what `Lessons_learned.md` → "A variance gap is not a doctrine gap" says not to write doctrine for. Run the rate study first: N samples of `hollow-modifier-false-implicature` on Haiku, behavioral classification (substituted / deleted), compare rates. Only if substitution reproduces is there a gap.
  - If it reproduces, the candidate is narrower than the rejected H1 block: not a word list, but a line in the repair guidance saying a hollow modifier is repaired by deleting the slot, not refilling it. Gate it normally.
  - Do not revive the rejected H1 word list on the strength of this. It is in `evals/rejected-edits.md` for a reason: detection was already at ceiling on all three models.


- [ ] **Cross-family judge.** The baseline judges are Claude grading Claude output (same-family, self-preference risk per `Lessons_learned.md`). A non-Claude judge is not available in the current harness. Wire one in when a second model family is reachable.
- [ ] **Observed multi-run trigger rates** in Pi, Claude Code, Codex, and OpenCode. The baseline records a single routing-decision pass, not live multi-run activation rates.
