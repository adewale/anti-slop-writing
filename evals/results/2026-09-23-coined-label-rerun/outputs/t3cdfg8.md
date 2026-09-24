## R1

Review sentence: "The queue uses a write-ahead log and copy-on-write snapshots, so a crash between the enqueue and the fsync replays from the last checkpoint instead of dropping the job."

Verdict: keep

Slop tells: None triggered. "write-ahead log" and "copy-on-write snapshots" are hyphenated compounds, but both are standard, pre-existing domain terms — the same class as the doctrine's own examples of coinages that don't need in-passage definition ("dead-letter queue," "two-phase commit"). The sentence is hypotactic ("so … instead of …" subordinates the consequence to the cause); it isn't a paratactic "Not X. Y." stack, and there's no em-dash, rule-of-three, or hedged-symmetry pattern.

Specificity missing: None. The sentence names both mechanisms (WAL, copy-on-write snapshots), the exact failure window (between the enqueue and the fsync), the recovery action (replay from the last checkpoint), and the avoided outcome (dropping the job). Actor, mechanism, and boundary are all present.

Inflated claim: None. The claim that the crash doesn't drop the job is a direct, checkable consequence of the two named mechanisms, not a significance claim riding on top of them.

Flow break: N/A — single isolated sentence, no surrounding paragraph to check flow against.

Concrete rewrite: Not needed; verdict is keep.

Rewrite check: N/A — no rewrite offered.

Remembered line: The sentence's own payload is already the carrier: "a crash between the enqueue and the fsync replays from the last checkpoint instead of dropping the job."

## R2

Review sentence: "We call the pre-merge comparison an exact-head check: the indexer hashes the head revision on both replicas and refuses the merge when they differ."

Verdict: keep

Slop tells: "exact-head check" is a coined compound label — a hyphenated noun phrase naming a check the passage invents. That would normally be a flag, but the same sentence defines it in place immediately after the colon: "the indexer hashes the head revision on both replicas and refuses the merge when they differ." That satisfies the doctrine's stated exception ("keep the coinage when the passage defines it in place"), so this is the earned case, not the undefined-jargon failure. "Pre-merge comparison" is plain compositional description (before merge + comparison), not a second coinage needing its own gloss.

Specificity missing: None. Actor (the indexer), mechanism (hash the head revision on both replicas), and consequence (refuse the merge on mismatch) are all named — nothing is left as an abstraction the reader has to take on faith.

Inflated claim: None. No significance language is layered on top of the mechanism (no "robust," "powerful," "critical"); the sentence names the check and states exactly what it does.

Flow break: N/A — single isolated sentence.

Concrete rewrite: Not needed; verdict is keep.

Rewrite check: N/A — no rewrite offered.

Remembered line: "the indexer hashes the head revision on both replicas and refuses the merge when they differ" — the definition itself is what a reader carries away.

## R3

Review sentence: "The API sits behind a read-through cache with a five-minute time-to-live, so a burst of identical requests reaches the database once and the rest are served from memory."

Verdict: keep

Slop tells: None triggered. "read-through cache" and "time-to-live" are standard caching-pattern terms, not passage-specific coinages, so they don't need in-place definition — same exemption class as R1's WAL/copy-on-write terms. No banned phrases, no high-risk words, no hedged symmetry ("whether X or Y"), no rule-of-three, no em-dash cluster. "So" again subordinates the effect to the cause (hypotaxis), not a bare juxtaposition.

Specificity missing: None. The TTL is a real number — five minutes, not "a short TTL" or "a brief caching window" — and the payoff claim is bounded and falsifiable: "reaches the database once," not a vague "reduces load on the database."

Inflated claim: None. The causal claim follows directly from the named mechanism (read-through cache + TTL); nothing is asserted beyond what that mechanism supports.

Flow break: N/A — single isolated sentence.

Concrete rewrite: Not needed; verdict is keep.

Rewrite check: N/A — no rewrite offered.

Remembered line: "a burst of identical requests reaches the database once and the rest are served from memory."

## R4

Review sentence: "The client runs a stale-edit sweep before each upload, which means it compares every draft's version number with the server's copy and discards drafts the server has already replaced."

Verdict: keep

Slop tells: "stale-edit sweep" is a coined compound label. Unlike R1/R3's terms, it isn't standard industry vocabulary, so it has to earn its keep by being defined in place — and it is, in the same sentence: "which means it compares every draft's version number with the server's copy and discards drafts the server has already replaced." "Which means" is the doctrine's own example of a hypotaxis connector, not a padding tell, and "sweep" is earned by "every draft" (the check runs over the full set, not a spot check on one).

Specificity missing: None. The trigger (before each upload), the comparison basis (version number vs. the server's copy), and the action (discard drafts the server already replaced) are all concrete and checkable.

Inflated claim: None. No significance language is attached to the mechanism; the sentence states what the client compares and what it drops, nothing more.

Flow break: N/A — single isolated sentence.

Concrete rewrite: Not needed; verdict is keep.

Rewrite check: N/A — no rewrite offered.

Remembered line: "it compares every draft's version number with the server's copy and discards drafts the server has already replaced."
