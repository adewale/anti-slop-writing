Paragraph reviewed:
"The billing job runs ledger-fold passes after each import, so invoice-drift totals stay accurate. Each pass finishes before the nightly export starts, and the export reads only folded rows."

Verdict: ask-author

Slop tells: Coined compound labels — "ledger-fold passes" and "invoice-drift totals" are hyphenated noun phrases that name a process and a metric the paragraph never defines. A coined compound is earned only if the passage defines it in place or the term is already standard in the domain (like "dead-letter queue" or "two-phase commit"). Neither holds here: "folded rows" in the second sentence reuses "fold" without saying what folding does to a row, and nothing states what invoice-drift is measured against. No other detector fires — no banned phrases, no copula displacement, no hedged symmetry, no em-dash cadence, no rule-of-three or negative parallelism. Otherwise this reads as plain, concrete engineering prose.

Specificity missing: (a) What operation does a ledger-fold pass perform on a row — sum, reconcile, dedupe, something else? (b) What baseline does "invoice-drift" measure against — a prior invoice, the current ledger balance, an external source? Sentence 1 leans on both undefined terms to support "stay accurate," so the accuracy claim currently rests on trust in an unnamed mechanism rather than on anything the reader can check.

Inflated claim: None. "Stay accurate" is stated plainly, not hyped — the gap is missing mechanism (see above), not inflated vocabulary.

Flow break: None. Sentence 2 does real work: it hands the accuracy claim in sentence 1 a partial, checkable backer — an ordering guarantee (pass completes before export starts) plus a filter (export reads only folded rows) — even though it never explains what folding computes. The two sentences build on each other rather than merely sitting side by side.

Concrete rewrite: Ask author: what does a ledger-fold pass do to a ledger row — sum each import's delta into a running total, reconcile against a prior snapshot, drop duplicate entries, something else? And what does "invoice-drift" measure against — the last invoice sent, the current ledger balance, an external system of record? Naming that turns "stay accurate" into a checkable claim.
Fallback if the mechanism can't be supplied: drop the unproven accuracy clause and keep only the guarantee the paragraph already proves: "The billing job runs a fold pass after each import. Each pass finishes before the nightly export starts, and the export reads only the rows that pass has already folded."

Rewrite check: The fallback contains no rule-of-three, no X-not-Y/negative parallelism, no em-dash antithesis, no avoid-by-default phrases, no prestige adjectives, no decorative closure, and no invented facts — it restates sentence 2 almost verbatim and drops the unsupported clause instead of filling it with a guessed mechanism. The ask-author question itself offers candidate mechanisms as options ("sum ... reconcile ... dedupe ... something else"), not as asserted fact, matching the doctrine's own ask-author pattern. Passes self-detectors.

Remembered line: "The export reads only folded rows" — the one claim in the paragraph that is already concrete and checkable without asking the author anything further; it is the detail worth keeping no matter how the ask-author question resolves.
