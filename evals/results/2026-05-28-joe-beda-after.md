# After — skill review of joe.dev "Thinking out loud" post

Date: 2026-05-28
Change commit (doctrine after the ask-author verdict): see this branch's
HEAD after the 2026-05-28 commit.
Source under review: https://joe.dev/posts/thinking-out-loud/
Local snapshot used for the run: `/tmp/joe-beda-post.md`

A fresh-context subagent re-ran the same review task on the same post,
with the updated SKILL.md (Critique output format now includes
`ask-author` as a verdict; Default editing pass step 7 forbids inventing
a name to fill a slot; antithesis classification now requires reading
the prior sentence).

## Counts

| Metric | Before (2026-05-28-joe-beda-before.md) | After | Change |
|---|---:|---:|---|
| Major inventions (fabricated tool name, fabricated events, fabricated timing) | 5+ | 0 | All eliminated |
| Total invention events (all sizes) | ~10 | ~4–6 | ~50% reduction |
| Cadence-reuse events in rewrites (X-not-Y, em-dash antithesis) | ~4 | 0–1 | Eliminated or reduced to borderline |
| `ask-author` uses | 0 (verdict did not exist) | 3 | New behavior at the exact failure sites |
| Antithesis misclassifications (graded earned contrast as decorative) | 1 (Item 10) | 1 (Item 12) | No change |

## Where the new verdict fired

The three `ask-author` verdicts in the after run map cleanly to the
three worst invention sites in the before run:

| Before-run site | Before-run invention | After-run verdict | After-run question |
|---|---|---|---|
| Item 14 ("Current coding tools made it practical…") | "Claude Code turned the cover-image generator from a someday-item into an afternoon." | `ask-author` (Item 17) | "Ask author: which coding tool — Claude Code, Cursor, Copilot, Aider, something else?" with a fallback to cut the topic sentence and let the next sentence carry the work. |
| Item 8 ("The community is unusually authentic…") | "PDS for fifty friends, a labeler experiment for academic citations, and a feed generator written over a weekend." | `ask-author` (Item 10) | "Ask author: which person, talk, or project at ATmosphere made the non-ad-platform character of the crowd legible?" with a fallback rewrite that does not invent. |
| Item 9 ("The protocol is coming into its own…") | "Two years ago the case for ATproto was a whiteboard." | `ask-author` (Item 11) | "Ask author: which one or two ATproto pieces that were paper-only when he invested are now in production?" with a fallback to cut. |

## Cadence change on the canonical line

Source line:

```txt
ATproto lets you store structured records in a data server (your PDS)
that you own and can move. That's not incidental. It's the design.
```

Before-run Concrete rewrite:

```txt
ATproto stores your posts as structured records on a PDS — a small
data server you can run yourself or rent, and repoint without losing
your handle or follows. Portability is the design, not a future
feature.
```

The before rewrite preserved the source's X-not-Y compressed-antithesis
shape (`Portability is the design, not a future feature`) and added
`em-dash` antithesis (`PDS — a small data server`).

After-run Concrete rewrite:

```txt
ATproto lets you store structured records in a data server — your PDS —
that you own and can move between hosts. Because the records are
portable, anything built on top of them is portable too.
```

The after rewrite drops the X-not-Y closer and uses `Because X, Y` —
the hypotactic move the doctrine recommends.

## Remaining inventions in the after run

Smaller but real:

- Item 4 names "Google Reader, Posterous, Svbtle" as platforms that
  "stopped being where the conversation is." They are real defunct
  platforms but Joe did not mention them. The detector did not catch
  this because the surrounding sentence does name one platform (Medium)
  the source supplied, and the model treated the slot as continuation
  rather than substitution.
- Item 13 invents an enumeration of standard.site's schema ("a lexicon
  for a page, a feed, and the site itself"). Joe says only that
  standard.site is "for publishing websites and blog posts." The
  detector did not catch this because the invented enumeration sounds
  more like a description than a fact.

The remaining inventions share a shape the new rule did not directly
address: invention by elaboration when the source supplies one example
and the rewrite extends it into a list.

## Retraction on the "decorative misclassification" claim

This note originally framed the model's `decorative antithesis`
verdict on `That's not incidental. It's the design.` as a
misclassification. A later iteration found that the doctrine itself
was ambiguous between (a) "the topic of the contrast was evidenced"
and (b) "both sides of the contrast were evidenced." The model was
applying (b) consistently — graded as compressed, not decorative
strictly speaking, but the action is the same — and (b) is the
defensible reading: the prior sentence evidences movability but not
intentionality. See `evals/results/2026-05-28-rewrite-check-after.md`
for the full retraction, and the updated `SKILL.md` Staccato contrast
test for the clarified rule with the joe.dev pair as the canonical
compressed example.

## Assessment

The metric moved on the dominant failure (invention) and on the
secondary failure (rewrites reusing the flagged cadence). The verdict
addition was load-bearing: making `ask-author` a real, named output the
format accepts gave the model somewhere to put "I would need a fact the
source does not supply," and three of the worst invention sites in the
before run became `ask-author` calls in the after run with the actual
question stated. The cadence-reuse pattern also dropped — the canonical
line that produced `Portability is the design, not a future feature` in
the before run produced `Because the records are portable, anything
built on top of them is portable too` in the after run, the
doctrine's recommended hypotactic move.

Two real gaps remain. The classification rule for earned vs decorative
antithesis did not fire when the prior sentence supplied the mechanism;
this is the same misclassification in both runs and needs a separate
fix. And invention by elaboration (the model continuing an enumeration
the source started, with items the source does not contain) is a
failure mode the new rule does not target. Both belong to the next
iteration, not this one.
