Verdict: keep

Slop tells: None found. No avoid-by-default phrases, no high-risk/prestige words, no copula displacement ("serves as," "stands as," "features," "marks," "represents"), no hedged symmetry ("Whether X or Y," "While X, Y is also important"), no em-dash cadence, no rule-of-three, no "Not X. Y." negative parallelism, no bullet/bold/table fake structure. Verbs are plain and specific throughout: runs, finishes, starts, reads.

Specificity missing: None. Every actor and object is named rather than gestured at: "the billing job," "ledger-fold passes," "invoice-drift totals," "the nightly export," "folded rows." Nothing here stands in for an unnamed "the system" or "it."

Inflated claim: None. "stay accurate" reads like an importance claim on first pass, but the second sentence earns it with two concrete, checkable guarantees instead of asserting it on cadence alone: (1) each fold pass finishes before the nightly export starts (an ordering guarantee), and (2) the export reads only folded rows (a read-time filter). This is the same shape as the doctrine's own keep example — "The queue is robust because each job has an idempotency key, a retry receipt, and a dead-letter cutoff" — where the qualifier is earned by named mechanism, not borrowed rhythm. Flattened-cadence test: "Billing folds ledgers after import; export waits for fold completion and reads only folded rows" — the claim still names an actor and a mechanism, so the idea is carrying the sentence, not the rhythm.

Flow break: None. Sentence 2 answers the question sentence 1 raises — how does folding keep totals accurate? — with the specific ordering-plus-filter mechanism. That's a dependency/evidence relation between the two sentences, not two facts merely placed in sequence. Inside sentence 2, the coordinating "and" is doing honest work joining two independent, complementary guarantees (timing and filtering); it is not disguising a single causal claim as a list. Forcing that "and" into "because" — e.g. "Because each pass finishes before the export starts, the export reads only folded rows" — would misstate the mechanism by chaining two independent guarantees into one false cause, which would be worse than the original.

Concrete rewrite: No rewrite needed; keep as written.

Rewrite check: N/A — no rewrite was produced (verdict: keep).

Remembered line: "the export reads only folded rows" — the concrete filter that makes the accuracy claim checkable rather than asserted.
