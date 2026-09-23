# Coined compound labels — round record (2026-09-05, corrected 2026-09-23)

Source: the OpenAI "Using GPT-6 Astra" prompting guide, section *Personality
and writing style*, fetched 2026-09-05 from
`https://developers.openai.com/api/docs/guides/latest-model.md`. Its anti-jargon
prompt asks the model to avoid "invented compound labels like 'exact-head
checks' and 'editorial-row layouts'".

**Outcome: inconclusive.** `SKILL.md` is unchanged. Only four trials per arm
turned out to be valid, too few to tell whether the candidate rule helps. The
round's durable output is its eval cases, a documented failure mechanism, and a
list of design defects. A pre-registered re-run that avoids those defects is in
`../2026-09-23-coined-label-rerun/`.

The first version of this record overstated the evidence. It counted verdicts
instead of grading the cases' assertions, it treated round 2 as independent, and
it said a decontamination check showed the rule transferring. The corrections
come from a blinded regrade in `regrade/` and from the subagent transcripts,
recorded in `run-metadata.json`.

## The mechanism

A coined hyphenated label is shaped like the name of a mechanism. So it can
pass the emphasis-source test, which asks whether the flattened claim still
names an actor, mechanism, or limit. It can then be rescued by false-positive
restraint, which keeps a term when the sentence supplies the mechanism. Neither
rule asks whether the supporting term is itself resolvable. One baseline
critique put it directly: "Specificity missing: None. The paragraph names ...
the mechanism (exact-head checks run before each merge)".

## What was tested

| Fixture | Content | Correct behaviour | Eval case |
|---|---|---|---|
| P1 | two coined labels, never defined | name them as coined or undefined | `coined-compound-label` |
| P2 | `write-ahead log`, `copy-on-write` | keep | `earned-domain-compound` |
| P3 | a coinage defined in the same sentence | keep | `coined-label-defined-in-place` |
| P4 | fresh coinages, other tells not removed | name them as coined or undefined | none, probe only |

The baseline arm was `SKILL.md` at `53370ff`. The candidate, `candidate.patch`,
added a detector, an editing-pass step, and a resolvability clause on
false-positive restraint, 135 words in all. `candidate-v2.patch` removed the P1
strings the first candidate quoted. Apply agents ran on Claude Sonnet 5, with
one baseline trial each on Claude Opus 5 and Claude Haiku 4.5.

## Results, regraded

From the primary judge in `regrade/`. The score is the fraction of the case's
assertions passed.

| Case | Arm | Valid trials | Mean score | Names the coinage |
|---|---|---:|---:|---:|
| P1 | baseline, Sonnet 5 | 4 | 0.50 | 2/4 |
| P1 | candidate, Sonnet 5 | 4 | 0.92 | 4/4 |
| P4 | baseline, Sonnet 5 | 4 | 0.42 | 2/4 |
| P4 | candidate-v2, Sonnet 5 | 4 | 0.75 | 3/4 |

The guards P2 and P3 scored 1.00 in every valid trial. On P1, Opus 5 passed
every assertion, and Haiku 4.5 named the coinage but invented a definition for
it. The round-1 gate still rejects, with a mean delta of +0.14 and a sign-flip p
of 0.51. The equivalence test returns NOT SHOWN, so an effect has not been ruled
out either.

## Design defects

Each of these is avoided in the re-run.

- **Too few trials.** A two-sided sign-flip test on four discordant pairs cannot
  go below p=0.125, so round 1 could not pass at any effect size.
- **Guards scored as pairs.** Eight of round 1's twelve pairs were guard
  fixtures, correct under both arms by construction, which diluted the four that
  could move.
- **The doctrine quoted the fixture.** The first candidate quoted P1's own
  coinages. `candidate-v2` removed them but still quoted P2's standard terms.
- **Round 2 was not independent.** Both of its agents read earlier trials'
  critiques before writing, including critiques from the other arm. All eight
  round-2 trials are excluded.
- **Several trials shared one context.** Four "independent" trials of one
  paragraph were written in a single context. Where several paragraphs shared a
  context, text leaked between them. One candidate critique of P1 copied P3's
  definition into its rewrite.
- **The arms could not load the same files.** The baseline read `SKILL.md` from
  the skill directory and could load its references. One baseline trial did.
  The candidate file sat outside that directory, where the reference paths do
  not resolve.
