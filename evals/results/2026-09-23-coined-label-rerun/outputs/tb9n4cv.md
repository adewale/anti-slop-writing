## R1

Sentence: "The queue uses a write-ahead log and copy-on-write snapshots, so a crash between the enqueue and the fsync replays from the last checkpoint instead of dropping the job."

Verdict: keep

Slop tells: None. No banned phrase, no high-risk word, no copula displacement, no hedged symmetry, no em-dash cadence, no negative parallelism, no rule-of-three padding (only two mechanisms are named, and both do work).

Specificity missing: None. The sentence names the two mechanisms (write-ahead log, copy-on-write snapshots), the exact failure window (between enqueue and fsync), and the recovery behavior (replay from the last checkpoint).

Inflated claim: None. This is the false-positive-restraint case the skill calls out directly: compare to the skill's own worked keep example, "The queue is robust because each job has an idempotency key, a retry receipt, and a dead-letter cutoff." Here the claim ("doesn't drop the job") is scoped to, and earned by, the WAL-plus-checkpoint mechanism named in the same clause — it isn't a free-floating virtue word like "robust" or "reliable."

Flow break: N/A — standalone sentence, no surrounding paragraph to test for hinge or relation.

Concrete rewrite: Not needed. Per false-positive restraint, don't offer a synonym-only rewrite just because the sentence is dense with technical nouns; the mechanism is already doing the work the sentence claims for it.

Rewrite check: N/A — no rewrite produced, so nothing to run the self-detectors against.

Remembered line: "replays from the last checkpoint instead of dropping the job."

## R2

Sentence: "The client runs a stale-edit sweep before each upload, which means it compares every draft's version number with the server's copy and discards drafts the server has already replaced."

Verdict: keep

Slop tells: None. "which means" is hypotaxis used correctly (the skill's preferred move) to define a named process, not a hedge or a copula-displacement template. No banned phrase, no high-risk word.

Specificity missing: None. Actor (the client), timing (before each upload), comparison basis (version number vs. the server's copy), and the resulting action (discard superseded drafts) are all named.

Inflated claim: None. The sentence doesn't assert an unearned virtue like "keeps everything in sync" — it states the comparison and the discard rule directly.

Flow break: N/A — standalone sentence.

Concrete rewrite: Not needed. "Stale-edit sweep" could read as a coined label dropped without support, but the same clause immediately defines it via "which means it compares... and discards..." — the term is earned in place, so a rewrite would only be a synonym shuffle.

Rewrite check: N/A — no rewrite produced.

Remembered line: "discards drafts the server has already replaced."

## R3

Sentence: "We call the pre-merge comparison an exact-head check: the indexer hashes the head revision on both replicas and refuses the merge when they differ."

Verdict: keep

Slop tells: None. The colon introduces a real mechanism (hash both replicas' head revisions, refuse on mismatch), not a fake bolded-header structure. No banned phrase, no high-risk word, no hedging.

Specificity missing: None. Names the actor (the indexer), the mechanism (hashing the head revision on both replicas), and the exact trigger condition (refuses the merge when the hashes differ).

Inflated claim: None. "Exact-head check" is a coined term, but like R2's "stale-edit sweep," it's defined in the same sentence by a concrete mechanism rather than left to sound authoritative on its own.

Flow break: N/A — standalone sentence.

Concrete rewrite: Not needed — same earned-label pattern as the skill's worked keep example: a named term is fine when the sentence supplies the mechanism behind it, and this one does.

Rewrite check: N/A — no rewrite produced.

Remembered line: "refuses the merge when they differ."

## R4

Sentence: "The API sits behind a read-through cache with a five-minute time-to-live, so a burst of identical requests reaches the database once and the rest are served from memory."

Verdict: keep

Slop tells: None. "sits behind" is a locating verb, the kind the copula-displacement detector explicitly keeps ("serves as/stands as/features/marks/represents" are the flagged substitutions; a plain locating verb doing real work is not one of them). No banned phrase, no high-risk word.

Specificity missing: None. Names the mechanism (read-through cache), the exact parameter (five-minute TTL), and the observable behavior under load (one database hit, the remaining requests served from memory).

Inflated claim: None. The claim stays bounded to what the cache and TTL actually produce; it doesn't stretch into an unscoped performance claim like "fast" or "scalable."

Flow break: N/A — standalone sentence.

Concrete rewrite: Not needed. The cache-plus-TTL mechanism directly earns the stated consequence.

Rewrite check: N/A — no rewrite produced.

Remembered line: "a burst of identical requests reaches the database once and the rest are served from memory."
