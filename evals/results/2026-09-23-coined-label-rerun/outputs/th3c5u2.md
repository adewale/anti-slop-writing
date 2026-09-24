# Critique

**Paragraph reviewed:**
> The indexer runs exact-head checks before each merge, so editorial-row layouts stay consistent across shards. Because the check happens at the head, drift between replicas surfaces during the merge rather than at read time.

Verdict: keep

Slop tells: None found. No banned phrases ("at its core," "not just X but Y," "this is where X comes in," etc.), no high-risk/prestige words ("robust," "seamless," "underscore," "crucial," and so on), no copula displacement ("serves as"/"stands as"/"represents"), no hedged symmetry, no em-dash clusters (no em-dashes appear at all), no rule-of-three, no "Not X. Y." negative parallelism. Both sentences use hypotaxis — "so" in sentence 1, "Because ..." in sentence 2 — to name the relation explicitly instead of leaving two clauses to sit side by side. That is the move this doctrine asks for, not one it flags.

Specificity missing: "drift" names the failure category (replicas diverging) without saying what diverges — row order, row content, row count, or a hash/checksum mismatch. The read-time side of "during the merge rather than at read time" is not spelled out with what a reader would actually see. This is not being scored against the paragraph: per the antithesis rule, when the prior clause already supplies the mechanism a contrast points at, the contrast is earned and should not be graded as compressed on cadence alone — and "Because the check happens at the head" is exactly that mechanism for the merge-time side. Naming the concrete read-time symptom would need a fact the paragraph doesn't supply (see Concrete rewrite).

Inflated claim: None. "stay consistent across shards" is a bounded claim tied directly to the named check (exact-head checks before merge), not an unbacked importance claim.

Flow break: None. Sentence 2 answers the question sentence 1 raises — if the indexer checks before merging, where does a mismatch actually get caught? — and adds the merge-vs-read-time timing. One soft spot: "the check happens at the head" partly restates sentence 1's "exact-head checks ... before each merge" before delivering the new point. Worth tightening, not a flow failure.

Concrete rewrite: Not required for the verdict. Two optional moves:
1. Trim the restatement: "The indexer runs exact-head checks before each merge, so editorial-row layouts stay consistent across shards; drift between replicas surfaces there, at the head, rather than later at read time."
2. To name the read-time symptom instead of implying it, that needs a fact the source doesn't give — Ask author: what does a reader actually hit when replica drift isn't caught before merge — stale editorial-row order, a missing row, a duplicate? Fallback if unavailable: keep the paragraph as written; the merge-time claim is already earned without it.

Rewrite check: The trimmed rewrite in (1) reuses only the source's own actor (indexer), mechanism (exact-head checks), and terms (drift, replicas, shards, merge, read time) — no rule-of-three, no X-not-Y negative parallelism, no em-dash antithesis, no banned avoid-by-default phrase, no prestige adjective, no decorative closer, no invented fact. The `ask-author` fallback in (2) does not invent the missing symptom. Passes self-detectors.

Remembered line: "Because the check happens at the head, drift between replicas surfaces during the merge rather than at read time." The paragraph's own second sentence already states the transferable structure — move the failure point from a reader's query to the merge — and needs no replacement.
