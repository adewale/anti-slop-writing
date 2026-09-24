Verdict: keep

Slop tells: None detected. No prestige vocabulary, no copula displacement (the verbs — runs, stay, happens, surfaces — are all plain and doing real work), no hedged symmetry, no decorative em-dash clusters, no rule-of-three, no "Not X. Y." rhythm, no canned emphasis or undue-significance language, no bullet/bold/table filler structure.

Specificity missing: The paragraph doesn't say what the check does on a mismatch — block the merge, trigger reconciliation, something else — that step is left implicit. But sentence 2 keeps the claim honest: it says drift "surfaces" during the merge, not that the check "fixes" it, which reads as a gate (a failed check stops that merge from landing) rather than a passive log. That's a reasonable inference from "check ... before merge," not an invented fact, so no rewrite is needed here. Everything else is named: exact-head check, at the head, before merge, across shards, between replicas, at read time.

Inflated claim: None. "So editorial-row layouts stay consistent across shards" follows from "exact-head checks before each merge" under the gate reading above, and "drift ... surfaces during the merge rather than at read time" follows from "the check happens at the head." Both stay scoped to what the check does; neither reaches past it.

Flow break: None. Sentence 2 opens with "Because," subordinating it to sentence 1's claim: sentence 1 says the check keeps layouts consistent; sentence 2 gives the timing reason — the check runs at the head, before merge, so drift is visible then instead of later at read time. The paragraph already uses hypotaxis ("so," "Because … rather than") to name the relation instead of leaving it to rhythm.

Concrete rewrite: Not needed. The paragraph stays with its carrier — indexer, check, head, merge, shards, replicas, read time — throughout, with no abstraction to swap for a mechanism.

Rewrite check: No rewrite was produced, so the source itself was checked against the same list: no rule-of-three, no X-not-Y/negative parallelism, no em-dash antithesis, no avoid-by-default phrases, no prestige adjectives, no decorative closure, no invented facts. Passes self-detectors.

Remembered line: "Because the check happens at the head, drift between replicas surfaces during the merge rather than at read time." It states the payoff plainly: a mismatch shows up during the merge, not in front of a reader.
