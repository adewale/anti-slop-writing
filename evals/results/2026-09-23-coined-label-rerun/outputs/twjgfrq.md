Paragraph under review:

"The indexer runs exact-head checks before each merge, so editorial-row layouts stay consistent across shards. Because the check happens at the head, drift between replicas surfaces during the merge rather than at read time."

Verdict: ask-author

Slop tells: Two coined compound labels carry the paragraph's real content without ever cashing it out. "Exact-head checks" names a specific verification step but never says what "exact" compares or what "head" points to (a version pointer, the latest merged row, a log position). "Editorial-row layouts" names the thing being protected but never says which property of the layout matters (row order, column order, formatting metadata). Neither term is standard cross-domain vocabulary the way "dead-letter queue" or "two-phase commit" is, and sentence 2's "the check happens at the head" repeats the word "head" without resolving it — that's support that relocates the gap instead of closing it. Apart from that, the paragraph is not doing the usual AI-slop moves: it uses "so" and "Because" to name the relation between its two clauses (hypotaxis, not staccato parataxis), and it has no banned phrases, no copula displacement, no em-dash cadence, and no rule-of-three padding.

Specificity missing: What "exact" verifies (a hash match, a full diff, a row count, a checksum) and what "head" is the head of (a replica's log, a version chain, the table itself). Which part of an "editorial-row layout" must match across shards (ordering, formatting, visibility). Whether "shards" (sentence 1's unit) and "replicas" (sentence 2's unit) are the same grouping, or replicas-within-a-shard — the paragraph switches nouns between the two sentences without bridging them.

Inflated claim: No importance-language inflation ("crucial," "a testament to," etc.) — the inflation here is precision, not significance. "Exact-head check" reads as a specific, well-understood mechanism because of the modifier "exact" and the technical-sounding "head," but the sentence never shows the comparison it names. The hyphen supplies the texture of precision while the referent stays out of reach.

Flow break: None at the macro level — "so" and "Because" correctly name a cause relation between the two sentences, which is what the flow-by-relation test wants. The break is narrower: sentence 2 swaps "shards" for "replicas" without saying whether that's the same unit, so the reader can't confirm that "drift between replicas" is the same failure the first sentence's consistency check is guarding against.

Concrete rewrite:
Ask author: (1) What does the exact-head check compare — a hash of the head row/version, a full row-by-row diff, or a checksum of row order? What is "head" the head of? (2) Which property of an editorial-row layout must survive the merge — row order, column order, or formatting/visibility metadata? (3) Are "shards" and "replicas" the same grouping here, or does each shard hold multiple replicas being compared at merge time?
Fallback: until those are answered, keep this paragraph as an internal engineering note rather than external-facing docs, since a reader outside the team can't verify either claim. If a fact can't be recovered, cut "exact-head" and "editorial-row" down to whatever is actually known (name the field or structure being compared) rather than let the coined labels stand in for it.

Rewrite check: The ask-author block above contains no rule-of-three, no X-not-Y / negative parallelism, no em-dash antithesis, no banned avoid-by-default phrases, no prestige adjectives, no decorative closure, and no invented facts — it asks for the missing mechanism rather than supplying one. Passes self-detectors.

Remembered line: "Surfaces during the merge rather than at read time" is the line worth keeping — a real engineering tradeoff (catching drift before a reader hits it), stated through hypotaxis rather than cadence. It only pays off once "exact-head check" names an actual comparison; right now the line is earning trust it hasn't shown its work for.
