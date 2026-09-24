Verdict: keep

Slop tells: None. No banned-by-default phrases, no high-risk/prestige vocabulary, no copula displacement ("runs," "finishes," "reads" are plain concrete verbs, not "serves as" / "represents"), no hedged symmetry ("whether... or"), no em-dash cadence (no em-dashes appear at all), no rule-of-three, no "not X, Y" / negative parallelism, no decorative antithesis, no canned emphasis, no bullet/bold/table fake structure.

Specificity missing: None load-bearing. The paragraph names an actor (the billing job), a mechanism (ledger-fold passes), a trigger (after each import), a metric (invoice-drift totals), a second job (the nightly export), an ordering constraint (each pass finishes before the export starts), and a filter (the export reads only folded rows). Nothing here is vague enough to need an ask-author fallback.

Inflated claim: "stay accurate" could look like an unearned outcome claim if it stood alone, but apply the emphasis-source test: flatten the sentence to "The billing job runs ledger-fold passes after each import; that keeps invoice-drift totals accurate" and the residual claim still names an actor and a mechanism, so it lands on content rather than cadence. This is the same shape as the doctrine's "robust queue" keep example — the qualifier ("accurate," like "robust") is earned by a mechanism named in the same sentence, not asserted on its own. Keep on this clause.

Flow break: None. Sentence 2 answers the question sentence 1 raises — what protects the export specifically — with two separately-stated, checkable guarantees: pass-before-export ordering, and a folded-rows-only read filter. They're joined with "and" rather than "because," and that is the correct choice: forcing a causal connective would assert the read filter exists *because of* the timing guarantee, a dependency the paragraph never establishes (the filter could just as easily be an independent safeguard). Inventing that link to satisfy a hypotaxis preference would be a worse failure than the coordinate "and." This is hypotaxis correctly withheld, not parataxis defaulting.

Concrete rewrite: Not needed. A rewrite here would either restate the same mechanism in different words or invent an unstated causal link between "each pass finishes before the export starts" and "the export reads only folded rows" — both moves the skill argues against (no invented mechanisms, no cadence-only tightening). Retained as-is:

"The billing job runs ledger-fold passes after each import, so invoice-drift totals stay accurate. Each pass finishes before the nightly export starts, and the export reads only folded rows."

Rewrite check: Running the source-backed detectors against the retained text: no rule-of-three, no X-not-Y / negative parallelism, no em-dash antithesis, no banned avoid-by-default phrases, no prestige adjectives, no decorative closure ("that's the point," "in conclusion," "overall," "ultimately"), no invented facts. Passes self-detectors.

Remembered line: "the export reads only folded rows" — the one guarantee a reader can go verify directly against the export's query, rather than a paraphrase of "accuracy."
