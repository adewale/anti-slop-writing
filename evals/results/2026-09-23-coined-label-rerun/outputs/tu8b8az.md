Paragraph reviewed:
> The billing job runs ledger-fold passes after each import, so invoice-drift totals stay accurate. Each pass finishes before the nightly export starts, and the export reads only folded rows.

Verdict: ask-author

Slop tells: Two coined compound labels carry the whole claim without being defined anywhere in the passage: "ledger-fold passes" (what does a fold pass actually compute over a ledger row?) and "invoice-drift totals" (drift between which two numbers?). Neither is a standard industry term the way "dead-letter queue" or "two-phase commit" would be, so neither earns the coinage on its own — the hyphenated phrasing gives both the texture of a defined system concept while the referent stays out of reach. The paragraph also leans on a causal "so" to assert an outcome ("so invoice-drift totals stay accurate") without showing the computation that produces it — stating the result of a mechanism instead of the mechanism.

Specificity missing: (1) What a fold pass does to a row — dedupe, sum, reconcile against billed amounts, collapse multiple entries per invoice? (2) What "invoice-drift" measures and what it drifts from — is there a specific discrepancy this prevents, with a source or an example? (3) What actually enforces "each pass finishes before the nightly export starts" — a scheduler/DAG dependency, a lock, single-threaded sequencing? The ordering guarantee is asserted, not shown.

Inflated claim: "so invoice-drift totals stay accurate" presents correctness as automatic once folding runs, but the only support that follows is timing (pass finishes before export starts) and scope (export reads only folded rows) — neither of which shows what folding computes or why skipping it would produce drift. The payoff sentence arrives before any mechanism earns it.

Flow break: The second sentence is offered as if it obviously explains the first, but the relation is left implicit — an unstated-relation parataxis: the reader has to supply the missing connective ("...and that is why totals stay accurate, because...") that the paragraph never states. Nothing ties "reads only folded rows" back to "drift" as the specific failure that the read-scope restriction prevents.

Concrete rewrite:
Ask author: what does a ledger-fold pass compute (e.g., collapsing duplicate ledger entries per invoice, reconciling ledger rows against billed amounts), and what specifically is "invoice-drift" — drift between which two values? Also: what mechanism guarantees the fold pass finishes before the nightly export starts (a workflow/DAG dependency, a lock, sequential execution in one job)?

Fallback (no invented facts; drops the unproven accuracy claim and keeps only what the source establishes):
"The billing job runs a ledger-fold pass after each import. The nightly export starts only once that pass finishes, and reads only folded rows."

Rewrite check: The fallback contains no rule-of-three, no "X not Y" / negative parallelism, no em-dash antithesis, no avoid-by-default phrases, no prestige adjectives, no decorative closure ("that was the point," "in conclusion," "overall," "ultimately"), and no invented facts — it restates only the ordering and scope guarantees the source already gives, and deliberately does not restate the "accurate"/"drift" claim, since backing that claim would require the mechanism the author hasn't supplied. Passes self-detectors.

Remembered line: The one thing this paragraph actually proves is that the export reads only folded rows; "accurate" and "drift" are still asserted, not shown.
