Verdict: ask-author

Slop tells: No stock AI cadence here — no rule-of-three, no "Not X. Y." parallelism, no decorative em-dashes, no hedged symmetry, no banned stock phrases, no prestige adjectives. Sentence 2's "Because the check happens at the head, ... rather than at read time" is exactly the hypotactic, relation-naming sentence this doctrine wants. The real problems are two coined compound labels ("exact-head checks," "editorial-row layouts") that aren't fully defined, and a claim in sentence 1 that outruns the mechanism sentence 2 actually supplies.

Specificity missing: "Exact-head check" gets a location ("at the head") but not a comparison target — exact match of what: row content, a hash, row count, schema? "Editorial-row layout" is never unpacked — what makes a row "editorial," and does "layout" mean row order, column shape, or formatting? Both terms have the texture of precision without a referent the reader can check.

Inflated claim: "so editorial-row layouts stay consistent across shards" asserts a guarantee. The only mechanism given is that the check makes drift "surface ... during the merge" — that's detection, not correction. Surfacing a problem at merge time only produces consistency if something then happens to the merge (block it, retry it, repair the divergent replica); the paragraph never says what. Sentence 1 claims more than sentence 2 proves.

Flow break: Sentence 2 is framed as backing sentence 1 ("Because the check happens at the head...") but it actually narrows the claim: it establishes *when* drift becomes visible, not that the drift stops existing. The paragraph needs a hinge that either states the corrective step after detection or downgrades "stay consistent" to match "surfaces."

Concrete rewrite: Ask author: when the exact-head check finds drift between replicas at merge time, what happens next — does the merge get blocked, does it fire an alert, or is the divergent replica repaired? That answer is what would earn "stay consistent." Fallback if it can't be confirmed: "The indexer runs exact-head checks before each merge, so drift in editorial-row layouts surfaces at merge time rather than later, when a reader would hit it." This keeps both coined terms as given instead of guessing their internals, and trades the unproven "stay consistent" for the weaker claim the passage actually supports.

Rewrite check: The fallback has no rule-of-three, no "X, not Y" / negative parallelism, no em-dash antithesis, no avoid-by-default phrase, no prestige adjective, no decorative closer, and no invented name, count, tool, or timing — it reuses only "surfaces ... rather than at read time" from the source sentence. Passes self-detectors.

Remembered line: Because the check runs at the head, replica drift surfaces at merge time, not later when a read exposes it.
