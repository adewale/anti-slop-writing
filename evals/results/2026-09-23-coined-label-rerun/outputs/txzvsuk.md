## R1

Verdict: keep

Slop tells: None. Checked against banned phrases, high-risk words, copula displacement ("serves as" / "stands as" / "features" / "marks" / "represents" — none present), hedged symmetry, em-dash cadence, staccato contrast/parataxis, and rule-of-three — none found. "Stale-edit sweep" names a mechanism and "which means" immediately unpacks it; that's hypotaxis doing real definitional work, not decoration.

Specificity missing: None. The sentence names the actor (the client), the timing (before each upload), the comparison field (version number), the comparand (the server's copy), and the outcome (discards drafts the server has already replaced).

Inflated claim: None. No significance/importance language is used; the sentence stays at the mechanism level throughout.

Flow break: N/A — single sentence, no surrounding paragraph supplied.

Concrete rewrite: Not needed.

Rewrite check: N/A (no rewrite produced; verdict is keep).

Remembered line: "It compares every draft's version number with the server's copy and discards drafts the server has already replaced."

## R2

Verdict: ask-author

Slop tells: None stylistically — no banned phrases, no copula displacement ("sits behind" is locating language describing request-path position, not a prestige inflation), no hedged symmetry, no decorative em-dash clusters, no staccato contrast. The problem here is a mechanism gap, not a rhetorical one.

Specificity missing: The sentence claims a burst of identical requests "reaches the database once," but a read-through cache with a TTL only guarantees, by itself, that reads made after an entry exists are served from memory. It does not by itself guarantee that concurrent requests arriving during the same cache-miss window are deduplicated — that needs an additional named mechanism (per-key locking, single-flight, request coalescing) that the sentence never states. Without it, a true burst (near-simultaneous arrivals) can each miss the still-empty cache and each query the database — the standard cache-stampede case.

Inflated claim: "Reaches the database once" is stated as a flat, exact guarantee rather than a hedged one, so it claims more certainty than "read-through cache + TTL" alone supports.

Flow break: N/A — single sentence.

Concrete rewrite: Ask author: does the cache coalesce or lock concurrent misses on the same key (single-flight), so simultaneous requests wait on the first instead of each querying the database? If yes, name that mechanism in the sentence. Fallback, if that can't be confirmed: "The API sits behind a read-through cache with a five-minute time-to-live, so identical requests are served from memory for the rest of that window once the first one populates the cache." This keeps the TTL-caching claim that's fully supported and drops the unsupported concurrency guarantee.

Rewrite check: The fallback contains no rule-of-three, no negative parallelism, no em-dash antithesis, no banned avoid-by-default phrases, no prestige adjectives, no decorative closure, and no invented facts — it narrows the claim to what's already supported rather than adding a new mechanism. Passes self-detectors.

Remembered line: "Identical requests are served from memory for the rest of that window once the first one populates the cache."

## R3

Verdict: keep

Slop tells: None. No banned phrases, no high-risk words, no hedged symmetry, no decorative dashes, no staccato contrast. "We call the pre-merge comparison an exact-head check:" names a term and defines it inline via a colon — the same name-then-define move the doctrine's "orphaned stream" example treats as earned technique, not jargon for its own sake.

Specificity missing: None. The sentence names the actor (the indexer), the mechanism (hashes the head revision on both replicas), and the condition/outcome (refuses the merge when the hashes differ).

Inflated claim: None. No significance language; the claim is scoped exactly to what the hash comparison does.

Flow break: N/A — single sentence.

Concrete rewrite: Not needed.

Rewrite check: N/A (no rewrite produced; verdict is keep).

Remembered line: "The indexer hashes the head revision on both replicas and refuses the merge when they differ."

## R4

Verdict: revise

Slop tells: None stylistically — no banned phrases, no copula displacement, no hedged symmetry, no decorative dashes, no staccato contrast. The problem is a mechanism error, not a rhetorical one.

Specificity missing: The sentence doesn't distinguish the two sides of the fsync boundary it names, and that boundary is exactly what the claim turns on.

Inflated claim: "A crash between the enqueue and the fsync replays from the last checkpoint instead of dropping the job" claims durability for the one window a write-ahead log does not yet cover. fsync is the durability barrier: before it completes, the enqueue is not yet on durable storage, so a crash in that window has nothing in the log to replay — that is the case where the job is lost, not recovered. Replay from the last checkpoint recovers entries whose fsync already completed before the crash, i.e., a crash *after* the fsync (and before the job is processed), not between enqueue and fsync. As written, the sentence names the one window its own mechanism does not protect.

Flow break: N/A — single sentence.

Concrete rewrite: "The queue uses a write-ahead log and copy-on-write snapshots, so once the enqueue is fsynced, a crash before the job is processed replays from the last checkpoint instead of dropping it." This corrects the boundary using only the mechanism already named (WAL, fsync, checkpoint) and adds no new facts, such as what happens to the caller on a pre-fsync crash, since the source doesn't state that.

Rewrite check: The rewrite contains no rule-of-three, no negative parallelism, no em-dash antithesis, no banned avoid-by-default phrases, no prestige adjectives, no decorative closure, and no invented facts. Passes self-detectors.

Remembered line: "Once the enqueue is fsynced, a crash before the job is processed replays from the last checkpoint instead of dropping it."
