# Lessons learned

This file records why doctrine changed. Each lesson should point to a concrete failure, the smallest rule that addressed it, and the boundary that prevents overgeneralization.

The per-attempt graveyard of rejected edits lives in `evals/rejected-edits.md`. Use this file for lessons that survived; use that one for the rejects that did not.

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
