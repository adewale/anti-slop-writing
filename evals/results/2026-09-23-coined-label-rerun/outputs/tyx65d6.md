Paragraph reviewed:
> The billing job runs ledger-fold passes after each import, so invoice-drift totals stay accurate. Each pass finishes before the nightly export starts, and the export reads only folded rows.

Verdict: keep

Slop tells: None. Checked against the doctrine detectors — banned-by-default phrases, high-risk words, copula displacement, hedged symmetry, em-dash cadence, rule-of-three, "Not X. Y." rhythm, decorative antithesis, bullet/bold fake structure — none occur. Both sentences use hypotaxis ("so," "before," and an "and" joining two concrete facts) rather than an unstated paratactic juxtaposition, which is what the doctrine asks for when the relation between clauses matters.

Specificity missing: None. The paragraph names the actor (the billing job), the mechanism (ledger-fold passes), the trigger (after each import), the outcome under test (invoice-drift totals), and the export's exact read scope (folded rows only). No abstract noun stands in for a mechanism.

Inflated claim: "so invoice-drift totals stay accurate" looks at first like a bare claim of importance, but under the false-positive restraint it's earned rather than inflated: the very next sentence supplies the mechanism that makes it true — ordering (every fold pass finishes before the nightly export starts) plus scope (the export reads only folded rows). Those two conditions together are what actually stop the export from ever reading a not-yet-folded row. The support arrives one sentence after the claim instead of inside the same clause, but it does arrive, so this is not significance-inflation without evidence.

Flow break: None. The second sentence answers exactly the question the first sentence's "so" raises — why would running fold passes guarantee accuracy? — by naming the two jointly sufficient conditions (finishes-before-export, reads-only-folded-rows). That is a dependency relation between the two sentences, not two facts placed side by side in a plausible order.

Concrete rewrite: Not required — no tell is flagged, so there is nothing to cut or replace. Optional, and not a fix for any flagged problem, purely a compression preference the author can take or leave: "The billing job keeps invoice-drift totals accurate because every ledger-fold pass finishes before the nightly export starts, and the export reads only folded rows." This folds the claim and its two supporting conditions into one hypotactic sentence instead of a claim sentence followed by a separate support sentence.

Rewrite check: passes self-detectors. The optional rewrite above contains no rule-of-three, no X-not-Y / negative parallelism, no em-dash antithesis, no avoid-by-default phrase, no prestige adjective, no decorative closure ("that's the point," "in conclusion," "overall," "ultimately"), and no invented fact — it reuses only the mechanism, actors, and terms already present in the source (ledger-fold pass, nightly export, folded rows).

Remembered line: "the export reads only folded rows" — the one concrete, checkable guarantee in the paragraph; it's the line to go verify first if invoice-drift totals are ever wrong.
