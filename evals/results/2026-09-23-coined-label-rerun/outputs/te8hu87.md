Verdict: ask-author

Slop tells:
- Coined compound label — "exact-head checks": named but never defined. It is not a standard term in this domain (unlike "dead-letter queue" or "two-phase commit"), and nothing in the paragraph says what "exact" compares or what "head" refers to.
- Coined compound label — "editorial-row layouts": same problem. "Editorial row" is presented as if the reader already knows which rows count as editorial and what "layout" property is being protected.
- Compressed antithesis — "during the merge rather than at read time": the prior clause ("before each merge") earns the merge side. Nothing earns the read-time side; it is the first mention of reading anywhere in the paragraph, so the contrast asserts a comparison the paragraph never sets up.
- Inflated claim riding on the two undefined labels: "stay consistent" promises more than the described mechanism demonstrates (see below).

Specificity missing:
- What the "exact-head" comparison actually checks: hash/checksum of the head row, byte-identical content, row count, something else.
- What "head" means in this system: first row of a shard, latest committed row, a specific offset or pointer.
- What makes a row "editorial," and why layout consistency is scoped to that row type rather than to all rows.
- What the indexer does once it finds a mismatch at merge time: block the merge, retry, merge-and-flag. Without this, "surfaces" could mean "is logged while the merge proceeds anyway," which would not deliver the "stay consistent" promised in sentence 1.

Inflated claim:
Sentence 1 claims an outcome — "editorial-row layouts stay consistent across shards" — that reads as a guarantee. Sentence 2 only supports a timing property: drift "surfaces during the merge." Surfacing is detection, not correction. Unless a detected mismatch actually blocks or fixes the merge (unstated), the check guarantees only that you find out earlier, not that layouts stay consistent. The paragraph lets the stronger claim (consistency) borrow support from the weaker, narrower one (earlier detection) without stating the connecting step.

Flow break:
The "Because" clause in sentence 2 reads as if it is backing up sentence 1's claim, but it actually narrows it: it defends "you find out at merge" (a timing claim), not "layouts stay consistent" (an outcome claim). The paragraph does not name that narrowing, so it reads as one continuous argument when it is really two claims of different strength stacked without a bridge. No prior or following paragraph was supplied, so cross-paragraph flow is not assessable here — this is the internal transition only.

Concrete rewrite:
Ask author: What does the "exact-head" comparison check, specifically — hash/checksum of the head row, byte-identical content, row count, or something else — and what does the indexer do when heads don't match across replicas: block the merge, retry, or merge and flag? Also, what makes a row "editorial" here, and is layout consistency scoped to that row type only or to all rows?

Fallback if those facts aren't available before this ships: drop the two undefined labels and the unproven guarantee, and say only what the paragraph actually supports:

"The indexer checks each shard's head before merging and catches a mismatch there. What 'head' means precisely, and what happens after a mismatch is found, are not stated in this paragraph."

Rewrite check: The concrete rewrite (the ask-author question and its fallback) contains no rule-of-three, no X-not-Y / negative-parallelism template, no em-dash antithesis, none of the banned avoid-by-default phrases, no prestige adjectives, and no decorative closure. It also does not reuse the merge-vs-read contrast flagged above — the fallback drops that comparison rather than repeating it without evidence — and it does not invent the mismatch-handling behavior; it names that gap explicitly instead of resolving it. Passes self-detectors.

Remembered line:
The check happening before merge earns "a mismatch gets caught there"; it doesn't yet earn "layouts stay consistent" — that second claim needs a stated answer for what happens after a mismatch is found.
