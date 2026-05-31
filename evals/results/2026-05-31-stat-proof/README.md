# 2026-05-31 — Fresh holdout statistical-proof run

Purpose: test whether current `main` is statistically better than the pre-integration skill snapshot after branch mining, using a larger fresh holdout set rather than the saturated 2026-05-29 baseline.

## Protocol

- Before candidate: frozen pre-integration skill snapshot from commit `f13e148`, archived at run time to `/tmp/asw-stat-before-skill/`.
- After candidate: current `main` at `0c10b47`.
- Cases: 42 fresh holdout cases in `fresh-holdout.json`, created before applying either candidate and not used for doctrine edits.
- Case mix: 6 each for borrowed emphasis, ask-author/non-invention, copula displacement, hedged symmetry, outline-shaped conclusions, decorative em-dash clusters, and earned-use boundary false positives.
- Graded dimensions: 60 total, scored 1-5 and normalized by `scripts/run_evals.py grade --include-graded`.
- Apply phase: separate before/after outputs under `before/outputs/` and `after/outputs/`.
- Judge phase: blind A/B pair judging. `blind/mapping.json` records the anonymization seed and mapping; pair judgments were unblinded only after judgment with `unblind_pair_judgments.py`.

## Results

### Binary assertion scores

| Split | Cases | Before mean | After mean | Delta | All-pass before | All-pass after |
|---|---:|---:|---:|---:|---:|---:|
| Holdout | 42 | 0.9286 | 1.0000 | +0.0714 | 34/42 | 42/42 |

Gate output (`gate-binary-holdout.txt`):

```txt
Split:         holdout-only
Cases:         42
Mean delta:    +0.0714
95% CI:        [+0.0317, +0.1190]
Sign-flip p:   0.0074
Verdict:       ACCEPT (improvement clears the noise floor).
```

### Scores with graded dimensions included

| Split | Cases | Before mean | After mean | Delta | All-pass before | All-pass after |
|---|---:|---:|---:|---:|---:|---:|
| Holdout | 42 | 0.9319 | 0.9988 | +0.0669 | 34/42 | 42/42 |

Gate output (`gate-graded-holdout.txt`):

```txt
Split:         holdout-only
Cases:         42
Mean delta:    +0.0669
95% CI:        [+0.0245, +0.1167]
Sign-flip p:   0.0074
Verdict:       ACCEPT (improvement clears the noise floor).
```

Because every case is holdout, the all-case and holdout gates are identical; `gate-binary-all.txt` and `gate-graded-all.txt` are kept for audit symmetry.

## Family-level graded deltas

| Family | Cases | Before | After | Delta |
|---|---:|---:|---:|---:|
| borrowed emphasis | 6 | 1.0000 | 1.0000 | +0.0000 |
| ask-author / non-invention | 6 | 0.6467 | 1.0000 | +0.3533 |
| copula displacement | 6 | 0.9167 | 1.0000 | +0.0833 |
| hedged symmetry | 6 | 1.0000 | 1.0000 | +0.0000 |
| outline-shaped conclusions | 6 | 1.0000 | 0.9917 | -0.0083 |
| decorative em-dash clusters | 6 | 0.9600 | 1.0000 | +0.0400 |
| earned-use boundaries | 6 | 1.0000 | 1.0000 | +0.0000 |

Interpretation: the accepted aggregate improvement mostly comes from the new `ask-author` / non-invention / rewrite-check behavior, with smaller gains on copula displacement and dash calibration. Boundary and already-solved families stayed at ceiling. The small outline-family graded dip is one 4/5 call on one after output; binary assertions still passed.

## Judge caveat

The completed blind judge run used the available default reviewer model (`gpt-5.5`). A cross-family Anthropic rerun was attempted (`167abebb-10ab-47a9-84e2-fb2698c5cf43`) but failed immediately because no Anthropic API key was configured. Treat this as statistically accepted under the available blind same-family judge, with cross-family/human confirmation still desirable before a release claim that depends on judge independence.

## Files

- `fresh-holdout.json` — pre-registered 42-case holdout suite.
- `worklist-before.json`, `worklist-after.json` — apply/judge worklists.
- `chunks/` — seven-case apply chunks for parallel runs.
- `before/outputs/`, `after/outputs/` — candidate outputs.
- `blind/` — anonymized A/B pair payloads and mapping.
- `pair-judgments/default-*.jsonl` — blind candidate judgments.
- `judgments/before.jsonl`, `judgments/after.jsonl` — unblinded judgment records.
- `scores-*.jsonl`, `delta-*.jsonl` — scored and joined rows.
- `gate-*.txt` — paired-bootstrap and sign-flip gate outputs.
- `unblind_pair_judgments.py` — reproducible unblinding helper.
- `cross-family-attempt.md` — failed Anthropic judge attempt and reason.
