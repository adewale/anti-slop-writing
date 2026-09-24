Paragraph reviewed:

> The billing job runs ledger-fold passes after each import, so invoice-drift totals stay accurate. Each pass finishes before the nightly export starts, and the export reads only folded rows.

Verdict: keep

Slop tells: None. Checked against the full detector list — no rule-of-three, no "Not X. Y." rhythm, no em-dash cadence, no hedged symmetry ("whether you're X or Y," "while X, Y is also important"), no copula displacement (the verbs are plain and literal — runs, finishes, starts, reads — not "serves as"/"stands as"/"represents"), no banned-by-default phrases, no high-risk words (no "robust," "seamless," "crucial," "underscore," etc.), no bullet/bold/table fake structure. The nouns ("ledger-fold passes," "invoice-drift totals," "folded rows") are domain mechanism names carrying real information, not prestige abstractions standing in for missing detail.

Specificity missing: None. The paragraph names a specific actor (the billing job), a specific process (ledger-fold passes), a specific trigger (after each import), a specific competing process (the nightly export), and a specific filter condition (reads only folded rows). There is no vague actor ("the system," "it is believed") to replace with a named source.

Inflated claim: "so invoice-drift totals stay accurate" reads on first pass like the kind of importance claim the core principle warns about — an accuracy claim without visible support. Applying the false-positive-restraint check: the next sentence supplies the mechanism that earns it — a completion-ordering guarantee (each fold pass finishes before the export starts) plus a read-scope guarantee (the export reads only folded rows). Both are concrete, checkable conditions, not borrowed emphasis. Emphasis-source test: flattened, the claim reads "fold passes run after import; every pass finishes before export runs; export reads only folded rows" — the residual claim still names the actor and the two guarantees, so the idea is carrying the weight, not the cadence. This keeps the claim earned rather than inflated.

Flow break: None. The two sentences sit in a dependency relation, and the relation is named through connectives rather than left to adjacency: sentence 1 states the outcome ("stay accurate"), and sentence 2 answers the question that outcome raises — accurate how? — with "before" (ordering) and the scoping fact ("only folded rows"). That is hypotaxis doing real work, not parataxis papering over a gap. The one coordinating "and" in sentence 2 joins two independent guarantees (timing, scope) rather than standing in for an unstated cause/contrast/consequence the reader would have to guess at, so it does not need converting to a subordinate clause.

Concrete rewrite: Not needed. No slop tell was flagged, so there is nothing to cut or replace; rewriting a paragraph that already states actor, mechanism, and scope condition would trade earned specificity for restated specificity.

Rewrite check: N/A — no rewrite was produced (verdict: keep). Running the same detectors on the source paragraph itself: no rule-of-three, no X-not-Y / negative parallelism, no em-dash antithesis, no banned avoid-by-default phrases, no prestige adjectives, no decorative closure ("that was the point," "in conclusion," "overall," "ultimately"), no invented facts. Passes self-detectors.

Remembered line: "the export reads only folded rows" — the one clause a reader could hold onto and use to check the accuracy claim against actual system behavior.
