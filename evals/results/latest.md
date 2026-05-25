# Latest eval results

Date: 2026-05-25
Skill version: current `skills/anti-slop-writing/SKILL.md` behavior; later README/contributor-doc edits do not change the evaluated doctrine.

These smoke evals were run from fresh subagent context. They check that the skill catches the repo's regression failures and satisfies the assertion set. They are not a full benchmark with persisted `with_skill/` versus `old_skill/` artifacts or observed multi-run trigger rates.

## Original manual evals

Source: `evals/cases.md`

Result: **5/5 pass**

| Case | Result | Evidence |
|---|---:|---|
| generic importance | PASS | Flags “underscores the importance” and requires a concrete durable-execution mechanism. |
| decorative contrast | PASS | Does not ban contrast; classifies compressed/decorative antithesis and rewrites the relation. |
| weak conclusion | PASS | Identifies the accurate-but-generic ending and returns to the pelican carrier. |
| product-tour flow | PASS | Catches list/product-tour flow and adds a level-of-detail hinge. |
| safe essay voice | PASS | Flags landscape/robust/empower/seamless and requires concrete actor/action/result. |

## Machine-readable output evals

Source: `evals/evals.json`

Result: **15/15 assertions pass**

| Eval | Assertions |
|---|---:|
| `generic-importance` | 3/3 |
| `decorative-contrast` | 3/3 |
| `weak-conclusion` | 3/3 |
| `product-tour-flow` | 3/3 |
| `safe-essay-voice` | 3/3 |

## Trigger-query sanity check

Source: `evals/trigger-queries.json`

Result: **20/20 labels pass**

| Group | Result |
|---|---:|
| should trigger | 10/10 |
| should not trigger | 10/10 |

This was a description/label sanity check: a fresh evaluator judged whether each query should activate the skill from the `SKILL.md` frontmatter description. It does not replace an observed trigger-rate run in Pi, Claude Code, Codex, or OpenCode.
