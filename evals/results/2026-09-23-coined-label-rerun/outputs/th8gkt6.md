Paragraph reviewed:

> The indexer runs exact-head checks before each merge, so editorial-row layouts stay consistent across shards. Because the check happens at the head, drift between replicas surfaces during the merge rather than at read time.

Verdict: ask-author

Slop tells: Coined compound labels. "Exact-head checks" and "editorial-row layouts" are hyphenated, technical-sounding names for a check and a row category that the paragraph never defines in place, and neither is an established domain term the way "dead-letter queue" or "two-phase commit" would be. The hyphens supply a texture of precision the sentence doesn't back up with a referent.

Specificity missing: The paragraph never says what the check actually compares at "the head" — a content hash, a row count, schema/column order, something else. It never says what makes a row "editorial" as opposed to any other row the indexer handles. And it never says what happens once drift is found mid-merge (does the merge abort, retry, get flagged for someone to reconcile?). "The check happens at the head" supplies a location and a timing, not a mechanism.

Inflated claim: The first sentence claims the check's effect is that "editorial-row layouts stay consistent across shards." The second sentence describes a narrower effect: drift "surfaces during the merge" — the check makes an inconsistency visible earlier, not that it removes or prevents the inconsistency. Surfacing a problem sooner is not the same claim as the problem stopping. Nothing in the paragraph names the corrective step that would actually make layouts "stay consistent," so the "so" in sentence one claims more than sentence two supports.

Flow break: "Because the check happens at the head" answers when drift is caught, which is a fine hypotactic move, but it doesn't answer the question sentence one raised: what makes the layouts consistent, not just checked. The paragraph moves from a consistency claim to a detection-timing explanation without a bridge between the two.

Concrete rewrite:
Ask author: what does the exact-head check compare — a content hash, a row count, schema/column order, something else? What distinguishes an "editorial" row from any other row the indexer handles? And what happens to the merge once drift is detected — does it block, retry, or get flagged for manual reconciliation?
Fallback (cut, using only what the paragraph already supports): "The indexer compares each shard's head state before merging. Because that comparison happens at the head, drift between replicas surfaces during the merge rather than at read time."
This fallback drops the unsupported "stay consistent" claim and the undefined "editorial-row" label rather than guessing at either.

Rewrite check: The fallback contains no rule-of-three, no X-not-Y/negative parallelism, no em-dash antithesis, none of the banned avoid-by-default phrases, no prestige adjectives, and no decorative closer ("that was the point," "in conclusion," "overall," "ultimately"). It does not invent what the check compares, what makes a row "editorial," or what happens once drift is found — those stay as open questions in the ask-author line rather than being filled with a confident-sounding guess. Passes self-detectors.

Remembered line: "Because the check happens at the head, drift between replicas surfaces during the merge rather than at read time." That's the one claim in the paragraph the described mechanism actually earns — build the rewrite around it instead of around "stay consistent."
