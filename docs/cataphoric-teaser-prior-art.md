# Cataphoric teasers: prior art and competing framings

`skills/anti-slop-writing/SKILL.md` carries one rule for this pattern — the cataphoric
teaser detector and its discharge test. That rule is a synthesis. At least seven traditions
have described the same behaviour, each cutting the space along a different axis, and they
do not agree on the verdicts. This note records what each one catches, where they conflict,
and which resolution the doctrine takes.

The motivating failure and the recorded pre-edit miss are in
`evals/failures/cataphoric-teaser.md`. This file is the literature layer, in the genre of
`docs/eval-null-result-literature.md`.

## The seven framings

| Framing | Source | Verdict axis | Names it |
|---|---|---|---|
| Forward-reference | Blom & Hansen 2015, linguistics | Referential mechanism (neutral) | `forward-reference`, `cataphora`, `discourse deixis` |
| Faithful FR | HonestBait 2023, NLP | Entailment between promise and body | `forward reference`, faithful vs clickbait |
| Infomercial hook | Sibling anti-slop skills | Surface phrase list | `infomercial engagement hook`, `fragment-hook` |
| Trope shape | tropes.fyi | Syntactic shape | `Here's the Kicker`, `The X? A Y.`, `Preamble` |
| Open loop | Copywriting / Zeigarnik | Whether the loop ever closes | `open loop`, `curiosity gap`, `information gap` |
| Promise / payoff | Sanderson, fiction craft | Structural debt across a piece | `promise`, `progress`, `payoff` |
| Eternal clickbait | Bloom 2026, criticism | Density and reader relationship | `eternal clickbait`, `Always Be Closing` |

### 1. Forward-reference (linguistics)

