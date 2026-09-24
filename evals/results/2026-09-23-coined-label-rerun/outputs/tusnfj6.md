## R1

Sentence: "The client runs a stale-edit sweep before each upload, which means it compares every draft's version number with the server's copy and discards drafts the server has already replaced."

Verdict: keep

Slop tells: Checked for a coined compound label ("stale-edit sweep") — a hyphenated term naming a process. Cleared: the "which means" clause defines it immediately (version-number comparison, discard-on-replacement), so the coinage earns itself in place instead of gesturing at an undefined process.

Specificity missing: None. "Version number," "the server's copy," and "discards drafts the server has already replaced" are concrete enough that an implementer could code the sentence directly.

Inflated claim: None. The sentence makes no importance claim ("robust," "seamless," etc.) — it states what the sweep does and stops.

Flow break: None. "Which means" is doing real subordinating work: one move links the coined name to its own definition, rather than leaving the relation implied.

Concrete rewrite: Not needed. The sentence already answers "what does the sweep do" without requiring a second sentence.

Rewrite check: No rewrite produced. Checked the source itself against the list: no rule-of-three, no X-not-Y, no em-dash antithesis, no avoid-by-default phrases, no prestige adjectives, no decorative closure, no invented facts. Passes self-detectors.

Remembered line: "discards drafts the server has already replaced" — the actual decision rule, stated as an action.

## R2

Sentence: "The API sits behind a read-through cache with a five-minute time-to-live, so a burst of identical requests reaches the database once and the rest are served from memory."

Verdict: ask-author

Slop tells: No rhetorical tells fire — no banned phrases, no hedged symmetry, no em-dash or staccato antithesis, and no copula displacement ("sits behind" is doing real locating work, placing the cache in front of the API in the request path, so it stays). The problem is a superficial-analysis gap: a real mechanism is named, but the claim built on it is stronger than that mechanism alone supports.

Specificity missing: "Burst" doesn't say whether the identical requests are concurrent or merely close together in time, and that distinction is exactly what decides whether the sentence's claim is true.

Inflated claim: "Reaches the database once" is a hard guarantee. A read-through cache with a TTL guarantees that requests arriving after the cache is populated are served from memory until the TTL expires. It does not, by itself, guarantee that a burst of concurrent requests arriving before the first one has written the cache entry collapses to a single database read — that needs request coalescing (single-flight / lock-the-fill), which the sentence never names. Applying the syntax-relation test: restating the "so" as "because it's a read-through cache with a five-minute TTL, therefore concurrent identical requests hit the database exactly once" requires inserting a mechanism the sentence doesn't contain, so the "so" is carrying a claim the stated mechanism doesn't earn on its own.

Flow break: None syntactic — the "so" reads smoothly. The break is evidentiary, between the claim and what the named mechanism actually secures.

Concrete rewrite: Ask author: does the cache layer coalesce concurrent misses (single-flight / request-collapsing), or would simultaneous identical requests each miss independently before the first one populates the cache? Fallback, using only the mechanism already stated: "The API sits behind a read-through cache with a five-minute time-to-live, so once the cache is populated, repeated identical requests are served from memory until the TTL expires."

Rewrite check: The fallback contains no rule-of-three, no X-not-Y, no em-dash antithesis, no avoid-by-default phrases, no prestige adjectives, no decorative closure, and no invented mechanism — it restates only what a TTL read-through cache is defined to do. Passes self-detectors.

Remembered line: whichever way the author answers, the fact worth keeping is the one with the number in it — "a five-minute time-to-live" — since that's the concrete detail actually carrying the sentence.

## R3

Sentence: "The queue uses a write-ahead log and copy-on-write snapshots, so a crash between the enqueue and the fsync replays from the last checkpoint instead of dropping the job."

Verdict: ask-author

Slop tells: Both named mechanisms are domain-standard terms ("write-ahead log," "copy-on-write snapshots"), so no coinage is owed a definition on that count. The tell here is an omitted relation: two real mechanisms are listed, but the recovery claim only clearly follows from one of them.

Specificity missing: "The last checkpoint" arrives with a definite article, as if already established, but neither named mechanism was called a checkpoint. The write-ahead log explains the replay directly (entries survive the crash and get replayed). Copy-on-write snapshots are a common way to implement a checkpoint cheaply, but the sentence never says the snapshot is the checkpoint — the reader has to supply that link, not read it.

Inflated claim: "Replays from the last checkpoint instead of dropping the job" is stated as a flat guarantee. That guarantee is only as strong as the checkpoint mechanism, and the checkpoint mechanism is exactly the part left unresolved.

Flow break: None syntactic — "so" reads fine. The gap is the same omitted relation: applying the syntax-relation test, restating the sentence as "because copy-on-write snapshots serve as the checkpoint and the write-ahead log replays what happened since, a crash between enqueue and fsync recovers the job" requires supplying the "snapshot serves as the checkpoint" link myself. The source doesn't supply it, so filling it in would mean inventing it.

Concrete rewrite: Ask author: does a copy-on-write snapshot double as the checkpoint the replay restores from, with the write-ahead log covering everything logged after that snapshot — or is "checkpoint" a separate mechanism not named yet? Fallback that cuts rather than invents: "The queue uses a write-ahead log, so a crash between the enqueue and the fsync replays the log from the last checkpoint instead of dropping the job." (This drops "and copy-on-write snapshots" until its role in the checkpoint is confirmed, instead of asserting a connection the source never states.)

Rewrite check: The fallback contains no rule-of-three, no X-not-Y, no em-dash antithesis, no avoid-by-default phrases, no prestige adjectives, no decorative closure, and no invented mechanism — it only removes the unconnected term rather than guessing its role. Passes self-detectors.

Remembered line: "instead of dropping the job" — the concrete stake, worth keeping in any rewrite since it's the reason the mechanism matters.

## R4

Sentence: "We call the pre-merge comparison an exact-head check: the indexer hashes the head revision on both replicas and refuses the merge when they differ."

Verdict: keep

Slop tells: Checked for a coined compound label ("exact-head check"). Cleared, cleanly: the sentence flags its own coinage ("We call...") and cashes it out immediately after the colon with the actual mechanism — hash both heads, refuse on mismatch. Nothing is left for the reader to take on faith.

Specificity missing: None. Hashing both replicas' head revisions and comparing them is a complete mechanism for "exact" — there's no third undefined term doing unexplained work, unlike the checkpoint gap in R3.

Inflated claim: None. "Exact" is earned by the described mechanism rather than asserted independently of it — hash equality is what "exact" means here, and the sentence says exactly that.

Flow break: None. The colon does the job an earned em-dash pair or a "which means" clause would do elsewhere in this set: it brackets a definition right where the term is introduced, instead of leaving the coinage to float.

Concrete rewrite: Not needed. The definition is already inline and complete.

Rewrite check: No rewrite produced. Checked the source itself: no rule-of-three, no X-not-Y, no em-dash antithesis, no avoid-by-default phrases, no prestige adjectives, no decorative closure, no invented facts. Passes self-detectors.

Remembered line: "refuses the merge when they differ" — the concrete consequence that makes "exact" a check and not just a label.
