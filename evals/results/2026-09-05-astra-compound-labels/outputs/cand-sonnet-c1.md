## P1

Verdict: ask-author

Slop tells: Two coined compound labels stand in for mechanism: "exact-head checks" and "editorial-row layouts." Both are hyphenated noun phrases naming a process/artifact the paragraph never defines.

Specificity missing: "Exact-head checks" — the paragraph says only that "the check happens at the head," which restates the label's location claim but never says what makes the comparison "exact" (a hash match? a byte diff? a field-by-field comparison?). "Editorial-row layouts" has zero support anywhere in the paragraph — no indication what an "editorial-row" is (a CMS row, a spreadsheet row, a schema element) or which layout property "stays consistent."

Inflated claim: "layouts stay consistent across shards" reads as a settled engineering guarantee, but the guarantee rides on two undefined nouns. The hyphens supply the texture that the mechanism should supply: "exact-head" and "editorial-row" sound like established internal terminology, but nothing in the paragraph cashes that out.

Flow break: None internally — "Because the check happens at the head..." correctly subordinates the second sentence to the first. The problem is referential, not structural: the sentences are well joined, just joined around a gap.

Concrete rewrite:
Ask author: (1) What does the head comparison actually check — a content hash, a row count, a timestamp, a full diff? (2) What is an "editorial-row," and which property of its layout has to match across shards (column order, a formatting rule, a schema version)?
Fallback if those facts aren't available: cut both coinages and keep only what the paragraph already supports — "The indexer checks the head revision before each merge, so layouts stay consistent across shards. Because the check happens at the head, drift between replicas surfaces during the merge rather than at read time."

Rewrite check: The fallback contains no rule-of-three, no X-not-Y, no em-dash antithesis, no avoid-by-default phrase, no prestige adjective, no decorative closer, and no invented fact — it removes the unearned modifiers rather than replacing them with new ones. Passes self-detectors.

Remembered line: Independent of how the two terms get resolved, the paragraph's real claim survives without them: drift between replicas shows up at merge time, not at read time. That is the specific, testable thing worth keeping.

## P2

Verdict: keep

Slop tells: None. "Write-ahead log" and "copy-on-write" are hyphenated compounds, but they are established domain terminology, not coinages the passage invents — the term-is-standard-in-the-domain exemption applies directly.

Specificity missing: None. "A crash between the enqueue and the fsync" names an exact failure window; "replays from the last checkpoint" names the recovery step. Both are concrete enough to picture and to test.

Inflated claim: None. The claim — crash safety instead of job loss — is earned in the same sentence by the two named mechanisms (write-ahead log, copy-on-write snapshots) plus the specific recovery step (replay from last checkpoint), not asserted by cadence.

Flow break: None. The sentence subordinates correctly: "so" carries the consequence, and "instead of dropping the job" is a contrast grounded in the mechanism just described rather than a free-floating antithesis.

Concrete rewrite: Not needed — the paragraph already clears the bar.

Rewrite check: N/A — no rewrite offered.

Remembered line: "A crash between the enqueue and the fsync replays from the last checkpoint instead of dropping the job" — already the paragraph's carrier; a rewrite would not improve on it.

## P3

Verdict: keep

Slop tells: None. "Exact-head check" is a coined term, but the paragraph defines it in place: "We call the pre-merge comparison an exact-head check:" is followed immediately by the definition itself.

Specificity missing: None. The clause after the colon supplies the mechanism directly: hashes the head revision on both replicas, refuses the merge when they differ. That also explains why "exact" is the right word — the check requires a match, not a tolerance.

Inflated claim: None. No claim exceeds what the definition supports.

Flow break: None. The colon does the paragraph's structural work — name the term, then define it, in one motion.

Concrete rewrite: Not needed.

Rewrite check: N/A — no rewrite offered.

Remembered line: "the indexer hashes the head revision on both replicas and refuses the merge when they differ" — the definition is itself the memorable, reusable line.
