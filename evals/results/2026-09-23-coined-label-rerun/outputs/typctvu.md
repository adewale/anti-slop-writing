## R1

Sentence: "We call the pre-merge comparison an exact-head check: the indexer hashes the head revision on both replicas and refuses the merge when they differ."

Verdict: keep

Slop tells: None. Considered as a hypothesis and dismissed: "We call the pre-merge comparison an exact-head check:" has the shape of a throat-clearing label-then-explain move (compare "This is where X comes in"), but the colon is followed immediately by the actual mechanism rather than a deferral, so the label is earned on the spot, not decorative.

Specificity missing: None — actor (the indexer), objects (head revision, both replicas), action (hashes), and the refusal condition (when they differ) are all named.

Inflated claim: None. No significance language is asserted beyond what the mechanism itself supports.

Flow break: N/A — single sentence, no surrounding paragraph supplied.

Concrete rewrite: N/A — sentence stands as written.

Rewrite check: N/A — no rewrite produced; the sentence was run against the same detector list used to evaluate it and raised nothing that survives scrutiny.

Remembered line: "the indexer hashes the head revision on both replicas and refuses the merge when they differ" — the hash-then-refuse mechanism is the carrier.

## R2

Sentence: "The queue uses a write-ahead log and copy-on-write snapshots, so a crash between the enqueue and the fsync replays from the last checkpoint instead of dropping the job."

Verdict: keep

Slop tells: Flagged as a hypothesis: "a write-ahead log and copy-on-write snapshots" is a two-item phrasal coordination of technical nouns, the shape the doctrine's rhetorical-style-drift check watches for informational density without mechanism. Dismissed: the sentence goes on to name the exact failure window (between the enqueue and the fsync) and the exact recovery outcome (replay from the last checkpoint, not job loss) that these two mechanisms jointly produce. This is the same pattern as the skill's own worked keep example — "robust because each job has an idempotency key, a retry receipt, and a dead-letter cutoff" — a coordinated list of concrete named mechanisms each doing traceable work, not a borrowed rhythm standing in for evidence.

Specificity missing: None — the crash window and the recovery target are both named rather than left generic.

Inflated claim: None.

Flow break: N/A — single sentence.

Concrete rewrite: N/A — sentence stands as written.

Rewrite check: N/A — no rewrite produced; re-running the detectors used above against the sentence surfaces nothing that needs cutting.

Remembered line: "a crash between the enqueue and the fsync replays from the last checkpoint instead of dropping the job."

## R3

Sentence: "The client runs a stale-edit sweep before each upload, which means it compares every draft's version number with the server's copy and discards drafts the server has already replaced."

Verdict: keep

Slop tells: Flagged as a hypothesis: "which means" is a definitional hinge that can be lazy paraphrase — restating a label instead of earning it. Dismissed: the clause after "which means" supplies the actual mechanism (a version-number comparison and a specific discard condition), so the label "stale-edit sweep" is unpacked into concrete behavior rather than left to do the work on its own.

Specificity missing: None — the comparison basis (draft version number vs. the server's copy) and the discard condition (server has already replaced the draft) are both concrete.

Inflated claim: None.

Flow break: N/A — single sentence.

Concrete rewrite: N/A — sentence stands as written. Optional (style, not a slop fix): "before each upload, which means it compares" could tighten to a colon — "stale-edit sweep: it compares..." — to match R1's rhythm, but nothing here is inflated or vague enough to require it.

Rewrite check: N/A — no rewrite produced.

Remembered line: "compares every draft's version number with the server's copy and discards drafts the server has already replaced."

## R4

Sentence: "The API sits behind a read-through cache with a five-minute time-to-live, so a burst of identical requests reaches the database once and the rest are served from memory."

Verdict: keep

Slop tells: Flagged as a hypothesis: "sits behind" is a spatial-metaphor verb near the copula-displacement watchlist ("serves as," "stands as," "features," "marks," "represents"). Dismissed: it isn't one of the listed templates, and per the doctrine's own carve-out for that check, it is doing locating work — naming the API's position relative to the cache — which the rule keeps rather than flags.

Specificity missing: None — the TTL value (five minutes) and the exact request-path outcome (database once, the rest from memory) are both named, not gestured at.

Inflated claim: None.

Flow break: N/A — single sentence.

Concrete rewrite: N/A — sentence stands as written.

Rewrite check: N/A — no rewrite produced.

Remembered line: "a burst of identical requests reaches the database once and the rest are served from memory."
