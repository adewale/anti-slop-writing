## P1

**Verdict:** ask-author

**Slop tells:** Two coined compound labels, both undefined and non-standard: "exact-head checks" and "editorial-row layouts." Neither is glossed anywhere in the paragraph, and neither is an established term in version-control, indexing, or storage engineering the way "write-ahead log" or "copy-on-write" are. The hyphens ("exact-head," "editorial-row") supply a texture of precision the passage never cashes out into a mechanism.

**Specificity missing:** What comparison makes the check "exact"? The second sentence says where the check runs ("at the head") and when drift surfaces ("during the merge rather than at read time"), but never says what is compared — a hash of the head revision, a version counter, a timestamp. "Editorial-row layouts" gets no gloss at all: not what "editorial" refers to, not what "layout" means here (row order on disk, a display arrangement, a schema), and no account of how the check touches it.

**Inflated claim:** "stay consistent across shards" is presented as a settled outcome of the check, but since both the check's comparison method and the thing it's protecting are undefined, the claim can't be weighed against a mechanism — it rests on the label doing work the sentence hasn't done.

**Flow break:** None. The second sentence is a well-formed "Because X, Y" construction that correctly elaborates timing (merge-time detection vs. read-time detection). The break is in definition, not transition.

**Concrete rewrite:** Ask author: (1) What does the exact-head check actually compare — a hash of the head revision, a version counter, something else? (2) What is an editorial-row layout, and how does the check keep it consistent? Fallback if those facts aren't available: cut "editorial-row layouts stay consistent across shards" and state the check's comparison directly — for example, modeled on how the term is defined elsewhere in this doctrine's own domain: "...runs exact-head checks before each merge: it hashes the head revision on both replicas and refuses the merge when they differ."

**Rewrite check:** passes self-detectors. The ask-author questions and fallback invent no tool, count, or mechanism; the fallback reuses only a definition already established for this exact term rather than inventing a new one, and contains no rule-of-three, X-not-Y, em-dash antithesis, banned avoid-by-default phrase, prestige adjective, or decorative closer.

**Remembered line:** The paragraph names two mechanisms and defines neither.

## P2

**Verdict:** keep

**Slop tells:** None. "Write-ahead log" and "copy-on-write" are hyphenated compounds, but both are standard, established terms in storage and database engineering — domain-standard vocabulary, not invented labels standing in for an undisclosed mechanism.

**Specificity missing:** None. The sentence names the actual failure window (a crash between the enqueue and the fsync), the recovery behavior (replay from the last checkpoint), and the outcome it avoids (dropping the job).

**Inflated claim:** None. Every claim maps to a named mechanism; nothing is asserted beyond what "write-ahead log," "copy-on-write," and "checkpoint" already entail.

**Flow break:** None. One self-contained sentence: mechanism, then consequence.

**Concrete rewrite:** Not needed.

**Rewrite check:** passes self-detectors (verdict is keep; no rewrite offered).

**Remembered line:** Enqueue, fsync, checkpoint, replay — the crash window and its recovery are both named in one clause.

## P3

**Verdict:** keep

**Slop tells:** None. "Exact-head check" is a coined compound, but the sentence defines it at the moment of coining — the colon after "an exact-head check" introduces the exact comparison (hash the head revision on both replicas) and the exact trigger (refuse the merge when they differ). A coinage defined in place earns its hyphen instead of hiding behind it.

**Specificity missing:** None. Comparison method (hash), scope (both replicas), and consequence (refuse merge on mismatch) are all named in the same sentence that introduces the term.

**Inflated claim:** None.

**Flow break:** None. Single sentence: name the term, then define it — no transition to evaluate.

**Concrete rewrite:** Not needed.

**Rewrite check:** passes self-detectors (verdict is keep; no rewrite offered).

**Remembered line:** "Exact-head check" earns its hyphen in the same breath it's coined — hash the head, refuse on mismatch.
