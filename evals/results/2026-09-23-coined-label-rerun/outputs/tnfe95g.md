Verdict: ask-author

Slop tells:
- Coined compound label — "exact-head checks": the hyphen promises precision ("exact") but the passage never says what is being compared. "The check happens at the head" just restates the label; it doesn't define it.
- Coined compound label — "editorial-row layouts": names an artifact ("layout") the passage never describes — row order, a schema, a column arrangement, or something else.
- Checked and not flagged — "drift... surfaces during the merge rather than at read time": sentence one already establishes the merge-time check, so the "merge" side of this contrast is evidenced, and it reads as an earned fail-fast framing (catch it at write time, not read time), not decorative rhythm. Not counted as a slop tell.

Specificity missing: What does "exact" compare — a checksum of the head record, a byte-for-byte diff, a row count, a schema/version match? What is an "editorial-row layout" concretely — the order rows are written in, a schema, a column arrangement? After drift "surfaces" at merge, what happens next — does the merge block, alert an operator, or repair from the head automatically?

Inflated claim: "so editorial-row layouts stay consistent across shards" claims a resolved state. The next sentence only supports detection: drift "surfaces during the merge." Surfacing a problem at merge time is a real, useful property, but it is not the same claim as layouts staying consistent — that would also require the merge to correct or block on what it finds, which the paragraph never says.

Flow break: None structurally — "Because the check happens at the head" correctly subordinates mechanism to outcome, which is the hypotaxis the doctrine wants. The gap is evidentiary rather than structural: sentence one asserts an outcome (consistent layouts) that sentence two doesn't fully back up, since it covers only the timing of detection, not what restores consistency. The paragraph raises the question "what happens once drift surfaces" without answering it.

Concrete rewrite:
Ask author: What does the exact-head check actually compare (checksum of the head record, byte-for-byte diff, row count)? What happens once drift surfaces at merge — does the merge block, alert someone, or auto-repair from the head? What does "editorial-row layout" mean here — row order, schema, or column arrangement?
Fallback (states only what the source already evidences, invents nothing): "Because the indexer checks each shard's head record against its replicas before merging, drift between replicas is caught at merge time rather than when a reader queries the data."

Rewrite check: The fallback has no rule-of-three, no "Not X. Y." negative parallelism, no em-dash antithesis, no banned avoid-by-default phrases, no prestige adjectives, and no decorative closer. It drops "exact" and "editorial-row layout" instead of guessing at a referent, and it says "caught" rather than "stays consistent," matching only what the source supports. Passes self-detectors.

Remembered line: A check called "exact" still owes the reader what it compares — catching drift at merge time is a claim the paragraph earns; calling that "consistent" is a bigger claim it hasn't paid for yet.
