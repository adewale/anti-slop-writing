Source paragraph:

> The billing job runs ledger-fold passes after each import, so invoice-drift totals stay accurate. Each pass finishes before the nightly export starts, and the export reads only folded rows.

---

Verdict: ask-author

Slop tells: None of the cadence-based AI tells apply — no em-dash antithesis, no rule-of-three, no "not X, Y" negative parallelism, no hedged symmetry, no copula displacement, no banned filler phrases, no prestige adjectives. The one real hit is coined-compound risk: "ledger-fold" and "invoice-drift" are dropped in as settled terms of art. The passage never shows what a fold pass does to a row or what drift measures — it only shows when passes run and what the export reads afterward. Per the false-positive restraint, an undefined term doesn't earn the claim built on it, it just relocates the gap.

Specificity missing: What a ledger-fold pass actually computes. "Folded" could mean netting several correction rows into one, recomputing a running balance from source invoices, or just flagging a row as processed — the paragraph gives a status change and a read filter, not a computation. "Invoice-drift" is used as if already defined (drift between the ledger and what? accumulated over what window?) with no antecedent anywhere in the paragraph.

Inflated claim: "so invoice-drift totals stay accurate" claims correctness, but the only mechanism the paragraph goes on to supply — each pass finishes before the export starts, the export reads only folded rows — proves consistency (the export never reads a row mid-fold), not accuracy (that the fold's arithmetic is correct). The paragraph swaps a proven ordering guarantee for an unproven correctness guarantee and lets "so" carry the difference.

Flow break: The second sentence is joined to the first as coordinate support ("Each pass finishes... and the export reads...") but it answers a different question than the first sentence raises. Sentence 1 answers "why are totals accurate?" Sentence 2 answers "why doesn't the export read stale data?" That's a dependency relation — the ordering guarantee is a precondition for a clean read, not proof of correct arithmetic — and the paragraph should name it as such instead of letting "so" and "and" imply one continuous proof.

Concrete rewrite: Ask author: what does a ledger-fold pass do to a row — net several adjustment entries into one corrected total, recompute a running balance from source invoices, or something else? And what does "invoice-drift" measure — divergence between ledger total and invoice total, or accumulated rounding across passes? Fallback (no invented facts, uses only what the paragraph already establishes): "The billing job runs ledger-fold passes after each import. Each pass finishes before the nightly export starts, and the export reads only folded rows, so it never reads a row mid-fold." This keeps the proven ordering/consistency claim and drops the accuracy claim until the fold mechanism is named.

Rewrite check: The fallback contains no rule-of-three, no X-not-Y negative parallelism, no em-dash antithesis, no avoid-by-default phrases, no prestige adjectives, no decorative closure, and no invented facts — "never reads a row mid-fold" restates the two guarantees already in the source (pass finishes before export starts; export reads only folded rows) rather than adding a new name, count, tool, or timing. Passes self-detectors.

Remembered line: The one claim this paragraph actually proves is that the export reads only folded rows, so it never reads a row mid-fold. Whether folding fixes drift is still open.
