## P1

Verdict: ask-author

Slop tells: "exact-head checks" and "editorial-row layouts" are compound labels coined for this system and used with confident specificity, but neither is cashed out. The paragraph states their downstream effects (shards stay consistent, drift surfaces at merge rather than later) while never saying what operation makes a check "exact-head" or what property makes a layout "editorial-row." That is informational density without mechanism: vocabulary that sounds precise standing in for a mechanism that was never supplied — the jargon-flavored twin of the core principle's "less detail, more importance."

Specificity missing: What makes the comparison "exact" (byte equality, a checksum, a hash of something)? What is "the head" — a version pointer, a row, a commit-like ref? What structurally defines an "editorial-row" layout, and what "consistent" concretely constrains (column order, a field set, something else)? None of this is recoverable from the two sentences given.

Inflated claim: None. The failure here is not borrowed importance language; both sentences are plainly factual in tone. The problem is that the tone of precision is not backed by an actual mechanism.

Flow break: None. The second sentence's "Because the check happens at the head" correctly subordinates a cause to its effect and elaborates on the first sentence rather than merely sitting beside it.

Concrete rewrite: Ask author: what operation makes the comparison "exact-head" — a hash of some field, a byte-for-byte equality check, a checksum? And what structurally defines an "editorial-row" layout — a column order, a schema shape, a specific field? Fallback without those facts: cut "exact-head" and "editorial-row" as unglossed labels, or add a short definitional clause after each term stating the actual comparison method and the actual layout property in the source's own terms. Do not borrow a mechanism from another system or paragraph without confirming it applies here.

Rewrite check: passes self-detectors — the question names exactly the missing mechanism rather than asserting one; the fallback does not invent a hash method, count, or timing; no rule-of-three, no X-not-Y, no em-dash antithesis, no banned phrases, no prestige adjectives, no decorative closer.

Remembered line: None yet. A memorable line needs the missing mechanism — once the comparison method and the layout property are actually named, a sentence that states the term and then what it does in the same breath would earn one; right now the terms only imply that such a sentence exists.

## P2

Verdict: keep

Slop tells: None. "Write-ahead log" and "copy-on-write snapshots" are established, industry-standard terms rather than labels invented for this paragraph, so they carry a referent a technical reader already has — they do not need to be redefined here. This is the false-positive-restraint case: a detector might flag dense technical nouns on sight, but the surrounding clause supplies the mechanism that earns them.

Specificity missing: None. The sentence names the exact failure window ("a crash between the enqueue and the fsync"), the recovery action ("replays from the last checkpoint"), and the averted outcome ("instead of dropping the job"). That is checkable engineering detail, not a claim resting on the vocabulary alone.

Inflated claim: None.

Flow break: None (single sentence). "So" correctly subordinates the consequence to the mechanism that produces it (the log and the snapshots).

Concrete rewrite: None needed.

Rewrite check: N/A — no rewrite offered; verdict is keep.

Remembered line: "A crash between the enqueue and the fsync replays from the last checkpoint instead of dropping the job" — names the exact failure window and its resolution, which is the sharp, checkable detail the doctrine asks for.

## P3

Verdict: keep

Slop tells: None. The coined term is introduced and defined in the same sentence: "We call the pre-merge comparison an exact-head check:" is immediately followed by the actual mechanism (hashes the head revision on both replicas, refuses the merge when they differ). The label is earned by mechanism rather than left to imply precision on its own, and the colon is doing real definitional work rather than standing in for structure.

Specificity missing: None. "Hashes the head revision," "on both replicas," and "refuses the merge when they differ" are all concrete and independently checkable.

Inflated claim: None.

Flow break: None. The sentence moves in one hypotactic unit from naming the term, to defining it, to stating the consequence, with "when they differ" naming the condition under which the merge is refused.

Concrete rewrite: None needed.

Rewrite check: N/A — no rewrite offered; verdict is keep.

Remembered line: "The indexer hashes the head revision on both replicas and refuses the merge when they differ" — the label survives because the sentence cashes it out as a specific hash comparison with a stated refusal condition, not because the name sounds technical.
