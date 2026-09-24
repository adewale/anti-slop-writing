Paragraph reviewed:

"The billing job runs ledger-fold passes after each import, so invoice-drift totals stay accurate. Each pass finishes before the nightly export starts, and the export reads only folded rows."

Verdict: keep

Slop tells: None found. No avoid-by-default phrase, no watch-list word (no "delve," "seamless," "robust," "crucial," "underscore," etc.), no copula displacement ("serves as" / "stands as" / "represents"), no rule-of-three, no negative parallelism ("Not X. Y."), no em-dash cadence, no hedged symmetry ("Whether X or Y"), no decorative antithesis. Every verb does real work: runs, finishes, starts, reads.

Specificity missing: None. The claim is carried by named, checkable mechanism, not assertion: a specific process (ledger-fold pass), a specific trigger (after each import), a specific ordering guarantee (pass finishes before the nightly export starts), and a specific read filter (export reads only folded rows). A reader can confirm each of these against the code that implements them.

Inflated claim: None. "stay accurate" is not left to float on its own significance — the same paragraph immediately supplies the two invariants that earn it (pass completes before export starts; export reads only folded rows), the same way the doctrine's own worked example earns "robust" with an idempotency key, a retry receipt, and a dead-letter cutoff rather than asserting it.

Flow break: None. Sentence 1 makes a claim ("totals stay accurate"); sentence 2 answers the question that claim raises — what actually stops the export from reading a row mid-fold? — with the two guarantees that make it true. The relation between the sentences is dependency (sentence 2 is why sentence 1 holds), and it's recoverable from adjacency and shared subject (pass, export) without requiring the reader to guess.

Concrete rewrite: Not required; the paragraph stands as written. For comparison only, a version that makes the dependency lexical instead of positional: "The billing job runs ledger-fold passes after each import. Invoice-drift totals stay accurate because each pass finishes before the nightly export starts and the export reads only folded rows." This is a punctuation/connective preference, not a fix for a defect, and should not be applied as if the source were broken.

Rewrite check: N/A as a replacement, since verdict is keep and no rewrite is being substituted in. The comparison sentence above passes self-detectors regardless: no rule-of-three, no X-not-Y, no em-dash antithesis, no avoid-by-default phrase, no prestige adjective, no decorative closure, no invented fact — it reuses only the nouns and verbs already in the source.

Remembered line: "the export reads only folded rows." That is the one clause a reader could go verify directly against the export's query, and the paragraph already ends on it — no added closer needed.
