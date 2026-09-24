Paragraph under review:

> The billing job runs ledger-fold passes after each import, so invoice-drift totals stay accurate. Each pass finishes before the nightly export starts, and the export reads only folded rows.

Verdict: ask-author

Slop tells:
The paragraph is largely clean of the usual AI-cadence tells — no banned phrases, no high-risk words (crucial, robust, seamless, etc.), no rule-of-three, no "Not X. Y." rhythm, no em-dash, no copula displacement, no hedged symmetry, no outline-shaped conclusion. The actors and actions are concrete: billing job, ledger-fold pass, nightly export. The real hit is coined compound labels: "ledger-fold passes" and "invoice-drift totals" are compound terms that name a process and a metric the paragraph never defines, and neither is a standard industry term the way "dead-letter queue" or "two-phase commit" would be. The passage does partly earn one piece of this: by the second sentence, "folded" works as a defined predicate — a row the fold pass has processed, as opposed to one it hasn't — so that detail is keep-worthy. But "fold" as an operation (what does it compute?) and "drift" as a metric (drift between what two values, caused by what?) stay unresolved. A name is not a mechanism.

Specificity missing:
- What does a ledger-fold pass compute — re-sum ledger entries into a running per-invoice balance, apply the latest correction entries, collapse duplicate postings, something else?
- What is "invoice-drift," concretely — drift between the invoice total and the sum of its ledger entries? Between two currencies? Between a cached total and a recomputed one? And what produces the drift that folding then removes (out-of-order imports, retried imports, rounding)?
- Sentence 2 gives two guarantees: pass-before-export ordering, and export-reads-only-folded-rows. The paragraph never says whether the second is a consequence of the first (a backstop in case ordering ever slipped) or whether unfolded rows can exist for an unrelated reason (e.g. a separate ingestion path). That distinction changes how much confidence the "stay accurate" claim deserves.

Inflated claim:
"so invoice-drift totals stay accurate" claims a correctness outcome, but the only mechanism the paragraph actually demonstrates — pass finishes before export starts, export reads only folded rows — shows completeness, i.e. the export can't see a partially processed import. It does not show correctness of the fold computation itself. A pass that ran to completion but computed the wrong fold would still satisfy both guarantees and still produce inaccurate totals. The sentence borrows the weight of a real ordering guarantee to back a broader accuracy claim it doesn't fully cover.

Flow break:
Minor. The link between sentence 1's claim ("stay accurate") and sentence 2's mechanism (ordering + filter) is left as a bare "and" — parataxis where a dependency is intended. The reader has to infer that sentence 2 is offered as the reason for sentence 1's claim; making that explicit would also surface the gap named above, since the mechanism shown backs completeness, not correctness.

Concrete rewrite:
Ask author: what does a ledger-fold pass actually compute, and what does "invoice-drift" measure — drift between which two values, caused by what?

Fallback (no invented mechanism; keeps only what the paragraph already demonstrates, and makes the dependency explicit instead of leaving it as "and"):

"The billing job runs a ledger-fold pass after each import. The nightly export starts only once that pass finishes, and reads only the rows the pass has folded."

This drops the unsupported "invoice-drift totals stay accurate" claim rather than propping it up with an invented fold algorithm, and switches the second sentence from parataxis ("and") to an explicit dependency ("only once ... finishes").

Rewrite check:
No rule-of-three, no X-not-Y / negative parallelism, no em-dash antithesis, no banned avoid-by-default phrases, no prestige adjectives, no decorative closure, no invented facts — the rewrite removes a claim rather than fabricating the mechanism that would earn it. Passes self-detectors.

Remembered line:
"the export reads only folded rows" — the one detail in the paragraph a reader could go verify directly against the code, and the detail any rewrite should stay anchored to.
