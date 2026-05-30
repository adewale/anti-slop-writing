No, four iterations against one document does not show the skill got better in general. It shows the doctrine got better at scoring that one document. Those are different claims, and the difference is the whole point of having a holdout.

Repeated tuning against a single text drifts the doctrine toward the quirks of that text: its specific failure modes, the particular cadences its author happens to use, the vocabulary clusters that happen to appear, the structural choices that one writer prefers. Each iteration that moves a metric on that document is consistent with two stories — the doctrine got sharper, or the doctrine learned the document — and the within-document metric cannot tell them apart. After four iterations the prior should shift toward the second story unless there is outside evidence for the first.

What to do next:

1. Freeze the current doctrine and run it, unchanged, against a different real text the doctrine was not tuned against. Pick something with different surface properties — different domain, different author, different length, ideally something whose known good and known bad passages you can label before grading. The generalization claim only survives if scores on the unseen text are at least comparable to scores on the tuned document.

2. For each rule that moved during the four iterations, ask whether it fixes a failure mode that is repeatable across texts or a pattern that happens to recur in the tuning document. A rule like "X-not-Y cadence with both sides unevidenced is decorative antithesis" is a repeatable failure; a rule that turns out to flag a phrase the tuning author overuses is a fit to that author. If you cannot articulate the failure mode independently of the document, the rule is suspect.

3. Lock in adversarial cases for any rule that could plausibly over-flag. If iteration N tightened a detector, add to the holdout: a passage from a different author where that detector should not fire, ideally one where earlier doctrine versions correctly let it pass. False-positive resistance is part of the skill's job — the staccato contrast test exists specifically to keep the skill from blanket-flagging earned antithesis — and the only way to keep that resistance from eroding across iterations is to make it a graded case the next iteration has to defend.

4. Treat "metric moved on the tuning document" as a necessary but insufficient signal going forward. The merge bar is movement on the holdout that does not come with regressions on the false-positive cases.

The honest summary of four single-document iterations: the doctrine has been fitted to one essay; whether it is better at the skill's actual job is unmeasured. Measure it on a text the doctrine has not seen before claiming the skill improved.
