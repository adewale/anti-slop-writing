Verdict: keep

Slop tells: None. No prestige vocabulary, no rule-of-three, no "not just X but Y," no hedged symmetry, no copula displacement ("serves as," "represents," etc.), no decorative em-dashes, no outline-conclusion template, no phrase from the avoid-by-default list.

Specificity missing: None. The paragraph names the actor (the billing job), the mechanism (ledger-fold passes), the trigger (after each import), the metric being protected (invoice-drift totals), the ordering guarantee (each pass finishes before the nightly export starts), and the read constraint (the export reads only folded rows).

Inflated claim: None. "So invoice-drift totals stay accurate" looks like a claim of importance, but the second sentence supplies the mechanism that earns it: an ordering guarantee (the fold pass always finishes before export starts, so this cycle's folded data is present) and a filter guarantee (the export never reads a row mid-fold). A claim earns its qualifier when the surrounding sentences supply the mechanism, and this one does.

Flow break: None. The second sentence answers the question the first raises — why does running fold passes keep totals accurate? — by giving the two guarantees that make the claim checkable. The "and" joins two independent guarantees (timing, then content) rather than hiding a causal relation that needed subordination: rewriting as "because the pass finishes first, the export reads only folded rows" would misstate the mechanism, since the read filter is a separate design choice, not a downstream effect of the timing.

Concrete rewrite: Not applicable — the paragraph already states mechanism before claim and needs no rewrite.

Rewrite check: Not applicable — no rewrite was produced.

Remembered line: "The export reads only folded rows" — this is the detail worth keeping; it is what makes "accurate" a checkable property instead of an asserted one.
