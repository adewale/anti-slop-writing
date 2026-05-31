# 2026-05-30 — Branch-specific paired eval run

Purpose: compare the pre-integration skill snapshot (`/tmp/asw-before-skill/SKILL.md`, commit `f13e148`) with the merged doctrine after mining the remote branches.

This run exists because the 2026-05-29 binary holdout baseline is saturated. The selected cases therefore include:

- branch-driving harder tune cases from the emphasis-source, rewrite-self-check, and score-gist detector branches;
- fresh non-adaptive holdout cases added during integration and not used to tune doctrine after scoring;
- graded dimensions for behaviors that binary assertions often miss.

## Case mix

- 12 paired cases total: 8 tune, 4 holdout.
- 11 cases have graded dimensions; 18 dimensions total.
- Both sides were applied from assertion-free worklists (`apply-before.json`, `apply-after.json`). Separate judge agents then wrote JSONL judgments.

## Results

### Binary assertion scores

| Split | Before mean | After mean | Delta | All-pass before | All-pass after |
|---|---:|---:|---:|---:|---:|
| Tune | 0.8250 | 0.7917 | -0.0333 | 4/8 | 4/8 |
| Holdout | 0.6042 | 0.9167 | +0.3125 | 1/4 | 3/4 |
| All | 0.7514 | 0.8333 | +0.0819 | 5/12 | 7/12 |

Gate output (`gate-binary.txt`):

```txt
Split:         all-cases
Cases:         12
Mean delta:    +0.0819
95% CI:        [-0.0833, +0.2625]
Sign-flip p:   0.3753
Verdict:       REJECT (CI overlaps zero; delta is within noise).
Split:         holdout-only
Cases:         4
Mean delta:    +0.3125
95% CI:        [+0.0000, +0.6250]
Sign-flip p:   0.4924
Verdict:       REJECT (CI overlaps zero; delta is within noise).
```

### Scores with graded dimensions included

`--include-graded` normalizes each 1-5 dimension to 0.2-1.0 and averages it with the binary assertion values for that case.

| Split | Before mean | After mean | Delta | All-pass before | All-pass after |
|---|---:|---:|---:|---:|---:|
| Tune | 0.8137 | 0.7925 | -0.0212 | 4/8 | 4/8 |
| Holdout | 0.6383 | 0.8917 | +0.2534 | 1/4 | 3/4 |
| All | 0.7552 | 0.8256 | +0.0703 | 5/12 | 7/12 |

Gate output (`gate-graded.txt`):

```txt
Split:         all-cases
Cases:         12
Mean delta:    +0.0703
95% CI:        [-0.0803, +0.2347]
Sign-flip p:   0.4366
Verdict:       REJECT (CI overlaps zero; delta is within noise).
Split:         holdout-only
Cases:         4
Mean delta:    +0.2534
95% CI:        [-0.0600, +0.5667]
Sign-flip p:   0.4924
Verdict:       REJECT (CI overlaps zero; delta is within noise).
```

## Interpretation

- The merged doctrine is **quantifiably better on the fresh holdout subset** in this run: binary holdout mean rose from 0.6042 to 0.9167, and graded holdout mean rose from 0.6383 to 0.8917.
- The result **does not clear the statistical gate**. The paired-bootstrap CI overlaps zero and the sign-flip p-value is above 0.05, largely because the fresh holdout set has only four cases.
- Tune cases reveal remaining gaps: the after-side output still often failed to write the explicit flattened artifact required by the emphasis-source cases, and it sometimes used `ask-author` where the eval expected a committed rewrite.
- Therefore this run supports “mined and measured; no final statistical acceptance yet,” not “proven improvement.” The next accepted round needs more independent holdout cases or a narrower branch-specific gate with enough N for the CI to clear zero.

## Files

- `selected-cases.json` — the 12 cases used for this paired run.
- `apply-before.json`, `apply-after.json` — apply-only worklists, stripped of assertions.
- `before/outputs/*.md`, `after/outputs/*.md` — skill-applied outputs.
- `judgments/before.jsonl`, `judgments/after.jsonl` — judge records with binary assertions and 1-5 graded dimensions.
- `scores-before.jsonl`, `scores-after.jsonl` — binary-only scores.
- `scores-before-graded.jsonl`, `scores-after-graded.jsonl` — scores with graded dimensions included.
- `delta-binary.jsonl`, `delta-graded.jsonl` — joined before/after rows.
- `gate-binary.txt`, `gate-graded.txt` — `score_delta.py` output.
