Verdict: ask-author

Slop tells: Two coined compound labels carry the paragraph's weight without being defined: "ledger-fold passes" and "invoice-drift totals." Both are hyphenated noun phrases naming a process/artifact the paragraph never explains, and neither is a standard, look-up-able term the way "dead-letter queue" or "two-phase commit" is.

Specificity missing: What a ledger-fold pass actually does to the rows (recompute a running balance? merge or dedupe entries? close a batch into a canonical snapshot?) is never stated. What "invoice-drift" concretely is — a mismatch between invoice and ledger totals, a monitoring metric, something else — is only implied by the ordering/filter guarantee in sentence two, never named.

Inflated claim: None. "Stay accurate" is a plain, checkable claim, and it's earned: "each pass finishes before the nightly export starts" plus "the export reads only folded rows" together explain why the export can't see stale or partial data. That support holds regardless of what folding computes internally, so the accuracy claim itself doesn't need rescuing.

Flow break: None. Sentence one states the claim; sentence two answers the question it raises — how does the timing between fold and export actually prevent drift — with a concrete ordering-plus-filter mechanism. The paragraph earns its own follow-up.

Concrete rewrite: Ask author: what does a ledger-fold pass do to the imported rows — recompute a running balance, merge/dedupe entries, or close a batch into a canonical snapshot? And does "invoice-drift" mean specifically the gap between invoice and ledger totals from reading pre-fold rows, or something else? Fallback: keep the paragraph as written. The claim it has to earn — accuracy — is already earned by the ordering guarantee and the read filter, independent of what folding does internally. Only spell out the fold mechanism if this text will be read by someone outside the billing team who needs to verify or debug it directly (an audit, an incident writeup, an onboarding doc).

Rewrite check: No rule-of-three, no X-not-Y/negative parallelism, no em-dash antithesis, no avoid-by-default phrases, no prestige adjectives, no decorative closure. The ask-author question offers named options for the author to choose from rather than asserting one as fact, and the fallback reuses only the mechanism already stated in the source (ordering, read filter) — no invented name, count, tool, or timing. Passes self-detectors.

Remembered line: "the export reads only folded rows" — the one clause that names a concrete, checkable boundary instead of a label, and the model the rest of the paragraph's jargon should be rewritten to match.
