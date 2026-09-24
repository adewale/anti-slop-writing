Verdict: keep

Slop tells: None. No avoid-by-default phrases, no high-risk words (delve/realm/tapestry/crucial/robust/etc.), no copula displacement ("serves as" / "stands as" / "features" / "marks" / "represents"), no hedged symmetry ("whether X or Y," "while X, Y is also important"), no rule-of-three, no "Not X. Y." rhythm, no em-dashes at all, and no unstated-relation parataxis — both sentences are hypotactic, built on "so" and "Because."

Specificity missing: None load-bearing. The actor is named (the indexer), the mechanism is named (exact-head checks, run before each merge), and the consequence is named at two levels: a correctness result (editorial-row layouts stay consistent across shards) and a timing result (drift surfaces at merge rather than at read). "Exact-head" and "editorial-row" are used as established internal terms doing real work in the sentence, not as vague filler standing in for a definition.

Inflated claim: None. "Stay consistent" and "drift... surfaces" are falsifiable operational claims tied directly to where the check runs, not unearned importance language — no prestige adjective (crucial, robust, seamless, powerful) rides on either clause.

Flow break: None. The second sentence is subordinate to the first ("Because the check happens at the head...") and answers the question the first sentence opens: given the check runs pre-merge, when does drift actually get caught? Sentence two answers with a named tradeoff (merge time vs. read time) instead of sitting beside sentence one as a disconnected observation.

Concrete rewrite: Not applicable — no line needs replacing. The paragraph already names an actor, a mechanism, and a specific tradeoff, so there is no generic sentence to swap for a concrete one.

Rewrite check: N/A, no rewrite produced (verdict: keep). Re-running the source-backed detectors on the original text: no rule-of-three, no X-not-Y / negative parallelism, no em-dash antithesis (no em-dashes present), no banned avoid-by-default phrases, no prestige adjectives, no decorative closure, no invented facts. The "during the merge rather than at read time" contrast is carried by hypotaxis ("Because the check happens at the head...") rather than left as an unstated juxtaposition, so it reads as earned, not decorative or compressed antithesis. Passes self-detectors.

Remembered line: "drift between replicas surfaces during the merge rather than at read time" — the specific, checkable tradeoff a reader carries away: this system catches replica drift at merge time instead of letting it surface later as a bad read.
