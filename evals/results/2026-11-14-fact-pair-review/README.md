# Facts-supplied pair review — 2026-11-14

The nineteen new twins supply the facts needed for their requested rewrites. The
review found remaining scoring defects: some missing-fact partners' graded rubrics
still demanded unavailable details or a named self-check, and the scoring pipeline
dropped the relationship between a task's two conditions. These defects are repaired
before model scoring. No model performance result is reported.

Reviewed commit: `69ade5d0e4cf3c1c9486b62fa9e104934326ddbe` on PR #26.
All nineteen twins were read with their originals, expected outputs, assertions, and
available dimensions. These are synthetic source scenarios; no claim about a real
product, client, or measured deployment is made by their presence in the suite.

## Case-by-case findings

IDs in the table identify the original; its twin appends `-with-facts`.
All supplied facts and case prompts remain byte-for-byte equivalent as JSON strings.

| Suite | Original case | Split | Evidence licensing the supplied-facts answer | Review result |
|---|---|---|---|---|
| Review | `decorative-contrast` | tune | Map assigned meeting points; the drill timed arrivals | Keep the earned contrast or state that relation. A substantive keep decision remains valid. |
| Review | `safe-essay-voice` | tune | Tallyroom's charity audience, statement imports, campaign tags, donor-report export | Specific product/reader and a supplied capability can replace the abstraction. |
| Review | `borrowed-emphasis` | tune | Step log, replayed variables, continuation at the first unfinished step, compared with a whole-function retry | Mechanism is supplied; no new durability guarantee is needed. Missing-fact partner's graded rubric corrected. |
| Review | `paragraph-scale-borrowed-emphasis` | tune | Payments team's request-ID rule after a failed payment could not be traced across five services | Design decision and reason are supplied. Missing-fact partner's graded rubric corrected. |
| Review | `copula-displacement` | tune | Dashboard content and support-agent use before replying | Plain action and objects are supplied. Missing-fact partner's graded rubric corrected. |
| Review | `hedged-symmetry` | tune | Restaurant-accountant audience, reconciliation task, price, absence of home features | Audience and task can be stated without inventing a tradeoff. Missing-fact partner's graded rubric corrected. |
| Review | `outline-conclusion-template` | tune | Pharmacy courier service, night-driver shortage and premium, planned refrigerated vans | Named obstacle/response and planned action support the ending. |
| Review | `abstract-system-noun-stack` | holdout | Kubernetes scheduler extension, GPU-memory readings every 30 seconds, job movement above 90% | Actor, actions, and thresholds are supplied. Missing-fact partner's graded rubric corrected. |
| Review | `holdout-borrowed-emphasis-release-safety` | holdout | 1% rollout, rollback trigger, on-call sign-off, full-release condition | Requested gates are supplied. Flattening remains a diagnostic procedure. |
| Review | `fake-precision-unnamed-source` | holdout | Catalogue-page median before/after measurement; database bills of $9,000 and $6,100 | Attribute observations to these sources. Added guard against causal or all-workload generalization; corrected missing-fact provenance rubric. |
| Rewrite | `pelican-process-relation` | tune | Leaders mark piers; organisers compare maps for unreached piers | Map-to-drill relationship is supplied. |
| Rewrite | `safe-essay-cut-or-concretize` | tune | Shiftboard's phone swaps, charge-nurse approvals, replacement of paper forms | Concrete workflow is supplied; no adoption or time-saving claims needed. |
| Rewrite | `multi-issue-output-manifest` | tune | `deploy init` writes config; dashboard groups shared-root-cause alerts | Both requested items have independent supplied mechanisms. |
| Rewrite | `emphasis-source-flatten` | tune | State saved after each step, crash resumption, ordinary sequential code | Relation can replace cadence. Missing-fact partner's graded rubric corrected. |
| Rewrite | `copula-displacement-to-is` | tune | Job assignment to one worker and reassignment after heartbeats stop | Specific action verbs are supported. Missing-fact partner's graded rubric corrected. |
| Rewrite | `hedged-symmetry-commit` | tune | Production build failures on unhandled rejections; prototype warnings | Real branch supports the stated priority. Missing-fact partner's graded rubric corrected. |
| Rewrite | `outline-conclusion-carrier-bound` | tune | March invoice-workflow outage/resumption, planned per-step timeouts | Example and next step are supplied. Missing-fact partner's graded rubric corrected. |
| Rewrite | `fake-precision-rewrite-finance` | holdout | 2025 backtest, median maximum-drawdown reduction, 31 portfolios, 2015–2024 window, no live results | Attribute the report and retain its scope. The comparator is unspecified: a supported rewrite may raise that question. Missing-fact provenance rubric corrected. |
| Rewrite | `holdout-ask-author-ai-tooling` | holdout | Patchwright, tracker durations of eleven weeks/six working days, engineer review | Report the records and reviewed work. Added guard against inferring that the tracker establishes a causal time saving. |

## Repairs

The facts-supplied guard now requires completing the supported review/rewrite and
rejects an answer that only asks or discards the material. It allows a genuine
remaining question alongside a supported answer. The previous categorical rejection
of an ask-author verdict could reject a careful response about an unspecified
comparator or causal explanation. It also had to preserve the earned-contrast
case's permitted keep verdict.

Eleven missing-fact graded rubrics now credit precise questions or justified cuts,
consistent with their assertions. Three self-check dimensions elsewhere in the
review/rewrite suites now assess the rewrite's actual fidelity and cadence; a
`Rewrite check` field is not required. This matters because `blind` removes that
field before judging, and the field was already an artifact in the retracted proof.

The original is marked `requires_fact_pair: true` for each of the nineteen pairs.
Validation rejects a missing required twin, a cross-split pair, empty supplied facts,
and malformed pair references. A source-sufficient case can remain unpaired.

`prepare` includes `pair_id` and `fact_condition` only in judge worklists and the
requested judgment schema. Grade/join preserve them and reject mismatches between
arms. The gate rejects a known pair split across independent units; cluster on
`pair_id` for a pooled analysis, or use a broader pre-registered family that keeps
both conditions together. The 59 cases in these two suites map to 40 pair IDs;
broader family dependencies may reduce independent N further. Report each fact
condition separately so an aggregate gain cannot hide harm on one side.

Procedure artifacts such as producing a flattened residual claim remain useful
diagnostics. They must be reported separately from primary rewrite-fidelity and
task-fulfillment outcomes in the baseline preregistration. The generic grader still
averages supplied assertions; the study's committed scoring/audit script must
implement that outcome separation before scoring.

## Validity record and verification

`case-changes.json` retains every old/new case object from this follow-up. The five
holdout twins received grading clarifications before any new output existed; their
facts, prompts, and split assignments were preserved. No installable skill file was
edited or tuned against them. Freeze these cases before the next study.

The regression tests use synthetic arithmetic judgments in temporary files to prove
that ten rows representing five tasks yield five clusters and UNDERPOWERED, that six
complete pairs can pass as six units, and that unrelated case IDs remain valid.
These are unit-test fixtures, not model trial data.

All seven required checks are run before the commit; command output is retained in
`validation/`. Model generation remains unrun. This review provides case validity
and software verification, without an efficacy claim.
