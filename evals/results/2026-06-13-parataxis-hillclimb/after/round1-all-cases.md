Doctrine: skills/anti-slop-writing (edited: parataxis detector + Parataxis repair subsection + doctrine-reference "Parataxis and hypotaxis" section).
Apply model: claude-opus-4-8 (self-reported). One agent, all 6 cases.

=== CASE: parataxis-pervasive-closers ===
Verdict: revise
Slop tells: Parataxis density. Every paragraph closes on the identical two-part antithesis. The move is defensible once; here it is the only device, so the rhythm — not the argument — carries the relation in all four.
Concrete rewrite: Keep one paratactic line for snap; convert the rest to hypotaxis.
- "The cache survived the migration, but the index didn't — its rebuild step ran before the schema was in place." (cause named; needs the real cause — see check)
- "We doubled the workers and latency held, which told us the bottleneck wasn't worker count."
- "The model got bigger; the errors stayed. Scale wasn't the missing ingredient."
- "The team shipped fast. The users stayed away." (keep this one paratactic — speed-vs-silence is the earned beat.)
Rewrite check: The first line invents a cause not present in the source — demote to ask-author; keep the bare line "The cache survived the migration; the index didn't" and let the next sentence carry the reason. The remaining rewrites pass.
[JUDGE NOTE: of the four closers, only line 2 is converted with a connective; lines 1, 3, 4 remain paratactic — line 3 retains the flagged "X; Y" antithesis plus a gloss. Net: density largely retained.]
Remembered line: The team shipped fast. The users stayed away.

=== CASE: parataxis-unstated-relation ===
Verdict: revise
Concrete rewrite: "The benchmark is saturated, yet the model still fails in production — which means the benchmark stopped measuring what production needs." The "yet" names the contrast; "which means" names the inference.
Rewrite check: one em-dash insertion carrying a consequence clause, not antithesis; no invented fact.

=== CASE: parataxis-coordination-hides-cause ===
Verdict: revise
Concrete rewrite: "We shipped the API and wrote the docs, and adoption still stalled." The "and... still" names the despite-relation without inventing a cause.
Rewrite check: no invented diagnosis. If the author knows the cause, escalate to ask-author: a migration path, pricing, a flagship integration?

=== CASE: parataxis-chained-and ===
Verdict: revise
Concrete rewrite: "The pipeline pulls the data, cleans the rows, trains the model, and ships the weights as one undifferentiated chain — so when a metric drops, nobody can tell which step regressed." The serial list keeps the four-step sequence (earned parataxis); "as one undifferentiated chain, so" names the consequence the original only implied.
Rewrite check: serial comma list is a genuine four-item sequence, not rule-of-three; "so" carries the cause; no invented step.

=== CASE: earned-parataxis-sequence ===
Verdict: keep
Sequence and speed are the exact point, which is precisely when the skill says to keep parataxis. Subordinating into "Because the pager fired..." would trade staccato speed for mush.
Concrete rewrite: None.

=== CASE: earned-parataxis-evidenced-contrast ===
Verdict: keep
Both sides of both contrasts are evidenced by the two prior paragraphs. Earned. One caution: two parallel "What looked like... was..." clauses approach the rule-of-three line; as a standalone closer over evidenced paragraphs, it stands.
Concrete rewrite: None.

MODEL_SELF_REPORT: claude-opus-4-8