Jonas Nygaard Blom and Kenneth Reinecke Hansen, "Click bait: Forward-reference as lure in
online news headlines," *Journal of Pragmatics* 76 (2015): 87-100,
[doi:10.1016/j.pragma.2014.11.010](https://doi.org/10.1016/j.pragma.2014.11.010). 100,000
Danish headlines; 251 citations. Its keyword list is `Cataphora · Discourse deixis ·
Forward-reference · Media commercialization · Tabloidization`, and the abstract opens by
performing the device: *"This is why you should read this article."*

They define forward-reference as a "stylistic and narrative luring device trying to induce
anticipation and curiosity," and split it in two:

- **Cataphora** — sentence-level. A word or phrase whose referent arrives later
  (`This is what nobody tells you: ...`).
- **Discourse deixis** — points at the text itself rather than at content
  (`Read on to find out`, `The rest of this section covers...`).

This is the oldest and most precise framing, and it is descriptive: forward-reference is a
device, and the paper measures its frequency against commercialization rather than judging
individual instances. Littrell did not coin the term in 2026; he moved a headline-level
concept into body prose.

### 2. Faithful forward references (NLP)

Chih-Yao Chen, Dennis Wu, Lun-Wei Ku, "HonestBait: Forward References for Attractive but
Faithful Headline Generation," [arXiv:2306.14828](https://arxiv.org/abs/2306.14828) (2023).
They define forward references as "a technique for creating curiosity gaps at a discourse
level," and they *keep* them deliberately — the goal is verified news that competes with
misinformation for attention. The gate is a **textual entailment scorer**: the body must
entail what the headline promises.

That is the discharge test implemented as a model. It is also narrower than ours, which
matters — see the disagreements below.

### 3. Infomercial engagement hooks (sibling skills)

Three anti-slop skills in the same genre as this repo ship the rule under the same metaphor:

- [`conorbronsdon/avoid-ai-writing`](https://github.com/conorbronsdon/avoid-ai-writing) —
  "Infomercial engagement hooks": `"The catch?"`, `"The kicker?"`, `"Here's the thing."`,
  `"But here's the kicker:"`, `"The best part?"`, `"Plot twist:"`, `"The result?"`. Their
  gloss: "AI uses these to fake momentum and manufacture suspense around ordinary
  information — the prose equivalent of a late-night infomercial." Fix: delete the hook and
  state the thing.
- `Aboudjem/humanizer-skill` P41, the upstream, adds `"The brutal truth?"`, `"Sound familiar?"`.
- `blader/humanizer` P33 covers the fake-candid register: `"Honestly?"`, `"Look,"`,
  `"Real talk:"` as standalone openers.

`avoid-ai-writing` also carves off four neighbours that a coarse rule would swallow. They are
covered under **Neighbouring patterns** below.

### 4. Trope shapes (tropes.fyi)

[tropes.fyi](https://tropes.fyi/) catalogues 49 AI-writing tropes. Four are this pattern,
split by syntax rather than by function:

- **"Here's the Kicker"** — "false-suspense transitions promising revelation but delivering
  obvious points."
- **"The X? A Y."** — self-posed rhetorical questions answered immediately
  (`The result? Devastating.`).
- **Preamble (announce-then-answer)** — `Two constraints shape the design.`
- **Signposted Conclusion** — the retrospective twin.

### 5. Open loops (copywriting)

The technique taught deliberately, grounded in Bluma Zeigarnik's 1927 work on unfinished
tasks and George Loewenstein's 1994 information-gap theory of curiosity. In this tradition
the device is a tool, and the criticism is internal and specific: a loop *engineered never to
close* creates standing anxiety, which the trade press describes as exploiting rather than
using the effect. This is the only framing that reasons about the reader's state over time
rather than about a sentence.

### 6. Promise, progress, payoff (fiction craft)

Brandon Sanderson's plot framework. A promise is good; the failures are no progress on it and
no payoff for it. Two of its claims are load-bearing here. First, a payoff is "a surprising
but fulfilling answer to your promise" — so a payoff that merely confirms the promise is a
weak payoff, not a discharge. Second, readers lose interest when they feel no progress is
being made on the promises they are invested in, which names the *delayed* discharge as its
own failure rather than a milder version of the undischarged one.

Ambar Ancira's ["Writing Hooks"](https://ambarancira.substack.com/p/writing-hooks) (July 2025)
states the same failure from the reader's side: "you can write an outlandish hook, but if you
can't back it up, you're doing your article a disservice." She reads a hollow hook as a signal
of inexperienced or AI writing.

### 7. Eternal clickbait (criticism)

Paul Bloom, [Substack note](https://substack.com/@smallpotatoes/note/c-322302112) (2026):
"It's eternal clickbait; every sentence is trying to get you to read further... **Good writers
do this too, but carefully, in small doses.** AI lacks the confidence to step back and let the
ideas engage the reader. Its motto is Always Be Closing, and the effect is cloying." Relayed by
Jan Zilinsky as "a clickbait-like urgency."

Shane Littrell, [X, 2026-08-26](https://x.com/MetacogniShane/status/2092638724915896675), is
the naming source for LLM output and reports Claude in particular as saturated with the
pattern, flagged by him as anecdotal.

The genre criticism of LinkedIn **broetry** is the same complaint against human writers, a
decade earlier: a dramatic one-line hook, line breaks that force pauses, and — per the
[Content Marketing Institute](https://contentmarketinginstitute.com/articles/avoid-broetry-writing-trend/)
— "broets pump up the hook but leave their readers disappointed when the content doesn't live
up to the promise made." The economic driver is explicit there: a click on "See more" reads as
high-value engagement, so writers fragment to hide context behind the button.

## Where the framings disagree

These are the decisions the doctrine has to make, and the reason it is not simply a copy of any
one source.

### Entailment is not discharge

HonestBait passes a forward reference when the body entails it. Our discharge test asks
whether the following sentences *deliver* the promised payload and whether the payload adds
anything the teaser did not already contain.

`Here's where it gets interesting: the cache is what makes the whole thing fast. Without the
cache, it would be slower.` — the body entails the headline perfectly. HonestBait passes it.
We flag it, because the payoff restates the tease. Sanderson supplies the principle: a payoff
that only confirms the promise is not a payoff.

**Doctrine takes:** delivery, not entailment.

### Discharge is necessary, not sufficient

A forward reference can be fully discharged and still be worth cutting, when the payload's own
specifics already carry the emphasis the frame claimed.

`What surprised me most about the migration was the rollback. We had budgeted a week for it. It
took forty minutes.` — the promise is discharged, specifically. The frame is still redundant:
"budgeted a week / took forty minutes" *is* the surprise, and announcing it first tells the
reader what to feel before showing them why. `avoid-ai-writing` files this separately as
**emotional flatline** ("tell-don't-show: if the thing is genuinely surprising, the reader
should feel that from the content").

**Doctrine takes:** run the discharge test first; when it passes, still ask whether the frame
adds anything the payload does not.

### Scarcity claims are a second, independent defect

`Here's what nobody tells you about connection pooling: size the pool to the database's max
connections, not to your worker count.` — discharged, and discharged well. But the frame
asserts that the knowledge is rare, and it is standard documented advice. `avoid-ai-writing`
ties these framings ("what nobody tells you about," "the insight everyone's missing") to
**novelty inflation**, whose defect is a false claim about the world.

This is why discharging cannot repair the scarcity forms: fixing the payload leaves the false
claim standing. The repair is to drop the frame and keep the content.

**Doctrine takes:** two defects, checked separately. The three literal forms on the
avoid-by-default list are there because they carry both.

### Direction: cataphoric versus anaphoric

`avoid-ai-writing`'s **self-labeling significance** is the mirror image: `"That last move is
the contrarian one,"` `"This is the interesting part."` It points *back* at something already
said. It is a real defect — the label does the work the content was supposed to do — but a
cataphora rule must not claim it, or the diagnosis is wrong even when the verdict is right.

**Doctrine takes:** the teaser rule is forward-pointing only. Back-pointing labels are flagged,
if at all, under significance inflation.

### A phrase list contradicts itself

`Aboudjem/humanizer-skill` lists `"Here's the thing."` as a P41 trigger to delete, and forty
lines later recommends `"So here's the thing:"` as an informal transition that raises
perplexity and humanizes prose. Both entries are defensible; the file cannot hold both because
the axis is the phrase rather than the discharge.

This repo has a standing lesson against blanket bans — see `evals/rejected-edits.md`
(2026-06-14) and the `earned-passive-adverb-when-opener` guard.

**Doctrine takes:** the detector reasons about discharge. The avoid-by-default list carries
only the three forms that also make a scarcity claim, which is what makes them
context-independent.

### Preamble: our own reference prescribes what tropes.fyi flags

tropes.fyi lists **Preamble (announce-then-answer)** — `Two constraints shape the design.` — as
a trope. `skills/anti-slop-writing/references/flow-by-relation.md` prescribes precisely that
move: "Add one hinge sentence before the list or section shift," and the adversarial guard
`earned-cataphoric-enumeration-label` keeps `We report three robustness checks: held-out
scoring, a paired bootstrap, and a sign-flip permutation test.`

Both are right about different sentences. The discharge test separates them: when the two
constraints are named immediately and specifically, the line is a label; when the paragraph
announces a count and then wanders, it is a preamble.

**Doctrine takes:** the shape is not the defect. Keep the hinge advice; gate it on discharge.

### Dosage, not prohibition

Bloom is explicit that "good writers do this too, but carefully, in small doses," and the
copywriting tradition only objects to loops engineered never to close. Neither supports a ban.

**Doctrine takes:** saturation is its own sub-form, and a single discharged forward reference
is not a finding.

## Neighbouring patterns

Adjacent failures that share a surface with the teaser and should be diagnosed separately.
Names in parentheses are `avoid-ai-writing`'s.

- **Back-pointing significance label** (self-labeling significance) — anaphoric mirror; see above.
- **Pre-announced feeling** (emotional flatline) — `"What surprised me most,"` `"The most
  interesting part."` Forward-pointing and usually discharged; the defect is tell-don't-show.
- **Scarcity framing** (novelty inflation) — false claim about the world; survives discharge.
- **Rhetorical question opener** — `"So why should you care?"` A question is a teaser only when
  the answer does not arrive; when it does, it is an earned cataphor
  (`earned-cataphoric-question-discharged`).
- **Manufactured punchlines / staccato drama** — retrospective. Already covered by the staccato
  contrast test.

## What is not yet covered

- **Delayed discharge.** Sanderson's "progress" failure: the promise is eventually paid off,
  but several paragraphs later, so the teaser was doing engagement work rather than structural
  work. No eval case pins this, and the boundary (how far is too far) is not obvious enough to
  assert without evidence.
- **Discourse deixis as a distinct sub-form.** `earned-discourse-deixis-roadmap` guards the
  earned case; there is no catch case for an undischarged roadmap line
  (`Read on to find out what went wrong`).
- **Frequency data.** Every claim here about how often LLMs produce the pattern is anecdotal,
  Littrell's included. The Antislop-style frequency comparison that `SKILL.md` recommends for
  word lists has not been run for this construction.

## Absent from the largest catalogues

[Wikipedia:Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)
(WikiProject AI Cleanup) is roughly 25,500 words assembled from thousands of flagged drafts. A
grep of its raw wikitext returns zero hits for *suspense, curiosity, hook, clickbait, cataphora,
teaser, cliffhanger, "the catch"* or *"plot twist"*. The same holds for Alex Reinhart's
stylometric [LLM writing styles](https://www.refsmmat.com/notebooks/llm-style.html) notebook and
Matthew Vollmer's
[30-tell field guide](https://matthewvollmer.substack.com/p/i-asked-the-machine-to-tell-on-itself).

One qualification keeps this from being stronger evidence than it is: Wikipedia is encyclopedic
register, where a teaser would be edited out or never generated. Its absence there says less
about LLM prose in general than the word count suggests. It does mean there was no entry to
borrow.
