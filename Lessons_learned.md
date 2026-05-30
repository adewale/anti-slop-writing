# Lessons learned

This file records why doctrine changed. Each lesson should point to a concrete failure, the smallest rule that addressed it, and the boundary that prevents overgeneralization.

The per-attempt graveyard of rejected edits lives in `evals/rejected-edits.md`. Use this file for lessons that survived; use that one for the rejects that did not.

## 2026-05-29 — Doctrine reaches the surface layer; the discourse layer is unaddressed

### Failure

[StoryScope, arXiv 2604.03136](https://arxiv.org/abs/2604.03136) reports 93.2% F1 on human-vs-AI fiction detection *after excluding surface stylistic features*. The current `anti-slop-writing` skill operates almost entirely at the surface stylistic level — banned phrases, cadence, "not just X but Y," staccato contrast. There is a discourse-layer of slop — over-explained themes, flat escalation across paragraphs, single-track whole-piece structure — that the doctrine does not reach.

### What changed

Nothing yet in the installable skill. This entry is deliberately a gap marker. The 13 hillclimb-infrastructure changes committed earlier on 2026-05-29 made the loop sound; they did not extend the doctrine surface. The next round of doctrine work should add tune cases at the paragraph-flow and whole-piece-shape layer (over-explained takeaway, flat escalation, missing counter-evidence) and let the new held-out gate decide whether the rules generalize.

### What not to overgeneralize

Most StoryScope findings are fiction-specific — dream sequences, character description, moral ambiguity, temporal complexity. Do not transfer those to non-fiction prose. The in-scope transfers are narrow: over-explained themes, flat escalation, single-track structure. Also: StoryScope studied ~5,000-word stories; most prose this skill edits is shorter, so discourse-level rules may apply weakly until pieces cross some length threshold.

### Eval coverage

- None yet. This is a gap marker, not a closed loop.
- Future doctrine should add tune cases under `evals/evals.json` or a new file for whole-piece-shape diagnostics, plus paired adversarial cases in `evals/adversarial.json` for earned single-track structure (a how-to guide is single-track by design).

## 2026-05-29 — Rewrite-eval grading inherited known judge biases

### Failure

The rewrite-eval suite was graded by a single static rubric and (implicitly) a single judge family. Documented judge biases — self-preference ([Panickssery, Bowman, Feng, NeurIPS 2024](https://arxiv.org/abs/2404.13076)), length ([Dubois et al., Length-Controlled AlpacaEval](https://arxiv.org/abs/2404.04475)), style-over-substance ([Wu & Aji, arXiv 2307.03025](https://arxiv.org/abs/2307.03025)), criteria drift ([Shankar et al., EvalGen, UIST 2024](https://arxiv.org/abs/2404.12272)) — were not specifically guarded against. For an anti-slop skill, longer-sounds-better is the slop pattern the skill targets, so a length-biased judge rewards the exact failure the skill is supposed to catch.

### What changed

The runbook now requires a cross-family judge ensemble, length normalization, orthogonal `graded_dimensions`, and a per-instance `dynamic_rubric` where the eval supplies one. Two holdout meta-evals were added: `judge-self-preference` and `noise-vs-signal-on-small-suite` in `evals/meta-evals.json`. Rewrite cases now carry a `length-control` graded dimension.

### What not to overgeneralize

Cross-family judging dilutes self-preference but does not eliminate it. Length normalization can mask cases where the rewrite genuinely needs to be longer (e.g. when the original conflated two failure modes). The judge layer cannot be "fixed" — it can only be diluted, audited, and spot-checked against humans. Goodhart is an impossibility result, not a warning ([Skalse et al., NeurIPS 2022](https://arxiv.org/abs/2209.13085)): no non-trivial proxy is safe under unbounded optimization, so the held-out split, the score-delta gate, and the cross-family ensemble are what protect the loop, not the judge prompt itself.

### Eval coverage

- `evals/meta-evals.json`: `judge-self-preference`, `noise-vs-signal-on-small-suite` (both holdout).
- `evals/rewrite-evals.json`: `graded_dimensions` with a `length-control` axis on `durable-execution-mechanism` and on `fake-precision-rewrite-finance`.
- `runbooks/hillclimb-skill.md` "Judge protocol" section.

## 2026-05-29 — Basic eval design beats exotic optimization for prose tasks

### Failure

The deep research into SkillOpt, ACE, TextGrad, GEPA, DSPy/MIPRO, Trace/OptoPrime, and SAMMO produced a tempting list of automated optimizers. For a manually-iterated prose skill where the judge layer is the weakest link, adopting any of them would reliably find the grader's gaming behavior. Meanwhile the simplest published interventions — [WritingBench's per-instance dynamic rubrics](https://arxiv.org/pdf/2503.05244) (84% vs 58% human alignment) and length-controlled judging — are cheap and produce the largest measured wins in the corpus.

### What changed

The Tier-S / Tier-A / Tier-B priority order in `docs/hillclimb-improvements.md` put structural basics (held-out split, statistical gating, per-instance rubrics) before exotic machinery. The "Out of scope, deliberately" section names ACE-style curators, TextGrad, SkillOpt, DSPy, and GEPA-as-code as not adopted at this scale.

### What not to overgeneralize

The automated methods are not dismissed. They are appropriate for scripted loops at larger scale, where the judge has been calibrated against human scores on a labeled set and the loss function is verifiable. For this repo, they would amplify judge weakness. The decision is scale-and-domain dependent, not a permanent verdict. Revisit when (a) the loop is scripted, (b) the judge ensemble has been calibrated against humans on a labeled set, and (c) eval-set scale exceeds the few-hundred-cases regime where small-sample CI corrections still dominate.

### Eval coverage

- `docs/hillclimb-improvements.md` "Out of scope, deliberately" section.
- Adoption priority is reflected in the runbook (held-out + statistical gate appear before any exotic-method language).

## 2026-05-29 — Iteration loop needed a held-out gate

### Failure

The hillclimb loop scored every eval case after every edit. Adaptive querying against a fixed set inflates apparent improvement: the writer of a doctrine change sees the score of the next case and steers accordingly. Without a held-out split the loop accepts edits that overfit the tuning cases (Dwork et al., STOC 2015; Blum & Hardt, ICML 2015), and without a statistical gate it accepts single-case deltas that are within seed and judge noise (Miller, arXiv 2411.00640; Bowyer et al., ICML 2025).

### What changed

The repo now has, end to end:

- Per-case `split: "tune" | "holdout"` on every eval file.
- `scripts/score_delta.py` for paired-bootstrap and sign-flip permutation gating; the runbook requires ACCEPT on the holdout split before merge.
- Per-instance `dynamic_rubric` and orthogonal `graded_dimensions` schema on rewrite-eval cases.
- Near-miss `near-neg-` trigger negatives in `evals/trigger-queries.json` to test the false-positive arm.
- Saturation stop condition, Pareto-front carryforward, length budget per round, cross-family judge protocol, length-normalized judging, eval-rot refresh policy — all documented in `runbooks/hillclimb-skill.md`.
- `evals/rejected-edits.md` graveyard so the same failed edit does not get relitigated.
- `docs/hillclimb-improvements.md` with sources for each change.

### What not to overgeneralize

- The split is structural; it only protects against overfit if the rule "never edit doctrine in response to a holdout failure" is actually followed. A holdout failure that drives a doctrine change converts the holdout back into a tune case.
- Statistical gating is a noise filter, not a quality judgment. A change can clear the gate and still be wrong on the merits.
- Cross-family judging dilutes self-preference; it does not eliminate it. Human spot-checks remain the ground truth when judges disagree.

### Eval coverage

- `evals/evals.json`: added holdout cases `fake-precision-unnamed-source`, `stacked-rule-of-three`, `abstract-system-noun-stack`.
- `evals/adversarial.json`: added holdout cases `earned-importance-immediate-mechanism`, `cost-benefit-not-just-earning-the-contrast`, `research-methods-staccato`.
- `evals/rewrite-evals.json`: added holdout cases `fake-precision-rewrite-finance`, `product-tour-rewrite-developer-tools` (both with `dynamic_rubric` + `graded_dimensions`).
- `evals/meta-evals.json`: added holdout cases `noise-vs-signal-on-small-suite`, `judge-self-preference`.
- `evals/trigger-queries.json`: added 6 near-miss negatives and split positives across tune/holdout.
- `scripts/score_delta.py`, `scripts/validate.py` (split + schema enforcement).
- `docs/hillclimb-improvements.md` (single source of truth for the 13 changes).

## 2026-05-25 — Runbooks prevent premature completion

### Failure

An agent can update one artifact, summarize success, and skip the eval, changelog, lesson, or failure corpus update that made the change complete.

### What changed

The repo now has `runbooks/hillclimb-skill.md`, with an output manifest, evaluation criteria, bounded iteration loop, common fixes, and final verification commands.

### What not to overgeneralize

Not every small typo fix needs a runbook. Use it when a change touches doctrine, evals, rubric, or multiple repository artifacts.

### Eval coverage

- `evals/meta-evals.json`: `ceiling-effect-detection`, `metric-artifact-check`
- `runbooks/hillclimb-skill.md`

## 2026-05-25 — Evals can go stale while staying green

### Failure

A suite can pass 100% because it only measures old failure modes. A new model may stop using banned phrases while creating a different kind of slop: fake precision, unnamed sources, or unsupported specificity.

### What changed

The repo now has `evals/meta-evals.json` to check for ceiling effects, metric artifacts, trigger drift, judge drift, and new failure modes.

### What not to overgeneralize

Do not treat every all-pass run as suspicious. Treat it as a prompt to ask whether the suite still distinguishes good output from merely compliant output.

### Eval coverage

- `evals/meta-evals.json`: all cases
- `docs/eval-runbook-notes.md`

## 2026-05-25 — Importance language hides missing mechanism

### Failure

`This underscores the importance of durable execution in modern software systems.`

### What changed

The skill now checks whether importance language is backed by a mechanism. A good rewrite names what durability does: retry a failed step, resume from a checkpoint, keep prior outputs, record a receipt, or enforce idempotency.

### What not to overgeneralize

Do not ban claims of importance when the surrounding prose has already shown the mechanism and the sentence is summarizing a proven point.

### Eval coverage

- `evals/evals.json`: `generic-importance`
- `evals/rewrite-evals.json`: `durable-execution-mechanism`
- `evals/failures/generic-importance.md`

## 2026-05-25 — Contrast can be earned or decorative

### Failure

`The point is not the pelicans. The point is the process.`

### What changed

The skill now classifies short contrast as earned, compressed, or decorative. The rewrite should replace rhythm with relation when the cadence implies a connection the prose has not explained.

### What not to overgeneralize

Do not remove every antithesis. A compressed line can work after the mechanism has been established.

### Eval coverage

- `evals/evals.json`: `decorative-contrast`
- `evals/adversarial.json`: `earned-antithesis`
- `evals/rewrite-evals.json`: `pelican-process-relation`
- `evals/failures/decorative-contrast.md`

## 2026-05-25 — A true conclusion can still be generic

### Failure

`A benchmark is stronger when you can inspect the run that produced it.`

### What changed

The skill now asks conclusions to return to the concrete carrier before stating the transferable claim.

### What not to overgeneralize

A final thesis sentence can work when the piece has no memorable carrier or when the prior sentence already binds the carrier to the claim.

### Eval coverage

- `evals/evals.json`: `weak-conclusion`
- `evals/rewrite-evals.json`: `carrier-bound-ending`
- `evals/failures/weak-conclusion.md`
- `examples/pelican-conclusion-before-after.md`

## 2026-05-25 — Lists need relations, not decoration

### Failure

`The Climb ranks the models. Head-to-Head is a filmstrip viewer. Runbook Diffs compares versions.`

### What changed

The skill now checks whether adjacent product descriptions form a sequence. A hinge should name the relation: resolution, level of detail, dependency, cause, or contrast.

### What not to overgeneralize

Do not reject every list. A list works when each item maps a concrete object to a role and the surrounding prose names the relation.

### Eval coverage

- `evals/evals.json`: `product-tour-flow`
- `evals/adversarial.json`: `specific-bullet-list`
- `evals/rewrite-evals.json`: `product-tour-hinge`
- `evals/failures/product-tour-flow.md`

## 2026-05-25 — Safe essay voice removes actors and actions

### Failure

`In today's rapidly evolving landscape, teams need robust solutions that empower developers to build seamless experiences.`

### What changed

The skill now cuts landscape framing and asks for a named actor, concrete action, and observable result.

### What not to overgeneralize

Some high-risk words are valid in technical contexts. `Robust` is acceptable when the sentence immediately names the failure mode and mechanism.

### Eval coverage

- `evals/evals.json`: `safe-essay-voice`
- `evals/adversarial.json`: `robust-engineering-context`
- `evals/rewrite-evals.json`: `safe-essay-cut-or-concretize`
- `evals/failures/safe-essay-voice.md`
