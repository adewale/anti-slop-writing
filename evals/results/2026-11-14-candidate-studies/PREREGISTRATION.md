# Candidate screening preregistration — 2026-11-14

**Registration state: no outputs from this campaign have been generated.** The commit
containing this document and its frozen inputs precedes every apply/judge request.
This is a bounded screening/within-scaffold rate study, **not a powered promotion
experiment**. The owner requested the candidate studies and remaining review items,
and previously authorized subscription use without a cost concern. No API-key billing,
provider substitution, quota bypass, or credential export is authorized.

## Questions and frozen candidates

Base: merged `main` at `92d37020c39da5f5f497b550f62997539318137b`, including the
validated maintenance-history examples in #22. The installable skill is unchanged
throughout the study. Candidate packages and patches are **repo-only alternatives**:

- **Compound**: `candidate-compound.patch`, a compact unresolved-supporting-label rule
  grounded in #18's motivating tune failure. It explicitly forbids inventing definitions
  and preserves standard terms and in-passage definitions. This is not a replication of
  every addition in the original #18 patch and cannot validate that entire PR.
- **Teaser**: `candidate-teaser.patch`, a compact promised-payload/discharge rule,
  including distinct rarity and redundant-significance boundaries. It does not import
  the branch's phrase blacklist, duplicated checklist, mandatory output changes, or
  123-line reference expansion.
- **Twitter/#17**: no doctrine candidate. Test the current skill against no skill on
  the branch's eight writing tasks. The prior report retained a null result; this is
  coverage/failure discovery, not an invented improvement comparison.
- **Highlighter**: no doctrine candidate. Test current versus no skill on grounded
  cases and earned-use guards. Any deterministic lint is separate triage tooling,
  never an AI-authorship detector or automatic prose-quality verdict.

The candidate text is frozen before new model outputs or scores; no candidate will
be adapted to any historical or standing holdout. The design inventory inspected the
public historical cases. They are explicitly **not fresh sealed holdouts**. Original
records, provenance and quarantines are retained in `historical-cases.json` and
`provenance.json`. No historical result is imported as a new trial.

## Cases, allocation and dependence

`cases.json`, `manifest.json`, `judge-worklist.json`, `prompt-templates.json` and the
three complete `package-*.txt` files are the exact input/slot contracts. `frozen-sources.json`
hashes source code and installed Markdown. `design-summary.json` gives exact counts:

| Panel | Cases | Arms | Trials per arm/apply model | Apply outputs |
|---|---:|---|---:|---:|
| Standing review/rewrite + antithesis controls | 69 | none/current/compound/teaser | 1 | 552 |
| Compound | 7 | none/current/compound | 3 | 126 |
| Teaser | 12 | none/current/teaser | 3 | 216 |
| Twitter/#17 | 8 | none/current | 3 | 96 |
| Highlighter | 11 | none/current | 3 | 132 |
| **Total** | **107** | | | **1,122** |

