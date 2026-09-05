## Trial 5

Verdict: keep

Slop tells: None found. Checked against the full list — superficial analysis, undue significance language, canned emphasis, negative parallelism, rule-of-three, formulaic dashes, table/bold-as-fake-structure — and none apply. No avoid-by-default phrase and no watch-list word appears anywhere in the passage. No copula displacement: "runs," "stay," "happens," and "surfaces" are all plain verbs doing real locating/enumerating work, not "serves as/stands as/features/marks/represents" standing in for "is." No hedged symmetry, no em-dash cadence (there are no dashes at all), no outline-conclusion template.

Specificity missing: None. "The indexer," "exact-head checks," "editorial-row layouts," "shards," and "replicas" are all named components of a specific system, not vague placeholders standing in for unexplained work. The claim is scoped to one mechanism (a check that runs before merge) and one measurable consequence (where drift becomes visible), which is exactly the "sharp detail" the doctrine asks for over inflated importance.

Inflated claim: None. Nothing here asserts significance — no "this is critical," no "this matters because." The paragraph states what happens and why, and stops.

Flow break: None. The second sentence opens with "Because," subordinating the mechanism (check runs at the head) to its consequence (drift surfaces at merge, not at read) instead of placing two independent clauses side by side and leaving the reader to infer the link. That answers the question the first sentence raises — why does checking at the head keep layouts consistent — rather than just sitting next to it.

Concrete rewrite: Not needed — the passage already meets the bar.

Rewrite check: N/A — no rewrite offered; verdict is keep.

Remembered line: "Drift between replicas surfaces during the merge rather than at read time" — a specific, falsifiable claim about when a failure becomes visible, not a generic close.

## Trial 6

Verdict: keep

Slop tells: Ran the two tests this paragraph is most likely to trip. First, the syntax-relation test on "Because the check happens at the head, drift... surfaces...": restated in plain prose, the connective holds without invention — the check runs pre-merge, so whatever it catches is caught pre-merge, which is a direct entailment, not a borrowed rhythm standing in for a relation. Second, the staccato-contrast test on "during the merge rather than at read time": one side (merge-time surfacing) is directly evidenced by sentence one's "before each merge"; the other side (read-time) is not spelled out, but it names the only other point in a two-stage merge-then-read pipeline where the same drift could first become observable, so it reads as scope-naming rather than a rhetorical leap. Neither test turns up cadence carrying a claim the prose hasn't earned. No banned phrases, watch-list words, or displaced copulas either.

Specificity missing: "Stay consistent" is the one phrase that could be read as soft, but the false-positive-restraint rule applies directly here: the same sentence supplies the mechanism that earns it ("exact-head checks... before each merge"), so the claim is tied to a stated check rather than floating free the way "seamless" or "robust" would without one.

Inflated claim: None. Every clause is an operational statement tied to the named check, not an unearned claim of importance.

Flow break: None — "Because" makes the dependency explicit between the two sentences.

Concrete rewrite: Not needed — the passage already meets the bar.

Rewrite check: N/A — no rewrite offered; verdict is keep.

Remembered line: "The check happens at the head" — the four words the rest of the paragraph's claim depends on.

## Trial 7

Verdict: ask-author

Slop tells: No banned phrases, no watch-list words, no copula displacement, no em-dash cadence, no rule-of-three. On surface texture this is clean, plain-verb prose.

Specificity missing: Two terms carry the paragraph's whole claim without being cashed out, and this excerpt is all the source I have to work with. "Exact-head checks" implies a precise comparison, but the paragraph never says what property it compares — a hash, a sequence number, a timestamp — so I can't tell what would count as a mismatch. And "stay consistent across shards" never says consistent in what respect: same row order, same row count, same content. Per the doctrine, ask-author is the right move exactly when a fix would need a fact — here, a named mechanism — that the source paragraph in front of me doesn't supply, whether or not it's defined somewhere else in a longer document I haven't seen.

Inflated claim: Borderline. "Stay consistent" is presented as a guarantee without naming the property it guarantees, which risks reading as reassurance rather than a claim a reader could check.

Flow break: None — the two sentences connect cleanly through "Because."

Concrete rewrite: Ask author: what does the exact-head check actually compare (hash of the head revision, sequence number, something else), and what does "consistent" mean for editorial-row layouts — row order, row count, or content match? Naming either would turn "stay consistent" from an assurance into a checkable claim. Fallback if those aren't available: leave "exact-head checks" as is (it names a mechanism even without the comparison detail) and cut "stay consistent" down to whatever single property the check verifies, rather than asserting consistency in general.

Rewrite check: The ask-author question names what to ask instead of guessing a mechanism, and the fallback narrows an existing claim instead of inventing a new one. No rule-of-three, X-not-Y, em-dash antithesis, banned phrase, prestige adjective, or decorative closer appears in either. Passes self-detectors.

Remembered line: "Exact-head checks before each merge" — precise enough to anchor the paragraph once the comparison it names is spelled out.

## Trial 8

Verdict: revise

Slop tells: No banned phrases, no watch-list words, no copula displacement, no hedged symmetry. The one thing that reads as cadence doing work evidence hasn't done yet is the closing contrast, "during the merge rather than at read time" — applying the staccato-contrast test.

Specificity missing: Sentence one evidences the merge-time half of that contrast: the check runs "before each merge," so anything it catches is caught there. Nothing in the paragraph evidences the read-time half — what a reader would actually see at read time, or why read time is the alternative worth naming at all. That is the shape of a compressed antithesis: one side shown, the other supplied by the "rather than" construction alone rather than by prior sentences.

Inflated claim: Not prestige-inflated, but the implicit claim riding on the contrast — that absent this check, drift would instead surface at read time — is asserted through word order rather than stated and supported.

Flow break: None between the two sentences; "Because the check happens at the head" correctly answers why this happens at merge. The break is internal to the second sentence, between its supported clause and its unsupported "rather than" clause.

Concrete rewrite: "The indexer runs exact-head checks before each merge, so editorial-row layouts stay consistent across shards. Because the check happens at the head, drift between replicas surfaces during the merge." (Cut the unevidenced contrast rather than inventing what a read-time symptom would look like.)

Rewrite check: The rewrite adds nothing — no rule-of-three, no X-not-Y, no em-dash antithesis, no banned phrase, no prestige adjective, no decorative closer, no invented fact. It only removes the clause the paragraph doesn't back up. Passes self-detectors.

Remembered line: "Drift between replicas surfaces during the merge" — the half of the closing claim the paragraph actually earns.
