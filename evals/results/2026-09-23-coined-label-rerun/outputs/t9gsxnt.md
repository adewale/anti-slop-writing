Verdict: keep

Slop tells: None found. Both sentences use hypotaxis to state the relation directly instead of leaning on parataxis or contrast-by-rhythm — "so" ties the check to its effect, and "Because … rather than" ties the check's location to the timing consequence. No banned avoid-by-default phrases, no watch-list prestige vocabulary, no copula displacement ("runs," "happens," "surfaces" are plain, concrete verbs, not "serves as"/"represents"), no hedged symmetry ("Whether X or Y"), no em-dash cadence, no rule-of-three, no "Not X. Y." negative parallelism.

Specificity missing: None. The paragraph names an actor (the indexer), a mechanism (exact-head checks, run before each merge, positioned at the head), a scope (across shards), and a consequence (drift surfaces at merge rather than at read time). Actor, mechanism, and result are all on the page rather than gestured at.

Inflated claim: None. "Stay consistent" is not a bare significance claim — it is earned by the named mechanism (exact-head checks before each merge), the same pattern the doctrine keeps "robust" for when a queue's idempotency key, retry receipt, and dead-letter cutoff are named. Nothing here asks the reader to accept importance without a mechanism behind it.

Flow break: None. The second sentence answers the question the first raises. Sentence one says checks run "before each merge" and layouts "stay consistent"; sentence two names where the check sits ("at the head") and what that placement buys (drift is caught at merge, not read time). "Because" makes the relation explicit instead of leaving two facts to sit side by side.

Concrete rewrite: Not needed — the paragraph passes as written.

Rewrite check: No rewrite was produced (verdict is keep), so the source paragraph itself was checked against the self-detector list: rule-of-three, X-not-Y/negative parallelism, em-dash antithesis, banned avoid-by-default phrases, prestige adjectives, decorative closure, invented facts. None present. passes self-detectors

Remembered line: "Because the check happens at the head, drift between replicas surfaces during the merge rather than at read time."
