Verdict: keep

Slop tells: None. No avoid-by-default phrases, no high-risk words (delve, realm, tapestry, testament, pivotal, crucial, underscore, intricate, meticulous, multifaceted, foster, bolster, garner, showcase, highlight, emphasize, encompass, utilize, facilitate, transformative, groundbreaking, seamless, robust-outside-engineering-context), no copula displacement ("serves as," "stands as," "features," "marks," "represents"), no hedged symmetry ("Whether X or Y," "While X, Y is also important"), no em-dash cadence (no em-dashes at all), no rule-of-three, no "Not X. Y." negative parallelism, no rhetorical staccato/antithesis (both sentences are additive and causal, not oppositional), no decorative closure ("In conclusion," "Overall," "Ultimately").

Specificity missing: None. Every noun phrase names a concrete actor or artifact: the billing job, ledger-fold passes, each import, invoice-drift totals, the nightly export, folded rows. Nothing stands in for an unnamed tool, person, count, or timing that would need an ask-author note.

Inflated claim: "stay accurate" is the one phrase worth testing, since claims of this kind are exactly what this skill checks against evidence. It survives the test: the second sentence supplies the two mechanisms that earn it — an ordering guarantee (the fold pass finishes before the export starts) and a filter guarantee (the export reads only folded rows). Together they rule out the specific failure the claim implies is being avoided: the export reading a row before it has been folded. Per false-positive restraint, nearby context supplies the mechanism, so this is not flagged. The shape matches the doctrine's own worked keep case — "The queue is robust because each job has an idempotency key, a retry receipt, and a dead-letter cutoff" — a qualifier earned by a named mechanism, not asserted by rhythm.

Flow break: None. Sentence 1 makes a claim that raises the obvious next question: accurate how, given the export is a separate process from the fold passes? Sentence 2 answers exactly that question with the ordering and filter guarantee. That is a dependency relation — the claim depends on, and is explained by, the mechanism in sentence 2 — not two facts sitting side by side and left to imply a connection.

Concrete rewrite: None needed. The paragraph already leads with mechanism (pass timing, row filtering) instead of asserting importance and expecting the reader to accept it on cadence.

Rewrite check: N/A — no rewrite was produced, since the verdict is keep. The source itself was checked against this slot's own list (rule-of-three, X-not-Y / negative parallelism, em-dash antithesis, banned avoid-by-default phrases, prestige adjectives, decorative closure, invented facts) and contains none of them.

Remembered line: "the export reads only folded rows" — the clause that turns "stay accurate" from an assertion into a guarantee.
