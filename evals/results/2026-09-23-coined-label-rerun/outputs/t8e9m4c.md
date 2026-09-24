Reviewing:

> The billing job runs ledger-fold passes after each import, so invoice-drift totals stay accurate. Each pass finishes before the nightly export starts, and the export reads only folded rows.

Verdict: revise

Slop tells:
- Coined compound labels not fully defined: "ledger-fold passes" and "invoice-drift totals" name a process and a failure mode the paragraph never spells out. Partial credit: sentence 2 shows a pass produces a checkable state ("folded rows") that the export filters on, so the gating behavior is resolvable. But what the fold pass actually computes (recomputes balances? dedupes reimported entries? resolves out-of-order writes?), and what "invoice-drift" concretely is, are never named.
- Unstated relation: sentence 2's two facts ("finishes before... starts," "reads only folded rows") are joined with "and" and left sitting next to sentence 1's accuracy claim. The reader has to infer that this is the reason totals stay accurate rather than an unrelated timing detail.
- Claim wider than the evidence given: "stay accurate" promises a correctness property; the two facts in sentence 2 only support a narrower scope/timing guarantee.

Specificity missing:
- What a ledger-fold pass changes or resolves in the ledger.
- What invoice-drift is and how anyone would detect or bound it — a metric, a past incident, a tolerance.
- What "folded" is as a data attribute (a flag, a timestamp, a separate table) — implied by "folded rows" but not stated.

Inflated claim:
"so invoice-drift totals stay accurate" claims the correctness of an underlying computation. The two facts actually given — pass finishes before export starts, export reads only folded rows — only prove that exported totals exclude any row whose fold hasn't finished. That is a real, checkable guarantee, but it is not the same claim as "accurate," which also depends on the fold computation itself being correct, and nothing here shows that.

Flow break:
Sentence 2 is doing the real work of supporting sentence 1's claim, but the paragraph never says so — it just places the two sentences in sequence. Naming the relation closes the gap between claim and evidence instead of leaving the reader to supply it.

Concrete rewrite:
"The billing job runs ledger-fold passes after each import. Each pass finishes before the nightly export starts, and the export reads only folded rows. That ordering means exported totals never include a row from an import whose fold hasn't finished."

This keeps every fact the source gives (actor, ordering, read scope), drops the "invoice-drift... accurate" framing that isn't evidenced, and states the outcome the two given facts actually prove. If the stronger claim is what's wanted: Ask author: what does the fold pass compute, and what does "invoice-drift" mean or how is it measured? Fallback if that isn't available: keep the narrower ordering/scope claim above and cut the accuracy framing.

Rewrite check:
No rule-of-three, no X-not-Y / negative parallelism, no em-dash, no banned avoid-by-default phrases, no prestige adjectives, no decorative closer. "Never include a row from an import whose fold hasn't finished" restates the source's own two facts (ordering + read-scope) rather than inventing a mechanism, count, or timing. Passes self-detectors.

Remembered line:
"The export reads only folded rows" — the one claim in the paragraph a reader could go verify directly against the code. The source already ends near this concrete fact instead of a generic thesis, which is the right instinct; the rewrite keeps that fact as the actual payoff rather than subordinating it to the unearned "accurate" claim that opens the paragraph.
