# Critique

Reviewed paragraph:
> The billing job runs ledger-fold passes after each import, so invoice-drift totals stay accurate. Each pass finishes before the nightly export starts, and the export reads only folded rows.

Verdict: ask-author

Slop tells:
"ledger-fold passes" and "invoice-drift totals" are coined, hyphenated compound labels carrying the paragraph's real claim (a mechanism and the artifact it supposedly fixes), but neither is defined in place and neither is an established cross-domain term the way "dead-letter queue" or "two-phase commit" is. The paragraph is dense with named objects (job, passes, export, folded rows) but supplies no mechanism for the one causal claim it makes.

Specificity missing:
What a ledger-fold pass actually does to a row (merges duplicate entries, recomputes a running balance, reconciles against the invoiced amount, something else), and what "invoice-drift" measures — drift between what two numbers, caused by what.

Inflated claim:
"so invoice-drift totals stay accurate" is presented as the proven payoff of running fold passes. The cause-and-effect phrasing makes it read as earned, but nothing in the paragraph shows the connection between folding and correctness — the effect is asserted, not demonstrated.

Flow break:
Sentence 2 doesn't back sentence 1's claim; it answers a different question. "Each pass finishes before the nightly export starts, and the export reads only folded rows" establishes that the export never sees a partially processed import — a read-consistency guarantee. It says nothing about whether the fold computation itself produces accurate drift totals. The paragraph is shaped like claim-then-evidence, but the evidence supports an adjacent property, not the claim it follows.

Concrete rewrite:
Ask author: what does a ledger-fold pass compute, and what does "invoice-drift" measure? Without that mechanism, "accurate" isn't earned by anything stated in this paragraph.

Fallback (cut the unearned claim; let the supported detail carry the paragraph):
"The billing job runs ledger-fold passes after each import. Each pass finishes before the nightly export starts, and the export reads only folded rows, so the export never reads a row from a partially processed import."

If the source document defines "invoice-drift" and the fold mechanism elsewhere, keep the original claim and point to that definition instead of restating it unsupported here.

Rewrite check:
No rule-of-three, no X-not-Y/negative parallelism, no em-dash antithesis, no banned avoid-by-default phrases, no prestige adjectives, no decorative closure. "The export never reads a row from a partially processed import" is drawn directly from the two facts already in the source (pass completes before export starts; export filters to folded rows only) — no new name, count, tool, or timing claim invented. Passes self-detectors.

Remembered line:
"the export reads only folded rows" — the one claim in the paragraph a reader could go check against the code. Keep it as the paragraph's anchor instead of the unearned "accurate."
