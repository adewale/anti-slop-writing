# Before — skill review of joe.dev "Thinking out loud" post

Date: 2026-05-28
Baseline commit (doctrine before the ask-author verdict): `0515987`
Source under review: https://joe.dev/posts/thinking-out-loud/
Local snapshot used for the run: `/tmp/joe-beda-post.md`

This is the raw critique a fresh-context subagent produced when given
the SKILL.md doctrine and all three reference files, then asked to
review the post using the Critique output format.

## Invention count

The rewrites introduced approximately 10 claims of fact not present in
the source paragraph they were rewriting:

| Item | Source line | Invented fact in rewrite |
|---|---|---|
| 4 | "You ran (or paid for) a server." | "Apache process," "HTML into a directory" |
| 8 | "Developers, researchers, artists, people just interested in what the internet could be." | "PDS for fifty friends," "labeler experiment for academic citations," "feed generator written over a weekend" |
| 9 | "felt more theoretical when I first bet on it" | "Two years ago," "a whiteboard" |
| 14 | "Current coding tools made it practical to add features that would otherwise get cut." | "Claude Code" |
| 15 | "Without good tooling that kind of thing stays on the 'someday' list." | "a weekend I wasn't going to spend," "cost an hour" |

None of these facts are in the source. The most flagrant case is Item 8,
which fabricates specific projects encountered at a conference the model
did not attend.

## Cadence-reuse count

The rewrites reused the cadence the items flagged in roughly four places:

| Item | Source cadence flagged | Rewrite cadence shipped |
|---|---|---|
| 5 | "without anyone in the middle" | "no ranker, paywall, or TOS between the words and the reader" (rule-of-three substituted for single phrase) |
| 6 | "not just the app" (X-not-Y) | "in the protocol, not bolted onto one app" (X-not-Y) |
| 8 | "Not trying to build the next ad platform. Trying to figure out…" (Not X. Y.) | "builders, not founders pitching ad models" (X-not-Y) |
| 10 | "That's not incidental. It's the design." (X-not-Y, period-split) | "Portability is the design, not a future feature." (X-not-Y, comma-split) |

## Misclassification

Item 10 classified `That's not incidental. It's the design.` as
*decorative* antithesis. The prior sentence —
`ATproto lets you store structured records in a data server (your PDS) that you own and can move.` —
supplies the mechanism. By the doctrine's own definitions this is closer
to *earned* antithesis. The classifier graded the sentence in isolation
and missed the paragraph-scope evidence.

## Why this happened

The Critique output format requires a `Concrete rewrite` slot.
`Verdict: revise` followed by a blank or hedged rewrite is not
syntactically valid output. When the legitimate fix needs a fact the
model does not have, the format compels the model to ship a fabricated
one.

The self-check question added on 2026-05-26 lives in the Final
self-check at the end of the file. The model writes the critique
linearly, never circles back, and the question never fires.

## Full captured critique

Stored in the corresponding result file
`evals/results/2026-05-28-joe-beda-after.md` alongside the after-run
output, for side-by-side comparison.
