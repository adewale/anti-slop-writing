Verdict: ask-author

Slop tells:
- Coined compound labels: "exact-head checks" and "editorial-row layouts" are hyphenated compounds naming a check and an artifact that the paragraph never defines. "Because the check happens at the head" only repeats the word "head" from the name; it doesn't say what is compared (a hash, row order, row count, a specific field), and nothing marks what makes a row "editorial" as opposed to any other row the indexer holds. Neither reads as settled industry terminology the way "dead-letter queue" or "two-phase commit" would, so the coinage isn't earned in-passage.
- Compressed antithesis: "surfaces during the merge rather than at read time" sets up a two-sided comparison where only one side is evidenced. The prior clause establishes that the check runs at merge time; nothing earlier mentions a read path or what an uncaught drift would look like to a reader. One evidenced side plus one asserted side is compressed, not earned.

Specificity missing:
- What the "exact-head" check compares.
- What makes a row "editorial" rather than any other row type the indexer tracks.
- Whether "editorial-row layouts stay consistent across shards" (sentence 1) and "drift between replicas" (sentence 2) name the same consistency property, or whether sentence 1 states an aggregate result and sentence 2 states the finer-grained mechanism that produces it. "Because" links them as if one explains the other, but shard-level and replica-level consistency are ordinarily distinct properties in a sharded, replicated system, and the paragraph doesn't say how they relate here.

Inflated claim:
No significance-language inflation is present (no "crucial," "robust," "seamless," and the like); the paragraph is otherwise plain. The one soft overreach is structural: "rather than at read time" states the merge-versus-read comparison as settled, but the paragraph never shows what drift surfacing at read time would look like or cost, so the comparison is asserted rather than demonstrated.

Flow break:
Between the sentences: none. "Because" correctly subordinates the second sentence to the first, which is the hypotaxis this doctrine prefers over unrelated juxtaposition. Inside the second sentence: the shift from "shards" to "replicas" is an unsignposted scope or level-of-detail change. The flow-by-relation test asks a paragraph to name that kind of shift rather than let "because" carry a relation it hasn't stated.

Concrete rewrite:
Ask author: what does the exact-head check compare? Row hash, row order, row count, something else?
Ask author: what marks a row as "editorial" rather than any other row the indexer tracks?
Ask author: is "consistent across shards" the same property as "drift between replicas," or is the first the system-level result and the second the per-shard mechanism that produces it?
Fallback (cut the two unearned coinages; leave the shard/replica relationship exactly as the source states it rather than guessing at it):
"The indexer runs head checks before each merge, so row layouts stay consistent across shards. Because the check happens at the head, drift between replicas surfaces during the merge rather than at read time."

Rewrite check:
No rule-of-three, no X-not-Y / negative parallelism, no em-dash antithesis, no banned avoid-by-default phrases, no prestige adjectives, no decorative closure. The fallback drops "exact" and "editorial" instead of substituting a new invented specific (no hash, count, or field is asserted as fact), and it leaves the shard/replica relationship and the merge-versus-read comparison exactly as the source posed them rather than resolving them by invention. Passes self-detectors.

Remembered line:
Because the check runs at merge time, drift shows up there instead of later, when a read would expose it.
