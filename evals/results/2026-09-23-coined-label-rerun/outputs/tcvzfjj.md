Verdict: keep

Slop tells: None found. Checked against the full detector list: no banned avoid-by-default phrases ("not just X but Y," "This is where X comes in," hedged symmetry, outline-shaped conclusions), no high-risk words ("robust," "seamless," "pivotal," "underscore," etc.), no displaced copula ("serves as" / "stands as" / "represents" — the paragraph uses plain "runs," "finishes," "reads"), no em-dash cadence (no dashes at all), no rule-of-three or negative parallelism ("Not X. Y." patterns), no generic opening or closing.

Specificity missing: None material. The actor is named (the billing job), the trigger is named (after each import), and the claim rests on two named invariants rather than a vague assurance: an ordering guarantee (each pass finishes before the nightly export starts) and a read-scope restriction (the export reads only folded rows).

Inflated claim: "so invoice-drift totals stay accurate" would be inflated standing alone, but the second sentence earns it by naming the exact race it closes off — the export cannot read a row before its fold pass finishes, and cannot read an unfolded row at all. That is the same shape as the doctrine's own keep example, where "robust" is earned by idempotency keys and a dead-letter cutoff: here "accurate" is earned by the ordering guarantee plus the read-scope restriction, not asserted on rhythm.

Flow break: None that forces a rewrite. Sentence 2 answers the question sentence 1 raises — how do you know it's accurate? — which is a dependency relation, not two facts merely sitting beside each other. The link runs through sentence order rather than a stated connective ("so" only covers sentence 1's own clause), but there is only one plausible reading of sentence 2 as support for sentence 1's claim, not contrast or an unrelated fact, so a reader is not left guessing.

Concrete rewrite (optional strengthening, not required): "Because each pass finishes before the nightly export starts and the export reads only folded rows, invoice-drift totals stay accurate." This names the dependency with "because" instead of leaving it to sentence order, at the cost of folding two short sentences into one longer one — a real tradeoff, not a strict improvement, which is why the verdict is keep rather than revise.

Rewrite check: The optional rewrite reuses only the actor, mechanism, and claim already in the source and adds no new fact. It contains no rule-of-three, no X-not-Y / negative parallelism, no em-dash antithesis, no banned avoid-by-default phrase, no prestige adjective, and no decorative closer. Passes self-detectors.

Remembered line: "the export reads only folded rows" — the specific, checkable detail a reader carries forward as the actual guarantee.
