Verdict: ask-author

Slop tells:
No banned avoid-by-default phrases, no rule-of-three, no em-dash clusters, no hedged symmetry ("Whether X or Y"), no copula displacement ("serves as" / "represents" / etc.), and no outline-shaped conclusion. Sentence 2 correctly uses hypotaxis ("Because the check happens at the head, ...") instead of an unrelated parataxis. The one real tell is two coined compound labels — "exact-head checks" and "editorial-row layouts" — hyphenated noun phrases that name a check and an artifact the paragraph never defines. The hyphen supplies the texture of precision; the referent isn't recoverable from the text.

Specificity missing:
- "exact-head checks": sentence 2 supplies where the check runs (at the head) and what its timing buys (drift "surfaces during the merge rather than at read time"), but never says what is compared. "Exact" implies an equality test, and the paragraph never names the operand — content hash? revision ID? row count? schema version?
- "editorial-row layouts": has no supporting context anywhere in the paragraph. Nothing says what makes a row "editorial" (a content type, a table, a class of user-facing rows) or which layout property the check is protecting (column order, formatting, schema).
- Secondary: sentence 1 frames the guarantee as consistency "across shards"; sentence 2 frames the failure mode as drift "between replicas." If a shard here is a partition served by multiple replicas, both sentences describe one mechanism at two levels (replica agreement inside a shard produces the cross-shard guarantee) — but the paragraph never states that a shard has multiple replicas, so a reader can't confirm the two nouns name the same axis rather than a loose substitution.

Inflated claim:
"stay consistent" in sentence 1 reads as unconditional — no drift, ever — but sentence 2 admits replicas do drift; the check only catches it "during the merge rather than at read time." The supportable claim is narrower: what a reader sees at read time stays consistent, not that replicas never diverge. Sentence 1 currently promises more than sentence 2 delivers.

Flow break:
None mechanically — "Because the check happens at the head" names the causal relation to sentence 1 explicitly, and "during the merge rather than at read time" is a real, checkable consequence, not a rhythm-only closer. The one unresolved link is the shard/replica switch noted above.

Concrete rewrite:
Ask author: (1) What does the exact-head check actually compare between shard heads — a content hash, a revision ID, or a schema/version marker? (2) What is an "editorial-row," and which layout property does the check protect — column order, formatting, or schema? (3) Is a replica a copy of a single shard, so that replica agreement is what produces the cross-shard guarantee in sentence 1?
Fallback if the author can't be reached: keep the paragraph only if it already sits inside a doc that defines "head," "editorial-row," and the shard/replica relationship elsewhere. Otherwise, rescope sentence 1 to what sentence 2 actually supports — "so merged editorial-row layouts stay consistent across shards" — and leave "exact-head check" and "editorial-row" as terms this paragraph uses rather than defines.

Rewrite check:
The three ask-author questions form a disambiguation list for the author to answer, not a rhetorical rule-of-three (the skill's own ask-author example — "which coding tool? Cursor, Claude Code, Copilot, Aider, other?" — takes the same form). No X-not-Y / negative parallelism, no em-dash antithesis (no em-dashes used), no banned avoid-by-default phrases, no prestige adjectives, no decorative closure. The fallback rewrite adds no invented name, count, tool, or mechanism — it only narrows "stay consistent" to the scope sentence 2 already states. Passes self-detectors.

Remembered line:
"Drift between replicas surfaces during the merge rather than at read time." Keep this sentence as written. It is the one line that names a checkable tradeoff — catch drift early at merge instead of late at read — rather than asserting quality, and it is what should stay memorable once "exact-head check" and "editorial-row" get defined.
