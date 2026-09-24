## P1

Verdict: keep

Slop tells: None found. No banned phrases, no watch-list words, no copula displacement (verbs are "runs," "stay," "happens," "surfaces" — all plain and concrete), no hedged symmetry, no em-dash cadence (no em-dashes present), no staccato antithesis, no rule-of-three, no bullet/bold/colon fake structure.

Specificity missing: None that the paragraph's own claims require. The claim is about detection *timing* (merge vs. read), and the mechanism for that claim is stated directly: the check runs "before each merge" and "at the head," so drift "surfaces during the merge rather than at read time." The paragraph never claims anything about what happens once drift is detected, so it isn't obligated to supply that detail — flagging it as a gap would be grading the paragraph against a claim it never made.

Inflated claim: None. "stay consistent" is not a free-floating evaluative word — it is the direct, in-sentence consequence of a named mechanism (exact-head checks run before each merge), the same pattern the doctrine's own "robust because..." example treats as earned.

Flow break: None. The second sentence is a genuine hinge, not a restatement: it explains *why* the check's placement ("at the head," "before each merge") produces the specific timing effect named in the first sentence. The relation is named explicitly with "Because," not implied by cadence or left for the reader to infer.

Concrete rewrite: Not needed — the paragraph already states mechanism and effect in plain, subordinated prose.

Rewrite check: N/A — no rewrite offered (keep verdict).

Remembered line: "drift between replicas surfaces during the merge rather than at read time" — the operational payoff of the paragraph in one clause.

## P2

Verdict: keep

Slop tells: None found. No banned phrases or watch-list words. "uses" is a plain, concrete verb naming the actual mechanism, not a displaced copula. No em-dashes, no hedged symmetry, no staccato antithesis.

Specificity missing: None. Every compound noun names a real, standard mechanism (write-ahead log, copy-on-write snapshots, fsync, checkpoint), and the sentence states exactly which failure window is covered ("between the enqueue and the fsync") and exactly what recovery looks like ("replays from the last checkpoint"). These are established systems-engineering terms, not coined or vague ones — the same category the skill's own worked example (queue + idempotency key + retry receipt + dead-letter cutoff) treats as earning their place.

Inflated claim: None. The paragraph never asserts durability, reliability, or robustness as a label — it states the mechanism and lets the reader infer the property, rather than claiming the property and hoping the reader doesn't check.

Flow break: None — single sentence; the internal cause/effect relation is named directly with "so," and the final clause ("instead of dropping the job") is an earned contrast because the preceding clause supplies the mechanism that makes it true, not cadence alone.

Concrete rewrite: Not needed.

Rewrite check: N/A — no rewrite offered (keep verdict).

Remembered line: "a crash between the enqueue and the fsync replays from the last checkpoint instead of dropping the job" — the exact failure window and the exact recovery behavior, in one clause.

## P3

Verdict: keep

Slop tells: None found. No banned phrases or watch-list words. "We call the pre-merge comparison an exact-head check" is a direct definitional move, not a cliché transition ("this is where X comes in") or a hedge.

Specificity missing: None — of the three paragraphs this one leaves the least room for doubt. It names the term and defines it in the same breath, with an operational mechanism: hash the head revision on both replicas, refuse the merge when they differ. Nothing about the claim is left abstract.

Inflated claim: None.

Flow break: None — single sentence; the subordinate clause "when they differ" names the exact trigger condition rather than leaving the relation implied.

Concrete rewrite: Not needed.

Rewrite check: N/A — no rewrite offered (keep verdict).

Remembered line: "the indexer hashes the head revision on both replicas and refuses the merge when they differ" — the full mechanism in one clause.
