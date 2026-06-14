# Stop-slop idea ablation — 2026-06-14

Source: a review of [hardikpandya/stop-slop](https://github.com/hardikpandya/stop-slop), a sibling instruction-only skill that fights the same target (generic LLM prose). This run tests whether two ideas borrowed from it improve our doctrine under our own harness.

## Ideas tested

Both were adapted to our mechanism-first philosophy (guards built in) rather than copied verbatim, because stop-slop's literal form uses blanket bans (all adverbs, all passive voice, all em-dashes, all Wh- openers) that our adversarial suite exists to catch. The guarded candidate block is in `treatment-block.md`.

1. **Self-score gate** — a 5-axis 1-10 numeric score (directness, rhythm, reader trust, authenticity, density) with a hard `< 35/50 → revise` threshold. Scored by mechanism presence, not surface tokens. This is the one structural feature stop-slop has that we lack as an explicit hard gate (we already have an ungated "score 1-5, improve the weakest dimension" pass).
2. **Cut quotables** — flag any line engineered to read like a pull-quote, then route it through the existing emphasis-source test.

## Method

A/B over the same six cases, two conditions each:
- **A** = current `skills/anti-slop-writing/SKILL.md` (snapshot: `baseline-SKILL.snapshot.md`).
- **B** = A with `treatment-block.md` appended.

Six cases (`cases.json`): three improvement cases from `rewrite-evals.json` (`durable-execution-mechanism`, `emphasis-source-flatten`, `outline-conclusion-carrier-bound`) and three over-flag-guard cases from `adversarial.json` (`robust-engineering-context`, `earned-antithesis`, `short-direct-answer`).

Apply/judge separation per `docs/judge-protocol.md`. Apply sub-agents ran across three models (Opus 4.8, Sonnet 4.6, Haiku 4.5; Fable 5 unavailable) and wrote outputs to `outputs/<model>/`. Judging done by Opus sub-agents, blind to the meaning of the `cond_A`/`cond_B` labels, grading each output independently against the case assertions with quoted evidence (`judgments/`).

18 paired before/after comparisons (6 cases × 3 models).

## Result: REJECT

Every paired delta is exactly 0.00. The candidate block changed no output on any case for any model — Opus produced byte-identical rewrites under both conditions on the clean cases. No improvement on the rewrite cases and no regression on the over-flag guards.

`scripts/score_delta.py delta.jsonl`:

```
Cases:         18
Mean delta:    +0.0000
95% CI:        [+0.0000, +0.0000]
Sign-flip p:   1.0000
Verdict:       REJECT (CI overlaps zero; delta is within noise).
```

## Why it was inert

The doctrine already does both jobs:

- **Cut quotables** is the **emphasis-source test** we already ship ("write the flattened version of the line... judge whether the residual claim still names actor/mechanism/limit"). The candidate restated it.
- **Self-score gate** is a numeric reskin of the existing **bounded judge-refine pass** ("score specificity, evidence fit, relation clarity, and rhythm on 1-5; improve the weakest dimension once"). Adding a 1-10 scale and a 35/50 threshold did not change any decision.

This repeats the 2026-06-13 parataxis finding: the gap, when there is one, is application, not rules.

## What was kept

- `evals/adversarial.json` → `earned-passive-adverb-when-opener` (tune): a regression guard that locks in "keep earned passive voice, adverbs, and subordinate openers." It is the standing defense against the blanket-ban form of the self-score idea, independent of whether the gate is ever adopted.

## Files

```
treatment-block.md            the guarded candidate addition (DOCTRINE_B = baseline + this)
baseline-SKILL.snapshot.md    DOCTRINE_A snapshot
cases.json                    the six A/B cases
outputs/<model>/*.md          36 applied outputs
judgments/<model>.jsonl       36 blind per-output judgments
delta.jsonl                   18 paired {id, split, before, after} rows
```
