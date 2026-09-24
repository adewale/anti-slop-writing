## R1

Sentence: "The client runs a stale-edit sweep before each upload, which means it compares every draft's version number with the server's copy and discards drafts the server has already replaced."

Verdict: keep

Slop tells: None. No prestige vocabulary, no copula displacement, no hedged symmetry, no banned phrases, no em-dash cadence, no rule-of-three, no unearned contrast. "Which means" is hypotaxis used correctly: it unpacks a named process ("stale-edit sweep") into its concrete mechanism instead of leaving the coined term to do unearned work.

Specificity missing: None. Actor (the client), mechanism (compares every draft's version number with the server's copy), and result (discards drafts the server has already replaced) are all named. The two coordinated verbs — "compares... and discards..." — are sequential steps of one mechanism, not two mechanisms bolted together for effect: the discard condition is exactly what the comparison detects, so the coordination is earned.

Inflated claim: None. The sentence carries no importance language ("critical," "ensures," "robust") that would need separate evidence — it just states what the sweep does.

Flow break: N/A — single isolated sentence, no surrounding paragraph.

Concrete rewrite: No rewrite needed. The sentence already has a named actor, a named mechanism, and a named result, with the relation stated ("which means") rather than implied by rhythm.

Rewrite check: passes self-detectors — no rule-of-three, no X-not-Y, no em-dash antithesis, no banned phrases, no prestige adjectives, no decorative closure, no invented facts.

Remembered line: "compares every draft's version number with the server's copy and discards drafts the server has already replaced."

## R2

Sentence: "We call the pre-merge comparison an exact-head check: the indexer hashes the head revision on both replicas and refuses the merge when they differ."

Verdict: keep

Slop tells: None. The colon introduces a definition, not a formatting trick — this is not the "bullet + bold-header + colon" fake-structure tell, which targets list-shaped padding, not a single defining clause. No prestige vocabulary, no copula displacement, no banned phrases, no em-dash cadence.

Specificity missing: None. Actor (the indexer), mechanism (hashes the head revision on both replicas), and the refusal condition ("when they differ") are concrete and tied together: "when they differ" names the exact condition produced by the hashing step just stated, so nothing is left for the reader to infer.

Inflated claim: None. "Exact-head check" is a coined term, but it is defined immediately and precisely by the clause that follows, so it is not a prestige label riding on unearned authority.

Flow break: N/A — single isolated sentence.

Concrete rewrite: No rewrite needed. Naming the term and then cashing it out mechanically (hash both sides, refuse on mismatch) is exactly the pattern the doctrine's worked examples reward.

Rewrite check: passes self-detectors — no rule-of-three, no X-not-Y, no em-dash antithesis, no banned phrases, no prestige adjectives, no decorative closure, no invented facts.

Remembered line: "the indexer hashes the head revision on both replicas and refuses the merge when they differ."

## R3

Sentence: "The API sits behind a read-through cache with a five-minute time-to-live, so a burst of identical requests reaches the database once and the rest are served from memory."

Verdict: keep

Slop tells: None. "Sits behind" is a locating verb describing real architecture, not a displaced copula from the watch list ("serves as," "stands as," "features," "marks," "represents") — it does concrete locating work, so it stays as is. No banned phrases, no prestige words, no em-dash cadence, no hedged symmetry.

Specificity missing: None. Cache type (read-through) and TTL (five minutes) are both named. "Reaches the database once and the rest are served from memory" is the standard, well-defined behavior of a read-through cache (miss goes to origin and populates the cache; hits are served locally), so the sentence isn't leaning on a term to do work it hasn't earned — "read-through cache" already carries that definition.

Inflated claim: None. The claim is scoped to "a burst of identical requests," not to all traffic or an unqualified performance guarantee.

Flow break: N/A — single isolated sentence.

Concrete rewrite: No rewrite needed. "So" correctly names the causal relation between the cache/TTL setup and the deduplication behavior instead of leaving it implied.

Rewrite check: passes self-detectors — no rule-of-three, no X-not-Y, no em-dash antithesis, no banned phrases, no prestige adjectives, no decorative closure, no invented facts.

Remembered line: "a burst of identical requests reaches the database once and the rest are served from memory."

## R4

Sentence: "The queue uses a write-ahead log and copy-on-write snapshots, so a crash between the enqueue and the fsync replays from the last checkpoint instead of dropping the job."

Verdict: ask-author

Slop tells: Phrasal coordination without mechanism. "A write-ahead log and copy-on-write snapshots" pairs two named mechanisms with "and," but the specific claim that follows — a crash between enqueue and fsync replays from the last checkpoint — is already fully explained by the write-ahead log plus checkpointing alone (replay the log entries since the last checkpoint; this is the standard WAL-recovery pattern). Copy-on-write snapshots is never tied to that outcome. Applying the syntax-relation test: to justify keeping "and copy-on-write snapshots" the reader has to supply an unstated connective — e.g., "because the checkpoint itself is captured as a copy-on-write snapshot, checkpointing is cheap enough to happen often" — and that fact isn't in the sentence. That's the tell: the coordination reads as more thorough than it is, because only one of the two named mechanisms is doing explanatory work for the claim actually made. Contrast with the doctrine's own keep example, "The queue is robust because each job has an idempotency key, a retry receipt, and a dead-letter cutoff": there each of three named mechanisms independently supports one general claim ("robust"). Here one specific causal claim is made, and only one of two named mechanisms is shown to produce it.

Specificity missing: How copy-on-write snapshots relates to "the last checkpoint" is not stated — whether the checkpoint is itself a copy-on-write snapshot (which would make the pairing earned) or whether snapshots serve a separate purpose (backups, replica bootstrapping, point-in-time reads) unrelated to this crash-recovery path.

Inflated claim: Borderline — not an importance word, but a credibility-by-association move: stacking a second named mechanism onto the explanation reads as more rigorous than the single-mechanism (write-ahead log + checkpoint) explanation that is actually doing the work.

Flow break: N/A — single isolated sentence.

Concrete rewrite: Ask author: is the last checkpoint itself captured as a copy-on-write snapshot (so checkpointing is cheap enough to run frequently), or do the two mechanisms serve separate purposes? Fallback without that fact — cut the unconnected clause: "The queue uses a write-ahead log, so a crash between the enqueue and the fsync replays from the last checkpoint instead of dropping the job."

Rewrite check: passes self-detectors — no rule-of-three, no X-not-Y, no em-dash antithesis, no banned phrases, no prestige adjectives, no decorative closure, no invented facts (the fallback only removes the clause the source never connected to the claim; it adds nothing).

Remembered line: "a crash between the enqueue and the fsync replays from the last checkpoint instead of dropping the job."
