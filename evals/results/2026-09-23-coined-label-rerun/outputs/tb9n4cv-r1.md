## R1

Verdict: keep

Slop tells: The "so ... instead of ..." close reads like it could be a staccato contrast, but it's earned, not decorative — "replays from the last checkpoint" is backed by the named mechanism (write-ahead log, copy-on-write snapshots) in the first clause, and "dropping the job" names the exact failure that mechanism prevents. No watch-list words, no banned avoid-by-default phrases, no copula displacement (uses is a plain, working verb), no rule-of-three, no em-dash cadence.

Specificity missing: None. The sentence names both mechanisms (write-ahead log, copy-on-write snapshots), the precise failure window (between the enqueue and the fsync), and the recovery behavior (replay from the last checkpoint) rather than asserting durability in the abstract.

Inflated claim: None. Nothing is called important, robust, or seamless without support — the claim is carried entirely by the mechanism named in the same sentence.

Flow break: N/A — single standalone sentence, no surrounding paragraph.

Concrete rewrite: N/A — the sentence passes as written.

Rewrite check: N/A — no rewrite produced.

Remembered line: "a crash between the enqueue and the fsync" — the exact vulnerability window is the detail worth keeping.

## R2

Verdict: keep

Slop tells: "stale-edit sweep" is a nominalization, which the doctrine flags as a rhetorical-style-drift risk — but the clause immediately cashes it out ("which means it compares every draft's version number with the server's copy and discards drafts the server has already replaced"), so the abstraction is grounded in the same sentence rather than left to do the work alone. No watch-list words, no banned phrases, no copula displacement (runs, compares, discards are all concrete action verbs), no hedged symmetry, no em-dash cadence.

Specificity missing: None. Names the actor (the client), the trigger (before each upload), the exact comparison (draft's version number vs. server's copy), and the outcome (discards drafts already replaced).

Inflated claim: None.

Flow break: N/A — single standalone sentence.

Concrete rewrite: N/A — the sentence passes as written.

Rewrite check: N/A — no rewrite produced.

Remembered line: "compares every draft's version number with the server's copy" — the comparison a reader would go verify.

## R3

Verdict: keep

Slop tells: The name-then-colon shape ("an exact-head check: the indexer hashes...") can resemble the bullet/bold-header/colon tell, but that tell is about formatting standing in for missing content; here the colon opens onto a real mechanism (hash comparison across both replicas, a stated refusal condition), so the structure earns its keep. "Refuses the merge when they differ" uses "when" for the conditional relation instead of flattening it into two side-by-side clauses — exactly the hypotaxis the doctrine asks for. No banned phrases, no watch-list words, no copula displacement.

Specificity missing: None. Names the actor (the indexer), the mechanism (hashes the head revision on both replicas), and the exact trigger (refuses when they differ).

Inflated claim: None. "Exact-head check" is a label earned by the hash-equality mechanism described in the same breath, not an unsupported intensifier.

Flow break: N/A — single standalone sentence.

Concrete rewrite: N/A — the sentence passes as written.

Rewrite check: N/A — no rewrite produced.

Remembered line: "hashes the head revision on both replicas and refuses the merge when they differ" — the exact check condition.

## R4

Verdict: keep

Slop tells: "reaches the database once and the rest are served from memory" is a two-sided contrast worth running through the staccato-contrast test — both sides are evidenced by the clause that precedes it (a read-through cache with a five-minute TTL), so this is earned antithesis, not cadence standing in for evidence. "Sits behind" is ordinary architectural shorthand, not one of the flagged copula-displacement verbs (serves as, stands as, features, marks, represents). No watch-list words, no banned phrases.

Specificity missing: None. Names the architecture (read-through cache), the exact TTL (five minutes), and the precise behavior under load (one database hit, remaining requests from memory).

Inflated claim: None.

Flow break: N/A — single standalone sentence.

Concrete rewrite: N/A — the sentence passes as written.

Rewrite check: N/A — no rewrite produced.

Remembered line: "a burst of identical requests reaches the database once" — the concrete claim a reader would carry forward.
