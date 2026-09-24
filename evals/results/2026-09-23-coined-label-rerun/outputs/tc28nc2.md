## R1

Sentence: "The client runs a stale-edit sweep before each upload, which means it compares every draft's version number with the server's copy and discards drafts the server has already replaced."

**Verdict:** keep

**Slop tells:** None. No banned avoid-by-default phrase, no high-risk/prestige word, no copula displacement, no rule-of-three, no hedged symmetry, no decorative em-dash, no staccato "Not X. Y." rhythm. "Which means" here unpacks what the named operation (a stale-edit sweep) actually does — a defining relation, not a filler connective standing in for an absent one.

**Specificity missing:** None load-bearing. The sentence names the actor (the client), the trigger (before each upload), the mechanism (compares version numbers), and the outcome (discards superseded drafts). One optional tightening: "the server's copy" elides "of that draft's version number," so the reader supplies the parallel noun themselves. Not a slop tell, just a possible clarity trim.

**Inflated claim:** None. "Discards drafts the server has already replaced" is a precise, checkable claim (server version newer than local version implies discard), and the sentence doesn't oversell it as more than a housekeeping step.

**Flow break:** N/A — single standalone sentence, no surrounding paragraph to test flow against.

**Concrete rewrite:** Not required; sentence passes as written. Optional tightening only: "...compares every draft's version number with the server's version number for that draft and discards any draft the server has already superseded."

**Rewrite check:** The optional tightening contains no rule-of-three, no X-not-Y, no em-dash antithesis, no banned phrase, no prestige adjective, no decorative closure, and invents no new fact — it only makes an existing referent explicit. Passes self-detectors.

**Remembered line:** "discards drafts the server has already replaced" — the concrete, checkable action the sentence is built on.

## R2

Sentence: "The API sits behind a read-through cache with a five-minute time-to-live, so a burst of identical requests reaches the database once and the rest are served from memory."

**Verdict:** keep

**Slop tells:** None. "Sits behind" is doing locating work — placing the API in the architecture relative to the cache — which the doctrine's copula-displacement carve-out keeps rather than flags; it isn't on the displaced-copula watch list ("serves as," "stands as," "features," "marks," "represents") and isn't a bare inflated copula. No banned phrases, no prestige words, no rule-of-three, no hedged symmetry, no em-dash.

**Specificity missing:** None. Names the mechanism (read-through cache), the exact TTL (five minutes), and the two-branch outcome (first request hits the database, the rest hit memory).

**Inflated claim:** Minor, non-blocking. "Reaches the database once" is exact only if the cache coalesces concurrent misses (single-flight / request-collapsing); a truly simultaneous burst against a cold cache, without that coalescing, could produce more than one database hit before the first response populates the cache. This is standard behavior for a "read-through cache" as usually built (most add coalescing specifically to prevent this), so the claim is a reasonable default reading rather than an overreach — worth a footnote only if the sentence needs to be literally exact rather than idiomatically true.

**Flow break:** N/A — single standalone sentence.

**Concrete rewrite:** Not required. If the author wants the precision gap closed: "...so the first request in a burst reaches the database and the rest, once the cache is populated, are served from memory."

**Rewrite check:** The optional rewrite contains no rule-of-three, no X-not-Y, no em-dash antithesis, no banned phrase, no prestige adjective, no decorative closure, and invents no new name/count/tool — it only turns "once" into "once the cache is populated," using terms already in the source. Passes self-detectors.

**Remembered line:** "a burst of identical requests reaches the database once" — the concrete before/after the sentence is built to demonstrate.

## R3

Sentence: "The queue uses a write-ahead log and copy-on-write snapshots, so a crash between the enqueue and the fsync replays from the last checkpoint instead of dropping the job."

**Verdict:** ask-author

**Slop tells:** None of the generic-AI patterns. No banned phrases, no prestige words, no copula displacement, no rule-of-three, no hedged symmetry, no decorative em-dash. The sentence is dense with named mechanism (write-ahead log, copy-on-write snapshots, checkpoint, enqueue, fsync) — exactly the register this skill asks for.

**Specificity missing:** None on vocabulary; the gap is in the timing claim itself (see Inflated claim).

**Inflated claim:** The sentence claims durability for the wrong side of its own named boundary. In a write-ahead log, fsync is normally the durability line: an entry is guaranteed to survive a crash only once it has been fsynced; a crash before the fsync is the classic window in which a WAL cannot help, because the entry may never have reached durable storage. This sentence describes "a crash between the enqueue and the fsync" — i.e., before the fsync completes — and claims that case "replays from the last checkpoint instead of dropping the job." That is the guarantee a WAL normally provides for a crash *after* the fsync, not before it. As written, the sentence asserts the recovery mechanism covers exactly the window it is normally powerless to cover.

**Flow break:** N/A — single standalone sentence.

**Concrete rewrite:** Ask author: does durability start at the enqueue call itself (for example a synchronous fsync-per-enqueue, or an in-memory buffer the checkpoint also captures), or only once the fsync completes? If the intended guarantee is the standard one, the fix is to move the safe boundary to after the fsync and state what happens before it: "a crash after the fsync replays from the last checkpoint instead of dropping the job; a crash before the fsync means the enqueue was never made durable, and [the producer retries / the job is resubmitted — confirm which]." Fallback if the author can't supply the retry detail: drop the "instead of dropping the job" claim for the pre-fsync case and state only the supported half: "a crash after the fsync replays from the last checkpoint; the write-ahead log gives no guarantee for a crash before it."

**Rewrite check:** The rewrite and its fallback name only mechanisms already in the source (fsync, checkpoint, enqueue) and mark the one missing fact — producer retry behavior — as a bracketed question rather than inventing it. No rule-of-three, no X-not-Y, no em-dash antithesis, no banned phrase, no prestige adjective, no decorative closure. Passes self-detectors.

**Remembered line:** "fsync is the line between an entry that survives a crash and one that doesn't" — the reusable structure, once the author confirms which side of that line the enqueue sits on.

## R4

Sentence: "We call the pre-merge comparison an exact-head check: the indexer hashes the head revision on both replicas and refuses the merge when they differ."

**Verdict:** keep

**Slop tells:** None. "We call the pre-merge comparison an exact-head check" is a named-term-then-mechanism construction, not a displaced copula or a rule-of-three; no banned phrases or prestige words appear.

**Specificity missing:** None. Names the actor (the indexer), the action (hashes the head revision on both replicas), and the exact trigger for refusal (hashes differ).

**Inflated claim:** None. Unlike R3, the described mechanism and the claimed guarantee point the same direction: hashing both replicas' current head and refusing to merge on a mismatch is a direct, checkable implementation of "exact" — there is no boundary condition here that the named mechanism fails to cover.

**Flow break:** N/A — single standalone sentence.

**Concrete rewrite:** Not required; sentence passes as written.

**Rewrite check:** N/A — no rewrite offered because none is needed.

**Remembered line:** "refuses the merge when they differ" — the concrete, checkable consequence that earns the term "exact-head check."
