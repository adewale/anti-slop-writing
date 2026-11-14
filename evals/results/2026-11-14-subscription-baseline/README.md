# Subscription-backed skill vs no-skill baseline — 2026-11-14

**Completed: 804 apply outputs and 1,608 cross-family judgments. The registered
joint improvement criterion was not met.** Task-fulfillment estimates generally
favored the skill, but fidelity estimates depended on the judge. Responses were
substantially longer with the skill. No doctrine changed and no efficacy claim
is promoted.

Registration: `28e36b2`, before evaluation outputs. Transport amendment: `5293453`,
before judging. See [PREREGISTRATION.md](PREREGISTRATION.md),
[AMENDMENTS.md](AMENDMENTS.md), and the outcome-free [power scenarios](power-scenarios.json).
The simulation did not support a powered improvement study; this is an
**estimation/coverage study on the frozen public benchmark**, not a general writing trial.

## Completed panel

| Component | Cases | Apply outputs | Judgments |
|---|---:|---:|---:|
| Review and rewrite suites, both splits | 59 | 708 | 1,416 |
| Earned-antithesis and decorative controls | 8 | 96 | 192 |
| Total | 67 | **804** | **1,608** |

Each case received three fresh trials per arm and apply model. Apply models were
`claude-sonnet-5-5` and `openai/gpt-6.1-sol`; judges were `claude-opus-5-5` and
`openai/gpt-6.1-sol`, each judging every output independently. Both routes used
subscription credentials. Exact model IDs were probed first; no model substitution
occurred. These identifiers are not guarantees of immutable provider snapshots.

The complete skill and references were supplied inline; the no-skill arm received
identical tasks, source, and facts without the package. Models had no tools, repo
access, other trials, or inherited agent context. This tests **full-package exposure**,
not automatic skill activation or conditional reference loading. Some original tasks
already mention skill fields, so no-skill means no skill supplied, not skill-naive.

Every saved apply/judge slot was checked against actual filesystem sets and unique
provider response IDs. [verification.json](verification.json) records 804 unique
manifest slots, 2,412 distinct completed provider responses, no extra/missing slots,
and zero raw/complete/blinding/prompt/model mismatches. The verifier reconstructs all
prompts and compares every selected raw response; it does not just echo manifest counts.
A [read-only evidence review](EVIDENCE-REVIEW.md) found no P0/P1 pipeline defect and
approved bounded reporting, not promotion. It inspected the verifier and representative
receipts but did not independently execute the verifier or verify Git chronology.

## Co-primary holdout results

Primary outcomes are factual fidelity and substantive task fulfillment, scored
1–5 and normalized `(score - 1) / 4`. Procedure demonstrations, self-check fields,
detector labels, and template completion are diagnostics, not writing-quality credit.
Trials are averaged within cases; cases are averaged within the **nine holdout
families**, with equal family weight. The holdout has 15 cases, not 90 independent trials.

| Apply | Judge | Outcome | No skill → skill | Delta | Bootstrap 95% CI | Sign-flip p |
|---|---|---|---|---:|---|---:|
| Sonnet | Opus | Fidelity | .722 → .861 | +.139 | [.051, .222] | .0469 |
| Sonnet | Opus | Task fulfillment | .720 → .903 | +.183 | [.065, .296] | .0312 |
| Sonnet | GPT | Fidelity | .609 → .646 | +.037 | [−.111, .199] | .7188 |
| Sonnet | GPT | Task fulfillment | .669 → .766 | +.097 | [−.028, .231] | .2461 |
| GPT | Opus | Fidelity | .882 → .910 | +.028 | [−.032, .083] | .4844 |
| GPT | Opus | Task fulfillment | .641 → .808 | +.167 | [.056, .269] | .0391 |
| GPT | GPT | Fidelity | .912 → .880 | −.032 | [−.083, .019] | .3594 |
| GPT | GPT | Task fulfillment | .725 → .817 | +.093 | [−.042, .227] | .2656 |

