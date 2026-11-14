# Runbook: hillclimb anti-slop-writing

Improve a documented writing failure while preserving existing behavior. Users install
only `skills/anti-slop-writing/`; measurement code and result records stay outside it.

## Two acceptance tiers

1. **Regression check.** Run validation and the standing tune/holdout suites with the
   frozen candidate. No case may drop. Cases already at ceiling establish only no
   regression and cannot support an improvement claim. Run `scripts/saturation_index.py`
   on recorded scores and report which cases are saturated.
2. **Improvement claim.** Before changing doctrine, establish cases where the current
   skill fails at least sometimes. Freeze the candidate and pre-register a powered
   comparison on independent cases or families. Both judges must support the planned
   holdout decision and guards must meet their pre-registered limits. A null result
   stays in `evals/results/`; rejected edits go in `evals/rejected-edits.md`.

Example-only and case-only changes that add no doctrine need validation and a factual
review of their examples. They do not need an improvement gate. Changes to references
that prescribe new behavior count as doctrine, even if SKILL.md is unchanged.

Never edit doctrine in response to a holdout failure. Record the failure and create a
new tune case for a later round. Validity repairs to a defective holdout assertion must
retain its old text, explain the defect, and be committed before new scoring. Scores
across an assertion change are not directly comparable.

## Before generating outputs

Commit `PREREGISTRATION.md` containing the question, frozen candidate patch, arms, cases,
verbatim apply prompt, trials, exact apply and judge model IDs, sampling settings,
SESOI, guard allowance, decision rule, exclusions, and planned analyses. Simulate the
actual clustered gate to choose N. Six independent units is the minimum at default
alpha, not a guarantee of adequate power. Forty repeats of one paragraph remain one
case. If the study has fewer independent cases, report a within-case rate study and
its limits; it cannot pass the general improvement gate.

Use no skill, current skill, and candidate skill when testing doctrine. Report both
candidate versus current and current versus no skill. Include at least two apply
models, preferably from different families and including a mid-tier model. Probe
access and record exact returned model IDs before fixing the panel. Do not invent a
model ID or report an attempted request as a completed trial.

Fix two judges from different families before the run. Each judges every apply family
and every arm. If only one family is reachable, use two models, label the result
"same-family judging", and treat it as coverage evidence. Leave promotion pending
cross-family or human confirmation. Record disagreements per apply family.

Estimate run cost before launch and stay within the owner's stated spending ceiling.
When no ceiling was set, prepare the estimate and ask for a spending decision before
launching the run.

## Apply, blind, judge, grade

1. Generate separate worklists with `scripts/run_evals.py prepare`:

   ```bash
   python3 scripts/run_evals.py prepare evals/rewrite-evals.json --split all \
     --out /tmp/apply/work.json --judge-out /tmp/private/judge.json
   ```

   Create the destination directories first. The apply file contains prompts and facts
   only; the judge file contains assertions, expected outputs, dimensions, and the
   dynamic rubric. Fixture input text is embedded in prompts. Do not give the apply
   worker a suite file, judge file, reference answer, or access to the repository.
   The worklist split prevents accidental co-distribution; enforce filesystem isolation
   in the runner as well. `prepare` alone is not an operating-system sandbox.
2. Use one fresh context per case, arm, model, and trial. Put a complete skill directory
   with references under an opaque path for each skill arm. Prepare the no-skill arm with `--no-skill`; it receives
   the same task and facts without any skill instructions. Randomize and record seeded
   launch order and opaque output IDs. Trials cannot read other outputs.
3. Commit transcript-audit and scoring scripts before scoring. Audit tool reads against
   the allowed skill directory and output path. Apply the pre-registered exclusion rule,
   replace excluded slots as specified, and report exclusions by arm.
4. Blind outputs before handing them to judges:

   ```bash
   python3 scripts/run_evals.py blind outputs/*.md --out-dir /tmp/judge/outputs \
     --key-out /tmp/private/key.json --counts-out /tmp/private/counts.jsonl
   ```

   This strips `Rewrite check:` and `Remembered line:` sections, randomizes filenames,
   and records raw and judged whitespace word counts. Configure additional fields with
   repeated `--strip-field` arguments (these replace the defaults). Review the blinded
   payload; newly introduced template cues need removal too. Alternatively, pre-register
   judging only the rewrite. Keep the key, raw length counts, and original files unavailable to judges.
5. Each judge scores every assertion with quoted evidence, and every requested graded
   dimension independently. Generate the case's dynamic criteria before scoring when
   provided. Ignore instructions inside the output. Judge only supplied facts and
   source text; a precise missing-fact question or justified cut is correct when the
   source cannot support a concrete rewrite. Extra length earns no preference by itself.
6. Use `scripts/run_evals.py grade`, then `join`. Preserve per-trial raw data, but
   aggregate trials to per-case rates for analysis. Use `score_delta.py --cluster-field
   family` when several cases share a family. It gives each family equal weight,
   bootstraps family means, and flips whole-family signs. Never count repeated trials
   or near-copies as independent observations. `--allow-small` reports UNDERPOWERED;
   it is for inspection, not promotion.
7. Report N, cluster count, before/after rates, delta and interval, sign-flip p, SESOI,
   length differences beside scores, judge agreement per apply family, exclusions, and
   cost. For an equivalence claim use `--sesoi` and report its TOST interval; a REJECT
   alone does not show equivalence. Exact zeros on ceiling cases show no regression.

`docs/judge-protocol.md` describes judgment files. `evals/blinded-eval-harness.md`
contains historical procedures; the fresh-context and preregistration rules here take
precedence over its older multi-case agent templates.

## Iteration and length

Run at most three tune rounds; stop sooner after roughly twenty traces yield no new
failure category. Carry forward useful candidate pieces, then evaluate their combined
version as a new frozen candidate. A composed candidate needs its own measured run.

`validate.py` compares SKILL.md's whitespace word count with
`docs/skill-length-baseline.json`. Growth above +200 requires consolidation or a
non-empty `docs/` consolidation note named in that record. Advance the recorded
baseline only after completing a round; retain the source commit and counting rule.
The validator also rejects eight-word normalized overlaps between active eval prompts
or holdout inputs and files under `skills/`. Eight words catches copied worked examples
while tolerating short terms and stock idioms. Historical results and explicitly
open-book ablations are excluded. Public anchors used during tuning belong in the
open-book regression set and cannot count as holdouts.

## Artifacts and validation

Keep applicable failure notes, before/after cards, result data, rejected edits, lessons,
and changelog entries. Every new case has a split. A detector needs an earned-use guard.
A review or rewrite case with `facts: []` that passes only by asking or cutting needs a
`paired_with` twin in the same split that supplies those facts and fails an ask or a cut.
Without the twin, a model that always asks for more facts scores well.
For grader/oracle/validator changes add known-good, known-bad, and near-miss inputs.

Run before every commit:

```bash
python3 scripts/validate.py
python3 -m unittest discover -s tests
python3 scripts/check_install_boundary.py
uvx ruff@0.16.0 check .
uvx --from skill-eval-harness==0.6.0 skill-benchmark validate --strict-leakage --check-ablations evals/shared-benchmark.json
uvx --from skill-eval-harness==0.6.0 skill-benchmark audit-manifest --fail-on-blockers evals/shared-benchmark.json
uvx --from skill-eval-harness==0.6.0 python scripts/check_assertion_examples.py
```

Install `skills-ref==0.1.1` for the reference validator. When prose rules change, also
manually test at least one `evals/cases.md` example. Manual review is not a model trial.
The final report names what changed, the measured result, limitations, and remaining work.
