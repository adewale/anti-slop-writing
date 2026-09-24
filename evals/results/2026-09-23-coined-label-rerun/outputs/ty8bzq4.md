# Critique

**Paragraph reviewed:**
> The billing job runs ledger-fold passes after each import, so invoice-drift totals stay accurate. Each pass finishes before the nightly export starts, and the export reads only folded rows.

Verdict: keep

Slop tells: None found. No avoid-by-default phrases, no high-risk/prestige words (delve, robust, seamless, crucial, etc.), no copula displacement ("serves as" / "stands as" / "features" / "marks" / "represents" — the verbs used are plain and concrete: runs, stay, finishes, starts, reads), no hedged symmetry, no rule-of-three, no negative parallelism ("Not X. Y."), no decorative em-dash cadence (no em-dashes appear at all), no bullet/bold/table fake structure, no outline-shaped conclusion template.

Specificity missing: None of the load-bearing nouns are abstractions. "Ledger-fold passes," "invoice-drift totals," "nightly export," and "folded rows" are named, checkable mechanisms, not generic filler like "data integrity" or "operational efficiency." One open question for the author, offered as a courtesy rather than a blocking gap: sentence two states two guarantees (fold passes finish before export starts; export reads only folded rows) without saying how they relate — is the row filter a backstop for a pass that overruns its window, or would the timing guarantee alone already make the filter redundant? The paragraph doesn't need to answer this to be readable, but a reader auditing the correctness claim in sentence one would want to know.

Inflated claim: None. "stay accurate" is a modest, falsifiable claim about a named metric, not a significance/prestige claim. Emphasis-source test: flattening sentence one to "The billing job runs ledger-fold passes after each import; invoice-drift totals then stay accurate" removes the cadence and the claim still names an actor (the billing job) and a mechanism (ledger-fold passes after each import) — it survives, so the idea is carrying the claim, not borrowed rhythm.

Flow break: None. Sentence one makes a claim ("totals stay accurate"); sentence two answers the question that claim raises ("how is that guaranteed?") with two named mechanisms — that's the flow-by-relation pattern working as intended (claim, then mechanism). Within sentence two, "finishes before the nightly export starts, and the export reads only folded rows" coordinates with "and" rather than subordinating, but that is earned, not a slop tell: the two clauses name mechanically different controls (execution order vs. a row-level filter). Forcing a "because" connective between them would assert a causal dependency — "the filter behaves the way it does because of the timing" — that the source doesn't establish and that may not even be true; subordinating here would misrepresent the relation rather than clarify it.

Concrete rewrite: Not needed; the original stands. If the author wants the one open question above resolved, that is the only lever worth pulling: `Ask author: does "the export reads only folded rows" exist as a backstop for a pass that runs past its window, or does it hold independently of the before-export timing guarantee?` No fallback rewrite is offered in its place, since inventing the relationship (e.g., writing "as a safeguard against a late-running pass") would add a mechanism the source never states.

Rewrite check: N/A — no rewrite is offered, so there is no rewrite to re-run detectors on. The ask-author line above names only what to confirm and invents no name, count, tool, or timing.

Remembered line: "the export reads only folded rows" — the one clause a reader can go verify directly, by checking the export query's filter, rather than take on faith.
