# Reading a null result: what the eval literature says

Context: the 2026-06-14 stop-slop ablation (`evals/results/2026-06-14-stop-slop-ablation/`) produced an exact zero — every paired A/B delta was 0.00, across two rounds, three models, and both binary and graded metrics, with `scripts/score_delta.py` returning REJECT (CI [0,0], p=1.0). The honest question is: what is a zero delta actually licensed to claim? This note collects the relevant methodology so the next person does not over- or under-read it.

## 1. A failed superiority test is not proof of "no effect"

The default gate (`score_delta.py`) is a *superiority* test: it asks "did the change improve scores?" and answers REJECT when the CI overlaps zero. REJECT means **we did not detect an improvement**, not **the change does nothing**. Treating a non-significant superiority result as proof of no effect is the "absence of evidence is not evidence of absence" fallacy — a high p-value can equally mean the test was underpowered.

To make the positive claim "it does nothing," the right tool is an **equivalence test** — most simply the two one-sided tests (TOST) procedure. You declare a smallest effect size of interest (a SESOI: the smallest score change worth shipping a doctrine edit for), then show the confidence interval on the delta falls entirely inside ±SESOI. Lakens' primer is the standard practitioner reference, and his "absence of evidence" posts make the point directly. Caveat the literature stresses: equivalence tests need *more* power than superiority tests — often N in the hundreds — so a small suite rarely proves tight equivalence.

How this maps to our run: we are in the unusual regime where the delta is not a small noisy number near zero but a **degenerate point mass at zero** — many outputs were byte-identical under A and B. So equivalence within these items is near-trivially satisfied for any sane SESOI; the binding limit is not power but **external validity** (do 12 items × 3 models represent the writing tasks the skill faces?). The correct claim is therefore narrow: "on the tested item/model distribution the block changed nothing," not "the block can never matter."

- Lakens, *Equivalence Tests: A Practical Primer for t Tests, Correlations, and Meta-Analyses* — https://journals.sagepub.com/doi/full/10.1177/1948550617697177
- Lakens, *Improving Your Statistical Inferences*, ch. 9 (Equivalence Testing) — https://lakens.github.io/statistical_inferences/09-equivalencetest.html
- "Absence of evidence is not evidence of absence: Testing for equivalence" — http://daniellakens.blogspot.com/2016/05/absence-of-evidence-is-not-evidence-of.html

## 2. Small N: don't trust CLT intervals — which the repo already follows

For benchmarks below ~a few hundred items, CLT/normal-approximation error bars dramatically underestimate uncertainty. Bowyer, Aitchison & Ivanova (ICML 2025 spotlight) is the position paper; it recommends paired Bayesian or permutation methods instead. `score_delta.py` already implements paired bootstrap + a sign-flip permutation test and cites this paper, which is the correct response. Relevant subtlety for our run: with all-zero deltas the bootstrap CI and sign-flip p are degenerate ([0,0], p=1.0). They are valid here, but they would be *falsely* reassuring if there were any real spread — another reason to keep the permutation/bootstrap machinery rather than reverting to CLT bars when deltas become non-trivial.

- Bowyer, Aitchison, Ivanova, *Position: Don't Use the CLT in LLM Evals With Fewer Than a Few Hundred Datapoints*, ICML 2025 — https://arxiv.org/abs/2503.01747
- Related, on decomposing eval noise sources: *Measuring all the noises of LLM Evals* — https://arxiv.org/abs/2512.21326

## 3. Analyze paired, question-level differences — which the ablation design does

Miller's *Adding Error Bars to Evals* argues that when comparing two configurations you should do inference on the **question-level paired differences**, not on population-level summary statistics, and use clustered standard errors when items come in groups. Our design compares A vs B on the *same item and same model*, then takes the per-pair difference — exactly this recommendation. Pairing is also why a true zero shows up so cleanly: holding item and model fixed removes the between-item variance that would otherwise swamp a small effect.

- Miller, *Adding Error Bars to Evals: A Statistical Approach to Language Model Evaluations* — https://arxiv.org/abs/2411.00640

## 4. Ceiling effects: why round 1 alone was not enough, and what fixed it

Round 1 used single-sentence binary cases that all scored 1.0 — a saturated metric. Saturation is defined in the benchmarking literature as the **loss of discriminative power**: when items sit at the ceiling, they can no longer separate conditions, so a 0.00 delta there is only weak ("no regression") evidence. The standard fixes are harder items, adaptive selection, and item-difficulty calibration via Item Response Theory. Round 2 applied the harder-items fix: fresh paragraph-length graded cases whose scores showed real spread (0.87, 0.93, not 1.0), confirming the metric *could* have moved and still did not. That converts the result from "no regression" to "no effect on a discriminating metric."

- *Lost in Benchmarks? Rethinking LLM Benchmarking with Item Response Theory* — https://arxiv.org/abs/2505.15055
- *When AI Benchmarks Plateau: A Systematic Study of Benchmark Saturation* — https://arxiv.org/abs/2602.16763

## 5. The real threat to this conclusion is the judge, not the statistics

The entire result rests on LLM-as-judge scoring. The 2025–26 literature documents systematic judge biases: position bias, self-preference (a judge favoring outputs in its own style), and verbosity/length bias; single-judge panels are shown to be psychometrically unstable, and the standard mitigation is a multi-judge panel plus blinding.

What protects this run: judges were **blind to the meaning of the A/B labels** and apply/judge were **separated**, so any symmetric bias cancels in the *difference* (it shifts A and B equally). The single-family risk was then closed directly: a **3-model panel (Opus, Sonnet, Haiku)** re-judged the only textually-differing A/B pairs and every judge returned A=B (EQUIVALENT at SESOI ±0.05), so the null no longer rests on one judge family (`evals/results/2026-06-14-stop-slop-ablation/panel/`). The remaining honest limit is item/model coverage, not judge identity.

- *Judging the Judges: A Systematic Study of Position Bias in LLM-as-a-Judge* (2025) — https://aclanthology.org/2025.ijcnlp-long.18/

## Bottom line for this repo

1. `score_delta.py` REJECT is a no-improvement verdict, not a no-effect proof; for an explicit "it does nothing" claim, run the TOST equivalence check against a stated SESOI: `python3 scripts/score_delta.py <delta>.jsonl --sesoi 0.05` (added 2026-06-14). On this ablation it returns EQUIVALENT at SESOI ±0.05, which licenses the narrow "no effect of practical size on these items/models" claim that a bare REJECT does not.
2. The defensible claim from this ablation is the narrow one: on the tested items and models, with a non-saturated graded metric, the candidate block changed nothing. The limiting factor is item/model coverage, not statistical power, because the deltas are an exact point mass at zero.
3. The weakest link is single-family judging; the cross-family-judge follow-up would most strengthen any future accept/reject, win or null.
