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
## 2026-05-26 — Rewrites must pass the same detectors as the source

### Failure

A critique correctly flagged `That's not incidental. It's the design.` as
compressed antithesis hiding the mechanism. The proposed rewrite,
`Portability isn't a feature bolted on — it's where the protocol starts.`,
reproduced the same contrast shape with an em-dash. In the same review,
two adjacent rewrites invented specifics the source did not contain
(named projects that were not in evidence; before/after timing numbers
the author had not supplied).

### What changed

The Final self-check now asks whether the rewrite reuses the cadence it
just flagged under different punctuation, and whether any rewrite that
needs a missing fact asked the author or recommended cutting instead of
inventing a confident-sounding specific.

### What not to overgeneralize

Do not refuse to rewrite whenever a sentence is short or contains a
contrast. Earned antithesis still works after the mechanism is
established. The rule applies when the rewrite is the place the
mechanism should appear and the cadence is doing the work instead.

### Eval coverage

- `evals/rewrite-evals.json`: `rewrite-reuses-flagged-pattern`, `rewrite-asks-or-cuts-when-fact-missing`
- `evals/failures/rewrite-reuses-flagged-pattern.md`

### Follow-up

An A/B run on 2026-05-27 scored 7/8 with-skill vs 7/8 without-skill: the
self-check question did not change observed behavior. The 2026-05-28
revision below is the corrected iteration, anchored on the real source
material (joe.dev/posts/thinking-out-loud) rather than a synthetic case.

## 2026-05-28 — Critique format must permit ask-author, or it invites invention

### Failure

