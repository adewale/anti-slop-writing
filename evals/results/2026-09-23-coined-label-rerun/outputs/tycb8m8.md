Paragraph reviewed:

> The indexer runs exact-head checks before each merge, so editorial-row layouts stay consistent across shards. Because the check happens at the head, drift between replicas surfaces during the merge rather than at read time.

Verdict: keep

Slop tells: None found. Verbs are plain and concrete (runs, stay, happens, surfaces) — no copula displacement (serves as / stands as / features / marks / represents). No hedged symmetry, no rule-of-three, no "Not X. Y." negative parallelism, no em-dashes, no banned avoid-by-default phrases, no high-risk/prestige words (crucial, robust, seamless, etc.), no bullet/bold/table fake structure, no generic opening, no outline-shaped conclusion.

Specificity missing: None. Every noun phrase names a real mechanism or timing point rather than a placeholder abstraction: "exact-head checks," "before each merge," "editorial-row layouts," "across shards," "drift between replicas," "during the merge," "at read time."

Inflated claim: None. The paragraph makes one narrow, falsifiable timing claim (checks run pre-merge, so drift is visible at merge rather than later) instead of an importance claim like "this ensures reliability" or "this is critical." No significance language is riding on top of the mechanism.

Flow break: None. Sentence 2 opens with "Because," which names the relation back to sentence 1 (checks run "at the head," i.e., "before each merge") instead of just sitting beside it. This passes the flow-by-relation test: the paragraph states a cause relation rather than implying one through order or rhythm.

Staccato-contrast check (per the skill's instruction to read the prior sentence before classifying): "during the merge rather than at read time" is a contrast, so classify it rather than flag it on cadence alone. Side A ("during the merge") is directly evidenced by sentence 1's "before each merge." Side B ("at read time") is not a separate, unsupported claim — it's the entailed complement of the same before/after-merge timing model the paragraph already sets up: once you know the check runs at merge time, "not at read time" follows from the same fact rather than requiring independent evidence. This is earned antithesis, not compressed or decorative. Expanding it (e.g., "if the check did not run at the head, engineers would instead discover drift only when a client read the row") would restate the same entailment in more words without adding evidence, so leave it as written.

Concrete rewrite: Not needed. The paragraph already states the actor (indexer), the mechanism (exact-head check before merge), and the result (drift caught at merge, not at read) without inflation or filler.

Rewrite check: N/A — no rewrite was produced, since the source paragraph passes. Running the self-detectors against the retained original: no rule-of-three, no negative parallelism, no em-dash antithesis, no banned avoid-by-default phrases, no prestige adjectives, no decorative closure ("That was the point" / "In conclusion" / "Overall" / "Ultimately"), no invented facts. Passes self-detectors.

Remembered line: "drift between replicas surfaces during the merge rather than at read time" — where the check runs decides when the failure becomes visible.
