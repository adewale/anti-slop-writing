Verdict: keep

Slop tells: None found. Checked against every source-backed detector: no banned avoid-by-default phrases, no high-risk words (delve, realm, landscape, tapestry, testament, pivotal, crucial, underscore, intricate, meticulous, multifaceted, foster, bolster, garner, showcase, highlight, emphasize, encompass, utilize, facilitate, transformative, groundbreaking, seamless, robust), no copula displacement (the verbs are "runs," "finishes," "starts," "reads" — plain or concrete-action, never "serves as" / "stands as" / "represents"), no hedged symmetry, no em-dash cadence, no rule-of-three, no staccato antithesis, no repeated "Not X. Y." rhythm, no bullet/bold-header fake structure.

Specificity missing: None. Every actor and mechanism is named and checkable: the billing job, ledger-fold passes, invoice-drift totals, the nightly export, folded rows. The one unquantified word is "accurate," but the second sentence cashes it out into two testable guarantees (a timing guarantee and a read-scope guarantee) instead of leaving it as mood.

Inflated claim: None. "Stay accurate" reads as an engineering property, not a prestige claim, because it is immediately earned by the mechanism that follows — the same pattern as the doctrine's own keep example ("robust because each job has an idempotency key, a retry receipt, and a dead-letter cutoff").

Flow break: None. Sentence 1 makes a claim; sentence 2 answers the question that claim raises — how do you know the export isn't reading data mid-fold? — with two distinct guarantees: a timing guarantee (each pass finishes before the nightly export starts, using hypotactic "before" to show which event gates which) and a read-scope guarantee (the export reads only folded rows). These are joined with "and" rather than forced into "because," which is correct: timing and query scope are separate mechanisms, and subordinating one under the other would assert a causal link ("the export reads only folded rows because the pass finished first") that the paragraph never states and that isn't necessarily true — the read-scope restriction could hold independent of timing. Per the parataxis rule, this is a single earned "and" naming an additional fact, not a chain of coordinate ands and not a load-bearing relation left for the reader to guess, so it doesn't need repair.

Concrete rewrite: None needed. The paragraph already has a named actor, a named mechanism, and two checkable guarantees instead of a mood word alone.

Rewrite check: No rewrite was produced, since the verdict is keep. Screening the source paragraph itself against the self-detector list — rule-of-three, X-not-Y / negative parallelism, em-dash antithesis, banned avoid-by-default phrases, prestige adjectives, decorative closure, invented facts — finds none. passes self-detectors.

Remembered line: "The export reads only folded rows." — the one clause a reader could go verify directly against the export's query.
