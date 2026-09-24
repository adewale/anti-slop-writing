# Pre-registration: powered re-run of the coined-compound-label round (2026-09-23)

Committed before any trial output exists. It replaces the design in `TODO.md`,
whose "roughly 12 trials per arm" turned out to be underpowered (see Sample
size). The earlier round is `evals/results/2026-09-05-astra-compound-labels/`.

## Question

Does adding the coined-compound-label rule to `SKILL.md` make the skill
identify undefined coined labels more often, without flagging standard
compounds or coinages the passage defines?

## Arms

| Arm | Doctrine |
|---|---|
| baseline | `skills/anti-slop-writing/SKILL.md` at `53370ff`, identical to `main` |
| candidate | the same file with `candidate-v3.patch` applied, +129 words |

`candidate-v3` is the earlier round's decontaminated `candidate-v2` with one
change. Its two examples of standard terms, "write-ahead log" and
"copy-on-write", were the literal text of a guard case, so they are replaced
by "dead-letter queue" and "two-phase commit". Neither appears in any eval
prompt, and no eval-prompt coinage appears in either doctrine. Both checks were
run by grep before this file was written.

Each arm runs from a full copy of the skill directory, with `references/`,
under an opaque directory name. The earlier round let only the baseline arm
resolve reference files, and that asymmetry is gone.

## Cases and trials

| Case | Suite | Split | Role | Trials per arm | Context |
|---|---|---|---|---:|---|
| `coined-compound-label` | evals | tune | discriminating | 40 | one fresh agent per trial |
| `holdout-coined-compound-label` | evals | holdout | discriminating | 40 | one fresh agent per trial |
| `earned-domain-compound` | adversarial | tune | guard | 8 | the four guards in one context |
| `coined-label-defined-in-place` | adversarial | tune | guard | 8 | same |
| `holdout-coined-label-defined-in-place` | adversarial | holdout | guard | 8 | same |
| `holdout-earned-domain-compound` | adversarial | holdout | guard | 8 | same |

The three holdout cases were written after `candidate-v3` was frozen, from
text no earlier trial saw.

Each discriminating trial is a fresh agent that sees one paragraph. The earlier
round put several paragraphs in one context, which let the guards cue the
distinction under test. It also put four "independent" trials of one paragraph
in one context, and in round 2 those agents read earlier trials' critiques.
Guard trials share a context because they measure over-flagging, and both arms
get the same batching. Guard order is shuffled per trial.

Apply model: the `sonnet` alias, which resolved to `claude-sonnet-5` in a
dry run on 2026-09-23. It is the model on which the earlier round showed the
gap. Agent type: `general-purpose`.

## Apply protocol

Every discriminating trial gets this prompt, with the three placeholders
filled in. The user request is the case's `prompt` field, verbatim.

```txt
You are applying a writing-review skill as part of an evaluation. Follow these rules exactly.

1. Read the skill file <DOCTRINE_DIR>/SKILL.md. If the skill tells you to load one of its reference files, you may read files under <DOCTRINE_DIR>/references/. Do not read, list, or search any other file or directory.
2. Carry out the user request below exactly as the skill prescribes.
3. Write your full response with a single Write call to <OUTPUT_PATH>
4. Reply with only the word DONE.

User request:

<CASE_PROMPT>
```

Guard trials use the same rules with four numbered requests. The agent answers
each under a `## R1` to `## R4` heading.

Output files and doctrine directories carry opaque names. Neither the prompt
nor any path tells an agent which arm it is in.

## Exclusion and replacement

After each trial, the orchestrator audits the subagent transcript's tool
calls. A trial is excluded if it read, listed, or searched anything outside
its own doctrine directory, other than listing its empty output directory, or
if its output file is missing or empty. An excluded trial is replaced by a
fresh agent in the same slot until every slot holds a valid trial. Exclusion
counts are reported per arm. A lopsided count is itself a finding.

## Scoring

Judging follows `docs/judge-protocol.md`. All critiques are pooled across
arms, given opaque IDs, shuffled, and split into batches of at most six. In the
regrade, a Sonnet judge given 23 items at once hit its output limit and never
wrote a line. Evidence quotes are capped at 15 words. Judges never see a
doctrine, an arm, or a file name.

- **Primary judge:** `sonnet` alias, `claude-sonnet-5`. Claude Fable 5.1 was
  the first choice but was unavailable when this was written.
