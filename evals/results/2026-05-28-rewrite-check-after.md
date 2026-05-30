# After — rewrite-self-check iteration

Date: 2026-05-28
Change commit (doctrine after the `Rewrite check` field): `6ee67be`
Source under review: https://joe.dev/posts/thinking-out-loud/
Local snapshot used for the run: `/tmp/joe-beda-post.md`

A fresh-context subagent re-ran the review task on the same post with
the updated `SKILL.md` (mandatory `Rewrite check` field in the Critique
output format) and the new "Rewrites must pass the same detectors as
the source" section in `references/rewrite-patterns.md`.

## Counts

| Metric | Before (iter-1 after) | After (iter-2 after) | Change |
|---|---:|---:|---|
| Rewrites with rule-of-three including invented or parenthetical list members | 2 | 0 | Eliminated |
| Rewrites with X-not-Y / negative-parallelism cadence | 3 | 0 | Eliminated |
| Rewrites with em-dash rule-of-three list as closer | 1 | 0 | Eliminated |
| Rewrites ending on a banned decorative closer ("That was the point", "Ultimately", etc.) | 1 | 0 | Eliminated |
| `ask-author` fallbacks that themselves invent specifics or use the flagged cadence | 1 | 0 | Eliminated |
| `Rewrite check` field uses (the field did not exist before this iteration) | 0 | 7 / 7 produced rewrites | New behavior, 100% adoption |
| Total items flagged on the same post | 21 | 12 | More conservative classification |
| Antithesis misclassification (earned graded as compressed/decorative) | 1 | 1 | No change (separate gap) |

## Where the new field fired

Every `Concrete rewrite` produced in this run carried a `Rewrite check`
line. The seven rewrites and their self-grades:

| Item | Rewrite (excerpt) | Rewrite check self-grade |
|---|---|---|
| 1 | "…some of that writing is longer than a social post can hold." | "one em-dash aside, which is naming the consequence rather than antithesis … Passes self-detectors." |
| 3 | "The original web ran on DNS and static files: if you owned the domain and kept the host paid…" | "no rule-of-three, no X-not-Y, no em-dash antithesis, no banned phrases, no invented facts … Passes self-detectors." |
| 5 (fallback) | "cut this paragraph entirely; the next paragraph already names the specific thing that makes the community visible (PDS records, standard.site running on this site)." | "fallback is a cut recommendation, not an invented rewrite — no invented topics, no X-not-Y, no rule-of-three. Passes self-detectors." |
| 6 | "ATproto stores structured records in a data server you own — your PDS — and the protocol is built so you can move that server without breaking the records' identity." | "one em-dash aside naming the PDS, no antithesis, no rule-of-three, no banned phrases. … Passes self-detectors." |
| 7 | "ATmosphere is where I saw this stack actually running, and the same records that show up at pdsls.dev for this site are what power the Bluesky preview cards above." | "no rule-of-three, no X-not-Y, no em-dash antithesis, no banned phrases, no invented facts (pdsls.dev and the preview cards are both already in the source). Passes self-detectors." |
| 9 (fallback) | "cut 'Current coding tools made it practical' and start the paragraph at 'The cover images on each post…' — the example carries the claim on its own." | "fallback is a cut, not an invented attribution … Passes self-detectors." |
| 10 | "Without that kind of help the Satori cover-image pipeline would have stayed on the 'someday' list with the long-dormant eightypercent.net migration." | "Passes self-detectors. Note: this rewrite still depends on Item 9 being resolved — if the author keeps 'Current coding tools' vague, 'that kind of help' inherits the same vagueness, and the better fix is to cut the sentence." |

Item 10's self-grade is the clearest evidence the field is doing
structural work. The model produced a rewrite, ran it through the
detectors, and noticed that one of its phrases inherits the vagueness
of an upstream item still pending an `ask-author` resolution. The
previous two iterations did not produce that kind of cross-item
self-awareness.

## Cadence change on the joe.dev ending paragraph

