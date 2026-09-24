```txt
Verdict: ask-author

Slop tells: Two coined compound labels carry the paragraph's whole claim without being defined: "exact-head checks" names a check but never says what it compares, and "editorial-row layouts" names a structure but never says what makes a row "editorial" or what "consistent" means for its layout. The closing comparison, "surfaces during the merge rather than at read time," is a compressed antithesis: the merge-time side is supported by sentence one (the check runs before each merge), but nothing in the paragraph supports the read-time side, so the comparison is asserted rather than shown.

Specificity missing: What "exact" compares at the head (a hash, a revision id, a specific field, a full-row diff) is not stated. What distinguishes an editorial row from any other row the indexer handles is not stated. What a client would actually see at read time if head drift went uncaught (a stale value, a missing row, mismatched columns across shards) is not stated.

Inflated claim: "Drift between replicas surfaces during the merge rather than at read time" is scoped wider than the mechanism it follows from. The check inspects only the head, so at most it catches head drift before merge; the sentence generalizes this to "drift" without that qualifier, which reads as a guarantee — no drift ever reaches read time — that an exact-head check alone cannot establish.

Flow break: None. "Because the check happens at the head" correctly subordinates cause to effect, and the second sentence answers a question the first raises: what checking at the head buys you. The paragraph's problem is undefined terms and an unqualified claim, not broken sequencing.

Concrete rewrite: Ask author: what does the exact-head check compare — a hash of the head row, a revision id, a specific field, or a full-row diff? What defines a row as editorial, as distinct from any other row the indexer handles? And what would a client actually see at read time if head drift went uncaught? Fallback without those facts, tightening only what the passage's own mechanism already supports: "The indexer runs an exact-head check before each merge, so editorial-row layout stays consistent across shards. Because that check compares the head, head drift between replicas is caught at merge time rather than surfacing later when a client reads the row." This keeps "exact-head check" and "editorial-row," which the author can define precisely, and narrows only the one claim the stated mechanism can support: head drift, not drift in general.

Rewrite check: The questions and the fallback contain no rule-of-three, no X-not-Y/negative parallelism, no em-dash antithesis, no avoid-by-default phrases, no prestige adjectives, no decorative closure, and no invented facts — the fallback names the same two undefined terms rather than guessing at them. Passes self-detectors.

Remembered line: "Exact" is a claim about what gets compared; this paragraph names where the comparison happens (the head) but never what it checks.
```
