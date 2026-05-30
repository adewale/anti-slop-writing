Verdict: reject the claim as stated; require more before accepting the change.

Slop tells: "proves the change worked" on a single-case delta in an eight-case suite is the same shape as "47% faster" without a baseline — a number presented as evidence without the machinery that would let it be evidence.

Specificity missing: which case flipped from fail to pass; whether the judge was held constant across both runs; whether the rubric or the apply prompt also changed; what the per-case score (not just pass/fail) looked like before and after; whether the eight cases are the tuning split the doctrine was iterated against or a holdout.

Inflated claim: 7/8 → 8/8 on N=8 is a one-case delta. With binary grading and a stochastic judge, a single case flipping is well within run-to-run noise: even at a fixed candidate, judge sampling and prompt-order effects can move one case across the threshold. The aggregate count does not separate signal from noise.

Flow break: the runbook step the author skipped is the one that turns a count into a claim — a paired test on per-case scores, on a split the doctrine has not been tuned against.

What the runbook should require before accepting:

1. A paired statistical test on per-case score deltas, not a raw 7/8 vs 8/8 comparison. Either a paired bootstrap over the eight per-case score differences with a confidence interval that excludes zero, or a sign-flip permutation test on the same per-case deltas. The unit of analysis is the per-case delta, not the suite-level count.

2. A holdout check. The eight cases the doctrine was iterated against are the tuning split by construction; gains there are expected and do not generalize. The merge gate has to be the holdout split, evaluated once, with the same paired test applied to its per-case deltas.

3. A judge-noise floor. Re-run the same candidate against the same suite with a different judge seed (or different judge sampling temperature) and report the run-to-run variance. A change smaller than that variance is not a signal, no matter how the count moves.

4. A diff scope check. Confirm that only the doctrine changed between the two runs — same judge model, same judge prompt, same apply prompt, same eval cases. A coincident change to any of those invalidates the comparison.

Concrete rewrite of the PR claim: "On the tuning suite, the change moved one case from fail to pass (7/8 → 8/8). The paired bootstrap on per-case score deltas has a 95% CI that includes zero, and the holdout suite has not been run yet. I am not claiming the change worked; I am asking for a holdout run before merge."

Remembered line: a one-case flip on an eight-case suite is a coin landing the way you hoped; the runbook's job is to require the test that tells you whether the coin is weighted.
