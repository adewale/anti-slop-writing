# Procedural emphasis-source — per-case scores

Date: 2026-05-28 (rebased onto the new hillclimb protocol 2026-05-30).

Per-case scores for Round 5 of the emphasis-source experiment described in `evals/results/2026-05-27-emphasis-source-experiment.md`. The five cases are the ones added in commit `d18c503` ("Add procedural emphasis-source/syntax-relation tests and five eval cases").

- `before` is the labeled-doctrine score (the version with the tests phrased as labels).
- `after` is the procedural-doctrine score (the version with the tests phrased as procedures that name the artifact the agent must produce).

Each score is the fraction of binary assertions passed in the case (3 assertions per case, so values are 0, 1/3, 2/3, or 1).

## Gate disposition

```
$ python3 scripts/score_delta.py evals/results/2026-05-28-emphasis-source-procedural/scores.jsonl
Cases: 5    Mean delta: +0.0666    95% CI: [+0.0000, +0.1998]    Sign-flip p: 1.0000
Verdict: REJECT (CI overlaps zero; delta is within noise).
```

Both the all-cases run and the `--holdout-only` run reject the change at N=5. The qualitative behavioral observation (procedural agent writes the flatten artifact, labeled agent does not) is recorded in the experiment write-up but is not a score claim.

Scoring methodology: blinded three-agent A/B in `evals/blinded-eval-harness.md`. Round 5 used the cleaned `C3.A2` and `C5.A2` assertions that test the underlying judgment rather than requiring the agent to invoke a named test.
