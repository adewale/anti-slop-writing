## R1

> The queue uses a write-ahead log and copy-on-write snapshots, so a crash between the enqueue and the fsync replays from the last checkpoint instead of dropping the job.

Verdict: keep

Slop tells: None. No avoid-list phrase, no copula displacement (the verb is the plain "uses," not "serves as"/"features"/"represents"), no rule-of-three, no em-dash, no hedged symmetry, no negative parallelism ("Not X. Y.").

Specificity missing: None. The sentence names the exact failure window ("a crash between the enqueue and the fsync") instead of a vague "if something fails," and names the two mechanisms responsible plus the exact recovery behavior ("replays from the last checkpoint").

Inflated claim: None. "Write-ahead log" and "copy-on-write" are standard domain terms in the same class as "dead-letter queue" or "two-phase commit," so they earn their use without needing in-line definition. The claim is scoped to the named crash window, not stretched into a general robustness claim.

Flow break: N/A — single sentence, no surrounding paragraph given.

Concrete rewrite: Not needed.

Rewrite check: N/A — no rewrite produced.

Remembered line: "a crash between the enqueue and the fsync" — the specific failure window is what a reader retains.

## R2

> The client runs a stale-edit sweep before each upload, which means it compares every draft's version number with the server's copy and discards drafts the server has already replaced.

Verdict: keep

Slop tells: None. "Stale-edit sweep" is a coined compound label, but the passage defines it in place: the "which means" clause immediately states the mechanism (compare each draft's version number against the server's copy) and the effect (discard drafts the server has already replaced). That satisfies the in-place-definition exception, so the coinage earns its claim instead of relocating the gap onto an undefined term.

Specificity missing: None. "Version number," "server's copy," and "drafts the server has already replaced" are concrete and checkable, not vague placeholders.

Inflated claim: None. No significance language; the sentence states a mechanism, not an importance claim.

Flow break: N/A — single sentence.

Concrete rewrite: Not needed. Optional punctuation tightening only, not a slop fix: "...runs a stale-edit sweep before each upload: it compares every draft's version number against the server's copy and discards drafts the server has already replaced." The "which means" clause is doing real definitional work (naming the mechanism), not padding, so this is a style choice, not something the verdict requires.

Rewrite check: N/A for the verdict (no rewrite required). The optional tightening above contains no rule-of-three, no negative parallelism, no em-dash antithesis, no avoid-list phrases, no prestige adjectives, and no invented facts — passes self-detectors.

Remembered line: "discards drafts the server has already replaced" — the concrete outcome the sweep exists to produce.

## R3

> The API sits behind a read-through cache with a five-minute time-to-live, so a burst of identical requests reaches the database once and the rest are served from memory.

Verdict: keep

Slop tells: None. "Sits behind" is a plain, standard technical verb phrase, not a listed copula-displacement term ("serves as," "stands as," "features," "marks," "represents"). "Read-through cache" is standard domain terminology, so it doesn't need a local definition to earn its use.

Specificity missing: None. "Five-minute time-to-live" is a real, falsifiable number, not "for a period of time." The consequence is quantified precisely: the database is hit "once," and the rest come "from memory."

Inflated claim: None. The claim matches exactly what a TTL-based read-through cache does; nothing generalizes past the named mechanism.

Flow break: N/A — single sentence.

Concrete rewrite: Not needed.

Rewrite check: N/A — no rewrite produced.

Remembered line: "a burst of identical requests reaches the database once" — a quantified, checkable behavior.

## R4

> We call the pre-merge comparison an exact-head check: the indexer hashes the head revision on both replicas and refuses the merge when they differ.

Verdict: keep

Slop tells: None. "Exact-head check" is a coined compound label — the sentence even flags it as a coinage ("We call... an exact-head check") — but the colon clause defines it immediately: "the indexer hashes the head revision on both replicas and refuses the merge when they differ." That is the in-place-definition exception at work, so the name earns its claim rather than supplying the texture of precision while the referent stays out of reach.

Specificity missing: None. Actor (the indexer), mechanism (hashes the head revision on both replicas), and consequence (refuses the merge when they differ) are all named.

Inflated claim: None. "Exact" is doing real work, not decoration: it marks that any hash mismatch blocks the merge rather than only a "significant" one, which is exactly what "refuses the merge when they differ" states.

Flow break: N/A — single sentence.

Concrete rewrite: Not needed.

Rewrite check: N/A — no rewrite produced.

Remembered line: "refuses the merge when they differ" — the concrete, binary consequence.
