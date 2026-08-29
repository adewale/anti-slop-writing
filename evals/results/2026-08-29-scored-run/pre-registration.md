# Pre-registration — scored A/B run over the 2026-08-29 additions

Written and committed before any run output was generated, per `runbooks/hillclimb-skill.md` → "Pre-registration (before the round)". The accept/reject rule below is fixed in advance.

## Question

Do the 13 cases added on 2026-08-29 discriminate the pre-change doctrine from the post-change doctrine, and does the post-change doctrine clear the statistical gate on them?

- **Arm A (old)**: `skills/anti-slop-writing/` as of commit `53370ff` (pre-mining), snapshotted into `doctrine-A/` in this directory. Apply agents for this arm read only the snapshot.
- **Arm B (new)**: `skills/anti-slop-writing/` at current HEAD (commit `98b958c` lineage).

## SESOI

0.05 mean per-case delta on the 0-1 assertion-fraction scale. A smaller effect, even if real, does not justify the added skill length. A null result is reported as TOST equivalence via `score_delta.py --sesoi 0.05`, not as bare "no improvement".

## N and axes

- **Cases**: the 13 new cases, paired across arms. 8 tune (`evals.json` 3, `adversarial.json` 3, `rewrite-evals.json` 1, `meta-evals.json` 1) and 5 holdout (2/1/1/1).
- **Apply**: one output per case per arm; apply model Sonnet for every apply agent in both arms (held constant so the doctrine is the only varied factor). One generation per case — run-to-run rate variance is not studied this round and the result note must say so.
- **Deterministic checks**: graded by `run_evals.py lint` per arm for the 7 cases that carry them; identical checks both arms.
- **Judges**: Opus and Haiku (two members, fixed before scoring). Independent per-output, per-assertion grading with quoted evidence; judges are blind to arm identity (outputs live under neutral `outputs-x/` and `outputs-y/`; the mapping is recorded in `arm-mapping.json` and withheld from judge prompts). Judges never re-grade deterministic checks.
- **Known limitation, recorded now**: both judges are Claude-family (no non-Claude judge is reachable in this harness; see `TODO.md`). Scores are read as within-family evidence, per the same caveat as the 2026-05-29 baseline.

## Accept/reject rule

Primary metric: binary assertion fraction per case (judge assertions + deterministic checks merged by `run_evals.py grade`), per judge.

1. Join per judge: arm A scores = `before`, arm B scores = `after`.
2. `python3 scripts/score_delta.py delta-<judge>.jsonl --holdout-only` must return **ACCEPT for both judges** for the round to claim a measured improvement on the new surface. All-case CIs are reported alongside.
3. Any per-case disagreement between judges (different `all_pass`) is flagged for human review, not averaged away.
4. `python3 scripts/saturation_index.py` over the judge axis on arm-B scores; ceiling cases are named in the result note and their zero-deltas read as no-regression only.
5. Graded dimensions (`--include-graded`) are reported as a secondary lens, not the gate.
6. Per the runbook: a holdout failure in arm B does not lead to doctrine edits in this round; it becomes a new tune case for the next round and is logged in `evals/rejected-edits.md`.

## Expected direction (stated for honesty, not part of the rule)

Arm A should fail assertions that require naming the new-register families and should trip deterministic checks by reusing cadence; arm B should pass. Adversarial keep-cases may be non-discriminating (both arms keep earned uses) — per-case deltas of zero there are acceptable and will be reported as such, not counted as evidence for the change.
