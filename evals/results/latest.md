# Latest eval results

Date: 2026-05-25

These smoke evals were run from fresh subagent context. They check that the skill catches the repo's regression failures, avoids adversarial false-positive cases, satisfies rewrite-quality assertions, and notices eval-suite health problems such as ceiling effects and metric artifacts. They are not a full benchmark with persisted `with_skill/` versus `old_skill/` artifacts or observed multi-run trigger rates.

## Results

| Eval set | Score | Source |
|---|---:|---|
| Manual regression cases | 5/5 cases | `evals/cases.md` |
| Machine-readable output assertions | 15/15 assertions | `evals/evals.json` |
| Adversarial false-positive assertions | 15/15 assertions | `evals/adversarial.json` |
| Rewrite-quality assertions | 19/19 assertions | `evals/rewrite-evals.json` |
| Eval-suite health assertions | 15/15 assertions | `evals/meta-evals.json` |
| Trigger-query label sanity | 20/20 labels | `evals/trigger-queries.json` |

## What changed in the latest enrichment

The runbook and eval-drift pass added:

- `runbooks/hillclimb-skill.md` so multi-artifact changes have an output manifest, bounded iteration loop, and final verification check;
- `evals/meta-evals.json` for ceiling effects, metric artifacts, new failure modes, trigger drift, and judge drift;
- one rewrite eval that checks whether the skill handles every requested input instead of stopping after a summary;
- a final self-check in `SKILL.md` so high-stakes edits get one bounded judge-refine pass.

## Assessment

The project is better covered. The original eval scores stayed at ceiling, while the new evals add protection against three important regressions: over-flagging good prose, producing critique without a concrete rewrite, and letting the eval suite become stale while all checks pass.

Remaining gap: observed trigger-rate runs in Pi, Claude Code, Codex, and OpenCode.