The skill was run against Joe Beda's real post
[Thinking out loud, with a URL I own](https://joe.dev/posts/thinking-out-loud/)
using the SKILL.md doctrine and the Critique output format. The critique
contained roughly ten invented specifics in its rewrites: a tool name
the post never used (`Claude Code turned the cover-image generator from
a someday-item into an afternoon` — the source paragraph names Node.js
and Satori but no tool); fabricated events at a conference the model
did not attend (`PDS for fifty friends, a labeler experiment for
academic citations, a feed generator written over a weekend`); invented
timing (`Two years ago`, `a working day`, `cost an hour`); and invented
infrastructure (`Apache process`, `HTML into a directory`). The
rewrites also reused the very cadence the items flagged: `Portability
is the design, not a future feature` replaced `That's not incidental.
It's the design.` — same `X, not Y` shape, different words.

### Why the previous lesson did not fix it

The previous self-check question lives at the end of the editing pass.
The model writes the critique linearly, item by item, and never circles
back. More important: the `Concrete rewrite` slot in the format is
required. When the only honest revision needs a fact the source does
not supply, the format gives the model no syntactically valid way to
say "I would need to ask," so it invents instead.

### What changed

The Critique output format gained `ask-author` as a verdict. The skill
now says: when the line could be improved but the improvement needs a
tool name, person, count, timing claim, or named mechanism that is not
in the source paragraph, the verdict is `ask-author` and the
`Concrete rewrite` slot names what to ask, with a fallback (cut, or
keep and let the next sentences carry the work). Default editing pass
step 7 was extended in parallel: replace vague actors with named
sources, named uncertainty, or an `ask-author` note — do not invent a
name to fill a slot. The classification rule for antithesis was also
tightened to require reading the prior sentence; the joe.dev case
showed the staccato-contrast classifier grading earned contrast as
decorative when it scored the sentence alone.

### What not to overgeneralize

`ask-author` is not a license to refuse rewrites whenever something is
mildly underspecified. Use it only when the missing fact is the
revision (a specific tool, a specific count, a specific event) and the
source paragraph does not supply it. If the paragraph already supplies
the mechanism — as it does for `That's not incidental. It's the design.`
— the verdict is usually `keep`, not `ask-author`.

### Eval coverage

- `evals/rewrite-evals.json`: `rewrite-reuses-flagged-pattern` (rewritten with real joe.dev paragraph context), `rewrite-asks-or-cuts-when-fact-missing` (rewritten with real joe.dev paragraph context)
- `evals/failures/rewrite-reuses-flagged-pattern.md` (rewritten to capture the real before/after from the joe.dev critique)
- `evals/results/2026-05-28-joe-beda-before.md` and `2026-05-28-joe-beda-after.md`

## 2026-05-28 — Rewrites must pass the same detectors as the source, inside the same loop

### Failure

The ask-author iteration eliminated major inventions at the verdict
level but the rewrites themselves still contained slop the doctrine
bans. On the same joe.dev post: a rule-of-three with three invented
list members (`Google Reader, Posterous, Svbtle`); a rule-of-three list
that fabricated a standard.site schema enumeration; an em-dash
rule-of-three closer ending on `That was the point.` — a stand-in for
the banned `In conclusion / Overall / Ultimately`; and an `ask-author`
fallback that itself invented topic pairs (`portability and moderation
tooling, not growth loops or ad inventory`) and used X-not-Y cadence.
The model correctly used `ask-author` at the verdict level, then
ignored the same rule when writing the fallback.

### Why the previous lesson did not fix it

The previous self-check questions live at the end of `SKILL.md`. The
model writes the per-item critique linearly and never circles back to
apply the Final self-check. Without a per-item slot for the rewrite
self-grade, the slop check does not fire on the rewrite — even when
the same model just flagged the same pattern on the source one item
earlier.

### What changed

The Critique output format now includes a mandatory `Rewrite check`
field. Whenever a `Concrete rewrite` is produced (including a fallback
inside an `ask-author` block), the model must state whether the
rewrite contains rule-of-three, X-not-Y, em-dash antithesis, banned
avoid-by-default phrases, prestige adjectives, decorative closure, or
invented facts. If it does, the rewrite is itself a `revise` and the
model either rewrites again or escalates to `ask-author`. The new
field sits inside the per-item loop, so the check fires when the
rewrite is fresh rather than at end-of-document. A new "Rewrites must
pass the same detectors as the source" section in
`references/rewrite-patterns.md` carries the real joe.dev before/after
pairs as worked examples.

### Boundary

`passes self-detectors` is a real allowed outcome. The check is not a
demand that every rewrite avoid every short cadence — earned
compression, named-tool lists, and short declarative closers all
remain legitimate moves. The check is a demand that the model
distinguish them honestly from their decorative versions.

### Eval coverage

- `evals/rewrite-evals.json`: `rewrite-reuses-flagged-pattern`, `rewrite-asks-or-cuts-when-fact-missing` (both strengthened with rewrite-self-check assertions), `rewrite-passes-own-slop-detectors` (new case using the joe.dev ending paragraph, where the previous iteration's `That was the point.` closure appeared)
- `evals/results/2026-05-28-rewrite-check-before.md` and `2026-05-28-rewrite-check-after.md`
- `skills/anti-slop-writing/references/rewrite-patterns.md` ("Rewrites must pass the same detectors as the source" section)

### What this iteration did not fix (correction below)

The original draft of this section claimed the staccato classifier
was misgrading `That's not incidental. It's the design.` across three
iterations. See the next lesson for the correction.

## 2026-05-28 — When a model keeps "failing" the same way, suspect the doctrine

### Failure

Across three iterations on joe.dev/posts/thinking-out-loud, the
critique kept grading `That's not incidental. It's the design.` as
compressed or decorative antithesis, while the contemporaneous
result notes kept calling that a misclassification. The notes claimed
the contrast should be earned because the prior sentence supplies
movability.

### What was actually wrong

The doctrine, not the model. The original Staccato contrast test
definition (`Earned antithesis: the contrast names a real distinction
already evidenced`) was ambiguous between two readings:

(a) Earned = the topic of the contrast was evidenced (movability was
mentioned).
(b) Earned = both sides of the contrast were evidenced (both
movability and intentionality were shown).

Reading (a) makes the joe.dev line earned. Reading (b) makes it
compressed, because the prior sentence evidences movability but not
intentionality — the `by design vs incidental` distinction is a new
claim added on cadence alone. The model applied reading (b)
consistently and correctly across three iterations, including on the
adjacent line `That's what I want. My words, at a URL I own.` (kept
as earned because both sides — the platform failures above and the
URL-ownership alternative above — were already shown). The result
notes applied reading (a) and incorrectly labeled the model wrong.

### What changed

`SKILL.md`'s Staccato contrast test now states the both-sides test
explicitly and carries the joe.dev pair as the canonical compressed
example. The Pattern C section of `evals/failures/rewrite-reuses-flagged-pattern.md`
was withdrawn. The assertion in `evals/rewrite-evals.json` that
previously expected `keep` on this line was updated to require
`revise` with a mechanism-naming rewrite, or `ask-author` if the
design rationale would have to be invented. The two affected result
notes carry retraction sections.

### What not to overgeneralize

This does not mean every model verdict should be assumed correct.
The previous two iterations identified real model failures (invention,
cadence-reused rewrites, slop in rewrites) and produced doctrine
changes that moved measurable metrics. This lesson is specifically
about the situation where (1) the model produces the same verdict
across multiple iterations, (2) the verdict applies the doctrine
consistently across cases, and (3) the analyst's "this is wrong"
intuition cannot be reduced to a precise rule. In that situation the
doctrine is the prime suspect.

### Eval coverage

- `skills/anti-slop-writing/SKILL.md` (Staccato contrast test now uses both-sides test with worked examples from joe.dev)
- `evals/rewrite-evals.json`: `rewrite-reuses-flagged-pattern` (assertion corrected)
- `evals/failures/rewrite-reuses-flagged-pattern.md` (Pattern C withdrawn; rule list updated)
- `evals/results/2026-05-28-joe-beda-after.md` and `2026-05-28-rewrite-check-after.md` (retraction sections added)

## 2026-05-28 — Tuning against one document needs a generalization check

### Failure (risk, not a bug)

Four consecutive doctrine iterations (ask-author verdict, Rewrite check
field, both-sides staccato clarification) were all tuned against one
post: joe.dev/posts/thinking-out-loud. Each moved a metric on that
post. But metric movement on the tuning document cannot distinguish a
doctrine rule that fixes a real, repeatable failure from one that
merely fits that document's quirks.

### What changed

Ran the doctrine against a real text it was never tuned on — Paul
Graham's "How to Write Usefully", chosen because it is dense with the
exact surface patterns the doctrine targets (short antithesis,
rule-of-three) but is almost entirely earned human rhetoric. The
doctrine flagged 0 of 15 paragraphs while still discriminating (it
named the demagogue line as earned-leaning-compressed and "more
fundamental" as a too-mild soft spot). A naive cadence-only classifier
would have wrongly flagged four paragraphs; the both-sides test
rescued them on text it had not seen. That is the evidence the rule
generalizes. The false-positive resistance was locked in as adversarial
cases so a future change cannot silently regress it.

### What not to overgeneralize

Zero flags is not automatically a pass. It was a pass here because the
document is genuinely clean and the per-item reasoning was inspectable
and discriminating. The complementary test is still missing: run a
deliberately sloppy real document and confirm the flag rate rises. A
clean-document test only exercises the false-positive half of
calibration.

### Eval coverage

- `evals/adversarial.json`: `earned-antithesis-synthesis-pg`, `cataphoric-label-defined-in-paragraph`, `escalating-magnitude-triple`
- `evals/meta-evals.json`: `single-source-overfitting`, `earned-rhetoric-false-positive-rate`
- `evals/results/2026-05-28-generalization-pg.md`

