Verdict: keep

Slop tells: "not just X; it Y" would normally be a fallback rhythm, but here the contrast marks a real category shift — from latency (how fast a request is) to failure model (whether a request can complete at all). The "because" clause supplies the concrete behavior that justifies the category shift.

Specificity missing: nothing load-bearing. A reader might still want to know what "completes locally" means in practice (writes to a local store? returns from a local cache? queues for later reconciliation?), but the sentence has done the work of naming the change in kind.

Inflated claim: none. The sentence promises a category shift and then supplies the behavior that constitutes it: the request now completes locally when the central service is down. That is the failure-model change, named directly.

Flow break: none. The shape is claim → category shift → mechanism, and the semicolon is doing the work the conjunction would otherwise do.

Emphasis-source test: flattened — "this change moves the request from depending on the central service to completing locally, which is a failure-mode change, not a latency tweak." The residual claim still names the actor (the request), the mechanism (local completion), and the limit (when the central service is down); the contrast was carrying real information, not rhythm.

Syntax-relation test: the implied relation is "the latency framing understates the change, because the request no longer depends on the central service being up." The connective is supplied by the sentence itself ("because… central service is down"), so the syntax is doing real work, not standing in for an absent relation.

Concrete rewrite: not needed. Leave the sentence as written; the "not just" earns its keep because the category it rules out (latency optimization) is a real and tempting misreading of what changed, and the clause after the semicolon names the actual change.

Remembered line: "not just" is allowed when the X it negates is the misreading the reader was about to make.
