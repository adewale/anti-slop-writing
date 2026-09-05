# Coined compound labels — round record (2026-09-05)

Source of the idea: the OpenAI "Using GPT-6 Astra" prompting guide, section
*Personality and writing style*, fetched 2026-09-05 from
`https://developers.openai.com/api/docs/guides/latest-model.md`. Its anti-jargon
prompt asks the model to avoid "invented compound labels like 'exact-head
checks' and 'editorial-row layouts'".

**Outcome: the doctrine edit was REJECTED and did not ship.** `SKILL.md` is
unchanged. Three eval cases and a failure record were kept. Graveyard entry in
`evals/rejected-edits.md`.

## Pre-registration

`PREREGISTRATION.md`, written before any output existed, plus an amendment
written before round 2 existed. SESOI 0.05. Accept rule: `score_delta.py`
ACCEPT.

## What was tested

Three fixtures (`probe-fixtures.md`), each stripped of the doctrine's other
tells so any flag has to come from the behaviour under test:

| Fixture | Content | Correct behaviour |
|---|---|---|
| P1 | two coined labels, never defined | flag |
| P2 | `write-ahead log`, `copy-on-write` | keep |
| P3 | a coinage defined in the same sentence | keep |

The candidate doctrine (`candidate-SKILL.md`, +135 words, budget +200) added a
coined-compound-label detector, one editing-pass step, and a resolvability
clause on **False-positive restraint** — the rule that turned out to be doing
the laundering.

## Results

Baseline, one trial each on the full fixture set: Opus flagged P1
(`ask-author`), Haiku flagged P1 (`revise`). Both kept P2 and P3.

Sonnet, the model that shows the gap, P1 verdicts across 8 baseline and 8
candidate trials:

| Round | Baseline P1 flagged | Candidate P1 flagged |
|---|---:|---:|
| 1 (4 trials/arm) | 2/4 | 4/4 |
| 2 (4 trials/arm) | 2/4 | 4/4 |
| **Total** | **4/8** | **8/8** |

P2 and P3 were kept in **every** run of both arms, all models. The candidate
introduced no over-flagging: it is not a blanket ban on hyphenated terms.

## Why it was rejected

Two independent reasons, either of which is sufficient.

**1. The gate rejects.** Round 1 as designed (12 pairs, including guard
fixtures that score 1 under both doctrines by construction): mean delta
+0.1667, 95% CI [+0.0000, +0.4167], sign-flip p=0.5057 — REJECT. Rounds 1+2 on
the discriminating fixture only (8 pairs, `delta-p1-contaminated.jsonl`): mean
delta +0.5000, 95% CI [+0.1250, +0.8750], sign-flip p=0.1254 — REJECT.

The second number is the important one. Four discordant pairs all pointing the
same way is the *most* extreme result this design can produce, and a two-sided
sign-flip test on four discordant pairs bottoms out at 2/2^4 = 0.125. The round
was structurally incapable of clearing p<0.05 no matter how large the true
effect. That is a power failure in the design, not evidence about the rule.

**2. The candidate arm was contaminated.** The candidate detector quoted
`"exact-head checks"` and `"editorial-row layouts"` — the exact strings in
fixture P1. A candidate-arm agent noticed and said so unprompted. So 8/8 may
measure string matching rather than the rule generalising. The comparison is
not valid evidence either way.

## Decontamination check

`candidate-v2-SKILL.md` carries the same rule with the fixture phrases removed
from the doctrine, tested on `probe-fixture-p4.md`, whose coinages
(`soft-quorum drains`, `tenant-affinity pools`) appear in neither doctrine.
Four trials per arm.

**The rule does transfer to coinages it has never seen.** The verdict counts are
not the evidence — read the diagnostic content instead:

| Arm | Verdicts | Flagged | Names the coinage *as* a coinage |
|---|---|---:|---:|
| baseline | revise, ask-author, revise, keep | 3/4 | **0/4** |
| candidate-v2 | ask-author, revise, ask-author, revise | 4/4 | **2/4** |

The baseline never once identified either hyphenated term as coined or
undefined. The candidate did it explicitly, and reached for the earned-side
boundary unprompted: "Neither is standard shorthand the way 'write-ahead log' or
'copy-on-write' is, and the paragraph never opens either one up." That is the
rule generalising, not a string match — which retires the contamination worry
about rounds 1-2, though not the power failure that actually caused the reject.

Two caveats keep this from being a clean win.

**P4 is a confounded fixture.** Unlike P1, it was not stripped of the doctrine's
other tells. The baseline flagged it 3/4 for unrelated defects: a
syntax-relation failure (sentence two asserts a detection outcome from a
mechanism that only establishes ordering) and an internal contradiction between
`soft-quorum` and `never`. So the 3/4-vs-4/4 verdict comparison measures almost
nothing, and only the 0/4-vs-2/4 diagnostic column carries signal.

**Transfer is partial.** 2/4 is not 4/4. On P1, where the doctrine named the
exact strings, the candidate fired 8/8. On unseen coinages it fires about half
the time. The gap between those two numbers is the size of the contamination
effect, and it is large.

## What a future round would need

- Roughly 12 trials per arm, not 4, to make p<0.05 reachable at this effect size.
- A doctrine that never quotes a fixture string.
- A held-out fixture with fresh coinages, scored separately from the tuning one.
- Ideally a cross-family judge; only the Claude family was reachable here, so
  per `docs/judge-protocol.md` these numbers are a coverage signal, not a
  calibrated measurement.

## Files

```txt
PREREGISTRATION.md              hypothesis, SESOI, accept rule, round-2 amendment
probe-fixtures.md               P1/P2/P3
probe-fixture-p4.md             fresh-coinage fixture for the decontamination check
probe-precedence.md             B1/B2, the separate instruction-precedence probe
baseline-SKILL.md               doctrine snapshot, before arm
candidate-SKILL.md              +135 words, quotes fixture strings (contaminated)
candidate-v2-SKILL.md           same rule, fixture strings removed
outputs/                        every critique produced, both arms
delta.jsonl                     round-1 pairs as designed
delta-p1-contaminated.jsonl     rounds 1+2, discriminating fixture only
gate-output.txt                 round-1 gate, full and holdout-only
gate-p1-contaminated.txt        rounds 1+2 gate
```

## Second finding: the instruction-precedence risk did not reproduce

The same guide's *Instruction following* section warns that GPT-6 Astra "can be
more sensitive to instructions contained in skills" and that "unclear or
conflicting guidance in a skill file may cause the model to pause and block work
early", and recommends an explicit precedence line. `SKILL.md` has no precedence
language and carries an `ask-author` verdict that tells the model to stop and
ask, so the risk looked real on inspection.

It did not reproduce. `probe-precedence.md` puts two user instructions directly
against skill instructions: B1 declines the critique format and asks to ship a
single line; B2 explicitly waives the mandatory `Rewrite check` slot. The skill
complied with both (`outputs/precedence-sonnet.md`). B1 returned the bare
rewrite and attached its concern without blocking — "Flagging one thing, not
asking it". B2 omitted the `Rewrite check` line as instructed.

No change made. The honest scope of this result: the warning is about GPT-6
Astra, which is not reachable from this environment, and the probe ran on one
model in the Claude family. It is untested for the model it describes rather
than disproved. Recorded in `TODO.md`.
