Paragraph reviewed:
"The indexer runs exact-head checks before each merge, so editorial-row layouts stay consistent across shards. Because the check happens at the head, drift between replicas surfaces during the merge rather than at read time."

Verdict: ask-author

Slop tells: Coined compound labels — "exact-head checks" and "editorial-row layouts" name a check and an artifact that the paragraph schedules and scopes but never defines. "at the head," "before each merge," and "across shards" say when and where the check runs, not what it compares or what the artifact is made of. A name is not a mechanism, and on the strength of this paragraph alone neither term is established domain vocabulary the way "two-phase commit" or "dead-letter queue" would be. Everything else is clean: no watch-list words, no banned phrases, no rule-of-three, no negative parallelism, no em-dash clustering, no copula displacement, no hedged symmetry.

Specificity missing: What "exact" compares is unstated — a content hash, a row count, a column/schema signature, or byte-for-byte equality of the serialized layout would each make the claim checkable, and right now none is named. What "editorial row" denotes is also unstated — a specific table/schema, a rendered page or section structure, and a CMS content-grid row are all plausible readings, and the paragraph gives no way to choose among them. Without one of these, "stay consistent" and "drift" are claims the reader has to take on trust rather than verify.

Inflated claim: None. The observability claim — drift surfaces at merge rather than at read time — is a direct, supported consequence of the stated check timing, not an inflated one.

Flow break: None. Sentence 2's "Because the check happens at the head" hinges directly on sentence 1's "exact-head checks ... before each merge," then extends it to a new, concrete consequence: when drift becomes visible. That is the hypotaxis the skill asks for (explicit "so" and "because" connectives, cause stated before effect); keep this structure in any rewrite.

Concrete rewrite: Ask author: (1) what does the exact-head check compare — a content hash, a row count, or a schema/column signature? (2) is "editorial-row layout" a term defined elsewhere in this document (a named table or schema), or does it need a one-clause gloss here? Fallback: keep the paragraph as written. Both terms read as plausible internal vocabulary that the surrounding document may already define, and guessing the comparison basis or inventing a gloss here would be worse than leaving it to the author.

Rewrite check: The ask-author questions and the fallback contain no rule-of-three, no "Not X. Y." / negative parallelism, no em-dash antithesis, no avoid-by-default phrases, no prestige adjectives, no decorative closure, and no invented facts — the fallback explicitly declines to invent the missing comparison basis or definition. Passes self-detectors.

Remembered line: "Drift between replicas surfaces during the merge rather than at read time" — a specific, checkable claim about when a failure becomes visible, earned by the stated check timing, and the line worth keeping even if the two terms above get tightened.
