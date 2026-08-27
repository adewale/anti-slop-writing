# Failure: cataphoric teasers walked past unflagged

## Original

The pattern was named for LLM output by Shane Littrell, PhD
([@MetacogniShane, 2026-08-26](https://x.com/MetacogniShane/status/2092638724915896675),
~1.1k likes):

> One of the red flags of AI-written text is the heavy use of these odd linguistic
> constructions called "cataphoric teasers" to create an artificial feeling of suspense.
> These are easy to spot because they usually take the form of phrases like, "Here's the
> part that nobody tells you…" or "Here's what most people get wrong…" or "Here's where it
> gets interesting." From my experience, text written by Claude is often saturated with
> these types of phrases. I don't see it as much in ChatGPT (that's anecdotal, though. I
> might be wrong).

Quoting Jan Zilinsky, who pointed at Paul Bloom's version of the same complaint
([Substack, 2026-08](https://substack.com/@smallpotatoes/note/c-322302112)):

> The problem is that it tries too hard. It's eternal clickbait; every sentence is trying to
> get you to read further — as in the classic AI tic, "It's not X … it's Y!" Good writers do
> this too, but carefully, in small doses. AI lacks the confidence to step back and let the
> ideas engage the reader. Its motto is Always Be Closing, and the effect is cloying. It's a
> strange thing to say about AI writing, but it's too needy to be enjoyable.

Bloom's second tell — `It's not X … it's Y!` — the doctrine already caught (`Not X. Y.`,
`Not just X, but Y`, the staccato contrast test). The teaser it did not.

## Why it failed

The skill had run over a canonical teaser and said nothing. `evals/adversarial.json` →
`stopslop-divergence-compressed-antithesis` puts `Here's the thing: building products is
hard...` verbatim in its prompt. The recorded Opus critique
(`evals/results/2026-06-14-stop-slop-ablation/panel/outputs/opus/`) fills every slot of the
output format and nails the compressed antithesis — and never mentions the opener. Worse,
the case's own `expected_output` ("Our skill keeps the opener") and the critique's rewrite
line ("keep the opener, restore the relation") both explicitly protect it. The case-writing
panel and the applier each had the pattern in front of them and read past it.

The coverage was one-sided in three ways:

- **No detector named the failure mode.** Nothing in `SKILL.md` covered forward reference or
  promise-discharge.
- **Lexical coverage was incidental: 2 of 14 probe phrases.** `This is where X comes in` and
  `Let's dive into` were on the avoid list as generic marketing phrases, not from any
  reasoning about cataphora. `Here's the thing`, `But there's a catch`, `It gets worse`,
  `The reason is simple`, `More on that below` and the rest had no hook at all.
- **The only calibrated position on cataphora was a *keep* rule.** `adversarial.json` →
  `cataphoric-label-defined-in-paragraph` (holdout) correctly protects Paul Graham's
  `loose, then tight`, and `references/flow-by-relation.md` actively *prescribes* generating
  cataphors ("Add one hinge sentence before the list or section shift"). The only brake was
  one unillustrated clause: "Make the hinge factual rather than grand."

## Mechanism

**Cataphoric teaser.** A forward-pointing line whose job is to manufacture suspense rather
than to label what follows. It is the prospective twin of decorative antithesis: the staccato
test catches a contrast that lands before the *prior* prose evidenced both sides; the teaser
lands a promise before any *following* prose discharges it. Same failure — rhythm standing in
for content — with the missing evidence on the other side of the line.

The discriminator is the discharge test: does the next sentence or two deliver the promised
payload? Three ways it fails — undischarged, payoff-restates-the-tease, and saturation
(Bloom's whole-piece version, where every paragraph opens by pulling the reader forward).

## Better rewrite

```txt
Before: Here's where it gets interesting: the cache is what makes the whole thing fast.
        Without the cache, it would be slower.
After:  The cache is what makes it fast: a cold read costs two round trips to Postgres,
        a warm one costs a map lookup.
```

The `After` keeps the colon. Forward reference is not the defect; an undischarged promise is.

## Not the parataxis case

The 2026-06-13 parataxis round drafted a plausible rule and lost the gate because the
doctrine already caught the behavior — application gap, not rule gap (see
`evals/failures/tweet-parataxis-density.md`). This is the opposite: the recorded miss above
is direct evidence that the pre-edit doctrine had no trigger to apply. That is what makes the
rule worth gating rather than assuming.

## Not a new observation

The pattern has at least seven names across seven traditions, the oldest predating LLMs by a
decade with the same word. Blom & Hansen, "Click bait: Forward-reference as lure in online news
headlines" (*Journal of Pragmatics* 76, 2015, 87-100) analysed 100,000 headlines under the
keywords `Cataphora · Discourse deixis · Forward-reference`, and its abstract opens by
performing the device: "This is why you should read this article." Three sibling anti-slop
skills ship the rule as "infomercial engagement hooks"; tropes.fyi splits it into four tropes by
shape; copywriting teaches it as "open loops"; Sanderson's craft framework calls the failure a
promise with no payoff; LinkedIn "broetry" criticism made the same complaint about human writers
a decade ago.

The framings disagree about verdicts, and those disagreements are what the doctrine had to
resolve. `docs/cataphoric-teaser-prior-art.md` records the comparison, the four disagreements
that change what gets flagged, and what was taken from each.

## Rule added or changed

- `SKILL.md`: a `Cataphoric teaser` detector with the discharge test, editing-pass step 19,
  three literal never-earned forms on the avoid-by-default list, and `undischarged cataphoric
  teaser` added to the mandatory `Rewrite check` self-audit so a fix does not reintroduce one.
- `references/anti-slop-writing-doctrine.md`: a `Cataphoric teasers` section with the three
  failure sub-forms, the earned twin (cataphoric label), the false-positive caution, and the
  relation to the staccato contrast test.
- `SKILL.md`: a `Teaser boundaries` line carrying the three distinctions that change runtime
  behaviour — forward-pointing only, discharge is necessary but not sufficient, and scarcity
  frames carry a defect discharging cannot repair.
- `references/anti-slop-writing-doctrine.md` → `Boundaries and neighbours`: the four
  cross-framing disagreements with worked examples, plus the adjacent patterns that must be
  diagnosed separately.
- Evals — catch: `evals.json` → `cataphoric-teaser-undischarged` (tune),
  `cataphoric-teaser-self-posed-question` (tune),
  `cataphoric-teaser-payoff-restates-tease` (holdout),
  `scarcity-framing-survives-discharge` (holdout); `rewrite-evals.json` →
  `cataphoric-teaser-saturated-section` (tune), `pre-announced-significance-rewrite` (tune).
  Earned guards and precision cases: `adversarial.json` →
  `earned-cataphoric-enumeration-label` (tune), `back-pointing-label-not-cataphoric` (tune),
  `earned-cataphoric-question-discharged` (holdout), `earned-discourse-deixis-roadmap`
  (holdout), alongside the existing `cataphoric-label-defined-in-paragraph`.

**Status: ungated.** The A/B round required by `runbooks/hillclimb-skill.md` has not been run
(it needs the sub-agent judge protocol). Tracked in `TODO.md`.
