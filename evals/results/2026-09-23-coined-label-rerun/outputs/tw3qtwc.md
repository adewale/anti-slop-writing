Reviewed paragraph:

"The indexer runs exact-head checks before each merge, so editorial-row layouts stay consistent across shards. Because the check happens at the head, drift between replicas surfaces during the merge rather than at read time."

Verdict: keep

Slop tells: None. No undue-significance language, canned emphasis, rule-of-three, em-dash cluster, or bullet/bold fake structure. No copula displacement: "runs," "stay," "happens," and "surfaces" are plain or concrete verbs, not "serves as," "stands as," "features," "marks," or "represents." No hedged symmetry such as "whether X or Y" or "while X, Y is also important." The one contrast in the paragraph, "surfaces during the merge rather than at read time," could be mistaken for decorative antithesis, but the prior clause in the same sentence supplies the mechanism it depends on ("the check happens at the head"), so both sides are earned rather than asserted on cadence alone. Both sentences use hypotaxis ("so," "Because ... rather than") instead of antithetical parataxis, which is the structure the doctrine prefers when the relation matters.

Specificity missing: None that the detectors flag. "Exact-head checks," "editorial-row layouts," and "the head" name a specific mechanism and a specific artifact instead of substituting importance language for missing detail. A reader outside this system might still want "head" defined precisely (a revision pointer, a shard leader, a row position), but that is a glossary gap in the source system's own documentation, not a case of rhythm or inflation standing in for content, so it does not move the verdict.

Inflated claim: None. "Stay consistent across shards" and "drift between replicas surfaces during the merge rather than at read time" are bounded, falsifiable engineering claims tied to the stated mechanism (the check runs before merge, at the head), not unearned significance language.

Flow break: None. Sentence one states a mechanism and its effect: checks before merge keep layouts consistent. Sentence two explains why, by naming where the check runs and what that ordering implies: drift is caught at merge, not at read. The second sentence is dependent on the first and named with an explicit cause connective ("Because"), matching the doctrine's cause pattern rather than sitting beside sentence one unexplained.

Concrete rewrite: Not needed. The paragraph already leads with the mechanism (check timing: before merge, at the head) and ends on a falsifiable consequence (drift caught at merge, not at read). There is no vague actor, no missing fact, and no borrowed cadence to unwind.

Rewrite check: No rewrite was offered, since the verdict is keep, so the same detector list was run against the source paragraph itself: no rule-of-three, no X-not-Y or negative parallelism, no em-dash antithesis, no avoid-by-default phrases, no prestige or high-risk adjectives, no decorative closure, no invented facts. Passes self-detectors.

Remembered line: "drift between replicas surfaces during the merge rather than at read time" is the one falsifiable claim worth carrying forward from this paragraph.