Two judges grade every output: **2,244 judgments**, **3,366 logical model calls**.
Standing includes all 61 current review/rewrite cases (59 from the prior baseline plus
#22's two cases) and all eight antithesis/control cases. One standing trial is a cheap
regression screen, not a reliable estimate of per-case stochastic regression risk.
The prior 804-output baseline is not reused because #22 changed the full package.

Each branch panel is **one conservative mechanism/source/scaffold family**, including
its targets, earned-use guards, historical holdouts and fact twins. Distinct nouns,
trials, models and judges do not add independent families. Standing has 18 families;
its 15 historical holdout cases span nine families. Existing fact pairs stay together.
Six new same-split tune twins supply definitions, retry/indexer events, sync-test
facts, investigation findings or editor capabilities. Supplied cases must use those
facts; asking alone or dropping all supported content fails.

Highlighter's three absent-fact-demand tune tasks get new `-grounded-v2` cases and
supplied-fact twins; original records remain archived. The devblog, therapy-retro and
staged-postmortem historical holdouts are **quarantined before generation**, not silently
regraded: their old expectations demand missing specifics, risk converting suggested
checks into completed events, or infer an escalation event from a rhetorical question.
The sourced earned-honesty holdout guard remains. No new detector is promoted from
this coverage exercise.

Opaque slot IDs and allocation shuffle use seed **261115**. Stage submission order
uses the manifest seed (judge adds one); actual arrival order and durations are logged.
Maximum eight concurrent requests. All registered slots are run regardless of interim
results; no efficacy-based stopping, optional extra trials, or selective judge panel.

## Models, prompts, isolation and access

Same previously probed exact models as the completed subscription baseline:

- Apply: `claude-sonnet-5-5` and `openai/gpt-6.1-sol` (SDK result: `gpt-6.1-sol`).
- Judges: `claude-opus-5-5` and `openai/gpt-6.1-sol`; each judges every apply model/arm.
- Effort low for apply, medium for judges. Provider/CLI default sampling; no server
  seed or temperature control is claimed. OpenAI output cap is 10,000 tokens.
- Claude Code 2.1.323: safe mode, no tools/skills/slash commands/MCP/settings,
  replacement neutral system prompt, no session persistence, fresh empty temporary cwd.
  API-key/token environment overrides are removed; use existing subscription login.
- Pi 1.4.0 ModelRuntime: subscription-auth assertion, ordinary tool-free completion,
  no agent session, no resource discovery or project context. Credentials are neither
  read by the runner nor copied into artifacts.

Wrappers, judge rubric and transformations reuse the audited baseline implementation.
Each request has a fresh isolated context. Apply receives only its task/source/facts
and, in skill arms, the complete selected package inline. It cannot access expected
answers, assertions, other outputs, the repo or a blinding key: no tools are available.
This measures **full-package exposure**, not live activation or conditional references.
The same literal task is used across arms; some tasks themselves name skill formats,
so “no skill” means no supplied package, not necessarily a skill-naive task.

Before judging, strip `Rewrite check` and `Remembered line` symmetrically. Keep raw and
judged lengths. Judges receive a single opaque blinded response and grading material,
not arm/model names, package, raw outputs, key, filenames, length counters or sibling
judgments. Residual template/style and length may reveal an arm; blinding does not
remove that confound. All raw responses and failed attempts are retained.

## Outcomes, gates and power

Co-primary: **factual fidelity** and **substantive task fulfillment**, independently
anchored 1–5 in the frozen `PRIMARY` rubric, normalized `(score - 1) / 4`. Neither named
self-checks nor flattening demonstrations nor critique templates earn primary credit.
Questions/cuts are correct only where evidence is missing; supplied facts must be used.
Judges score primaries first, with quoted evidence or a precise description of absence.
Existing assertions/dimensions and dynamic criteria are diagnostics, not blended into
primary outcomes. Secondary: rewrite quality, material unsupported-claim rate
(fidelity ≤3), diagnostic assertion rate, raw/judged length, and judge disagreement.

Average trials within case/arm, then cases within frozen family, with equal family
weights. Compare current–none and each candidate–current only where those arms were
allocated. Report every judge/apply-model separately, by panel; all, historical holdout,
target, guard, supplied-fact and no-additional-fact selections separately. Target and
guard subsets of a single branch still have one family, not independent replications.
Report per-case scores as well as family summaries; retain losses and nulls.

Use the existing family sign-flip test and 10,000-resample bootstrap, seed 261115,
SESOI **0.05**, alpha **0.05**. An efficacy gate would require all eight holdout
co-primary contrasts (2 outcomes × 2 apply models × 2 judges) to have a positive 95%
lower bound, p < .05 and delta ≥ .05. Required guards: no >.05 point increase in
unsupported claims or >.05 normalized rewrite-quality loss in either fact condition,
and report every standing case decrease. Point guards are not powered harm tests.
A failed superiority test is not equivalence. `score_delta.py --holdout-only
--cluster-field family --sesoi .05` is retained for every candidate co-primary contrast.

**No doctrine promotion is authorized even if an isolated contrast passes.**
`power-scenarios.json` simulates the actual ordinal clustered conjunction and allocated
trial counts (500 simulations/scenario). Branch holdouts have one family: their exact
maximum power at the independent-family gate is zero at any repeat count. The standing
one-trial conjunction also misses the 80% power target in every declared scenario.
More repeats cannot make a one-scaffold target panel independent. Accordingly spend
only the registered screening allocation, not a large pseudo-powered repeat campaign.
Fresh independently sourced examples/families and an appropriately powered preregistered
study remain necessary before a general promotion claim.

## Exclusions, audit, resources and publication

Reuse the baseline's fixed three-attempt policy. Exclude/replace only transport failures,
>240-second host or >180-second SDK timeout, incomplete result, wrong model, tools,
empty response or schema-invalid judge response. Keep bad writing, disagreement and
noncompliance. Preserve successful outputs on resume. Stop on auth, usage-limit or
model drift rather than substitute a model/provider or bypass the subscription.
Unknown usage from an interrupted process is reported, never assumed zero.

Audit exact slot sets, model identities, raw terminal success, prompts and hashes,
raw-to-blinded identity, length counts, every assertion/dimension/evidence field, and
trusted suite/split/fact-pair metadata. `grade --worklist` checks all normalized judgments.
Missing/extra slots block analysis. Audit and analysis code is committed before scoring.

Estimate: roughly 1.4× the prior study's logical calls, about 100–150 minutes at eight
workers under similar provider load; list-price-equivalent counters might be $60–$160,
not a subscription invoice. The owner has authorized subscription use without a cost
concern; no separate API expenditure is authorized. Record returned usage, durations,
replacements, exclusions and all null/harmful findings. Any necessary code amendment
is committed and timestamped before resumption. Publish raw attempts compressed, a
checksum inventory, reproducible comparisons, guard/length reports and limitations.
Human fidelity calibration is a separate outstanding human decision, not simulated by
another model. Live client activation is a separately registered trace experiment.
