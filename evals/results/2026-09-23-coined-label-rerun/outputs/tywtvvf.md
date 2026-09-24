Paragraph reviewed:
"The billing job runs ledger-fold passes after each import, so invoice-drift totals stay accurate. Each pass finishes before the nightly export starts, and the export reads only folded rows."

Verdict: ask-author

Slop tells: Two coined compound labels carry the paragraph's central claim without being defined: "ledger-fold passes" and "invoice-drift totals." Neither is a standard domain term the way "dead-letter queue" or "two-phase commit" is, and the passage never states what a fold pass does to a row or what "drift" is measured against. Aside from that, the paragraph is clean: no banned avoid-by-default phrases, no high-risk words, no em-dash clusters, no rule-of-three, no hedged symmetry, no displaced copulas, no staccato contrast cadence.

Specificity missing: What does a fold pass do to a raw imported row (dedupe by invoice ID, aggregate line items into a parent invoice, reconcile against a separate source ledger, something else)? What does "invoice-drift" measure against (a prior snapshot, an external payment feed, a second ledger)? "Ledger-fold" and "folded rows" are at least internally consistent — the paragraph uses the term the same way twice — but "invoice-drift" names a metric the reader has no way to check.

Inflated claim: "so invoice-drift totals stay accurate" claims correctness, but the sentence that follows only demonstrates timing safety, not correctness: each pass finishes before the export starts, and the export reads only folded rows, so the export can never see a row that has not finished folding. That rules out reading stale or partial data; it does not rule out a bug inside the fold pass itself producing a wrong total on a perfectly well-ordered read. The paragraph proves timing safety and reports it as accuracy.

Flow break: None severe. The second sentence is the unstated evidence for the first sentence's claim, a dependency relation ("because passes finish before export starts and export reads only folded rows, the export sees complete data") that the reader has to infer rather than one the prose names directly. Fine at this length; would only need an explicit connective in a longer document.

Concrete rewrite: Ask author: what transformation does a ledger-fold pass apply to a row (dedupe by invoice ID, aggregate line items into a parent invoice, reconcile against a separate source ledger, or something else), and what baseline does "invoice-drift" measure against (a prior snapshot, an external payment feed, a separate ledger)?

Fallback if that mechanism isn't available: cut the unproven accuracy claim and let the sentence that already carries evidence stand alone: "The billing job runs ledger-fold passes after each import. Each pass finishes before the nightly export starts, and the export reads only folded rows." This keeps the one guarantee the paragraph actually demonstrates and drops the one it only asserts.

Rewrite check: No rule-of-three, no X-not-Y / negative parallelism, no em-dash antithesis, no avoid-by-default phrases, no prestige adjectives, no decorative closing line, and no invented facts: the ask-author question offers candidate mechanisms inside a question rather than asserting one, matching the skill's own "which coding tool? Cursor, Claude Code, Copilot, Aider, other?" pattern, and the cut fallback is a direct subset of the source sentence with nothing added. Passes self-detectors.

Remembered line: "the export reads only folded rows": the one claim in this paragraph a reader could independently verify by reading the export's query, and the fact any revision should be built on instead of the unproven "accurate."
