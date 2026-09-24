Paragraph reviewed:

> The billing job runs ledger-fold passes after each import, so invoice-drift totals stay accurate. Each pass finishes before the nightly export starts, and the export reads only folded rows.

Verdict: ask-author

Slop tells: The causal claim runs on a coined compound label the paragraph never opens up. "Ledger-fold pass" names a process — fold could mean dedupe, delta-recompute, or overwrite — with no domain precedent like "dead-letter queue" or "two-phase commit" to lean on, and "folded rows" inherits the same gap since it's just the participle of that undefined verb. "Invoice-drift" is a softer case: "drift" is a recognizable engineering metaphor (config drift, clock drift), so the compound reads, but nothing says what invoice-drift is measured against. No banned phrases, copula displacement, rule-of-three, hedged symmetry, or em-dash clusters — the cadence is clean; the gap is definitional, not rhythmic.

Specificity missing: What a ledger-fold pass actually does to the ledger — dedupe reimported entries, recompute totals from per-invoice deltas, overwrite a stale cached total — is the mechanism the whole claim depends on, and it's absent. Secondary: what invoice-drift is measured against (a source ledger, a prior export, a reconciliation report), and what "accurate" means as a checkable condition.

Inflated claim: "so invoice-drift totals stay accurate" is an unconditional correctness guarantee resting on the fact that a process ran, not on any check — no checksum, reconciliation, or idempotency detail backs it. The paragraph's real evidence (pass finishes before export starts, export reads only folded rows) proves a narrower thing: the export never reads pre-fold data. That's a read-consistency guarantee, not an accuracy guarantee, and "so" is asked to cover the difference.

Flow break: Sentence 1 claims a correctness property of the fold itself. Sentence 2 proves a different, narrower property — that the export is ordered after, and scoped to, folded rows. The two read as continuous because of "so" / "and," but sentence 2 backs the export's consistency, not the fold's correctness, so the implied proof doesn't fully land.

Concrete rewrite:
Ask author: what does a ledger-fold pass do to the ledger (dedupe reimported entries, recompute totals from per-invoice deltas, overwrite a stale cached total, something else), and what does invoice-drift measure against (a source ledger, a prior export, a reconciliation report)?
Fallback (cut the unproven claim, let the next sentence carry the evidence): "The billing job runs a ledger-fold pass after each import and finishes it before the nightly export starts. Because the export reads only folded rows, it never emits an invoice total computed from an import that has not yet been folded."

Rewrite check: No rule-of-three, no X-not-Y / negative parallelism, no em-dash antithesis, no avoid-by-default phrases, no prestige adjectives, no decorative closure, no invented facts — the fallback reuses only the timing and row-scope details already in the source and drops the unproven accuracy claim instead of re-asserting it under new wording. Passes self-detectors.

Remembered line: "the export reads only folded rows" — the one claim in the paragraph precise enough to check, and the fact the fallback rewrite is built around.
