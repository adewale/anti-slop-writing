Verdict: ask-author

Slop tells: Coined compound labels — "ledger-fold passes," "invoice-drift totals," and "folded rows" are hyphenated, technical-sounding terms that name a process and a metric the paragraph never defines, and an accuracy claim is then allowed to ride on them. Secondary: rhetorical-style drift — the two compounds compress "what the job actually computes" into noun labels, giving informational density without mechanism.

Specificity missing: (1) What a ledger-fold pass does to a ledger row — recompute a running balance, merge duplicate postings, apply late credits, replay deltas? (2) What "invoice-drift" measures and what causes it — out-of-order imports, rounding, multi-currency conversion, late refunds? (3) Whether "folded" is a boolean flag, a separate reconciled table, or a computed column — the mechanism the export's filter actually depends on.

Inflated claim: "so invoice-drift totals stay accurate" claims correctness, but the only support the paragraph supplies — each pass finishes before the export starts, and the export reads only folded rows — is an ordering/consistency guarantee, not a correctness mechanism. It shows the export sees a stable view of whatever the fold produced; it does not show that what the fold produced is right. Per the false-positive check, an undefined term can't earn a claim on its own — "ledger-fold" relocates the gap instead of closing it.

Flow break: Sentence 2 functions as the evidence for sentence 1's claim, but the dependency is left implicit — nothing marks "each pass finishes... reads only folded rows" as the reason totals "stay accurate" rather than an unrelated scheduling note. The coordinating "and" also treats "pass finishes before export starts" and "export reads only folded rows" as two same-weight facts, when the more likely relation is dependency (the timing guarantee is what makes the row-filter guarantee meaningful) — hypotaxis would make that explicit instead of leaving it to be inferred.

Concrete rewrite:
Ask author: What does a ledger-fold pass actually compute on a ledger row (recompute running balance, merge duplicate postings, apply late credits), and what specifically causes invoice drift (out-of-order imports, rounding, late refunds)? Naming that turns "stay accurate" into a checkable claim instead of a label.
Fallback (no invented facts — cuts the unearned claim, keeps only the two verifiable operational facts):
"The billing job runs ledger-fold passes after each import. Each pass finishes before the nightly export starts, and the export reads only folded rows."

Rewrite check: The fallback contains no rule-of-three, no X-not-Y / negative parallelism, no em-dash antithesis, none of the banned avoid-by-default phrases, no prestige adjectives, and no decorative closure. It contains no invented facts — every clause is copied from the source paragraph, minus the unearned "so invoice-drift totals stay accurate" clause. Passes self-detectors.

Remembered line: "the export reads only folded rows" — the one line in the paragraph that names a checkable mechanism (a read-time filter) rather than an asserted outcome. Once the author supplies what folding computes, rebuild the paragraph's accuracy claim around this filter fact instead of around the bare word "accurate."
