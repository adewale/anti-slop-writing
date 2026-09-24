Verdict: revise

Slop tells: None of the standard markers. No banned phrases, no prestige vocabulary, no copula displacement ("serves as" / "represents" etc.), no hedged symmetry, no decorative em-dashes, no rule-of-three, no "Not X. Y." rhythm. The paragraph already has what the doctrine asks for instead: a named actor ("the indexer"), a named mechanism ("exact-head checks"), and a subordinating "Because" clause rather than two same-weight clauses set side by side.

Specificity missing: Sentence 1 scopes consistency "across shards"; sentence 2 scopes drift "between replicas." The paragraph never states how those units relate — whether each shard is backed by several replicas and it's their disagreement that sentence 1's "consistent" depends on, or whether "shard" and "replica" name the same thing here. A reader who doesn't already know this system's replication layout has to guess the mapping.

Inflated claim: "so editorial-row layouts stay consistent across shards" claims a maintained state. What the rest of the paragraph actually earns is narrower: the check makes drift "surface ... during the merge rather than at read time" — that's earlier detection, not demonstrated prevention. "Surfaces" is a visibility verb; the paragraph never says a failed check blocks the merge or fixes the divergent replica, so "stay consistent" asserts the outcome of a step the paragraph doesn't describe.

Flow break: None in the connective logic — "Because the check happens at the head" correctly subordinates to sentence 1's mechanism instead of standing beside it as an unrelated second claim. The seam is the shard/replica swap noted above, not the causal link.

Concrete rewrite: "The indexer runs exact-head checks before each merge, so replica drift in editorial-row layouts surfaces at merge time instead of at read time." This replaces "stay consistent" (unproven by what follows) with "surfaces" (the verb the source's own second sentence already earns), and standardizes on "replica," the unit the explanation actually measures, instead of switching to "shard" without a bridge.

Two facts would let the original's stronger phrasing stand. Ask author: (1) does a failed exact-head check block the merge, or only flag the drift while the merge proceeds? (2) is a shard here backed by multiple replicas, so "across shards" and "between replicas" describe the same drift at two grain sizes? Fallback with no answer: use the rewrite above — it claims only earlier detection of replica-level drift, not a guaranteed shard-level state.

Rewrite check: No rule-of-three, no X-not-Y/negative parallelism, no em-dash antithesis, no avoid-by-default phrases, no prestige adjectives, no decorative closure. No invented facts — every term (indexer, exact-head checks, merge, replica, editorial-row layouts, read time) is already in the source. Passes self-detectors.

Remembered line: Drift surfaces at merge time, not read time — the one load-bearing, checkable fact in the paragraph. Everything else is framing around it.
