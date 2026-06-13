# Changelog

All notable changes to this project are recorded here. This changelog tracks doctrine, eval coverage, compatibility, and docs because a skill can change behavior without changing code.

## [Unreleased]

### Doctrine

- Added a `Parataxis and hypotaxis` teaching section to `references/anti-slop-writing-doctrine.md` and a flow-by-relation diagnosis bullet. This names the concept and consolidates existing guidance (the staccato "keep or use once" rule and the symmetrical-structure tell); it is a reference-only addition and does not change gated `SKILL.md` behavior. A stronger `SKILL.md` rule was tried and reverted (see Evals / `evals/rejected-edits.md`).
- Added detectors for copula displacement, hedged symmetry, outline-shaped conclusions, and decorative em-dash clusters. The rules include earned-use boundaries: `serves` can introduce a concrete enumeration, `Whether X or Y` can name a real branching condition, and em-dash pairs can bracket an inline definition.
- Added a time-dated-word-list note: high-risk word lists should be re-profiled against current human-vs-LLM corpora; do not invent precise drift percentages when the source only supports a qualitative claim.
- Added two procedural detectors to `skills/anti-slop-writing/SKILL.md`: the **emphasis-source test** (write the flattened version of the line in the critique; judge whether the residual claim still names actor/mechanism/limit) and the **syntax-relation test** (restate the implied relation with a connective; if no connective fits without invention, the syntax was empty). Sourced from Ruth Starkman, "Model Style Is So Cringe." Retained on qualitative behavioral evidence: under the blinded harness the procedural wording reliably produces the flatten artifact in critique text while the labeled wording does not. The +1 score delta from the worked Round 5 does not pass `scripts/score_delta.py` at N=5 (CI overlaps zero, sign-flip p=1.0); recorded honestly in `evals/results/2026-05-27-emphasis-source-experiment.md` and the gate output in `evals/results/2026-05-28-emphasis-source-procedural/`.

### Evals