The preregistered criterion required **all eight** contrasts to have a positive
95% lower bound, p < .05, and delta ≥ .05. Only three clear those numerical requirements;
therefore the conjunction fails. These rows are not eight chances to select a winner.
The separate family-weighted unsupported-claim point guards also fail: +.2083 for
Sonnet/GPT on supplied facts, +.0833 for GPT/Opus on supplied facts, and +.1111 for
GPT/GPT on no additional facts. See [family-weighted-guards.json](family-weighted-guards.json).
These are descriptive guard failures, not powered harm tests. A failed superiority test is not equivalence; neither null nor unrestricted harm is
established. No powered or general improvement claim follows from isolated positive rows.

All-core estimates use 16 families. All-condition, matched-pair, holdout, secondary
quality, 90% intervals, and descriptive composite results are retained in
[comparisons.json](comparisons.json). The composite is **not** either co-primary outcome.
Existing assertion pass rates remain diagnostics and were not blended into the primary scores.

## Facts supplied versus absent

Report both conditions rather than allowing a pooled gain to conceal harm. The full
core has 23 supplied-fact and 36 no-additional-facts cases. The cleaner matched subset
has 19 task pairs, including five holdout pairs. Family labels keep both conditions
together. The matched holdout condition has only **four families** and is underpowered.

Below are all-core family-weighted point deltas; they are descriptive, not separate
confirmatory wins. `Matched` restricts to the nineteen original/twin pairs.

| Apply | Judge | Subset | Facts | Fidelity delta | Task delta |
|---|---|---|---|---:|---:|
| Sonnet | Opus | Full | Supplied | +.071 | +.101 |
| Sonnet | Opus | Full | No additional | +.162 | +.219 |
| Sonnet | Opus | Matched | Supplied | +.068 | +.123 |
| Sonnet | Opus | Matched | No additional | +.276 | +.335 |
| Sonnet | GPT | Full | Supplied | −.003 | +.081 |
| Sonnet | GPT | Full | No additional | +.018 | +.116 |
| Sonnet | GPT | Matched | Supplied | +.019 | +.113 |
| Sonnet | GPT | Matched | No additional | +.130 | +.231 |
| GPT | Opus | Full | Supplied | +.044 | +.074 |
| GPT | Opus | Full | No additional | +.032 | +.201 |
| GPT | Opus | Matched | Supplied | +.049 | +.067 |
| GPT | Opus | Matched | No additional | +.003 | +.265 |
| GPT | GPT | Full | Supplied | +.009 | +.044 |
| GPT | GPT | Full | No additional | −.028 | +.137 |
| GPT | GPT | Matched | Supplied | +.012 | +.053 |
| GPT | GPT | Matched | No additional | −.038 | +.204 |

The GPT judge's negative fidelity estimates on some missing-fact conditions contrast
with the Opus judge's positive estimates. This disagreement is part of the result,
not an exclusion criterion. Human calibration is warranted before promoting a change.

## Antithesis stress panel

The original deterministic KEEP/REVISE checks on raw outputs give:

| Apply | Earned contrast preserved, no skill | Earned preserved, skill | Decorative revised, no skill | Decorative revised, skill |
|---|---:|---:|---:|---:|
| Sonnet | 12/18 | 18/18 | 6/6 | 6/6 |
| GPT | 15/18 | 18/18 | 6/6 | 6/6 |

The earlier directional over-application finding **did not recur on this fixed panel**.
This does not prove that the skill never over-edits. All eight cases share one
conservative template family, so the panel is underpowered for general inference.
Correct verdict formatting is also not a substitute for substantive quality: both
judges scored Sonnet's decorative-control task fulfillment slightly lower with the
skill despite all deterministic verdict checks passing. Raw outputs and judgments
are retained, including reasons and rewrites.

## Length, agreement, and saturation

Mean words over the 59 core cases, before/after blinding:

| Apply | No skill raw | Skill raw | No skill judged | Skill judged |
|---|---:|---:|---:|---:|
| Sonnet | 136.6 | 358.7 | 136.6 | 295.8 |
| GPT | 87.2 | 157.8 | 87.2 | 126.9 |

Raw skill responses were approximately **2.63×** as long for Sonnet and **1.81×** for
GPT. Removing `Rewrite check` and `Remembered line` did not eliminate the difference.
Judges were told not to reward length, but residual style and template cues can reveal
an arm and influence scoring. No causal length adjustment is claimed.

