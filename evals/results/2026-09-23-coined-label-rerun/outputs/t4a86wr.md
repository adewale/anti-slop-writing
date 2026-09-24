Reviewed paragraph:

> The billing job runs ledger-fold passes after each import, so invoice-drift totals stay accurate. Each pass finishes before the nightly export starts, and the export reads only folded rows.

Verdict: keep

Slop tells: None found. No banned phrases from the avoid-by-default list, no high-risk/prestige words (delve, realm, robust, seamless, etc.), no copula displacement (serves as / stands as / marks / represents), no hedged symmetry (whether X or Y), no em-dash cadence, no rule-of-three, no X-not-Y negative parallelism, no bullet/bold-header fake structure, no outline-shaped conclusion.

Specificity missing: None that blocks trust in the claim. "Ledger-fold pass" and "invoice-drift totals" are unglossed domain terms, but they do locating work (naming what runs and what stays accurate) rather than standing in as prestige abstractions for a missing mechanism — the mechanism itself (pass-before-export ordering, folded-rows-only read scope) is spelled out in the same paragraph. No fact is missing that would need an ask-author flag to evaluate the claim as written.

Inflated claim: None. "stay accurate" is a narrow, checkable claim about one specific value (invoice-drift totals), not undue-significance language, and the second sentence immediately supplies the two mechanisms that earn it: a completion-ordering guarantee (each pass finishes before the export starts) and a read-scope restriction (the export reads only folded rows). The claim is checked against evidence inside the same paragraph.

Flow break: None. Sentence 1 states the claim with the relation already named via hypotaxis ("so"). Sentence 2 answers the question sentence 1 raises — how is that guaranteed? — with two concrete, independent supporting facts joined by "and." That "and" coordinates parallel evidence rather than papering over an unstated causal or contrastive leap, so it does not trip the parataxis/unstated-relation failure mode.

Flagged slop tells requiring a rewrite: none.

Concrete rewrite: Not needed. The source already names the actor (the billing job), the mechanism (ledger-fold passes run after each import; passes complete before the nightly export starts; the export's read scope is limited to folded rows), and the result (accurate invoice-drift totals), all in plain verbs (runs, finishes, starts, reads) with no copula displacement to unwind.

Rewrite check: N/A — no rewrite was produced, since the verdict is keep and the source already passes the same detectors a rewrite would be checked against.

Remembered line: "the export reads only folded rows" — this is the concrete guardrail that makes the accuracy claim checkable rather than asserted, and the detail a reader is most likely to carry forward.
