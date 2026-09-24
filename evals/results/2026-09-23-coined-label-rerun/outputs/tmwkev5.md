Paragraph reviewed:

> The indexer runs exact-head checks before each merge, so editorial-row layouts stay consistent across shards. Because the check happens at the head, drift between replicas surfaces during the merge rather than at read time.

Verdict: ask-author

Slop tells: Two undefined coined compound labels carry the paragraph's technical weight: "exact-head checks" and "editorial-row layouts." Neither is a standard domain term (unlike "dead-letter queue" or "two-phase commit"), and neither is defined in place. Sentence 2 reads like it is supplying the mechanism behind sentence 1's claim ("Because the check happens at the head...") but it only repeats "the head" without saying what it is or what "exact" means, so it relocates the specificity gap instead of resolving it. The paragraph also shifts entities mid-argument: sentence 1's consistency claim is about "shards," sentence 2's drift claim is about "replicas," with no statement of whether these are the same partitions or a shard-then-replica hierarchy.

Specificity missing: (1) What the "exact-head" check actually compares: a hash of the head row, a row count, a schema fingerprint, something else. (2) What an "editorial-row layout" physically is: row order, column structure, ID-to-position mapping. (3) Whether "shards" and "replicas" name the same thing here, and whether "the merge" in sentence 1 is the same merge event referenced in sentence 2.

Inflated claim: None. "Stay consistent" and "surfaces during the merge" are modestly scoped claims, not oversold.

Flow break: Sentence 1 raises the obvious next question: what makes the check "exact," what is "the head"? Sentence 2 answers a different question (when drift gets caught) instead of that one, so the reader's first question is never closed. The "because" clause supplies subordination but not a new relation: "the check happens at the head, [so] drift ... surfaces during the merge rather than at read time" mostly restates the timing already implied in sentence 1, which reads as informational density without added mechanism.

Concrete rewrite:
Ask author: What does the "exact-head" check actually compare between shards (a hash of the head row, a row count, a schema fingerprint)? What is an "editorial-row layout" (row order, column structure, ID-to-position mapping)? And are "shards" and "replicas" the same partitions here, or does each shard hold multiple replicas that this check reconciles before a separate shard merge?

Fallback (cuts the undefined coinages, keeps only the timing claim the source already supports): "The indexer checks each shard's head before merging, so shards stay consistent. Because that check runs before the merge completes, a mismatch blocks the merge instead of surfacing later when something reads the data."

Rewrite check: The fallback contains no rule-of-three, no "Not X. Y." negative parallelism, no em-dash antithesis, no avoid-by-default phrases, no prestige adjectives, and no decorative closure. It does not invent a comparison mechanism, tool, count, or name — "checks each shard's head" sits at the same specificity as the source's "exact-head checks," just without the jargon. It still doesn't say what the check compares; that gap is the ask-author question itself, not a fact safe to invent. Passes self-detectors.

Remembered line: "A mismatch blocks the merge instead of surfacing later when someone reads the data." That's the paragraph's one carrier-bound, concrete claim, and it's worth keeping once the author names what "exact-head" actually compares.
