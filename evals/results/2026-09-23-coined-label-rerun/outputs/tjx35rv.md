Paragraph reviewed:
"The indexer runs exact-head checks before each merge, so editorial-row layouts stay consistent across shards. Because the check happens at the head, drift between replicas surfaces during the merge rather than at read time."

Verdict: ask-author

Slop tells:
- Coined compound labels — "exact-head checks" and "editorial-row layouts" are hyphenated noun phrases naming a check and an artifact that the paragraph never defines. Neither reads as settled domain shorthand the way "dead-letter queue" or "two-phase commit" would; each requires the reader to already know this specific system.
- Nothing else fires. No banned phrases, no inflated-significance words, no rule-of-three, no hedged symmetry, no em-dashes to audit, no negative parallelism. Both sentences state their relation with a connective ("so," "Because") instead of implying it through rhythm, so this isn't staccato parataxis dressed as logic.

Specificity missing:
- "Head" is never anchored to a structure. "Exact-head checks" and "the check happens at the head" both lean on the word, but the paragraph doesn't say head of what — a shard's log, a replica's latest commit, a merge queue — or what gets compared there: a checksum, a row count, a specific field.
- "Editorial-row layouts" never says what a layout consists of (column set, field order, schema version) or what makes a row "editorial" rather than any other kind.
- Scope shift between the two sentences: sentence 1 claims consistency "across shards," sentence 2 explains a check for "drift between replicas." A shard is a data partition; a replica is a copy of one. The paragraph doesn't establish that catching replica drift is what actually keeps layouts consistent across different shards, as opposed to just across copies of the same shard.

Inflated claim: None. The causal claims are sized to the mechanism named — check before merge implies earlier consistency, check at the head implies earlier detection — and don't borrow significance language to carry weight they haven't earned.

Flow break: Mild, and internal to the paragraph rather than between paragraphs. Sentence 2 says when drift becomes visible ("during the merge rather than at read time") but stops before saying what the merge does once drift is caught — block, retry, auto-repair, alert. That may be covered in a paragraph not shown here, so this is a note rather than a defect.

Concrete rewrite:
Ask author: what does the exact-head check compare, and the head of what — a shard's log position, a replica's latest commit, a merge-queue entry?
Ask author: what fields make up an "editorial-row layout," and does checking replica drift inside a shard actually guarantee the cross-shard consistency claimed in sentence 1, or is that guaranteed some other way (for example, a schema fixed at shard creation)?
Fallback if those facts aren't available: leave the paragraph as written for readers already working in this codebase — its causal structure and hypotaxis are sound — but for a wider or onboarding audience, add one clause per term defining it in place instead of letting the compound noun stand in for the definition.

Rewrite check: passes self-detectors. No rule-of-three, no X-not-Y, no em-dash antithesis, no avoid-by-default phrases, no prestige adjectives, no decorative closure. No fact was invented: both ask-author questions offer candidate options without asserting which one is correct, matching the skill's own "which coding tool? Cursor, Claude Code, Copilot, Aider, other?" pattern.

Remembered line: "drift between replicas surfaces during the merge rather than at read time." It's the sharpest, most checkable claim in the paragraph: catching inconsistency at merge time instead of serving it silently at read time is a real tradeoff, and the line will keep working once "exact-head check" is defined. It doesn't depend on that gap to land.
