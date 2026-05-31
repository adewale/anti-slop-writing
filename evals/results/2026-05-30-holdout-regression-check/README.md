# 2026-05-30 — Held-out regression check on the procedural emphasis-source change

## What this run answered

After rebasing this branch onto the new hillclimb protocol (PR #2), the open question for the doctrine change in commit `d18c503` (procedural emphasis-source and syntax-relation tests) was: does it regress any of the held-out cases the upstream baseline scored 1.0 on? The branch had no gated answer; only qualitative behavioral evidence from the blinded harness.

## Setup

- Apply sub-agent (`general-purpose`) read `skills/anti-slop-writing/SKILL.md` (this branch's version, with the procedural detectors) and produced one output per holdout case in `outputs/<suite>/<id>.md`. No assertions in its context.
- Judge sub-agent (`general-purpose`) — separate sub-agent context, never read the doctrine — graded each output against its case's assertions, with quoted evidence. Wrote `judgments/<suite>.jsonl`.
- `scripts/run_evals.py grade` aggregated per-assertion judgments into per-case scores: `scores.jsonl`.
- `scripts/run_evals.py join` produced `delta.jsonl` against `evals/results/baseline-2026-05-29/scores.jsonl`. Two cases this branch added (`earned-emphasis-from-idea`, `earned-paragraph-escalation`) have no baseline and were excluded from the join.
- `scripts/score_delta.py` ran the paired-bootstrap and sign-flip-permutation gates. Output in `gate-output.txt`.

## Result

12/12 cases at score 1.0 under this branch's doctrine. 10/10 of the cases with baselines match the baseline exactly. Per-case delta is exactly 0.0 for every joined case.

Gate verdict: REJECT — but mechanically, because the CI collapses to `[+0.0000, +0.0000]` when before = after = 1.0 everywhere. This is what "no regression" looks like when the baseline is already at ceiling. The gate cannot return ACCEPT in this configuration; the achievable outcomes are zero (no regression) or negative (regression). The achieved outcome is zero.

## Interpretation

- **No regression.** The procedural emphasis-source and syntax-relation tests do not break any of the upstream's holdout cases. The new doctrine handles the upstream's flag cases (`stacked-rule-of-three`, `abstract-system-noun-stack`, `fake-precision-unnamed-source`, `fake-precision-rewrite-finance`, `product-tour-rewrite-developer-tools`) correctly, and it keeps the adversarial keep-cases (`earned-importance-immediate-mechanism`, `cost-benefit-not-just-earning-the-contrast`, `research-methods-staccato`) without over-flagging.
- **Not an accept-able improvement.** Under a binary-assertion gate, no doctrine change can score positive against a 1.0 baseline. This is a known eval-suite health problem; `evals/meta-evals.json#ceiling-effect-detection` and `noise-vs-signal-on-small-suite` flag it.
- **Path to a gated positive.** Adding `graded_dimensions` to the cases where the procedural detectors should matter — e.g., a `flatten-artifact-produced` 1–5 axis on `stacked-rule-of-three` — would let a doctrine that produces the explicit flattened sentence score higher than one that only gestures. That work is not in this run.

## What this run does NOT measure

- The two adversarial keep-cases added on this branch (`earned-emphasis-from-idea`, `earned-paragraph-escalation`) scored 1.0 under the new doctrine but have no baseline to compare against. They are listed in `scores.jsonl` for completeness; they are excluded from `delta.jsonl`.
- The trigger-query suite was not exercised in this run.
- Single judge from a single model family. The runbook's "cross-family ensemble" rule applies to the next round, not this one — this run is a regression check, not a doctrine-quality benchmark.

## File layout

- `outputs/<suite>/<id>.md` — apply sub-agent's skill output per case (12 files).
- `judgments/<suite>.jsonl` — judge sub-agent's per-assertion judgments (4 files).
- `scores.jsonl` — per-case aggregated scores produced by `run_evals.py grade`.
- `delta.jsonl` — joined `{id, split, before, after}` against the 2026-05-29 baseline.
- `gate-output.txt` — captured `score_delta.py` output for both all-cases and `--holdout-only`.
