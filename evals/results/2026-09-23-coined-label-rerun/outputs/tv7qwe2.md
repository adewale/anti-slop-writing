Reviewed paragraph:

> The indexer runs exact-head checks before each merge, so editorial-row layouts stay consistent across shards. Because the check happens at the head, drift between replicas surfaces during the merge rather than at read time.

Verdict: keep

Slop tells: None of the source-backed signs fire. No banned avoid-by-default phrase, no copula displacement ("serves as"/"represents"), no hedged symmetry ("whether you're X or Y"), no rule-of-three, no em-dash cadence (no em-dashes at all), no "not just X but Y." The one construction worth stress-testing is "surfaces during the merge rather than at read time," a two-sided contrast. Applying the staccato contrast test: the "merge" side is evidenced twice over (sentence 1's "before each merge," and this sentence's own "Because the check happens at the head"); the "read time" side gets no separate evidence, but the "because" clause supplies the mechanism the contrast points at — checks fire at the head, so whatever they'd catch is necessarily caught before a read can happen. That satisfies the earned-contrast condition ("read the prior sentence first; if it supplies the mechanism, the contrast is earned") rather than the compressed-antithesis one, so it's not graded as a leap.

Specificity missing: "exact-head checks" and "editorial-row" are used as settled domain terms with no one-clause gloss (what's compared at the head — row hash, schema, column order?). That's reasonable compression for a reader who already knows this indexer, not a slop tell, but it's the one spot an unfamiliar reader would stall on. The paragraph also shifts from shard-level consistency (sentence 1) to replica-level drift (sentence 2) without stating that replicas sit inside shards — a fine assumption if the audience already holds that model, a gap otherwise.

Inflated claim: None. Nothing claims significance ("crucial," "ensures," "guarantees," "seamless"). The paragraph states a mechanism (check timing) and a deterministic, falsifiable consequence (detection timing) — it doesn't tell the reader the mechanism matters, it shows when it fires.

Flow break: None. Sentence 2 takes the premise sentence 1 established (checks run before merge, i.e., at the head) and derives a new, non-redundant consequence from it (when drift becomes observable). That's an inference relation, correctly marked with "Because," not a restatement of sentence 1's claim.

Concrete rewrite: Not needed — paragraph keeps as written.

Rewrite check: N/A, no rewrite produced. Ran the same detectors on the kept original anyway: no rule-of-three, no X-not-Y / negative parallelism, no em-dash antithesis, no avoid-by-default phrases, no prestige adjectives, no decorative closure ("that was the point," "in conclusion," "overall," "ultimately"), no invented facts. Passes self-detectors.

Remembered line: "drift between replicas surfaces during the merge rather than at read time" — the concrete payoff of the paragraph: it names exactly when the failure becomes visible, which is the fact a reader would carry away and could go verify.
