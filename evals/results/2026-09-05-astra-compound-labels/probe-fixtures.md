# Probe fixtures — coined compound labels

Three paragraphs. Each is otherwise clean of the doctrine's existing tells
(no importance language, no X-not-Y, no decorative dashes, no weak conclusion),
so a flag can only come from the compound-label behavior under test.

## P1 — coined labels, never defined

The indexer runs exact-head checks before each merge, so editorial-row layouts
stay consistent across shards. Because the check happens at the head, drift
between replicas surfaces during the merge rather than at read time.

## P2 — established technical compounds (adversarial guard)

The queue uses a write-ahead log and copy-on-write snapshots, so a crash between
the enqueue and the fsync replays from the last checkpoint instead of dropping
the job.

## P3 — coined label, defined in place (boundary)

We call the pre-merge comparison an exact-head check: the indexer hashes the head
revision on both replicas and refuses the merge when they differ.
