## P1

Verdict: ask-author

Slop tells: Two coined compound labels stand in for mechanisms the passage never supplies: "exact-head checks" and "editorial-row layouts." Neither is standard, portable domain vocabulary (unlike, say, "write-ahead log"); both are local names invented for this passage, and a local name has to be earned by a local definition. Neither gets one.

Specificity missing:
- "exact-head checks" — sentence 2 supplies *when* the check runs (at the head, before merge) and *what it accomplishes* (drift surfaces at merge instead of at read time), but never says *how* it decides two heads differ — a hash, a byte-for-byte diff, a revision-number compare? The word "exact" is doing the work of a definition without supplying one.
- "editorial-row layouts" — completely unglossed. The reader can't tell whether this names a rendering format, a database row schema, a UI component, or something else, and has no way to picture what "inconsistent" would even look like here.

Inflated claim: None. The paragraph doesn't oversell — the failure is referential (naming without defining), not exaggeration.

Flow break: Sentence 1 makes two claims off one "so": checks run → row layouts stay consistent. Sentence 2 only follows up on the first claim (why the check catches drift early); the row-layout claim is dropped and never supported anywhere in the paragraph.

Concrete rewrite: Ask author — (1) What makes the check "exact": a hash of the head revision, a byte-for-byte diff, or a revision-number match? (2) What is an "editorial-row layout," and what would make one diverge across shards if the check didn't run? Fallback if those aren't available: cut "so editorial-row layouts stay consistent across shards" and end the sentence at "before each merge"; for the check itself, drop "exact" and write plain "head checks" until the comparison method can be named.

Rewrite check: The ask-author question and fallback contain no rule-of-three, no X-not-Y, no em-dash antithesis, no avoid-by-default phrases, no prestige adjectives, no decorative closure, and — the point of asking rather than guessing — no invented mechanism or artifact definition. Passes self-detectors.

Remembered line: Not yet available from the source. Once the author names the comparison mechanism, the line to keep is the existing "drift between replicas surfaces during the merge rather than at read time" — it's already concrete and should anchor whatever rewrite follows.

## P2

Verdict: keep

Slop tells: None. "Write-ahead log" and "copy-on-write" look hyphen-heavy on a surface scan, but both are established systems vocabulary — decades old, used across databases and filesystems — not labels coined for this passage. A term the reader can look up elsewhere doesn't need to be re-defined here.

Specificity missing: None. The mechanism is concrete and complete: WAL plus copy-on-write snapshots, with the vulnerable window named exactly ("between the enqueue and the fsync") and the recovery behavior stated ("replays from the last checkpoint").

Inflated claim: None.

Flow break: None — one sentence, cause and effect chained through "so," failure window and recovery named together with nothing deferred to a later clause.

Concrete rewrite: Not needed.

Rewrite check: N/A — no rewrite produced; the paragraph is kept as written.

Remembered line: "a crash between the enqueue and the fsync replays from the last checkpoint instead of dropping the job" — it names the exact failure window and the exact recovery behavior in one clause.

## P3

Verdict: keep

Slop tells: None. "Exact-head check" is a coined term, but it's coined and defined in the same breath: "We call the pre-merge comparison an exact-head check:" is immediately followed by the mechanism. The hyphenated name isn't standing in for anything the reader has to take on faith.

Specificity missing: None. The definition names the actor (the indexer), the operation (hashes the head revision on both replicas), and the decision rule (refuses the merge when they differ) — enough to reimplement the check from this sentence alone.

Inflated claim: None.

Flow break: None. Single sentence: name the term, then define it after the colon. Nothing is asserted before it's earned.

Concrete rewrite: Not needed.

Rewrite check: N/A — no rewrite produced; the paragraph is kept as written.

Remembered line: "the indexer hashes the head revision on both replicas and refuses the merge when they differ" — concrete and mechanism-bearing, and it doubles as both the term's definition and the paragraph's memorable line.
