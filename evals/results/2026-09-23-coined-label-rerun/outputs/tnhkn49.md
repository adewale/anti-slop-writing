Verdict: ask-author

Slop tells: Compressed antithesis (staccato contrast test), in "surfaces during the merge rather than at read time." One side is evidenced: merge-time detection, established by "the check happens at the head." The other side, read time as the point drift would otherwise surface, is never shown; the paragraph never describes the read path. Flattened, the core claim still stands ("the check runs at merge time and catches replica drift then"). This fits the compressed case: the claim survives without the cadence, but the comparison to read time is still unsupported — an unstated relation carried by "rather than" instead of by evidence.

Specificity missing: What happens on the read path. Does a query hit any replica directly, with no equivalent check, so drift would otherwise go unnoticed until a client read a drifted replica? That fact would earn "rather than at read time." Separately, sentence one claims consistency "across shards" and sentence two claims drift "between replicas." The paragraph never says whether the exact-head check compares a shard's replicas against each other, shards against each other, or both, so it is unclear whether these are one guarantee stated twice or two different ones.

Inflated claim: None from the watch-list vocabulary (no "crucial," "seamless," "robust," etc.). The overclaim is structural, not lexical: the read-time half of the contrast is stated with the same confidence as the merge-time half despite having no support in the paragraph.

Flow break: The "Because" opening sentence two correctly answers sentence one's implicit "why," so that relation holds. The break is the unbridged noun switch from "shards" to "replicas": a reader can only follow it by assuming, not being told, that each shard's consistency is checked through its replicas.

Concrete rewrite:
Ask author: On the read path, does a query hit any replica without a head check, so drift would otherwise stay invisible until a client's read landed on the drifted replica, or is read time the alternative for some other reason? And does "consistent across shards" describe the same comparison as "drift between replicas" (the check running per shard, across that shard's replicas), or are these two separate guarantees?

Fallback, if that can't be confirmed: cut the unsupported comparison and stop at what the paragraph earns.

"The indexer runs exact-head checks before each merge, so editorial-row layouts stay consistent across shards. Because the check happens at the head, drift between replicas surfaces during the merge."

Rewrite check: The fallback only deletes "rather than at read time"; it adds nothing. No rule-of-three, no X-not-Y / negative parallelism, no em-dash antithesis, no avoid-by-default phrases, no prestige adjectives, no decorative closure, no invented facts. It leaves the shard/replica wording exactly as the source had it; that question is still open, which is why this is a fallback and not a full fix. Passes self-detectors.

Remembered line: "the check happens at the head." The one concrete, falsifiable detail the paragraph's claims lean on. Keep it, and do not let it carry a comparison to read time that it has not yet earned.
