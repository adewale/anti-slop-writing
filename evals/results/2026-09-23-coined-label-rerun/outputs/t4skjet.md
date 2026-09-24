Verdict: revise

Slop tells: None of the canonical AI-writing markers are present — no banned phrases, no copula displacement, no hedged symmetry, no em-dash cadence, no rule-of-three, no "Not X. Y." negative parallelism. The paragraph already uses hypotaxis correctly ("so" links cause to effect, "before" states a timing dependency). The real issue here is a claim/evidence-scope mismatch, not a rhetorical slop tell.

Specificity missing: The paragraph never says what a "ledger-fold pass" actually does to the numbers — recompute from the source ledger, dedupe, apply late corrections — so "accurate" has no stated standard to be accurate against. It also doesn't say whether any read path other than the nightly export (a dashboard, an API, a reconciliation job) could see a row before its fold pass finishes.

Inflated claim: "so invoice-drift totals stay accurate" asserts a general, ongoing correctness outcome. The two facts that follow it — each pass finishes before the export starts, and the export reads only folded rows — prove only that the nightly export is isolated from in-progress or not-yet-folded rows. That is a read-timing/consistency guarantee, not proof that the fold computation itself is correct. The "so" borrows more certainty than the mechanism shown actually earns.

Flow break: Sentence 1 raises the question a careful reader asks next: why does running fold passes make totals accurate? Sentence 2 answers an adjacent, narrower question instead — when, relative to folding, does the export read? It never comes back to justify the accuracy claim itself, so the paragraph reads as resolved when only the ordering half is actually shown.

Concrete rewrite: "The billing job runs a ledger-fold pass after each import, and each pass finishes before the nightly export starts. Because the export reads only folded rows, it never reads an invoice-drift total mid-fold."

Rewrite check: No rule-of-three, no X-not-Y/negative parallelism, no em-dash antithesis, no banned avoid-by-default phrases, no prestige adjectives, no decorative closure, no invented facts — the rewrite uses only the mechanism already in the source (fold pass, pass-before-export ordering, folded-rows filter) and drops the unearned "accurate" for the narrower claim the source actually supports. Passes self-detectors.

Remembered line: "The export reads only folded rows" — the one fact in the paragraph a reader can hold onto and check against the system's real behavior.
