# Runbook: hillclimb anti-slop-writing

## Objective

Improve the `anti-slop-writing` skill from a concrete writing failure. The outcome is not a nicer doctrine file; the outcome is a skill that produces a better rewrite on a documented case without regressing existing evals.

Use this runbook when adding a detector, changing the rubric, expanding eval coverage, or updating the skill's runtime instructions.

The acceptance discipline below borrows from the held-out validation, statistical-gating, per-instance-rubric, cross-family-judge, length-control, saturation-stop, Pareto-front, and length-budget patterns documented in `docs/hillclimb-improvements.md`. Read that file once before your first hillclimb session.

## Inputs

- A concrete writing failure or eval gap.
- The current installable skill in `skills/anti-slop-writing/`.
- Repo-only evals in `evals/`, each split into `tune` and `holdout` cases.

## Output manifest

The task is not complete until every applicable artifact exists and is non-empty:

- Updated doctrine or reference file in `skills/anti-slop-writing/` when runtime behavior changes.
- Updated eval file: `evals/evals.json`, `evals/rewrite-evals.json`, `evals/adversarial.json`, `evals/meta-evals.json`, or `evals/trigger-queries.json`. New cases must be marked `split: "tune"` or `split: "holdout"`.
- Failure record in `evals/failures/` when the change comes from a new failure mechanism.
- Rejected-edit entry in `evals/rejected-edits.md` when an attempted change failed an eval and was discarded.
- Before/after card in `examples/cards/` when the pattern should be easy to inspect.
- Lesson entry in `Lessons_learned.md` when doctrine changes.
- Changelog entry in `CHANGELOG.md` when doctrine, eval coverage, compatibility, or contributor workflow changes.
- Eval result note in `evals/results/` when scores are captured.

## The tune/holdout split

Each eval file carries a `split` field per case:

- `tune` — read freely during iteration. Use these to diagnose failures and to write the next doctrine edit.
- `holdout` — scored at end-of-round and at PR merge. **Never edit doctrine in response to a holdout failure.** When a holdout case exposes a gap, write a new failure case (which becomes a `tune` case in the next round) and leave the holdout untouched.

Why: adaptive querying against a fixed eval set inflates apparent improvement (Dwork et al., STOC 2015; Blum & Hardt, ICML 2015). The split is the cheap structural defense; the rule above is what keeps it honest.

## Evaluation criteria

A change passes when all of these are true:

1. The new rule is tied to a concrete failure or eval gap.
2. The eval checks behavior, not just keyword presence.
3. The eval includes at least one assertion with observable evidence.
4. The change does not bloat the installable skill with repo-only machinery.
5. Existing regression, adversarial, rewrite, trigger, and meta-eval checks still pass on both tune and holdout splits.
6. The score-delta gate accepts the change (see "Statistical gating" below).
7. The final answer explains whether results improved, stayed at ceiling, or exposed a gap.

## Iteration loop

Run at most three improvement rounds. Stop earlier if the saturation rule fires.

1. Score the relevant tune evals before the change when comparing results matters. Record per-case scores in JSONL with fields `{id, split, before, after}`.
2. Make the smallest doctrine/eval/doc change that targets the weakest dimension.
3. Run validation.
4. Score the affected tune evals again. Keep the per-case `before` and `after` scores.
5. **Statistical gating**: run `python3 scripts/score_delta.py <results.jsonl>` and require ACCEPT before promoting the change. The script computes a paired bootstrap 95% CI and a sign-flip permutation p-value on per-case deltas; an edit whose CI overlaps zero is within noise and must be REJECTED. Small suites (N < ~30) cannot use CLT-based intervals (Bowyer et al., ICML 2025), which is why the helper avoids them.
6. **Pareto-front carryforward**: keep the best candidate doctrine **per eval case** across rounds, not only the single global best. If round 2 regresses cases that round 1 won, restore the round-1 doctrine for those specific cases when composing the round-3 candidate.
7. If a tune eval fails, fix the smallest cause and repeat. If a holdout eval fails, do not edit doctrine — add a new tune case for the next round and log the rejection in `evals/rejected-edits.md`.
8. **Saturation stop**: stop earlier than 3 rounds when roughly 20 consecutive eval traces yield no new failure category. Most measured prompt-optimization gains land in the first 3-5 iterations (OPRO, GEPA, TextGrad); past that, marginal edits add length without signal.
9. **Length budget**: cap `SKILL.md` word-count growth at +200 words per round. When the cap is exceeded, the round must include a consolidation pass before adding new rules.
10. End-of-round: rerun the **holdout** split with `--holdout-only`. If the holdout CI overlaps zero, the change does not merge; iterate again or stop.
11. If three rounds do not converge, keep the best attempt and flag the unresolved gap for human review.

