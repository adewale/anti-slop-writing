# Critique

Reviewing:
> The indexer runs exact-head checks before each merge, so editorial-row layouts stay consistent across shards. Because the check happens at the head, drift between replicas surfaces during the merge rather than at read time.

Verdict: ask-author

Slop tells: None of the standard AI-writing or rhetorical-drift patterns apply. No banned phrases, no watch-list prestige words, no copula displacement ("serves as," "stands as," etc.), no hedged symmetry, no rule-of-three, no decorative em-dash clusters, no "Not X. Y." parataxis. Sentence 2 already runs on a "Because..." subordinate clause, which is the hypotaxis the doctrine prefers over side-by-side clauses, so there is no cadence here to flatten or thin.

Specificity missing: "exact-head check," "editorial-row layouts," and "the head" are named, specific mechanisms, not vague filler; they don't need re-explaining to count as concrete (the doctrine's own approved example, "fail on step 4," is just as unglossed and still counts as good). The real gap is relational, not lexical: the paragraph never says how a "replica" relates to a "shard." Sentence 1's guarantee is scoped to shards; sentence 2's failure mode is scoped to replicas, and the paragraph is equally consistent with three different readings: a replica is one shard's own copy, shards and replicas are independent partitioning axes, or "shard" and "replica" are two names for the same unit.

Inflated claim: None. Both claims ("stay consistent across shards," "surfaces during the merge rather than at read time") are scoped to the named head-check mechanism, not stretched into a broader guarantee than that mechanism could produce.

Flow break: sentence 2 depends on the reader already knowing the answer to the shard/replica question above. As written, "Because the check happens at the head, drift between replicas surfaces..." does not clearly follow from "...layouts stay consistent across shards" — it could be restating the first claim at finer grain or asserting a second, unconnected guarantee. Name the relation (same unit at finer grain vs. a second axis) instead of leaving the reader to infer it from two unlinked nouns.

Concrete rewrite: Ask author: is a "replica" a copy of one shard (so "drift between replicas" means drift within that shard's own copies), are shards and replicas independent, or are "shard" and "replica" naming the same unit here? Fallback: keep the paragraph as written. Its sequencing claim holds regardless of the answer — the head check runs before merge, so drift is caught at merge and not at read — only the shard/replica relationship is underspecified, and guessing at an architecture to resolve it risks stating something false about the system.

Rewrite check: The question names the missing mechanism instead of asserting an answer, and the fallback adds no new claim. Contains: no rule-of-three, no X-not-Y negative parallelism, no em-dash antithesis, no avoid-by-default phrases, no prestige adjectives, no decorative closure, no invented facts. Passes self-detectors.

Remembered line: The check runs at the head, before merge, so whatever drift exists becomes a merge-time finding rather than a read-time surprise.
