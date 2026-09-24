Verdict: ask-author

Slop tells: Coined compound labels. "ledger-fold passes" names a process and "invoice-drift totals" names a metric that the paragraph never defines; "folded rows" inherits the same gap, since it depends on what "fold" actually does. Neither term is standard the way "dead-letter queue" or "two-phase commit" is. "invoice-drift" gets partial credit for following a recognizable pattern (schema drift, clock drift, config drift = gradual divergence), so it's a lower-risk coinage. "ledger-fold" has no comparable domain meaning and is not defined in place.

Specificity missing: What operation does a fold pass perform on a ledger row — merge duplicate entries per invoice, reconcile debits against credits, mark a row as finalized, something else? What does an "invoice-drift total" measure — the gap between invoiced and recorded amounts, or something else? Without that, "folded rows" names an output but not a transformation.

Inflated claim: "so invoice-drift totals stay accurate" is presented as earned, but the only support the paragraph gives is timing and filtering (pass finishes before export starts; export reads only folded rows) — both describe when folded data is available and that export is restricted to it, not why folding is what makes a total accurate. A term can't earn a claim by pointing to another undefined term: the support relocates the gap instead of closing it.

Flow break: None. Sentence 2 answers the question sentence 1 raises — how is that guaranteed? — with a real ordering invariant ("before... starts") and a real filter ("reads only folded rows"). The dependency is named, not just implied by cadence.

Concrete rewrite: Ask author: what does a ledger-fold pass do to a row, and what does an invoice-drift total measure? Fallback if that's out of scope here: drop the unearned inference and keep only what the paragraph can verify on its own —

"The billing job runs ledger-fold passes after each import. Each pass finishes before the nightly export starts, and the export reads only folded rows."

This keeps the two concrete guarantees (ordering, filtering) and drops the accuracy claim that neither sentence actually earns.

Rewrite check: The fallback contains no rule-of-three, no X-not-Y/negative parallelism, no em-dash antithesis, no avoid-by-default phrases, no prestige adjectives, no decorative closure, and no invented facts — it only removes a clause. Passes self-detectors.

Remembered line: "the export reads only folded rows" — the one clause in the paragraph that names an actual mechanism (a filter) rather than an outcome, and worth keeping in any rewrite.