The iter-1 after run produced this rewrite for the ending:

```txt
The whole stack — Hugo, standard.site, my PDS — means the URL at the
top of this page survives me losing interest in any one of them.
That was the point.
```

Em-dash rule-of-three list + a decorative closer ("That was the point")
that is a stand-in for the banned "In conclusion / Overall /
Ultimately" closure.

The iter-2 after run keeps the ending instead of rewriting it:

```txt
Verdict: keep
Flow break: the post just stops at a fact, which is unusual for a
personal blog post but defensible. The doctrine's conclusion test asks
for a return to the concrete carrier and a transferable claim; this
ending returns to a concrete artifact (the source repo, the licenses)
and lets the reader infer the transferable claim from the post's
title and from "My words, at a URL I own." The post earns its lack of
decorative closer.
```

The change is not just "no rule-of-three closer in the rewrite" — it
is "no rewrite at all, because the existing ending defends." The new
field made the model audit its rewrite before shipping it, and the
audit revealed the rewrite was worse than the source.

## Verdict discrimination shifted

| Item type | iter-1 after | iter-2 after |
|---|---:|---:|
| `keep` | 6 | 6 |
| `revise` | 13 | 5 |
| `ask-author` | 3 | 2 |
| `reject` | 0 | 0 |
| Items in the post not flagged at all | n/a | n/a |
| Total items reviewed | 21 | 12 |

The total items reviewed dropped from 21 to 12. Items previously
revised that are now kept include the LinkedIn-trio paragraph (Item 5
in iter-1, Item 2 in iter-2), the colophon, and the licensing-line
ending. The Rewrite check requirement appears to have raised the bar
for declaring a revision: if the model cannot produce a rewrite that
passes the same detectors, it is more likely to either keep the
source or use `ask-author` than to ship a rewrite that itself fails.

## Retraction: the "persistent misclassification" was a doctrine ambiguity

This note originally claimed Item 6 of the iter-2 run was a
misclassification: `That's not incidental. It's the design.` graded as
compressed antithesis when (the original claim went) it should have
been earned because the prior sentence supplies the mechanism.

On re-reading the doctrine, the model's call was right and the claim
above was wrong. The original Staccato contrast test definition was
ambiguous between two readings:

(a) Earned = the topic of the contrast was evidenced.
(b) Earned = both sides of the contrast were evidenced.

Reading (a) treats the line as earned because movability is evidenced.
Reading (b) treats it as compressed because the prior sentence
evidences movability but not intentionality — the contrast adds the
"by design vs incidental" claim on cadence alone. The model applied
reading (b) consistently across three iterations, including on the
same post's `That's what I want. My words, at a URL I own.` (kept as
earned because both sides — the failure of platforms and the value of
owning a URL — were already shown).

The 2026-05-28 doctrine update makes reading (b) the explicit rule:
`SKILL.md` now states the both-sides test directly and uses the
joe.dev pair as the canonical compressed example. The eval assertion
in `rewrite-reuses-flagged-pattern` (which previously expected `keep`
on this line) was updated to require `revise` with a mechanism-naming
rewrite, or `ask-author` if the design rationale would have to be
invented.

The lesson: when a model's behavior keeps "failing" the same way
across iterations, check whether the doctrine is unambiguous before
assuming the model is wrong.

## Assessment

The doctrine change moved the dominant metric of this iteration. Every
category of slop the rewrites contained in iter-1 — rule-of-three with
invented members, X-not-Y cadence, em-dash rule-of-three closers,
banned decorative closers, ask-author fallbacks that invent — went to
zero in iter-2. The structural mechanism was making `Rewrite check` a
mandatory field in the per-item Critique output format: the model now
applies the same detectors to its rewrite inside the same loop that
applied them to the source, rather than being asked to circle back to
a Final self-check that never fired.

The remaining gap is the staccato classifier failing the prior-sentence
rule on tight one-sentence-prior context. That gap has now persisted
across three iterations on the same input, which makes it the obvious
target for the next round.
