# Failure: Rewrites invent specifics and reuse the flagged cadence

## Source

A real review of [Joe Beda, "Thinking out loud, with a URL I own"](https://joe.dev/posts/thinking-out-loud/) (2026-05-25),
captured in `evals/results/2026-05-27-rewrite-self-check.md` and
`evals/results/2026-05-27-joe-beda-before.md`. The skill was given the
full post, the Critique output format, and the doctrine, and asked to
produce a per-item review.

## What the skill produced (verbatim, before)

### Pattern A — invention substitutes for ask-or-cut

Source line:

```txt
Current coding tools made it practical to add features that would otherwise get cut.
```

Concrete rewrite the skill produced:

```txt
Claude Code turned the cover-image generator from a someday-item into an afternoon.
```

The post never names the tool. The rewrite picked one and shipped it as
fact. The paragraph beneath the topic sentence is already concrete (Node.js,
Satori, sidecar regeneration), so the rewrite did not need a tool name —
but the format invited one, and the skill obliged with invention.

Source line:

```txt
The community is unusually authentic. Developers, researchers, artists, people just interested in what the internet could be. Not trying to build the next ad platform. Trying to figure out what good social infrastructure actually looks like.
```

Concrete rewrite the skill produced:

```txt
The room was mostly builders, not founders pitching ad models. I talked to people running their own PDS for fifty friends, a labeler experiment for academic citations, and a feed generator written over a weekend. Nobody was waiting on Bluesky the company to ship anything for them.
```

The rewriter was not at ATmosphere. "PDS for fifty friends," "labeler
experiment for academic citations," and "feed generator written over a
weekend" are fabricated events. The replacement reads more concrete but
is more wrong than the abstract version it replaced.

Similar invention appears in the rewrites for "The original web didn't
work this way" (invents "Apache process," "HTML into a directory") and
"The protocol is coming into its own" (invents "Two years ago," "a
whiteboard").

### Pattern B — rewrites reuse the cadence the item flags

Source line:

```txt
That's not incidental. It's the design.
```

Concrete rewrite the skill produced:

```txt
Portability is the design, not a future feature.
```

The item correctly flagged the source as compressed antithesis. The
rewrite reproduced the same `X, not Y` shape with different punctuation.
Same pattern appears in the rewrite of "the protocol underneath, not
just the app" (becomes "in the protocol, not bolted onto one app") and
in the rewrite of "unusually authentic" (becomes "builders, not founders
pitching ad models").

### Pattern C — withdrawn

An earlier draft of this file claimed the review misclassified
`That's not incidental. It's the design.` as decorative when it should
have been earned. On re-reading the doctrine, the model's call was
correct: the prior sentence evidences movability (`you own and can
move`) but does not evidence intentionality (that this is by design
rather than incidental). One side of the contrast is supported; the
other is a new claim. That is the doctrine's definition of compressed
antithesis, and the model's `revise` verdict was the right action.

The lesson is about the doctrine, not the model: the original
definition (`the contrast names a real distinction already evidenced`)
was ambiguous between "the topic was evidenced" and "both sides were
evidenced." See the clarified Staccato contrast test in `SKILL.md`,
which now states the both-sides test explicitly and uses this exact
joe.dev pair as the canonical compressed example.

## Why it failed

The doctrine has a self-check question that asks whether a rewrite needs
a fact the source did not supply, but the critique output format does
not give the model anywhere to say "ask the author." The only verdicts
are `keep / revise / reject`. When `revise` is the right call and the
fix needs a fact, the model produces the rewrite anyway, because the
format demands a `Concrete rewrite` field. Invention fills the slot.

For Pattern B, the self-check is positioned at the end of the editing
pass. The model writes the items linearly and never circles back to
apply it.

For Pattern C, the staccato-contrast classifier examines a single
sentence. It cannot tell earned from decorative without the prior
sentence in scope.

## Mechanism

When the output format requires a field, the model fills it. If the
field is `Concrete rewrite` and the legitimate fix requires a missing
fact, the model invents the fact rather than refuse the format.

## Better outcome

Source line:

```txt
Current coding tools made it practical to add features that would otherwise get cut.
```

Better verdict and rewrite:

```txt
Verdict: ask-author
Concrete rewrite: Ask author: which coding tool? Cursor, Claude Code, Copilot, Aider, other? Without that, cut the topic sentence — the next sentences (Node.js script, Satori, sidecar regeneration) carry the paragraph on their own.
```

Source line:

```txt
That's not incidental. It's the design.
```

Better verdict (with full paragraph in scope):

```txt
Verdict: keep
Slop tells: Surface cadence resembles compressed antithesis, but the prior sentence ("ATproto lets you store structured records in a data server (your PDS) that you own and can move.") supplies the mechanism. The contrast is earned.
```

## Rule added or changed

1. Add `ask-author` as a verdict in the Critique output format.
2. Require that `Concrete rewrite` not name a fact (tool, person, number, mechanism) absent from the source paragraph. If the fix needs such a fact, the verdict is `ask-author` and the rewrite slot states what to ask.
3. Clarify the Staccato contrast test: an antithesis is earned only when *both sides* of the contrast are evidenced in the prior prose, not when only the topic of the contrast was mentioned. Use the joe.dev pair as the canonical compressed example.
