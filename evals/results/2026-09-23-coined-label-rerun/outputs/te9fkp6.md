Verdict: ask-author

Slop tells:
- Coined compound label: "exact-head checks" is a hyphenated, technical-sounding name for a process the paragraph never defines. The reader gets the check's purpose (layouts stay consistent) and its rough timing (before merge, "at the head"), but not what "exact" is comparing or what "head" is the head of. It isn't a standard domain term like "dead-letter queue," so it doesn't earn a pass on domain-standard grounds — it has to be defined in place, and it isn't.
- Coined compound label: "editorial-row layouts" has the same problem. "Editorial-row" is never defined, and "layout" is never given a referent (field order? schema? something else?). Nothing later in the paragraph resolves it.

Specificity missing:
- What "exact-head checks" compares to decide a match (field-by-field diff, checksum, version stamp) is not stated.
- What an "editorial-row layout" is — the thing that "stays consistent" — is not stated.
- What "the head" is the head of (a shard's row set, a replication log, a merge queue) is not stated.

Inflated claim: None. The paragraph doesn't reach for significance language — it makes one proportionate, mechanism-shaped claim (checking at the head catches drift at merge time instead of read time) and stops there.

Flow break: Sentence 1 measures consistency "across shards"; sentence 2 measures drift "between replicas." That's an unnamed scope change — the paragraph never says whether a shard's replicas are the unit the check runs over, or whether "shard" and "replica" are being used as loose synonyms here. Because the relation isn't named, sentence 2 reads as sentence 1 restated under a new noun rather than a step that answers the question sentence 1 raises (consistent *how*, checked at what granularity).

Concrete rewrite:
Ask author: (1) What does the head check actually compare to call two heads a match? (2) What is an "editorial-row layout" — row field order, schema, something else? (3) Is a "replica" one copy of a shard, so the check runs per-shard across that shard's replicas — or are "shard" and "replica" the same unit under two names here?
Fallback if that can't be resolved before publishing — drop the unsupported precision and keep only what the paragraph itself establishes:
"The indexer checks the head before each merge, so row layouts stay consistent across shards. Because that check runs before the merge, drift between replicas surfaces there instead of at read time."
This keeps the one mechanism the source actually earns (checking before merge catches drift before read time) and cuts "exact" and "editorial," which supplied the look of precision without a referent.

Rewrite check: No rule-of-three, no X-not-Y / negative parallelism, no em-dash antithesis, no avoid-by-default phrases, no prestige adjectives, no decorative closer. The fallback doesn't invent a comparison mechanism, a layout definition, or a shard/replica relationship — it only removes the two unsupported modifiers and keeps the terms the source already used. Passes self-detectors.

Remembered line: "Because the check happens at the head, drift between replicas surfaces during the merge rather than at read time." Keep this one close to as-is in any revision — it's the one place the paragraph names a real, checkable tradeoff (caught at merge vs. caught at read) instead of just asserting consistency.
