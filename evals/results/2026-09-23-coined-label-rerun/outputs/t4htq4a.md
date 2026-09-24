Paragraph reviewed:
"The billing job runs ledger-fold passes after each import, so invoice-drift totals stay accurate. Each pass finishes before the nightly export starts, and the export reads only folded rows."

Verdict: ask-author

Slop tells: Coined compound label doing the work of an explanation. "Ledger-fold passes" names a process, but the paragraph never says what folding does to a row, so the process's name is offered as the reason invoice-drift totals stay accurate instead of a mechanism being shown. This is the "a name is not a mechanism" pattern: the hyphen and the procedural framing (runs, after each import, finishes before) supply the texture of precision while the actual transformation stays out of reach.

Specificity missing: Two unresolved terms carry the paragraph's central claim. What does a fold pass do to a ledger row: dedupe entries, recompute a running balance, reconcile against the import source, something else? What does "invoice-drift" measure: a mismatch between imported and ledgered totals, a discrepancy that accumulates over time, a reconciliation error? "Invoice-drift" reads like the standard ops pattern behind "config drift" or "data drift," so the label alone is plausible domain jargon, but the paragraph still never states what is drifting from what, so a reader can't check the claim against the term.

Inflated claim: "So invoice-drift totals stay accurate" is a correctness claim, but the only evidence given is an ordering and read-scope fact: the fold pass finishes before the nightly export starts, and the export reads only folded rows. That fact earns an isolation guarantee: the export never reads a row before it has been folded. It does not earn an accuracy guarantee, which also depends on the fold logic itself being correct, and that logic is never shown. The sentence lets a timing guarantee stand in for a correctness guarantee.

Flow break: None outright. Sentence 2 supplies the ordering detail that sentence 1's claim leans on, so the paragraph reads as claim-then-support. But the support only backs isolation, not accuracy, so the implied relation ("this is why totals stay accurate") is wider than what the sentence actually shows ("this is why the export never sees an unfolded row").

Concrete rewrite: Ask author: what does the fold pass do to a row, and what does "invoice-drift" measure? Name the mechanism and the metric so "stay accurate" can be checked instead of assumed.
Fallback (cut the unsupported claim, keep what the paragraph actually establishes): "The billing job runs ledger-fold passes after each import. Each pass finishes before the nightly export starts, and the export reads only folded rows."

Rewrite check: The fallback contains no rule-of-three, no X-not-Y / negative parallelism, no em-dash antithesis, no avoid-by-default phrases, no prestige adjectives, no decorative closure, and no invented facts. It keeps only the ordering and read-scope statements already in the source and drops the claim that was not backed. Passes self-detectors.

Remembered line: The evidence shown proves the export never reads an unfolded row; whether the folded totals are correct depends on a fold mechanism this paragraph names but never explains.
