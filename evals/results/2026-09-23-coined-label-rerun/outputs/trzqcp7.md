Verdict: ask-author

Slop tells:
- Coined compound label: "exact-head checks" never cashes out what "head" is (the newest row per shard? a version pointer? an offset compared across shards?). The second sentence repeats "at the head" but only restates the term instead of defining it — a name is not a mechanism.
- Coined compound label (softer): "editorial-row layouts" plausibly reads as "rows holding editorial content," but the passage never confirms that's a formal row type, or says what "layout" property the check actually protects (column order, byte layout, schema version).
- Compressed antithesis: "surfaces during the merge rather than at read time." The merge side is evidenced (the check runs before merge, at the head). The read-time side is asserted, not shown — nothing in the paragraph establishes what a "read" is here or why drift would otherwise appear there if the check didn't run.

Specificity missing:
- What "head" refers to structurally.
- What layout property must match across shards, and whether "editorial row" is a formal type or a description.
- What a read-time failure would concretely look like without the pre-merge check.

Inflated claim: None. The claims are scoped and mechanism-shaped ("before each merge," "at the head," "during the merge"), not evaluative or hype language.

Flow break: None between the two sentences — both consequences trace to one cause (the pre-merge head check), and the second sentence subordinates mechanism to consequence with "Because" rather than stacking two clauses side by side. The unresolved relation is internal to the second sentence's own contrast (see compressed antithesis above), not between the sentences.

Concrete rewrite: Ask author: (1) What does "head" mean in "exact-head check" — the most recent row per shard, a version pointer, or a specific offset compared across shards? (2) Is "editorial row" a formal row type, and which layout property must match across shards? Fallback if those facts aren't available: cut the undefined modifiers and the unevidenced merge/read-time contrast, keeping only the certain claim: "The indexer checks each shard's data before merging it, catching replica drift at that point."

Rewrite check: The ask-author questions and fallback contain no rule-of-three, no X-not-Y/negative parallelism, no em-dash antithesis, no banned avoid-by-default phrases, no prestige adjectives, and no decorative closure. No invented facts: the fallback drops "exact-head" and "editorial-row" rather than guessing a definition, and drops the merge/read-time comparison rather than reasserting the same unevidenced contrast under new wording. Passes self-detectors.

Remembered line: Once "head" is defined, the paragraph's own line already earns its place: "the check happens at the head, [so] drift between replicas surfaces during the merge rather than at read time" — it names a real operational choice, catching drift early instead of letting it surface later. Until then, the safer remembered line is the fallback: "The indexer checks each shard's data before merging it, catching replica drift at that point."
