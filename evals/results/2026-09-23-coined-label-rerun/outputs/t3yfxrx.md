Paragraph reviewed:

"The indexer runs exact-head checks before each merge, so editorial-row layouts stay consistent across shards. Because the check happens at the head, drift between replicas surfaces during the merge rather than at read time."

Verdict: ask-author

Slop tells: None of the standard AI-writing tells apply. No prestige vocabulary, hedged symmetry, copula displacement, decorative em-dashes, rule-of-three, canned emphasis, or banned avoid-by-default phrases. Verbs are plain (runs, stay, happens, surfaces), and both sentences use hypotactic connectors ("so," "because") instead of side-by-side clauses, which is the doctrine's preferred structure, not a violation of it.

Specificity missing: Sentence 1 states a cross-shard property ("editorial-row layouts stay consistent across shards"). Sentence 2 shifts to "drift between replicas" without saying whether "replicas" are the same entities as "shards" under a looser name, or a distinct layer — copies of a single shard — that the same head check would need to reach separately. Applying the syntax-relation test: restating the sentence-1-to-sentence-2 link in plain prose ("because each shard's replicas must present the same head to pass the check...") requires assuming a shard-has-replicas structure the paragraph never states. The connective can't be supplied without inventing the mechanism, so the relation is asserted, not shown.

Inflated claim: None. "Stay consistent," "surfaces during the merge," and "rather than at read time" are specific, falsifiable claims, not significance-inflating language.

Flow break: The "Because" clause in sentence 2 reads as a further consequence of sentence 1's mechanism, but it introduces a new entity ("replicas") sentence 1 never names, so a reader can't tell whether sentence 2 restates sentence 1 in looser terms or extends it to a second, unstated failure mode. The same gap weakens "rather than at read time": read time is the implied default surfacing point, but the paragraph never says what a reader would actually hit there (stale rows, mismatched layout across shards), so that side of the comparison is asserted rather than shown.

Concrete rewrite: Ask author: are "shards" and "replicas" the same partitions under two names, or does each shard have multiple replicas, meaning the exact-head check has to compare every replica of every shard? The fix follows directly from the answer.
- If they're the same thing: replace "replicas" with "shards" so sentence 2 reuses sentence 1's term: "...so editorial-row layouts stay consistent across shards. Because the check happens at the head, drift across shards surfaces during the merge rather than at read time."
- If they're different: name the mechanism that lets one check cover both: "...so editorial-row layouts stay consistent across shards. The check compares the head record on every replica of each shard, so drift between a shard's replicas surfaces during the merge rather than at read time."
- Fallback if neither can be confirmed: cut "between replicas" and write "drift across shards," reusing sentence 1's term instead of introducing a second, unreconciled one.

Rewrite check: The two conditional rewrites and the fallback contain no rule-of-three, X-not-Y negative parallelism, em-dash antithesis, banned avoid-by-default phrases, prestige adjectives, or decorative closure. Neither invents a name, count, tool, or timing: each either reuses "shards" from the source or states the covering mechanism as conditional on the author's answer, not as an asserted new fact. Passes self-detectors.

Remembered line: "drift between replicas surfaces during the merge rather than at read time" is the paragraph's real payoff — failing at merge time instead of silently at read time — and it still lands with the cadence flattened out ("the merge, not a later read, is where drift becomes visible"), so the idea is carrying it, not the rhythm. Keep this line once "replicas" is reconciled with "shards."
