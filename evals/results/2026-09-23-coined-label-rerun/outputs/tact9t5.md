Reviewed paragraph:

> The billing job runs ledger-fold passes after each import, so invoice-drift totals stay accurate. Each pass finishes before the nightly export starts, and the export reads only folded rows.

Verdict: keep

Slop tells: None found. Checked against every listed detector: no banned-by-default phrases ("at its core," "not just X but Y," "when it comes to," "whether you're X or Y," "in conclusion," etc.), no watch-list prestige words ("crucial," "seamless," "robust," "underscore," "utilize," etc.), no copula displacement — the verbs are "runs," "finishes," "starts," "reads," all plain and concrete, none of the "serves as / stands as / features / marks / represents" family — no hedged symmetry, no em-dash cadence (no em dashes appear at all), no rule-of-three or negative-parallelism ("Not X. Y."), and no outline-shaped conclusion ("despite challenges...," "looking ahead..."). The paragraph reads as source-grounded systems documentation, not generated filler.

Specificity missing: None blocking. "Ledger-fold pass" and "invoice-drift totals" are used as established internal terms rather than defined inline, but the paragraph supplies enough operational detail around them — runs after each import, must finish before the export starts, the export is scoped to folded rows only — that a reader can infer what the fold guarantees without a dictionary definition of "fold" itself. If this text will be read by someone outside the team who has never seen "ledger-fold" before, one clause on what a pass actually does to a row (merges it into a running balance? recomputes from scratch?) would help; for internal documentation the current compression is earned, not vague.

Inflated claim: None. "Stay accurate" is a plain, unhedged technical claim, not importance language (contrast with "ensures seamless accuracy" or "is critical for accuracy"), and it is earned by the very next sentence: because every fold pass finishes before the export starts, and the export reads only folded rows, the export can never read a mix of pre-fold and post-fold state that would corrupt the total. That is the same pattern as the doctrine's own kept example — "The queue is robust because each job has an idempotency key, a retry receipt, and a dead-letter cutoff" — a claim immediately followed by the concrete condition that earns it.

Flow break: None. Sentence 1 makes a claim ("totals stay accurate") and sentence 2 answers the question that claim raises — accurate because of what? — a dependency relation, not two sentences merely sitting beside each other. Sentence 1 is already hypotactic (the "so" names the consequence directly). Sentence 2 coordinates two independent, verifiable facts (finish-before-export timing, folded-only row scope) with "and"; that is legitimate parataxis rather than an unstated relation, since neither clause makes the reader guess whether it is cause, contrast, or consequence — both are plain, complementary facts about the same guarantee.

Concrete rewrite: None needed. The paragraph passes as written.

Rewrite check: No rewrite was issued, since the verdict is keep — there is nothing new to run the self-detectors against.

Remembered line: "the export reads only folded rows" — the one concrete invariant worth carrying forward: accuracy here is a read-scope guarantee, not a vague promise.
