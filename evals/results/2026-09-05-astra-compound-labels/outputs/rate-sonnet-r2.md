## P1

Verdict: keep

Slop tells: None found. No banned avoid-list phrases, no watch-list prestige words, no copula displacement (the verbs are "runs," "stay," "happens," "surfaces" — all plain and direct, none of "serves as / stands as / features / marks / represents"), no hedged symmetry ("Whether X or Y"), no em-dash cadence (no dashes present at all), no rule-of-three, no negative parallelism ("Not X. Y."), no bullet/bold/table fake structure.

Specificity missing: None. The paragraph names the actor (the indexer), the mechanism (exact-head checks run before each merge), the object being protected (editorial-row layout consistency across shards), and a falsifiable consequence (drift surfaces during the merge rather than at read time). That is sharp detail carrying the claim, not inflated significance standing in for it — the core principle the skill asks for.

Inflated claim: None. "Stay consistent" and "surfaces during the merge" are literal operational claims tied directly to the stated mechanism, not unearned importance language asserted without support.

Flow break: None. The second sentence opens with "Because," correctly subordinating mechanism to consequence (hypotaxis over parataxis, the syntax-relation the doctrine prefers) and answers the question the first sentence raises — what does checking at the head buy you — rather than merely sitting beside it.

Concrete rewrite: Not needed — the passage already meets the bar.

Rewrite check: N/A — no rewrite offered; verdict is keep.

Remembered line: "Drift between replicas surfaces during the merge rather than at read time" — already concrete and carrier-bound.

## P2

Verdict: keep

Slop tells: None found. "Write-ahead log" and "copy-on-write snapshots" are precise systems-engineering terms used in engineering context (the doctrine's own watch list flags "robust" only "outside engineering context," which implies in-context engineering vocabulary is fine); neither is a watch-list word, a banned phrase, a displaced copula, or a hedged-symmetry template. No em-dashes, no rule-of-three, no bullet/bold fake structure.

Specificity missing: None. The mechanism is named concretely (write-ahead log plus copy-on-write snapshots), the failure window is named precisely ("a crash between the enqueue and the fsync"), and the recovery behavior is stated exactly ("replays from the last checkpoint instead of dropping the job").

Inflated claim: None. The sentence claims only what the named mechanism supports; it does not reach for unearned significance.

Flow break: None. "So" carries the mechanism-to-consequence relation within one sentence. The closing contrast — replays from checkpoint "instead of" dropping the job — is earned antithesis under the staccato-contrast test: both sides are evidenced by the write-ahead-log/snapshot mechanism named earlier in the same sentence, not implied by cadence alone.

Concrete rewrite: Not needed — the passage already meets the bar.

Rewrite check: N/A — no rewrite offered; verdict is keep.

Remembered line: "A crash between the enqueue and the fsync replays from the last checkpoint instead of dropping the job" — a specific, inspectable claim.

## P3

Verdict: keep

Slop tells: None found. "We call ... an exact-head check" is a plain naming/definition construction, not a displaced copula from the watch list ("serves as," "stands as," "features," "marks," "represents") and not an inflation of a simple "is." The colon introduces a definition inside running prose, not a bullet/bold/table fake-structure pattern. No banned phrases, no watch-list words, no em-dashes, no hedged symmetry, no rule-of-three.

Specificity missing: None. The paragraph defines its own term in the same breath it introduces it and immediately supplies the mechanism behind the name: hashing the head revision on both replicas and refusing the merge on mismatch.

Inflated claim: None. Every clause states an operational fact tied directly to the named mechanism; nothing is asserted on the strength of the label alone.

Flow break: None — one sentence, definition and mechanism joined by a colon with no gap between naming the check and explaining what it does.

Concrete rewrite: Not needed — the passage already meets the bar.

Rewrite check: N/A — no rewrite offered; verdict is keep.

Remembered line: "The indexer hashes the head revision on both replicas and refuses the merge when they differ" — concrete and mechanism-bearing.
