# Critique

Paragraph reviewed:

```txt
The billing job runs ledger-fold passes after each import, so invoice-drift totals stay accurate. Each pass finishes before the nightly export starts, and the export reads only folded rows.
```

Verdict: keep

Slop tells: None found. No banned avoid-by-default phrases or watch-list words, no copula displacement ("serves as" / "stands as" / "features" / "marks" / "represents"), no hedged symmetry ("Whether you're X or Y" / "While X, Y is also important"), no decorative em-dash cadence, no rule-of-three, no "Not X. Y." negative parallelism, no decorative antithesis, no table/bold-as-fake-structure.

Specificity missing: None material. The paragraph names the actor (the billing job), the mechanism (ledger-fold passes), the trigger (after each import), the downstream consumer (the nightly export), and the two guarantees that connect them (pass-before-export ordering, and export scope limited to folded rows).

Inflated claim: "stay accurate" reads like a claim of importance on first pass, but it is earned, not inflated. Emphasis-source test: flattening the paragraph to "A fold pass runs after each import; the export starts only once that pass finishes and reads only folded rows; so the totals it reports are accurate" preserves the claim, and the residual still names an actor, a mechanism, and a boundary condition. The emphasis comes from the ordering guarantee itself, not from borrowed rhythm.

Flow break: None. Sentence 2 answers the question sentence 1 implicitly raises — how do we know the export never reads pre-fold, still-drifting rows? — with a dependency relation: a timing guarantee ("before") and a scope guarantee ("only folded rows"). Both sentences already use hypotactic connectives ("so," "before") instead of parataxis, and the relation between the two sentences is inferable without a meta-sentence, so no hinge sentence is needed; adding one would expand earned compression into bland restatement.

Concrete rewrite: Not needed. The paragraph already states actor, trigger, mechanism, and ordering guarantee in two sentences with no padding, no vague actors, and no unearned abstraction.

Rewrite check: N/A — no rewrite text was produced to audit (verdict: keep).

Remembered line: "the export reads only folded rows" — the concrete, checkable detail that makes the accuracy claim inspectable rather than asserted.
