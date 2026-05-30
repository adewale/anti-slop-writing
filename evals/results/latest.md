# Latest eval results

Date: 2026-05-29

These smoke evals check that the skill catches the repo's regression failures, avoids adversarial false-positive cases, satisfies rewrite-quality assertions, notices eval-suite health problems such as ceiling effects and metric artifacts, and triggers correctly on prose-edit queries while declining on adjacent non-prose ones. They are not a full benchmark with persisted `with_skill/` versus `old_skill/` artifacts or observed multi-run trigger rates.

This iteration is an infrastructure update only; doctrine in `skills/anti-slop-writing/` did not change. Scores below are the pre-change baseline for the new holdout cases — they need to be rerun against an actual skill execution to populate real numbers. Until then, treat the holdout counts as the new measurement surface, not as scored results.

## Schema changes

| Suite | Old count | New tune count | New holdout count |
|---|---:|---:|---:|
| `evals/evals.json` | 5 | 5 | 3 |
| `evals/adversarial.json` | 12 | 12 | 3 |
| `evals/rewrite-evals.json` | 6 | 6 | 2 |
| `evals/meta-evals.json` | 5 | 5 | 2 |
| `evals/trigger-queries.json` | 20 | 16 | 10 |

Six new `near-neg-` near-miss negatives were added to `trigger-queries.json` (fact-check, link-check, draft-from-bullets, storyboard, slide-export, docx-from-dataset). The docx case is taken from a real production bug, [anthropics/claude-code#43259](https://github.com/anthropics/claude-code/issues/43259).

## Held-out and rewrite-eval additions

- `evals/evals.json` holdout: `fake-precision-unnamed-source`, `stacked-rule-of-three`, `abstract-system-noun-stack`.
- `evals/adversarial.json` holdout: `earned-importance-immediate-mechanism`, `cost-benefit-not-just-earning-the-contrast`, `research-methods-staccato`.
- `evals/rewrite-evals.json` holdout: `fake-precision-rewrite-finance`, `product-tour-rewrite-developer-tools` — both with `dynamic_rubric` and `graded_dimensions`.
- `evals/meta-evals.json` holdout: `noise-vs-signal-on-small-suite`, `judge-self-preference`.

## What changed in the infrastructure

- Tune/holdout split on every eval suite.
- `scripts/score_delta.py` for paired-bootstrap + sign-flip-permutation accept/reject gating.
- `dynamic_rubric` and `graded_dimensions` schema fields on rewrite cases.
- `evals/rejected-edits.md` graveyard for previously rejected edits.
- `runbooks/hillclimb-skill.md` rewritten with held-out gate, judge protocol, saturation stop, Pareto-front carryforward, length budget, and eval-rot refresh policy.
- `docs/hillclimb-improvements.md` with sources for each change.

## Assessment

The project's iteration loop now has the structural defenses the field treats as standard (Dwork et al. on adaptive overfitting; Blum & Hardt's ladder mechanism; Miller and Bowyer on small-sample CIs). The remaining gap is the same one called out in the previous results note: observed multi-run trigger rates in Pi, Claude Code, Codex, and OpenCode, and end-to-end scored runs of the new holdout cases against an actual skill execution.

## Doctrine change retained on qualitative evidence

The emphasis-source and syntax-relation tests in `SKILL.md` were added (procedural wording) as part of the emphasis-source experiment described in `evals/results/2026-05-27-emphasis-source-experiment.md`. Five new eval cases were added with proper splits (`borrowed-emphasis`, `paragraph-scale-borrowed-emphasis`, `emphasis-source-flatten` as tune; `earned-emphasis-from-idea`, `earned-paragraph-escalation` as holdout).

Under the new statistical gate (`scripts/score_delta.py`), the experiment's headline score claim does not clear the noise floor at N=5: bootstrap 95% CI `[+0.0000, +0.1998]`, sign-flip p=1.0, verdict REJECT. Per-case scores are in `evals/results/2026-05-28-emphasis-source-procedural/scores.jsonl`.

The change is retained on qualitative behavioral evidence (the procedural agent reliably produces the flatten artifact in its critique; the labeled agent does not), not as a gated score improvement. The blinded harness used to surface that observation is `evals/blinded-eval-harness.md`.

## Previous results

| Date | File |
|---|---|
| 2026-05-25 | `2026-05-25-before.md`, `2026-05-25-after.md`, `2026-05-25-adversarial-expansion.md`, `2026-05-25-runbook-eval-drift.md` |
| 2026-05-27 | `2026-05-27-emphasis-source-experiment.md` |
| 2026-05-28 | `2026-05-28-emphasis-source-procedural/` (per-case scores) |
