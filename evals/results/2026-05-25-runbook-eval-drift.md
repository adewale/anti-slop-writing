# Results — runbook and eval-drift enrichment

Date: 2026-05-25

This run incorporated two external ideas into the project:

- runbooks as bounded, manifest-driven hillclimbing documents;
- eval suites as living systems that can go stale, hit ceiling effects, or reward metric artifacts.

## Scores

| Eval set | Score | Notes |
|---|---:|---|
| Manual regression cases (`evals/cases.md`) | 5/5 cases | Maintained. |
| Output assertions (`evals/evals.json`) | 15/15 assertions | Maintained. |
| Adversarial assertions (`evals/adversarial.json`) | 15/15 assertions | Maintained. |
| Rewrite assertions (`evals/rewrite-evals.json`) | 19/19 assertions | Added `multi-issue-output-manifest`. |
| Meta-eval assertions (`evals/meta-evals.json`) | 15/15 assertions | Added coverage for ceiling effects, metric artifacts, regime shifts, trigger drift, and judge drift. |
| Trigger label sanity (`evals/trigger-queries.json`) | 20/20 labels | Maintained; not an observed client trigger-rate run. |

## Assessment

The project is better covered. The original evals stayed green, while the suite now checks whether the eval process itself is becoming brittle or stale. The runtime skill also gained a final self-check so review tasks are less likely to stop after critique without producing the requested concrete rewrite.

Remaining gap: observed trigger-rate runs in Pi, Claude Code, Codex, and OpenCode.
