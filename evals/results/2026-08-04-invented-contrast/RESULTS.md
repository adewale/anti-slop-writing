# Results: Phase 0 baseline, 2026-08-04 (both hypotheses rejected)

Plan and pre-registration: `README.md` in this directory. Phase 0 ran exactly as pre-registered, the stop rule fired, and **no doctrine edit was made**. No treatment arm was built, so no `score_delta.py` gate was run — there is no before/after pair to gate. That is the designed outcome of a null-first Phase 0, not a skipped step.

Round scope: `SKILL.md` unchanged. Holdout cases never unsealed.

## Scores

Baseline doctrine, five tune cases, three apply models, judge fixed at Opus.

| case | hypothesis | opus | sonnet | haiku | graded (o/s/h) |
|---|---|---:|---:|---:|---|
| `hollow-modifier-false-implicature` | H1 | 1.00 | 1.00 | **0.75** | 1.00 / 0.97 / 0.77 |
| `hollow-modifier-delete-not-expand` | H1 | 1.00 | 1.00 | 1.00 | 1.00 / 0.97 / 1.00 |
| `substantive-actual-measured-vs-advertised` | H1 guard | 1.00 | 1.00 | 1.00 | 1.00 / 1.00 / 1.00 |
| `self-planted-strawman-tune` | H2 | 1.00 | 1.00 | 1.00 | 1.00 / 1.00 / 1.00 |
| `negation-answers-the-users-hypothesis` | H2 guard | 1.00 | 1.00 | 1.00 | 1.00 / 1.00 / 1.00 |

Binary mean 0.9833 (n=15), graded mean 0.9800. Saturation index 0.800 binary / 0.600 graded — `self-planted-strawman-tune` and both guards are flat at CEILING across the model axis.

Both adversarial guards returned `keep` on all three models, with the right justification named rather than guessed: the advertised 40 ms p99 in the prior paragraph, and the user's own memory-leak hypothesis.

## H2 is rejected, and my reasoning for it was wrong

The prediction in `README.md` was that baseline would grade the self-planted strawman `earned` (the writer's own prior sentence supplies the opposing side) or `compressed` (and then repair by evidencing that side, growing the strawman). Neither happened on any model. All three classified it **decorative** and cut the invented premise.

The reason is the thing my textual analysis missed. I read `both sides of the contrast are evidenced in the prior sentences` as scoping to the passage under review, which the writer controls. The models read it as scoping to what was actually established — and in a reply, that means what the user said. Opus, unprompted:

> The staccato contrast test classifies this as decorative: neither side is evidenced by anything the user said.

and its closing line:

> Deleting the first two sentences loses nothing, because the writer supplied the opponent.

That is the whole H2 candidate rule, produced by the doctrine as it already stands, without the word "provenance" appearing anywhere in `SKILL.md`. Haiku got there too, naming it a "self-planted strawman" and writing "defeating an argument nobody made." The ambiguity I identified on the page is real; it is not an ambiguity in practice.

This is the third consecutive time an outside idea looked like a gap and measured inert, and the second time (after parataxis) where the mechanism was already reachable under a different name. It is also the first time the failure was in my *analysis* rather than in the measurement: I predicted a specific misgrade, named the exact line that would cause it, and the models did not make it. Reading a rule adversarially is not the same as observing how it is applied.

## H1 is rejected, with one real observation kept

Detection is at ceiling: `implicature-naming` scored 5 on all three models. Every model flagged `actual`/`real`/`key`, applied the deletion test, and named the false implication about alternatives the reader was never given. The existing `undue significance language` detector plus the emphasis-source test already cover this; the candidate word-list block adds nothing to detection.

The one genuine miss is narrower than the hypothesis. On `hollow-modifier-false-implicature`, haiku repaired `The key issue is deciding who owns the rollback` as `Deciding who owns the rollback is the remaining blocker` — substituting `remaining` into the slot `key` vacated. Escalated to the full three-judge panel per amendment A2 (the apply models disagreed on the case outcome). The panel was **unanimous 3/3 that assertion 4 fails**, so this is a real substitution, not judge noise.

It is a repair-purity failure on the weakest model, not a detection gap, and it is a single observation. `Lessons_learned.md` → "A variance gap is not a doctrine gap" applies directly: one miss can be run-to-run variance, and the fix is a rate study before any doctrine text. Recorded as a follow-up in `TODO.md`, not as support for the candidate block — which is the move that lesson exists to prevent.

## What the cases are worth now

Regression coverage, and that is not nothing. Four of five sit at ceiling across the model axis, so a future zero on them is no-regression evidence only, per `saturation_index.py`'s own warning. The two guards are the durable part: they pin the boundary against a future edit that catches strawmen by banning negation, or hollow modifiers by banning `key`. That is the same defensive value the 2026-06-14 round kept out of an otherwise null result.

The two sealed holdout cases (`self-planted-strawman-contrast`, `invented-contrast-cut-the-strawman`) were not scored and stay sealed for a future round.

## Threats to validity

- **Single-family panel.** Apply and judge are both Claude, so self-preference is undiluted (`docs/judge-protocol.md`; the standing cross-family TODO). This cuts the right way for a null: self-preference inflates scores, and inflation cannot manufacture a rejection of a doctrine edit that was never applied. A positive result here would have needed heavy discounting; this one does not.
- **N is small.** Five cases, three models. The round was never powered to detect a small effect, and it did not need to be: the question was whether baseline already produces the behavior, and it does, at ceiling, on the decisive case.
- **Ceiling.** Four of five cases cannot separate a good doctrine from a merely compliant one. Any future round that wants to move these needs harder cases, not more runs.

## Artifacts

```
phase0-baseline/
  apply-prompts.json          assertions stripped; what the apply agents saw
  judge-prompts.json          what the judges saw
  run-metadata.json           models, judge policy, stated limitations
  {opus,sonnet,haiku}/
    outputs/<suite>/<id>.md   15 skill-applied outputs
    judgments/*.jsonl         per-assertion verdicts with quoted evidence
    scores.jsonl              binary
    scores-with-graded.jsonl  binary + normalized 1-5 dimensions
  panel/                      3-judge escalation on the disputed case
  combined-scores*.jsonl      model axis merged, input to saturation_index.py
  saturation.txt              captured saturation output
```
