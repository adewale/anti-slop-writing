Paragraph reviewed:
> The indexer runs exact-head checks before each merge, so editorial-row layouts stay consistent across shards. Because the check happens at the head, drift between replicas surfaces during the merge rather than at read time.

Verdict: keep

Slop tells: None. Checked against the source-backed detectors: no banned avoid-by-default phrases, no watch-list words (robust, seamless, crucial, underscore, etc.), no copula displacement ("serves as" / "stands as" / "features" / "marks" / "represents" — the verbs here are "runs," "stay," "happens," "surfaces," each doing concrete work), no hedged symmetry ("Whether X or Y," "While X, Y is also important"), no em-dash cadence (no dashes present), no rule-of-three, no "Not X. Y." parataxis, no bullet/bold-header fake structure.

Specificity missing: None. The paragraph names the mechanism (exact-head checks), its timing (before each merge, at the head), its scope (editorial-row layouts, across shards), and the consequence of that timing (drift surfaces during the merge rather than at read time). That is the sharp-detail standard the skill asks for in place of inflated-significance language — nothing here asserts importance without a mechanism behind it.

Inflated claim: None. "stay consistent across shards" is scoped to the named mechanism (the check itself), not asserted as a free-floating virtue. Nothing calls the system "robust" or "critical" and leans on the adjective instead of the mechanism doing the work.

Flow break: None. Sentence two is hypotactic, not paratactic: "Because the check happens at the head, drift...surfaces during the merge rather than at read time" subordinates the timing explanation to sentence one's claim and answers the question sentence one raises — why does checking at the head matter? Sentence one states its own causal relation explicitly via "so" rather than leaving it to be inferred from bare juxtaposition. The two sentences also differ in shape (subject-led vs. because-led), so nothing here reads as symmetrical or templated.

Concrete rewrite: Not needed. No slop tell was flagged to fix, and per the skill's false-positive-restraint rule, a synonym-only or unnecessary rewrite is not owed just because the prose is technical and dense — here the mechanism (exact-head check, timed at the head, before merge) earns the consistency claim it makes.

Rewrite check: N/A — no rewrite was produced (verdict is keep), so there is no candidate text to run the self-detectors against.

Remembered line: "Because the check happens at the head, drift between replicas surfaces during the merge rather than at read time." This is the paragraph's actual payoff — early detection at merge time instead of at read time — stated as a named mechanism rather than an inflated claim.
