## R1

```txt
The queue uses a write-ahead log and copy-on-write snapshots, so a crash between the enqueue and the fsync replays from the last checkpoint instead of dropping the job.
```

Verdict: keep

Slop tells: None. No banned phrases, no prestige vocabulary, no hedged symmetry, no decorative em-dashes (none present), no negative parallelism, no rule-of-three padding. "Uses" is a plain verb doing real work, not a displaced copula.

Specificity missing: None for this skill's bar — the sentence names the mechanism (write-ahead log, copy-on-write snapshots), the exact failure window (between the enqueue and the fsync), and the resulting behavior (replay from last checkpoint), instead of asserting importance in the abstract. Both terms are domain-standard (comparable to the doctrine's own "dead-letter queue" / "two-phase commit" examples), so they don't need in-sentence definition. Outside this skill's rhetorical scope: a systems reviewer might still want to know whether "crash" here means a process crash (the OS page cache can retain the write and WAL replay recovers it even though fsync hadn't completed — consistent with this claim) or a full power-loss crash (where only a completed fsync protects the write). That's a technical-accuracy question worth confirming with the author, not a slop tell, and it doesn't change the verdict.

Inflated claim: None. "Instead of dropping the job" is earned by the named mechanism, not asserted as a bare claim of importance.

Flow break: N/A — standalone sentence, no surrounding paragraph.

Concrete rewrite: None needed.

Rewrite check: N/A — no rewrite produced; verdict is keep.

Remembered line: "replays from the last checkpoint instead of dropping the job" — the sentence already ends on its concrete carrier.

## R2

```txt
We call the pre-merge comparison an exact-head check: the indexer hashes the head revision on both replicas and refuses the merge when they differ.
```

Verdict: keep

Slop tells: None. "Exact-head check" is a coined compound label, but the false-positive-restraint carve-out applies directly: the coinage is defined in place, in the same sentence, right after the colon. "Exact" maps to the hash-equality check; "head" maps to the head revision — the name matches its own definition, so it doesn't relocate the gap. A reader can resolve the term without leaving the sentence.

Specificity missing: None. Actor named (the indexer), actions named (hashes, refuses), condition named (when they differ).

Inflated claim: None. No significance language is layered on top of the mechanism.

Flow break: N/A — standalone sentence.

Concrete rewrite: None needed.

Rewrite check: N/A — no rewrite produced; verdict is keep.

Remembered line: "hashes the head revision on both replicas and refuses the merge when they differ."

## R3

```txt
The API sits behind a read-through cache with a five-minute time-to-live, so a burst of identical requests reaches the database once and the rest are served from memory.
```

Verdict: keep

Slop tells: None. "Sits behind" is a locating verb — it states the cache's position in the request path — not a displaced copula like "serves as" or "represents," so the doctrine's exception for locating verbs applies. "Read-through cache" and "time-to-live" are domain-standard terms that don't need in-sentence definition.

Specificity missing: None for this skill's bar — the sentence gives a mechanism (read-through cache), a concrete parameter (five-minute TTL), and a specific outcome (one database hit, the rest from memory) instead of a vague performance claim. Outside this skill's rhetorical scope: "reaches the database once" is fully earned for requests spread across the TTL window, but "burst" usually implies near-simultaneous arrivals, and a plain read-through cache without request coalescing (a "singleflight"-style lock on the key) can let several concurrent misses all reach the database before the first response populates the cache — the standard cache-stampede failure mode. Worth confirming with the author whether the cache deduplicates concurrent misses on the same key; this is a technical-accuracy question, not a slop tell, and it doesn't change the verdict.

Inflated claim: None in the rhetorical sense (no unearned "importance" language). See the concurrency note above if the author wants the claim to hold under literal concurrent load rather than a burst spread across the TTL window.

Flow break: N/A — standalone sentence.

Concrete rewrite: None needed.

Rewrite check: N/A — no rewrite produced; verdict is keep.

Remembered line: "reaches the database once and the rest are served from memory."

## R4

```txt
The client runs a stale-edit sweep before each upload, which means it compares every draft's version number with the server's copy and discards drafts the server has already replaced.
```

Verdict: keep

Slop tells: None. "Stale-edit sweep" is a coined compound label, but — the same pattern as R2 — it is defined in place: "which means it compares every draft's version number with the server's copy and discards drafts the server has already replaced" gives the reader the actual mechanism immediately. "Stale" maps to "the server has already replaced"; "sweep" maps to "every draft." The name doesn't outrun its own definition.

Specificity missing: None. Actor named (the client), actions named (compares, discards), comparison basis named (version number vs. the server's copy), and the discard condition is specific (server has already replaced the draft) rather than a vague "keeps things in sync."

Inflated claim: None.

Flow break: N/A — standalone sentence.

Concrete rewrite: None needed.

Rewrite check: N/A — no rewrite produced; verdict is keep.

Remembered line: "discards drafts the server has already replaced."
