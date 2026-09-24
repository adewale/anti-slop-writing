Reviewed paragraph:
"The billing job runs ledger-fold passes after each import, so invoice-drift totals stay accurate. Each pass finishes before the nightly export starts, and the export reads only folded rows."

Verdict: ask-author

Slop tells: One coined compound label carries the paragraph's main claim: "ledger-fold passes" names a process, but the passage never says what folding does to a row (merge import deltas into a running balance? recompute the total from source lines? drop duplicate imports?). Nothing else here reads as slop — no banned phrases, no copula displacement, no hedged symmetry, no em-dash clusters, no rule-of-three. The sentence-level construction is clean, hypotactic prose: "so" and "before" name relations instead of leaving them implied.

Specificity missing: What does a fold pass compute or change on a row? What does "invoice-drift" measure, and drift from what baseline — a source invoice total, a prior import, a reconciliation target? Without that, "ledger-fold" and "invoice-drift" are precise-sounding labels standing in for mechanisms the reader can't check, not the mechanisms themselves.

Inflated claim: "so invoice-drift totals stay accurate" claims correctness, but the only mechanism the paragraph actually shows — the fold pass finishes before the nightly export starts, and the export reads only folded rows — proves freshness and ordering, not accuracy. It shows the export never reads a row from an in-progress import; it does not show that folding corrects, deduplicates, or otherwise makes the totals right. "Accurate" is asserted, not earned by what's on the page.

Flow break: None. The second sentence answers the question the first raises ("how do you know totals stay accurate?") with a specific, checkable ordering-and-filter guarantee. The relation between the two sentences is named, not implied — "so" and "before" are doing real work instead of leaving the reader to infer cause or sequence.

Concrete rewrite: Ask author: what does the fold pass actually do to a row — merge import deltas into the running balance, recompute the total from source invoice lines, or drop duplicate imports? Naming that turns "so invoice-drift totals stay accurate" from an assertion into a shown mechanism.
Fallback (cuts the unearned claim instead of inventing the mechanism): "The billing job runs ledger-fold passes after each import. Each pass finishes before the nightly export starts, and the export reads only folded rows, so it never reads a row mid-import."

Rewrite check: The fallback contains no rule-of-three, no X-not-Y / negative parallelism, no em-dash antithesis, no avoid-by-default phrases, no prestige adjectives, no decorative closure, and no invented facts. It keeps the source's own vocabulary ("fold," "folded rows") rather than coining new terms, states only what the ordering-and-filter mechanism actually entails (the export never reads a mid-import row), and drops "accurate" rather than replacing it with an invented justification. Passes self-detectors.

Remembered line: "the export reads only folded rows" — the one claim in the paragraph a reader could go verify directly, by checking the filter in the export query.
