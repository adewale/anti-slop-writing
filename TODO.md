# TODO

Tracked work for the `anti-slop-writing` hillclimb loop. Done items stay listed for one cycle so the next contributor sees what changed.

## Blocked — needs a human

- [ ] **Real discourse-layer failure examples.** 3–5 pieces of multi-paragraph prose (~500+ words) that use no banned phrases and read fine at the sentence level but are still slop: over-explained takeaway, flat paragraph escalation (siblings at the same altitude), or single-track structure with no counter-evidence. These cannot be synthesized here without circularity (drafting the rule then writing examples to fit it) or contamination (public long-form may be in training data). See `Lessons_learned.md` → "Doctrine reaches the surface layer." Until these land, the discourse-layer doctrine work in `SKILL.md` stays blocked.
  - Acceptance: each example added to `evals/failures/`, plus `tune` cases in an eval file and at least one `holdout` case in the same vein.

## Done — 2026-05-29

- [x] **Execution runner** (`scripts/run_evals.py`): prepare/grade/join over the eval suites, filtered by split. Orchestration only — the repo is instruction-only, so model calls are done by sub-agents per `docs/judge-protocol.md`.
- [x] **Judge implementation using sub-agents** (`docs/judge-protocol.md`): file-based apply → judge → grade protocol, with the strict judgment-line format the runner consumes.
- [x] **Clean baseline** (`evals/results/2026-05-29-baseline.md` + `evals/results/baseline-2026-05-29/`): current skill scored on every tune and holdout case, recorded as the comparison point future rounds join against.

## Done — 2026-08-29

- [x] **Deterministic slop-lint oracle** (`evals/oracles/slop_lint.py` + `run_evals.py lint`): 22 detectors ported from simonw/tools' llm-cliche-highlighter (Apache-2.0), forbid-shaped `deterministic_checks` on eval cases, self-tests wired into `scripts/validate.py`. See `docs/deterministic-graders.md`.
- [x] **New-register doctrine coverage** (significance compression, therapy voice, performative honesty, stage management, dev-blog boilerplate, structural cadence) with 13 new eval cases across the four suites, a failure record, and a card.
- [x] **Full scored run over the 2026-08-29 additions** (`evals/results/2026-08-29-scored-run.md`): pre-registered A/B (doctrine at 53370ff vs post-mining), blinded Opus+Haiku panel, deterministic checks merged. All four `score_delta.py` gates REJECT at N=13/5 (every mean positive; TOST equivalence also not shown) — recorded as coverage + baseline, not measured improvement, per the pre-registration.
- [x] **Shared Skill Eval Harness bridge** (`evals/oracles/slop_lint_oracle.py` + two shared-benchmark cases); manifest revalidated green against harness main.

## Open — buildable without the blocked item

- [ ] **Cross-family judge.** The baseline judges are Claude grading Claude output (same-family, self-preference risk per `Lessons_learned.md`). A non-Claude judge is not available in the current harness. Wire one in when a second model family is reachable. Partially mitigated 2026-08-29: `deterministic_checks` now grade the mechanical assertions with no judge at all (`docs/deterministic-graders.md`), shrinking the surface exposed to same-family bias; the earned-vs-decorative and mechanism-quality assertions still need the cross-family panel.
- [ ] **Power the next scored round.** The 2026-08-29 scored run's effect size (~+0.10 mean delta, consistent across two judges) cannot clear a 95% paired gate at N=13; before re-attempting, add cases and/or repeat generations per case, and harden the 8 ceiling cases named in `2026-08-29-scored-run/saturation-y.txt` (all four adversarial guards saturate).
- [ ] **Fix the mis-specified tune assertion.** `evals/evals.json` → `structural-cadence-run` assertion 3 demands a "verified finding" its source excerpt cannot supply without invention; reword to verified-or-explicitly-requested (the doctrine's ask-author form). Exposed by the scored run (Opus failed arm B for honestly declining to invent).
- [ ] **New tune case from the arm-B holdout miss.** Under the new doctrine, the `holdout-devblog-boilerplate` rewrite still reused "fits in your head" (deterministic FAIL, both judges 0.800). Per the runbook, the holdout stays untouched; write the reuse pattern up as a fresh tune case next round.
- [ ] **Real-world corpus for the new-register families.** The new eval inputs are synthesized from the highlighter's pattern families. Capture 3-5 real passages (launch posts, postmortems, README intros) that exhibit the register, per the discipline in the blocked discourse-layer item.
- [ ] **Observed multi-run trigger rates** in Pi, Claude Code, Codex, and OpenCode. The baseline records a single routing-decision pass, not live multi-run activation rates.
