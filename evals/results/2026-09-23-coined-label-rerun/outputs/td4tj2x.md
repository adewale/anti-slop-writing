Verdict: keep

Slop tells: None found against the source-backed detectors. No undue-significance language, no canned emphasis, no negative parallelism, no rule-of-three, no formulaic em-dash cadence (no em-dashes at all), no copula displacement ("runs," "finishes," "starts," "reads" are all plain, concrete verbs doing real work, not "serves as"/"stands as"/"represents" substitutes), no hedged symmetry ("Whether X or Y" / "While X, Y is also important"), and no bullet/bold/table fake structure. No avoid-by-default phrase or watch-list word appears.

Specificity missing: None. The paragraph already names a specific actor (the billing job), a specific mechanism (ledger-fold passes run after each import), a specific downstream consumer (the nightly export), and a specific guard condition (reads only folded rows) — not vague stand-ins like "the system" or "the process."

Inflated claim: None. "stay accurate" reads as a quality claim but is earned, not inflated: the second sentence supplies the two mechanisms that make it true — an ordering guarantee (each pass finishes before the export starts) and a filter guarantee (the export reads only folded rows). Per the false-positive restraint rule, when the same paragraph supplies the mechanism that earns a quality word, the verdict is keep, not a flag.

Flow break: None. Sentence 1 makes a causal claim ("X, so Y"); sentence 2 answers the question that claim raises — what actually enforces it? — with the two guarding mechanisms, which is a level-of-detail move (claim, then supporting mechanism) rather than two facts placed beside each other in a merely plausible order. The "and" joining the two guarantees in sentence 2 is correct parataxis, not a hypotaxis violation: the ordering guarantee and the read-filter guarantee are independent safeguards, not one causing the other, so subordinating them (e.g., "Because each pass finishes before export, the export reads only folded rows") would invent a dependency the source does not state.

Concrete rewrite: Not applicable — no slop tell was flagged, so no rewrite is offered. The paragraph already matches the doctrine's target style: named actor, concrete mechanism, verifiable outcome.

Rewrite check: N/A, no rewrite was produced. Re-running the detectors on the source itself as a check: it contains no rule-of-three, no X-not-Y/negative parallelism, no em-dash antithesis, no avoid-by-default phrase, no prestige adjective, no decorative closure ("That was the point," "In conclusion," "Overall," "Ultimately"), and no invented fact. Passes self-detectors.

Remembered line: "the export reads only folded rows" — the one clause a reader could go check against the code or the logs.
