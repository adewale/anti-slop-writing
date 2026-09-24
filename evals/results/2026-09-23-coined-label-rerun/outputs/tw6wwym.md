## R1

Sentence reviewed: "The queue uses a write-ahead log and copy-on-write snapshots, so a crash between the enqueue and the fsync replays from the last checkpoint instead of dropping the job."

Verdict: keep

Slop tells: None. No banned phrase or watch-list word appears. "uses" is a plain verb, not a displaced copula. "instead of dropping the job" is subordinated onto the main clause with "so... instead of," not paired as a standalone "Not X. Y." staccato, so it doesn't trip the antithesis detector — it's one hypotactic sentence, which the doctrine prefers over side-by-side clauses.

Specificity missing: None in the writing. The sentence names both mechanisms (write-ahead log, copy-on-write snapshots), the exact failure window (between enqueue and fsync, not just "a crash"), and the exact recovery step (replay from the last checkpoint). One thing worth confirming with whoever owns this system: if "enqueue" means the WAL append and that happens before the fsync, is that specific write durable enough to replay, or does the client end up retrying it instead? The sentence asserts the job survives; naming which of those two it is would make the claim checkable rather than just plausible.

Inflated claim: None. The sentence carries no importance language beyond the mechanism itself.

Flow break: Not applicable — single sentence, no surrounding paragraph. One grammar note, not a slop tell: the subject of "replays" is "a crash," but a crash doesn't replay anything; recovery does, triggered by the crash. Common shorthand in engineering prose, worth a fix only if you want the actor named precisely.

Concrete rewrite: Not required to clear this skill's detectors. To fix the subject: "so if a crash happens between the enqueue and the fsync, recovery replays from the last checkpoint instead of dropping the job."

Rewrite check: N/A — verdict is keep, so no rewrite was required. The optional variant above only reassigns the grammatical subject; it preserves the original claim's scope exactly and adds no new fact. No rule-of-three, no X-not-Y, no em-dash antithesis, no banned phrase. Passes self-detectors.

Remembered line: "replays from the last checkpoint instead of dropping the job."

## R2

Sentence reviewed: "The API sits behind a read-through cache with a five-minute time-to-live, so a burst of identical requests reaches the database once and the rest are served from memory."

Verdict: keep

Slop tells: None. "sits behind" names an actual position in the request path, which the doctrine keeps rather than flags ("keep the verb when it does concrete work... locating"). No banned phrase, no watch-list word, no hedged symmetry, no dash cadence.

Specificity missing: None in the writing. The TTL is a number (five minutes), the cache type is named (read-through), and the outcome is a ratio (one database hit, the rest from memory), not a vague efficiency claim. One thing worth confirming: "burst" could mean requests arriving concurrently, before the first response has populated the cache. A plain TTL cache doesn't by itself guarantee only one database hit in that case — that guarantee needs request coalescing on top of it. If the cache has that, the claim holds as written; if "burst" means sequential arrivals against an already-warm cache, it holds either way.

Inflated claim: None. The sentence states a specific split, not an abstract benefit.

Flow break: Not applicable — single sentence.

Concrete rewrite: Not required. To close the question above without asking the author: "so the first of a burst of identical requests reaches the database, and the rest, arriving within the TTL, are served from memory." This narrows the claim to what a TTL cache guarantees on its own.

Rewrite check: N/A — verdict is keep, so no rewrite was required. The optional variant narrows the claim rather than inventing a fact about request coalescing. No rule-of-three, no X-not-Y, no em-dash antithesis, no banned phrase. Passes self-detectors.

Remembered line: "reaches the database once and the rest are served from memory."

## R3

Sentence reviewed: "We call the pre-merge comparison an exact-head check: the indexer hashes the head revision on both replicas and refuses the merge when they differ."

Verdict: keep

Slop tells: None. The colon introduces a definition and its mechanism in one sentence of ordinary prose — not the bullet-plus-bold-header-plus-colon pattern the doctrine flags, which is about list formatting standing in for argument. No copula displacement, no hedged symmetry, no dash cadence, no banned phrase or watch-list word.

Specificity missing: None. The sentence names the actor (the indexer), the exact operation (hashes the head revision on both replicas), and the exact trigger for refusal (when the hashes differ).

Inflated claim: None. "Exact-head check" is a coined name, but the clause after the colon cashes it out immediately, so the name isn't carrying weight on its own.

Flow break: Not applicable — single sentence. "The pre-merge comparison" assumes context from outside this line, which is a property of reviewing an isolated sentence, not a defect in it.

Concrete rewrite: Not needed. Mechanism and trigger condition are both already stated.

Rewrite check: N/A — verdict is keep, no rewrite produced.

Remembered line: "hashes the head revision on both replicas and refuses the merge when they differ."

## R4

Sentence reviewed: "The client runs a stale-edit sweep before each upload, which means it compares every draft's version number with the server's copy and discards drafts the server has already replaced."

Verdict: keep

Slop tells: None. "which means" unpacks a named process (stale-edit sweep) rather than standing in for a canned transition like "this is where X comes in." No copula displacement, no hedged symmetry, no dash cadence, no rule-of-three, no banned phrase or watch-list word.

Specificity missing: None in the writing. The comparison is named precisely (version number against the server's copy), and the discard condition is concrete (drafts the server has already replaced), not a vague "keeps things in sync." One thing worth confirming: "discards" is reassuring shorthand. It's worth checking that the sweep only fires on drafts with no independent local edits — a true stale copy — and not on a draft the user kept editing past the server's version, which is a different case (redundant cache versus unsynced work) that this sentence doesn't distinguish.

Inflated claim: None. Nothing here claims the sweep is valuable in the abstract; it states what it checks and what it discards.

Flow break: Not applicable — single sentence.

Concrete rewrite: Not required. To close the question above without asking the author: "...and discards local copies the server has already superseded, leaving any draft with edits the server hasn't seen for the next sync pass." Use this only if it's actually true of the system.

Rewrite check: N/A — verdict is keep, so no rewrite was required. The optional variant adds no rule-of-three, no X-not-Y, no em-dash antithesis, no banned phrase — but it does state a behavior ("leaving any draft with edits... for the next sync pass") the source sentence doesn't confirm. Per the doctrine's rule against inventing facts to fill this slot, treat that clause as an ask-author placeholder, not something to publish as fact.

Remembered line: "discards drafts the server has already replaced."
