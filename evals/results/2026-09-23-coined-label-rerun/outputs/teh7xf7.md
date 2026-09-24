Verdict: keep

Slop tells: None found. Every actor is named (the billing job, ledger-fold passes, the nightly export) and every verb does real work — runs, finishes, starts, reads — rather than a displaced copula ("serves as," "represents," etc.). Nothing from the avoid-by-default phrase list or the high-risk word list appears. No rule-of-three, no "Not X. Y." rhythm, no hedged symmetry ("whether X or Y"), no em-dash cadence (there are no em-dashes at all), and no decorative antithesis — the two sentences add distinct facts rather than setting up a contrast.

Specificity missing: None. "ledger-fold passes," "invoice-drift totals," and "folded rows" are the same concrete nouns carried across both sentences rather than swapped for vaguer synonyms on a second mention, and the paragraph states two separate, checkable guarantees (fold-completes-before-export, export-reads-only-folded) instead of one vague assurance.

Inflated claim: "so invoice-drift totals stay accurate" reads like a claim of importance, so apply the emphasis-source test: flatten it to "fold passes run after every import, finish before the export starts, and the export reads only rows a fold has touched." The flattened version still names the actor (the fold pass), the trigger (each import), and the boundary condition (unfolded rows are excluded from the export) — the claim survives losing its cadence, so the idea is carrying the sentence, not borrowed emphasis. Earned, not inflated.

Flow break: None. Sentence 2 answers the question sentence 1 raises — how does folding after import actually keep the export correct? — with a dependency relation: a timing guarantee (each pass finishes before the export starts) plus an independent scope guarantee (the export reads only folded rows). The second guarantee is not a restatement of the first: it is what protects the export if a fold pass from a very recent import were still in flight when the export starts. Both clauses are load-bearing, so nothing here is a list-like juxtaposition.

Concrete rewrite: Not applicable — no slop tell was flagged, so nothing needs replacing. Nothing can be cut for length either: dropping the timing clause or the read-scope clause would drop one of the two independent guarantees the paragraph is making.

Rewrite check: Not applicable — no rewrite was produced under a keep verdict.

Remembered line: "the export reads only folded rows" — the hard filter is the guarantee worth carrying away; the timing guarantee earlier in the same sentence is the softer, defense-in-depth half.
