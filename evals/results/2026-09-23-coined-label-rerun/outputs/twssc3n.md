Paragraph reviewed:

> The billing job runs ledger-fold passes after each import, so invoice-drift totals stay accurate. Each pass finishes before the nightly export starts, and the export reads only folded rows.

Verdict: ask-author

Slop tells: None of the standard tells apply: no banned phrases, no prestige adjectives, no rule-of-three, no "Not X. Y." parallelism, no copula displacement ("serves as"/"represents"), no hedged symmetry, no decorative em-dashes, no outline-shaped conclusion. The one real issue is structural: sentence 2 joins two clauses with "and," and that coordination hides a relation instead of naming it (the parataxis "unstated relation" failure mode).

Specificity missing: The paragraph names an actor (the billing job), a mechanism (ledger-fold passes), a trigger (after each import), and an artifact (folded rows), which is genuinely concrete. What it doesn't name is whether "the export reads only folded rows" is an enforced filter in the export query, independent of timing, or just the state that necessarily exists once a pass finishes before export starts. The paragraph never says which.

Inflated claim: "so invoice-drift totals stay accurate" is stated as an unconditional guarantee. It holds for the case where every pass finishes on schedule, but the paragraph never says what happens if a pass runs long: does the export then read unfolded rows and produce a wrong total, or does a filter exclude them first. Until that's answered, "stay accurate" claims more than the two supporting facts prove for the failure case.

Flow break: "Each pass finishes before the nightly export starts, and the export reads only folded rows" reads as two side-by-side facts. A reader checking the accuracy claim in sentence 1 needs to know which one is doing the work: an independent safeguard that protects the total even if a pass runs late, or a restatement of what the first clause already guarantees, with no protection if a pass runs late. The sentence doesn't say, and the two readings produce different reliability stories.

Concrete rewrite: Ask author: is "reads only folded rows" an explicit filter or status check in the export query, or just the state produced by the timing in the first clause? Fallback: keep the sentence as written until confirmed; inventing an answer would misstate the guarantee. Once confirmed, add the missing clause: "...and, even if a pass runs long, the export's row filter excludes anything not yet folded" for an independent filter, or "...so by the time it runs, every row it can see is already folded" for a consequence of timing only.

Rewrite check: The ask-author question and both fallback clauses were run against the same detectors as the source. Result: no rule-of-three, no X-not-Y/negative parallelism, no em-dash antithesis, no banned avoid-by-default phrases, no prestige adjectives, no decorative closing line, no invented fact (both fallback clauses stay conditional on what the author confirms rather than asserting one mechanism). Passes self-detectors.

Remembered line: "The export reads only folded rows." Keep that detail in any rewrite; whether it's an enforced guarantee or a description of the lucky case is the open question, and that's what the author should settle.
