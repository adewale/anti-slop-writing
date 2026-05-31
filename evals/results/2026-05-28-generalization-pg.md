# Generalization test — Paul Graham, "How to Write Usefully"

Date: 2026-05-28
Doctrine commit under test: `7db66c1` (after ask-author, Rewrite check, both-sides staccato test)
Source: https://paulgraham.com/useful.html (published February 2020)
Local snapshot: `/tmp/pg-useful-post.md`

## Why this test exists

Four consecutive doctrine iterations (ask-author verdict, Rewrite check
field, both-sides staccato clarification) were all tuned against a
single document: joe.dev/posts/thinking-out-loud. Metric movement on
the tuning document does not prove the skill improved in general — it
could mean the doctrine was fit to that post's quirks. This run tests
the doctrine on real prose it was never tuned against.

The target was chosen adversarially. A heavily-proofread Paul Graham
essay about writing carefully is dense with exactly the surface
patterns the doctrine targets — short antithesis ("Useful writing is
bold, but true.", "loose, then tight"), rule-of-three, and
short-declarative cadence — but almost all of it is *earned* human
rhetoric. If the doctrine over-flags PG, that is a real false-positive
finding about over-correction. If it stays restrained while still
discriminating, that is evidence against overfitting.

## Result

A fresh-context subagent reviewed all 15 paragraphs with the full
doctrine loaded.

| Metric | Value |
|---|---:|
| Paragraphs flagged revise / ask-author / reject | 0 |
| Paragraphs kept | 15 |
| Short antitheses correctly classified earned | 5+ |
| Banned-phrase stems correctly read as mention/working-usage | 3 ("Let's put them all together", "This is where", "Believe it or not, there is a trick") |

## Is zero flags a ceiling effect?

The repo's own discipline says an all-pass run is a prompt to ask
"success or ceiling effect?" Two reasons this reads as success, not a
ceiling artifact:

1. The document is genuinely clean. A published, heavily-proofread
   essay by a careful writer, on the subject of writing carefully,
   *should* pass an anti-slop review. Over-flagging it would be the
   failure mode, not the pass.

2. The review showed discrimination, not blanket leniency. The
   subagent named:
   - the demagogue line ("The converse of vaporous academic writing is
     the bold, but false, rhetoric of demagogues") as
     earned-leaning-compressed, because one side (academic vagueness)
     was evidenced and the demagogue side was introduced fresh — kept
     only because the sentence names the relation explicitly ("the
     converse of") rather than relying on cadence;
   - "more fundamental" in P7 as an asserted-not-shown soft spot,
     weighed and judged too mild to flag.

   A reviewer going easy on a famous author would not surface these.

The most important observation: the subagent stated that a naive
classifier keyed on cadence alone would have wrongly flagged P5, P12,
P13, and P14. The both-sides test is what rescued them. That means the
2026-05-28 staccato clarification is doing real work on text it was not
tuned against — the strongest available evidence that the rule
generalizes rather than fitting joe.dev.

## What this produced

This run did not motivate a doctrine change; the doctrine behaved
correctly. Instead it locked in the false-positive resistance as
regression coverage, so a future "improvement" cannot silently
reintroduce over-flagging:

- `evals/adversarial.json`: `earned-antithesis-synthesis-pg`
  ("Useful writing is bold, but true."),
  `cataphoric-label-defined-in-paragraph` ("loose, then tight"),
  `escalating-magnitude-triple` (the delete/abandon escalation).
- `evals/meta-evals.json`: `single-source-overfitting` (the risk this
  run was designed to check) and `earned-rhetoric-false-positive-rate`
  (how to read a near-zero flag rate honestly).

## Limits of this test

One document cannot fully separate "well-calibrated doctrine" from
"lenient model." The mitigation is that the per-item both-sides
reasoning is inspectable and was checked. A stronger future test would
run a deliberately sloppy real document (marketing copy, a generated
draft) through the same doctrine and confirm the flag rate rises — the
true-positive half of the calibration that this clean-document test
does not exercise.
