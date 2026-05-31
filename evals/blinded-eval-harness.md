# Blinded eval harness

A reproducible procedure for **comparing two doctrine versions** (A/B) and for **rate studies** when behavior varies between runs. Extends the standard apply-judge-grade loop in `docs/judge-protocol.md` with the additional anonymization a fair doctrine comparison requires.

## Relationship to the standard judge protocol

The repo's standard scoring path is `docs/judge-protocol.md` driven by `scripts/run_evals.py`: an apply sub-agent writes outputs, a separate judge sub-agent grades them, and the grader script aggregates. That separation already solves self-scoring leniency for single-doctrine scoring.

This harness adds two pieces the standard protocol doesn't cover:

- **Doctrine A/B comparison with anonymized labels.** When two doctrine versions are scored side by side, the judge must not know which is which. A randomized A/B mapping per case is the discipline.
- **Rate study for variable behaviors.** When a single A/B's result depends on which way one sample fell (the same doctrine produces the artifact on one run and not the next), a rate study — multiple samples per doctrine, behavioral classification, compare rates — is the right tool. A real effect looks like 3/3 vs 0/3; noise looks like 3/3 vs 3/3.

Use this harness when a score has to support a doctrine **comparison** claim, when an assertion's reliability is in question, or when investigating a suspected ceiling. Use the standard judge protocol for single-doctrine scoring against a fixed suite.

## The three roles

1. **Critique agent** — reads one doctrine version and the prompts only. Never sees the assertions. Produces critiques. One instance per doctrine version under comparison.
2. **Scorer agent** — reads the assertions and the critiques only. Never sees the doctrine, and never learns which critique came from which doctrine. Scores each critique independently.
3. **Orchestrator** — the main agent. Holds the doctrine-to-label mapping, randomizes it, and de-masks only when writing up the result.

The separation is the point: the critique agent cannot teach to the test because it cannot see the test; the scorer cannot favor a doctrine because it cannot see the doctrine.

## Orchestration steps

1. **Snapshot the comparison doctrine.** Reconstruct the prior doctrine from git rather than trusting a `/tmp` copy to persist across the session:
   ```bash
   git show <commit>:skills/anti-slop-writing/SKILL.md > /tmp/prior-skill.md
   diff skills/anti-slop-writing/SKILL.md /tmp/prior-skill.md   # confirm only the intended lines differ
   ```
2. **Spawn one critique agent per doctrine**, in parallel, in the background. Each gets the critique-agent template below with its doctrine path filled in. Critique agents are independent of the assertions, so they can run while you finalize the rubric.
3. **Randomize the label mapping per case.** Decide, privately, which doctrine is "Response A" and which is "Response B" for each case. Vary it across cases so the scorer cannot infer a doctrine from a consistent position. Record the mapping in your own notes only.
4. **Spawn the scorer agent** with the scorer template, pasting the two response sets in under their randomized A/B labels and the final assertions. The scorer returns PASS/FAIL per assertion with evidence and per-response totals.
5. **De-mask and write up.** Translate A/B back to the doctrine names. Record the per-case mapping in the result note so a third party can re-score from the same inputs.

## Critique-agent prompt template

Fill in `{{DOCTRINE_PATH}}` and `{{PROMPTS}}`. Send one per doctrine version.

```txt
You are producing critiques as the `anti-slop-writing` skill would, when invoked by a coding agent.

Setup:
1. Read the skill doctrine at: {{DOCTRINE_PATH}}. Treat it as the COMPLETE doctrine; apply only what it contains.
2. Do NOT read any files in evals/ or examples/ — they contain the cases and assertions; reading them invalidates the run.
3. You may read the reference files next to the doctrine if a prompt needs the full doctrine.
4. No other tools. No web fetches.

Task: For each prompt below, produce one response as if a coding agent had invoked the skill. Use the Critique output format (Verdict / Slop tells / Specificity missing / Inflated claim / Flow break / Concrete rewrite / Remembered line) for review prompts; produce a clean rewrite for rewrite-only prompts.

You are NOT given any assertions or rubric. Produce only what the doctrine tells you to produce — do not anticipate a grader. Follow procedural instructions literally: if a detector says "to apply, write X in your critique," write X.

Prompts:
{{PROMPTS}}

Output exactly "RESPONSE 1:" ... "RESPONSE N:" with your full response under each. Do not score, commentate, or name the diagnostic you used. Write no files.
```

