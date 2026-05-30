A move from 7/8 to 8/8 is one case flipping on an eight-case suite. That is well within the noise you expect from seed variation and judge nondeterminism, so it is not evidence the change worked. It is evidence that one case, on one run, scored differently. The PR author is reading a single Bernoulli flip as a trend.

The runbook should refuse the count comparison and require the following before merge.

1. Score at the per-case level, not the aggregate. "7/8 to 8/8" throws away almost all the information. Record each case's score on the old and new doctrine, ideally a graded score rather than pass/fail, and look at the paired deltas. Most of the eight cases probably did not move at all; the headline is carried entirely by one.

2. Run a paired significance test on those deltas. Because the cases are the same under both conditions, the test must be paired: a sign-flip permutation test or a paired bootstrap over per-case score differences. A raw count of passes is not a test. With N=8 and a single case flipping, no paired test will reach significance, which is exactly the point: the data cannot distinguish this change from noise.

3. Control for run-to-run variance. Re-run both the old and new doctrine across multiple seeds (and, if the judge is stochastic, multiple judge samples) and report the distribution, not a single 8/8. If the old doctrine also hits 8/8 on some seeds, the delta vanishes.

4. Gate on the holdout, not the tuning split. The change was developed against the tuning cases, so improvement there is partly fitting. The decision to merge belongs to the held-out split, which was not used during iteration. Report the holdout delta with the same paired test, and let that gate the merge.

5. State the limit honestly. With eight cases the suite simply lacks the power to certify a one-case improvement. The right conclusion is often "no detectable harm, no detectable benefit, merge only if it is justified on reasoning or it helps the holdout," not "proven to work."

The reusable structure: on a small suite, an aggregate count is a low-resolution instrument, and a single-case delta is below its resolution. Move to paired per-case deltas with a permutation or bootstrap test, replicate across seeds, and make the holdout, not the tuning split, the thing that decides the merge.
