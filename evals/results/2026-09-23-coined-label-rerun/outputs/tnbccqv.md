Verdict: ask-author

Slop tells:
- Coined compound label — "exact-head checks" (sentence 1): this names the mechanism the whole paragraph depends on, but never says what is compared. "Exact" implies precision against some baseline, yet no baseline, comparison method, or data (hash, row count, row-by-row diff) is given. The hyphen supplies the texture of precision while the referent stays out of reach; this isn't an established term of art like "dead-letter queue," so it doesn't earn a pass under false-positive restraint.
- Coined compound label, weaker instance — "editorial-row layouts" (sentence 1): a hyphenated artifact name never defined in place. Lower-confidence flag than the one above, since this may be legitimate internal schema vocabulary — but nothing in the paragraph confirms that, so it can't be waved through either.
- Compressed antithesis — "surfaces during the merge rather than at read time" (sentence 2): reading the prior sentence first, as the classification rule requires, it supports only the "during the merge" side (checks run "before each merge"). Nothing in the paragraph supports the "at read time" side — what a reader would actually see, or why the absence of this check would push the symptom to read time. The cadence implies the contrast before the paragraph earns it.

Specificity missing:
- What the exact-head check actually compares (a hash of each shard's head state? a row-by-row diff of editorial rows? a count?).
- What "consistent" fails to look like when the check would catch a problem (reordered rows? duplicated rows? a stale value?).
- What happens after the check finds a mismatch at merge time — block the merge, retry, auto-repair? The paragraph stops exactly where this question opens.

Inflated claim:
- No prestige vocabulary or significance-inflation language ("crucial," "ensures," "guarantees" — none appear), so this isn't the usual less-detail-more-importance failure. The one unscoped claim is the categorical "rather than at read time," which reads as a completeness guarantee (drift is always caught before a read, never after) with no stated boundary — e.g., a replica added after the check ran, or a read that races an in-flight merge. Minor, but worth a boundary condition if the claim is meant to be load-bearing.

Flow break:
- The sentence-to-sentence relation is fine: "Because the check happens at the head" correctly signals a dependency/cause relation to sentence 1, and hypotaxis is used correctly throughout — no parataxis problem here.
- The break is internal to sentence 2 and at the paragraph's end: it asserts the merge-vs-read-time contrast without grounding the read-time side, and it closes right as the natural next question opens ("what does the merge do with a mismatch?") instead of answering it or handing it off to the next paragraph.

Concrete rewrite:
Ask author: what does the exact-head check actually compare — a hash of each shard's head state, a row-by-row diff of editorial rows, or a count? And is "editorial-row" a term already defined elsewhere in this document, or does it need a first-use gloss here?
Fallback if no answer is available: keep the sentence as written rather than guess at the comparison method. Cutting "exact" only removes the false-precision signal — it doesn't supply the missing mechanism, so it isn't offered as a fix on its own.

The antithesis half doesn't need an unstated fact, so it gets a direct rewrite instead of an ask-author flag:
"Because the check happens at the head, a shard that has drifted from its replicas is caught before the merge completes, so the mismatch never reaches a reader."
This keeps the paragraph's own claim (drift is caught at merge, not at read) but replaces the bare "rather than" contrast with the concrete before/after it was implying, without inventing what "caught" mechanically does (fail the merge, retry, auto-repair) — that piece stays open; see specificity missing above.

Rewrite check:
- Rule-of-three: none.
- X-not-Y / negative parallelism: none (no "not X, Y" construction in either the ask-author block or the antithesis rewrite).
- Em-dash antithesis: no em-dashes used for contrast.
- Banned avoid-by-default phrases: none of the listed phrases appear.
- Prestige adjectives: none.
- Decorative closure: none (the remembered line below is carrier-bound, not a generic closer like "that was the point").
- Invented facts: the ask-author block offers named options (hash / row-by-row diff / count) as a multiple-choice question, not an asserted fact — matching the skill's own worked example ("which coding tool? Cursor, Claude Code, Copilot, Aider, other?"). The antithesis rewrite adds no new named tool, count, or mechanism beyond what "caught ... before the merge completes" already implies from the source's own "before each merge."
Passes self-detectors.

Remembered line:
"Checking at the head catches drift before it reaches a reader." — the one concrete, carrier-bound claim the paragraph earns even before the author fills in what the check actually compares.
