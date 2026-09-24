Paragraph reviewed:

> The billing job runs ledger-fold passes after each import, so invoice-drift totals stay accurate. Each pass finishes before the nightly export starts, and the export reads only folded rows.

Verdict: keep

Slop tells: The only detector that fires is coined compound labels: "ledger-fold passes," "invoice-drift totals," and "folded rows" are hyphenated/compound terms the passage never spells out mechanically. Nothing else fires: no avoid-by-default phrase or watch-list word, no rule-of-three, no em-dash cadence (no dashes appear at all), no copula displacement ("serves as" / "stands as" / "features" / "marks" / "represents"), no hedged symmetry, no negative parallelism ("Not X. Y."), no outline-conclusion template, no bullet-plus-bold fake structure.

Specificity missing: Running the false-positive check on the compound labels (does nearby context supply a mechanism, failure mode, measurement, or boundary that earns the term?) finds a real boundary for "folded": the second sentence states that each pass finishes before the nightly export starts and that the export reads only folded rows. A reader can verify both halves directly (the ordering guarantee and the row filter), the same kind of support the skill's own keep example uses for "robust" (three named mechanisms: idempotency key, retry receipt, dead-letter cutoff). What that boundary does not supply: what a fold pass actually changes on a row, and what "invoice-drift" measures (rounding error, re-priced line items, late corrections, something else). That gap is worth a one-line glossary note if this paragraph will reach readers outside the team that owns the billing job; it is not, by itself, a reason to hold the paragraph.

Inflated claim: One narrow, non-blocking spot. "So invoice-drift totals stay accurate" is supported by the second sentence, but that sentence proves a narrower fact than the claim it is backing: it shows the export never reads a row while that row is still mid-fold (ordering plus a filter), not that the fold computation itself produces a correct number. Treating "never reads mid-fold" as equivalent to "accurate" quietly assumes the fold pass is correct. That assumption is ordinary in internal system documentation and does not block a keep, but it is the one place a stricter reader could ask "accurate by which check?"

Flow break: None. The second sentence answers the question the first raises, why totals stay accurate, with a concrete, checkable mechanism: completion-before-export ordering plus a folded-only read filter. That is a dependency relation, and it is already carried by subordination ("so," "before...starts," "and") rather than by side-by-side clauses, so no rewrite is needed for rhythm or hypotaxis.

Concrete rewrite: Not required; the paragraph clears the bar as written. Optional, non-blocking addition if the author wants "invoice-drift" itself earned rather than assumed: Ask author: what does invoice-drift measure? Rounding error, re-priced line items, late-arriving corrections, or something else? And what does a fold pass change on a row? Leave the term as domain shorthand until answered; do not fill in a plausible-sounding definition to close this slot.

Rewrite check: No full rewrite performed (verdict: keep). Checking the optional question above against the same detectors: no rule-of-three, no negative parallelism, no em-dash antithesis, no avoid-by-default phrase, no prestige adjective, no decorative closer, and no invented fact.

Remembered line: "the export reads only folded rows." It is the paragraph's most concrete, checkable line, the one a reader could confirm against the actual export query.
