Reviewed paragraph:
"The indexer runs exact-head checks before each merge, so editorial-row layouts stay consistent across shards. Because the check happens at the head, drift between replicas surfaces during the merge rather than at read time."

Verdict: keep

Slop tells: None. No avoid-by-default phrases, no high-risk words (delve, realm, tapestry, testament, pivotal, crucial, underscore, seamless, robust, etc.), no rule-of-three, no "Not X. Y." negative parallelism, no em-dash cadence, no copula displacement ("runs," "stay," "happens," "surfaces" are concrete action verbs, not "serves as" / "stands as" / "represents"), no hedged symmetry ("Whether... or..."), no canned emphasis, no bullet/bold/table fake structure.

Specificity missing: None. The paragraph names a specific actor (the indexer), a specific mechanism (exact-head checks, run before each merge), a specific outcome (editorial-row layouts stay consistent across shards), and a specific timing tradeoff (drift caught during the merge rather than at read time). No vague actor or unproven importance claim stands in for a mechanism.

Inflated claim: None. Both sentences stay scoped to what the mechanism does; no significance language ("crucial," "underscores," "transformative") is layered on top of the claim.

Flow break: None. Sentence two is hypotactic ("Because... rather than...") and names the relation explicitly instead of implying it through cadence, answering a real next question raised by sentence one: not just what the check does (keep layouts consistent) but what checking at that point in the pipeline buys you (drift is caught at merge, before a read would expose it). Applying the staccato contrast test to "during the merge rather than at read time": side A ("during the merge") is directly evidenced by "the check happens at the head" in the same sentence; side B ("at read time") is the direct logical complement of a check placed before merge, not an unsupported rhetorical leap. This is earned contrast, not compressed or decorative.

Concrete rewrite: Not needed. No slop tell is flagged to fix or cut; the source paragraph already is the concrete version — named actor, named mechanism, named consequence, named timing tradeoff.

Rewrite check: N/A — no rewrite was produced. Ran the same detector pass on the source in its place (see Slop tells above): no rule-of-three, no X-not-Y / negative parallelism, no em-dash antithesis, no banned avoid-by-default phrases, no prestige adjectives, no decorative closure, no invented facts. Passes self-detectors.

Remembered line: "Because the check happens at the head, drift between replicas surfaces during the merge rather than at read time." Already concrete — it states the reusable structure (catch drift where the check sits, not where the data is later read) without needing a rewrite.
