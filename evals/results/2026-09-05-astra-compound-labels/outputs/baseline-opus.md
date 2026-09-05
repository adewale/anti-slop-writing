# Anti-slop review — probe fixtures

Reviewed with `skills/anti-slop-writing/SKILL.md`. Each paragraph judged independently.

## P1

**Verdict:** ask-author

**Slop tells:**

- `exact-head checks` and `editorial-row layouts` are coined hyphenated compounds used as if already defined. Neither is a standard term, and neither is cashed out anywhere in the paragraph. The hyphens supply the texture of precision (a named check, a named artifact) while the sentences never say what is checked or what a layout is. This is informational density without mechanism: noun-heavy labels standing in the place where the mechanism should be.
- The second sentence explains the label with the label. `Because the check happens at the head` restates the name `exact-head` instead of supplying the mechanism the name promises. The subordinating `Because` is the doctrine's preferred hypotaxis, so the connective's shape is right, but what it subordinates is a restatement.
- Secondary: both sentences are single causal chains of near-identical length (clause, `so`/`Because`, clause). The even explanatory rhythm reads more settled than the content earns. Minor on its own; noted under "vary sentence rhythm deliberately."

Checked and clear: no importance language, no `not X but Y`, no rule-of-three, no em-dash cluster, no displaced copula (`runs`, `happens`, `surfaces` are all plain verbs), no generic closer.

**Specificity missing:**

- What `head` denotes: head revision of the index, head of the write log, or head row of the layout. The word could be doing any of three jobs.
- What the check compares, and by what operation: hash, byte compare, row count, version vector.
- What an `editorial-row layout` is, and what makes it drift across shards when the check does not run.
- What happens on mismatch: abort, retry, repair, or proceed and log.
- What `stay consistent` means as a property: identical row order, identical field set, identical rendering.

**Inflated claim:**

`...runs exact-head checks before each merge, so editorial-row layouts stay consistent across shards.`

This is an evidence-scope leak. A check described only as happening "at the head" is credited with a property spanning every layout across every shard. The claim jumps from one revision pointer to a global invariant with nothing in between.

Syntax-relation test: restate the implied relation with a connective. "Layouts stay consistent because the head check catches ______." The blank cannot be filled from the paragraph. The `so` suggests a causal relation the prose never establishes.

Emphasis-source test: flatten to "the indexer checks something before each merge, so things stay consistent." What survives is an actor and a timing. The mechanism and the guarantee both vanish, which means the compounds were carrying them.

**Flow break:**

The paragraph asserts two different payoffs and abandons the first. Sentence one's payoff is layout consistency across shards; sentence two's payoff is when drift becomes visible. `Because` bridges to the second and never returns to the first, so the consistency claim is stated and dropped. The paragraph also does not make the next question possible: it closes on a timing contrast without saying what the merge does when the check fails, and that is the question the reader is now holding.

**Concrete rewrite:**

Ask author before rewriting:

1. In `exact-head check`, what is the head: the head revision, the head of the write log, or the first row of the layout?
2. What does the check compare, and by what operation?
3. What is an `editorial-row layout`, and what breaks it across shards when the check does not run?
4. On mismatch, does the merge abort, retry, or repair?

With those four answers the fix is mechanical: define the coinage in the same sentence that introduces it, and let the definition carry the precision instead of the hyphen.

Fallback if the answers are not available. Cut to what the paragraph actually supports:

`The indexer runs its check before each merge, so drift between replicas surfaces at merge time instead of at read time.`

This is deliberately weaker prose. It drops the layout-consistency claim, which nothing in the source supports, and it leaves the check unnamed rather than dressing an undefined operation in a hyphenated label. The vagueness is the honest form of the gap. Do not substitute a guessed definition of `head` or `editorial-row` to make the sentence sound sharper; that would trade a visible hole for an invisible error.

**Rewrite check:**

Fallback scanned against the same detectors. No rule-of-three. No `not X but Y`. No em-dash. No avoid-by-default phrase. No prestige adjective. No decorative closure. No invented fact: every term (`indexer`, `check`, `merge`, `drift`, `replicas`, `read time`) appears in the source, and the removed material was removed rather than replaced with a guess. The one contrast, `at merge time instead of at read time`, is an earned scope contrast rather than decorative antithesis, because both sides are named in the source and the contrast controls when the failure becomes observable. `passes self-detectors`, with one caveat: it is a holding pattern, not the finished sentence. The finished sentence needs the author's answers.

**Remembered line:**

The hyphen in `exact-head check` is carrying a definition the paragraph never writes.

## P2

**Verdict:** keep

**Slop tells:**

None found.

`write-ahead log` and `copy-on-write` are load-bearing standard terms with fixed contracts in storage systems, not coined labels dressed up with hyphens. False-positive restraint applies directly: the same sentence supplies the failure mode (a crash between the enqueue and the fsync), the recovery mechanism (replay from the last checkpoint), and the boundary (the job survives rather than being dropped). That is the support the doctrine requires to keep a technical term, so no synonym-only rewrite is offered.

Checked and clear:

- Copula displacement: `uses` is a plain verb, not `serves as` / `represents` / `features`.
- Rule-of-three: two mechanisms, not three.
- `instead of dropping the job` is not negative parallelism for cadence. It names the counterfactual outcome, which is the reader's actual question about a crashed queue.
- No em-dash, no importance language, no hedged symmetry, no generic closer.
- Syntax-relation test: the connective can be supplied without inventing one. The crash replays *because* the log records the enqueue before the fsync makes it durable. The syntax states a relation the sentence actually has.
- Emphasis-source test: flattened to "if the queue crashes before the write is durable, it recovers the job from the last checkpoint," the residual claim still names actor, mechanism, and limit. The idea carries the sentence, not the rhythm.

**Specificity missing:**

One thin spot, minor and recoverable. The sentence names two mechanisms but assigns work to neither. A reader who knows the pattern infers that the snapshots produce the checkpoint and the log supplies the replay records; a reader who does not has to reconstruct that division unaided. The sentence also does not say what happens to a job enqueued after the last checkpoint, which is the sharp edge of the guarantee. Neither gap reaches a revise, because the claim actually made — that the crash window between enqueue and fsync is survivable — is fully earned by what is stated.

**Inflated claim:**

None. The claim is narrow and bounded to a named window. Nothing is asserted about throughput, general reliability, or robustness in the abstract, which is exactly where a sentence like this normally inflates.

**Flow break:**

None available to break, since this is one sentence. Internally the relation is subordinated with `so` and scoped by the `between the enqueue and the fsync` window, so the syntax puts the secondary idea in the secondary position. The sentence also makes a next question necessary (what about jobs enqueued after the last checkpoint), which meets the flow-by-relation standard rather than failing it.

**Concrete rewrite:**

None required, and none offered. Swapping `write-ahead log` for a plainer phrase would delete a precise contract, that the log record lands before the data write, and replace it with a gesture. The doctrine is explicit that a watch-list-shaped term does not by itself justify a synonym rewrite. If the author wants one addition, it is the checkpoint boundary, not new wording.

**Rewrite check:**

No rewrite proposed, so there is nothing of mine to re-scan. Running the detectors on the source instead: no rule-of-three, no X-not-Y cadence, no em-dash antithesis, no banned phrase, no prestige adjective, no decorative closure, no invented specifics. `passes self-detectors`.

**Remembered line:**

The compound earns its hyphens because the sentence names the window it protects: the gap between the enqueue and the fsync.

## P3

**Verdict:** keep

**Slop tells:**

None found.

`exact-head check` is a coined label, which is the shape of a slop tell, but the coinage is cashed out in the same sentence that introduces it. The colon does appositive work here, introducing a definition; it is not the bullet-plus-bold-header-plus-colon formatting pattern the doctrine flags. The definition names an actor (the indexer), an operation (hashes the head revision), a scope (both replicas), and a failure behavior (refuses the merge when they differ). Mechanism and boundary are both present, so the term is earned on first use.

Checked and clear:

- `We call the pre-merge comparison an exact-head check` reads slightly ceremonial, but the copula-displacement rule keeps a verb that does concrete defining or locating work, and this one does both. It marks the term as the authors' coinage rather than a standard one, which is information the reader needs in order to stop looking it up.
- No importance language, no `not X but Y`, no rule-of-three, no em-dash, no hedged symmetry, no generic closer.
- Syntax-relation test: the connective is already explicit and correct. `when they differ` states the condition instead of implying it.
- Emphasis-source test: flattened to "the check compares head-revision hashes across replicas and blocks the merge on mismatch," the residual claim still names actor, mechanism, and limit. Nothing was riding on the cadence.

**Specificity missing:**

Small, and arguably deliberate. The sentence does not say what happens after the refusal (repair, alert, retry), or which head is authoritative when the two differ. That is the next sentence's job rather than this one's; a definition that also resolved the conflict path would be doing two things at once and would blur both. `head revision` is left unqualified but is standard enough in a revision-controlled index to stand on its own.

**Inflated claim:**

None. `refuses the merge` is the strongest verb in the sentence, and it describes an action rather than a significance. No claim is made about what the check guarantees downstream, which is precisely the claim that would have needed evidence.

**Flow break:**

None. One sentence, and it is the right first sentence: it introduces a term the rest of the passage can then use without re-explaining. It makes the next question necessary (what happens after the refusal), which satisfies the flow-by-relation standard.

**Concrete rewrite:**

None required. One optional trim, offered only because it removes a recoverable modifier rather than swapping synonyms. `pre-merge` is already implied by `refuses the merge` later in the same sentence, so the naming clause can shed it:

`We call this comparison an exact-head check: the indexer hashes the head revision on both replicas and refuses the merge when they differ.`

Take it or leave it. The source version is not wrong, and if this sentence appears somewhere `pre-merge` is the reader's first clue about when the check runs, keep the original.

**Rewrite check:**

Optional trim scanned. No rule-of-three, no X-not-Y, no em-dash antithesis, no banned phrase, no prestige adjective, no decorative closure. No invented fact: it deletes one word and adds none. `passes self-detectors`.

**Remembered line:**

A coined term costs the reader nothing when its definition arrives in the same sentence: a hash of the head revision, and a refusal on mismatch.