- **Verdicts stood in for grades.** No judge agent ran. A flag for the wrong
  reason, or a rewrite that invented a definition, counted as a pass.
- **The P4 fixture was confounded.** It was not stripped of other tells, and a
  hand check of it counted only critiques that called the terms "coined", the
  candidate doctrine's own word.
- **Model versions were not recorded.** They are recovered in
  `run-metadata.json`.

## What the guide covers, and what these rounds tested

The guide's *Personality and writing style* section gives three prompts. Every
instruction in them is listed below, along with the skill-file warning from its
*Instruction following* section. Statuses were checked against
`skills/anti-slop-writing/` on 2026-09-23.

| Guide instruction | Status here |
|---|---|
| Avoid "invented compound labels like 'exact-head checks' and 'editorial-row layouts'" | **Tested** here, inconclusively; the re-run in `../2026-09-23-coined-label-rerun/` is pre-registered |
| A skill file "may cause the model to pause and block work early"; add a precedence line | **Probed** on Sonnet 5 and did not reproduce; untested on non-Claude models (`TODO.md`) |
| Avoid "delve", "foster", "it's worth noting" | Already in the avoid lists |
| Avoid "This isn't about X. It's about Y." and "X, not Y" framing | Already covered by the negative-parallelism detector and the staccato contrast test |
| Avoid canned transitions; state the actual relationship | Already covered by the flow-by-relation test and hypotaxis rules |
| State the main point early | Already covered: "Delete generic opening" and "What is the exact point?" |
| Avoid "leverage", "importantly", "genuinely" | **Not tested.** None is on a list, and `SKILL.md` itself uses "genuinely" once |
| Avoid "Bottom Line:", "In short:", "The simplest mental model is:" | **Not tested.** The conclusion test covers the class, but none is listed |
| Avoid the "Question? Answer." rhythm | **Not tested.** No detector covers it |
| Don't say what you won't do, what stays unchanged, or how you'll group results | **Not tested.** No detector covers this kind of padding |
| Use lists only for parallel, sequential, or comparable items; avoid nested lists | **Not tested.** The doctrine flags formatting as fake structure but has no positive criterion for when a list is right |
| Avoid hyphenated compound descriptions in general | **Not tested, deliberately.** Read literally, it bans standard terms, and the guard cases exist to stop that |
| Prefer active voice, plain language, and less jargon | **Not tested.** The doctrine covers concreteness but has no rule on voice or jargon |

The untested rows are candidates, not gaps. `Lessons_learned.md` records that
borrowed surface rules are often inert once an existing mechanism test is
applied, so each one needs a failing case before it earns doctrine.

## The instruction-precedence probe

The guide's *Instruction following* section warns that GPT-6 Astra "can be more
sensitive to instructions contained in skills" and that "unclear or conflicting
guidance in a skill file may cause the model to pause and block work early". It
recommends an explicit precedence line. `SKILL.md` has none, and its
`ask-author` verdict tells the model to stop and ask.

`probe-precedence.md` sets two user instructions directly against the skill. B1
declines the critique format and asks to ship one line. B2 waives the mandatory
`Rewrite check` slot. On Claude Sonnet 5 the skill complied with both, one trial
each (`outputs/precedence-sonnet.md`). It shipped the line with its concern
attached, "Flagging one thing, not asking it", and left out the `Rewrite check`.
No change was made. The warning concerns a model not reachable here, so it is
untested there rather than disproved; see `TODO.md`.

## Files

```txt
PREREGISTRATION.md              hypothesis, SESOI, accept rule, round-2 amendment
run-metadata.json               per-agent model, doctrine, context design, transcript audit, status
probe-fixtures.md               P1, P2, P3
probe-fixture-p4.md             P4
probe-precedence.md             B1, B2
candidate.patch                 against SKILL.md at 53370ff; quotes P1's coinages
candidate-v2.patch              P1's coinages removed; still quotes P2's terms
outputs/                        every critique produced
delta.jsonl, gate-output.txt    round-1 gate as first scored, by verdict
delta-p1-contaminated.jsonl, gate-p1-contaminated.txt
                                rounds 1 and 2 on P1, by verdict; round 2 since excluded
regrade/                        blinded regrade against the eval cases' assertions
```

To rebuild a candidate doctrine:

```bash
git show 53370ff:skills/anti-slop-writing/SKILL.md > SKILL.md
patch SKILL.md < evals/results/2026-09-05-astra-compound-labels/candidate-v2.patch
```
