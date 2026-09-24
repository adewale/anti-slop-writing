Paragraph reviewed:

> The billing job runs ledger-fold passes after each import, so invoice-drift totals stay accurate. Each pass finishes before the nightly export starts, and the export reads only folded rows.

Verdict: keep

Slop tells: None. No avoid-by-default phrases (no "It's worth noting," "not just X but Y," "This is where X comes in," etc.), no high-risk words (delve, realm, tapestry, testament, pivotal, crucial, underscore, seamless, robust, transformative, and the rest), no displaced copulas ("serves as," "stands as," "represents"), no hedged symmetry ("Whether you're X or Y"), no em-dash cadence, no rule-of-three, no "Not X. Y." parallelism, no decorative closer.

Specificity missing: None. The actor is named ("The billing job"), the mechanism is named ("ledger-fold passes"), the measured quantity is named ("invoice-drift totals"), and both the timing guarantee ("before the nightly export starts") and the scope restriction ("reads only folded rows") are concrete and independently checkable, not gestured at.

Inflated claim: None. "stay accurate" is a specific, falsifiable claim about a named quantity, not a borrowed significance word. It is earned in the same paragraph: the export is ordered to run only after folding completes and is filtered to folded rows only, so pre-fold (drifted) rows are excluded by construction rather than by assertion.

Flow break: None. Sentence 2 answers the question sentence 1 raises — how does folding keep totals accurate — with a named dependency relation: a temporal dependency ("before... starts") plus a scope filter ("reads only folded rows"). Sentence 2 makes that dependency explicit rather than leaving it implied, which is what makes the pair read as one argument instead of two facts placed side by side.

Concrete rewrite: Not needed. Rewriting this would trade earned compression for restatement: both sentences already carry a named actor, a named mechanism, and an explicit relation (cause in sentence 1, dependency in sentence 2), with nothing vague left to sharpen and nothing padded left to cut.

Rewrite check: N/A — no rewrite offered, since the source paragraph already passes the same detectors it would be checked against.

Remembered line: "the export reads only folded rows." That clause is the actual drift guard; the timing guarantee in the first half of sentence 2 only matters because this filter exists to make timing enforceable.
