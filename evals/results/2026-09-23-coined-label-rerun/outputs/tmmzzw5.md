## R1

Sentence reviewed: "The API sits behind a read-through cache with a five-minute time-to-live, so a burst of identical requests reaches the database once and the rest are served from memory."

Verdict: keep

Slop tells: None. Checked as a hypothesis and dismissed: "read-through cache" and "time-to-live" are compound terms, but both are standard in the domain, the same class as "dead-letter queue" or "two-phase commit," so neither needs an in-sentence definition.

Specificity missing: None. The TTL is a named number (five minutes), the trigger is named (a burst of identical requests), and both outcomes are named (one request reaches the database, the rest are served from memory).

Inflated claim: None. The claimed behavior is the ordinary, direct consequence of a read-through cache with a TTL. Nothing is asserted beyond what the mechanism supports.

Flow break: N/A. Single sentence, no surrounding paragraph to check against.

Concrete rewrite: Not needed.

Rewrite check: N/A, no rewrite. The original already passes the self-detectors: no rule-of-three, no negative parallelism, no em-dash antithesis, no avoid-by-default phrases, no prestige adjectives, no decorative closure, no invented facts.

Remembered line: "A burst of identical requests reaches the database once; the rest are served from memory."

## R2

Sentence reviewed: "The client runs a stale-edit sweep before each upload, which means it compares every draft's version number with the server's copy and discards drafts the server has already replaced."

Verdict: keep

Slop tells: Flagged as a hypothesis, then dismissed. "Stale-edit sweep" is a coined compound label, but the same sentence defines it in place: "which means it compares every draft's version number with the server's copy and discards drafts the server has already replaced." The referent isn't left out of reach, which is the doctrine's explicit carve-out for coined labels.

Specificity missing: None. The comparison key (version number), both sides of the comparison (draft versus server's copy), and the resulting action (discard replaced drafts) are all named.

Inflated claim: None. "Stale-edit sweep" claims no more than the definition that follows it delivers.

Flow break: N/A. Single sentence.

Concrete rewrite: Not required for the verdict, but the name-then-gloss shape can tighten. Trading "which means it" for a colon pulls the name and its definition closer together: "The client runs a stale-edit sweep before each upload: it compares every draft's version number with the server's copy and discards drafts the server has already replaced." That is optional polish, not a slop fix.

Rewrite check: passes self-detectors. No rule-of-three, no negative parallelism, no em-dash antithesis, no avoid-by-default phrases, no prestige adjectives, no decorative closure, no invented facts.

Remembered line: "It compares every draft's version number with the server's copy and discards drafts the server has already replaced."

## R3

Sentence reviewed: "We call the pre-merge comparison an exact-head check: the indexer hashes the head revision on both replicas and refuses the merge when they differ."

Verdict: keep

Slop tells: Flagged as a hypothesis, then dismissed. "Exact-head check" is a coined compound label, but the sentence defines it in the same breath, in the strongest form of the carve-out: an explicit "We call X an exact-head check" followed immediately by the mechanism. The name fits the mechanism: hashing enforces exact agreement between the two head revisions, not approximate similarity, which is what "exact" refers to.

Specificity missing: None. Actor (the indexer), action (hashes the head revision), scope (on both replicas), and the condition and consequence (refuses the merge when they differ) are all named.

Inflated claim: None.

Flow break: N/A. Single sentence.

Concrete rewrite: Not needed.

Rewrite check: N/A, no rewrite. Passes self-detectors.

Remembered line: "The indexer hashes the head revision on both replicas and refuses the merge when they differ."

## R4

Sentence reviewed: "The queue uses a write-ahead log and copy-on-write snapshots, so a crash between the enqueue and the fsync replays from the last checkpoint instead of dropping the job."

Verdict: ask-author

Slop tells: "Write-ahead log" and "copy-on-write snapshots" are standard domain terms, the same class as "dead-letter queue," and need no in-line definition, so that hypothesis is dismissed. The real problem sits downstream of the word list, in the "so" clause. Applying the syntax-relation test: restate the relation with a connective. "Because the queue uses a write-ahead log and copy-on-write snapshots, a crash between the enqueue and the fsync replays from the last checkpoint instead of dropping the job." Supplying that "because" needs a fact the sentence does not give. Under ordinary write-ahead-log semantics, fsync is the durability boundary: a crash before fsync completes is normally the window where a write can be lost, not the window a checkpoint replay recovers. The sentence names the right pair of concepts (log, fsync, checkpoint) but asserts safety on what reads as the wrong side of that boundary.

Specificity missing: What makes the pre-fsync window recoverable is missing. Does the enqueue call block until the log write is fsynced, so the named window can never actually hold an unsynced entry? Does a separate durable buffer or an upstream retry cover it instead? Also missing: what the copy-on-write snapshot does in this specific recovery path. The explanation after "so" only uses the log-plus-checkpoint-replay mechanism; the snapshot is named but never connected to the claim.

Inflated claim: "replays from the last checkpoint instead of dropping the job" is stated as the direct consequence of a crash "between the enqueue and the fsync," which is the window before the write becomes durable. As written, the claim is not earned by the mechanism named.

Flow break: N/A. Single sentence.

Concrete rewrite: Ask author: does the enqueue call block until its log entry is fsynced, so the named window is effectively unreachable? Or is there a separate mechanism that recovers a pre-fsync write? Does the copy-on-write snapshot do any work in this recovery path, or does it cover a different guarantee, such as point-in-time rollback? Fallback if that is not available: cut the specific crash-window claim and state only what is directly supported: "The queue uses a write-ahead log and copy-on-write snapshots for crash recovery."

Rewrite check: the fallback line contains no rule-of-three, no negative parallelism, no em-dash antithesis, no avoid-by-default phrases, no prestige adjectives, no decorative closure, and no invented facts. It repeats only the two mechanisms the source already names.

Remembered line: Until the author confirms the mechanism, the only line it earns is "The queue uses a write-ahead log and copy-on-write snapshots for crash recovery." The enqueue-to-fsync window claim needs a name before it can be kept.
