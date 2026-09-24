## R1

Sentence: "The client runs a stale-edit sweep before each upload, which means it compares every draft's version number with the server's copy and discards drafts the server has already replaced."

Verdict: keep

Slop tells: None. No avoid-by-default phrase or watch-list word appears. No copula displacement ("serves as"/"stands as"/"features"/"marks"/"represents"), no hedged symmetry template, no em-dash cadence (no dashes present), no rule-of-three or negative parallelism, no decorative antithesis. Hypotaxis is used correctly: "which means" subordinates the definition to the named mechanism, and "and discards" stays inside that same clause instead of restarting as a rhythm-matched parallel clause.

Specificity missing: None. The sentence names the actor (the client), the trigger (before each upload), the mechanism (compares every draft's version number with the server's copy), and the result (discards drafts the server has already replaced).

Inflated claim: None. "Stale-edit sweep" is a coined label, but it is unpacked in the same sentence instead of left to do rhetorical work on its own — the "more detail, earned importance" move the skill asks for, not the "less detail, more importance" failure. Unlike R3 and R4 below, the stated result follows directly and necessarily from the stated mechanism (a stale version number is, by definition, one the server has replaced); nothing beyond the named comparison has to be assumed for the sentence to be true.

Flow break: N/A — sentence reviewed in isolation; no surrounding paragraph was supplied to check against.

Concrete rewrite: Not needed. Per the false-positive restraint rule, a detector hit is a hypothesis, not a verdict, and nothing hits here — the sentence's own clauses supply the mechanism that would otherwise make "stale-edit sweep" read as inflated.

Rewrite check: N/A — no rewrite produced (verdict: keep). The retained sentence was already screened against the same self-detectors above (see Slop tells) and passes them.

Remembered line: "discards drafts the server has already replaced" — already concrete and carrier-bound; nothing to strengthen.

## R2

Sentence: "We call the pre-merge comparison an exact-head check: the indexer hashes the head revision on both replicas and refuses the merge when they differ."

Verdict: keep

Slop tells: None. No banned phrase or watch-list word, no copula displacement, no hedged symmetry, no em-dash cadence, no decorative antithesis. The colon does the job the skill asks of kept dash-insertions: it brackets an inline definition rather than supplying cadence. "when they differ" is a real conditional connective (hypotaxis), not a second clause placed beside the first for rhythm.

Specificity missing: None. Actor named (the indexer), mechanism named (hashes the head revision on both replicas), condition and result named (refuses the merge when they differ).

Inflated claim: None. "Exact-head check" is a label the sentence immediately earns by stating exactly what "exact" means here (hash equality of the head revision on both replicas). As in R1, the consequence is definitional, not an added empirical claim: "refuses the merge when they differ" follows necessarily from "hashes and compares," so nothing outside the named mechanism has to be assumed.

Flow break: N/A — sentence reviewed in isolation; no surrounding paragraph was supplied to check against.

Concrete rewrite: Not needed; nothing flagged.

Rewrite check: N/A — no rewrite produced (verdict: keep). The retained sentence was already screened against the same self-detectors above (see Slop tells) and passes them.

Remembered line: "refuses the merge when they differ" — the sentence's own mechanism-bound payoff.

## R3

Sentence: "The API sits behind a read-through cache with a five-minute time-to-live, so a burst of identical requests reaches the database once and the rest are served from memory."

Verdict: ask-author

Slop tells: None of the cadence-based tells (no banned phrase/word, no copula displacement, no hedged symmetry, no em-dash cadence, no antithesis). This is a claim-precision problem, not a rhythm problem — but it is still a "sharp detail beats inflated significance" failure: the detail is specific, but not fully earned by the named mechanism.

Specificity missing: The sentence doesn't say whether concurrent cache misses are coalesced (a single-flight/request-collapsing lock or equivalent) or handled independently. "Once" is a claim about concurrent-request behavior that a plain read-through cache with a TTL does not by itself guarantee.

Inflated claim: "reaches the database once" overclaims what a bare read-through TTL cache guarantees. A TTL cache guarantees that a request landing after the cache is populated is served from memory; it does not by itself guarantee that a *simultaneous* burst of first-time misses collapses to a single database read. Without a coalescing mechanism, several concurrent misses can each reach the database before any of them has finished populating the cache (the standard cache-stampede case). Applying the skill's syntax-relation test: restating "so" as an explicit connective requires an unstated assumption ("so, assuming concurrent misses are coalesced, a burst reaches the database once") — the sentence states the stronger, coalesced-burst behavior as if it followed directly from "read-through cache with a five-minute TTL" alone.

