## R1

The API sits behind a read-through cache with a five-minute time-to-live, so a burst of identical requests reaches the database once and the rest are served from memory.

Verdict: keep

Slop tells: None. No avoid-by-default phrases, no high-risk/prestige words, no copula displacement ("sits behind" is a plain locating verb, not "serves as" / "stands as" / "features" / "marks" / "represents"), no hedged symmetry, no decorative em-dash, no unearned staccato antithesis. The sentence is hypotactic — "so" names the causal relation directly — instead of leaving two clauses to sit side by side.

Specificity missing: Little. The sentence names a real mechanism (read-through cache, five-minute TTL) rather than an abstract performance claim. One real gap: "reaches the database once" holds for a roughly sequential burst, but not necessarily for a genuinely concurrent one. Two identical requests that both miss the cache before the first database read returns will, in a plain TTL cache with no request coalescing, both reach the database — the standard cache-stampede case. The sentence doesn't say whether the burst is sequential or truly concurrent, or whether misses are coalesced.

Inflated claim: Borderline, not a rhetorical overclaim. "Once" is stated as an unconditional guarantee, which is accurate for the common case (only the first read in a window is a database read) but not for concurrent misses without coalescing. This is a scope gap, not manufactured importance — the sentence isn't inflating significance, it's just silent on one boundary condition.

Flow break: N/A — single sentence, no surrounding paragraph.

Concrete rewrite: Not required to keep the sentence. If the claim needs to hold under real concurrency, the missing piece is a coalescing mechanism: "...so identical requests are coalesced into a single in-flight read; the first one to miss reaches the database, and every other request in that five-minute window — concurrent or not — is served from memory." Use this only if coalescing actually exists; otherwise soften "once" to "at most once per cold window."

Rewrite check: N/A — no revision issued; the optional clause above states coalescing as a condition, not as an invented fact.

Remembered line: "a burst of identical requests reaches the database once" — it lands because the cache and its TTL are named, not asserted in the abstract.

## R2

The client runs a stale-edit sweep before each upload, which means it compares every draft's version number with the server's copy and discards drafts the server has already replaced.

Verdict: keep

Slop tells: None. No avoid-by-default phrases, no high-risk words. "Which means" is doing real defining work here — it unpacks the named mechanism ("stale-edit sweep") into its concrete steps, which is the move the doctrine wants, not the displaced-copula pattern it wants cut. No hedged symmetry, no em-dash, no staccato antithesis, no vague actor: the actors are "the client" and "the server."

Specificity missing: None of consequence. The sentence says what the sweep compares (each draft's version number), against what (the server's copy), and what it does on a mismatch (discards). That is the concrete mechanism the doctrine asks for in place of a label left unexplained.

Inflated claim: None. The sentence doesn't claim the sweep prevents conflicts or guarantees consistency — only that it discards drafts already known to be superseded. That claim is exactly what "compares version numbers, discards on mismatch" supports; nothing here reaches past the named mechanism.

Flow break: N/A — single sentence.

Concrete rewrite: None needed.

Rewrite check: N/A — no revision issued.

Remembered line: "compares every draft's version number with the server's copy and discards drafts the server has already replaced" — a checkable mechanism, not a description that could apply to any sync client.

## R3

The queue uses a write-ahead log and copy-on-write snapshots, so a crash between the enqueue and the fsync replays from the last checkpoint instead of dropping the job.

Verdict: revise

Slop tells: None of the rhetorical kind — no avoid-by-default phrases, no prestige words, no hedged symmetry, no decorative dashes. The sentence is hypotactic and mechanism-first, which is the right shape. The problem is not style; the claim contradicts the mechanism it cites.

Specificity missing: None — if anything the sentence is specific enough to expose the problem. It names the mechanism (write-ahead log, copy-on-write snapshots) and the exact failure window: "between the enqueue and the fsync."

Inflated claim: This is the real issue. A write-ahead log's durability guarantee begins at the fsync, not at the enqueue call — that is the reason systems fsync at all. "Between the enqueue and the fsync" names precisely the window where the record has not yet been made durable. Claiming a crash in that window "replays from the last checkpoint instead of dropping the job" asserts the opposite of what a WAL guarantees: a crash before the fsync completes is the case a WAL does not cover, not the case it recovers. As written, the sentence cites the mechanism that defines the danger window and then claims immunity inside that same window.

Flow break: N/A — single sentence.

Concrete rewrite: "The queue doesn't tell the caller a job is enqueued until the fsync completes. A crash before that point means the caller never got an acknowledgment and retries; a crash after it replays from the last checkpoint instead of dropping the job." This keeps the named mechanisms (WAL, checkpoint, fsync) and moves the guarantee to the side of the fsync boundary where a WAL actually provides it, instead of inventing a new mechanism.

Rewrite check: The rewrite does not reuse rule-of-three, "X isn't A, it's B," em-dash antithesis, avoid-by-default phrases, prestige adjectives, or decorative closure. The before/after split is an earned branch, not compressed antithesis — the two sides trigger different concrete outcomes (retry vs. replay), the same shape the doctrine's hedged-symmetry section calls out as worth keeping. No invented facts: the rewrite applies the standard fsync-is-the-durability-line property of the WAL already named in the source, rather than asserting a new mechanism. Passes self-detectors.

Ask-author fallback: If the actual design differs — e.g., "enqueue" already blocks internally until the fsync completes, so this window cannot occur, or a separate durability path (a synchronous replica acknowledgment, say) covers it — that is a fact this sentence doesn't supply. Ask: does the enqueue call return before or after the fsync, and is there any durability path besides the WAL for the pre-fsync window? Fall back to the rewrite above if not.

Remembered line: "a crash after the fsync replays from the last checkpoint" is the version of this line that actually matches what a write-ahead log promises.

## R4

We call the pre-merge comparison an exact-head check: the indexer hashes the head revision on both replicas and refuses the merge when they differ.

Verdict: keep

Slop tells: None. No avoid-by-default phrases, no high-risk words. The colon introduces one earned definition — a real, testable mechanism — not a bullet-plus-bold-header-plus-colon pattern used as fake structure. No hedged symmetry, no dashes, no staccato antithesis, no vague actor: "the indexer" is concrete.

Specificity missing: None of consequence. The check is fully specified: what is compared (the head revision, hashed), where (both replicas), and the consequence of a mismatch (the merge is refused).

Inflated claim: None. "Exact-head check" is earned by the mechanism named right after the colon — hash comparison, refuse on any difference — the same pattern the doctrine's false-positive-restraint example calls out as worth keeping: a term justified by a mechanism sitting next to it, not asserted on its own.

Flow break: N/A — single sentence.

Concrete rewrite: None needed.

Rewrite check: N/A — no revision issued.

Remembered line: "refuses the merge when they differ" — a concrete, binary consequence, not a vague claim about safety or correctness.