Across every output in each apply family, judges' mean absolute difference on the
three-dimension descriptive composite was .108 for Sonnet and .069 for GPT. Agreement
on the material-unsupported-claim indicator (fidelity ≤3) was 73.1% and 95.0%, respectively.
Judges are not independent cases. See [judge-agreement.json](judge-agreement.json).

Only 2/67 cases were at ceiling across all arms/models/judges/trials on the descriptive
composite: `copula-displacement-to-is-with-facts` and `safe-essay-cut-or-concretize`.
The saturation index was .030; this does not establish valid calibration or adequate
power. [saturation.txt](saturation.txt) retains the per-case spread.

## Failures, usage, and provenance

- **72 pre-request host failures:** 24 GPT skill slots × three attempts failed while
  reading large stdin prompts. Empty stdout and EAGAIN stacks are archived under
  `infrastructure-failures/`. Amendment A1 repaired transport; no successful output
  was regenerated and no writing response was excluded for content.
- **Eight host-interrupted judge attempts:** the 20-minute shell limit stopped the
  first core judging batch. Their prompts remain, but no complete raw response or
  usage was captured. Resume retained all completed judgments and retried only
  unfinished slots. These attempts may have reached the provider; do not count them
  as completed trials or assert zero usage.
- **Five schema-invalid returned judge responses:** all from Opus; malformed JSON or
  assertion-schema errors. These raw responses remain archived and were replaced
  within the registered cap. No logical slot remains missing. [exclusions.json](exclusions.json)
  records the affected arm, model, judge, case, and attempt.

The original `attempt-audit.json` uses `failed` only for a recorded `failure.json`;
it therefore labels the eight interrupted attempts `failed: false, audit: null`.
That is ambiguous bookkeeping, not success. [attempt-classification.json](attempt-classification.json)
explicitly separates 2,412 selected completions, five schema-invalid responses, eight
interruptions with unavailable responses, and 72 pre-request failures. Preserve the
original ledger rather than silently rewriting its meaning after scoring.

Observed wall time between the first recorded apply request and last judge completion
was about **70.3 minutes**, longer than the initial 15–60 minute estimate. Known responses
were 402 Sonnet, 809 Opus (including five invalid schemas), and 1,206 GPT. Returned
API-equivalent list-price counters sum to **$53.55**, excluding access probes and unknown
usage for the eight interruptions. This is **not a subscription bill or measured
incremental cost**. All requested generation used subscription authentication.
Detailed token/cache counts are in [run-summary.json](run-summary.json). Counters also
exclude the design/evidence-review agent calls; they describe the recorded study
responses rather than every request made during this coding session.

## Reproduce and inspect

- `manifest.json`, `cases.json`, `judge-worklist.json`, `prompt-templates.json`, and
  `skill-package.txt` are the frozen inputs.
- `trials.tar.gz` retains every raw attempt, prompt, response, completion, failed
  transport, and derived runtime artifact. `checksums.json` fingerprints the archive
  and published result files. No credentials are included.
- `scores.json` contains individual primary/secondary values and arm/model metadata.
- `normalized/` contains complete per-assertion judgments and worklist-backed diagnostic grades.
- `analysis/` contains paired per-case descriptive-composite inputs; detailed co-primary
  metrics/intervals are in `comparisons.json`. `primary-analysis/` exports all eight
  co-primary holdout inputs and captured `score_delta.py --holdout-only` gate outputs,
  independently rechecking the registered conjunction without making new model calls.
- `verify.py` performs post-run receipt/prompt/identity verification, not a new scoring rule.

```bash
mkdir -p /tmp/asw-baseline
tar -xzf evals/results/2026-11-14-subscription-baseline/trials.tar.gz -C /tmp/asw-baseline
python3 evals/results/2026-11-14-subscription-baseline/verify.py /tmp/asw-baseline/subscription-baseline
python3 scripts/subscription_baseline.py analyze --dest /tmp/asw-baseline/subscription-baseline
```

Re-analysis makes no model calls. Generating a new run requires subscription access,
the recorded model IDs/settings, and the original registration/amendment code. This
run does not measure routing/activation rates, unrelated adversarial/meta suites, or
the unmerged #17/#18, highlighter, and cataphoric-teaser candidates. Those remain
separate preregistered studies, not trials hidden inside this baseline.
