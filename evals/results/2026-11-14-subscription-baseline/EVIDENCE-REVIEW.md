## Review

**No P0/P1 pipeline defect found.** The evidence supports reporting this completed baseline, but **not a confirmed benchmark improvement**.

### Correct: execution and evidence integrity

- **804 apply outputs and 1,608 valid judgments**, with no missing/extra completed slots or duplicate completed provider responses. The supplementary verifier checks actual filesystem sets, unique manifest IDs and `(case, model, arm, trial)` tuples—not merely the echoed counters in `slot-audit.json`. It reports **2,412 distinct completed response/session IDs** (`eval-workspace/subscription-baseline/verification.json:1–25`; verifier implementation: `evals/results/2026-11-14-subscription-baseline/verify.py:23–80`).
- The verifier checks every selected raw response against its completed payload, reconstructed prompt, prompt hash, stripping transformation, word counts, exact requested model, and tool-free receipt. Representative Sonnet/Opus/GPT transcripts corroborate these checks. Reported identities are `claude-sonnet-5-5`, `claude-opus-5-5`, and `gpt-6.1-sol`; these are **reported model identities, not immutable backend snapshots**.
- Failure accounting is consistent with the evidence:
  - **72 archived EAGAIN processes:** empty stdout and stdin-read errors before provider invocation; consistent with amendment A1.
  - **8 interrupted judge attempts:** prompt-only/no raw response. These establish missing receipts, **not proof that no remote request or completion occurred**.
  - **5 returned, schema-invalid judge responses:** preserved and replaced. A sampled response is terminal-successful but malformed/incomplete JSON, supporting exclusion for schema rather than unfavorable scores.
- Dependence is handled appropriately: three trials become case means, cases become equally weighted family means, and paired fact conditions remain within families (`scripts/subscription_baseline.py:585–616, 811–874`). There are **19 complete condition pairs**; core holdout has **15 cases/9 families**. Pair-restricted holdout reports have **5 cases/4 families**, not five independent families.

### Finding: P2 — attempt ledger understates interruptions

`attempt-audit.json` labels the eight interrupted attempts `"failed": false, "audit": null`, because `"failed"` means only that `failure.json` exists (`scripts/subscription_baseline.py:758–769`). For example, `attempt-audit.json:36338–36342` records a prompt-only interrupted attempt this way.

**Smallest resolution:** use the supplementary verification classification when reporting failures; explicitly distinguish completed, schema-invalid, and interrupted/no-response attempts. This is bookkeeping ambiguity, **not evidence of corrupted scores**.

### Decision and allowable claims

The preregistered requirement is an **eight-contrast conjunction**, including SESOI **Δ ≥ .05**, positive 95% lower bounds, and p < .05—not selection of favorable contrasts (`PREREGISTRATION.md:143–150`).

| Apply / judge | Fidelity Δ; p | Task Δ; p | Qualifying contrasts |
|---|---:|---:|---|
| Sonnet / Opus | +.1389; .0469 | +.1829; .0313 | Both |
| Sonnet / GPT | +.0370; .7188 | +.0972; .2461 | Neither |
| GPT / Opus | +.0278; .4844 | +.1667; .0391 | Task only |
| GPT / GPT | −.0324; .3594 | +.0926; .2656 | Neither |

The three qualifying contrasts also have positive 95% lower bounds; the other five intervals cross zero (`comparisons.json:208–310, 1341–1443, 2474–2576, 3607–3709`). **The global joint criterion fails.** Local/composite `"ACCEPT"` fields must not be presented as study acceptance.

Family-weighted holdout unsupported-claim **point guards also fail**:
- Sonnet/GPT, supplied facts: **+.2083**
- GPT/Opus, supplied facts: **+.0833**
- GPT/GPT, no additional facts: **+.1111**

No normalized rewrite-quality loss exceeds .05 (`family-weighted-guards.json:82–161`). These are point-guard failures, **not powered demonstrations of harm**.

**Allowable summary:** On this frozen public benchmark, the skill improved deterministic earned-antithesis preservation from **12/18 to 18/18 for Sonnet** and **15/18 to 18/18 for GPT**. Decorative controls passed **6/6 in every arm/model**. These are regex-defined successes in **one dependent scaffold family**, not proof of perfect substantive writing. Opus supports three core-holdout contrasts; GPT judging does not confirm them.

**Required limitations:** underpowered estimation baseline; historically inspected public holdouts; full-package inline exposure rather than live skill activation; residual stylistic unblinding and shared-rubric priming; model-judge disagreement; substantially longer skill responses. Failed superiority is not equivalence. The two pooled composite ceiling cases provide only no-regression evidence.

**Merge verdict: OK with notes for bounded evidence reporting—not doctrine promotion or unrestricted efficacy claims.**

Audit was read-only and generated no trials. I inspected the supervisor-run deterministic verifier and its output; I did not independently execute it or inspect historical Git ranges, so commit chronology remains outside this audit’s verification.