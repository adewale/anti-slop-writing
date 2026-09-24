Verdict: ask-author

Slop tells: Coined compound labels. "Exact-head checks" and "editorial-row layouts" are hyphenated terms that read as precise but are never cashed out. Sentence 2 looks like it defines "exact-head" ("the check happens at the head") but only repeats the word "head" — that adds a location word, not a mechanism. Nothing else in the paragraph trips a detector: no banned phrases, no prestige adjectives, no inflated significance language. The "merge / read time" distinction is a standard architectural contrast (build phase vs. serve phase), not decorative antithesis, so it doesn't need separate evidencing inside these two sentences.

Specificity missing:
- What "head" points to structurally: the shard's latest committed row, a leader/primary replica's pointer, the first row in scan order, or something else.
- What "exact" is checked against: a row hash, a byte-for-byte diff, a row count, or column/schema order.
- What "editorial-row layout" denotes: schema/column order for a content row, or something else — "editorial" is carrying unexplained weight.

Inflated claim: None. Both sentences make plain, falsifiable timing claims (checks run before merge; drift is caught at merge instead of later) with no significance language inflating them.

Flow break: None. Sentence 2's "Because ... " names the causal relation back to sentence 1 explicitly — checking at the head is why drift is caught at merge instead of later. That's hypotaxis doing real work, not two clauses left to sit beside each other.

Concrete rewrite: Ask author: what does "head" point to (latest committed row, leader replica's pointer, first row in scan order), and what does the "exact" check compare (row hash, byte-for-byte diff, row count)? Also confirm what "editorial-row layout" means (schema/column order, or something else). Fallback if that isn't available before publishing — cut the second sentence's restatement of "head," since it repeats sentence 1 without adding a fact, rather than guessing at the mechanism:

"The indexer runs exact-head checks before each merge, so editorial-row layouts stay consistent across shards. The check runs before the merge completes, catching drift between replicas at that point."

This fallback removes the empty repetition without inventing what "head," "exact," or "editorial-row" mean.

Rewrite check: The concrete rewrite is a clarifying question plus a cut-only fallback; it introduces no invented mechanism, count, tool, or timing. It contains no rule-of-three, no X-not-Y / negative parallelism, no em-dash antithesis, no banned avoid-by-default phrases, no prestige adjectives, and no decorative closer. Passes self-detectors.

Remembered line: The timing claim is worth keeping: the check runs before the merge, so drift is caught before anything downstream reads the data. "Exact-head" and "editorial-row" are the two hyphens standing in for a mechanism the paragraph never names.
