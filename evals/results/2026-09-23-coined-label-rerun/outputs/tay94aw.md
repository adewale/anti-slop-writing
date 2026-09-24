## Critique

**Paragraph reviewed:**
> The billing job runs ledger-fold passes after each import, so invoice-drift totals stay accurate. Each pass finishes before the nightly export starts, and the export reads only folded rows.

**Verdict:** ask-author

**Slop tells:** Two coined compound labels carry the paragraph's whole claim without being defined in place: "ledger-fold passes" and "invoice-drift totals." The hyphen and the flat declarative tone ("so ... stay accurate") supply the texture of precision, but neither term is standard domain vocabulary the way "dead-letter queue" or "two-phase commit" is, and nothing in the paragraph says what a fold pass computes or what "drift" measures. "Folded rows" gets partial credit under false-positive restraint — the second sentence gives it a real boundary (a row status that partitions folded from not-yet-folded data, and the export's read is scoped to that boundary) — but "ledger-fold" as an operation and "invoice-drift" as a metric stay undefined coinages.

**Specificity missing:**
- What a ledger-fold pass does to the rows from an import — recomputes a running balance, merges partial/duplicate entries from a re-sent import, reconciles against a prior snapshot? The paragraph gives timing (after each import) but not the transformation.
- What "invoice-drift" measures — the gap between an invoiced amount and the ledger's recorded amount, cumulative rounding error, something else? Without this, "stay accurate" has no measurable referent.

**Inflated claim:** "so invoice-drift totals stay accurate" is presented as a direct consequence of running fold passes after each import, but the sentence that actually backs a claim up (sentence two) only supports a narrower one: that the export never reads stale or partially folded rows. That earns "the export sees consistent state," not "the fold computation produces accurate totals" — the second depends on what folding does internally, which the paragraph never shows. As written, "accurate" is asserted, not earned.

**Flow break:** Minor. "Each pass finishes before the nightly export starts, and the export reads only folded rows" coordinates a timing guarantee and a scope guarantee with a bare "and," so a reader can't tell whether the row-scope filter is an independent, sufficient safeguard or a backstop in case the timing guarantee is ever violated. This doesn't need forcing into "because" — that would assert a causal link the paragraph doesn't establish — but the relation between the two guarantees is worth naming explicitly if the author knows it.

**Concrete rewrite:** Ask author: what does a ledger-fold pass compute from the raw imported rows, and what does "invoice-drift" measure?
`Ask author: does the fold pass recompute a running balance, merge partial/duplicate entries, or something else — and is "invoice-drift" the gap between invoiced and ledgered amounts, or a different figure?`
Once that's answered, sentence one can name the mechanism directly, e.g. "The billing job runs ledger-fold passes after each import, [mechanism from author, e.g. recomputing each account's running balance], which keeps the invoice-drift total (defined by the author) accurate."

Fallback if the mechanism isn't available: cut the unearned claim and let the two facts the paragraph can already back up carry it: "The billing job runs ledger-fold passes after each import. Each pass finishes before the nightly export starts, and the export reads only folded rows." This drops "stay accurate" instead of inventing why it's true.

**Rewrite check:** Neither the ask-author question nor the fallback contains rule-of-three, X-not-Y/negative parallelism, em-dash antithesis, avoid-by-default phrases, or prestige adjectives, and neither ends on decorative closure. The fallback doesn't invent a name, count, tool, or timing — it keeps only the order and scope facts already in the source and removes the unsupported claim instead of replacing it with an invented mechanism. Passes self-detectors.

**Remembered line:** "the export reads only folded rows" — the one line in the paragraph that names an actual, checkable boundary instead of an outcome asserted on trust.
