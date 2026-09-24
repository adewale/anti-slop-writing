Paragraph under review:

> The billing job runs ledger-fold passes after each import, so invoice-drift totals stay accurate. Each pass finishes before the nightly export starts, and the export reads only folded rows.

Verdict: keep

Slop tells: None of the catalogued AI-writing or marketing tells are present. No banned phrases or watch-list words (no "robust," "seamless," "crucial," "underscore," etc.), no copula displacement — every verb is plain and load-bearing ("runs," "stay," "finishes," "starts," "reads"), no rule-of-three, no "Not X, Y" negative parallelism, no hedged symmetry ("Whether X or Y"), no em-dash cadence (no dashes at all), no rhetorical staccato or antithesis, no generic opener or closer, no bullet/bold-header fake structure.

Specificity missing: None. Every actor and mechanism is named: "the billing job," "ledger-fold passes," "each import," "each pass," "the nightly export," "folded rows." Nothing here falls back on a vague actor ("the system," "it") or an unnamed process.

Inflated claim: "so invoice-drift totals stay accurate" reads, in isolation, like a claim that would need support. The paragraph supplies that support, just in the next sentence rather than the same one: the fold pass finishes before the nightly export starts, and the export reads only folded rows — so the export can never see an import's rows before drift has been folded into them. Per false-positive restraint, nearby context earns the term here: naming that support, the ordering guarantee (fold-before-export) plus the read filter (folded rows only) is what turns "stay accurate" into a checkable property of the export's inputs rather than an unsupported assertion.

Flow break: None. Sentence 1 states a practice and its result, which raises the natural next question — what stops the export from reading data before it has been folded? Sentence 2 answers exactly that question with the two guarantees (order, then filter). That is a dependency relation resolved inside the paragraph, not two facts sitting side by side in a plausible order.

Concrete rewrite: Not needed. The paragraph already carries its claim on a named actor and a checkable mechanism (fold-pass timing plus a row filter) instead of on inflated language, so there is nothing to rewrite.

Rewrite check: N/A — no rewrite was produced, since the verdict is keep.

Remembered line: the export reads only folded rows.
