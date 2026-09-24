Verdict: ask-author

Slop tells:
- Coined compound label: "exact-head checks" names a check but never says what is compared (hash/checksum of the head, byte-for-byte diff, a version or offset counter) or what "head" is a pointer into.
- Coined compound label: "editorial-row layouts" names a row type and a property of it, but never says what makes a row "editorial" or what "layout" means for one (storage order, schema, on-disk position, rendered form).

Specificity missing:
- The comparison method behind the head check.
- What "the head" is the head of (a per-shard log, a row sequence, a version chain).
- The definition of "editorial-row" and why that row type specifically needs the guarantee.
- Whether "shards" (sentence 1) and "replicas" (sentence 2) name the same unit or two different ones.

Inflated claim:
"so editorial-row layouts stay consistent across shards" moves from a check on one point (the head) to a guarantee about the whole layout. That move only holds if everything before the head is already known-identical, e.g. an append-only structure where the head is the only place two copies can diverge. The paragraph never states that invariant, so the sentence reads as settled where it is actually assumed.

Flow break:
Sentence 1 states the guarantee "across shards"; sentence 2 restates the failure mode as "between replicas" with nothing connecting the two nouns. A reader can't tell whether shard and replica are the same thing under two names, or whether replicas sit one level below shards (each shard has several), which would put the drift sentence 2 describes at a different granularity than the consistency sentence 1 claims.

Concrete rewrite:
Ask author: (1) What does the head check compare: a hash of the head, a full-row diff, a version/offset counter? (2) What makes a row "editorial" and what does "layout" mean for it? (3) Are "shard" and "replica" the same unit here, or does each shard have multiple replicas?

Fallback, cutting the undefined coinages and keeping only what the two sentences already support: "The indexer checks that each shard's head matches exactly across its copies before merging. Because the check runs at the head rather than over the whole shard, a copy that has drifted is caught at merge time instead of being served to a reader first."

Rewrite check: No rule-of-three, no X-not-Y, no em-dash antithesis, no avoid-by-default phrases, no prestige adjectives, no decorative closure. The fallback drops "exact-head" and "editorial-row" instead of guessing at what they mean, and uses the neutral "copies" instead of picking between "shard" and "replica." No invented names, counts, tools, or timings. Passes self-detectors.

Remembered line:
"A copy that has drifted is caught at merge time instead of being served to a reader first." This is already the paragraph's sharpest sentence; keep it as the carrier once "exact-head" and "editorial-row" are either defined or cut.
