**Paragraph reviewed:**

> The indexer runs exact-head checks before each merge, so editorial-row layouts stay consistent across shards. Because the check happens at the head, drift between replicas surfaces during the merge rather than at read time.

Verdict: keep

Slop tells: None triggered. Checked against the full detector set: banned avoid-by-default phrases, high-risk words (delve, realm, tapestry, testament, pivotal, crucial, underscore, intricate, meticulous, multifaceted, foster, bolster, garner, showcase, highlight, emphasize, encompass, utilize, facilitate, transformative, groundbreaking, seamless, robust), copula displacement (serves as / stands as / features / marks / represents), hedged symmetry (whether...or / while...also), em-dash cadence, rule-of-three, and outline-shaped conclusions. None of these appear. The verbs stay plain (runs, happens, surfaces, stay). The one short contrast in the paragraph, "surfaces during the merge rather than at read time," is not decorative staccato: applying the staccato contrast test, sentence 1's "before each merge" and this sentence's own "the check happens at the head" already supply the mechanism the contrast points at, since the check running at merge time is exactly why drift shows up then. Both terms in the contrast, merge and read time, are named in the source rather than invented, so the contrast reads as earned, not compressed or decorative.

Specificity missing: Minor, non-blocking. The paragraph already names an actor (the indexer), a mechanism (exact-head checks), a timing/location (at the head, before each merge), and concrete architecture nouns (shards, replicas), which clears the bar the doctrine sets for a named mechanism rather than an abstraction. The one gap is that the paragraph doesn't say what happens once drift is found during merge: a blocked merge, a log entry, an alert, or automatic reconciliation are all consistent with the text but none is stated. That is a named-mechanism fact belonging to the author, not something to invent for a rewrite, and it does not change the verdict, since the paragraph's actual claim here is about detection timing (merge vs. read), not remediation.

Inflated claim: None. "Stay consistent across shards" is earned by the mechanism named in the same clause (exact-head checks before merge). That is the same shape as the doctrine's keep example for "robust": a term justified by an adjacent concrete mechanism rather than asserted alone.

Flow break: None. Sentence 1 states the mechanism and its result, consistency. That result raises the next question a careful reader would ask: what happens if replicas drift anyway? Sentence 2 answers exactly that question and names the relation explicitly with "because" instead of leaving it to rhythm or juxtaposition. This passes the flow-by-relation test: sentence 2 is necessary given sentence 1 rather than simply following it in a plausible order.

Concrete rewrite: Not required; the verdict is keep. An optional tightening removes the redundant second reference to "head" and folds both effects of the same mechanism, consistency and early drift detection, under one connective:

"Because the indexer's exact-head checks run before each merge, editorial-row layouts stay consistent across shards and any drift between replicas surfaces during the merge rather than at read time."

Rewrite check: The optional rewrite above contains no rule-of-three, no X-not-Y or negative parallelism, no em-dash antithesis, no banned avoid-by-default phrases, no prestige adjectives, and no decorative closure. It invents no facts: every noun carried over (indexer, exact-head checks, editorial-row layouts, shards, drift, replicas, merge, read time) comes from the source. Passes self-detectors.

Remembered line: The paragraph already ends on its concrete carrier rather than a generic thesis. "Drift between replicas surfaces during the merge rather than at read time" is specific enough to stick on its own, so the conclusion test is satisfied without further editing.
