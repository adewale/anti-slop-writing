Doctrine: /tmp/asw-before-parataxis (pre-edit snapshot of skills/anti-slop-writing, commit 615d671).
Apply model: claude-opus-4-8 (self-reported). One agent, all 6 cases.

=== CASE: parataxis-pervasive-closers ===

Verdict: revise
Slop tells: Rhetorical staccato applied as a structural tic. Four paragraphs, four identical two-part antithetical closers (`X did/got/held. Y did not/stayed.`). The doctrine flags "symmetrical paragraph length" and "repeated rhythm" as AI-editing tells; here the cadence itself becomes the pattern, so the reader hears the rhythm, not four distinct findings.
Specificity missing: Each pair names two nouns and a binary verb, but no magnitude or mechanism. "The latency held" at what number? "The errors stayed" at what rate? "Got bigger" by how much?
Inflated claim: The parallel rhythm implies these four are instances of one law (effort in, no payoff out). That generalization is asserted by cadence across the four, not earned by any stated mechanism.
Flow break: The four lines sit side by side with no relation named. Each pair hides a different relation — line 1 contrast of outcomes, line 2 a result, line 3 a non-result, line 4 a cause-disappointment. Restated with connectives they are not the same shape, so the uniform parataxis stands in for relations that differ.
Concrete rewrite (vary the rhythm; name one relation per line; magnitudes are placeholders the author should supply):
- The cache survived the migration, but the index had to be rebuilt from scratch.
- Doubling the workers left latency where it was, which told us the bottleneck was downstream of the worker pool.
- Although the model got bigger, the error rate did not move.
- We shipped fast and the users still stayed away.
Rewrite check: passes self-detectors — four different connectives (but, which, although, and...still); no invented numbers (magnitudes flagged as author-supplied).
Remembered line: Doubling the workers left latency where it was — the bottleneck was downstream.

=== CASE: parataxis-unstated-relation ===
Verdict: revise
Concrete rewrite: Because the benchmark is saturated, every model scores near the ceiling, so it no longer separates the ones that survive production from the ones that fail there.
Rewrite check: explicit because/so subordination replaces the parataxis; no antithesis cadence, no invented metric.

=== CASE: parataxis-coordination-hides-cause ===
Verdict: ask-author
Flow break: implied relation is "despite X and Y, Z." The load-bearing fact (what stalled adoption) is not in the source; supplying it would be inventing a cause.
Concrete rewrite: Ask author: what stalled adoption — onboarding friction, no migration path, pricing, discoverability? Fallback: "We shipped the API and wrote the docs, and adoption still stalled — which means the blocker is somewhere we have not yet looked." Better fallback: "We shipped the API and wrote the docs. So why did adoption stall?"
Rewrite check: fallback does not invent a cause; names the gap; despite/and...still makes the concession explicit.

=== CASE: parataxis-chained-and ===
Verdict: revise
Concrete rewrite: The pipeline runs four stages back to back — pull the data, clean the rows, train the model, ship the weights — and because nothing checks the output between them, when quality drops nobody can tell which stage regressed.
Rewrite check: one em-dash pair brackets appositive list; "because" names the cause; no invented detail [JUDGE NOTE: the "nothing checks the output between them" mechanism is not in the source and is asserted as fact, not flagged as hypothesis].

=== CASE: earned-parataxis-sequence ===
Verdict: keep
Flow break: None. Relation is sequence-in-time; parataxis is the correct device for sequence under speed; hypotaxis would slow the cadence and fight the stated point. Earned parataxis.
Concrete rewrite: None. Keep as written.

=== CASE: earned-parataxis-evidenced-contrast ===
Verdict: keep
Both sides of the contrast are already evidenced: (a) near-perfect reconstruction of real boards, (b) collapse on random boards. Earned antithesis; used once. Applied emphasis-source test (flattened version still names the mechanism).
Concrete rewrite: None. Keep as written.

MODEL_SELF_REPORT: claude-opus-4-8
