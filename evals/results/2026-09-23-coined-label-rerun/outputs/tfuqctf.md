Paragraph under review:
"The billing job runs ledger-fold passes after each import, so invoice-drift totals stay accurate. Each pass finishes before the nightly export starts, and the export reads only folded rows."

Verdict: keep

Slop tells: None. No avoid-by-default phrases or watch-list words, no rule-of-three, no negative parallelism ("Not X. Y."), no em-dash cadence (none present), no bullet/bold/table fake structure, no hedged symmetry ("Whether X or Y," "While X, Y is also important"), no copula displacement — the verbs (runs, finishes, reads, stay) are plain and each does concrete work.

Specificity missing: None load-bearing. The actor is named (the billing job), the mechanism is named (ledger-fold passes), the trigger is named (after each import), and the claim of accuracy is backed by two named guarantees (pass finishes before the nightly export starts; export reads only folded rows). The one thing left undefined is what a ledger-fold pass computes internally — but the paragraph's claim doesn't depend on that detail, so it isn't a gap in this specific claim.

Inflated claim: None. "Accurate" is a plain, checkable claim, not a prestige or significance word, and it is earned by the two mechanisms in the second sentence rather than asserted on rhythm alone. Emphasis-source test: flattening sentence 1 to "Ledger-fold passes run after each import; invoice-drift totals are accurate as a result" still names an actor, a mechanism, and a claim — the mechanism is carrying the sentence, not the cadence.

Flow break: Minor and optional. Sentence 2 is the evidence for sentence 1's claim (it explains why totals stay accurate), but that dependency is left implicit — the paragraph moves from claim to evidence with no connective marking the jump. A reader gets there on one pass, so this isn't a rewrite-forcing break, just a spot where naming the relation would tighten the joint.

Concrete rewrite: Not required — the paragraph is kept as written. Optional tightening, no new facts added, only makes the existing dependency explicit:
"The billing job runs ledger-fold passes after each import, so invoice-drift totals stay accurate: each pass finishes before the nightly export starts, and the export reads only folded rows."
(Single change: period to colon between the two sentences, so the second sentence reads as the stated mechanism for the first instead of an adjacent, separate fact.)

Rewrite check: passes self-detectors. No rule-of-three, no X-not-Y / negative parallelism, no em-dash antithesis, no avoid-by-default phrases, no prestige adjectives, no decorative closure, no invented facts — the only change from the source is one punctuation mark.

Remembered line: "the export reads only folded rows" — the actual safety mechanism: whatever else is true about timing, the export is scoped to never read a row that hasn't been through a fold pass.
