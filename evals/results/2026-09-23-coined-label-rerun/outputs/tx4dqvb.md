Paragraph reviewed:

```txt
The billing job runs ledger-fold passes after each import, so invoice-drift totals stay accurate. Each pass finishes before the nightly export starts, and the export reads only folded rows.
```

Verdict: keep

Slop tells: None. Nothing from the avoid-by-default phrase list or the high-risk word list appears. The verbs are plain and concrete (runs, finishes, starts, reads) — no copula displacement ("serves as," "represents," etc.), no hedged symmetry ("whether X or Y"), no em-dash cadence, no rule-of-three, no negative parallelism, and no unearned antithesis.

Specificity missing: None. The actor is named (the billing job), the mechanism is named (ledger-fold passes), the trigger is named (after each import), and the metric is named (invoice-drift totals). Nothing hides behind "the system" or an unnamed process.

Inflated claim: None. "Stay accurate" is a bounded, checkable claim wired to its mechanism by "so," not dressed up with importance language ("critical," "essential," "seamless").

Flow break: None at the sentence-to-sentence level — sentence 2 supplies the concrete mechanism that earns sentence 1's claim (claim, then evidence: a level-of-detail relation), rather than just restating it. One small internal gap: the two clauses of sentence 2 are joined with a bare "and," so a reader can't immediately tell whether "reads only folded rows" is a second, independent safeguard (for example, against a late import that lands after the last scheduled pass but before the export starts) or just a restatement of the ordering guarantee in clause 1. It reads as the former on inspection, but the paragraph doesn't say so.

Concrete rewrite: Not needed — the paragraph already meets the bar: named actor, named mechanism, a causal connective instead of asserted importance, and an ending on the most checkable detail rather than a generic wrap-up. If the redundancy in sentence 2 is worth closing, one option — to confirm with the author rather than assume — is: "...and the export reads only folded rows, so a row from an import that lands after the last pass still can't reach the export unfolded." Use only if that is in fact the case being guarded against; otherwise drop it.

Rewrite check: No text was changed, since the verdict is keep. The one optional sentence above is offered conditionally, not asserted as fact, so as written it introduces no invented fact; asserting it outright without confirming the scenario with the author would. It contains no rule-of-three, no X-not-Y, no em-dash antithesis, no banned phrase, no prestige adjective, and no decorative closer — passes self-detectors.

Remembered line: "the export reads only folded rows" — the most specific, falsifiable detail in the paragraph, and the one a reader could go check directly against the export query.
