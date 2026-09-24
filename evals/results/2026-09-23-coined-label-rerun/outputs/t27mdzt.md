Verdict: keep

Slop tells: None. No banned phrases, no high-risk watch-list words, no copula displacement ("serves as" / "represents" / etc.), no hedged symmetry ("Whether X or Y"), no decorative em-dashes (none appear), no rule-of-three, no "Not X. Y." negative parallelism, no generic opening or closing.

Specificity missing: None that blocks the claim — every actor and object is named: the billing job, ledger-fold passes, invoice-drift totals, the nightly export, folded rows. Non-blocking aside: the paragraph asserts "each pass finishes before the nightly export starts" as a given fact without naming what enforces that ordering (a scheduler dependency, a lock, a cutoff window). Worth a follow-up question in a longer design doc, not a defect here.

Inflated claim: None. "stay accurate" is a plain, mechanism-tied claim, not "ensures," "guarantees," or "transformative accuracy." Sentence 1 names the mechanism (ledger-fold passes after each import); sentence 2 supplies the two guarantees, timing and read-scope, that make the claim hold instead of asserting importance and moving on.

Flow break: None. Sentence 1's claim raises the next question a careful reader asks: could the export ever see a row that hasn't been folded yet? Sentence 2 answers it directly with the two guarantees that rule it out — the pass finishes before export starts, and export reads only folded rows. That is the dependency the "so" in sentence 1 promised.

Concrete rewrite: None needed. The paragraph already runs on named mechanism and named guarantees rather than inflated significance language. A rewrite would restate the same content in different words without adding detail, judgment, or a cut.

Rewrite check: No rewrite was produced. The original was run against the same detectors used above and contains none of: rule-of-three, X-not-Y negative parallelism, em-dash antithesis, banned avoid-by-default phrases, prestige adjectives, decorative closure, or invented facts. passes self-detectors.

Remembered line: "the export reads only folded rows."
