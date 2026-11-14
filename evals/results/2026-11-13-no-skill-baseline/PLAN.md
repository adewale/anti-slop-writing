# No-skill baseline — historical unrun plan

Superseded by the preregistered, completed [2026-11-14 subscription baseline](../2026-11-14-subscription-baseline/README.md): 804 outputs, 1,608 cross-family judgments, joint improvement criterion not met. The text below records the blocked state on 2026-11-13, not current model access or study status.

No apply model passed the access probe, so there are no trial outputs, judgments,
scores, intervals, length comparisons, agreement figures, or per-model efficacy results.
Question: **does the current skill beat no skill?** Answer: **unmeasured here**.

This is a planning note, not a preregistration. Exact models, sampling settings, N,
cost estimate, seeded launch order, exclusions, and decision thresholds must be fixed
and committed before generating outputs. The instrument PR must land first.

1. Restore model access and record exact returned IDs. Select two apply models and
   two judges, preferably with cross-family coverage and one mid-tier apply model.
   Estimate baseline cost; with the ceiling blank, the handoff requires stopping after Phase 3 and reporting cost. Set a ceiling before Phase 4.
2. Earned-antithesis family first: six independent earned cases plus two decorative
   controls in `evals/shared-benchmark.json`. Compare no skill with current skill on
   every apply model, both judges scoring every output. At least three trials per
   case/arm/model are required; choose final N by simulating power on case means.
3. Then compare no skill/current skill on both splits of the corrected rewrite suite
   and rewrite-shaped review cases. Explicitly score factual invention and task
   fulfillment; report skill versus no skill separately for each fact condition.
   Retain pair IDs, aggregate trials to per-case rates, and cluster by pair ID
   (or broader pre-registered family) for pooled comparisons. Procedure artifacts
   such as a flattening demonstration are diagnostics rather than primary efficacy
   outcomes. Preserve the no-skill task and facts
   verbatim; omit only the skill instruction.
4. Audit isolated trial contexts and blind template fields before scoring. Report
   mean raw/judged word differences beside scores and agreement per apply family.
   Run saturation_index on completed scores. Do not create zero-valued placeholder
   rows or use this chat as a source of purported independent model trials.

PR #18's forty repeats on one holdout paragraph cannot pass the repaired six-independent-
unit gate when clustered by case. A general claim needs additional independent cases
chosen before the run; a single-case replication can instead be reported as a bounded
behavioral rate study. Preserve its frozen patch. This design conflict in the handoff
must be resolved before Phase 4, without treating repeated trials as new cases.
