Paragraph reviewed:

> The billing job runs ledger-fold passes after each import, so invoice-drift totals stay accurate. Each pass finishes before the nightly export starts, and the export reads only folded rows.

Verdict: keep

Slop tells: Two coined compound labels trip the detector as hypotheses, not verdicts — "ledger-fold" (passes) and "invoice-drift" (totals): hyphenated noun phrases naming a process and a metric that the paragraph never spells out algorithmically. Nothing else on the source-backed detector list fires: no banned phrases, no copula displacement (runs/finishes/starts/reads are all plain verbs doing plain work), no hedged symmetry, no em-dash cadence, no rule-of-three, no staccato antithesis, no nominalization padding.

Specificity missing: The fold algorithm and the drift computation are both left undefined — a reader still can't say what "folding" does to a row or what unit "drift" is measured in. Neither gap is load-bearing here, though. The paragraph isn't explaining how folding works or how drift is computed; it's claiming that the export's read set can't contain unreconciled data, and that narrower claim is fully specified (see Inflated claim).

Inflated claim: "so invoice-drift totals stay accurate" reads, in isolation, like an unearned correctness claim riding on an undefined metric. Checked against the next sentence, it's earned: "Each pass finishes before the nightly export starts, and the export reads only folded rows" gives export a read set restricted to already-folded rows, with folding always complete before export starts — so export can never read a row mid-fold or still unfolded. That ordering-plus-scope mechanism is sufficient support for "accurate" as used here, independent of what the fold computation does internally. Flattened (cadence removed, claim preserved): "The billing job folds rows after import; export only reads rows that have already been folded, and folding always finishes first." The residual claim still names an actor (the billing job) and a mechanism (ordered fold-then-export, restricted read set) instead of collapsing into a generic assertion — the ordering guarantee is doing the work, not the cadence.

Flow break: None. The second sentence answers the question the first raises — how do we know the totals export sees are always fully folded — with the ordering and scope guarantee. "So" and "before" are causal/temporal subordination, not unstated juxtaposition; the trailing "and the export reads only folded rows" adds a second concrete fact about the export rather than an implied contrast.

Concrete rewrite: None needed. Both terms flagged under Slop tells resolve to keep once checked against the surrounding sentence, so there is no tell here that needs a rewrite, a cut, or an ask-author fallback.

Rewrite check: N/A — no rewrite produced; the paragraph stands as written. Checked anyway: it contains no rule-of-three, no X-not-Y / negative parallelism, no em-dash antithesis, no avoid-by-default phrases, no prestige adjectives, no decorative closure, and no invented facts.

Remembered line: "the export reads only folded rows" — the one fact a reader should carry away: export never touches a row before its fold pass has run.
