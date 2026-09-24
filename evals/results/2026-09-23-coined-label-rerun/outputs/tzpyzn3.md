# Critique

Paragraph reviewed:

> The indexer runs exact-head checks before each merge, so editorial-row layouts stay consistent across shards. Because the check happens at the head, drift between replicas surfaces during the merge rather than at read time.

Verdict: ask-author

Slop tells: Two coined compound labels carry the whole claim without being defined: "exact-head checks" and "editorial-row layouts." Both read as precise engineering terms, but neither is standard domain usage the way "dead-letter queue" or "two-phase commit" is, and neither is defined in the passage. The hyphens supply the texture of precision; the referents stay out of reach.

Specificity missing:
- What does an "exact-head check" actually compare — a hash of the head row, full row equality, specific fields, or a row count? The paragraph never says.
- What makes a row "editorial" as opposed to any other row this indexer handles, and which part of its "layout" is at risk (column order, field mapping, row width)?
- Sentence 1 scopes consistency "across shards"; sentence 2 scopes drift "between replicas." The paragraph never states whether these are the same axis (a replica being a copy of a shard) or two different things the check spans.

Inflated claim: "So editorial-row layouts stay consistent across shards" promises an outcome — consistency is maintained — but the only mechanism described is detection: the check makes drift "surface" during the merge. Surfacing a mismatch is not the same as preventing or correcting one; that needs an enforcement step (the merge aborts, the drifted replica gets repaired, an operator is paged) that the paragraph never states. The evidence given supports "drift gets caught at merge time," not "layouts stay consistent." This isn't marketing-style inflation — no prestige adjectives, no banned phrases — it's the same failure in a quieter, technical register: a guarantee asserted where only a detection step was shown.

Flow break: Sentence 2 shifts the unit from "shards" to "replicas" without naming the relation between them. The "Because" clause is otherwise well-formed hypotaxis — it correctly states a timing consequence (checking at the head means drift is caught at merge, not at read) — but it inherits the undefined "head" from sentence 1 and adds a second unreconciled shift (shard to replica) instead of resolving the first.

Concrete rewrite:
Ask author: (1) What does the exact-head check compare — a hash of the head row, full row equality, specific fields, or something else? (2) Is a replica a copy of a shard, so "across shards" and "between replicas" mean the same scope, or are they different axes? (3) When the check finds a mismatch, what happens — does the merge abort or retry, does the drifted replica get repaired, is this alert-only, or something else? (4) What distinguishes an "editorial" row from the other rows this indexer handles?

Fallback if those facts aren't available: drop the unproven guarantee and the undefined qualifier, and keep only what the source actually supports: "The indexer compares shard heads before each merge. Because that comparison runs before the merge completes, drift between shards surfaces then, rather than later when a reader hits it." This keeps the one claim the paragraph earns — merge-time detection beats read-time discovery — and cuts "stay consistent" and "editorial-row," which the source never backs up. It does not name what the check compares or what happens on a mismatch, because that would be inventing a mechanism the source doesn't supply.

Rewrite check: The ask-author questions and the fallback both checked against the source's own detector list — rule-of-three, X-not-Y / negative parallelism, em-dash antithesis, avoid-by-default phrases, prestige adjectives, decorative closers, invented facts. None are present: the multiple-choice questions run four options deep (plus "something else") rather than a tidy triad, the one contrast in the fallback ("rather than later when a reader hits it") is earned because both sides — before the merge completes, when a reader hits it — are already stated in the source, and the fallback only removes unsupported claims rather than adding new specifics. Passes self-detectors.

Remembered line: Checking at the head catches drift at merge time, before a reader ever sees it. That's the one claim in the paragraph that's already concrete and already earned; the rest — what the check compares, what counts as "editorial," whether shard and replica are the same thing, and what happens after a mismatch — needs the author before it can carry the same weight.
