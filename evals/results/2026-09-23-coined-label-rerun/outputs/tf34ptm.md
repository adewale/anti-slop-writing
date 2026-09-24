Paragraph reviewed:

> The billing job runs ledger-fold passes after each import, so invoice-drift totals stay accurate. Each pass finishes before the nightly export starts, and the export reads only folded rows.

Verdict: keep

Slop tells: None found. No banned phrase from the avoid-by-default list, no rule-of-three, no negative parallelism ("Not X. Y."), no decorative em-dash, no hedged symmetry ("Whether you're X or Y"), no displaced copula ("serves as," "represents"). The verbs are plain and load-bearing (runs, finishes, reads). No generic opener or closer.

Specificity missing: None. Every claim has a named carrier: the actor (the billing job), the mechanism (ledger-fold passes, run after each import), the timing guarantee (each pass finishes before the nightly export starts), and the read boundary (the export reads only folded rows).

Inflated claim: "so invoice-drift totals stay accurate" reads like an unearned significance claim on first pass, but the next sentence supplies the mechanism that backs it: fold passes complete before the export runs, and the export is restricted to folded rows, so it cannot see pre-fold state. That is a concrete boundary condition, not a borrowed rhetorical pattern. Per the false-positive restraint, this is earned — keep it as written.

Flow break: None. The two sentences are in a dependency relation: sentence 1 states the accuracy claim, sentence 2 supplies the ordering and read-boundary that make it true. "So" and "and" name that relation instead of leaving it implicit.

Concrete rewrite: Not needed. The paragraph already names its actor, mechanism, and boundary condition instead of asserting importance.

Rewrite check: No concrete rewrite was produced — the verdict is keep, so there is nothing to check for self-detectors.

Remembered line: "the export reads only folded rows" — the clause that turns the accuracy claim into a boundary a reader could go verify in the code.
