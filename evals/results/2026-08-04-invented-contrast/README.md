# Round plan: hollow modifiers and invented contrasts (2026-08-04)

**Status: pre-registered, not yet run.** No scores exist in this directory. Everything below was written before any output was generated, per `runbooks/hillclimb-skill.md` → Pre-registration. Nothing here may be edited after Phase 0 begins except by appending a `## Deviations` section that says what changed and why.

Source of the hypotheses: [@stanine, 2026-08-03](https://x.com/stanine/status/2084385000959701146), a set of writing instructions addressed to coding agents. Mechanism write-ups in `evals/failures/hollow-modifier-implicature.md` and `evals/failures/invented-contrast-strawman.md`.

## Why this round exists in this shape

The last two times an outside idea was imported — parataxis density (2026-06-13), the stop-slop block (2026-06-14) — it looked like a real gap and measured exactly inert. Both times the doctrine already produced the behavior under a different name. Both times the cost was a full A/B to find out.

So the eval cases landed first, with no doctrine change, and Phase 0 below is a null-first test: assume the doctrine already handles this until the baseline says otherwise. The candidate edit is written out in this file rather than in `SKILL.md`, fixed before any output is generated, so it cannot be reshaped to fit a disappointing result.

## Hypotheses

**H1 — hollow modifiers.** The doctrine does not delete `actual`, `real`, `true`, `key` when they carry no information, because its detectors are built for a different failure. Prestige adjectives inflate the noun and are repaired by naming a mechanism; a hollow modifier says nothing about its noun and is repaired by deletion. Predicted baseline failure: the reviewer keeps the modifier because the surrounding sentence is already concrete, or repairs by adding a mechanism, which grows the line.

**H2 — self-planted strawman.** The staccato contrast test judges a contrast by whether the prior prose evidences both sides. It never asks who introduced the opposing side, so a writer who supplies the opposition themselves can pass at any grade, and none of the three grades prescribes cutting the invented premise. Predicted baseline failure: the reviewer grades the contrast `earned` (the writer's own prior sentence supplies the Docker side) or `compressed` and then repairs by evidencing the Docker build — growing the strawman instead of cutting it.

H2 is the stronger claim and the one worth the round. H1 may well turn out to be covered by `undue significance language` plus the emphasis-source test.

## Case sets

The seven cases partition cleanly by hypothesis, which is what makes separate arms affordable.

| Hypothesis | Suite | Case | Split | Role |
|---|---|---|---|---|
| H1 | `evals.json` | `hollow-modifier-false-implicature` | tune | detection |
| H1 | `rewrite-evals.json` | `hollow-modifier-delete-not-expand` | tune | repair-by-deletion |
| H1 | `adversarial.json` | `substantive-actual-measured-vs-advertised` | tune | guard |
| H1 | `adversarial.json` | `key-issue-earned-by-stated-ranking` | holdout | guard |
| H2 | `evals.json` | `self-planted-strawman-contrast` | holdout | detection |
| H2 | `rewrite-evals.json` | `invented-contrast-cut-the-strawman` | holdout | repair-by-cutting |
| H2 | `adversarial.json` | `negation-answers-the-users-hypothesis` | tune | guard |

Regenerate the executable worklist (`worklist.json` in this directory) with:

```bash
python3 scripts/run_evals.py prepare \
  evals/evals.json evals/rewrite-evals.json evals/adversarial.json \
  --split all --out /tmp/all.json
# then filter to the seven ids above; see the note field in worklist.json
```

## Pre-registration

- **SESOI**: 0.05 on the 0-1 graded scale, matching the 2026-06-14 ablation. Below this, a real effect does not earn the skill length.
- **Arms**: three conditions — `baseline` (current `SKILL.md`), `baseline+H1`, `baseline+H2`. Tested **separately**, not as one block. The 2026-06-14 round bundled two borrowed ideas and got a joint zero, which cannot distinguish "both inert" from "one works, one dilutes." Separate arms also remove the length-dilution confound, where adding two rules degrades attention on cases neither rule targets.
- **N and axes**: baseline runs all 7 cases; `+H1` runs its 4; `+H2` runs its 3. Three models (Opus 5, Sonnet 5, Haiku 4.5) = 21 baseline runs + 12 + 9 = 42 case-runs. This is underpowered for a small true effect and is not pretending otherwise: at N=4 and N=3 per arm, only a large, consistent effect will clear the CI. A null here is an equivalence claim **on these cases only**.
- **Judges**: three-model Claude panel, blinded A/B labels per `evals/blinded-eval-harness.md`, apply and judge separated per `docs/judge-protocol.md`. Unanimity required; any split verdict goes to human review rather than being averaged. Fixed now so a disappointing run cannot be rescued by swapping judges.
- **Known threat to validity**: the panel is single-family, and the skill is drafted with the same family. This is the standing `judge-self-preference` risk and the open cross-family TODO. It is not fixable in this harness; it is recorded, and it makes a *positive* result the one to distrust, since self-preference inflates rather than deflates.
- **Length budget**: the two candidate blocks below total 137 words against the +200/round cap. No consolidation pass required.

## Accept / reject rule, fixed in advance

1. **Pareto veto, checked first.** Any regression on a guard case — `substantive-actual-measured-vs-advertised`, `key-issue-earned-by-stated-ranking`, `negation-answers-the-users-hypothesis` — rejects that arm outright, regardless of mean delta. A rule that catches strawmen by banning negation has made the skill worse. This veto is not tradeable against a good aggregate.
2. **Then the gate.** `python3 scripts/score_delta.py <delta.jsonl>` must return ACCEPT for the arm to reach `SKILL.md`.
3. **Then the holdout.** `--holdout-only` must also ACCEPT. H2's detection and repair cases are both holdout, so H2 cannot be accepted on tune evidence alone. If H2's holdout fails, no doctrine edit — write a fresh tune case for the next round and leave the holdout untouched.
4. **On a zero.** Run `python3 scripts/saturation_index.py <scores.jsonl>` before believing it. Then run `score_delta.py --sesoi 0.05` and report EQUIVALENT or NOT SHOWN. A bare REJECT means "no improvement detected", not "no effect" (`docs/eval-null-result-literature.md`).

## Phase 0 — baseline probe (do this first)

Run the `baseline` arm on the four **tune** cases only, three models, before touching the candidate text. The holdout cases stay sealed.

Decision rule, pre-committed:

- **If baseline passes all four tune cases with unanimous panel agreement** → the doctrine already does this. Stop. No doctrine edit. The seven cases become regression coverage, a `Lessons_learned.md` entry records "already covered, third time", and the round is written up as a null. Do not proceed to Round 1.
- **If baseline fails `hollow-modifier-*` but passes the H2 tune case** → run the `+H1` arm only.
- **If baseline fails the H2 tune case** → run the `+H2` arm. This is the outcome the round is designed for.

Record which of the three predicted failure modes actually appears; "kept the modifier because the sentence was concrete" and "repaired by adding a mechanism" are different failures and imply different edits.

## Candidate doctrine edits (fixed text — do not revise mid-round)

**H1**, appended to the `Words to review` section of `SKILL.md` (62 words):

```txt
Hollow modifiers: actual, real, true, genuine, honest, clear, main, key, important. Delete when removal leaves the meaning unchanged. Unlike prestige adjectives these say nothing about their noun; they assert a contrast with alternatives the reader was never given. Repair by deletion, not by naming a mechanism. Keep when the alternative is on the page: a measured figure against a stated advertised one, or a ranking among enumerated items whose criterion is given.
```

**H2**, appended to the `Staccato contrast test` section (75 words):

```txt
Provenance check, before classifying: ask who introduced the opposing side. If the writer supplied it themselves and no one raised it, the contrast is invented — cut the premise rather than evidencing it, and do not grade it earned because the writer's own prior sentence supplies that side. When drafting a reply, the alternatives that count as raised are the ones in the user's message; the surrounding prose cannot settle this, because the writer controls it.
```

The H2 block is deliberately placed *before* the earned/compressed/decorative classification rather than beside it. The defect is not a fourth category of contrast; it is a precondition on the whole test, and a rule that reads as a fourth category will be applied after the classification has already gone wrong.

## Outputs this round must produce

- `scores.jsonl` — per-case scores from `run_evals.py grade --include-graded`.
- `delta.jsonl` — `run_evals.py join --before baseline.jsonl --after <arm>.jsonl`.
- `gate-output.txt` — captured `score_delta.py` output, including the `--sesoi 0.05` verdict on any null.
- `saturation.txt` — captured `saturation_index.py` output.
- `run-metadata.json` — model ids and versions for apply and judge, per the 2026-06-13 precedent.
- On ACCEPT: the `SKILL.md` edit, a `Lessons_learned.md` entry, a `CHANGELOG.md` entry.
- On REJECT: an `evals/rejected-edits.md` entry with the quoted evidence, and the cases stay as regression coverage.

## Amendments (before Phase 0, no output generated yet)

**A1 — Phase 0 could not have tested H2.** As first written, the four tune cases gave H2 exactly one: `negation-answers-the-users-hypothesis`, which is a *guard* (keep the negation the user raised). Baseline was always going to pass it, and the pre-committed stop rule would then have closed H2 as a null without testing H2's claim at all — the detection and repair cases are both holdout and sealed. The rule was self-defeating, not conservative.

Fix: added `evals/evals.json` → `self-planted-strawman-tune` (tune), a detection case with the same shape as the sealed holdout but different content (a bigger-instance strawman in answer to an index question). Writing a fresh tune case before any scoring is allowed; the holdout stays sealed. Phase 0 now runs **five** tune cases and can decide both hypotheses.

**A2 — how the panel is operationalized.** "Three-model Claude panel" in the Pre-registration section is ambiguous between *grade every output three times* and *escalate to three judges on disagreement*. Fixed as the latter, following the 2026-06-14 precedent where only the differing pairs were re-judged by all three families. The apply axis carries the three models; the judge is **fixed at Opus** across that axis so scores stay comparable and the apply model is the only variable. A case escalates to the full three-judge panel when the three apply models disagree on the case outcome, or when any judgment is a borderline pass. Grading every output three times with a fixed judge set would not have added information, only cost.

Neither amendment touches the SESOI, the arms, the accept/reject rule, or the candidate doctrine blocks.

## Not in scope

- **Trigger queries.** Activation does not change. The tweet is an agent instructing itself mid-draft, which is a usage mode rather than a routing decision, and `evals/trigger-queries.json` measures routing.
- **A `references/` teaching section.** If H2 is rejected as inert but the distinction still reads as useful, that is the 2026-06-13 parataxis outcome: reference-only prose, not gated runtime behavior. Decide after the gate, not before.
