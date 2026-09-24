Paragraph reviewed:
"The indexer runs exact-head checks before each merge, so editorial-row layouts stay consistent across shards. Because the check happens at the head, drift between replicas surfaces during the merge rather than at read time."

Verdict: ask-author

Slop tells: None of the usual cadence markers fire here — no rule-of-three, no em-dash antithesis, no hedged symmetry, no banned filler phrases, no copula displacement, no decorative parallelism. Both sentences are hypotactic ("so," "because," "rather than") instead of stacked parataxis, which the doctrine prefers. One coined-compound-label hit: "exact-head checks" names a specific check the paragraph never defines — sentence 2's "the check happens at the head" restates *where* the check runs, not *what it compares*. Lower-confidence secondary note: "editorial-row" is also unglossed; keep it if it's established vocabulary elsewhere in this document set, otherwise it has the same gap.

Specificity missing: What does "exact" verify at the head — byte-for-byte equality of the head row's content, a checksum/hash of it, or equality of a head pointer/offset? The paragraph supplies timing ("before each merge," "at the head") but not the comparison itself, so a reader can't tell which failure modes the check actually catches.

Inflated claim: Sentence 1 moves from a check scoped to "the head" to a claim about "editorial-row layouts stay consistent across shards" — the whole layout, not just the head. That jump only holds if the head comparison stands in for full row-layout state (for example, a hash that summarizes the row set). As written, the described mechanism supports a narrower claim ("head state matches across replicas before the merge proceeds") than the one actually made.

Flow break: None. Sentence 2 earns its "because" — it doesn't restate sentence 1's cadence, it adds the reason the timing matters (a mismatch is caught during merge, a controlled step, instead of later, when something reads the result). Keep this structure.

Concrete rewrite: Ask author — does the exact-head check compare a hash/checksum of the full head row, field-by-field equality of the head row, or just a head pointer/offset? And does that comparison stand in for the full editorial-row layout, or only for the head row itself?
Fallback, scoped to what the paragraph actually supports: "The indexer compares each shard's head row across replicas before merging, so a head-row mismatch is caught at merge time instead of surfacing later, at read time."

Rewrite check: The fallback contains no rule-of-three, no X-not-Y / negative parallelism, no em-dash antithesis, no avoid-by-default phrases, no prestige adjectives, no decorative closer, and no invented facts. It drops the unsupported full-layout claim and keeps only the timing claim (merge vs. read) that sentence 1's "before each merge" already evidences, and it restates "the check" as "head row" using a noun ("row") already present in the source's own "editorial-row." Passes self-detectors.

Remembered line: Drift caught during merge never reaches a reader.
