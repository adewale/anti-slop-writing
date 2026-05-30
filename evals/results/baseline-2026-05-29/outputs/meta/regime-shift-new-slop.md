This is a regime shift: the failure moved, and the phrase list is now aimed at the old position. A banned-phrase detector matches surface strings, so a model that simply stops emitting those strings will pass while producing a new kind of bad writing the list was never built to catch. Holding the pass rate steady here would be measuring compliance with a blocklist, not quality.

Name the new failure mode precisely, because the fix depends on naming it:

- Unsupported specificity. The sentence cites a number ("reduced latency by 43%," "across 12 regions") with no run, dataset, or method behind it. Precision is being used as a rhetorical texture, not as evidence.
- Fake precision / false provenance. "Studies show," "internal benchmarks indicate," "the data suggests" — an authority is invoked without a nameable source. The confident, clinical register makes the claim feel verified when nothing has been verified.

This is the same underlying disease as the old slop (significance asserted rather than earned) but expressed through manufactured evidence instead of inflated adjectives. The detector has to shift from "which words appear" to "is each specific claim backed by a real, nameable source."

How to adapt the suite:

1. Add a failure-corpus entry for unsupported specificity and false provenance, with real examples of clinically precise sentences whose numbers and sources cannot be traced. Make the corpus the thing the suite is responsible for, not the phrase list.

2. Add evals that test provenance directly. Given a draft containing a statistic, the skill should either attach a checkable source, mark the number as illustrative, or replace it with a qualitative claim it can actually support. An eval passes when fabricated precision is flagged or grounded, and fails when it is passed through unchanged.

3. Add adversarial cases that are clean on the old axis and dirty on the new one: zero banned phrases, varied rhythm, no rule-of-three, but every concrete detail is invented. If the current skill passes these, that is the gap to close.

4. Stop treating the phrase list as the spec. It is one detector among several. The durable target is: every specific claim is either sourced, hedged as illustrative, or cut. Encode that as a rubric, not a string match, so the next regime shift does not silently sail through.

The reusable structure: when models route around a surface-level detector, the metric measures evasion, not improvement. Re-anchor the eval on the mechanism the detector was a proxy for here, "is this specificity earned and traceable?" and add held-out cases built from the new failures so you can tell whether the skill actually adapted or just got quieter.
