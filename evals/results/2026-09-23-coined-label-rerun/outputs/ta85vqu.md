**Verdict:** revise

**Slop tells:**
Coined compound label — "exact-head checks" (echoed as "the check happens at the head") names a check the paragraph never defines. "Exact" supplies the texture of precision without stating what's compared (content? a hash? a row count? a timestamp/version?); "head" is never anchored to a concrete referent. This isn't a domain-standard term like "two-phase commit," so it doesn't clear the false-positive bar on its own.

No other tells: the paragraph already uses hypotaxis correctly ("so," "Because"), and has no banned avoid-by-default phrases, no watch-list words, no copula displacement, no em-dash cadence, no rule-of-three, no hedged symmetry, no decorative closure.

**Specificity missing:**
- What makes the match "exact" (byte-for-byte content equality, a content hash, a row count, a version/timestamp field) is unstated.
- What "head" denotes structurally (a specific row, a version pointer, a commit) is unstated.
- The paragraph names "shards" in sentence 1 and "replicas" in sentence 2 without confirming whether those are the same entities or the check spans both.

**Inflated claim:** None. The claim itself is bounded and falsifiable (drift is caught at merge time rather than read time); nothing here oversells importance.

**Flow break:** Sentence 2's "Because the check happens at the head" reuses "head" from sentence 1 to explain why drift surfaces at merge rather than read time, but sentence 1 already supplied the operative timing fact ("before each merge"). The connective reads as causal but leans on the same undefined term instead of the timing fact already on the table, so it doesn't add a new, checkable link.

**Concrete rewrite:**
"The indexer runs head checks before each merge, so editorial-row layouts stay consistent across shards. Because that check runs before the merge, drift between replicas surfaces there rather than at read time."

If "exact" is load-bearing — distinguishing this from a sampling or fuzzy check elsewhere — name the comparison instead of restoring the adjective: "checks that the head row matches across replicas by [content hash / full equality / row count]." The bracketed choice is the author's fact to supply, not a guess to make here.

**Rewrite check:** No rule-of-three. No X-not-Y / negative-parallelism template (the "rather than" clause is a plain comparative, not the "Not X. Y." pattern, and both sides — merge-time surfacing, read-time as the named alternative — come from the source). No em-dash antithesis. No avoid-by-default phrases. No prestige adjectives. No decorative closure. No invented facts: every element (head, before the merge, drift between replicas, editorial-row layouts, across shards) is carried over from the source rather than added. Passes self-detectors.

**Remembered line:** The check runs before the merge, so drift shows up there instead of waiting until someone reads the data.
