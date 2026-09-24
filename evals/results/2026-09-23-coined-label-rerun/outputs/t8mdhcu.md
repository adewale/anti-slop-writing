Verdict: ask-author

Slop tells:
- Coined compound labels: "exact-head checks" and "editorial-row layouts" name a check and a data shape the passage never fully defines. "head" (the latest state per shard) and "row" (an indexed record) are standard, earned vocabulary; the modifiers "exact" and "editorial" are not — nothing in the paragraph says what makes the comparison "exact" (full content? a hash? row count or order?) or what makes a row "editorial" rather than any other kind.
- Compressed antithesis: "surfaces during the merge rather than at read time" sets up a contrast where only the merge side is built by the prior sentence (the check already runs "before each merge"); the read-time side is asserted, not shown — nothing earlier in the paragraph describes a read path.
- No hits for: banned avoid-by-default phrases, prestige/inflation vocabulary (crucial, robust, seamless, etc.), rule-of-three, em-dash cadence, copula displacement, hedged symmetry. "Because the check happens at the head, drift ... surfaces during the merge rather than at read time" is hypotaxis doing real work, not a slop tell.

Specificity missing:
- What "exact" comparison the check performs (full row content, a hash/checksum, row count, or ordering).
- What distinguishes an "editorial" row from any other row in the index.
- What "drift" looks like concretely when it does surface (a missing row, a reordered row, a mismatched field).

Inflated claim:
- None. The paragraph makes one scoped, falsifiable claim about timing (check-at-head means detection-at-merge) and attaches no evaluative or significance language to it.

Flow break:
- Minor. The "because" clause earns the merge half of its contrast (sentence 1 already established the check runs before merge) but not the read-time half — nothing before it mentions a read path, so that side of the contrast is implied by the stated goal ("stay consistent") rather than demonstrated.

Concrete rewrite:
Ask author: What does the "exact-head" check actually compare between replicas — full row content, a hash, row count, or ordering — and what makes a row "editorial" as opposed to any other row in the index?
Fallback, if that detail isn't available: cut the two undefined modifiers instead of keeping unearned precision —
"The indexer checks that each shard matches at the head before merging it in, so row layouts stay consistent across shards. Because the check happens at the head, drift between replicas surfaces during the merge rather than at read time."
This keeps everything the source already supports (a check at the head, before merge, catching drift between replicas) and drops only "exact" and "editorial," which the paragraph never earns.

Rewrite check:
No rule-of-three, no X-not-Y/negative parallelism, no em-dash antithesis, no banned avoid-by-default phrases, no prestige adjectives, no decorative closure. "Matches" is not an invented fact: sentence 2 already says the check catches "drift between replicas," so a check that catches drift is a check for a match. Passes self-detectors.

Remembered line:
"Drift between replicas surfaces during the merge rather than at read time." Already the sharpest, most concrete line in the paragraph — it names the actor (drift between replicas), the mechanism's timing (at the head, before merge), and the alternative it avoids (read time). Worth keeping verbatim once "exact-head" and "editorial-row" are resolved.
