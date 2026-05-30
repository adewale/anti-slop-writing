A 7/8 → 8/8 move on an eight-case suite is one case flipped. With judge stochasticity, seed variance, and the binary collapse from per-assertion scoring up to per-case pass/fail, a single-case delta sits well inside the noise band you would expect from rerunning the same skill against the same suite. The runbook should not let the PR author treat that delta as evidence on its own.

Before accepting the change, the runbook should require:

1. A per-case score delta, not a raw count comparison. The grade step already produces fractional per-case scores (assertions passed / total). Compare the paired vector of per-case scores before and after, not the headline 7 vs 8. A paired bootstrap over per-case score deltas, or a sign-flip permutation test on the same paired deltas, gives a defensible p-value or confidence interval; a count comparison on N=8 does not.

2. Multiple seeds per case on both runs before computing that paired delta, so the test is measuring the doctrine change rather than judge or apply noise. If the suite is non-deterministic, the variance across seeds on the unchanged side is the floor for any claim about the changed side.

3. The decision must be gated on the holdout split, not the tune split the doctrine was iterated against. If the 7/8 → 8/8 came from cases the author was looking at while editing the doctrine, the move is consistent with overfitting to those cases and tells you nothing about generalization. The merge criterion is: holdout paired delta is positive and survives the resampling test, and no regression on the tune split beyond noise.

4. A specific failing case to point at. "One more case passes" is not a finding until you can name which case flipped, read its before/after output side by side, and decide whether the rewrite is genuinely better or whether the judge is rewarding a surface change (cadence, length, vocabulary) that the doctrine edit happened to produce. If you cannot articulate the mechanism by which the doctrine change caused that specific case to pass, the win is suspect.

5. An adversarial case lock-in if the doctrine change added or tightened a rule. Any case that the old doctrine handled correctly and that the new doctrine could plausibly over-flag (earned antithesis, deliberate rule-of-three in a known-good human passage) should be added to the holdout before merge, so the next iteration cannot quietly trade false-positive resistance for one more pass.

The default answer to "we went from 7/8 to 8/8" on a suite this small is: not yet. Show the paired test on the holdout, show the seed variance, and name the case that moved.
