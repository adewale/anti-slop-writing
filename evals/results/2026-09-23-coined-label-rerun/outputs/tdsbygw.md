# Critique

Paragraph reviewed:
> The indexer runs exact-head checks before each merge, so editorial-row layouts stay consistent across shards. Because the check happens at the head, drift between replicas surfaces during the merge rather than at read time.

Verdict: ask-author

Slop tells:
- Coined compound label, unresolved: "editorial-row layouts." Neither sentence says what an editorial-row is (a curated ordering, a schema element, a rendering unit) or what "layout" covers (column order, row order, a template). The hyphen supplies the texture of precision; the referent stays out of reach.
- Coined compound label, verdict keep: "exact-head checks." This one earns itself. The second sentence supplies the mechanism ("the check happens at the head") and a consequence (drift is caught at merge, not at read), so "exact-head" reads as "the head value matches exactly across replicas before merge is allowed." No rewrite needed.

Specificity missing:
- What "exact-head" compares is still implicit: a content hash, a version or sequence number, or some other field of the head record. The paragraph supports that a comparison happens at the head; it doesn't say of what.
- "Shards" (sentence 1) and "replicas" (sentence 2) are used as if interchangeable. In most sharded systems a shard is a partition and a replica is a copy of a partition, so "drift between replicas" is probably drift between copies of the same shard, but the paragraph never states that relationship, so a reader outside the system has to guess it.
- "Editorial-row," as above: the one undefined term the paragraph's main claim depends on.

Inflated claim:
- One mild leap, not marketing inflation: sentence 1 moves from "checks the head" to "layouts stay consistent" as though the two are the same guarantee. That only holds if the head value fully determines layout state. If the layout can drift for a reason the head doesn't capture, the check is necessary but not sufficient for the claim as written, and nothing here rules that out.

Flow break:
- The noun shifts from "shards" to "replicas" across the sentence boundary without a bridge; sentence 2 opens a new frame ("drift between replicas") instead of continuing the one sentence 1 set up ("across shards"). One connecting clause, such as "each shard's replicas," would remove the guesswork.
- The "during the merge rather than at read time" contrast is not decorative: sentence 1 establishes merges, and the "because" clause gives the reason drift shows up at merge instead of at read. Checked against the staccato-contrast test, this reads as earned, not compressed: the causal clause supplies the mechanism before the contrast lands, which is what the test asks for.

Concrete rewrite:
Ask author: does the exact-head check compare a content hash, a sequence number, or a specific field of the head record? What is an "editorial-row": a term already defined elsewhere in this document, or one this paragraph should gloss inline? And are shards and replicas two different layers here, or is "replica" shorthand for a copy of a shard?

Fallback, if those facts aren't available before this ships: cut "editorial-row" and stop the claim at what the paragraph already supports. For example: "The indexer runs an exact-head check before each merge, so shard replicas agree before the merge completes. Because the check happens at the head, drift surfaces during the merge rather than at read time." This keeps the earned mechanism in sentence 2 unchanged and drops the unverifiable "layout" claim instead of guessing what it names.

Rewrite check: the fallback contains no rule-of-three, no "Not X. Y." or negative parallelism, no em-dash antithesis, no avoid-by-default phrases, no prestige adjectives, no decorative closer, and no invented facts. It reuses wording already in the source and removes the undefined term rather than replacing it with a guess. Passes self-detectors.

Remembered line: "Drift between replicas surfaces during the merge rather than at read time" is already the paragraph's strongest, most concrete sentence. It names a specific design tradeoff, catching drift early at merge instead of late at read, rather than reaching for a generic closer. Anchor the paragraph on that line once "editorial-row" is either defined or cut.