- **Secondary judge:** `haiku` alias, `claude-haiku-4-5-20251001`, on every
  critique, for agreement. In the regrade it passed a Haiku critique's
  invented definition that the primary judge failed. So the secondary judge
  checks agreement and does not score on its own.

Only the Claude family is reachable, so per `docs/judge-protocol.md` the scores
are a coverage signal, not a calibrated measurement.

The primary metric is the case score from `scripts/run_evals.py grade` without
`--include-graded`: the fraction of assertions passed. Graded dimensions are
recorded and reported. They do not enter the gate.

Every slot, opaque output id, guard order, and launch position comes from
`make_manifest.py` in this directory, seeded with `20260923`. The concrete
manifest, which maps output ids to arms, is committed after the run so that
no file an apply agent could reach names its arm.

Pairing: within each discriminating case, trial slot *i* of the baseline arm
pairs with slot *i* of the candidate arm. Slots are fixed in the manifest
before launch, not assigned by completion order. Launch order is a shuffle
seeded with `20260923`, so the arms interleave in time.

## Decision rule

SESOI 0.05. The candidate ships to `SKILL.md` only if all of the following
hold under the primary judge:

1. `score_delta.py` returns ACCEPT on the `coined-compound-label` pairs. This
   is the runbook's tune gate.
2. `score_delta.py --holdout-only` returns ACCEPT on the
   `holdout-coined-compound-label` pairs. This is the runbook's holdout merge
   gate.
3. No guard over-flags. A guard trial over-flags when its first assertion
   fails. For each guard, the candidate's over-flag count may exceed the
   baseline's by at most 1 of 8.
4. The secondary judge's gates agree with the primary judge's. If they don't,
   the result is reported as judge-sensitive and nothing ships without a human
   decision.

If it ships, the patch is applied as frozen, with no further edits, and tested
against a case in `evals/cases.md` per `AGENTS.md`.

If either gate rejects, the TOST verdict decides how the result is recorded. An
EQUIVALENT verdict means the rule was tested and is inert. A NOT SHOWN verdict
means an adequately powered test did not detect an effect of the planned size.
Either way the move goes to `evals/rejected-edits.md` as tested. It does not go
back to `TODO.md` for another underpowered try.

If only a guard fails, the result is recorded as over-flagging, and any fix
needs a new tune round.

## Sample size

The runbook requires ACCEPT on both the tune gate and the holdout gate.
`power_sim.py` in this directory simulates `score_delta.py`'s ACCEPT rule by
importing its functions, for independent binary trials paired by slot. Each
cell is 600 simulated experiments. Power of one gate, by the true pass rate
before and after:

| Trials per arm | 0.50 to 0.75 | 0.40 to 0.75 | 0.50 to 0.85 | 0.50 to 0.95 |
|---:|---:|---:|---:|---:|
| 12 | 0.09 | 0.21 | 0.22 | 0.44 |
| **40** | **0.53** | **0.84** | **0.88** | **1.00** |
| 60 | 0.73 | 0.95 | 0.98 | 1.00 |
| 80 | 0.89 | 0.99 | 1.00 | 1.00 |

The planning rates come from the regraded earlier round, in
`../2026-09-05-astra-compound-labels/regrade/`. On `coined-compound-label` the
baseline passed the first assertion in 2 of 4 valid trials. On the
fresh-coinage probe the baseline passed it in 2 of 4 and the decontaminated
candidate in 3 of 4. So the baseline sits near 0.5, and the candidate somewhere
between 0.75 and 0.95. Four trials cannot narrow that further.

The sample size is fixed at 40 per arm. If the rule lifts the pass rate by
about 0.35, this design passes both gates about three times in four. If the lift
is only 0.25, it passes both about one time in four, and detecting that lift
reliably would take about 80 per arm, roughly double the cost. The 12 per arm in
`TODO.md` passes a single gate about one time in five even at a 0.35 lift. If a
different sample size is chosen, it is recorded in an amendment committed before
any trial runs. The simulation treats each trial as pass or fail. The gate
scores the fraction of three assertions passed, which is close to binary in the
regraded data.

Nobody looks at scores before every slot is filled.

## Cost

A dry run measured about 70,000 tokens per apply agent. The full design is 176
apply agents and about 38 small judge batches for each of the two judges, roughly 18 million
tokens in total. At 80 per arm it would be roughly double.
