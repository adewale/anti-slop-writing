Paragraph under review:
> The indexer runs exact-head checks before each merge, so editorial-row layouts stay consistent across shards. Because the check happens at the head, drift between replicas surfaces during the merge rather than at read time.

Verdict: ask-author

Slop tells: None of the classic AI-writing tells fire here. No banned phrases, no prestige adjectives (delve/robust/seamless/etc.), no rule-of-three, no hedged symmetry, no decorative em-dash clusters, no displaced copulas, no outline-conclusion template. The paragraph already prefers hypotaxis over parataxis ("so"; "Because ... rather than ..."), naming a cause and a contrast instead of leaving them implied. The one real tell is a coined compound label: "exact-head checks" names a check and a comparison target ("the head") without fully resolving either. The hyphen reads as precise; the referent is still open.

Specificity missing: What does "head" denote — a single value that summarizes the whole replica or shard (so any change anywhere would change it), or literally the first/head row (so only that row's drift is visible to the check)? What makes a match "exact" — byte equality, hash equality, row count? Secondary and lower-stakes: what does "editorial-row layout" cover structurally — schema, column order, presentation formatting?

Inflated claim: "drift between replicas surfaces during the merge" is stated without qualification, but the check is explicitly scoped to "the head." That generalization is earned only if head is a full-replica summary. If head is just the first row, drift elsewhere in the replica would not be caught at merge, and the sentence claims more coverage than a head-only check can verify.

Flow break: None. Sentence 2 answers the question sentence 1 raises (why does this check keep layouts consistent) and names the relation explicitly: "during the merge" is earned by "before each merge" in sentence 1, and "rather than at read time" supplies a real structural contrast (checked pre-merge vs. not checked until a later read) inherited from the source, not a decorative one I introduced. No paragraph-to-paragraph flow to assess — only one paragraph was given.

Concrete rewrite:
Ask author: does "head" mean a single value that summarizes the whole replica (any change anywhere changes it), or literally the first/head row (only head-row drift is caught)? Separately: does "editorial-row layout" mean schema, column order, or presentation formatting?
Fallback (invents nothing; narrows the claim to what "at the head" already supports): "The indexer runs exact-head checks before each merge, so editorial-row layouts stay consistent across shards. Because the check happens at the head, drift at the head surfaces during the merge rather than at read time." If the author confirms head is a full-replica summary, the original "drift between replicas" wording is earned as written and this narrowing is unnecessary.

Rewrite check: The fallback reuses the source's own words and structure and adds nothing. No rule-of-three, no X-not-Y/negative parallelism, no em-dash antithesis, no banned avoid-by-default phrases, no prestige adjectives, no decorative closure, no invented facts — the only change is relocating "at the head" (already in the source) into the drift clause to scope the claim. It leaves "exact-head checks" and "editorial-row layout" undefined rather than inventing definitions for them, per the ask-author fallback rule. Passes self-detectors.

Remembered line: Because "head" could mean the whole replica or just its first row, the paragraph's strongest claim — that merge catches drift before read does — rests on a word the passage never defines.
