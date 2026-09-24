Paragraph reviewed:

> The indexer runs exact-head checks before each merge, so editorial-row layouts stay consistent across shards. Because the check happens at the head, drift between replicas surfaces during the merge rather than at read time.

Verdict: keep

Slop tells: None. No avoid-by-default phrases, no copula displacement (serves as/stands as/features/marks/represents), no hedged symmetry, no rule-of-three, no decorative em-dashes (none present), no prestige/hype adjectives. The one contrast in the paragraph — "surfaces during the merge rather than at read time" — passes the syntax-relation test: the implied relation restates in plain prose with the connective already in the text ("because the check happens at the head, drift is caught then instead of going unnoticed until a client reads the data"), so the cadence isn't standing in for an unsupported claim.

Specificity missing: One soft gap. Sentence 1's claim that layouts "stay consistent" depends on some action once a mismatch is found, and neither sentence names it (merge rejected? row repaired? alert raised?). "Surfaces" only says the drift becomes visible, not what happens next. Minor, since the paragraph's apparent job is detection timing, not remediation.

Inflated claim: None. "Stay consistent across shards" is bounded and tied to a named mechanism (exact-head checks before merge), not unearned significance language.

Flow break: Minor. Sentence 1 scopes the property "across shards"; sentence 2 shifts to drift "between replicas." If a shard's consistency is defined by agreement across its own replicas, the two sentences track the same axis and the shift is harmless; the paragraph doesn't say so, so a reader has to supply the link between "shard" and "replica" themselves.

Concrete rewrite: Not required — the paragraph can stand as written. If closing the shard/replica gap: "The indexer runs exact-head checks before each merge, so a replica whose editorial-row layout has drifted from its shard is caught before it lands. Because the check happens at the head, that drift surfaces during the merge rather than at read time." If the remediation step matters for this section: Ask author: when the head check finds a mismatch, what happens next — is the merge rejected, is the row repaired, or is it only logged?

Rewrite check: The optional rewrite reuses only the source's own connectives ("so," "because") and adds no rule-of-three, no X-not-Y negative parallelism, no em-dash antithesis, no avoid-by-default phrase, no prestige adjective, and no decorative closer; the ask-author line names the missing fact without inventing an answer. Passes self-detectors.

Remembered line: Because the check happens at the head, drift surfaces at merge, not at read time.