## Judge protocol

When using LLM-as-judge for any eval (rewrite quality, meta-eval reasoning, dynamic-rubric grading):

- **Cross-family ensemble.** Use at least two judges from different model families (e.g. Claude + GPT, or Claude + an open-source judge). Same-family judging rewards "look more like me" (Panickssery et al., NeurIPS 2024). When judges disagree, flag for human review rather than averaging.
- **Length normalization.** Record candidate length in tokens or words. Either normalize the score by length or apply a length-counterfactual adjustment: a longer candidate may not be preferred over a shorter one unless an orthogonal-axis check confirms the extra length earns its keep. For an anti-slop skill, longer-sounds-better is the slop pattern the skill targets; a length-biased judge rewards exactly the failure the skill is supposed to catch.
- **Orthogonal axes when available.** Use the `graded_dimensions` block on a case rather than a single aggregate score. Single aggregates hide Pareto regressions where a change raises one axis while quietly degrading another (FLASK, ICLR 2024).
- **Dynamic per-instance rubric when present.** For rewrite cases carrying a `dynamic_rubric` block, generate 3-5 case-specific criteria from the brief before grading. Static rubrics on prose tasks reliably collapse to "good cadence wins" (WritingBench reports 84% vs 58% human alignment for dynamic vs static rubrics).
- **Doctrine A/B comparison and rate study.** When the scoring task is comparing two doctrine versions rather than scoring against a fixed suite, use `evals/blinded-eval-harness.md`. It extends the apply-judge separation above with an anonymized A/B label (the judge does not learn which critique came from which doctrine) and a rate-study procedure for behaviors that vary run-to-run. Self-scored A/B inflated results by ~13% in the worked run; the blinded run was the calibrated comparison.

## Common fixes

| Failure | Fix |
|---|---|
| Eval passes on keyword stuffing | Replace keyword assertion with a mechanism or evidence assertion. |
| Skill over-flags concise prose | Add an adversarial eval with an earned version of the pattern. |
| Skill critiques but does not rewrite | Add a rewrite eval requiring concrete output. |
| All evals pass too easily | Add harder cases from the failure corpus or a meta-eval for ceiling effects. |
| Trigger behavior drifts in a client | Add `near-neg-` near-miss trigger negatives and tighten the description boundary. |
| Rule becomes dogmatic | Add a lesson entry with "what not to overgeneralize." |
| Score delta looks good but CI overlaps zero | Reject the edit. Either add more eval cases to reduce the CI or scope the edit narrower. |
| Holdout regression after round 2 | Stop and roll back. Do not edit doctrine to fix a holdout case. |
| Doctrine accreting past +200 words | Run a consolidation pass before any new rule is added. |
| Judges from the same family always agree | Add a cross-family judge or a human spot-check; same-family agreement is not evidence. |

## Between major versions

When cutting a major version, sample new tune cases from real anti-slop usage if available. Static eval sets score 99% on the failure modes that mattered six months ago while users have moved to new ones (the "eval rot" pattern). Refresh inputs from production traces; do not just rerun the existing set.

## Final checklist

Before declaring done:

- [ ] Every applicable output in the manifest exists and is non-empty.
- [ ] `python3 scripts/validate.py` passes.
- [ ] New evals test behavior, not only words.
- [ ] Each new case carries a `split` of `tune` or `holdout`.
- [ ] At least one adversarial or boundary case exists when a rule could overgeneralize.
- [ ] `python3 scripts/score_delta.py <results.jsonl> --holdout-only` returns ACCEPT for the holdout split.
- [ ] If an attempt was rejected, the entry is in `evals/rejected-edits.md`.
- [ ] The README/CONTRIBUTING docs still distinguish installable skill files from repo-only eval machinery.
- [ ] The final report states before scores, after scores on both splits, the score-delta CI, and whether coverage improved.

## Verification script

Run from the repository root:

```bash
python3 scripts/validate.py

test -s skills/anti-slop-writing/SKILL.md
test -s evals/evals.json
test -s evals/rewrite-evals.json
test -s evals/adversarial.json
test -s evals/meta-evals.json
test -s evals/rejected-edits.md
test -s CHANGELOG.md
test -s Lessons_learned.md
test -s docs/hillclimb-improvements.md
test -x scripts/score_delta.py
```
