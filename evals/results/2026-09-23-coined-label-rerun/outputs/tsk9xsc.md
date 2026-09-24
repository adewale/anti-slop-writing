Verdict: ask-author

Slop tells: Two coined compound labels carry the paragraph's key claims without being defined anywhere in it: "exact-head checks" and "editorial-row layouts." Neither is standard shorthand the way "dead-letter queue" or "two-phase commit" is, and neither sentence states what "exact" is matching or what a "row" is in this system. Sentence 1 also claims a maintained state ("stay consistent") on the strength of the connective "so" rather than on a stated mechanism — the "so" borrows more certainty than sentence 2 actually delivers.

Specificity missing:
- What does the "exact-head" check compare between replicas: a checksum, a row count, a version/commit id, a timestamp?
- What is an "editorial-row," and which of its properties must match across shards — order, content, schema, count?
- When drift is found at merge, what happens next: is the merge rejected, the lagging replica excluded, a resync triggered, an alert raised? Sentence 1's "stay consistent" claim depends on this step, and the paragraph never states it.

Inflated claim: "so editorial-row layouts stay consistent across shards" asserts an achieved, ongoing state. The only mechanism given for it, in sentence 2, is detection: drift "surfaces during the merge." Surfacing a discrepancy is not the same as correcting one. Applying the syntax-relation test to sentence 1's "so" — restate the relation in plain prose without inventing anything — it only holds if you add an unstated step (something acts on the drift once it's found), and that step is not in the paragraph. The claim is getting credit for an enforcement action the text never describes.

Flow break: Sentence 2 answers "when and where does the check run" (at the head, before merge) but not "how does running there make layouts stay consistent," which is the question sentence 1 actually raises. The paragraph states a cause (checks run at the head) and a consequence (drift surfaces at merge, not read time) but is missing the resolution step between them that would connect detection to the claimed outcome.

Concrete rewrite: Ask author: (1) What does the exact-head check compare — checksum, row count, or version id? (2) What is an "editorial-row," and what specifically must stay in sync across shards? (3) When the check finds drift at merge, what happens to the merge — blocked, retried, or does the divergent replica get excluded?

Fallback, using only what the paragraph already supports (drops "exact," "editorial-row," and the unproven "stay consistent"; keeps the one earned claim, timing):
"The indexer compares each replica's head before merging, so drift between replicas is caught at merge time rather than at read time."

Rewrite check: The ask-author questions name missing facts, not rhetoric, so there is no cadence to audit there. The fallback sentence has no rule-of-three, no X-not-Y/negative parallelism, no em-dash antithesis, no avoid-by-default phrase, no prestige adjective, no decorative closing line, and no invented fact — it narrows the claim to the one thing sentence 2 actually establishes (merge-time detection) instead of guessing at what "exact" or "editorial-row" mean. Passes self-detectors.

Remembered line: The one claim this paragraph earns is that drift shows up at merge time, not read time. The rest — what "exact" checks, what a "row" is, what happens after drift is found — still needs the author's answer.
