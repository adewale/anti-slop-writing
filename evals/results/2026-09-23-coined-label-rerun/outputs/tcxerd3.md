Paragraph reviewed:
"The billing job runs ledger-fold passes after each import, so invoice-drift totals stay accurate. Each pass finishes before the nightly export starts, and the export reads only folded rows."

Verdict: keep

Slop tells: None. No banned avoid-by-default phrases, no watch-list vocabulary (delve, pivotal, crucial, robust, seamless, etc.), no displaced copulas ("serves as," "represents," "features"), no hedged symmetry ("whether you're X or Y"), no decorative em-dash clusters (the paragraph has no em-dashes), no rule-of-three, no "Not X. Y." staccato, no bullet/bold/table fake structure.

Specificity missing: None that undermines the claim. The paragraph names a concrete actor (the billing job), a concrete mechanism (ledger-fold passes), a concrete trigger (after each import), a concrete ordering guarantee (finishes before the nightly export starts), and a concrete scope guarantee (export reads only folded rows). Minor, non-blocking note: it doesn't say what enforces the ordering claim, whether that's a scheduled gap, a dependency check, or a lock. That gap doesn't weaken "accurate," though, because the scope guarantee already carries the correctness burden on its own. Even if a fold pass ran long, the export would exclude those rows instead of reading a stale one.

Inflated claim: None. "Accurate" is earned, not asserted on rhythm. The same paragraph supplies the mechanism that earns the term: fold-before-export ordering plus a read filter that excludes unfolded rows. This matches the skill's own keep example, "The queue is robust because each job has an idempotency key, a retry receipt, and a dead-letter cutoff": a qualitative claim backed by named, checkable mechanisms rather than a bare intensifier.

Flow break: None. Sentence 1 states mechanism plus effect and raises the reader's next question: how is that guaranteed? Sentence 2 answers with the ordering guarantee and the read filter. That is a dependency relation, not two facts sitting side by side in a merely plausible order.

Concrete rewrite: No rewrite needed. The paragraph is kept as written:

"The billing job runs ledger-fold passes after each import, so invoice-drift totals stay accurate. Each pass finishes before the nightly export starts, and the export reads only folded rows."

Rewrite check: No rewrite was made, so this checks the kept text itself: no rule-of-three, no X-not-Y or negative parallelism, no em-dash antithesis, no banned phrases, no prestige adjectives, no decorative closer, no invented facts. Passes self-detectors.

Remembered line: The export reads only folded rows. That single filter is what keeps totals accurate regardless of how the fold-versus-export timing plays out.
