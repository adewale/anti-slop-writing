Source paragraph reviewed:

"The indexer runs exact-head checks before each merge, so editorial-row layouts stay consistent across shards. Because the check happens at the head, drift between replicas surfaces during the merge rather than at read time."

Verdict: ask-author

Slop tells: Coined compound labels. "exact-head checks" and "editorial-row layouts" are hyphenated technical noun phrases that name a check and an artifact the paragraph never defines, and neither is an established domain term the way "dead-letter queue" or "two-phase commit" is. The hyphens supply the texture of precision, but the reader cannot resolve what the check actually compares or what a "layout" consists of. This pairs with a secondary, related tell: the paragraph is noun-dense (checks, layouts, drift, merge, shards, replicas, read time) without exposing the mechanism behind any of those nouns, so the density reads as informational rather than explanatory.

Specificity missing: (1) What does an exact-head check compare: a hash or checksum of each shard's most recently committed row, a monotonic sequence number, something else? What object's "head" is being checked (a shard's write log, a replica's index segment, the merge input itself)? (2) What is an editorial-row layout: a column schema, a row ordering, a rendering format? Why would it diverge across shards if the check didn't run?

Inflated claim: None. The claims are causal and mechanical (check runs, so layouts stay consistent; check runs at the head, so drift surfaces at merge instead of read), not significance claims. No prestige vocabulary or unearned importance language is present.

Flow break: None. Sentence 2 extends sentence 1 with an explicit hypotactic "because" clause and names a real relation: a timing tradeoff where drift is caught at merge rather than surfaced later at read time. That is exactly the kind of named relation the flow-by-relation test asks for, not a list-like juxtaposition. Keep this structure.

Concrete rewrite: Ask author: what does the exact-head check compare, and what object's head does it check? Separately, what is an editorial-row layout, and why would it drift across shards if the check didn't run? Fallback: cut "exact-head" and "editorial-row" as unglossed coinages and let the rest of the sentence carry the claim, or keep them only if this paragraph sits inside a document that already defines this system's internal terms elsewhere (a glossary, an earlier section).

Rewrite check: The concrete rewrite above contains no rule-of-three, no X-not-Y / negative parallelism, no em-dash antithesis, no banned avoid-by-default phrases, no prestige adjectives, and no decorative closure. It contains no invented facts: it asks questions and offers a cut / keep-if-defined-elsewhere fallback rather than supplying a name, count, tool, or mechanism the source didn't give. Passes self-detectors.

Remembered line: The tradeoff already in the source is worth keeping through any rewrite: drift between replicas is caught at merge, not discovered later at read time. Once the author names what the check actually compares and what a layout is, that timing tradeoff is the line the paragraph should end on.
