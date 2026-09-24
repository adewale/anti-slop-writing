Paragraph reviewed:
"The indexer runs exact-head checks before each merge, so editorial-row layouts stay consistent across shards. Because the check happens at the head, drift between replicas surfaces during the merge rather than at read time."

Verdict: ask-author

Slop tells:
- "exact-head checks" is a coined compound label: the hyphen promises a precise mechanism, but the passage never says what "exact" compares (an offset? a content hash? a row count?) or what "head" refers to (first row, latest write pointer, replica offset).
- "editorial-row layouts" is a second coined compound label: "layout" could mean row order, schema, or rendered structure, and nothing in the paragraph fixes which.

Specificity missing:
- The comparison basis for the "exact" check.
- The referent of "head" (shard head vs. replica head vs. index head).
- What "editorial-row layout" denotes, and what "stay consistent" would fail to look like if the check didn't run.

Inflated claim:
- No stock significance vocabulary ("crucial," "seamless," etc.) appears. The risk here is unearned precision rather than unearned importance: "exact" and "stay consistent" promise a specific guarantee that the passage doesn't back with a stated mechanism, so the claim reads more certain than the evidence given supports.

Flow break:
- None. "Because the check happens at the head" is real hypotaxis, not decoration: it subordinates sentence two to explain sentence one's timing consequence (check placement -> when drift is caught), and the "rather than at read time" contrast is earned by that same explanation, not asserted on cadence alone.

Concrete rewrite:
- Ask author: What does the exact-head check actually compare between replicas — an offset/pointer match, a hash of the head record, or a row count? And what does "editorial-row layout" mean here — row order, a schema, or rendered structure?
- Fallback, using only what sentence two already commits to and adding no new facts: "Before merging, the indexer checks whether each shard's head matches its replica's head. Because that check runs at the head, a drifted replica is caught at merge time rather than later, when a reader queries a stale shard."

Rewrite check:
- No rule-of-three, no X-not-Y / negative parallelism, no em-dash antithesis, no avoid-by-default phrases, no prestige adjectives, no decorative closure. The fallback's "matches its replica's head" and "a reader queries a stale shard" restate what the source's own second sentence already implies (a replica-to-replica comparison whose failure is the "drift" a reader would otherwise hit) rather than inventing a tool, count, or timing. Passes self-detectors.

Remembered line:
- Put the check at the head, before merge, where a mismatch is still cheap to catch, rather than after a reader hits a stale shard.
