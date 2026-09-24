Verdict: ask-author

Slop tells: No banned avoid-by-default phrases, copula displacement, hedged symmetry, em-dash cadence, rule-of-three, or "Not X. Y." staccato. The one detector that fires is coined compound labels: "ledger-fold" and, more mildly, "invoice-drift" name a process and a metric the paragraph never defines.

Specificity missing: "Ledger-fold" appears in three forms (the job runs "ledger-fold passes," a "pass" finishes, the export reads "folded rows") but the paragraph only ever names the output state, never the transformation. We learn that a row becomes "folded" — not what folding computes (dedup? correction? merge into a running balance?). Per the coined-compound-label test, that's a name standing in for a mechanism: "fold" isn't a standard ledger/billing term the way "dead-letter queue" or "two-phase commit" are, so it doesn't clear the domain-standard bar, and the passage never defines it in place. "Invoice-drift" gets a lighter version of the same gap: it reads as an application of the standard "data drift / config drift" sense (a value diverging from an expected one over time), which is common enough usage to keep, but the paragraph never says what the drift is measured against, so a reader can't independently check the claim.

Inflated claim: "so invoice-drift totals stay accurate" claims more than the rest of the paragraph proves. The two mechanisms actually given — the pass finishes before the export starts, and the export reads only folded rows — are read-ordering and filtering guarantees: together they keep the export from ever reading a row before its import has been folded in. That secures freshness and read-consistency. It does not establish that the fold computation itself is arithmetically correct. The "so" treats a consistency guarantee as if it were a correctness proof.

Flow break: None. The second sentence answers the question the first one raises — how do you know the export isn't reading stale or half-folded data? — and the "and" correctly coordinates two independent safeguards (a timing barrier, a read filter) instead of falsely subordinating one to the other.

Concrete rewrite: Ask author: what does a ledger-fold pass do to a row — deduplicate it, apply a correction, merge it into a running balance, something else? And what is invoice-drift measured against (a prior total, an upstream source, a reconciliation target)? Until that's answered, the defensible fallback keeps "ledger-fold" as a named term — the paragraph doesn't need to explain it to support the ordering claim — but narrows the causal claim to what the two stated mechanisms actually prove:

```
The billing job runs ledger-fold passes after each import. Each pass finishes
before the nightly export starts, and the export reads only folded rows, so
the export never reads a row before its import has been folded in.
```

This drops "invoice-drift totals stay accurate" — a claim about the fold's arithmetic that this paragraph doesn't support — and keeps only the read-consistency claim the stated mechanisms earn.

Rewrite check: passes self-detectors. No rule-of-three, no X-not-Y / negative parallelism, no em-dash antithesis, no avoid-by-default phrases, no prestige adjectives, no decorative closure. No invented facts: "ledger-fold" is left undefined rather than glossed with a guessed mechanism, and the rewrite's closing claim ("the export never reads a row before its import has been folded in") is a direct restatement of the two premises already in the source, not a new one.

Remembered line: The source already has it: "the export reads only folded rows." Concrete, checkable, and specific enough to keep verbatim as the paragraph's anchor.
