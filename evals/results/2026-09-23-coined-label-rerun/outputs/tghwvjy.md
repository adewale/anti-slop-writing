Paragraph under review:

> The indexer runs exact-head checks before each merge, so editorial-row layouts stay consistent across shards. Because the check happens at the head, drift between replicas surfaces during the merge rather than at read time.

Verdict: keep

Slop tells: None fire. No banned phrase ("In today's...", "It's worth noting", "Not just X but Y", "This is where X comes in", etc.), no high-risk word (no delve/realm/tapestry/testament/pivotal/crucial/underscore/robust-outside-engineering/etc.), no copula displacement ("serves as"/"stands as"/"represents"), no hedged symmetry ("Whether you're X or Y"), no decorative em-dash cluster (no em-dashes at all), no rule-of-three, no "Not X. Y." negative parallelism, no outline-shaped conclusion, no bullet/bold/table fake structure, no generic opening. Both sentences use hypotaxis ("...checks before each merge, so..."; "Because the check happens at the head, ...") instead of parataxis, which is the doctrine's preferred move when the relation matters.

Specificity missing: Nothing that rises to a flag. The paragraph names a concrete actor (the indexer), a concrete mechanism (exact-head checks run before each merge), a concrete scope (editorial-row layouts, shards, replicas), and a concrete timing claim (drift surfaces at merge, not at read time) — this already clears the concrete-mechanism-over-abstract-noun bar. The one implicit step is that "runs checks before each merge, so layouts stay consistent" assumes a failing check blocks or corrects the merge, without saying so directly; that's ordinary gating shorthand (parallel to "CI runs before merge, so main stays green"), not a vague-actor or inflated-significance tell, so it doesn't merit a rewrite or an ask-author query on its own.

Inflated claim: None. The paragraph never asserts importance apart from mechanism — no "this is critical/robust/essential" language. It states what the check does and when its effect becomes visible, and stops there.

Flow break: None. The second sentence is not a new item sitting beside the first; "Because the check happens at the head" unpacks "exact-head checks" from sentence one and uses that to license a specific, testable consequence — when drift becomes visible. That is a dependency/inference relation, marked hypotactically, not two clauses left to imply their own connection. "Surfaces during the merge rather than at read time" is a single, embedded comparison, not a decorative antithesis: the "during the merge" half is directly licensed by the same sentence's "Because" clause, and "at read time" is its plain logical complement (nothing here claims a read-time check exists or was removed), so it is not a leap dressed as a contrast.

Concrete rewrite: None offered. No slop tell was flagged, so there is nothing to cut or rewrite.

Rewrite check: N/A — no rewrite was produced, since the verdict is keep.

Remembered line: "drift between replicas surfaces during the merge rather than at read time" — the fail-fast-at-write-time-instead-of-silent-at-read-time distinction is the one concrete, carrier-bound fact worth taking from this paragraph.
