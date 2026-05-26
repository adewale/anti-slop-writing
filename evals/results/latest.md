# Latest eval results

Date: 2026-05-25

These smoke evals were run from fresh subagent context. They check that the skill catches the repo's regression failures, avoids adversarial false-positive cases, satisfies rewrite-quality assertions, and notices eval-suite health problems such as ceiling effects and metric artifacts. They are not a full benchmark with persisted `with_skill/` versus `old_skill/` artifacts or observed multi-run trigger rates.

## Results

| Eval set | Score | Source |
|---|---:|---|
| Manual regression cases | 5/5 cases | `evals/cases.md` |
| Machine-readable output assertions | 15/15 assertions | `evals/evals.json` |
| Adversarial false-positive assertions | 36/36 assertions | `evals/adversarial.json` |
| Rewrite-quality assertions | 19/19 assertions | `evals/rewrite-evals.json` |
| Eval-suite health assertions | 15/15 assertions | `evals/meta-evals.json` |
| Trigger-query label sanity | 20/20 labels | `evals/trigger-queries.json` |

## What changed in the latest enrichment

The adversarial expansion added cases for:

- exact `not just X but Y` distinctions;
- controlled-variable staccato;
- concrete comparison tables;
- legitimate three-step operational sequences;
- direct warnings with destructive consequences;
- source-backed use of `highlights`;
- concise imperative runbook steps.

## Assessment

The project is better covered. The adversarial suite now protects against overcorrecting prose that is concise, technical, quoted, structured, or contextually earned.

Remaining gap: observed trigger-rate runs in Pi, Claude Code, Codex, and OpenCode.
