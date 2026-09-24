Reviewing:

> The billing job runs ledger-fold passes after each import, so invoice-drift totals stay accurate. Each pass finishes before the nightly export starts, and the export reads only folded rows.

Verdict: ask-author

Slop tells:
- Coined compound label, "ledger-fold": named but never defined. The only thing offered as support is "folded rows" in sentence 2, which reuses the same undefined word instead of saying what a fold pass does to a row.
- Coined compound label, "invoice-drift": named but never defined. Nothing says what causes it, how it's measured, or what a non-drifted total looks like.
- Parataxis hiding a dependency: sentence 2 joins "each pass finishes before the nightly export starts" and "the export reads only folded rows" with "and," as if these were two separate facts. They aren't — the first is the reason the second is guaranteed. Coordinating them with "and" flattens a causal relation into a list.

Specificity missing:
- What operation a fold pass performs on a row (merges duplicate line items? recomputes a running balance? applies a late adjustment?).
- What invoice-drift is and how "accurate" would be checked against it.
- Whether "each pass finishes before the nightly export starts" is an enforced guarantee (a lock, a dependency check, a scheduler constraint) or just the current schedule's usual behavior.

Inflated claim:
"so invoice-drift totals stay accurate" is a correctness claim resting on two undefined terms. The paragraph supplies a sequencing mechanism (fold runs after import, finishes before export, export reads only fold output) but not a correctness mechanism (why folding removes drift). Checked against the false-positive restraint test: the supporting phrase "folded rows" doesn't resolve what folding does — it repeats the term. It relocates the gap instead of closing it.

Flow break:
Sentence 1 asserts the accuracy claim. Sentence 2 should supply the mechanism that earns it, but instead supplies two ordering facts joined by "and," so the paragraph ends on a coordination where a dependency was needed.

Concrete rewrite:
Ask author: what does a ledger-fold pass change on a row — merge duplicate line items, recompute a running balance, apply a late adjustment, something else? And what counts as invoice-drift here — a mismatch between imported and ledger totals, double-counted entries, a timing lag between import and fold? Also confirm whether fold-before-export is an enforced ordering (lock, dependency check) or just the current schedule.

Fallback (no invented facts; cuts the unearned claim and fixes the coordination):
"The billing job runs ledger-fold passes after each import. Because each pass finishes before the nightly export starts, the export reads only folded rows."

Rewrite check: The fallback has no rule-of-three, no X-not-Y construction, no em-dash antithesis, none of the avoid-by-default phrases, no prestige adjectives, and no decorative closer. It doesn't assert what folding does or what drift is, so it invents nothing. Passes self-detectors.

Remembered line:
The checkable part of this paragraph is the ordering guarantee: fold finishes before export starts, so export never sees an unfolded row. "Accurate" stays an open claim until the paragraph says what a fold pass changes and what counts as drift.
