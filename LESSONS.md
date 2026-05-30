# Lessons learned

This file records why doctrine changed. Each lesson should point to a concrete failure, the smallest rule that addressed it, and the boundary that prevents overgeneralization.

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

## 2026-05-27 — Copula displacement hides concrete verbs

### Failure

`The dashboard serves as the central hub for user activity and stands as a testament to the platform's capabilities.`

### What changed

The skill now flags `serves as`, `stands as`, `features`, `marks`, and `represents` as copula displacement when they replace plain `is/are` without doing concrete work. The rewrite should use `is` or a specific action verb (`shows`, `lists`, `routes`, `surfaces`).

### What not to overgeneralize

Keep the displaced verb when it does concrete enumeration, definition, or location work. `The retry policy serves three distinct failure modes: ...` is earned; `serves` introduces a real list.

### Eval coverage

- `evals/evals.json`: `copula-displacement`
- `evals/adversarial.json`: `serves-as-enumeration`
- `evals/rewrite-evals.json`: `copula-displacement-to-is`

## 2026-05-27 — Hedged symmetry refuses to commit

### Failure

`Whether you're a beginner or an expert, our framework scales to your needs. While simplicity matters, power is also important.`

### What changed

The skill now flags `Whether you're X or Y` and `While X, Y is also important` as hedged symmetry that addresses every possible reader and every possible value at once. The rewrite should pick a specific reader and a concrete tradeoff.

### What not to overgeneralize

Keep the structure when it names a real branching condition with distinct downstream behavior. `Whether the worker crashes before or after the receipt is written determines whether recovery retries or marks complete` is earned: the two branches trigger different recovery paths.

### Eval coverage

- `evals/evals.json`: `hedged-symmetry`
- `evals/adversarial.json`: `branching-condition-symmetry`
- `evals/rewrite-evals.json`: `hedged-symmetry-commit`
- `evals/trigger-queries.json`: `pos-hedged-symmetry`

## 2026-05-27 — Outline conclusions are templates, not closings

### Failure

`Despite ongoing challenges, the team continues to thrive in an evolving landscape. Looking ahead, the platform will play an increasingly pivotal role in the AI ecosystem.`

### What changed

The conclusion test now explicitly rejects two templates: `Despite challenges, X continues to thrive` and `Looking ahead, X will play an increasingly pivotal role`. Neither names a specific challenge, a specific next move, or a concrete carrier.

### What not to overgeneralize

Conclusions about challenges or future direction can still work when they cite a specific challenge from the body or a specific next step. The template is the failure, not the topic.

### Eval coverage

- `evals/evals.json`: `outline-conclusion-template`
- `evals/rewrite-evals.json`: `outline-conclusion-carrier-bound`

## 2026-05-27 — Em-dashes are not slop; clusters are

### Failure

`The system is fast — really fast — and reliable — at scale — with a clean API — that just works.`

### What changed

The skill now distinguishes decorative em-dash clusters (cadence-for-emphasis) from earned em-dashes that bracket a parenthetical or appositive. The rewrite reduces the count and keeps only earned dashes.

### What not to overgeneralize

Em-dashes are not banned. Professional human writers use them, and a single dash bracketing an inline definition (`The orphaned stream — the one where the original readable was lost but the chunks survived in SQLite — can still be finalized`) is earned. The cluster is the failure.

### Eval coverage

- `evals/evals.json`: `em-dash-cluster`
- `evals/adversarial.json`: `em-dash-earned`
- `evals/trigger-queries.json`: `neg-em-dash-mechanical`

## 2026-05-27 — High-risk word lists are time-dated

### Failure

External reporting showed `delve` usage in LLM outputs dropped off sharply during 2025 after a 2023-2024 peak, while new patterns such as copula displacement and hedged symmetry became more visible. A static word list maintained by taste becomes a stale detector.

### What changed

The doctrine reference and SKILL.md now note that the high-risk word and phrase lists are time-dated detectors. Entries should be re-profiled against a current human-vs-LLM corpus before being added or removed. The Antislop research finding that some slop patterns appear over 1,000 times more frequently in LLM output than in human text is the reference frequency-based test.

### What not to overgeneralize

Do not strip `delve` or other older entries blindly. Slower-drifting models and older outputs still produce them. The lesson is about maintenance method (corpus profiling), not list deletion.

### Eval coverage

- `evals/meta-evals.json`: `word-list-drift`

## 2026-05-27 — The skill author injected fake precision (caught on review)

### Failure

While adding the word-list-drift material, the change introduced an unsourced statistic: that `delve` usage "dropped roughly 80%" in 2025. The public reporting describes the decline only qualitatively ("dropped off sharply"); the 80% figure was invented. This is the exact unsupported-specificity / fake-precision failure that `regime-shift-new-slop` warns about — reproduced inside the anti-slop doctrine itself, by the person writing it.

### What changed

Replaced the invented percentage with the qualitative claim the source actually supports, in the doctrine reference, the `word-list-drift` meta-eval prompt, and this file. Added an explicit instruction in the doctrine reference not to manufacture a drop percentage for `delve`.

### What not to overgeneralize

Sourced quantitative claims are good and wanted: the Antislop 1,000x figure stays because the paper states it. The rule is provenance, not number-avoidance. Cite the figure the source gives; do not invent precision the source lacks. A clean-looking statistic is the most persuasive form of slop, which is why it has to clear the same evidence bar as any other claim.

### Eval coverage

- `evals/meta-evals.json`: `regime-shift-new-slop` (the pre-existing guard this violation should have tripped), `word-list-drift`
