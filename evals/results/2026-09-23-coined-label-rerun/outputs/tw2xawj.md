Paragraph reviewed:

> The indexer runs exact-head checks before each merge, so editorial-row layouts stay consistent across shards. Because the check happens at the head, drift between replicas surfaces during the merge rather than at read time.

**Verdict:** ask-author

**Slop tells:**
- Coined compound label — "exact-head checks" (sentence 1). Sentence 2's "the check happens at the head" restates "head" instead of defining what makes the comparison "exact." The hyphen supplies the texture of precision; the referent stays out of reach.
- Coined compound label — "editorial-row layouts" (sentence 1). Never defined, glossed, or referenced again. Nothing says what makes a row "editorial" or what its "layout" covers.
- Compressed antithesis — "surfaces during the merge rather than at read time." The merge-time side is evidenced (the check runs pre-merge, at the head). The read-time side is a leap: nothing in the paragraph says what would make drift visible on read, or why it otherwise would be.

**Specificity missing:**
- What "exact" compares at the head: a content hash, a byte-for-byte row match, a version or sequence number, something else.
- What an "editorial-row" is, and what part of its "layout" is at risk of drifting across shards.
- What "surfaces ... at read time" would concretely look like without the pre-merge check — a checksum mismatch handed to a caller, differing row counts between two reads, or silent divergence caught only by a later audit.
- A smaller gap: sentence 1 says "across shards," sentence 2 says "between replicas." The paragraph never states the relationship (e.g., that each shard holds multiple replicas), so the reader has to supply it.

**Inflated claim:**
None. The paragraph isn't claiming importance ("crucial," "critical," etc.) — it's making a causal/timing claim (a pre-merge, at-the-head check causes cross-shard consistency and merge-time-not-read-time surfacing). The logic is plausible, but it rests entirely on the two undefined terms above, so as written it can't be checked, only trusted.

**Flow break:**
None between the sentences — sentence 2's "Because" answers the question sentence 1 raises (why does this check produce consistency, and what does running it at the head actually buy you). That hypotactic move is correct and should stay. The break is internal to sentence 2's own claim: the merge-vs-read-time contrast outruns the evidence sentence 2 itself supplies.

**Concrete rewrite:**
Ask author: (1) What does the exact-head check actually compare — a hash of the head row, a byte-for-byte match, a version/sequence number? (2) What is an editorial-row, and what specifically about its layout can drift between shards? (3) Without the pre-merge check, what would drift look like on read — a checksum mismatch returned to the caller, a row-count mismatch, or silent divergence found only by a later audit?

Fallback: if those facts aren't available, cut "exact-head" and "editorial-row" as unexplained coined labels and keep only the claim the paragraph can support without them: "The indexer compares [the defined thing] across shard replicas before merging, so a mismatch is caught at merge time." Drop "rather than at read time" unless the read-time alternative can be named — an unevidenced contrast is weaker than no contrast at all. If this paragraph sits inside a longer document that defines "exact-head check" and "editorial-row" nearby, it can stand as written and let that definition carry the weight.

**Rewrite check:**
The Concrete rewrite offers three author questions with named alternatives (hash / byte match / version number; checksum mismatch / row-count mismatch / silent divergence) — these are multiple-choice prompts for the author to answer, the same shape as the skill's own ask-author example, not a rhetorical rule-of-three. No X-not-Y negative parallelism, no em-dash antithesis (no em-dashes used), no banned avoid-by-default phrases, no prestige adjectives, no decorative closure. No invented facts: the fallback sentence uses a bracketed placeholder rather than asserting a specific mechanism. Passes self-detectors.

**Remembered line:**
"Exact-head" and "editorial-row" are hyphenated like mechanisms, but no sentence here says what either one actually compares.
