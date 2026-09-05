Paragraph under review:

"Rollout gating relies on soft-quorum drains, so tenant-affinity pools never see a partial config. Because the drain completes before the flip, a bad config is caught in staging rather than in production."

## Trial 1

Verdict: revise

Slop tells: The paragraph is lexically clean — no avoid-by-default phrases, no watch-list words, no em-dash cadence, no rule-of-three — and it uses real subordination ("so," "because") instead of parataxis. The tell is structural rather than lexical: the second sentence's "because" asserts a relation the first sentence doesn't actually secure. "Caught in staging rather than in production" is a staccato contrast where neither side is evidenced by what came before — the paragraph never establishes that this drain-and-flip cycle runs in a staging environment at all.

Specificity missing: "Soft-quorum drains" and "tenant-affinity pools" read as specific because they're compound technical nouns, but the paragraph never says what the quorum actually gates on. A quorum that's explicitly "soft" (a partial threshold, not full agreement) is normally a liveness pattern — proceed once most replicas have drained rather than waiting on stragglers — which has nothing to do with validating whether the new config is good or bad. If the softness of the quorum is instead a health vote among draining replicas, the paragraph needs to say so.

Inflated claim: "A bad config is caught in staging rather than in production" claims a detection outcome, but the only mechanism given — the drain finishes before the flip — is a sequencing guarantee (old and new config don't overlap), not a validation step. Sequencing makes the cutover atomic; it doesn't tell you anyone checked the new config was correct before cutting over. The sentence borrows the credibility of "because" without supplying the check that would actually catch a bad config.

Flow break: Sentence 1 establishes an atomicity property (no mixed-config reads). Sentence 2 should cash that out into a consequence of atomicity, but instead pivots to a claim about where validation happens (staging vs. production) — a different property that "drain completes before flip" doesn't establish. The reader is asked to accept a detection claim on the strength of an ordering claim.

Concrete rewrite: "Rollout gating uses soft-quorum drains, so tenant-affinity pools always read either the old config or the new one, never a mix mid-flip. That guarantees a clean cutover — it doesn't by itself say who checks the new config before the flip runs." This keeps the part the source actually supports (atomicity) and cuts the unsupported staging/production detection claim rather than inventing the missing validation step.

Rewrite check: No rule-of-three, no X-not-Y parallelism, no em-dash antithesis, no banned avoid-by-default phrases, no prestige adjectives, no decorative closure, no invented facts — the missing validation mechanism is named as missing, not fabricated. Passes self-detectors.

Remembered line: Ordering isn't validation — the drain-before-flip sequence proves the cutover is atomic, not that anyone checked the new config first.

## Trial 2

Verdict: ask-author

Slop tells: Nothing on the banned list appears, and both sentences subordinate correctly instead of stacking parallel clauses, so this doesn't read as templated AI prose at the sentence level. The tell is that "the flip" arrives with a definite article and no antecedent — the reader has to guess whether it means an in-place config swap or a promotion from a staging environment to production. The paragraph is trading on the confidence of a technical register rather than on stated facts.

Specificity missing: The paragraph needs one fact it doesn't supply: what actually determines that a config is "bad" before the flip happens. Without that, "caught in staging rather than in production" is asserted, not shown. Two genuinely different systems fit the words as written — (a) the drain runs a health/quorum vote on the new config and blocks the flip on failure, or (b) the drain is a plain connection-drain and "staging" refers to an earlier pipeline stage that isn't described here at all — and the sentence means different things depending on which one is true.

Inflated claim: "A bad config is caught in staging rather than in production" implies a validation step exists and reliably runs before production traffic is affected. The source only names an ordering guarantee (drain before flip). Ordering prevents a mixed-state read; it doesn't, on its own, prevent a fully-applied bad config from reaching production, unless something in the drain evaluates correctness. That something is never named.

Flow break: Sentence 1's claim (no partial-config reads) is about consistency during the transition. Sentence 2 changes the subject to detection and environment (staging vs. production) with no hinge connecting "no partial reads" to "validated before production." The two sentences sound continuous because of "because," but they're answering different questions.

Concrete rewrite: Ask author: does the soft-quorum drain itself evaluate the new config's health, so a failed quorum blocks the flip — or is "staging" a separate pipeline stage upstream of this mechanism, where the same drain-and-flip logic runs first? Name the check that fails on a bad config. Fallback: if no such check exists yet, cut the second sentence and end on the atomicity claim alone — "tenant-affinity pools never see a partial config" is fully supported without it.

Rewrite check: The ask-author question names what's missing without inventing an answer; the fallback cuts rather than fabricates a mechanism, count, or name. No rule-of-three, no X-not-Y, no em-dash antithesis, no banned phrases, no invented facts. Passes self-detectors.

Remembered line: The paragraph earns "pools never see a partial config." It hasn't yet earned "caught in staging rather than in production" — that sentence is still waiting on a fact.

## Trial 3

Verdict: revise

Slop tells: No banned words or phrases, and the paragraph avoids parataxis in favor of "so" / "because" — structurally this looks like what the skill asks for. The problem is a claim/evidence mismatch inside the first sentence that the confident cadence papers over.

Specificity missing: "Soft-quorum" names a threshold that is explicitly partial, not full agreement — that's what "soft" is doing there. The sentence then claims an absolute: tenant-affinity pools "never" see a partial config. If completion only requires a soft quorum of replicas to finish draining, the remaining replicas are, by definition, allowed to still be mid-drain when the flip fires. The paragraph doesn't explain why traffic to those still-draining replicas can't observe a partial config — it just asserts "never" one clause after choosing a word, "soft," that describes exactly that gap.

Inflated claim: "Never" is doing more work than "soft-quorum" can support. Either the quorum threshold is high enough in practice that the residual risk is negligible — a fact the paragraph could state, such as a percentage or a timeout bound — or "never" should be scoped down. As written, the absolute reads as confidence borrowed from the sentence's certainty, not from the mechanism named.

Flow break: This is a within-sentence break rather than a between-sentence one: the qualifier ("soft") and the guarantee ("never") point in opposite directions, so a careful reader has to stop and resolve the tension the sentence itself introduces, before even reaching the staging/production claim in sentence 2.

Concrete rewrite: "Rollout gating waits for a soft quorum of replicas to drain before flipping, so most tenant-affinity pools never see a partial config — the exception is a pool pinned to a straggler still draining when the flip fires." This keeps "soft-quorum" and "never" both in play but scopes the guarantee to match the threshold the source actually named, instead of letting "never" overwrite "soft."

Rewrite check: No rule-of-three, no negative-parallelism template, no em-dash antithesis, no banned avoid-by-default phrases, no prestige adjectives, no decorative closure. No invented count or name — the straggler exception is a logical consequence of "soft quorum," not a fabricated new fact. Passes self-detectors.

Remembered line: "Soft" already told you "never" wasn't going to hold for every pool.

## Trial 4

Verdict: keep

Slop tells: None of the avoid-by-default phrases or watch-list words appear, there's no em-dash cadence, no rule-of-three, no hedged symmetry, and both sentences subordinate correctly ("so," "because") instead of stacking parallel clauses. Read as internal engineering shorthand rather than public-facing copy, this is closer to the target register than to the failure modes the skill lists.

Specificity missing: "Soft-quorum drains," "tenant-affinity pools," and "the flip" are precise enough for the audience this is written for. A quorum is a vote; "soft" names the threshold as partial-agreement rather than unanimous, which for a reader who already knows this rollout system reads as "the drain gates on replica health, not just on 100% completion" — that's the detail that makes "never see a partial config" and "caught in staging" cohere. Spelling out the vote mechanism in full would expand earned compression into explanation the intended reader doesn't need.

Inflated claim: None found. "Never" matches the guarantee a quorum gate is meant to provide (block the flip until enough replicas confirm), and "caught in staging rather than in production" follows if — as "rollout gating" implies — this same drain-and-flip step runs in staging ahead of the production promotion. Nothing here reaches for significance beyond what the two named mechanisms (quorum-gated drain, ordered flip) support.

Flow break: None. Sentence 1 states the consistency property; sentence 2 states the consequence for where a failure surfaces. The second sentence answers the question the first raises — never see a partial config, so what happens to a bad one? — rather than sitting beside it.

Concrete rewrite: Not needed. If anything, one clause of insurance would help a reader outside this system: naming what the drain checks (for example, "soft-quorum drains — enough replicas confirm the new config is healthy before the flip fires") would remove any doubt that "soft quorum" is a health gate and not just a straggler-tolerant liveness threshold. That's an optional addition, not a rewrite.

Rewrite check: passes self-detectors. No rewrite was made; the optional addition above introduces no banned phrase, no rule-of-three, and no invented count or name — "enough replicas" restates what "quorum" already means rather than adding a new fact.

Remembered line: "The drain completes before the flip" is already the memorable, load-bearing clause — the one fact in the paragraph that does real mechanical work.
