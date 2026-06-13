# Failure: pervasive parataxis defended instead of repaired

## Original

From the `tweet-taste-as-model` fixture (a real X thread arguing research taste is a
trainable model). Nearly every section closes on a paratactic antithesis:

```txt
what looked like perception was retrieval. what looked like a gift was inventory.
...
same cognitive hardware, opposite training loop.
...
that's not taste. that's an rss feed.
```

## Why it failed

When the skill was applied to the whole tweet (`evals/results/2026-06-13-tweet-taste-as-model/`),
the sub-agent ran the staccato contrast test per closer, found each one individually
earned (prior sentences evidence both sides), and **kept them all** — "I do not touch
any of this." It never asked whether the *piece* leans on the same paratactic move in
every section. The document-level over-reliance went unflagged.

## Mechanism

Parataxis density. Parataxis places clauses side by side and leaves the relation
unstated. Each instance can pass a per-sentence test while the piece as a whole uses
rhythm — not argument — to carry its relations. The per-sentence staccato test is
structurally blind to this; the lens has to be the whole document.

## What the round-1 and round-2 experiments showed

This looked like a doctrine gap, so a `Parataxis density` rule and a `Parataxis repair`
subsection were drafted for `SKILL.md`, plus six eval cases. Two A/B rounds
(`evals/results/2026-06-13-parataxis-hillclimb/`) measured before-edit vs after-edit
doctrine on Opus 4.8:

- Round 1 (6 cases, bare/unevidenced parataxis): both doctrines at ceiling; delta within
  noise (gate REJECT).
- Round 2 (`parataxis-earned-but-pervasive`, built so only a document-level check should
  fire): the **pre-edit** doctrine still caught it every time, via the staccato contrast
  test's "keep or use once" line and the "symmetrical paragraph length, parallel
  structure" tell. before 0.833 vs after 0.917 (N=3), within noise.

So the failure on the tweet was an **application inconsistency**, not a missing rule: the
doctrine already contains the tools ("use once", symmetrical-structure tell), and the
agent simply did not apply the across-the-piece lens during a long, multi-issue review.

## Rule added or changed

None in `SKILL.md` (the behavior change did not clear the gate; reverted — see
`evals/rejected-edits.md`). Kept: a `Parataxis and hypotaxis` teaching section in
`references/anti-slop-writing-doctrine.md` that *names* the concept and consolidates the
existing "use once" + symmetrical-structure guidance into one place, plus a
flow-by-relation diagnosis bullet. Six eval cases lock in the (already-passing) behavior:
`parataxis-pervasive-closers`, `parataxis-unstated-relation`,
`parataxis-coordination-hides-cause`, `parataxis-chained-and`,
`parataxis-earned-but-pervasive` (rewrite-evals), and the earned guards
`earned-parataxis-sequence`, `earned-parataxis-evidenced-contrast` (adversarial).
