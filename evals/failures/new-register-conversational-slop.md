# Failure: New-register conversational slop

## Original

```txt
Let's be honest: most migration guides are useless. I won't pretend ours was painless. But here's the thing: the schema change took four hours, not four weeks. Turns out the scary part was renaming a column. That's the whole story. Sit with that for a moment.
```

## Why it failed

The paragraph contains two real facts (four hours, a column rename) buried under five pieces of borrowed cadence. None of the flagged phrases appear in the doctrine's pre-2026-08 avoid lists, and the pre-change skill graded similar passages as merely "informal": the word list was tuned to the 2023-24 essay register (delve, tapestry, testament) while the model register had moved to a punchy conversational voice.

## Mechanism

Five distinct moves, all asserting what they should demonstrate:

- Performative honesty: `Let's be honest`, `I won't pretend` announce sincerity instead of showing it.
- Stage management: `here's the thing`, `Turns out` stage a reveal the content does not need.
- Significance compression: `That's the whole story` claims completeness while withholding the mechanism.
- Therapy voice: `Sit with that` performs reflection at the reader.
- The facts survive all five cuts, which is the tell that the cadence was decoration.

The register was catalogued externally before it was covered here: Simon Willison's llm-cliche-highlighter (simonw/tools, Apache-2.0) ships regexes for each of these families, alongside the Wikipedia-derived group the doctrine already covered. The gap was found by diffing that catalog against `SKILL.md` (all 27 of its "rhetorical tics" patterns were absent).

## Better rewrite

```txt
Our schema change took four hours, not the four weeks we had budgeted. The only step that needed care was renaming a column: everything else was additive, so old and new code could run against the same database during the rollout.
```

## Rule added or changed

Added the new-register families (significance compression, therapy voice, performative honesty, stage management, dev-blog boilerplate) and the structural-cadence detectors to `SKILL.md`, with dose-response framing: one hit can be voice, several in one passage is the tell. Deterministic coverage lives in `evals/oracles/slop_lint.py`; earned uses are pinned by `evals/adversarial.json` (`earned-negation-chain-changelog`, `earned-turns-out-with-trace`, `earned-anaphora-invariant-chain`, `holdout-earned-honesty-clarification`) so the flag stays a hypothesis, not a verdict.
