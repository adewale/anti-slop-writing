Paragraph reviewed:

> The indexer runs exact-head checks before each merge, so editorial-row layouts stay consistent across shards. Because the check happens at the head, drift between replicas surfaces during the merge rather than at read time.

Verdict: ask-author

Slop tells:
- Coined compound labels ("exact-head checks," "editorial-row layouts"): both are hyphenated terms naming a check and an artifact that the paragraph doesn't fully define. Checked each for in-place support before flagging, per the false-positive-restraint rule (a name is not a mechanism):
  - "exact-head checks" is partially earned: sentence 2 says the check runs "at the head" and that this positioning is why drift surfaces at merge rather than read time — a real, resolvable design detail (a positional check, not a full scan), not just a label.
  - "editorial-row layouts" is not earned: neither sentence says what a "layout" consists of (row order, row membership, row content) or what would count as "inconsistent."
- Unbridged reference shift: sentence 1's unit of consistency is "shards"; sentence 2's unit of drift is "replicas." The paragraph never states whether a replica is one copy of a shard, so the reader can't verify that sentence 2's mechanism actually produces sentence 1's claim — it's implied by adjacency, not shown.
- No hits elsewhere: no banned phrases, no watch-list words, no copula displacement, no hedged symmetry, no em-dash cadence, no staccato antithesis, no generic conclusion. The paragraph already uses hypotaxis correctly ("so," "because"), which is the structure this skill prefers.

Specificity missing:
- What "head" refers to structurally (head of what — a per-replica row sequence, a version pointer, a commit log).
- What "editorial-row layout" concretely tracks (order, membership/identity, or content) and what would count as a mismatch.
- Whether "replica" means one copy of a given shard, which would make replica drift the specific failure mode the check protects shard-level consistency from.

Inflated claim: None. Both sentences make bounded, checkable engineering claims; the paragraph doesn't reach for significance language or an unsupported superlative. The gap here is specificity, not inflation.

Flow break: Sentence 2 reads as the mechanism behind sentence 1's claim, but it switches the unit of reference from "shards" to "replicas" without equating them. The causal chain the paragraph wants — check catches drift, so shards stay consistent — has a missing link: why replica-level drift detection implies shard-level layout consistency.

Concrete rewrite:
Ask author: (1) Is a "replica" one copy of a given shard, so "drift between replicas" is the specific failure the exact-head check keeps from reaching cross-shard inconsistency? (2) What does "editorial-row layout" track — row order, row membership, or row content?

Fallback if those facts aren't available (cut the unsupported clause and let the sentence that already has support stand on its own, rather than guessing at what the cut clause means):

"The indexer runs exact-head checks before each merge. Because the check happens at the head, drift between replicas surfaces during the merge rather than at read time."

This drops "so editorial-row layouts stay consistent across shards" instead of inventing what it means; the remaining two sentences are the source's own words and assert nothing beyond what it already stated.

Rewrite check: The fallback is a trimmed subset of the source paragraph's own sentences, with no added vocabulary — so no rule-of-three, no X-not-Y parallelism, no em-dash antithesis, no banned avoid-by-default phrases, no prestige adjectives, no decorative closer, and no invented facts (nothing is asserted that the source didn't already state). The ask-author question is phrased as a question, not a smuggled assertion. Passes self-detectors.

Remembered line: "Because the check happens at the head, drift between replicas surfaces during the merge rather than at read time." It is the one claim in the paragraph that names both a mechanism (check position) and a verifiable consequence (merge-time detection, not read-time), and it should anchor whatever the shard/replica clarification turns into.
