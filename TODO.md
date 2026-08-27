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

- [ ] **Gate the cataphoric-teaser rule.** The detector, doctrine section, and five eval cases are merged but the A/B round in `runbooks/hillclimb-skill.md` has not been run: pre-edit `SKILL.md` snapshot vs current, apply/judge separated per `docs/judge-protocol.md`, over the six catch cases and the five guard/precision cases. SKILL.md grew +184 words this round against a +200 cap, so the next round owes a consolidation pass before any new rule lands (`runbooks/hillclimb-skill.md` item 9). Pre-register SESOI 0.05. Require ACCEPT from `python3 scripts/score_delta.py <results.jsonl> --holdout-only`; on a zero delta run `--sesoi 0.05` and `scripts/saturation_index.py` before reading it as equivalence. If it rejects, revert the `SKILL.md` rule, keep the reference section and the six cases as regression coverage, and log it in `evals/rejected-edits.md` — the disposition the parataxis round took.
  - Motivation and the recorded pre-edit miss: `evals/failures/cataphoric-teaser.md`.
  - Two sub-forms are named but uncovered: **delayed discharge** (Sanderson's "progress" failure — the promise pays off several paragraphs later) and an **undischarged discourse-deixis** catch case ("Read on to find out what went wrong"); `earned-discourse-deixis-roadmap` guards only the earned side. See `docs/cataphoric-teaser-prior-art.md` → "What is not yet covered".

- [ ] **Cross-family judge.** The baseline judges are Claude grading Claude output (same-family, self-preference risk per `Lessons_learned.md`). A non-Claude judge is not available in the current harness. Wire one in when a second model family is reachable.
- [ ] **Observed multi-run trigger rates** in Pi, Claude Code, Codex, and OpenCode. The baseline records a single routing-decision pass, not live multi-run activation rates.
