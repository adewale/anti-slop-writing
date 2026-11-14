# Subscription baseline preregistration — 2026-11-14

Status at registration: **no evaluation outputs generated**. Access probes and synthetic
software/power fixtures only. The Git commit containing this registration freezes the
study before generation. This is an **estimation/coverage baseline**, not a powered
doctrine-promotion experiment. The owner requested the model evals and authorized
subscription use without a cost concern in the current session.

## Question, models, and arms

Does the current complete skill package improve source-grounded writing/review over
no skill supplied, on these existing public benchmark tasks?

- Apply: `claude-sonnet-5-5` via Claude Code 2.1.323 (mid-tier Claude); `openai/gpt-6.1-sol`
  via Pi 1.4.0 ModelRuntime. Both passed exact-ID subscription access probes.
- Judge: `claude-opus-5-5` and `openai/gpt-6.1-sol`, each grading every apply family and arm.
  Access responses are in `access/final-*`. The SDK reports `gpt-6.1-sol`; no immutable
  backend snapshot ID is exposed. Claude reports canonical model IDs in modelUsage.
- Arms: identical case task/source/facts, without skill vs with the complete frozen
  `skills/anti-slop-writing/` package. No candidate doctrine and no new writing rule.
- Claude uses safe mode, no tools, no slash commands/skills, no settings/MCP servers,
  a neutral replacement system prompt, and no session persistence. API-key/bearer-token
  environment overrides are removed so the existing Max login is used.
- OpenAI uses the low-level ModelRuntime completion API, not an agent session. It asserts
  subscription auth before calling and has no tools, resource discovery, extensions,
  project instructions, or prior messages. The installed Codex CLI 0.145.0 rejected
  three model IDs; those failed probes are not trials. The successful SDK route is
  fixed before registration, not a fallback within the experiment.
- Reasoning effort: low for apply, medium for judges. Claude sampling/output limits
  otherwise use CLI/provider defaults (no temperature/seed controls exposed here).
  OpenAI also uses provider-default sampling; requested output cap 10,000 tokens.
  Random seeds control allocation/bootstrap, not server-side token sampling.

## Frozen artifacts and delivery

`frozen-sources.json` hashes the source scripts, suites, fixture inputs, and installed
skill Markdown files. `cases.json` contains the exact 67 selected cases with embedded
fixture source and facts. `skill-package.txt` is the full skill and all references.
`prompt-templates.json` records verbatim apply wrappers and the primary rubric;
substitute the frozen task and package literally. `judge-worklist.json` is the frozen
coverage contract. No suite, assertion, expected answer, or reference rewrite is sent
to an apply model.

The skill is supplied inline in one request, including all reference files, rather
than allowing conditional file reads. This bounds the estimand to **full-package
instruction exposure**, not live skill activation or conditional-reference behavior.
Each request is a fresh tool-free model context. CLI requests run in unique empty
OS temporary directories; SDK calls never create an agent or expose a filesystem tool.
Models cannot read the repo, sibling trials, keys, or judgment artifacts because they
have no tools. The host process retains those files, but does not send them. This is
capability isolation of the model, not a general-purpose OS sandbox of the host CLI.

The apply wrapper includes the task's explicit output constraints in both arms. The
skill arm additionally says to apply the package. Some existing tasks name the skill
or its output fields; they remain verbatim. Thus no-skill means **no skill supplied**,
not necessarily a skill-naive task. No holdout facts, assertions, or doctrine changed.
PR #26 is not merged: at the owner's request, this baseline runs on its locally
committed repaired instrument before merge; it does not authorize merging the PR.

## Allocation, dependence, and resource decision

- 26 review + 33 rewrite cases = 59 core cases: 44 tune, 15 holdout; 36 have no additional
  facts, 23 supply facts. Nineteen paired tasks have both conditions; five are holdout.
- Add the six `neg-earned-antithesis-*` and two `pos-decorative-antithesis-*` cases only.
- Exactly three fresh trials per case × two arms × two apply models: **804 outputs**.
  Two independent fresh-context judges per output: **1,608 judgments**, **2,412 logical
  calls**, excluding access probes and replacements. No judges share conversation state.
- `manifest.json` fixes opaque output IDs, slots, trial counts, and seeded shuffled
  allocation (`261114`). Stage-specific seeded submission order is deterministic;
  actual concurrency/arrival order and durations are recorded. Maximum eight concurrent
  calls, balanced by the random schedule. No automatic model substitution.
- Core family labels in `cases.json` are fixed: 16 mechanism/source families, including
  nine represented in holdout. The nineteen pairs remain intact within families.
  Examples: all borrowed-emphasis variants share one family; the nominalization/copula
  tasks share one; repeated product-tour and parataxis tasks each share a family.
- All eight antithesis cases form **one conservative family**. Report six earned cases
  and two decorative controls separately. Different nouns in a shared scaffold are
  not eight independent replications. The stress panel cannot pass the six-family gate.

`power-scenarios.json` records 500 outcome-free simulations per scenario/allocation,
using ordinal scores, correlated contrasts, exact family sign flips, 10,000 bootstrap
resamples, and the eight-contrast conjunction. At three trials, simulated joint success
was 1.6% in the declared central (+0.10 latent effect) scenario and 23.8% in the large
(+0.15) scenario. Even ten trials did not reach the 80% target in any tested scenario.
These assumptions are not pilot data or forecasts. Therefore use the minimum three
trials for estimation/coverage; **do not advertise this as a powered improvement study**.
More repeats cannot add independent families. Pair-restricted holdout condition reports
have only four families and are underpowered regardless of trial count.

