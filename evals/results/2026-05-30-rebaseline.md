# Re-baseline under updated doctrine

Date: 2026-05-30
Branch: `claude/thinking-out-loud-feedback-acAqK`
Doctrine commit under test: `48f29fc` (ask-author verdict, mandatory Rewrite check field, both-sides Staccato test)
Baseline compared against: `evals/results/baseline-2026-05-29/scores.jsonl`

## Why this run exists

The 2026-05-29 hillclimb-infrastructure baseline scored every case at 1.0 against the **pre-change** doctrine. This PR adds doctrine on top of that baseline. Without a re-run, the PR has no scored evidence that the new doctrine does not regress the holdout suite. This run is that scored evidence. The full suite was not re-scored — only the holdout split (the gate the runbook actually uses to decide merge).

## Method

Followed `docs/judge-protocol.md` end to end:

1. **Prepare.** `python3 scripts/run_evals.py prepare evals/{evals,adversarial,rewrite-evals,meta-evals}.json --split holdout` produced 15 work units, split across four suites.
2. **Apply.** Four sub-agents in parallel — one per suite — each read `SKILL.md` plus the three reference files, then wrote the skill-applied output for every case in its suite to `outputs/<suite>/<id>.md`. The apply agents did not read the assertions.
3. **Judge.** Four different sub-agents read the outputs and the assertions, judged each assertion independently with a quoted snippet as evidence, and wrote one JSONL line per case to `judgments/<suite>.jsonl`.
4. **Grade.** `python3 scripts/run_evals.py grade` produced `scores.jsonl`.
5. **Delta.** `python3 scripts/run_evals.py join` against the 2026-05-29 baseline, then `python3 scripts/score_delta.py --holdout-only`.

## Results

| Suite | Cases | Assertions passed | Score |
|---|---:|---:|---:|
| `evals.json` | 3 | 9/9 | 1.000 |
| `adversarial.json` | 6 | 18/18 | 1.000 |
| `rewrite-evals.json` | 2 | 6/6 | 1.000 |
| `meta-evals.json` | 4 | 12/12 | 1.000 |
| **Holdout total** | **15** | **45/45** | **1.000** |

Delta vs 2026-05-29 baseline on the 10 cases present in both runs:

```
Cases:         10
Mean delta:    +0.0000
95% CI:        [+0.0000, +0.0000]
Sign-flip p:   1.0000
Verdict:       REJECT (CI overlaps zero; delta is within noise).
```

## How to read the REJECT verdict

`score_delta.py` is designed to detect *improvement* over a baseline. Both runs are at 100% — the binary assertions saturated. A REJECT verdict in this ceiling-on-ceiling regime means "no detectable signal," which is the correct outcome for *non-regression*, not a failure. The actual finding has two parts:

1. **No regression.** The 10 cases present in both runs (`evals.json` holdout × 3, `adversarial.json` holdout × 3 from the 2026-05-29 set, `rewrite-evals.json` holdout × 2, `meta-evals.json` holdout × 2) scored 1.000 → 1.000 under the new doctrine. The ask-author verdict, mandatory Rewrite check field, and both-sides Staccato test did not break existing holdout behavior.

2. **Net-new cases all pass.** The 5 cases this PR adds (`earned-antithesis-synthesis-pg`, `cataphoric-label-defined-in-paragraph`, `escalating-magnitude-triple`, `single-source-overfitting`, `earned-rhetoric-false-positive-rate`) scored 1.000 under the new doctrine. The adversarial judge specifically noted the three PG cases returned `Verdict: keep` with explicit earned reasoning citing the mechanism / contrast / escalation — the calibration this PR was meant to lock in.

## Ceiling effect, named honestly

This run is at ceiling. The repo's own `evals/meta-evals.json -> ceiling-effect-detection` says treat that as a coverage warning, not proof the skill is done. The binary assertions test specific failure mechanisms; once doctrine catches them, the same assertions will keep scoring 1.0 even as new failure modes emerge. The `latest.md` already lists the remaining work this implies:

- A complementary calibration test on a deliberately sloppy real document (true-positive sensitivity).
- An adversarial case for invention-by-elaboration (the failure mode that was reduced in iteration 2 but never directly targeted).
- Cross-family judging to control for the same-family self-preference bias documented in `Lessons_learned.md`.
- A re-run that also scores the `graded_dimensions` axes on rewrite cases (this grader only scores the binary assertions).

## Known limitation: same-family judging

Apply and judge sub-agents in this run shared a model family. Per `docs/judge-protocol.md`, that risks self-preference — the judge can favor outputs that look like its own. The runbook calls for a cross-family judge to dilute the bias. This run did not arrange one, so the 45/45 score should be read as a coverage signal that nothing obviously broke, not as a calibrated number. The PR's test plan flags this as a still-open item.

## Files

- `outputs/<suite>/<id>.md` — 15 verbatim skill-applied outputs.
- `judgments/<suite>.json.jsonl` — per-assertion judgments with quoted evidence.
- `scores.jsonl` — grade output, 15 lines.
- `delta.jsonl` — joined before/after, 10 lines (cases present in both runs).
