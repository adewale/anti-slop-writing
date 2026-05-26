# Runbook: hillclimb anti-slop-writing

## Objective

Improve the `anti-slop-writing` skill from a concrete writing failure. The outcome is not a nicer doctrine file; the outcome is a skill that produces a better rewrite on a documented case without regressing existing evals.

Use this runbook when adding a detector, changing the rubric, expanding eval coverage, or updating the skill's runtime instructions.

## Inputs

- A concrete writing failure or eval gap.
- The current installable skill in `skills/anti-slop-writing/`.
- Repo-only evals in `evals/`.

## Output manifest

The task is not complete until every applicable artifact exists and is non-empty:

- Updated doctrine or reference file in `skills/anti-slop-writing/` when runtime behavior changes.
- Updated eval file: `evals/evals.json`, `evals/rewrite-evals.json`, `evals/adversarial.json`, `evals/meta-evals.json`, or `evals/trigger-queries.json`.
- Failure record in `evals/failures/` when the change comes from a new failure mechanism.
- Before/after card in `examples/cards/` when the pattern should be easy to inspect.
- Lesson entry in `LESSONS.md` when doctrine changes.
- Changelog entry in `CHANGELOG.md` when doctrine, eval coverage, compatibility, or contributor workflow changes.
- Eval result note in `evals/results/` when scores are captured.

## Evaluation criteria

A change passes when all of these are true:

1. The new rule is tied to a concrete failure or eval gap.
2. The eval checks behavior, not just keyword presence.
3. The eval includes at least one assertion with observable evidence.
4. The change does not bloat the installable skill with repo-only machinery.
5. Existing regression, adversarial, rewrite, trigger, and meta-eval checks still pass.
6. The final answer explains whether results improved, stayed at ceiling, or exposed a gap.

## Iteration loop

Run at most three improvement rounds.

1. Score the relevant evals before the change when comparing results matters.
2. Make the smallest doctrine/eval/doc change that targets the weakest dimension.
3. Run validation.
4. Score the affected evals again.
5. If an eval fails, fix the smallest cause and repeat.
6. If three rounds do not converge, keep the best attempt and flag the unresolved gap for human review.

## Common fixes

| Failure | Fix |
|---|---|
| Eval passes on keyword stuffing | Replace keyword assertion with a mechanism or evidence assertion. |
| Skill over-flags concise prose | Add an adversarial eval with an earned version of the pattern. |
| Skill critiques but does not rewrite | Add a rewrite eval requiring concrete output. |
| All evals pass too easily | Add harder cases from the failure corpus or a meta-eval for ceiling effects. |
| Trigger behavior drifts in a client | Add near-miss trigger negatives and tighten the description boundary. |
| Rule becomes dogmatic | Add a lesson entry with “what not to overgeneralize.” |

## Final checklist

Before declaring done:

- [ ] Every applicable output in the manifest exists and is non-empty.
- [ ] `python3 scripts/validate.py` passes.
- [ ] New evals test behavior, not only words.
- [ ] At least one adversarial or boundary case exists when a rule could overgeneralize.
- [ ] The README/CONTRIBUTING docs still distinguish installable skill files from repo-only eval machinery.
- [ ] The final report states before scores, after scores, and whether coverage improved.

## Verification script

Run from the repository root:

```bash
python3 scripts/validate.py

test -s skills/anti-slop-writing/SKILL.md
test -s evals/evals.json
test -s evals/rewrite-evals.json
test -s evals/adversarial.json
test -s evals/meta-evals.json
test -s CHANGELOG.md
test -s LESSONS.md
```
