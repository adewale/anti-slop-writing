Verdict: ask-author

Slop tells:
- Coined compound label: "exact-head checks" names a check the passage never fully defines. "Head" plausibly means the latest record or tip of a shard's log/index (a reasonably standard sense, close to git's HEAD), but "exact" doesn't say what property is compared — row count, checksum, schema hash, timestamps all fit. The hyphen supplies the texture of precision; the comparison basis stays out of reach.
- Coined compound label: "editorial-row layouts" names an artifact the passage never defines. "Editorial row" is transparent enough (a row of editorial content), but "layout" is ambiguous — column order, field schema, and visual formatting all fit, and the paragraph doesn't say which one the check protects.
- Compressed antithesis: "during the merge rather than at read time." The merge side is evidenced by sentence 1 (the check runs before each merge, so drift showing up "during the merge" follows directly from that setup). The read-time side is asserted, not shown — nothing in the paragraph establishes that, absent this check, drift would otherwise surface specifically when data is read, rather than at write time or via a separate audit.

Specificity missing:
- What does "exact" compare at the head — a checksum, a row count, a schema hash, or something else?
- What counts as "editorial-row layout" — column order, field set, or formatting?
- What establishes the read-time alternative: is "drift surfaces at read time" an observed failure mode this check replaced, or the design assumption behind adding it?

Inflated claim:
None. The paragraph doesn't reach for significance language ("crucial," "seamless," and similar are absent). Its only overreach is structural, not rhetorical: it asserts a specific consequence ("layouts stay consistent") from an unnamed comparison, and asserts an unevidenced counterfactual (drift "at read time") rather than showing either.

Flow break:
None. Sentence 2 extends sentence 1 through a shared concrete carrier ("the check," "the head," "the merge"), and the "Because X, Y rather than Z" clause is exactly the hypotactic structure the doctrine prefers over side-by-side clauses.

Concrete rewrite:
Ask author: What does the exact-head check actually compare (row-count parity, a checksum, a schema hash)? What does "editorial-row layout" cover (column order, field schema, formatting)? And what shows that, without this check, drift would surface at read time specifically — a past incident, a design doc, or an inference from how reads are served?

Fallback (cut, no invented specifics): "The indexer checks each shard's head before merging, so row layout stays consistent across shards. Because the check happens at the head, drift between replicas surfaces during the merge rather than at read time." This drops "exact-" and "editorial-" — the two qualifiers the paragraph doesn't earn — and keeps every claim the source actually supports (actor, timing, and the merge-vs-read-time consequence) unchanged.

Fallback (keep as-is): if "exact-head check" and "editorial-row layout" are terms this document defines earlier, or that are already standard within the team's own docs, keep the original wording — the timing mechanism in sentence 2 is already concrete enough to stand on its own.

Rewrite check: The cut fallback reuses only source material — no rule-of-three, no "Not X. Y." or X-not-Y negative parallelism, no em-dash antithesis, no avoid-by-default phrase, no prestige adjective, no decorative closer — and invents no name, count, or mechanism. The merge-vs-read-time contrast from the source is carried over unresolved by design; that gap is routed to the ask-author question above rather than patched with a guess. Passes self-detectors.

Remembered line:
"Drift between replicas surfaces during the merge rather than at read time." Once "exact-head check" and "editorial-row layout" are pinned down, this is the sentence worth keeping — it names a concrete, testable design payoff (fail at merge, not at read) without leaning on either coined term.
