Paragraph reviewed:

> The billing job runs ledger-fold passes after each import, so invoice-drift totals stay accurate. Each pass finishes before the nightly export starts, and the export reads only folded rows.

Verdict: keep

Slop tells: None. Checked against the source-backed detectors: no undue significance language, no canned emphasis, no rule-of-three, no negative parallelism ("Not X. Y."), no em-dashes, no bullet/bold/table fake structure. Verbs are "runs," "finishes," "reads," "starts" — plain, none displaced into "serves as"/"stands as"/"represents." No hedged symmetry, no decorative antithesis, no avoid-by-default phrases or watch-list words.

Specificity missing: None. Both sentences carry named objects instead of abstractions: "ledger-fold passes," "invoice-drift totals," "nightly export," "folded rows." The mechanism is stated directly (fold-then-export ordering, export restricted to folded rows), not gestured at with a noun-heavy stand-in.

Inflated claim: None. "invoice-drift totals stay accurate" is a bounded, checkable claim, and it's earned inside the same paragraph rather than merely asserted: sentence two supplies the ordering guarantee (pass finishes before export starts) and the read restriction (export reads only folded rows) that make the claim hold.

Flow break: None. Sentence one raises the question a careful reader asks next — what stops the export from reading a row mid-fold? Sentence two answers it with a dependency relation, named through connectives rather than implied by rhythm: "so" for cause, "before" for the ordering guarantee, "and" for the added read restriction. The paragraph answers its own next question instead of placing two facts side by side.

Concrete rewrite: Not needed. The paragraph already names the actor (billing job), the mechanism (ledger-fold pass ordered before export), and the boundary (export reads only folded rows) — the three things a rewrite would otherwise exist to recover.

Rewrite check: No rewrite was produced (verdict: keep). Re-running the same detector list against the source paragraph itself turns up no hits — passes self-detectors.

Remembered line: "the export reads only folded rows" — the specific, checkable guarantee the paragraph's accuracy claim actually depends on.
