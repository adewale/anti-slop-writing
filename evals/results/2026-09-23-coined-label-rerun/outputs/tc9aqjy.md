Verdict: keep

Slop tells: None. Checked against the full detector list: no copula displacement (plain verbs throughout — "runs," "finishes," "reads," "stay"), no hedged symmetry, no em-dash cadence (no dashes present), no rule-of-three, no "Not X. Y." rhythm, no banned avoid-by-default phrases, no high-risk/prestige vocabulary, no decorative bullet/bold/table structure. The "and" joining "Each pass finishes before the nightly export starts" and "the export reads only folded rows" is parataxis, but it's a single earned instance, not a density problem: the two clauses name two independent guarantees (temporal completion order, and row-level read scope), not one relation split into two beats for rhythm. Forcing hypotaxis here ("Because each pass finishes before export starts, the export reads only folded rows") would invent a false causal link between two separate mechanisms, so parataxis is the correct choice, not a tell.

Specificity missing: None that undermines the claim. The paragraph names the actor (the billing job), the mechanism (ledger-fold passes), the trigger (after each import), and two distinct guarantees (finishes before the nightly export starts; export reads only folded rows). It doesn't define what folding does internally, but the paragraph's job is to state the ordering/scope guarantee, not the fold algorithm — that's a scope choice, not a gap.

Inflated claim: None. "Invoice-drift totals stay accurate" is a strong claim standing alone, but the second sentence earns it rather than asserting it on cadence: the export can never see unfolded rows, both because of timing (pass finishes first) and because of scope (filtered to folded rows only). Per false-positive restraint, the same paragraph supplies the mechanism, so the claim holds as written.

Flow break: None. Sentence 1 states the mechanism and outcome; sentence 2 answers the question sentence 1 raises — how do you know the export isn't reading stale, unfolded data — with the two guarantees. That's a dependency relation (sentence 2 is why sentence 1 is true), not two facts placed side by side.

Concrete rewrite: Not required. Actor, mechanism, trigger, and both guarantees are already named; nothing here needs an ask-author fallback because no fact is missing.

Rewrite check: No new prose was introduced — original retained verbatim. Run against the same detectors: no rule-of-three, no X-not-Y/negative parallelism, no em-dash antithesis, no banned avoid-by-default phrases, no prestige adjectives, no decorative closure, no invented facts. Passes self-detectors.

Remembered line: "the export reads only folded rows" — the sharpest, most checkable detail in the paragraph, and the fact to verify first if invoice-drift ever reappears.
