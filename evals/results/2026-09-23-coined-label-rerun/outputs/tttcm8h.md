Verdict: ask-author

Slop tells: Coined compound labels — "exact-head checks" and "editorial-row layouts" are hyphenated terms that name a check and a row category the paragraph never defines, and neither is an established domain term the way "dead-letter queue" or "two-phase commit" is; the hyphen supplies a texture of precision the sentence doesn't back up. Nothing else here reads as slop: no avoid-by-default phrases or watch-list words, no copula displacement, no rule-of-three, no hedged symmetry, no decorative em-dash, and sentence 2 already uses the subordination the doctrine asks for ("Because the check happens at the head, drift... surfaces...").

Specificity missing:
1. What "head" refers to structurally — a shard's most recently committed row, a version/commit pointer, something else.
2. What the "exact" comparison evaluates — row count, checksum, row content, ordering.
3. What marks a row as "editorial" rather than any other row this indexer handles.
4. What happens once the check finds a mismatch — block the merge, trigger reconciliation, or just make the drift visible in a log someone has to act on afterward.

Inflated claim: Sentence 1 states a guarantee — layouts "stay consistent across shards" — but the only mechanism sentence 2 actually describes is detection: drift "surfaces during the merge." Surfacing a problem is not the same as preventing one. Flattened, cadence removed, claim preserved: "Editorial-row layouts are consistent across shards because the indexer checks something about the head before merging." That residual still names an actor (the indexer) and a rough timing mechanism, but not one strong enough to license "stay consistent" as a guarantee rather than "a mismatch gets caught before the merge finishes."

Flow break: None. Sentence 2 opens with an explicit connective ("Because the check happens at the head,") that names the dependency relation to sentence 1 instead of leaving the reader to infer it — the strongest move in the paragraph.

Concrete rewrite: "Exact-head check" can be de-jargoned without asking anyone anything, since unpacking it adds no new fact: "The indexer checks that each shard's head matches before it merges." "Editorial-row" can't be resolved the same way — dropping the qualifier would silently widen the claim from a specific row category to all rows, and keeping it unexplained leaves the claim unverifiable either way.
Ask author: Does "editorial-row" mark a row category with different consistency behavior than other rows this indexer handles, and if so, what's the difference — or is "editorial" incidental phrasing and droppable without changing the claim? Also: when the head check finds a mismatch, does it block the merge, reconcile automatically, or only log the drift for someone to fix later?
Fallback if unanswered: cut the row-category qualifier and the unproven guarantee, keeping only what the paragraph already evidences — "The indexer checks each shard's head before merging. Because the check runs there, drift between replicas surfaces during the merge rather than at read time."

Rewrite check: Neither the "exact-head" paraphrase nor the ask-author fallback contains rule-of-three, X-not-Y construction, em-dash antithesis, avoid-by-default phrases, prestige adjectives, or decorative closure. The paraphrase invents nothing — it reorders the source's own words. The fallback invents nothing either — it states only what sentence 2 already evidences. Passes self-detectors.

Remembered line: "Drift between replicas surfaces during the merge rather than at read time" is the one claim here already concrete enough to keep as written; the layout-consistency guarantee in sentence 1 needs the author's mechanism before it earns the same trust.
