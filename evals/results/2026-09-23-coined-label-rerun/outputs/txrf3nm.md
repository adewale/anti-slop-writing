Verdict: ask-author

Slop tells: "ledger-fold" and "invoice-drift" are coined compound labels — hyphenated noun phrases naming a process and a metric that the paragraph never defines and that aren't standard domain terms the way "dead-letter queue" or "two-phase commit" are. "Stay accurate" is a correctness claim riding on those undefined terms rather than on demonstrated behavior. Nothing else here reads as slop: no banned phrases or watch-list words, no rule-of-three, no negative parallelism, no em-dash cadence, no copula displacement, no hedged symmetry. Sentence 2's ordering-and-filter detail is genuinely concrete and should not be flagged.

Specificity missing: What a fold pass actually does to a row (recompute a balance? dedupe reissued lines? reconcile against a source ledger?), and what "invoice-drift" measures (a dollar delta? a count of unresolved rows?). Neither is stated or recoverable from the rest of the paragraph.

Inflated claim: "so invoice-drift totals stay accurate" asserts a correctness result. The only support offered is sentence 2, which proves a timing-and-read-filter guarantee — the export never reads a row before its fold pass finishes. That shows the export is consistent with whatever the fold pass produced; it does not show the fold pass produces correct totals. The paragraph lets "accurate" cover both.

Flow break: None between the sentences — sentence 2 answers a real question sentence 1 raises ("how do you know the export isn't reading half-processed rows?"). The unmarked move is a level-of-detail change: sentence 1 asserts a correctness property, sentence 2 evidences a narrower consistency property, and nothing signals that swap.

Concrete rewrite: Ask author: what does a fold pass do to a row — recompute a running balance, dedupe reissued lines, reconcile against a source ledger, something else? And what does "invoice-drift" measure — a dollar delta, a row count, something else? Fallback if that's not available: cut the accuracy claim and let the mechanism carry the paragraph — "The billing job runs ledger-fold passes after each import. Each pass finishes before the nightly export starts, and the export reads only folded rows."

Rewrite check: The ask-author question names the missing mechanism without inventing one; the fallback sentence reuses only source wording and adds no new claim. It contains no rule-of-three, no X-not-Y / negative parallelism, no em-dash antithesis, no banned avoid-by-default phrases, no prestige adjectives, no decorative closer, and no invented facts. Passes self-detectors.

Remembered line: "the export reads only folded rows" — the one clause here that names a checkable mechanism instead of asserting a result.
