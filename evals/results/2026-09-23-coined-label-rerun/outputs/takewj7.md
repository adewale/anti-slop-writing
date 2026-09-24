Verdict: ask-author

Slop tells: The paragraph's whole claim rests on two coined compound labels that are never defined and aren't standard domain terms: "exact-head checks" (names a check) and "editorial-row layouts" (names an artifact). Per the coined-compound-label detector, a hyphenated name is not a mechanism — a reader can't resolve either term from the passage, and neither is standard the way "dead-letter queue" or "two-phase commit" would be.

Specificity missing:
- "Head" is never anchored to a structure (replication-log position, version pointer, per-shard commit reference), so "exact-head check" names an action — compare heads — without saying what's being compared or what "exact" means as a match criterion (hash equality, row count, schema equality).
- "Editorial-row layout" never says what "layout" covers (storage order, column/schema shape, sort order) or what makes a row "editorial" rather than any other row, so "stay consistent" doesn't say which dimension of consistency the check actually protects.
- Sentence 2 reuses "head" ("the check happens at the head") but relocates the term instead of resolving it; support has to name something the reader can look up or that the passage defines, and repetition alone doesn't clear that bar.

Inflated claim: None. No watch-list words, banned phrases, or unsupported significance language. The one causal claim — drift surfaces at merge rather than at read time — is earned: it follows from sentence 1's timing detail (the check runs before the merge) instead of being asserted on rhythm alone.

Flow break: None. The paragraph states the relation instead of leaving it implied ("so," "Because … ,"), which is the hypotaxis the doctrine asks for. A rewrite should keep that shape, not flatten it back into two side-by-side clauses.

Concrete rewrite:
Ask author: what does "head" refer to here — a replication-log position, a version pointer, a per-shard commit reference, something else — and what does "exact" check for (full hash equality, row count, schema equality)? Separately, what does "editorial-row layout" mean structurally (storage order, column/schema shape, sort order), and what distinguishes an "editorial" row from any other row?
Fallback if unavailable: cut both modifiers down to what the paragraph already supports, and keep the earned timing claim: "The indexer checks each shard's head against its replicas before merging. Because that check runs before the merge, drift between replicas surfaces there rather than later, at read time." This drops "exact" and "editorial-row" rather than guessing at them, and it also drops the paragraph's stated purpose (consistent row layout) — restore that clause once "layout" has a definition.

Rewrite check: No rule-of-three, no "Not X. Y." / negative parallelism, no em-dash antithesis, no avoid-by-default phrases, no prestige adjectives, no decorative closure. The fallback asserts only what sentence 2 already established (replicas, merge-vs-read timing) and does not invent a name, count, or mechanism for "head" or "layout" — it removes the undefined claims rather than resolving them with invented specifics. Passes self-detectors.

Remembered line: "Drift between replicas surfaces during the merge, rather than at read time" — the one claim in the paragraph fully earned by its own timing detail. Keep it as the anchor once "head" and "row layout" are defined.
