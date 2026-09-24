# Critique

**Paragraph reviewed:**

> The billing job runs ledger-fold passes after each import, so invoice-drift totals stay accurate. Each pass finishes before the nightly export starts, and the export reads only folded rows.

---

Verdict: ask-author

Slop tells: Coined compound labels. "Ledger-fold passes" and "invoice-drift totals" are hyphenated, technical-sounding compounds that name a process and a metric the paragraph never defines. Neither is standard domain vocabulary (unlike "dead-letter queue" or "two-phase commit"), and neither is glossed in place. Sentence 1 hangs a causal claim on both undefined terms at once ("runs ledger-fold passes ... so invoice-drift totals stay accurate"), asking the reader to accept a cause-effect relationship whose mechanism was never shown. The hyphens supply the texture of precision; the referents stay out of reach.

Specificity missing: What a ledger-fold pass actually computes (deduplicating import rows, recomputing running balances, reconciling against source invoices, something else) is not stated. What "invoice-drift" measures (mismatch between invoiced amount and ledger amount, rounding error, currency-conversion error) is not stated. Sentence 2 supplies a state label ("folded rows") and a pipeline position (after import, before export), but that is a timing/scope fact, not a definition of the fold operation itself.

Inflated claim: "Stay accurate" is asserted as unconditional, with no boundary named (a failed pass, a concurrent import, a retry). The mechanism the paragraph actually shows — the pass finishes before the nightly export starts, and the export reads only folded rows — supports a narrower, verifiable claim: the export never reads unfolded (in-progress or stale) rows. That is a read-scope guarantee, not proof that the fold computation itself produces correct totals. The paragraph borrows the bigger claim's credibility from the smaller, shown one.

Flow break: Between sentence 1 and sentence 2 the paragraph shifts from a correctness claim (totals stay accurate) to a concurrency/ordering guarantee (pass-before-export, read-only-folded) without marking that the second is partial support, not proof, for the first. Smaller break in the same sentence: "Each pass finishes before the nightly export starts, and the export reads only folded rows" coordinates with "and" where the second clause is actually enabled by the first — because the pass finishes first, the export is guaranteed to see only folded rows. "So" would name that dependency; "and" just adds it.

Concrete rewrite: Ask author: what does a ledger-fold pass compute, and what does "invoice-drift" measure? Without that fact, sentence 1's causal claim can't be rewritten without inventing a mechanism. Fallback — cut the unsupported claim and tighten the "and" flagged above into "so":

"The billing job runs ledger-fold passes after each import. Each pass finishes before the nightly export starts, so the export reads only folded rows."

Rewrite check: No rule-of-three, no X-not-Y/negative parallelism, no em-dash antithesis, no avoid-by-default phrases, no prestige adjectives, no decorative closure, no invented facts — the only change from the source is "and" to "so," which names a dependency already implied by the given timing fact rather than adding a new one. Passes self-detectors.

Remembered line: "The export reads only folded rows." This is the paragraph's one fully concrete, checkable claim — a read-scope boundary — and it is a stronger carrier than "totals stay accurate," which currently rests on an undefined mechanism.
