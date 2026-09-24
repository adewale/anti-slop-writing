Verdict: ask-author

Slop tells:
- Coined compound label — "exact-head checks": a hyphenated term naming a check the paragraph never fully defines. Sentence 2 supplies *where* it runs ("at the head") but not *what* it compares (a content hash? row count? schema fingerprint?). Support must resolve a term, not just gesture at it — this only partially resolves, so the flag stands.
- Coined compound label — "editorial-row layouts": names the artifact under test but is never defined. Not a standard cross-domain term (unlike "dead-letter queue" or "two-phase commit"); "row" of what, and whether "layout" means column order, schema, or formatting, is unstated.
- Staccato contrast checked: "during the merge rather than at read time." Side A (merge-time) is evidenced by sentence 1's pre-merge head check; side B (read-time) is the natural counterfactual, not a fresh unsupported claim. Classify earned — keep as is.
- Everything else is clean: no banned avoid-by-default phrase, no copula displacement, no hedged symmetry, no rule-of-three, no em-dash cluster, no outline-shaped conclusion. Both sentences already use hypotaxis correctly ("checks..., so...", "Because..., drift...") — the syntax isn't the failure mode; the undefined referents are.

Specificity missing:
- What "exact" means for the head check — equality of which value.
- What an "editorial row" is and what "layout" means for it.
- What the indexer does when the check finds a mismatch. The paragraph says the check "runs" but never names an enforcement action (block the merge, retry, alert).
- The relation between "shards" (sentence 1) and "replicas" (sentence 2) is assumed, not stated.

Inflated claim:
- "runs exact-head checks before each merge, so editorial-row layouts stay consistent across shards" treats consistency as a guaranteed side effect of running a check. A check only detects a mismatch; staying consistent requires an enforcement step after detection that the paragraph never names. The "so" claims more than the stated mechanism earns.

Flow break:
- None structurally — sentence 2's "Because" correctly names its relation to sentence 1 (cause). The only gap is referential (shard vs. replica), not sequential.

Concrete rewrite:
Ask author: (1) What does the exact-head check compare — a content hash, a row count, a schema fingerprint of the head? (2) What is an "editorial row," and which layout property must match (column order, schema version, formatting)? (3) When the check finds a mismatch, what happens — does the indexer abort the merge, retry the shard, or alert and continue? (4) Are "shards" and "replicas" the same units here (a shard's head compared across its own replicas), or two different things?

Fallback, if those facts aren't available (drops the unsupported consistency claim, keeps only what the paragraph already establishes, invents nothing new):

"The indexer checks each replica's head for an exact match before merging. Because that comparison happens at the head, drift between replicas surfaces during the merge rather than later, at read time."

Rewrite check: No rule-of-three, no X-not-Y / negative parallelism, no em-dash antithesis, no banned avoid-by-default phrases, no prestige adjectives, no decorative closure. "each replica's head" restates what sentence 2 already implies (the check compares replica heads) rather than adding a new fact — it synthesizes the two source sentences rather than inventing beyond them. Passes self-detectors.

Remembered line:
"Because the check happens at the head, drift between replicas surfaces during the merge rather than at read time." This is the paragraph's one fully-earned, concrete claim — it names a timing mechanism (merge-time detection instead of read-time discovery) without inflating it. The first sentence needs the ask-author facts above before it can carry equal weight.
