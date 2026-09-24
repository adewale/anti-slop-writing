Paragraph reviewed:

> The billing job runs ledger-fold passes after each import, so invoice-drift totals stay accurate. Each pass finishes before the nightly export starts, and the export reads only folded rows.

Verdict: keep

Slop tells: Two candidate coined compound labels — "ledger-fold passes" and "invoice-drift totals" — read as hyphenated/compound jargon that could relocate the gap instead of closing it. Applying the false-positive-restraint check: the passage supplies a trigger (after each import), a purpose (keep invoice-drift totals accurate), an output state ("folded rows"), and a consumer boundary (export reads only that state). That's resolvable support, not a bare coinage, so both terms pass as earned domain jargon rather than slop. No other detector fires: no banned avoid-by-default phrase, no copula displacement (the verbs — "runs," "finishes," "starts," "reads" — are all plain and concrete, none of them "serves as/stands as/represents"), no hedged symmetry, no em-dash cadence, no rule-of-three, no "Not X. Y." rhythm, no table/bold fake structure.

Specificity missing: None load-bearing. What's absent is the internal fold algorithm — what transformation actually makes drift totals correct (merge, recompute, replay) — but that sits outside this paragraph's actual claim, which is a synchronization guarantee (ordering plus read-filtering), not an algorithm explanation. This matches the doctrine's own kept example, "The retry policy serves three distinct failure modes: ..." — enumerating the failure modes earns the sentence without explaining retry internals; here, naming the trigger, the output state, and the read boundary earns the accuracy claim without explaining fold internals.

Inflated claim: None. "Stay accurate" is a modest, checkable claim, not a prestige adjective like "seamless," "robust," or "transformative." It is earned by two distinct mechanisms named in the next sentence: an ordering guarantee (pass finishes before export starts) and a filtering guarantee (export reads only folded rows). The two are non-redundant, not decorative padding: ordering buys freshness (this cycle's imports are included in time), filtering buys correctness (no partially-folded rows leak into the export even if timing slipped). The claim is asserted on stated mechanism, not on rhythm.

Flow break: None. Sentence 1 raises the implicit question "how do you know totals stay accurate?" and sentence 2 answers it with two concrete guarantees — a dependency relation, not two ideas merely sitting side by side in a plausible order. The coordinating "and" inside sentence 2 joins two independent, both-true safeguards (timing, then filtering); rewriting it as "because each pass finishes before the nightly export starts, the export reads only folded rows" would invent a causal link that the source doesn't make — the filter holds regardless of whether the timing guarantee does. So the parataxis is the syntactically correct choice here, not an unstated relation to repair.

Concrete rewrite: None needed; the paragraph stands as written.

Rewrite check: N/A — no rewrite was produced, so there is nothing to audit for reintroduced slop. Running the same detectors on the source itself confirms: no rule-of-three, no X-not-Y / negative parallelism, no em-dash antithesis, no banned avoid-by-default phrases, no prestige adjectives, no decorative closer ("That was the point," "In conclusion," "Overall," "Ultimately"), no invented facts. Passes self-detectors.

Remembered line: "the export reads only folded rows" — the one falsifiable detail a reader can hold onto and check directly against the code or the logs.
