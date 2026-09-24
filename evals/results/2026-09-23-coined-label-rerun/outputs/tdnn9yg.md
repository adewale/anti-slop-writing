Paragraph reviewed:
"The billing job runs ledger-fold passes after each import, so invoice-drift totals stay accurate. Each pass finishes before the nightly export starts, and the export reads only folded rows."

Verdict: revise

Slop tells:
- Coined compound labels: "ledger-fold" and "invoice-drift" are hyphenated process/artifact names the paragraph never defines, and neither is standard industry terminology (unlike "dead-letter queue" or "two-phase commit"). Applying the false-positive-restraint test: sentence 2 gives "ledger-fold" partial support — it names a boundary (pass completes before export starts; export reads only folded rows), so "folded" points to an inspectable row state, not pure abstraction. "Invoice-drift" gets no such support anywhere in the paragraph: no cause, no measurement, no failure mode is named. The hyphen supplies precision the term itself doesn't pay for.
- No cadence tells: no rule-of-three, no em-dash antithesis, no hedged symmetry, no displaced copula, no banned filler phrases, no watch-list words. The paragraph isn't leaning on rhythm to sound true, so this is a light, targeted flag, not a rewrite-from-scratch.

Specificity missing:
- What does a ledger-fold pass actually do to a row? The paragraph gives its schedule (after each import, done before export) and its output label ("folded"), not its operation (dedupe by invoice ID, recompute a running balance, something else).
- What is invoice-drift, concretely — a rounding gap, a mismatch between two systems, a stale total from a retried import? No definition or example is given.
- Optional next step: ask the author what a ledger-fold pass computes and what specifically causes drift without it. Don't guess a mechanism to fill this gap; the rewrite below avoids inventing one and still stands on its own.

Inflated claim:
"so invoice-drift totals stay accurate" claims a correctness property, but the paragraph only proves a scope guarantee: the export excludes rows the current fold pass hasn't reached. That shows the export can't see in-progress data — it doesn't show the fold computation itself is correct. "Accurate" borrows more weight than the two stated mechanisms (ordering, selective read) actually carry.

Flow break:
Sentence 2 is the evidence for sentence 1's claim, but the paragraph never says so. It reads as two adjacent facts (a claim, then separate facts) instead of claim-then-proof; the reader has to infer that the pass-before-export ordering and the folded-only read are *why* the "so" in sentence 1 holds.

Concrete rewrite:
The billing job runs a ledger-fold pass after each import. Because that pass finishes before the nightly export starts and the export reads only folded rows, invoice-drift totals reflect only imports whose fold has completed.

Rewrite check: no rule-of-three, no X-not-Y / negative parallelism, no em-dash antithesis, no banned avoid-by-default phrases, no prestige adjectives, no decorative closure, no invented facts — "ledger-fold" and "invoice-drift" are kept exactly as given rather than assigned a guessed mechanism, and "stay accurate" is narrowed to the scope guarantee the source actually proves. Passes self-detectors.

Remembered line:
"the export reads only folded rows" — the one claim in the paragraph a reader could go verify directly, by checking the export query's filter. Keep the paragraph anchored here; if "ledger-fold" and "invoice-drift" get a one-clause gloss later, attach it to this line rather than to "stay accurate."