- Added a real-world test case captured from an X thread: `evals/fixtures/tweet-taste-as-model/input.md` plus `evals/rewrite-evals.json` → `tweet-taste-as-model` (tune). Scored original vs naive (no-skill) rewrite vs skill rewrite in `evals/results/2026-06-13-tweet-taste-as-model/`, which also records the sub-agent model/version (claude-opus-4-8) in a `run-metadata.json` provenance block — the first run to capture model identity, not just the skill commit.
- Added a new eval kind, the **reference-anchor**: a `holdout` case that pins a fixed, human-reviewable floor for one high-value rewrite and uses it as a don't-regress gate for future models and skill versions — a candidate must score at least the reference score, and scoring below it is a regression. First instance: `evals/rewrite-evals.json` → `tweet-best-rewrite-anchor`, with the original and the best known rewrite stored under `evals/fixtures/tweet-taste-as-model/` (`best-rewrite.md`, `HUMAN-REVIEW.md`), the reference scorecard (1.0/1.0, the floor) under `evals/results/2026-06-13-tweet-best-anchor/`, the protocol in `docs/reference-anchor-tests.md`, and enforcement in `scripts/validate.py` (referenced artifacts must exist; reference scores must be in [0,1]).
- Added six parataxis eval cases: `evals/rewrite-evals.json` (tune) → `parataxis-pervasive-closers`, `parataxis-unstated-relation`, `parataxis-coordination-hides-cause`, `parataxis-chained-and`, `parataxis-earned-but-pervasive`; `evals/adversarial.json` (tune, earned guards) → `earned-parataxis-sequence`, `earned-parataxis-evidenced-contrast`. Plus `evals/failures/tweet-parataxis-density.md`.
- Ran a three-round parataxis hillclimb (`evals/results/2026-06-13-parataxis-hillclimb/`) with a rate study on the pivotal case and a multi-model A/B. A drafted `Parataxis density` / `Parataxis repair` rule for `SKILL.md` did not clear the gate (round 1 N=6 delta -0.028, CI [-0.25,+0.17]; round 2 discriminating case before 0.833 vs after 0.917, within noise) because the pre-edit doctrine already catches document-level parataxis via the staccato "keep or use once" rule and the symmetrical-structure tell. Round 3 re-ran the A/B across every available model (Opus 4.8, Sonnet 4.6, Haiku 4.5; Fable 5 unavailable): all models on both doctrines caught the document-level over-reliance, with one noise-prone Haiku-only gain on the discriminator (0.75->1.00). Reverted in `SKILL.md`; logged in `evals/rejected-edits.md`.
- Added harder branch-specific cases and graded dimensions so merged doctrine branches can be compared above the saturated binary baseline: flatten-artifact, mechanism-specificity, ladder-flattening, non-invention, rewrite-check-integrity, copula verb-concreteness, hedged-symmetry commitment, dash calibration, and multi-detector coverage axes.
- Added fresh holdout cases that were not part of the original branch tuning loops: `holdout-borrowed-emphasis-release-safety`, `holdout-copula-hedged-outline-combo`, `holdout-earned-branching-dash-copula`, `holdout-ask-author-ai-tooling`, and `pos-outline-conclusion-template`.
- Added score-gist detector coverage: `copula-displacement`, `hedged-symmetry`, `outline-conclusion-template`, `em-dash-cluster`, `serves-as-enumeration`, `branching-condition-symmetry`, `em-dash-earned`, `copula-displacement-to-is`, `hedged-symmetry-commit`, `outline-conclusion-carrier-bound`, `word-list-drift`, `neg-em-dash-mechanical`, and `pos-hedged-symmetry`.
- Added five eval cases for the emphasis-source diagnostic, all with proper splits: `evals/evals.json` → `borrowed-emphasis` (tune), `paragraph-scale-borrowed-emphasis` (tune); `evals/rewrite-evals.json` → `emphasis-source-flatten` (tune); `evals/adversarial.json` → `earned-emphasis-from-idea` (holdout), `earned-paragraph-escalation` (holdout). Plus `evals/failures/borrowed-emphasis.md` and `examples/cards/borrowed-emphasis.md`.
- Added `evals/blinded-eval-harness.md`: doctrine A/B comparison with anonymized labels and a rate-study procedure for behaviors that vary run-to-run. Extends the standard `docs/judge-protocol.md` apply-judge separation with the additional discipline a fair doctrine comparison requires.
- Added `evals/rejected-edits.md` entry: paragraph-scale ladder guidance on the emphasis-source test was tried and reverted as inert (rate study: 3/3 vs 3/3 on both decisive prompts).
- Ran the held-out regression check under the new protocol: this branch's doctrine scores 10/10 on the upstream's holdout cases, matching the 2026-05-29 baseline case-for-case. Per-case delta is exactly 0.0 on every joined case. The procedural emphasis-source change does not regress any upstream holdout case. Full run in `evals/results/2026-05-30-holdout-regression-check/` with outputs, judgments, scores, joined delta, and captured gate output.
- Added `evals/results/2026-05-31-stat-proof/`, a 42-case fresh holdout proof run with blind A/B pair judging and 60 graded dimensions. The pre-integration snapshot vs current `main` comparison clears the statistical gate: binary delta +0.0714, 95% CI [+0.0317, +0.1190], p=0.0074; graded delta +0.0669, 95% CI [+0.0245, +0.1167], p=0.0074.

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
- Updated `scripts/validate.py` to enforce per-case split, minimum holdout counts per suite, the `near-neg-` near-miss requirement on trigger queries, and the root `skills.sh.json` display config.
- Added `evals/rejected-edits.md` graveyard so previously rejected edits are not relitigated.
- Added `docs/hillclimb-improvements.md` with sources for all thirteen changes (Dwork, Blum & Hardt, Miller, Bowyer, WritingBench, FLASK, BFCL, Panickssery, Dubois, Hamel/Shankar, GEPA, SkillOpt, Decagon, Schaeffer).

