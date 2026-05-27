# Eval results — research-driven detector additions

Date: 2026-05-27

## What changed

External research on AI-writing tells (Wikipedia "Signs of AI writing", the Antislop paper, recent linguistic surveys) surfaced patterns the doctrine did not yet cover. The change followed a TDD sequence: the eval contract was added first, then the doctrine was updated to satisfy it.

### New evals (RED step)

- `evals/evals.json`: `copula-displacement`, `hedged-symmetry`, `outline-conclusion-template`, `em-dash-cluster`
- `evals/adversarial.json`: `serves-as-enumeration`, `branching-condition-symmetry`, `em-dash-earned`
- `evals/rewrite-evals.json`: `copula-displacement-to-is`, `hedged-symmetry-commit`, `outline-conclusion-carrier-bound`
- `evals/meta-evals.json`: `word-list-drift`
- `evals/trigger-queries.json`: `neg-em-dash-mechanical`, `pos-hedged-symmetry`
- `evals/cases.md`: cases 6 (copula displacement), 7 (hedged symmetry), 8 (outline conclusion), 9 (em-dash cluster)

### Doctrine updates (GREEN step)

- `skills/anti-slop-writing/SKILL.md`: added detectors for copula displacement, hedged symmetry, em-dash cadence; expanded the conclusion test with outline templates; added editing-pass steps 15-18; added the new templates to banned phrases and the displaced verbs to the words list; added a note that the lists are time-dated.
- `skills/anti-slop-writing/references/anti-slop-writing-doctrine.md`: mirror of the SKILL.md additions plus longer-form explanation, kept/earned examples, and the Antislop frequency-baseline note.
- `LESSONS.md`: five new entries dated 2026-05-27 covering each new pattern plus the word-list-drift lesson.
- `CHANGELOG.md`: Unreleased entries describe the eval, doctrine, and docs additions.

## Counts

| File | Before | After | Delta |
|---|---:|---:|---:|
| `evals/evals.json` | 5 evals | 9 evals | +4 |
| `evals/adversarial.json` | 12 evals | 15 evals | +3 |
| `evals/rewrite-evals.json` | 6 evals | 9 evals | +3 |
| `evals/meta-evals.json` | 5 evals | 6 evals | +1 |
| `evals/trigger-queries.json` | 20 queries | 22 queries | +2 |
| `evals/cases.md` | 5 cases | 9 cases | +4 |

## What is and is not measured here

`python3 scripts/validate.py` checks repo structure, JSON validity, required SKILL.md phrases, required reference files, eval-file minimum counts, and trigger-query positive/negative balance. It does not run the evals against a model. Validation is green after both phases.

Observed pass rates against a fresh subagent context, with quoted evidence for each assertion, are the next measurement step and are not captured here. The doctrine now codifies behavior matching each new assertion, but the assertion that the skill actually produces that behavior in a live run requires a fresh smoke eval.

## Source attribution

The new detectors trace to specific external findings:

- Copula displacement: Wikipedia "Signs of AI writing", section on avoidance of simple copulas.
- Hedged symmetry: Charlie Guo's "Field Guide to AI Slop"; Riedman Report (10 tells).
- Outline-shaped conclusions: Wikipedia "Signs of AI writing", section on outline-like conclusions.
- Em-dash nuance: Rolling Stone, languagehat, SALT.agency (defending em-dash use); The Conversation (caveat that em-dash is contested).
- Word-list drift / Antislop frequency baseline: Antislop paper (OpenReview, 2025), 1,000× frequency claim.

## Remaining gaps

- Sentiment-variance and lexical-diversity tells from the linguistic-features literature are not directly testable as per-rewrite JSON assertions; they need a corpus-level script. Flagged in `LESSONS.md` for future work, not added as evals.
- A live smoke eval against a fresh subagent context with the new doctrine has not yet been recorded.
