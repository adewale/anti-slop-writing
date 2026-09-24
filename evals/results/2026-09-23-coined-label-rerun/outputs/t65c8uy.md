Paragraph reviewed:
"The indexer runs exact-head checks before each merge, so editorial-row layouts stay consistent across shards. Because the check happens at the head, drift between replicas surfaces during the merge rather than at read time."

Verdict: ask-author

Slop tells:
- Coined compound label — "exact-head checks": the hyphen supplies the texture of a defined technical term, but the passage never says what property is being compared (a hash/checksum of the head row? full field-by-field equality? row count or column order?) or what "head" refers to (head row of a shard, head of a replication log, most recent write). Sentence 2 ("the check happens at the head") only restates *where/when* the check runs — it relocates the gap instead of closing it; an undefined supporting phrase doesn't earn the claim.
- Coined compound label — "editorial-row layouts": names a row type/format the paragraph never defines. Not treated as domain-standard (unlike "dead-letter queue" or "two-phase commit") because nothing here lets an outside reader resolve what makes a row "editorial" or what "layout" means for it (column order? field set? serialization shape?).
- Considered and not flagged: the merge-vs-read-time distinction in sentence 2 reads like a staccato contrast ("during the merge rather than at read time"), but the prior clause supplies the mechanism (check runs before merge), and the merge-then-read pipeline it implies is a reasonable inference rather than a bare cadence trick — earned, not decorative.

Specificity missing:
- What property "exact-head" compares across replicas.
- What "head" refers to (row, commit, log position).
- What defines an "editorial" row versus the index's other row types.

Inflated claim: None. No prestige adjectives, no undue-significance language, no avoid-by-default phrases. Both claims (checks run before merge; drift surfaces at merge, not read) are scoped and causal rather than inflated.

Flow break: None structural. Sentence 2 ("Because the check happens at the head, drift... surfaces during the merge rather than at read time") is hypotactic and correctly subordinates mechanism (timing) to consequence (when drift is caught) — this is the sentence machinery the skill prefers, not a tell. The one soft gap: "read time" is introduced with no earlier mention of a read path, so the contrast leans on the reader inferring the indexer's merge-then-read pipeline rather than the passage stating it.

Concrete rewrite:
Ask author: what does "exact-head" compare — a hash/checksum of the head row, full row equality, or row count/schema shape? And what marks a row as "editorial" versus the index's other row types?
Fallback if unavailable: drop the unresolved modifiers rather than guess at them — "The indexer checks each shard's head row before merging, so row layout stays consistent across shards. Because that check runs before the merge, replica drift surfaces there instead of later, at read time." This keeps the paragraph's causal structure and cuts "exact" and "editorial," which is safer than inventing what they mean. If "exact-head" and "editorial-row" are already defined earlier in the source document (a glossary, an adjacent section), keep the original wording as-is — the sentence structure and causal claim are already sound and need a definition on first use, not a rewrite.

Rewrite check: The fallback rewrite contains no rule-of-three, no X-not-Y/negative parallelism, no em-dash antithesis, no avoid-by-default phrases, no prestige adjectives, no decorative closure, and no invented facts (it removes "exact" and "editorial" rather than guessing at their referents, and reuses the source's own "at read time" instead of adding unstated detail). Passes self-detectors.

Remembered line: "Drift between replicas surfaces during the merge rather than at read time" is the paragraph's one genuinely memorable, specific claim — caught early at merge, not late at read. It would land harder once "exact-head" names the actual comparison, since right now the reader remembers the timing but not the mechanism.
