# Lessons learned

This file records why doctrine changed. Each lesson should point to a concrete failure, the smallest rule that addressed it, and the boundary that prevents overgeneralization.

The per-attempt graveyard of rejected edits lives in `evals/rejected-edits.md`. Use this file for lessons that survived; use that one for the rejects that did not.

## 2026-08-29 — The scored run found our own contamination and a can't-pass-honestly assertion before it measured anything

### Failure

Two flaws in the same day's additions, both caught by the pre-registered A/B run rather than by review. First, the new `references/rewrite-patterns.md` examples reused the exact source passages of two tune eval cases — worked answers sitting in arm B's visible references (the arm-B apply agent reported it unprompted, and also reported the second flaw: those reference rewrites invented counts, dates, and mechanisms absent from their sources, violating the skill's own no-invention rule). Second, `structural-cadence-run`'s third assertion demanded "at least one verified finding" from an excerpt containing no evidence — an assertion satisfiable only by inventing, so Opus failed the honest output that declined.

### What changed

The run note discloses and discounts the two affected tune deltas (the pre-registered gate was holdout-only and no holdout passage appears in any reference, so the decision rule survived). Post-scoring: both reference examples were rewritten onto non-eval passages with invention-honest rewrites (ask-author for the missing mechanism; a check-plan where the source has no evidence), each with an inline note recording the original flaw; the failure record's rewrite got the same fix. The assertion reword is queued as next-round tune work in `TODO.md`, not hot-fixed after seeing scores.

### What not to overgeneralize

Teaching examples may still use invented *scenarios* — a fictional product in a card is fine. The rule is narrower and two-sided: an example presented as the rewrite of a specific quoted source may only contain facts that source supplies; and no passage may serve as both eval input and reference material, because the reference side of that pair is an answer key. On the eval side: an assertion must be satisfiable by the doctrine-compliant response — when the source lacks evidence, "resolution" means naming the checks, and the assertion has to accept that form.

### Eval coverage

- `evals/results/2026-08-29-scored-run.md` (disclosures §3-4) and `run-metadata.json` (known_contamination).
- Assertion fix and hardening queued in `TODO.md`; the corrected reference sections carry inline notes.

## 2026-08-29 — The register moved while the word list stood still; an external catalog found the gap

### Failure

Diffing Simon Willison's llm-cliche-highlighter (simonw/tools, Apache-2.0) against `SKILL.md` showed the doctrine's lists tracked the 2023-24 essay register (delve, tapestry, testament — the Wikipedia group, which the 2026-05-27 research round had already mined) while all 27 of the highlighter's conversational-register patterns were absent: significance compression ("that's the whole point", "that's not nothing"), therapy voice ("sit with that", "worth naming"), performative honesty ("I won't pretend", "let's be honest"), stage management ("here's the thing", "turns out"), dev-blog boilerplate ("zero config", "it just works"), and six structural cadence shapes. This is the drift the doctrine's own time-dated-detectors note predicted, caught by someone else's catalog rather than our re-profiling.

### What changed

Eval contract first (five `evals.json` cases, four earned-use `adversarial.json` guards, two `rewrite-evals.json` cases, two `meta-evals.json` checks, manual cases 11-12), then the smallest doctrine edit that satisfies it: two detector entries (new-register families with dose-response framing; structural cadence), nine avoid-phrases, five high-risk words, one drift-note sentence — +197 words against the +200 budget, after consolidating the two "not just/only" banned-phrase near-duplicates. Full family detail went to the doctrine reference, not `SKILL.md`. Separately, the highlighter's design was ported as a deterministic grading layer: `evals/oracles/slop_lint.py` (22 detectors, embedded positive+negative self-tests, a demo fixture that trips every detector exactly once) plus `run_evals.py lint`, so forbid-shaped rewrite checks now grade without a judge (`docs/deterministic-graders.md`).

### What not to overgeneralize

The oracle is recall, not verdict: it flags "no breaking changes, no new dependencies" and "Every request… Every trace id…" exactly as it flags their decorative twins, which is why the four earned-use adversarial cases exist. Deterministic checks stay forbid-shaped; a deterministic require-check is a keyword-stuffing incentive. And the new families are as time-dated as `delve` was — the durable import is the structural detectors and the two-layer grading design, not the 2025 phrase list. Score evidence is pending a full sub-agent run: the smoke run in `evals/results/2026-08-29-highlighter-mining.md` covers deterministic checks only, so this round claims coverage expansion, not measured doctrine improvement.

### Eval coverage

- `evals/evals.json` (tune): `new-register-significance-compression`, `performative-honesty-stage-management`, `structural-cadence-run`; (holdout): `holdout-devblog-boilerplate`, `holdout-therapy-voice-retro`.
- `evals/adversarial.json` (tune): `earned-negation-chain-changelog`, `earned-turns-out-with-trace`, `earned-anaphora-invariant-chain`; (holdout): `holdout-earned-honesty-clarification`.
- `evals/rewrite-evals.json` (tune): `strip-new-register-launch`; (holdout): `holdout-stage-managed-postmortem`.
- `evals/meta-evals.json` (tune): `deterministic-vs-judge-split`; (holdout): `holdout-oracle-drift-review`.
- Oracle self-tests run inside `scripts/validate.py`.

## 2026-06-14 — Borrowed surface rules were inert; our mechanism tests already subsume them

### Failure

A review of the sibling skill [hardikpandya/stop-slop](https://github.com/hardikpandya/stop-slop) surfaced two ideas worth borrowing: a numeric self-score gate (5 axes, `< 35/50 -> revise`) and a "cut quotables" detector. The open question was whether either adds anything our doctrine lacks. It also surfaced a trap: stop-slop's literal rules are blanket bans (all adverbs, all passive voice, all em-dashes, all Wh- openers), which our adversarial suite exists to reject.

### What changed

Nothing in the installable `SKILL.md`. A guarded, mechanism-aware version of both ideas was A/B-tested against a baseline snapshot across three models (Opus 4.8, Sonnet 4.6, Haiku 4.5), apply/judge separated, in `evals/results/2026-06-14-stop-slop-ablation/`. All 18 paired deltas were exactly 0.00 (CI [0,0], p=1.0 — REJECT): the candidate did not move a single decision. "Cut quotables" is the emphasis-source test we already ship; the self-score gate is a numeric reskin of the existing bounded judge-refine pass. Logged in `evals/rejected-edits.md`. Kept: one regression guard, `evals/adversarial.json` → `earned-passive-adverb-when-opener`, which locks in "keep earned passive voice, adverbs, and subordinate openers."

### What not to overgeneralize

Do not read this as "stop-slop has nothing." Its numeric `< 35/50` gate is a crisp self-checkable stop condition, and its short rule handles ("cut quotables") aid recall; those are presentation ideas, not new capabilities. The lesson is narrower: before importing a surface rule, flatten it to the behavior it asks for and check whether an existing mechanism test already produces that behavior. When it does, the import is inert and belongs in the graveyard, not the doctrine. The one durable transfer was defensive — a guard against the blanket-ban failure mode the borrowed rule would have introduced if copied literally.

### Eval coverage

- `evals/adversarial.json` (tune): `earned-passive-adverb-when-opener` (earned passive/adverb/Wh-opener guard).
- Run: `evals/results/2026-06-14-stop-slop-ablation/` (treatment block, 36 outputs, 36 blind judgments, paired delta, gate output).

## 2026-06-13 — The doctrine already covered parataxis; the gap was application, not rules

### Failure

Applied to a real X thread (`evals/fixtures/tweet-taste-as-model/`) that closes nearly
every section on a paratactic antithesis, the skill kept all of them — "I do not touch
any of this." Each closer was individually earned, so the per-sentence staccato test
passed each one and the document-level over-reliance went unflagged. This looked like a
missing rule about parataxis.

### What changed

Nothing in the installable `SKILL.md`. A `Parataxis density` rule and `Parataxis repair`
subsection were drafted and A/B-tested against a pre-edit snapshot over two rounds
(`evals/results/2026-06-13-parataxis-hillclimb/`). The edit did not clear the gate —
not even on `parataxis-earned-but-pervasive`, a case built so that only a document-level
check should fire. The pre-edit doctrine caught that case every time via the staccato
contrast test's "keep or use once" line and the "symmetrical paragraph length, parallel
structure" tell. The behavior change was reverted (`evals/rejected-edits.md`). Kept: a
`Parataxis and hypotaxis` teaching section in the doctrine reference (names the concept,
consolidates the existing guidance, gives before/after examples) and six regression
cases that lock in the already-passing behavior.

### What not to overgeneralize

Do not read this as "parataxis is always fine." The real failure — defending pervasive
parataxis on the tweet — was an application inconsistency: during a long, multi-issue
review the agent did not apply the across-the-piece "use once" lens. The fix for that is
attention/checklist discipline at apply time, not a new detector. And do not delete the
staccato "use once" guidance: it is the mechanism that already does this work.

### Eval coverage

- `evals/rewrite-evals.json` (tune): `parataxis-pervasive-closers`,
  `parataxis-unstated-relation`, `parataxis-coordination-hides-cause`,
  `parataxis-chained-and`, `parataxis-earned-but-pervasive`.
- `evals/adversarial.json` (tune, earned guards): `earned-parataxis-sequence`,
  `earned-parataxis-evidenced-contrast`.
- Runs: `evals/results/2026-06-13-parataxis-hillclimb/` (round 1, round 2, rate study)
  and the motivating `evals/results/2026-06-13-tweet-taste-as-model/`.

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

## 2026-05-28 — A variance gap is not a doctrine gap
### Failure

A round of the emphasis-source blinded A/B showed that the paragraph-scale flatten (`C4.A2`) was not produced in one sample: the agent reached for the syntax-relation connective on the observability escalation instead of flattening it. The tempting read was a doctrine gap — the emphasis-source test said "flatten the line," with no handle for a multi-sentence ladder — so guidance was added to flatten whole ladders, with a guard to keep ordered timelines.

A second blinded round (15/15 vs 15/15) and then a rate study (3/3 vs 3/3 on flatten-the-ladder, 3/3 vs 3/3 on keep-the-timeline) showed the guidance was inert. The baseline already flattened escalation ladders reliably and already kept timelines. The original miss was sampling variance, not a capability the doctrine lacked.

### What changed

Nothing, in the end. The provisional doctrine change was reverted; the rate-study method was added to `evals/blinded-eval-harness.md`.

### What not to overgeneralize

Before adding doctrine to fix a single observed miss, check whether the miss reproduces. One failed sample can be run-to-run variance; a rate study (N samples, behavioral classification, compare rates) tells you whether the capability is actually absent. Adding words to fix noise leaves dead text the skill's own "contribution must justify length" bar would cut. The discipline: hypothesize, measure, and when the result is null, remove your own change rather than keep it or loosen the assertion to manufacture a win.

### Eval coverage

- `evals/results/2026-05-27-emphasis-source-experiment.md` Round 6.
- `evals/blinded-eval-harness.md` rate-study section.
- `evals/rejected-edits.md` records the rejected ladder-guidance edit.

## 2026-05-28 — An assertion can test for the label instead of the behavior

### Failure

In the emphasis-source blinded A/B, the scorer flagged the original `C3.A2` assertion as ambiguous: "Recognizes that applying the emphasis-source test (flatten the cadence) would lose the symmetric drop/re-add operation." On an adversarial keep-case, a correct critique says "keep, the symmetry is load-bearing" — it does not need to name or perform a specific doctrine test. The assertion was demanding a vocabulary move (invoke the named test) rather than the underlying judgment, which is the same keyword-stuffing anti-pattern the runbook warns about, inverted onto the grader.

### What changed

`C3.A2` and `C5.A2` were rewritten to reward recognizing that the structure carries distinct, non-redundant content, with "explicitly performing a flatten is sufficient but not required." Under the cleaned wording both doctrines pass both cases — the false failures disappeared.

### What not to overgeneralize

A keep-case assertion should test that the agent does not misclassify, not that it recites a procedure. A flag-case assertion may legitimately require a specific artifact (e.g., the flattened sentence) when producing that artifact is the behavior under test. The line: require the artifact when the artifact is the point; never require the artifact's *name*.

### Eval coverage

- `evals/adversarial.json` holdout: `earned-emphasis-from-idea` (`A2`), `earned-paragraph-escalation` (`A2`).
- `evals/blinded-eval-harness.md` assertion-design rules.

## 2026-05-28 — Procedures produce artifacts; labels do not. The statistical gate is a separate question.

### Failure

Adding the named Starkman tests (`Emphasis-source test`, `Syntax-relation test`) to `SKILL.md` as labels — phrased as questions to ask — did not change agent behavior in a blinded A/B (13/15 vs 13/15). Both doctrines reached the diagnostic by inference from `Unseeing frame` and the staccato contrast test. The named labels were inert.

Rewording the same tests as procedures — "to apply, write the flattened version of the line in your critique" — produced a measurable behavioral change in the critique text. The procedural agent reliably wrote the flattened sentence and called the residual generic. The labeled agent gestured ("flatten it and the line collapses") without producing the artifact.

### What changed

`SKILL.md` carries the procedural wording of both tests. The behavioral evidence is recorded in `evals/results/2026-05-27-emphasis-source-experiment.md` (Rounds 4–5).

### What not to overgeneralize

The observed +1/+2 deltas in the blinded A/B do **not** pass the new statistical gate added in PR #2 (paired-bootstrap CI overlaps zero at N=5, sign-flip p=1.0). The doctrine change is retained on qualitative behavioral evidence, not as a gated score improvement. Two distinct claims live here, and both are true:

- Procedures cause a specific observable artifact to appear in the output; labels do not. This is qualitative and reproducible.
- A small-N delta on five cases is not statistically significant. The right way to convert the qualitative claim into a gated score improvement is more cases, not more confidence in the existing few.

Procedural language costs words. Use it where the assertion has a specific observable artifact in mind. Do not procedural-ize tests whose value is interpretive judgment ("classify this contrast as earned, compressed, or decorative") — for those, the label and three-way split is the procedure.

### Eval coverage

- `evals/results/2026-05-27-emphasis-source-experiment.md` Rounds 3–5 and the gate disposition.
- `evals/results/2026-05-28-emphasis-source-procedural/scores.jsonl` per-case audit trail.
- `evals/blinded-eval-harness.md`.

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

While adding the word-list-drift material, the change introduced an unsourced statistic: that `delve` usage "dropped roughly 80%" in 2025. The public reporting describes the decline only qualitatively ("dropped off sharply"); the 80% figure was invented. This reproduces the exact unsupported-specificity / fake-precision failure that `regime-shift-new-slop` warns about, inside the anti-slop doctrine itself, by the person writing it.

### What changed

Replaced the invented percentage with the qualitative claim the source actually supports, in the doctrine reference, the `word-list-drift` meta-eval prompt, and this file. Added an explicit instruction in the doctrine reference not to manufacture a drop percentage for `delve`.

### What not to overgeneralize

Sourced quantitative claims are good and wanted: the Antislop 1,000x figure stays because the paper states it. The rule is provenance, not number-avoidance. Cite the figure the source gives; do not invent precision the source lacks. A clean-looking statistic is the most persuasive form of slop, which is why it has to clear the same evidence bar as any other claim.

### Eval coverage

- `evals/meta-evals.json`: `regime-shift-new-slop` (the pre-existing guard this violation should have tripped), `word-list-drift`
