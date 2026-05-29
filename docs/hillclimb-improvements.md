# Hillclimb improvements

This file documents the thirteen changes made to the eval and runbook machinery, why each one was added, and the source that motivated it. The changes do not modify skill doctrine. They tighten the loop that decides whether a doctrine change actually helped.

The motivating problem: the existing `runbooks/hillclimb-skill.md` had no held-out validation split, no statistical acceptance gate, and used static rubrics on a small fixed eval set. Each of those is a known failure mode of iterative LLM improvement. Sources are cited inline below.

## Tier S — adopt first

### 1. Held-out validation split

Each eval file now carries a `split` field per case: `tune` (used to diagnose and iterate) or `holdout` (scored at the end of a round and at PR merge, never used to write doctrine). The split is roughly 60/40 tune/holdout on each suite.

The rule: never write a doctrine change in response to a holdout failure. Write a new failure case for the next round instead. A holdout failure that drives a doctrine change converts the holdout back into a tune case and defeats the purpose of the split.

Source: Dwork, Feldman, Hardt, Pitassi, Reingold, Roth, *Preserving Statistical Validity in Adaptive Data Analysis* ([STOC 2015, arXiv 1411.2664](https://arxiv.org/abs/1411.2664)); the companion *Reusable holdout* in [Science 2015](https://www.science.org/doi/10.1126/science.aaa9375). Practitioner precedent: [Anthropic Skill Creator](https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md) (60/40 split, select by held-out score) and [LangChain Better Harness](https://www.langchain.com/blog/better-harness-a-recipe-for-harness-hill-climbing-with-evals).

### 2. Statistical gating before accepting an edit

Added `scripts/score_delta.py` for paired bootstrap and beta-binomial CIs on accept/reject decisions. The runbook now requires running it for any close call: if the CI on the score delta overlaps zero, the edit is not accepted.

The default test is a sign-flip permutation on per-case deltas; with N ≤ 20 cases per suite, CLT-based standard errors are dramatically too tight, so the helper avoids them.

Source: Miller, *Adding Error Bars to Evals* (Anthropic, [arXiv 2411.00640](https://arxiv.org/abs/2411.00640), Nov 2024); Bowyer, Aitchison, Ivanova, *Don't Use the CLT in LLM Evals With Fewer Than a Few Hundred Datapoints* ([ICML 2025 Spotlight, arXiv 2503.01747](https://arxiv.org/abs/2503.01747)). Acceptance-gate precedent: Blum & Hardt, *The Ladder* ([ICML 2015, arXiv 1502.04585](https://arxiv.org/abs/1502.04585)).

### 3. Per-instance dynamic rubrics for rewrite-evals

`rewrite-evals.json` cases now support an optional `dynamic_rubric` block that names per-case criteria generated from the brief, rather than reusing a global checklist. The existing binary assertions are kept; the dynamic block adds 3–5 instance-specific criteria scored on a small ordinal scale.

Source: [WritingBench, arXiv 2503.05244](https://arxiv.org/pdf/2503.05244) — 84% human alignment with dynamic per-piece rubrics vs **58%** with static rubrics, the single largest measured improvement in the deep-research dump. Reinforced by Wu & Aji, *Style Over Substance* ([arXiv 2307.03025](https://arxiv.org/abs/2307.03025)): static prose rubrics reliably collapse to "good cadence wins."

## Tier A — high leverage

### 4. Orthogonal-axis scoring

Cases now support an optional `graded_dimensions` array (specificity, mechanism-presence, length-control, evidence-fit, relation-clarity), scored independently on a 1–5 scale. Single aggregate scores hide Pareto regressions: a change can raise mechanism-presence while lowering specificity, invisible to a binary pass.

Source: [FLASK, ICLR 2024 Spotlight, arXiv 2307.10928](https://arxiv.org/abs/2307.10928) — fine-grained skill decomposition catches regressions that aggregates miss. Reinforced by Wu & Aji (Multi-Elo / MERS proposal in [arXiv 2307.03025](https://arxiv.org/abs/2307.03025)).

### 5. Should-NOT-trigger near-miss queries

`trigger-queries.json` previously measured only positive trigger accuracy alongside generic non-prose negatives. It now includes explicit near-miss negatives that share surface vocabulary with positive triggers but should not load the skill: fact-check, link-check, draft-from-bullets, storyboard, slide-export, docx-from-dataset.

The docx case is taken from a real production bug, [anthropics/claude-code#43259](https://github.com/anthropics/claude-code/issues/43259), where the docx skill loaded on `.md` output tasks because the description triggered on the content noun before the format qualifier was evaluated.

Source: irrelevance-detection subset of the [Berkeley Function Calling Leaderboard](https://gorilla.cs.berkeley.edu/leaderboard.html) (Patil et al., ICML 2025); [MetaTool, ICLR 2024, arXiv 2310.03128](https://arxiv.org/abs/2310.03128) — separates the "whether" decision from the "which" decision.

### 6. Cross-family judge ensemble

The runbook now requires that any LLM-as-judge step uses at least two model families (e.g. Claude + GPT, or Claude + an open-source judge), and flags any case where they disagree for human review.

Source: Panickssery, Bowman, Feng, *LLM Evaluators Recognize and Favor Their Own Generations* ([NeurIPS 2024, arXiv 2404.13076](https://arxiv.org/abs/2404.13076)) — self-recognition probability correlates linearly with self-preference strength. Reinforced by Zheng et al., *Judging LLM-as-a-Judge* ([NeurIPS 2023, arXiv 2306.05685](https://arxiv.org/abs/2306.05685)) on judge bias broadly.

### 7. Length-controlled judging

The runbook's judge protocol now records candidate length and either normalizes by word count or applies a length-counterfactual adjustment (longer answers do not get preference unless an orthogonal-axis check confirms they earn it). For an anti-slop skill specifically, length-without-mechanism is the failure mode being fought.

Source: Dubois et al., *Length-Controlled AlpacaEval* ([arXiv 2404.04475](https://arxiv.org/abs/2404.04475)) — length is the single most exploitable judge confound.

### 8. Theoretical-saturation stop condition

The 3-round bounded loop now has a secondary stop signal: stop earlier than 3 rounds if ~20 consecutive eval traces yield no new failure categories. Captures both "rounds exhausted" and "nothing new to learn."

Source: Hamel Husain & Shreya Shankar, *LLM Evals FAQ* ([Jan 2026](https://hamel.dev/blog/posts/evals-faq/)) — theoretical-saturation rule from grounded theory.

## Tier B — supplementary

### 9. Pareto-front of best-per-instance candidates across rounds

The runbook now instructs that each iteration keeps the best candidate doctrine *per eval case*, not only the single global best. Round 3 then combines the doctrine pieces that won different cases. Prevents premature convergence on edits that improve the aggregate but regress a subset.

Source: [GEPA, arXiv 2507.19457](https://arxiv.org/abs/2507.19457) (ICLR 2026 Oral) — Pareto-front maintenance beats single-best carryover on prompt evolution, 35× fewer rollouts than RL.

### 10. Formal rejected-edit buffer

`evals/rejected-edits.md` is a new structured log. Every rejected edit gets an entry: the edit, the eval case that rejected it, and the reason. `LESSONS.md` continues to record durable "what not to overgeneralize" lessons; `rejected-edits.md` records the per-attempt graveyard so future iterations don't relitigate the same failed move.

Source: SkillOpt's rejected-edit buffer ([arXiv 2605.23904](https://arxiv.org/abs/2605.23904)) and the Darwin Gödel Machine archive ([arXiv 2505.22954](https://arxiv.org/abs/2505.22954)). Practitioner precedent: ExpeL's insight pool ([arXiv 2308.10144](https://arxiv.org/abs/2308.10144)).

### 11. Refresh eval inputs from production traces between major versions

Documented policy in the runbook: when a major version cuts, sample new cases from real anti-slop usage if available. Static evals score 99% on the cases that mattered six months ago while users have moved to new failure modes.

Source: industry framing of [eval rot](https://www.willowtreeapps.com/craft/llm-evaluation-framework) (WillowTree/TELUS, 2025). Academic precedent: [Dynabench, NAACL 2021](https://aclanthology.org/2021.naacl-main.324/).

### 12. Length budget per round

The runbook now caps `SKILL.md` word-count growth at +200 words per iteration. When the cap is exceeded, the round must include a consolidation pass before adding new rules.

Source: [Decagon, *Optimizing GEPA for Production*](https://decagon.ai/blog/optimizing-gepa-for-production) — prompt bloat is a documented failure mode of any add-edit loop. Reinforced by [TextReg, arXiv 2605.21318](https://arxiv.org/html/2605.21318).

### 13. Continuous metrics over discontinuous

Where natural, eval cases now expose a `graded_dimensions` block (see #4) alongside the binary `assertions`. Continuous metrics let small movements show up as small numbers rather than as a censored 0-or-1. The binary assertions remain for backwards-compatible CI gating; the graded dimensions feed the statistical gate in #2.

Source: Schaeffer, Miranda, Koyejo, *Are Emergent Abilities of Large Language Models a Mirage?* ([NeurIPS 2023 Outstanding Paper, arXiv 2304.15004](https://arxiv.org/abs/2304.15004)) — discontinuous metrics manufacture phantom step-changes and hide real progress.

## Out of scope, deliberately

- **Automated text-space optimizer** (ACE, TextGrad, SkillOpt, DSPy, GEPA as code) — too much machinery for a manually-iterated skill at this scale. Adopt only if the loop is ever scripted.
- **Rotating eval generation** (Dynabench-style) — overkill; the manual failure-corpus discipline already covers the spirit.
- **Judge meta-eval** (JudgeBench-style) — useful if a single LLM judge is the only gate; lower priority while cross-family ensembling (#6) and human spot-checks remain in the loop.
- **Skill doctrine changes** — none. This update changes only the infrastructure that decides whether a doctrine change is real.
