Verdict: keep

Slop tells: None. No avoid-by-default phrases, no high-risk words, no copula displacement ("runs," "finishes," "reads," "stay" are all plain verbs doing concrete work), no hedged symmetry, no em-dash clusters (no em-dashes at all), no rule-of-three, no "Not X. Y." negative parallelism, no bullet/bold/table fake structure.

Specificity missing: None. The actor is named (the billing job), the mechanism is named (ledger-fold passes), the trigger is named (after each import), the ordering guarantee is named (each pass finishes before the nightly export starts), and the read-scope guarantee is named (the export reads only folded rows). There is no vague actor or unnamed process that would need an ask-author note.

Inflated claim: None. "Invoice-drift totals stay accurate" is a bounded, checkable claim, not a significance flourish — the second sentence immediately supplies the specific mechanism (timing plus row scope) that earns it, rather than just asserting importance and moving on.

Flow break: None. Sentence 1 states the mechanism and its result; sentence 2 answers the question sentence 1 raises — what makes that accuracy claim hold — with two guarantees: timing (each pass finishes before the export starts) and scope (the export reads only folded rows). That is a resolution / level-of-detail relation, not two facts placed side by side. Inside sentence 2, "and" coordinates two guarantees that both have to hold, not one causing the other — the row filter is not a consequence of the timing, it is an independent safeguard — so this is earned parataxis (the sequence itself is the point), not an unstated relation that needs forcing into "because."

Concrete rewrite: None needed. The paragraph already does what the doctrine asks generic prose to earn its way back to: a named actor, a named mechanism, a named trigger, and a two-part guarantee a reader could go verify against the code.

Rewrite check: No rewrite was produced (verdict: keep), so the original stands as the reviewed text. Checked against the same detectors run on the source: no rule-of-three, no X-not-Y / negative parallelism, no em-dash antithesis, no banned avoid-by-default phrases, no prestige adjectives, no decorative closure ("That was the point," "In conclusion," "Overall," "Ultimately"), no invented facts. Passes self-detectors.

Remembered line: "the export reads only folded rows" — the one guarantee in the paragraph a reader could go check against the code.
