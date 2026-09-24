Paragraph reviewed:

"The indexer runs exact-head checks before each merge, so editorial-row layouts stay consistent across shards. Because the check happens at the head, drift between replicas surfaces during the merge rather than at read time."

Verdict: keep

Slop tells: None found. Every verb is plain and concrete (runs, stay, happens, surfaces) — no copula displacement ("serves as," "stands as," "represents"). No avoid-by-default phrase, no rule-of-three, no hedged symmetry ("Whether X or Y"), no em-dash, no "Not X. Y." negative parallelism. The one candidate worth testing is "surfaces during the merge rather than at read time," which has the shape of a contrast. Run through the staccato contrast test, it classifies as earned, not compressed or decorative: the prior sentence supplies the mechanism the contrast depends on ("before each merge" / "at the head" establishes that the check sits upstream of any read), and reading that prior sentence first is exactly the doctrine's instruction for judging this kind of contrast. The cadence isn't carrying a claim the prose hasn't earned.

Specificity missing: None that weakens the claim. Actor (the indexer), mechanism (exact-head checks), pipeline location (at the head), timing (before each merge), and both effects (consistent editorial-row layouts across shards; drift caught at merge instead of at read) are all named — this is "more detail, earned importance," not "less detail, more importance." One open question worth asking the author, though it doesn't change the verdict: what "surfaces" means operationally once drift is caught — does the merge block, alert, or retry? The two sentences as given don't need that answer to be correct or well-formed.

Inflated claim: None. No significance language ("crucial," "critical," "seamless," "robust," "pivotal") and no claim of importance asserted without evidence — every clause states what the system mechanically does.

Flow break: None. The second sentence answers the question the first raises — why does checking "at the head" matter? — with an explicit "Because X, Y" connective. That's hypotaxis naming the relation (dependency/cause) instead of leaving two clauses to sit side by side and make the reader guess.

Concrete rewrite: Not applicable — no slop tell was flagged, so there is nothing to rewrite. Forcing one would expand an already-tight paragraph into bland restatement, which the skill's self-check explicitly warns against.

Rewrite check: N/A — no rewrite was produced, since the verdict is keep and nothing was flagged as revise or ask-author.

Remembered line: "drift between replicas surfaces during the merge rather than at read time" — the concrete payoff of an exact-head check: it moves the moment inconsistency is caught from a read query to the merge step itself.
