# Latest eval results

Date: 2026-05-25

These smoke evals were run from fresh subagent context. They check that the skill catches the repo's regression failures, avoids the new adversarial false-positive cases, and satisfies rewrite-quality assertions. They are not a full benchmark with persisted `with_skill/` versus `old_skill/` artifacts or observed multi-run trigger rates.

## Results

| Eval set | Score | Source |
|---|---:|---|
| Manual regression cases | 5/5 cases | `evals/cases.md` |
| Machine-readable output assertions | 15/15 assertions | `evals/evals.json` |
| Adversarial false-positive assertions | 15/15 assertions | `evals/adversarial.json` |
| Rewrite-quality assertions | 15/15 assertions | `evals/rewrite-evals.json` |
| Trigger-query label sanity | 20/20 labels | `evals/trigger-queries.json` |

## What changed in this eval expansion

Before the expansion, the suite already passed the original manual cases, output assertions, and trigger-label checks. The expansion added coverage rather than raising those ceiling scores:

- adversarial examples for earned antithesis, valid technical `robust`, quoted bad phrases, useful concrete lists, and short direct answers;
- rewrite evals that require concrete mechanisms, named relations, and carrier-bound endings;
- a curated failure corpus under `evals/failures/`;
- before/after cards under `examples/cards/`;
- `LESSONS.md` to record what not to overgeneralize;
- `CHANGELOG.md` to track doctrine and eval changes.

## Assessment

The project is better covered. The original eval scores stayed at ceiling, while the new evals add protection against two important regressions: over-flagging good prose and producing critique without a strong rewrite.

Remaining gap: these are smoke evals and label sanity checks. They do not replace observed trigger-rate runs in Pi, Claude Code, Codex, or OpenCode.
