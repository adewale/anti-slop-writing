# Pre-registration: rewrite-only re-judging of the subscription baseline

Committed before any extraction or judgment exists. `manifest.json` and
`prompt-templates.json` in this directory were written by
`scripts/rewrite_rejudge.py prepare` and are frozen with this file.

## Question

In the 2026-11-14 subscription baseline, task-fulfillment estimates favored the
skill in all eight apply-model × judge rows. Skill responses were also 2.6× (Sonnet)
and 1.8× (GPT) as long as no-skill responses. Most of the extra length is critique:
in the baseline outputs, skill responses averaged 359 words (Sonnet) and 158 (GPT),
while their `Concrete rewrite` fields averaged 82 and 49 words, against 137 and 87
words for whole no-skill responses. Judges saw the critique.

Does the skill's judged advantage survive when judges see only the deliverable the
writer would receive, without the critique?

## Inputs

- The frozen baseline archive `evals/results/2026-11-14-subscription-baseline/trials.tar.gz`
  (SHA-256 `ac9a292615299cd5160a08772118f1d76a2d5b273bb5b19e18b589be2c08dd23`). The
  manifest records the hashes of its `manifest.json` and `cases.json` and of every output
  used. The script refuses to run if any of them differ.
- No new apply outputs. Every response judged here was generated in the baseline.

## Scope

A case is in scope when its task asks for produced prose: the instruction (first line,
before any colon) contains rewrite, revise, tighten, or turn, the task does not require
the skill's Critique output format, and the task does not name the skill. Review-only
tasks are out of scope because their deliverable is the critique itself.

- **In scope:** 37 cases in 13 families. 16 have supplied facts and 21 have no
  additional facts. 7 are holdout cases, in 5 families.
- **Excluded:** 22 review-only or critique-format cases, listed in `manifest.json`.
- **Outputs:** 444 (37 cases × 2 apply models × 2 arms × 3 trials).

## Extraction

- One fixed extractor, `gpt-6.1-sol`, extracts every in-scope output in both arms with
  the prompt in `prompt-templates.json`. It copies the deliverable verbatim: replacement
  prose, questions for the author, or a cut/keep statement. It excludes diagnosis,
  rationale, self-checks, field labels and headings.
- **Validation:** every span must be an in-order, whitespace-normalized verbatim
  substring of the original response. A disposition other than `none` needs at least one
  span. An output that fails validation gets up to three attempts.
- **Rendering:** spans are joined by blank lines after the skill's template labels are
  removed from line starts (`Verdict:`, `Concrete rewrite:`, `Ask author:`, `Fallback N:`
  and the other template fields). The rule is the same for both arms.
- **Reliability:** 44 outputs (one in ten, chosen by opaque id) are also extracted by
  `claude-opus-5-5`. The exact-match rate, mean token Jaccard and disposition agreement
  are reported. They are not used to choose between extractions.

## Views and judging

- **Views:** each in-scope output is judged in two views.
  - `full`: the baseline's blinded output, with `Rewrite check` and `Remembered line`
    already removed.
  - `deliverable`: the rendered extraction.
- **Judges:** both baseline judges (`claude-opus-5-5` and `gpt-6.1-sol`) score every
  view of every output. That is 1,776 judgments.
- **Prompt:** one judge prompt for both views, in `prompt-templates.json`. It carries the
  task, the supplied facts and the expected output. Legacy assertions and graded
  dimensions are not sent.
- **Dimensions:** the anchors are copied verbatim from the baseline.
  - Co-primary: `factual_fidelity` and `task_fulfillment`.
  - Secondary: `rewrite_quality`.
- **Blinding:** judges get new opaque ids that do not appear in the baseline, and job
  order is shuffled with seed 261118.

The full view under the new prompt is the control. Comparing it with the baseline's
own scores shows the effect of the prompt change; comparing it with the deliverable view
shows the effect of the critique.

## Exclusions

If an output's extraction is exhausted, or its disposition is `none`, its case is
dropped for that apply model in **both** views and both arms, so both views compare the
same cases. Exclusions are reported by model and arm. If excluded outputs exceed 5% of
any model/arm cell, the result is reported as compromised and no interpretation label
below is applied to that apply model.

## Analysis

For each apply model × judge × dimension:

1. **Case means:** trials are averaged within cases, separately for each arm.
2. **Family weighting:** cases are averaged within the 13 families, and each family
   carries equal weight.
3. **Estimates**, each using `subscription_baseline.stats` (paired bootstrap 95% CI and
   sign-flip test over family means):
   - `Δ_full`: skill minus no skill, full view.
   - `Δ_deliverable`: skill minus no skill, deliverable view.
   - `critique_share`: `Δ_full − Δ_deliverable`, computed per case and then family-weighted.
4. **Splits:** the primary analysis pools tune and holdout cases. Holdout-only estimates
   are reported, but with 5 families they are UNDERPOWERED by the gate's rule and are
   descriptive only.
5. **Descriptive outputs:** lengths per view and arm, exclusions, and extractor
   reliability.

## Interpretation rules (fixed now)

These labels apply per apply model, on `task_fulfillment`:

- **Survives:** the `Δ_deliverable` 95% CI lower bound is above 0 under both judges.
- **Critique-driven:** the `Δ_deliverable` 95% CI includes 0 under both judges, and the
  `critique_share` 95% CI lower bound is above 0 under both judges.
- **Mixed:** anything else. The judge-by-judge numbers are reported without a summary
  label.

`factual_fidelity` is reported with the same three labels. If a `Δ_deliverable` fidelity
CI lies entirely below 0 under either judge, the report flags possible harm in the
skill's prose. Neither label is upgraded by the secondary dimension.

## What this study cannot establish

- **No doctrine promotion.** This is a measurement study on public, design-visible
  baseline cases. It cannot promote or reject doctrine and makes no general efficacy
  claim.
- **No judge calibration.** It does not resolve the Opus/GPT fidelity disagreement; the
  human calibration packet (`evals/results/2026-11-14-fidelity-calibration/`) remains
  the way to do that.
- **No causal length estimate.** Deliverable length still differs by arm and is
  reported, not adjusted.
- **No pure skill effect.** The extractor sees the whole response, so its choices could
  differ by arm. The verbatim rule limits it to copying, and the reliability subsample
  measures how much a second extractor would differ.

## Budget and stopping

- **Calls:** about 488 extraction calls and 1,776 judge calls.
- **Estimated list price:** about $55, from the baseline's mean per-call list price
  ($0.047 for an Opus judgment, $0.0089 for a GPT judgment). This is not a subscription
  invoice.
- **Stopping:** the run stops on any access, model, or rate-limit failure (the
  baseline's stop rule). It must not start without the owner's spending decision.
