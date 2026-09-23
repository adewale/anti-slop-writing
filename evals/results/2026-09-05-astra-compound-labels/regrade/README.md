# Regrade of the 2026-09-05 round (done 2026-09-23)

The round's original scores came from matching each critique's `Verdict:`
line: `revise` or `ask-author` counted as a pass on P1, and `keep` as a pass on
the guards. No judge agent ran. That missed two things the eval cases actually
assert. One baseline critique flagged P1 for its "rather than at read time"
contrast, not its coinages, and its rewrite kept both coined labels. The
Haiku critique invented a definition for the label, which the case's third
assertion forbids. Both counted as passes.

This directory regrades every critique the round produced against the
assertions of its eval case, following `docs/judge-protocol.md`.

## Method

- `build_batches.py` splits the 46 critiques into one item per case, gives each
  an opaque id, shuffles across arms and models, and writes the judge inputs and
  `key.json`. It regenerates the exact inputs the judges saw. P4 is not an eval
  case, so it is graded against three assertions that mirror P1's with P4's
  coinages.
- Two judges graded every item without seeing arm, doctrine, model, or file
  name. The primary judge was `claude-sonnet-5`, eight batches of up to six
  items each. The secondary judge was `claude-haiku-4-5-20251001`, two batches
  of 23. Transcript audits show each judge read only its batch and wrote only
  its output.
- `score_regrade.py` unblinds the judgments, scores them with
  `scripts/run_evals.py grade`, rebuilds the round-1 pairs exactly as
  `../delta.jsonl` paired them, and runs `scripts/score_delta.py`. Its output is
  `summary.md`.

Two deviations. A first attempt gave the Sonnet judge 23 items per agent; both
agents hit their output limit and wrote nothing, so they were stopped and the
same items were re-batched in sixes. One line of the Haiku judge's second file
nested `graded_dimensions` inside the assertions array. It was repaired by
moving one bracket, and the file as written is kept as
`judgments/haiku-batch-2.as-written.jsonl`.

## Results

Scores are the fraction of the case's assertions passed, from the primary
judge. "Names it" means the first assertion passed: the critique identified a
coined label as coined or undefined.

| Case | Arm | Trials | Mean score | Names it |
|---|---|---:|---:|---:|
| P1, round 1 | baseline, Sonnet 5 | 4 | 0.50 | 2/4 |
| P1, round 1 | candidate, Sonnet 5 | 4 | 0.92 | 4/4 |
| P1 | baseline, Opus 5 | 1 | 1.00 | 1/1 |
| P1 | baseline, Haiku 4.5 | 1 | 0.67 | 1/1 |
| P4 | baseline, Sonnet 5 | 4 | 0.42 | 2/4 |
| P4 | candidate-v2, Sonnet 5 | 4 | 0.75 | 3/4 |

P2 and P3, the guards, scored 1.00 in every valid trial of both arms and all
three models. Round 2 is excluded because both of its agents read earlier
trials' critiques before writing their own; its scores are in `summary.md` for
the record.

The round-1 gate, regraded, still rejects, and nothing can be concluded from it:

```txt
round-1 design, 12 pairs   mean +0.1389   95% CI [+0.0000, +0.3333]   p=0.5057   REJECT   TOST NOT SHOWN
P1 only, 4 pairs           mean +0.4167   95% CI [+0.0000, +0.8334]   p=0.4995   REJECT   TOST NOT SHOWN
```

The judges agreed on 127 of 138 assertions and on the first assertion for 43
of 46 items. Every gate verdict was the same under both judges.

## What the regrade changes

- **The decontamination check did not show transfer.** The round's README said
  the P4 baseline "never once" identified a coinage as coined or undefined,
  against 2 of 4 for the decontaminated candidate. Both judges put it at 2 of 4
  against 3 of 4. The earlier hand check counted only critiques that called the
  terms coined, which is the candidate doctrine's own word. Two baseline
  critiques asked what the terms meant, and that meets the assertion.
- **"Reliably on Opus and Haiku" was one trial each.** Opus 5 passed every
  assertion. Haiku 4.5 named the coinage and then invented a definition for it.
- **A shared context leaked text between paragraphs.** One candidate critique
  of P1 wrote a fallback that "hashes the head revision on both replicas", which
  is P3's definition, copied from the paragraph beside it.
- **The secondary judge was lenient toward its own model.** The Haiku judge
  passed the Haiku critique's invented definition, citing the invented text as
  evidence. The Sonnet judge failed it.

## Files

```txt
build_batches.py                       rebuilds the blinded judge inputs and key.json
key.json                               opaque id -> file, case, split as run, arm, model, status
judgments/sonnet.jsonl                 primary judge, blinded
judgments/haiku.jsonl                  secondary judge, blinded
judgments/haiku-batch-2.as-written.jsonl  the file before the one-bracket repair
judgments/*.unblinded.jsonl            the same, keyed by case, file, and section
score_regrade.py                       unblinds, scores, pairs, and gates
scores/                                run_evals.py grade output per judge
delta-*.jsonl                          round-1 pairs rebuilt from the regrade
summary.md                             every table and gate output
```
