## P1

Verdict: revise
Slop tells: Coined compound labels used without definition ("exact-head checks," "editorial-row layouts") block reader understanding despite clear mechanism.
Specificity missing: What specifically is an "exact-head check"? What constitutes an "editorial-row layout"?
Inflated claim: None.
Flow break: None; mechanism is clear once past the undefined terms.
Concrete rewrite: "The indexer compares the current revision on both shards before merging, so row layouts stay aligned. Because the comparison happens before the merge, replica drift surfaces during the merge operation rather than at read time."
Rewrite check: passes self-detectors.
Remembered line: Drift surfaces during merge, not at read time.

## P2

Verdict: keep
Slop tells: None; "write-ahead log" and "copy-on-write snapshots" are established technical terms, not coined.
Specificity missing: None.
Inflated claim: None.
Flow break: None.
Concrete rewrite: Not needed.
Rewrite check: Mechanism is concrete and specific (hashing, fsync, checkpoint replay); no banned phrases or prestige abstractions.
Remembered line: Crash replays from checkpoint instead of dropping the job.

## P3

Verdict: keep
Slop tells: None; coined term "exact-head check" is defined in place by the appositive that follows.
Specificity missing: None; definition is concrete (hashing head revisions, refusing merge on difference).
Inflated claim: None.
Flow break: None.
Concrete rewrite: Not needed.
Rewrite check: Coin-and-define pattern correctly models how to introduce technical compounds; no self-detector violations.
Remembered line: Exact-head check — indexer hashes both replicas and refuses merge when they differ.
