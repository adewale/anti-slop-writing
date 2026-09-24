# Critique

Paragraph reviewed:

> The billing job runs ledger-fold passes after each import, so invoice-drift totals stay accurate. Each pass finishes before the nightly export starts, and the export reads only folded rows.

Verdict: keep

Slop tells: None found. Checked against the source-backed detectors: no undue-significance language, no canned emphasis, no rule-of-three, no negative parallelism ("Not X. Y."), no em-dash cadence (no dashes at all), no copula displacement ("serves as," "stands as," "features," "marks," "represents" — the verbs here are plain: runs, stay, finishes, starts, reads), no hedged symmetry ("Whether X or Y," "While X, Y is also important"), no bullet/bold/table fake structure, no banned avoid-by-default phrases, no watch-list words (delve, realm, tapestry, testament, pivotal, crucial, underscore, seamless, robust, etc.).

Specificity missing: None. Every actor and mechanism is named rather than gestured at: the billing job, the trigger ("after each import"), the operation ("ledger-fold passes"), the object of the accuracy claim ("invoice-drift totals"), and the two facts that back the export's safety ("finishes before the nightly export starts," "reads only folded rows"). Nothing here is a vague "it" or an unnamed process.

Inflated claim: None. "stay accurate" is a bounded, modest claim — not "ensures," "guarantees," or "seamlessly" — and it is earned by mechanism, not asserted on cadence. Sentence 1 gives the reconciliation mechanism (fold runs after every import, not just nightly). Sentence 2 gives the read-side guarantee (temporal ordering plus a row-level filter to "folded" rows), which matches the scope of the claim: the paragraph never overreaches into "real-time," "complete," or "guaranteed," so the claim and the evidence are the same size.

Flow break: None. Sentence 2 answers the question sentence 1 raises rather than sitting beside it: if fold passes run after each import, what stops the nightly export from reading a row mid-fold? The second sentence resolves that with two concrete, complementary facts (pass-before-export ordering, folded-only read scope) instead of restating the first sentence or drifting topic. That is a dependency relation, not a list.

Concrete rewrite: Not applicable — no rewrite needed; the original wording stands.

Rewrite check: N/A. No rewrite was produced because the verdict is keep; there is nothing to run the self-detectors against.

Remembered line: "the export reads only folded rows" — the specific, inspectable safeguard a reader would carry away: a filter on what gets read, not just a promise about when it runs.
