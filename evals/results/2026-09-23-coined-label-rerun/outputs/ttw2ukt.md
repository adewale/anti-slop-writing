Reviewing:

"The billing job runs ledger-fold passes after each import, so invoice-drift totals stay accurate. Each pass finishes before the nightly export starts, and the export reads only folded rows."

Verdict: ask-author

Slop tells: Coined compound labels are the only tell that fires. "Ledger-fold" (pass/rows) and "invoice-drift" are hyphenated process/metric names the paragraph uses but never defines, and neither reads as an established domain term the way "dead-letter queue" or "two-phase commit" would. The hyphen supplies the texture of precision the paragraph hasn't paid for yet. Nothing else fires: no copula displacement ("runs," "finishes," "reads" are all doing real work), no hedged symmetry, no em-dash cadence, no rule-of-three or negative parallelism, no avoid-by-default phrases or watch-list words, no fake bullet/bold structure. The sentence-level cadence is clean and the connectives ("so," "before... starts," "and") are genuine hypotaxis, not decoration.

Specificity missing: What a ledger-fold pass computes (dedupe on import? recalculation of running balances? reconciliation against a source ledger?), and what "invoice-drift" is a delta between (invoiced amount vs. ledger amount? one import vs. the next?). Without either, "folded" names a status the reader must trust rather than check.

Inflated claim: "so invoice-drift totals stay accurate" asserts a correctness result, but what the paragraph actually earns is narrower: the export can never read a row before its fold pass completes (ordering) and never reads a non-folded row (filter). That's a data-freshness guarantee, not proof that folding fixes drift. Apply the doctrine's own keep-test: the "robust" example is earned because each supporting term (idempotency key, retry receipt, dead-letter cutoff) is independently resolvable by the reader; here the one term the accuracy claim leans on, "ledger-fold," is exactly what's unresolved, so it relocates the gap instead of closing it.

Flow break: None in sequencing — sentence two follows sentence one with real subordination ("before... starts") rather than sitting beside it. The break is evidentiary, not structural: sentence two proves a narrower claim (the export can't see pre-fold data) than the one sentence one makes (totals are accurate), and the paragraph reads as though the second sentence closes the first's claim when it only partly does.

Concrete rewrite:
Ask author: What does a ledger-fold pass compute, and what is invoice-drift measured against?
Fallback (cut, no invented fact): "The billing job runs ledger-fold passes after each import. Each pass finishes before the nightly export starts, and the export reads only folded rows." This keeps the two facts the paragraph earns (ordering, filter) and drops the claim it doesn't earn.

Rewrite check: The fallback reuses the paragraph's own second sentence and the unclaused half of the first — no new wording, so it can't contain rule-of-three, X-not-Y, em-dash antithesis, banned avoid-by-default phrases, prestige adjectives, or decorative closure. It invents nothing: an earlier draft of this fallback added "so it never reads a row mid-reconciliation," which would have quietly asserted that folding equals reconciliation — a fact this critique flagged as unknown two fields up. That clause was cut. Passes self-detectors.

Remembered line: "the export reads only folded rows" is the one fully checkable detail in the paragraph — an engineer could find the filter in the export query and confirm it. That is the line worth building the paragraph around; "totals stay accurate" is the one that needs the author before it can be trusted the same way.
