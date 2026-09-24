Paragraph reviewed:

> The billing job runs ledger-fold passes after each import, so invoice-drift totals stay accurate. Each pass finishes before the nightly export starts, and the export reads only folded rows.

Verdict: keep

Slop tells: None found. No avoid-by-default phrases ("at its core," "when it comes to," "it's worth noting that," etc.), no high-risk/prestige words ("crucial," "robust," "seamless," "utilize," and the like), no copula displacement (the verbs — runs, stay, finishes, starts, reads — are plain or do real locating work, not inflated "serves as"/"represents" substitutes), no hedged symmetry, no em-dash cadence (no dashes appear at all), no rule-of-three padding, no negative parallelism ("Not X. Y."), no bullet/bold/table dressing standing in for structure, no generic opening or generic closing.

Specificity missing: Largely none. The actor (the billing job), the trigger (after each import), the ordering guarantee (each pass finishes before the nightly export starts), and the filtering guarantee (the export reads only folded rows) are concrete and checkable by anyone who knows the pipeline. One item worth watching: "ledger-fold" and "invoice-drift" are hyphenated compounds the paragraph names but never defines internally — a reader learns that a pass runs and yields "folded" rows, not what folding does to a row's data. Applying the false-positive restraint check: the claim on the table is about pipeline ordering (the export can only see rows a fold pass has already processed), and that specific claim is earned by the two facts given — timing and filtering — without needing to know what the fold computation itself does. So the coined terms are a minor watch item here, not a block on this verdict.

Inflated claim: None. "Stay accurate" is scoped to the one hazard the paragraph actually addresses (the export reading unprocessed or half-processed rows), with no intensifier like "guaranteed" or "always correct" stacked on top of it.

Flow break: None. The first sentence states the claim; the second sentence answers the question the claim raises — how does it stay accurate? — with the ordering fact, then the filtering fact. Those two facts are coordinate supports for the same claim, so "and" is the right connector between them; forcing "because" onto either clause would merge two independent guarantees into one and lose the enumeration.

Concrete rewrite: Not needed.

Rewrite check: N/A — verdict is keep, so no rewrite was produced.

Remembered line: "the export reads only folded rows" — already the paragraph's own concrete detail, and the one line a reader could use to check the accuracy claim.