Flow break: N/A — sentence reviewed in isolation; no surrounding paragraph was supplied to check against.

Concrete rewrite: Ask author: does the cache coalesce concurrent misses (a single-flight lock or equivalent), so a simultaneous burst really does produce only one database read — or can several concurrent misses each reach the database before the first fill completes? If it coalesces, name that mechanism instead of leaving "once" to imply it, e.g., "a single-flight lock ensures only the first miss reaches the database; the rest wait on that fill." If it doesn't coalesce, narrow the claim to what the TTL alone earns, e.g., "so requests that land after the first one within the five-minute window are served from memory; a genuinely concurrent burst can still produce more than one database read before the cache fills." Fallback if the coalescing behavior can't be confirmed: cut the concurrency claim and keep only the TTL-hit claim — "so requests within the five-minute window are served from memory once the first one has populated the cache."

Rewrite check: The ask-author question and both fallback rewrites contain no rule-of-three, no X-not-Y/negative parallelism, no em-dash antithesis, no avoid-by-default phrases, no prestige adjectives, no decorative closure. Neither fallback invents a fact — both name the two possible states (coalesced / not coalesced) without asserting which is true. Passes self-detectors.

Remembered line: Once the fact is supplied, the line worth keeping is whichever one names the actual concurrency guarantee — the single-flight lock, or the "after the first fill" boundary — not "once" standing in for a mechanism the sentence hasn't named.

## R4

Sentence: "The queue uses a write-ahead log and copy-on-write snapshots, so a crash between the enqueue and the fsync replays from the last checkpoint instead of dropping the job."

Verdict: ask-author

Slop tells: None of the cadence-based tells. Like R3, this is a mechanism-precision issue rather than a rhythm issue.

Specificity missing: Two things the sentence needs and doesn't supply. First, how "copy-on-write snapshots" relates to "the last checkpoint" — is the checkpoint the copy-on-write snapshot itself, with the write-ahead log replaying only entries written since that snapshot? The sentence names both mechanisms but never states how they compose. Second, whether the enqueue call is acknowledged to the caller before or after the fsync completes — that fact determines whether the named crash window is actually recoverable.

Inflated claim: "replays from the last checkpoint instead of dropping the job" claims full recovery across a window — a crash between enqueue and fsync — that, under standard write-ahead-log semantics, is normally the one window where a write is *not yet durable*: fsync is what commits the log entry to disk, so a crash before it completes usually means that entry was never persisted, leaving nothing on disk for replay to recover. As written, the sentence claims its mechanism protects against the one failure window that, by the mechanism's own logic, it would not protect against — unless the enqueue call doesn't return success until after the fsync, in which case the crash is invisible to the caller (an unacknowledged job, not a dropped one) and the sentence should say that instead of "replays ... instead of dropping."

Flow break: N/A — sentence reviewed in isolation; no surrounding paragraph was supplied to check against.

Concrete rewrite: Ask author: does the enqueue call block until its write-ahead-log entry is fsynced (so a crash in that window is invisible to the caller and no acknowledged job is ever lost), or can a job be enqueued, crash before its fsync, and still come back — and if so, recovered from what durable record, given that fsync is what makes the entry durable? Also confirm whether "the last checkpoint" is the copy-on-write snapshot, with the log covering only entries since it. Fallback if enqueue is synchronous: "The queue's enqueue call returns only after its write-ahead-log entry is fsynced, so a crash never loses an acknowledged job; recovery replays whatever log entries were written since the last copy-on-write snapshot." Fallback if enqueue is asynchronous and the window can genuinely lose data: say that plainly instead of claiming full recovery — "a crash before the fsync completes can drop an enqueued-but-unsynced job; recovery from the last copy-on-write snapshot only replays what was already fsynced to the log."

Rewrite check: Both fallback rewrites and the ask-author question contain no rule-of-three, no X-not-Y/negative parallelism, no em-dash antithesis, no avoid-by-default phrases, no prestige adjectives, no decorative closure. Neither fallback invents a new fact; each states a conditional tied to which unconfirmed fact turns out to be true. Passes self-detectors.

Remembered line: Once confirmed, the line worth keeping is whichever one actually names the boundary of the guarantee — "returns only after its write-ahead-log entry is fsynced" if enqueue is synchronous, or the explicit admission of the loss window if it isn't. Either is more defensible than "instead of dropping the job" standing in for a guarantee the stated mechanism doesn't fully supply on its own.
