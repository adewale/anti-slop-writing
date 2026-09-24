Verdict: revise

Slop tells: Two, both versions of the core failure ("less detail, more importance"). (1) Coined compound label: "ledger-fold pass" is never defined. The only nearby support — "the export reads only folded rows" — names the output state (folded vs. not), not the transformation. It relocates the gap instead of resolving it. (2) Evidence/claim mismatch: "so invoice-drift totals stay accurate" promises that the scheduling relationship causes accuracy, but sentence two only proves that the export never reads a partially-folded row. That is a read-consistency guarantee, not a correctness guarantee.

Specificity missing: What folding does to a row (merge duplicate entries? net out adjustments? reconcile against a source ledger?), what causes invoice drift in the first place, and what "accurate" is checked against are all unstated.

Inflated claim: "stay accurate" overclaims what the mechanism proves. Ordering plus read-scope guarantee that the export always reads complete, finished output; they say nothing about whether the fold computation itself is correct. A bug in the fold logic would satisfy this same guarantee while producing consistently wrong totals.

Flow break: Sentence two functions as evidence for sentence one's claim, but the relation is left implicit across the sentence boundary — a "because" would state it instead of relying on adjacency.

Concrete rewrite:
```txt
The billing job runs a ledger-fold pass after each import, and each pass finishes before the nightly export starts. Because the export reads only folded rows, every invoice-drift total it reports comes from a finished pass.
```
Every noun here is carried over from the source (billing job, ledger-fold pass, import, nightly export, folded rows, invoice-drift total); nothing is invented. It states the guarantee the mechanism actually supports — completeness of what's read — instead of "accurate," which the mechanism doesn't establish. Keeping the "accurate" framing would need one fact this paragraph doesn't supply: what the fold computes and what baseline the drift totals are checked against. That is a question for the author, not something to invent here.

Rewrite check: No rule-of-three, no X-not-Y/negative parallelism, no em-dash antithesis, no banned avoid-by-default phrase, no prestige adjective, no decorative closure, no invented facts. Passes self-detectors.

Remembered line: What's provable here is that the export reads only folded rows and every pass finishes before export starts — the ordering guarantee, not the word "accurate," is what this paragraph actually earns.
