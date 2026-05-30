# Eval and runbook notes

These notes record the outside ideas that now shape the repo's improvement loop.

## Runbooks for hillclimbing

Source: Jonathan Lebensold, “Runbooks: what agents need to hill-climb” (`https://lebensold.substack.com/p/runbooks-what-agents-need-to-hill`).

Applied idea: a skill-improvement task needs more than a loose instruction and less than a fixed workflow. The repo now has `runbooks/hillclimb-skill.md`, which names:

- the outcome to achieve;
- the output manifest that must exist before the task is done;
- evaluation criteria;
- a bounded judge-refine-rejudge loop;
- common fixes;
- a final checklist and verification commands.

The useful mechanism is not “write more process.” It is preventing premature completion: an agent should not stop after updating one file if the eval, lesson, changelog, and failure corpus also need to change.

## Evals that can break

Source: Lun Wang, “Your Evals Will Break and You Won't See It Coming” (`https://wanglun1996.github.io/blog/your-evals-will-break.html`).

Applied idea: a passing eval suite can still be stale. The repo now treats all-pass scores as a coverage signal, not proof that the skill is finished.

Concrete changes:

- `evals/meta-evals.json` checks for ceiling effects, metric artifacts, trigger drift, judge drift, and new failure modes.
- `evals/rewrite-evals.json` separates rewrite quality from critique labeling.
- `evals/adversarial.json` checks false positives and overgeneralization.
- `Lessons_learned.md` records what not to overgeneralize.

The practical test is whether a new model could pass the old evals while failing in a new way. If yes, add a meta-eval or failure-corpus entry before changing doctrine.

## Held-out validation and statistical gating

Source: deep research summarized in `docs/hillclimb-improvements.md`, drawing on Dwork, Feldman, Hardt, Pitassi, Reingold, Roth, *Preserving Statistical Validity in Adaptive Data Analysis* (STOC 2015, arXiv 1411.2664), Blum & Hardt, *The Ladder* (ICML 2015), Miller, *Adding Error Bars to Evals* (Anthropic, arXiv 2411.00640), and Bowyer, Aitchison, Ivanova, *Don't Use the CLT in LLM Evals* (ICML 2025 Spotlight, arXiv 2503.01747). Practitioner precedent: Anthropic Skill Creator (60/40 train/holdout, select by held-out score) and LangChain *Better Harness: A Recipe for Harness Hill-Climbing with Evals* (Apr 2026).

Applied idea: a fixed eval set queried adaptively cannot bound generalization without structural defenses. The repo now uses two:

- A per-case `split: "tune" | "holdout"` field on every eval file. Doctrine is iterated only against `tune`; `holdout` is scored at end-of-round and at merge, and never used to drive a doctrine edit.
- `scripts/score_delta.py`: paired-bootstrap CI plus sign-flip permutation test on per-case score deltas. Required ACCEPT on the holdout split before merge.

## Why prose-quality judges need extra guardrails

Source: WritingBench (arXiv 2503.05244) reports 84% human alignment with per-instance dynamic rubrics vs 58% with static rubrics; Wu & Aji *Style Over Substance* (arXiv 2307.03025), Dubois et al. *Length-Controlled AlpacaEval* (arXiv 2404.04475), and Panickssery et al. *LLM Evaluators Recognize and Favor Their Own Generations* (NeurIPS 2024, arXiv 2404.13076) document specific judge biases. FLASK (ICLR 2024, arXiv 2307.10928) shows single aggregate scores hide Pareto regressions.

Applied idea: the judge layer is the weakest link in any prose hillclimb. The runbook's judge protocol now requires a cross-family ensemble, length normalization, orthogonal `graded_dimensions`, and a per-instance `dynamic_rubric` where the eval supplies one.

## The "first systematic controllable text-space optimizer for agent skills"

Source: SkillOpt (arXiv 2605.23904, May 2026) and its closest neighbors — ACE (Stanford/SambaNova, arXiv 2510.04618), GEPA (arXiv 2507.19457, ICLR 2026 Oral), and Voyager's skill library (arXiv 2305.16291). Documented in this repo's deep-research synthesis.

Applied idea: the field is converging on iterative doctrine editing with validation gates and rejected-edit memory. This repo runs the loop manually, but adopts the discipline: bounded edits, held-out gate, rejected-edit graveyard (`evals/rejected-edits.md`), Pareto-front carryforward across iterations, and a length budget to prevent doctrine bloat.
