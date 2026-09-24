## R1

Review sentence: "The client runs a stale-edit sweep before each upload, which means it compares every draft's version number with the server's copy and discards drafts the server has already replaced."

Verdict: keep

Slop tells: "stale-edit sweep" trips the coined-compound-label detector (a hyphenated noun phrase naming a process). But the same sentence defines it immediately via "which means..." — the coinage is earned in place, not left to float on the texture of the hyphen alone.

Specificity missing: none. The sentence names the actor (the client), the trigger (before each upload), the comparison (draft version number vs. the server's copy), and the exact discard condition (the server has already replaced the draft).

Inflated claim: none — no significance language is asserted anywhere; the sentence is pure mechanism from start to finish.

Flow break: none. "Which means" is hypotaxis doing real work: it turns a coined label into its own definition in one move instead of leaving the term to stand alone.

Concrete rewrite: not needed.

Rewrite check: n/a — no rewrite produced.

Remembered line: A draft gets discarded the moment the server's version number shows it's already been replaced.

## R2

Review sentence: "The API sits behind a read-through cache with a five-minute time-to-live, so a burst of identical requests reaches the database once and the rest are served from memory."

Verdict: keep

Slop tells: "read-through cache" and "time-to-live" could trip the coined-compound-label / prestige-vocabulary detectors on a skim, but both are standard, domain-established terms (the same bar the doctrine sets with "dead-letter queue" and "two-phase commit"), and the clause after "so" spells out the read-through behavior anyway: first request misses to the database, later identical ones hit memory. "Sits behind" is ordinary architecture idiom, not a displaced copula (not "serves as," "stands as," "features," "marks," "represents"), and it isn't inflating anything a plain "is" wouldn't already say.

Specificity missing: none — five minutes is a real number, and "reaches the database once" / "served from memory" name the exact before/after behavior for a burst.

Inflated claim: none.

Flow break: none. "So" makes the cause-to-effect relation explicit instead of leaving two clauses paratactically stacked with the relation implied.

Concrete rewrite: not needed.

Rewrite check: n/a — no rewrite produced.

Remembered line: One request pays the database; every identical request in the next five minutes doesn't.

## R3

Review sentence: "We call the pre-merge comparison an exact-head check: the indexer hashes the head revision on both replicas and refuses the merge when they differ."

Verdict: keep

Slop tells: "exact-head check" is a coined compound label, but the colon that follows defines it in the same sentence (hash the head revision on both replicas, refuse the merge on mismatch). This is the pattern the doctrine wants a coinage to meet, not the pattern it warns against — the referent is not left out of reach.

Specificity missing: none — the mechanism (hash comparison of the head revision across replicas) and the exact failure behavior (refuse the merge on divergence) are both named.

Inflated claim: none.

Flow break: none. The colon does the same job a "which means" clause does in R1: name the term, then define it, rather than naming it and moving on.

Concrete rewrite: not needed.

Rewrite check: n/a — no rewrite produced.

Remembered line: The merge is refused the instant the two replicas' head hashes stop matching.

## R4

Review sentence: "The queue uses a write-ahead log and copy-on-write snapshots, so a crash between the enqueue and the fsync replays from the last checkpoint instead of dropping the job."

Verdict: ask-author

Slop tells: none rhetorical. "Write-ahead log," "copy-on-write snapshots," "enqueue," "fsync," and "checkpoint" are standard, correctly-used domain terms — no banned phrases, no copula displacement, no em-dash antithesis, no rule-of-three, no hedged symmetry, no decorative cadence anywhere in the sentence.

Specificity missing: "the fsync" has two possible referents that carry different guarantees, and the sentence never says which one is meant: (a) the fsync that makes this specific job's own write-ahead-log entry durable, or (b) the fsync that finalizes the next copy-on-write checkpoint. The sentence also never states whether "the last checkpoint" is the copy-on-write snapshot named in the first clause or something else — the two named mechanisms (WAL, COW snapshots) are coordinated with "and" but only one of them is actually cashed out by the recovery claim that follows.

Inflated claim: under reading (a), the sentence claims a crash lands safely in exactly the window a write-ahead log's fsync boundary is normally understood not to cover. An entry that hasn't been fsynced yet is the standard case a crash *can* lose — that is the reason fsync exists — not the case the sentence claims it survives. The sentence names the fsync boundary and then asserts the guarantee on the far side of it, without naming whatever extra mechanism (a separately durable enqueue path, or a crash type narrow enough to spare the OS page cache) would make that reading true.

Flow break: none — this is a gap in evidence, not in structure.

Concrete rewrite: Ask author: does "the fsync" mean this job's own write-ahead-log entry being fsynced, or the next checkpoint's fsync? If it's the job's own fsync, what makes that specific write durable before the fsync runs? And is "the last checkpoint" the copy-on-write snapshot named in the first clause?

Fallback without inventing that mechanism: "The queue uses a write-ahead log, so a crash after a job's entry is fsynced replays it from the last checkpoint instead of dropping it." This keeps the claim to the part of the mechanism that is unambiguous — a durably fsynced entry survives and replays — and drops both the disputed pre-fsync window and "copy-on-write snapshots" until the author confirms what actually produces "the last checkpoint."

Rewrite check: passes self-detectors — no rule-of-three, no X-not-Y / negative parallelism, no em-dash antithesis, no banned avoid-by-default phrases, no prestige adjectives, no decorative closer ("that was the point," "in conclusion," "overall," "ultimately"), and no invented fact: the fallback relies only on fsync's standard meaning, which the source sentence had already invoked itself.

Remembered line: "The fsync" names two different moments in this sentence, and the crash-safety claim is only true for one of them.