Resource estimate: roughly 4–8 million total input/output tokens, depending on response
length, about 15–60 minutes with eight workers and provider load. Calls are routed to
subscriptions, not separately authorized API-key billing. A loose API-equivalent list
price estimate is $30–$150, **not a subscription invoice**. Record returned usage and
list-price counters; do not claim actual billing was measured. Stop at authentication,
usage-limit, or model-change failures rather than changing providers or bypassing limits.

## Outcomes and blinding

Before judging, symmetrically strip `Rewrite check` and `Remembered line` sections using
the frozen `strip_template_fields` function. Preserve raw and judged word counts and
original text privately. Judge payloads contain the task/source/facts and one blinded
response under an opaque ID, without arm identity, apply model identity, skill package,
original filenames, key, or length counters. This removes direct labels but cannot
prevent a judge inferring an arm from stylistic/template remnants; disclose that limit.

Two **co-primary outcomes**, independently scored 1–5 and normalized `(score - 1) / 4`:

1. Factual fidelity: support, epistemic qualifications, provenance, absence of invention.
2. Substantive task fulfillment: completes the supported review/rewrite, uses supplied
   facts, preserves earned material, and asks precisely or cuts only when facts require it.

The exact anchors are frozen in `PRIMARY` and `prompt-templates.json`. A necessary
question, justified cut, or earned keep can receive full marks. A fluent invented
rewrite cannot. Named self-checks, flattening demonstrations, connective demonstrations,
detector vocabulary, exact verdict formatting, or other template compliance earn no
primary credit. Judges must produce primary scores first and use quoted evidence or
identify an omission. A missing source is not repaired by invented specific details.

Secondary outcomes: rewrite-quality 1–5, material unsupported-claim rate (fidelity ≤3),
raw/judged length, and an equally weighted mean of the three normalized dimensions
(descriptive composite only). Existing assertions, graded dimensions, and dynamic
criteria are collected **as diagnostics**, never blended into co-primary inference.
Both tracks share a judge request for tractability; primary-first instructions and
separate arithmetic do not eliminate all rubric priming. Dynamic criteria must be
three to five non-empty case-specific criteria. Generated criteria are retained but
not treated as independent outcomes. Antithesis also receives the existing deterministic
regex/not-regex checks on raw outputs, reported separately from substantive judgments.

## Analysis, guards, and interpretation

Analyze every judge and apply model separately; do not average away disagreement.
Average the three trials within case/arm; compute skill-minus-no-skill differences;
average cases within the frozen family; weight families equally. The two fact
conditions stay together for pooled inference. Report equal-case means descriptively,
clearly distinguished from the family-weighted inferential means.

For each co-primary outcome report before/after means, delta, paired-bootstrap 95% CI,
two-sided family sign-flip p, cases/families, and SESOI 0.05. Use 10,000 bootstrap and
permutation iterations, seed 261114; exact sign flips at ≤16 families, matching
`score_delta.py`. Report 90% intervals against ±0.05 as an optional numerical
equivalence diagnostic; a failed superiority test is not equivalence.

A confirmatory benchmark gain would require **all eight** core-holdout contrasts
(two outcomes × two judges × two apply models) to have positive 95% lower bounds,
p < .05, and point estimate ≥.05. This conjunction is not eight chances to select a
winner. In addition, every judge/model must show no >.05 point-estimate increase in
unsupported claims and no >.05 normalized rewrite-quality loss in either fact
condition. These point guards are not powered non-inferiority tests. Regardless of
numerical success, the power limitation means no doctrine promotion or unrestricted
writing-efficacy claim is authorized by this study.

Report: all-core and holdout; supplied and no-additional-facts separately; the cleaner
19-pair subset separately by condition; antithesis earned preservation and decorative
correction separately; judge disagreement per apply family; saturation/ceiling cases;
failed calls/replacements by arm; model IDs, usage, duration, and limitations. Preserve
all raw trial data. Public, historically inspected holdouts are not fresh unseen data.
No doctrine will be edited in response to this run.

## Exclusions, retries, audit, and stopping

Exclude only transport/auth errors, timeout (>240 seconds host or >180 seconds SDK),
incomplete result, wrong model, any tool call, empty response, or schema-invalid judge
output. Do not exclude bad writing, harmless noncompliance, surprising scores, or
disagreement. Keep failed attempts and raw responses. Replace the same slot up to two
times (three attempts total); no prompt changes, optional stopping on efficacy, or
model substitution. A finished, audited output is reused on resume, never regenerated
because of its content. Model/auth/usage failures are not completed trials.

Audit every apply/judge transcript for exact model, terminal success, no tools, and
required output coverage; reconstruct normalized judgments with trusted identity from
the manifest. Run `grade --worklist` on all normalized diagnostic judgments, audit exact
trial counts before analysis, and refuse analysis if any logical slot is incomplete.
Retain audit/status records. Any necessary software amendment after registration must
be recorded with its timing and effect; never conceal a repaired failure as an original
successful trial. No model trial can be synthesized from this parent conversation.

## Execution

```bash
# Copy the frozen registration inputs to ignored runtime storage first.
export ASW_PI_SDK=/path/to/pi-coding-agent/dist/index.js
python3 scripts/subscription_baseline.py apply --dest eval-workspace/subscription-baseline --group antithesis
python3 scripts/subscription_baseline.py judge --dest eval-workspace/subscription-baseline --group antithesis
python3 scripts/subscription_baseline.py apply --dest eval-workspace/subscription-baseline --group review-rewrite
python3 scripts/subscription_baseline.py judge --dest eval-workspace/subscription-baseline --group review-rewrite
python3 scripts/subscription_baseline.py analyze --dest eval-workspace/subscription-baseline
```

Raw attempts and prompts will be archived compressed beside the final report, with
machine-readable normalized scores/comparisons and a SHA-256 inventory. Test and power
fixtures are explicitly not model results.
