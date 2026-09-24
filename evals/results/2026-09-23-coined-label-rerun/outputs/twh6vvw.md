Verdict: keep

Slop tells: None found. No avoid-by-default phrases or high-risk words (no "delve," "testament," "pivotal," "seamless," etc.). No copula displacement — the verbs are plain and concrete (runs, stay, finishes, starts, reads), not "serves as"/"stands as"/"represents." No hedged symmetry, no decorative em-dashes, no rule-of-three, no "Not X. Y." antithesis rhythm, no bullet/bold/table fake structure.

Specificity missing: None. The actor is named (the billing job), and the mechanism is named (ledger-fold passes run after each import). The paragraph backs its claim with two distinct, checkable guarantees rather than a vague assurance: an ordering guarantee ("each pass finishes before the nightly export starts") and a scope guarantee ("the export reads only folded rows"). Nothing here needs an ask-author fallback — there is no missing tool name, count, or timing; the timing relation given is itself the concrete fact.

Inflated claim: "stay accurate" reads as evaluative, but it passes the emphasis-source test. Flattened, the line is "fold passes run after each import, so totals are accurate" — it still names an actor and a mechanism, so the claim is carried by the idea, not by cadence. It's further earned by the second sentence's two supporting mechanisms (temporal ordering + read-scope filter), the same shape as the skill's own "robust" example (a qualifier earned by naming the specific mechanisms that produce it). Verdict: keep, earned.

Flow break: None. Sentence 1 raises an implicit question — if fold passes and the nightly export can run independently, how do we know the export never reads a row mid-fold or unfolded? — and sentence 2 answers exactly that with two concrete guarantees, timing then scope. Applying the syntax-relation test: the implied relation can be restated as "...stay accurate because each pass finishes before the nightly export starts and the export reads only folded rows" without inventing anything, so the "and" in sentence 2 is coordinating two independently true guarantees, not standing in for a relation that isn't there. No hinge sentence needed.

Concrete rewrite: Not applicable — the paragraph already meets the bar, so no rewrite is produced.

Rewrite check: N/A, no rewrite produced.

Remembered line: "the export reads only folded rows" — the specific, checkable guarantee a reader could verify against the actual code.
