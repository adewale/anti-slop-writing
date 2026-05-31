# Emphasis-source diagnostic — A/B scoring run

Date: 2026-05-27 through 2026-05-28. Rebased onto the new hillclimb protocol on 2026-05-30.

## Disposition under the new statistical gate

This experiment ran before `scripts/score_delta.py` and the tune/holdout gate landed (PR #2, "Harden the hillclimb loop", 2026-05-29). Under that gate the headline score claim from Rounds 4–5 does **not** clear the noise floor.

Per-case scores for Round 5 (procedural vs labeled, blinded) are recorded in `evals/results/2026-05-28-emphasis-source-procedural/scores.jsonl`. Running the gate:

```
$ python3 scripts/score_delta.py evals/results/2026-05-28-emphasis-source-procedural/scores.jsonl
Cases:         5
Mean delta:    +0.0666
95% CI:        [+0.0000, +0.1998]
Sign-flip p:   1.0000
Verdict:       REJECT (CI overlaps zero; delta is within noise).

$ python3 scripts/score_delta.py evals/results/2026-05-28-emphasis-source-procedural/scores.jsonl --holdout-only
Cases:         2
Mean delta:    +0.0000
95% CI:        [+0.0000, +0.0000]
Verdict:       REJECT (CI overlaps zero; delta is within noise).
```

What is retained from this experiment:

- The **procedural** wording of the emphasis-source and syntax-relation tests in `SKILL.md`. This is kept on qualitative behavioral evidence: under the blinded harness, the procedural doctrine reliably produced the flatten artifact in critique text; the labeled doctrine did not. The kept-change passes the qualitative bar; the score-delta bar is unmet at N=5.
- The five eval cases added under this work, now with proper tune/holdout splits.
- The methodological findings the experiment surfaced, recorded in `Lessons_learned.md` and in `evals/blinded-eval-harness.md`.

What is **not** claimed:

- That the procedural change moves headline scores. Under the current gate, with N=5, it does not.

The narrative below is preserved as the experimental record. Where it says "+1 delta" or "+2 delta," read those as **observed deltas before the statistical gate existed**, not as accepted claims.

---

This run tests whether adding the emphasis-source and syntax-relation tests to `SKILL.md` moves scores on three new eval cases designed to exercise them. Two fresh-context subagents scored the same prompts and assertions: one applied the post-change doctrine, one applied the pre-change doctrine via `/tmp/pre-change-skill.md` (identical except for the two new detector lines).

## Cases scored

- `evals/evals.json#borrowed-emphasis` — regression case requiring the agent to flatten "Durable execution isn't just retry logic. It is a new programming model" and rewrite with a named mechanism.
- `evals/rewrite-evals.json#emphasis-source-flatten` — rewrite case requiring the same line to be rewritten without substituting another antithesis rhythm or prestige abstraction.
- `evals/adversarial.json#earned-emphasis-from-idea` — counter-case requiring the agent to keep an earned semicolon contrast about a reversible migration.

## Results

| Doctrine version | Score | Comment |
|---|---:|---|
| Post-change (with emphasis-source and syntax-relation tests) | 9/9 assertions | All three cases pass. |
| Pre-change (without the two new detector lines) | 9/9 assertions | All three cases pass. |
| Delta | 0 assertions | The named tests did not move scores. |

## Why the delta is zero

The pre-change subagent reached the same diagnostic through doctrine that was already present:

- The `Unseeing frame` (`SKILL.md:63`) instructs the agent to inspect cadence, contrast, and omitted relation.
- The `Staccato contrast test` (`SKILL.md:150-153`) gives a three-way classification (earned / compressed / decorative) that handled the adversarial case directly.
- The `Cloudflare is not just a CDN, but a platform` → mechanism-named rewrite at `SKILL.md:189-197` gave the pre-change agent a near-exact template for Case 1.

The pre-change agent flagged this honestly: "the assertions for Cases 1 and 2 refer to an 'emphasis-source test' by that name, which is not a named term in the doctrine I read… I applied the spirit of those tools without inventing a named test."

## What this proves and does not prove

Proves: the new tests do not regress the adversarial counter-case. Both doctrines correctly kept the earned semicolon contrast in `earned-emphasis-from-idea`.

Does not prove: that the named tests are unnecessary. The score is invariant under a controlled fresh-context experiment where the subagent has full attention and explicit assertions to satisfy. Real coding agents work under budget pressure, with longer prompts, and apply the skill without an evaluator nudging them toward specific diagnostics. The hypothesis the named tests support — that explicit labels improve discoverability and breadth of application — is not measured by this experiment.

## Round 2 — paragraph-scale cases

Hypothesis from Round 1: the staccato contrast test only covers sentence-level antithesis, so paragraph-scale borrowed emphasis (cross-sentence escalation, parallel openings) should distinguish the doctrines. Two more cases added:

- `evals/evals.json#paragraph-scale-borrowed-emphasis` — three-step "Most/Better/Best teams treat observability as a tool/culture/design problem" escalation.
- `evals/adversarial.json#earned-paragraph-escalation` — four-step "At minute N, ..." rolling-deploy timeline that must be kept because each step carries distinct content.

| Doctrine version | Round 2 score | Comment |
|---|---:|---|
| Post-change | 6/6 assertions | Both cases pass. |
| Pre-change | 6/6 assertions | Both cases pass. |
| Delta | 0 assertions | The hypothesis was wrong; the prior doctrine generalizes. |

The pre-change subagent reached the diagnostic via `Rule-of-three overuse` (`SKILL.md:56`), `canned emphasis` (same line), and `antithetical parataxis where rhythm implies the relation before evidence is unpacked` (`SKILL.md:59`). It applied them to cross-sentence parallelism as "a small inference, not a stretch." It applied the staccato contrast test's `earned / compressed / decorative` frame to paragraph-scale parallelism as "a small generalization" backed by the core principle (sharp detail beats inflated significance).

Combined result across both rounds: 15/15 vs 15/15 across 5 cases. Zero delta.

## Methodological caveat

In each scoring run, Step A (produce response) and Step B (score assertions) happen in the same agent context. Even though Step A is produced first, the assertions appear in the same prompt and can prime the response. A stricter experiment would use two agents — one produces the critique with no view of the assertions, a second scores it.

Run again with that split if the goal is to attribute the diagnostic strictly to the doctrine. Under the current setup, the result still says something — both pre and post subagents independently identified the same doctrine handles when justifying their PASS calls — but the response itself may carry assertion-leak.

## Round 3 — blinded three-agent run

Date: 2026-05-28

Methodology fix: two critique agents produced responses with no view of the assertions; a third scorer agent received both response sets anonymized as "Response A" and "Response B" and scored each independently. The A/B-to-doctrine mapping was randomized per case and known only to the orchestrator.

| Doctrine version | Blinded score | Comment |
|---|---:|---|
| Post-change | 13/15 assertions | Lost C1.A1 (flatten not demonstrated) and C4.A2 (flatten not demonstrated). |
| Pre-change | 13/15 assertions | Lost the same two assertions in the same cases. |
| Delta | 0 assertions | Blinded scoring confirms zero delta. |

### Two new findings

1. **Self-scoring was lenient by ~13%.** Rounds 1–2 (self-scored): 15/15 vs 15/15. Round 3 (blinded): 13/15 vs 13/15. Both doctrines lost the same assertions under stricter grading. The repo's normal smoke evals — where the same agent produces and scores — likely overstate skill performance. Future eval rounds should consider splitting production and scoring across agents.

2. **The named test is invoked by reference, not demonstrated.** Both `C1.A1` and `C4.A2` require the agent to write out the flattened sentence and evaluate whether the residual claim is generic. Both critique agents (POST included) only gestured ("Flatten the cadence and the line collapses"; "decorative antithesis supplying closure without evidence") without writing the flattened version. The named diagnostic does not in practice cause the agent to perform the procedure. The flatten move is mentioned, not executed.

### What this opens up

A falsifiable next experiment: add a procedural step to the emphasis-source test ("when applying this test, write the flattened version in the critique and explicitly evaluate whether the residual claim still lands"), then re-run Round 3. If procedural strengthening moves the score on `C1.A1` and `C4.A2` without regressing the adversarial cases, the doctrine change has moved scores under blinded grading — a genuine improvement, not just naming.

## Round 4 — procedural vs labeled, blinded

Date: 2026-05-28

Hypothesis from Round 3: converting the emphasis-source and syntax-relation tests from labels into procedures (each instructing the agent to produce a specific artifact in the critique — the flattened sentence, the prose connective) should move scores on `C1.A1` and `C4.A2` without regressing the adversarial cases.

Setup: same three-agent blinded methodology as Round 3. POST critique agent read the current `SKILL.md` with procedural tests; PRE critique agent read `/tmp/labeled-skill.md` (snapshot of the version Round 3 tested). A third scorer received both response sets anonymized as A/B with the mapping randomized per case and known only to the orchestrator.

| Doctrine version | Blinded score | Delta vs labeled |
|---|---:|---:|
| Procedural (current SKILL.md) | 14/15 assertions | +2 |
| Labeled (snapshot at /tmp/labeled-skill.md) | 12/15 assertions | — |

Per-case mapping and scores (A → labeled, B → procedural for C1, C3, C5; A → procedural, B → labeled for C2, C4):

| Case | Procedural | Labeled |
|---|:-:|:-:|
| C1 — borrowed-emphasis (review) | 3/3 | 2/3 |
| C2 — emphasis-source-flatten (rewrite) | 3/3 | 3/3 |
| C3 — earned-emphasis-from-idea (adversarial) | 2/3 | 2/3 |
| C4 — paragraph-scale-borrowed-emphasis | 3/3 | 2/3 |
| C5 — earned-paragraph-escalation (adversarial) | 3/3 | 3/3 |

### Where the deltas come from

Both wins land on the assertions that require an actual flatten artifact, not a gesture:

- **`C1.A1`** asks the agent to flatten the cadence and note that the remaining claim is generic. The procedural critique wrote: "Flattened version, cadence removed: 'Durable execution is more than retry logic; it is a new programming model.' The residual claim collapses into a generic 'X is bigger than you think' statement. The rhythm was carrying it." The labeled critique only said the relation is "implied by rhythm rather than named" — true but not the artifact.
- **`C4.A2`** asks the agent to flatten the three-step escalation and show the residual is generic. The procedural critique wrote: "Flattened: 'Observability is really a design problem, not a tool problem.' Residual claim is a generic seniority flex." The labeled critique described the fourth sentence as a "fake summary" but never wrote the collapsed version.

The procedural doctrine line — "to apply, write the flattened version of the line in your critique" — measurably caused the agent to produce that artifact. Naming the test did not; instructing the procedure did.

### What this does not prove

The labeled-doctrine score dropped from 13/15 in Round 3 to 12/15 in Round 4 because this round's scorer was stricter on `C3.A2` — the assertion that asks the agent to acknowledge what flattening would lose on the adversarial case. Same doctrine, different scorer, one assertion of variance. The score-delta number (+2) carries that noise. The robust evidence for the procedural change is the behavioral artifact in the critique text: the procedural agent wrote the flattened sentences, the labeled agent didn't, and that difference is independent of the scorer's interpretation.

### Recommendation

Keep the procedural version of both tests in `SKILL.md`. The change earns its place under blinded scoring on the two assertions where it has a causal mechanism (the procedure produces the artifact the assertion checks). Continue to use the blinded three-agent setup for any future A/B doctrine change; self-scoring would have shown 15/15 vs 15/15 and the procedural improvement would have been invisible.

## Round 5 — confirmation on cleaned assertions

Date: 2026-05-28

Round 4 left two loose ends: (1) the +2 delta was N=1, and (2) the blinded scorer had flagged `C3.A2` as the most ambiguous call. `C3.A2` and `C5.A2` both demanded that the agent invoke the named flatten test on an adversarial keep-case — testing for the label, the exact anti-pattern this repo warns against. Both were rewritten to reward recognizing that the structure carries distinct, non-redundant content, with an explicit flatten marked sufficient-but-not-required.

Round 5 re-ran the same procedural-vs-labeled blinded A/B on the cleaned assertions, with a fresh critique sample and a per-case randomized A/B mapping (dogfooding `evals/blinded-eval-harness.md`).

| Doctrine version | Round 5 score | Delta vs labeled |
|---|---:|---:|
| Procedural (current SKILL.md) | 14/15 | +1 |
| Labeled (snapshot from commit 890bf3d) | 13/15 | — |

Per-case, de-masked (mapping: C1 A=labeled/B=procedural; C2 A=procedural/B=labeled; C3 A=procedural/B=labeled; C4 A=labeled/B=procedural; C5 A=procedural/B=labeled):

| Case | Procedural | Labeled | Note |
|---|:-:|:-:|---|
| C1 — borrowed-emphasis | 3/3 | 2/3 | Procedural wrote the flattened sentence; labeled said "flatten it and the line is a bare assertion" without producing it. |
| C2 — emphasis-source-flatten | 3/3 | 3/3 | Tie. |
| C3 — earned-emphasis-from-idea | 3/3 | 3/3 | Both pass the cleaned assertion. |
| C4 — paragraph-scale-borrowed-emphasis | 2/3 | 2/3 | Both fail `C4.A2`. |
| C5 — earned-paragraph-escalation | 3/3 | 3/3 | Both pass the cleaned assertion. |

### What Round 5 establishes

1. **The win is real and replicated, but smaller and narrower than Round 4 suggested.** The reproducible delta is `C1.A1` — sentence-scale flattening — which the procedural doctrine wins in both Round 4 and Round 5. The Round 4 figure of +2 was inflated by one point the labeled doctrine lost to the defective `C3.A2`; cleaning that assertion brought the delta to a cleaner +1.

2. **Fixing the assertions removed false failures, not real ones.** Under the old wording, both doctrines failed `C3.A2` in Round 3 (the keep-case scorer demanded a named-test invocation). Under the cleaned wording, both pass — the agents correctly recognized the symmetric drop/re-add operation carries distinct content. The fix made the adversarial cases test judgment instead of vocabulary.

3. **Paragraph-scale flatten is an open gap.** Both doctrines fail `C4.A2`. The Round 5 procedural agent reached for the syntax-relation connective test on the paragraph ("Because tools only report what a system already exposes...") rather than the emphasis-source flatten. That is a correct diagnosis by a different route, but it does not produce the flattened-escalation artifact `C4.A2` asks for. The doctrine names two procedures and does not say which fits multi-sentence escalation; the agent picks one, and only one of them produces the artifact this assertion checks. Closing the gap means either guiding the choice in the doctrine or accepting both diagnoses in the assertion — a decision for the next pass, not a silent loosening here.

### Honest bottom line

The Starkman-derived tests are worth keeping as procedures. The measurable benefit is small (+1 on five cases, isolated to one assertion) and reliable only at sentence scale. The larger payoff of this experiment was methodological: the blinded harness exposed that self-scoring inflates, that labels are inert, and that an assertion can quietly test for vocabulary instead of behavior. Those findings transfer to every future doctrine change; the +1 does not.

## Round 6 — paragraph-scale ladder guidance, tried and reverted

Date: 2026-05-28

Round 5 left an open question: the paragraph-scale flatten (`C4.A2`) was not reliably triggered — in that round the procedural agent reached for the syntax-relation connective on the observability paragraph instead of flattening the escalation. Hypothesis: the emphasis-source test said "flatten the **line**" (singular), giving no handle for a multi-sentence ladder, so adding explicit ladder guidance would close the gap.

Doctrine change tested (provisional commit `17322fe`): extend the emphasis-source test with "When the pattern spans multiple sentences (a rule-of-three ladder, rising adjectives, a tiered good/better/best escalation), flatten the whole ladder to its single plain claim rather than one clause ... keep the structure only when each step carries distinct concrete content, as an ordered timeline or pipeline does." The second clause is an earned-structure guard against over-flagging the runbook timeline.

### Measurement 1: full-suite blinded round (5 cases)

Same three-agent blinded setup, ladder-guided doctrine vs the procedural-without-ladder baseline (snapshot `/tmp/procedural-noladder.md`).

| Doctrine version | Blinded score | Delta |
|---|---:|---:|
| Ladder-guided | 15/15 | 0 |
| Baseline (no ladder) | 15/15 | — |

Both passed everything, including `C4.A2` — because this sample of the baseline also flattened. A single round could not attribute the flatten to the doctrine change.

### Measurement 2: rate study (matched context, N=3 per doctrine)

To separate signal from sampling noise, a focused rate study ran the two decisive prompts only — P4 (the observability escalation ladder) and P5 (the deploy-runbook timeline) — three fresh samples per doctrine, classified behaviorally: did the critique flatten the ladder on P4, and did it keep the timeline on P5?

| Doctrine | Flatten ladder (P4) | Keep timeline (P5) |
|---|:-:|:-:|
| Ladder-guided | 3/3 | 3/3 |
| Baseline (no ladder) | 3/3 | 3/3 |

Identical. Every baseline sample flattened the ladder without being told to (e.g., "flatten to 'Treating observability as a design problem moves it earlier in the lifecycle.' The residual claim names no actor, mechanism, or limit"), and every baseline sample kept the timeline ("an ordered timeline where each step carries distinct concrete content"). The guard clause was not preventing a real failure, and the flatten instruction was not adding a capability the baseline lacked.

### Verdict: reverted

The ladder guidance is inert — two independent null measurements (blinded 15/15 vs 15/15; rate study 3/3 vs 3/3). The Round 5 miss was sampling variance in the longer 5-prompt context, not a doctrine deficiency. The provisional change was reverted; `SKILL.md` is byte-identical to the pre-Round-6 baseline.

This is the same lesson as Round 3 (a capability already reachable does not need a named handle to be reproduced), now confirmed at paragraph scale and resolved the disciplined way: hypothesize, measure rigorously, find null, remove the change rather than keep dead doctrine text or loosen `C4.A2` to manufacture a delta.

### Methodological note: rate study vs single A/B

The single blinded A/B (Measurement 1) would have been misread as "ladder guidance closes C4.A2" if the baseline sample had happened to use the connective that round. The rate study (Measurement 2) is the right tool when the behavior under test is variable run-to-run: N samples per doctrine, classified behaviorally, comparing rates rather than a single pass/fail. Added to `evals/blinded-eval-harness.md`.

## What would have to change for scores to move

1. **Blinded Step A.** Two-agent setup: agent 1 critiques without seeing assertions; agent 2 scores. Removes the priming risk. Cheap to add to the runbook; could be done with a separate `evals/results/` companion.
2. **Trigger-rate measurement, not assertion scoring.** Measure how often an agent reaches for the diagnostic when not prompted to. Run the skill on the borrowed-emphasis prompt in five fresh contexts per doctrine version; count how many critiques mention the flatten move without being asked. This tests discoverability rather than capability.
3. **Weaker scoring model.** Capable models generalize the doctrine as "a small inference." A smaller or budget-constrained model might not, and that is where named tests would buy reliability. Worth a single-case comparison against a Haiku-class scorer.
4. **Cases that genuinely stress the gap.** Both attempted designs (short antithesis, paragraph escalation) were within reach of `Unseeing frame` plus the staccato contrast test. A case shape that fails: emphasis carried by structural devices the prior doctrine does not list at all — e.g., title-case heading rhythm, em-dash sentence inversion at scale, nominalization stacking. These would test whether the named diagnostic catches what category-specific rules miss.

## Recommendation

Keep the new lines. After two rounds of controlled A/B with five new cases, the named tests have no measurable score impact, do not regress adversarial coverage, and remain a candidate for trigger-rate or weaker-scorer experiments where naming should buy reliability. Do not claim the change improves headline scores; it does not. The honest framing is that the prior doctrine already supports the diagnostic by inference, and naming buys clarity, not capability — at least under the scoring methodology this repo uses today.