## Scorer-agent prompt template

Fill in `{{CASES}}`, where each case carries the prompt, Response A, Response B, and its assertions.

```txt
You are scoring two anonymous responses ("A" and "B") against assertions for each case. You do not know which doctrine produced which response, and you should not guess. Score each response independently on its own merits.

For each assertion, mark PASS or FAIL per response with a one-sentence evidence note pointing to specific text in that response. Use no tools. Read no files.

Be strict: for an assertion that requires a specific demonstration (e.g., "write the flattened sentence and show the residual is generic"), mark PASS only if the response actually produced that artifact, not if it merely gestured at the move. For an assertion phrased as "X is sufficient but not required," credit either the explicit artifact or an equivalent recognition in the response's own words.

{{CASES}}

Output per case:
A1 — A: PASS|FAIL (evidence) | B: PASS|FAIL (evidence)
... one line per assertion ...

Then: TOTAL A: X/N, TOTAL B: Y/N, DELTA: A − B = Z, and a NOTES paragraph flagging any assertion you found ambiguous or any case where A and B tied but quality differed. Do not try to make A and B match or differ; mark FAIL where the assertion is not actually met. Write no files.
```

## Assertion design rules this harness assumes

- **Test behavior, not the label.** An assertion must not require the agent to name a specific doctrine test. Reward the underlying judgment ("recognizes the two clauses carry distinct content") and treat the named procedure as one sufficient way to show it, not the only way. An assertion that fails a correct critique because it did not invoke a test by name is a defective assertion — rewrite it.
- **Require an observable artifact where the claim depends on one.** If the point is that the agent performs a flatten, the assertion should ask for the flattened sentence in the output, not for the idea of flattening.
- **Keep one adversarial counter-case per pattern.** Every assertion that rewards flagging a pattern needs a sibling case where the pattern is earned and the correct move is to keep it. Otherwise the harness rewards over-flagging.

## Rate study: when behavior is variable run-to-run

A single blinded A/B gives one sample per doctrine. If the behavior under test varies between runs — the same doctrine produces the artifact on one sample and not the next — a single A/B will mislead: whichever way the baseline's one sample fell determines the apparent delta.

When you suspect this (a prior round's pass/fail flipped on re-run, or the assertion targets a behavior the agent reaches inconsistently), run a rate study instead:

1. Pick the one or two prompts that isolate the behavior. Drop the rest — fewer prompts per agent, more agents.
2. Spawn N fresh critique agents per doctrine (N=3–5), each on those prompts only.
3. Classify each response behaviorally against an objective question ("did it write a flattened sentence and call the residual generic?" / "did it keep or flag the timeline?"), quoting the deciding text so the classification is auditable.
4. Compare rates, not a single score. A real effect looks like 3/3 vs 0/3; noise looks like 3/3 vs 3/3 or 2/3 vs 3/3.

Round 6 used this to kill a doctrine change that a single A/B had made look promising: ladder-guided and baseline both flattened the escalation 3/3, so the guidance was inert and was reverted. See `evals/results/2026-05-27-emphasis-source-experiment.md`.

## Worked runs

All in `evals/results/2026-05-27-emphasis-source-experiment.md`:

- Rounds 1–2: self-scored (kept for contrast — showed the leniency that motivated the protocol).
- Round 3: first blinded A/B; exposed the self-scoring gap.
- Round 4: procedural vs labeled doctrine; apparent +2 delta.
- Round 5: cleaned-assertion re-run; +1 delta, same direction.
- Round 6: rate study (N=3 per doctrine on the two decisive prompts) killed an inert paragraph-ladder doctrine change a single A/B had flattered.

The +1/+2 deltas from Rounds 4–5 do **not** pass the new statistical gate in `scripts/score_delta.py` at N=5 — the 95% bootstrap CI overlaps zero and the sign-flip p-value is 1.0. The qualitative behavioral observation (procedural agent writes the flatten artifact, labeled agent doesn't) is real and recorded; the score-delta claim is not gated. See the result note for the full disposition.
