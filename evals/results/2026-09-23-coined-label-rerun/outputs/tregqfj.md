Paragraph reviewed:

```txt
The billing job runs ledger-fold passes after each import, so invoice-drift totals stay accurate. Each pass finishes before the nightly export starts, and the export reads only folded rows.
```

Verdict: keep

Slop tells: None of the default signs are present — no avoid-by-default phrase, no high-risk word, no rule-of-three, no formulaic dash, no bullet/bold fake structure, no hedged symmetry, no decorative antithesis. The verbs (`runs`, `finishes`, `reads`, `stay`) are plain, not displaced copulas. Two hyphenated compounds — `ledger-fold` and `invoice-drift` — trip the coined-compound-label detector as hypotheses, so they get tested rather than assumed guilty. `ledger-fold` is earned: the passage supplies a boundary two clauses later ("the export reads only folded rows") — a row is either folded or not, and only folded rows are read — which is a checkable condition, not a name standing in for one. `invoice-drift` is weaker support: nothing here says what it's drift *from* (a prior snapshot, the ledger, a source system). But the paragraph's claim is about pipeline timing, not about the metric's definition, so the undefined dimension doesn't prop up a claim it isn't being used to prop up. Both resolve to keep, the second on a lower bar than the first.

Specificity missing: None for the claim actually made. The paragraph names the actor (the billing job), the trigger (after each import), the ordering guarantee (each pass finishes before the nightly export starts), and the read boundary (the export reads only folded rows) — four concrete, independently checkable facts, not a hand-wave.

Inflated claim: Worth naming as a boundary rather than a defect. "Accurate" is carrying two different guarantees at once: (1) the export never reads a row mid-fold, which the ordering-plus-filter sentence proves, and (2) the fold computation itself produces the right number, which nothing in this paragraph addresses. The text earns (1). If this paragraph is ever reused in a context where (2) is the question — e.g., an incident writeup about a wrong total — "accurate" would overclaim what was actually shown here.

Flow break: None. Sentence 2 reads as elaboration of "passes" from sentence 1 (`ledger-fold passes` → `Each pass`), and there is only one plausible relation to infer: the ordering/filter detail is what operationalizes the "so ... accurate" claim. That is unlike the doctrine's bad example ("The benchmark is saturated. The model still fails in production."), where the relation is genuinely ambiguous — cause, contrast, or non sequitur. Here the antecedent is unambiguous, so leaving the connective implicit doesn't cost the reader anything.

Concrete rewrite: None required. If the author wants to close the accuracy-vs-consistency gap noted above, the smallest fix is a scope change, not new rhetoric:

```txt
The billing job runs ledger-fold passes after each import. Each pass finishes before the nightly export starts, and the export reads only folded rows, so invoice-drift totals never reflect a partially folded ledger.
```

This reuses only words already in the source (`folded`, `ledger`, `passes`, `export`) and narrows the claim to exactly what the ordering-and-filter sentence proves. Optional — not needed for the keep verdict.

Rewrite check: The optional line above contains no rule-of-three, no X-not-Y / negative parallelism, no em-dash antithesis, no avoid-by-default phrase, no prestige adjective, no decorative closer ("that was the point," "in conclusion," "overall," "ultimately"), and no invented fact — it reorders and rescopes existing content rather than adding anything new. Passes self-detectors.

Remembered line: "the export reads only folded rows" — already in the source. It is the one clause a reader could go check directly against the export query (a `WHERE folded = true` or equivalent), which is the kind of inspectable detail the doctrine wants a paragraph to leave the reader with.
