Paragraph under review:

> The billing job runs ledger-fold passes after each import, so invoice-drift totals stay accurate. Each pass finishes before the nightly export starts, and the export reads only folded rows.

Verdict: revise

Slop tells: None of the standard AI-writing patterns fire here — no banned phrases, no copula displacement ("serves as" / "represents"), no hedged symmetry, no decorative em-dash clusters (there are no dashes at all), no rule-of-three, no "Not X. Y." staccato antithesis, no bullet/bold/table fake structure. The nouns are concrete, named system parts (billing job, ledger-fold pass, nightly export, folded rows), not prestige abstractions. This reads as engineering prose, not marketing fog.

Specificity missing: The paragraph never says who else, besides the nightly export, reads "invoice-drift totals." "Stay accurate" is phrased as a standing property of the totals themselves, but the only mechanism given (ordering plus a folded-rows-only read) protects the nightly export's view specifically. If any other process reads the totals outside that path — a live dashboard, an API, an ad hoc query run between imports — nothing here says it sees consistent data too.

Inflated claim: Syntax-relation test — try supplying "because" between the two sentences: "...totals stay accurate because each pass finishes before the export starts and reads only folded rows." That connective only holds if the nightly export is the sole reader of the totals. The paragraph states the general claim ("stay accurate") but the evidence proves only the export-scoped case, so the claim's scope outruns what's shown.

Flow break: The two sentences are plain parataxis — set side by side with no connective at all — even though the second sentence is clearly meant to be the mechanism that earns the first sentence's claim. The reader has to supply "and here's why" between them; nothing marks that dependency relation.

Concrete rewrite: "The billing job runs a ledger-fold pass after each import, so the totals the nightly export reports stay accurate: each pass finishes before the export starts, and the export reads only rows that have already been folded."

Rewrite check: No rule-of-three, no X-not-Y / negative parallelism, no em-dash antithesis (no dashes used), no banned avoid-by-default phrases, no prestige adjectives, no decorative closure, no invented facts — the rewrite reuses "nightly export," a detail already in the source, to scope the claim, and adds no new name, count, tool, or timing. Passes self-detectors.

Remembered line: The guarantee this paragraph actually proves isn't "the totals are accurate" — it's "the export never reads a row before its fold pass is done."
