# Writing Review — R1–R4

Applying `anti-slop-writing`'s Critique output format. Each verdict is driven by the False-positive-restraint rule (treat detector hits as hypotheses, name the support before returning `keep`) and the Coined-compound-label carve-out (keep a coined term when the domain already standardizes it, or when the passage defines it in place).

## R1

> The API sits behind a read-through cache with a five-minute time-to-live, so a burst of identical requests reaches the database once and the rest are served from memory.

Verdict: keep

Slop tells: None confirmed. Working hypothesis: "read-through cache" and "time-to-live" are hyphen-flavored technical compounds, the shape the coined-compound-label detector watches for. Resolution: both are pre-existing, standard domain terms — the same class as the doctrine's own carve-out examples "dead-letter queue" and "two-phase commit" — not labels invented for this passage, so the detector does not fire.

Specificity missing: None. The sentence gives the exact TTL (five minutes) and the exact burst behavior (one database hit, remainder served from memory) instead of gesturing at "efficient caching" or "improved performance."

Inflated claim: None. There is no significance language riding alongside the mechanism ("crucial," "powerful," "seamless"); the sentence's only claim is the mechanical one, and the sentence spends its whole length proving that claim rather than asserting it.

Flow break: N/A — single sentence, no surrounding paragraph.

Concrete rewrite: Not needed. The sentence already states the actor (the cache), the condition (TTL, burst of identical requests), and the result (one DB hit, rest from memory) in one hypotactic clause ("so … reaches … and … are served").

Rewrite check: N/A — no rewrite produced; verdict is keep.

Remembered line: "a burst of identical requests reaches the database once and the rest are served from memory" — the cache mechanic itself is the carrier.

## R2

> The queue uses a write-ahead log and copy-on-write snapshots, so a crash between the enqueue and the fsync replays from the last checkpoint instead of dropping the job.

Verdict: keep

Slop tells: None confirmed. Working hypothesis: "write-ahead log" and "copy-on-write snapshots," paired with "and," could pattern-match the coined-compound-label or list-for-texture detectors. Resolution: both are standard, independently defined domain terms (WAL, COW), not coinages, matching the "dead-letter queue" / "two-phase commit" carve-out — and the sentence is structurally the same shape as the doctrine's own worked keep example, "The queue is robust because each job has an idempotency key, a retry receipt, and a dead-letter cutoff": named mechanisms earning a durability claim, not decoration.

Specificity missing: The sentence names the exact failure window ("between the enqueue and the fsync") rather than a vague "in case of failure," and the exact recovery point ("the last checkpoint") rather than "recovers gracefully." One soft spot: two mechanisms are named ("a write-ahead log and copy-on-write snapshots") but the outcome clause spells out only one strand explicitly ("replays from the last checkpoint"), so the reader has to infer that "checkpoint" is the snapshot and "replay" is the WAL played forward from it. That is a reasonable inference for a reader who already knows both terms, so it does not block `keep`, but it is the one place the sentence asks the reader to do linking work the syntax does not do for them.

Inflated claim: None. No significance language; the claim is plain and mechanical.

Flow break: N/A — single sentence.

Concrete rewrite: Not required for the verdict. Offered only to close the inference gap noted above: "so a crash between the enqueue and the fsync recovers from the last copy-on-write snapshot and replays the write-ahead log after it, instead of dropping the job." This is an optional tightening, not a fix for a confirmed slop tell — the source sentence already clears the keep bar on its own.

Rewrite check: The optional rewrite adds no rule-of-three, no X-not-Y / negative parallelism, no em-dash antithesis, no banned avoid-by-default phrase, no prestige adjective, no decorative closing, and no invented fact — it only makes explicit a pairing the source already implies. Passes self-detectors.

Remembered line: "a crash between the enqueue and the fsync replays from the last checkpoint instead of dropping the job" — names the exact failure window and the exact outcome.

## R3

> The client runs a stale-edit sweep before each upload, which means it compares every draft's version number with the server's copy and discards drafts the server has already replaced.

Verdict: keep

Slop tells: None confirmed. Working hypothesis: "stale-edit sweep" is a hyphen-adjacent coined compound naming a process — the paradigm case the coined-compound-label detector exists to catch ("the hyphen supplies the texture of precision while the referent stays out of reach"). Resolution: the same sentence defines the term in place via the "which means" clause (compares every draft's version number with the server's copy, discards drafts the server has already replaced). A name is not a mechanism, but here the mechanism arrives in the same breath as the name, which is exactly the carve-out condition.

Specificity missing: None. "compares every draft's version number with the server's copy" and "discards drafts the server has already replaced" are concrete operations, not a restatement of "stale-edit sweep" in different words.

Inflated claim: None.

Flow break: N/A — single sentence.

Concrete rewrite: Not needed; the sentence already pairs the coined term with its mechanism.

Rewrite check: N/A — no rewrite produced; verdict is keep.

Remembered line: "compares every draft's version number with the server's copy and discards drafts the server has already replaced."

## R4

> We call the pre-merge comparison an exact-head check: the indexer hashes the head revision on both replicas and refuses the merge when they differ.

Verdict: keep

Slop tells: None confirmed. Working hypothesis: "exact-head check," introduced by "We call X …," could read as a self-congratulatory naming flourish that leaves the referent undefined. Resolution: the colon opens directly onto the definition (hashes the head revision on both replicas, refuses the merge when they differ), so the term is defined in place rather than left to float. This is the strongest form of the carve-out — the sentence's own structure (name, colon, mechanism) makes the definition unavoidable.

Specificity missing: None. "hashes the head revision on both replicas" and "refuses the merge when they differ" name the exact operation and the exact trigger condition, not "checks for consistency."

Inflated claim: None.

Flow break: N/A — single sentence.

Concrete rewrite: Not needed.

Rewrite check: N/A — no rewrite produced; verdict is keep.

Remembered line: "the indexer hashes the head revision on both replicas and refuses the merge when they differ."
