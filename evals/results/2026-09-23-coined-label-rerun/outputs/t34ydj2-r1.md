Verdict: ask-author

Slop tells: Coined compound labels. "Ledger-fold passes" and "invoice-drift totals" name a process and a metric the paragraph never defines, and neither is a standard, widely-recognized domain term the way "dead-letter queue" or "two-phase commit" is. The hyphenated phrasing supplies the texture of precision while the actual referent stays out of reach.

Specificity missing: What does a ledger-fold pass actually do to ledger rows — recompute a running balance, dedupe re-imported entries, reconcile against a source system? What does "invoice-drift" measure, and drift relative to what (invoiced vs. paid amount, two ledgers, a rounding/timing artifact)? Without an answer, "folded rows" in sentence two just restates the same undefined term instead of explaining it.

Inflated claim: "So invoice-drift totals stay accurate" claims correctness, but the only support given — the pass finishes before export starts, and export reads only folded rows — proves freshness/ordering (export never reads a stale or in-flight row), not accuracy of the fold computation itself. Per the skill's own support test, a supporting phrase must be resolvable by the reader or defined in the passage; "folded rows" is neither, since "folded" just points back to the still-undefined "ledger-fold." The support relocates the gap instead of closing it, so it does not earn "accurate."

Flow break: Sentence two functions as evidence for sentence one's claim, but it quietly narrows scope from a correctness claim ("stay accurate") to an ordering/freshness guarantee ("finishes before," "reads only folded rows") without naming that narrowing. The paragraph would read cleaner if it marked the shift directly instead of letting the two properties blur together.

Concrete rewrite: Ask author: what does a ledger-fold pass compute over the ledger rows, and what does "invoice-drift" measure? Fallback (cut, no new facts invented): "The billing job runs a ledger-fold pass after each import. Each pass finishes before the nightly export starts, and the export reads only folded rows, so the export never reads a row from an in-flight import." This drops the unearned "accurate" claim and keeps only the two guarantees the paragraph actually supports.

Rewrite check: The fallback contains no rule-of-three, no X-not-Y/negative parallelism, no em-dash antithesis, none of the banned avoid-by-default phrases, no prestige adjectives, and no decorative closure. It invents no new facts — it restates only the ordering and filter the source already asserts and cuts the unsupported "accurate" claim rather than fabricating what folding does. Passes self-detectors.

Remembered line: "The export reads only folded rows" is the one claim in the paragraph that is fully concrete and checkable as written. It is also the line any author follow-up should anchor to, since defining "folded" resolves the rest of the paragraph.