### Evals

- Added adversarial evals to prevent over-flagging earned contrast, technical use of `robust`, quoted bad phrases, useful lists, short direct answers, exact `not just` distinctions, controlled-variable staccato, concrete tables, ordered three-step sequences, direct warnings, source-backed `highlights`, and imperative runbook steps.
- Added adversarial evals from a generalization test on a Paul Graham essay: `earned-antithesis-synthesis-pg`, `cataphoric-label-defined-in-paragraph`, and `escalating-magnitude-triple` lock in false-positive resistance against dense earned human rhetoric the doctrine was not tuned on.
- Added meta-evals `single-source-overfitting` (repeated tuning against one document does not prove generalization) and `earned-rhetoric-false-positive-rate` (how to read a near-zero flag rate on clean prose honestly).
- Added rewrite evals that score concrete output quality, not just critique labels.
- Added rewrite evals covering rewrites that reuse the flagged cadence under different punctuation (`rewrite-reuses-flagged-pattern`) and rewrites that should ask the author or cut instead of inventing a specific (`rewrite-asks-or-cuts-when-fact-missing`).
- Added meta-evals for ceiling effects, metric artifacts, capability drift, trigger drift, and judge drift.
- Added a curated failure corpus under `evals/failures/`, including `rewrite-reuses-flagged-pattern.md`.
- Added before/after cards under `examples/cards/` for fast inspection of core patterns.

### Doctrine

- Added a final self-check and one bounded judge-refine pass for high-stakes prose.
- Extended the Final self-check to require running the same detectors on the rewrite and to require asking or cutting when a rewrite would need a fact not present in the source.
- Added `ask-author` as a verdict in the Critique output format, with a triggering rule in the Default editing pass: do not invent a tool, person, count, or timing to fill the Concrete rewrite slot when the source paragraph does not supply it.
- Tightened the antithesis classification rule: read the prior sentence in the paragraph before grading contrast as compressed or decorative. Anchored on a real failure from joe.dev/posts/thinking-out-loud where the skill graded earned contrast as decorative because it scored the sentence alone.
- Added a mandatory `Rewrite check` field to the Critique output format so the same detectors run against every Concrete rewrite (including ask-author fallbacks) inside the per-item loop, not at end-of-document. Added a "Rewrites must pass the same detectors as the source" section to `references/rewrite-patterns.md` with real before/after pairs from the joe.dev review.
- Clarified the Staccato contrast test in `SKILL.md` with the both-sides test: an antithesis is earned only when both sides of the contrast are evidenced in the prior prose, not when only the topic of the contrast was mentioned. Carries the joe.dev pair as the canonical compressed example. Corrected the eval assertion and failure-file claims that previously framed the model's compressed verdict on `That's not incidental. It's the design.` as a misclassification.

### Docs

- Added the skills.sh badge, canonical Skills CLI install command, telemetry opt-out note, and root `skills.sh.json` display grouping.
- Added `Lessons_learned.md` (originally `LESSONS.md`) to record what each failure taught and what not to overgeneralize.
- Added `runbooks/hillclimb-skill.md` to keep multi-artifact skill improvements from stopping early; rewritten to include the held-out gate, statistical gating, cross-family judge protocol, length normalization, saturation stop, Pareto-front carryforward, length budget, and eval-rot refresh policy.
- Added `docs/eval-runbook-notes.md` to record the external runbook and eval-drift ideas that shaped this iteration.
- Added `docs/hillclimb-improvements.md` as the single source of truth for the thirteen hillclimb-infrastructure changes and their citations.
- Added `docs/branch-mining-2026-05-30.md` to document which remote-branch artifacts were merged, manually ported, or deliberately left behind as stale.

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
