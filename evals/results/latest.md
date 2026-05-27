# Latest eval results

Date: 2026-05-27

The 2026-05-25 smoke run remains the most recent live eval against a fresh subagent context. The 2026-05-27 additions expanded the eval contract (RED) and updated the doctrine to match (GREEN). Live pass rates against the new evals have not yet been recorded; the change has only been validated structurally via `python3 scripts/validate.py`.

## Eval counts

| Eval set | 2026-05-25 | 2026-05-27 | Source |
|---|---:|---:|---|
| Manual regression cases | 5 | 9 | `evals/cases.md` |
| Output evals | 5 | 9 | `evals/evals.json` |
| Adversarial evals | 12 | 15 | `evals/adversarial.json` |
| Rewrite-quality evals | 6 | 9 | `evals/rewrite-evals.json` |
| Eval-suite health evals | 5 | 6 | `evals/meta-evals.json` |
| Trigger queries | 20 | 22 | `evals/trigger-queries.json` |

## Live results (2026-05-25 baseline, unchanged)

| Eval set | Score | Source |
|---|---:|---|
| Manual regression cases | 5/5 cases | `evals/cases.md` |
| Machine-readable output assertions | 15/15 assertions | `evals/evals.json` |
| Adversarial false-positive assertions | 36/36 assertions | `evals/adversarial.json` |
| Rewrite-quality assertions | 19/19 assertions | `evals/rewrite-evals.json` |
| Eval-suite health assertions | 15/15 assertions | `evals/meta-evals.json` |
| Trigger-query label sanity | 20/20 labels | `evals/trigger-queries.json` |

## What changed in the latest enrichment

The 2026-05-27 round added detectors that surfaced from external research (Wikipedia "Signs of AI writing", Antislop paper, linguistic-features surveys):

- copula displacement (`serves as`, `stands as`) and its earned counterpart (enumeration);
- hedged symmetry (`Whether X or Y`, `While X, Y is also important`) and its earned counterpart (real branching conditions);
- outline-shaped conclusion templates (`Despite challenges, X continues to thrive`, `Looking ahead, X will play a pivotal role`);
- decorative em-dash clusters and their earned counterpart (parenthetical/appositive use);
- a `word-list-drift` meta-eval treating high-risk word lists as time-dated detectors.

Full breakdown: `evals/results/2026-05-27-research-additions.md`.

## Assessment

The eval contract now covers patterns the doctrine previously did not address. The doctrine has been updated to match the contract. Live smoke pass rates against a fresh subagent context with the new SKILL.md are the next measurement step.

Remaining gaps: live smoke run against the new evals; observed trigger-rate runs in Pi, Claude Code, Codex, and OpenCode; corpus-level checks for sentiment variance and lexical diversity (flagged in `LESSONS.md` as not testable via per-rewrite assertions).
