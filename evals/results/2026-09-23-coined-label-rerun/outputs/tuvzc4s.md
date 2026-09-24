Paragraph under review:

"The billing job runs ledger-fold passes after each import, so invoice-drift totals stay accurate. Each pass finishes before the nightly export starts, and the export reads only folded rows."

Verdict: keep

Slop tells: None. The paragraph names a specific actor (the billing job), a specific mechanism (ledger-fold passes run after each import), and two specific guarantees (the pass finishes before the nightly export starts; the export reads only folded rows). None of the avoid-by-default phrases or high-risk words appear. Verbs are plain and concrete (runs, stay, finishes, starts, reads), with no copula displacement such as "serves as" or "represents." No hedged symmetry, no decorative em-dash cluster, no rule-of-three, no "Not X. Y." parallelism, no decorative closer.

Specificity missing: None. "Stay accurate" is not left as an unsupported claim; it is tied directly to the fold-pass mechanism named in the same sentence. "Reads only folded rows" states the export's exact scope rather than gesturing at "clean" or "consistent" data.

Inflated claim: None. "Accurate" is a plain, checkable property earned by a stated cause, not a significance word asserted without mechanism.

Flow break: None. Sentence 1 states the practice and its result. Sentence 2 answers the question sentence 1 raises, namely what stops the export from reading rows mid-fold or before folding is done, with two concrete guarantees: ordering (the pass finishes before the export starts) and scope (the export reads only folded rows). The "and" joining those guarantees is earned, not a stand-in for an unstated relation: ordering prevents a race between fold and export, while scope is an independent filter on what the export reads; the filter is not caused by the timing, they are separate, cooperating mechanisms. Rewriting this as "because each pass finishes before the export starts, the export reads only folded rows" would invent a causal link the source does not make. Parataxis is the right choice here, not a fix-it target.

Concrete rewrite: Not needed; the original stands.

Rewrite check: No concrete rewrite was produced, since the verdict is keep. Checked the original paragraph itself against the same list: no rule-of-three, no negative parallelism, no em-dash antithesis, no avoid-by-default phrases, no prestige adjectives, no decorative closure, no invented facts. Passes self-detectors.

Remembered line: "the export reads only folded rows." That is the concrete filter a reader carries away, more specific than the paragraph's own opening claim that totals "stay accurate."
