# Rejected edits

This file is the graveyard of doctrine edits that failed an eval before being merged. One entry per rejection. The point is to stop relitigating the same failed move in a future round.

`Lessons_learned.md` records durable "what not to overgeneralize" lessons that survived. This file records the per-attempt rejects that did not. See `docs/hillclimb-improvements.md` (item 10) for the rationale, including SkillOpt's rejected-edit buffer ([arXiv 2605.23904](https://arxiv.org/abs/2605.23904)).

## Entry format

```
## YYYY-MM-DD — short label

### Edit attempted
The smallest description of the doctrine change.

### Eval that rejected it
The case id and suite (`evals/<file>.json` -> `<id>`), plus the holdout/tune split.

### Why it was rejected
Quoted evidence from the failing case.

### Lesson (if any)
Optional. Only fill in if the rejection generalizes. Otherwise leave blank and let the entry stand as a graveyard marker.
```

## Entries

## 2026-05-28 — Multi-sentence ladder guidance on the emphasis-source test

### Edit attempted

Extend the emphasis-source test in `SKILL.md` with explicit guidance for multi-sentence patterns: "When the pattern spans multiple sentences (a rule-of-three ladder, rising adjectives, a tiered good/better/best escalation), flatten the whole ladder to its single plain claim rather than one clause, because the structure is the borrowed pattern; keep the structure only when each step carries distinct concrete content, as an ordered timeline or pipeline does."

### Eval that rejected it

Rate study against `evals/evals.json` → `paragraph-scale-borrowed-emphasis` (split: tune) and `evals/adversarial.json` → `earned-paragraph-escalation` (split: holdout). Methodology: `evals/blinded-eval-harness.md` rate-study section, N=3 fresh critique agents per doctrine on the two decisive prompts, behavioral classification.

### Why it was rejected

Identical rates on both prompts:

- Flatten the observability escalation (P4): ladder-guided 3/3, baseline 3/3.
- Keep the deploy timeline (P5): ladder-guided 3/3, baseline 3/3.

The baseline doctrine already flattened escalation ladders reliably and already kept timelines. The original failure that motivated the edit was a single sample from an earlier 5-prompt round — sampling variance in the longer context, not a missing capability. Full Round 6 record in `evals/results/2026-05-27-emphasis-source-experiment.md`.

### Lesson (if any)

Recorded in `Lessons_learned.md` → "A variance gap is not a doctrine gap." A single observed miss can be variance; check whether it reproduces before adding doctrine to fix it.

## 2026-06-13 — Parataxis-density rule in SKILL.md

### Edit attempted

Add a `Parataxis density` detector line and a `Parataxis repair` subsection to `SKILL.md`: flag paratactic juxtaposition (side-by-side clauses with the relation unstated) used as the dominant device — every section closing on a two-part contrast, chained "and," repeated "X. Y." antithesis — even when each instance is individually earned, and convert most instances to hypotaxis while keeping at most one.

### Eval that rejected it

A/B (pre-edit snapshot vs edited doctrine), Opus 4.8 apply+judge, in `evals/results/2026-06-13-parataxis-hillclimb/`:
- Round 1: `evals/rewrite-evals.json` → `parataxis-pervasive-closers`, `parataxis-unstated-relation`, `parataxis-coordination-hides-cause`, `parataxis-chained-and`; `evals/adversarial.json` → `earned-parataxis-sequence`, `earned-parataxis-evidenced-contrast` (all tune). N=6, mean delta -0.0278, 95% CI [-0.2500, +0.1667], sign-flip p=1.0 — REJECT.
- Round 2: `evals/rewrite-evals.json` → `parataxis-earned-but-pervasive` (tune), built so only a document-level check should fire. N=3/side: before 0.833, after 0.917 — within noise.

### Why it was rejected

The pre-edit doctrine already catches document-level parataxis. Round-2 before-doctrine quotes: "earned antithesis may be kept once. Used four times it stops being a distinction and becomes the format" (the staccato contrast test's "keep or use once"); "Four in a row makes the passage symmetrical and formulaic" (the "symmetrical paragraph length, parallel structure" tell). The new rule renamed an existing capability without moving the score. Reverted `SKILL.md` to the snapshot; kept a `Parataxis and hypotaxis` teaching section in `references/anti-slop-writing-doctrine.md` (reference, not gated runtime behavior) and the six eval cases as regression coverage.

### Lesson (if any)

Recorded in `Lessons_learned.md` → "The doctrine already covered parataxis; the gap was application, not rules."
