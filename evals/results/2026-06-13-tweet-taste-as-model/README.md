# 2026-06-13 — Tweet "taste as a trainable model" (before/after)

Stores a real-world piece as a test case and measures what the skill does to it.

- **Source:** https://x.com/itsreallyvivek/status/2065477778125062177 (@itsreallyvivek), captured 2026-06-13.
  x.com gates unauthenticated fetches (HTTP 402), so the text was pasted by the repo owner and stored verbatim in `evals/fixtures/tweet-taste-as-model/input.md`.
- **Case:** `tweet-taste-as-model` in `evals/rewrite-evals.json` (split `tune`).
- **before:** the original essay, no skill applied.
- **after:** `SKILL.md` (commit `483fd5b`) applied by a sub-agent.

## Model / version captured

| Side | Model id | Name | How captured |
|---|---|---|---|
| after (rewriter) | `claude-opus-4-8` | Opus 4.8 | Pinned at sub-agent launch; the agent also self-reported `claude-opus-4-8` on its last line. |
| judge | `claude-opus-4-8` | Opus 4.8 | Graded both sides against the case assertions + graded dimensions. |
| before | — | — | No model; raw source text. |

Full provenance, including the exact tool commands, is in `run-metadata.json`. This is the
first run in the repo to record the model/version; existing runs only captured the skill commit.

## Results

| Scoring | Before | After | Delta |
|---|---:|---:|---:|
| Binary assertions (3/5 pass after vs 2/5 before) | 0.400 | 0.600 | +0.200 |
| With graded dimensions | 0.475 | 0.625 | +0.150 |

Gate output (`gate-binary.txt`, `gate-graded.txt`): **REJECT**. This is expected and not a
negative result — the run has **N=1**, so the paired bootstrap CI collapses to a point and the
sign-flip test has no power. The gate is a significance test for doctrine changes across a suite;
here it is being run on a single stored case, so treat the deltas as a recorded measurement, not
an accept/reject decision.

## Interpretation: the assertions and the skill-as-applied disagree

The case assertions encode the repo owner's audit of the tweet, which flagged two weaknesses:
(1) a monotonous section-closing cadence (nearly every section ends on a parallel antithetical
aphorism), and (2) the central "taste is a trainable model" conceit being asserted rather than
demonstrated, especially the claim that calibration "transfers upward" from fast- to slow-feedback
bets.

The `claude-opus-4-8` sub-agent, applying the skill cold, **diverged on both**:

- On cadence, it invoked the skill's false-positive restraint and **defended** the closers as
  earned ("I do not touch any of this"), keeping `that's an rss feed` and
  `same cognitive hardware, opposite training loop`. So assertions 1 and the `cadence-variety`
  dimension stay low (it did change one X-not-Y *header* and added a flow hinge).
- On the conceit, it treated the model framing as the legitimate organizing spine and
  **reinforced** it in a new conclusion line, never marking the transfer claim as a bet. Assertion
  2 and `conceit-honesty` stay low.
- It instead fixed two flow-level issues the audit did not prioritize (header-driven structure,
  an implicit conclusion) and produced self-checked rewrites (assertion 5 passes; `fidelity` = 5).

The honest read: the skill, as applied by Opus 4.8, makes this strong piece modestly better on
flow and fidelity but does **not** address the two weaknesses the assertions target. That gap is
the value of the case — it is a candidate disagreement to resolve, either by accepting the
sub-agent's restraint (and softening the assertions) or by hillclimbing the doctrine so cadence
monotony and asserted-conceit detection fire on a piece this strong.

## Reproduce

```sh
D=evals/results/2026-06-13-tweet-taste-as-model
python3 scripts/run_evals.py prepare evals/rewrite-evals.json --split tune --out /tmp/worklist.json
# apply: sub-agent (claude-opus-4-8) runs the apply_prompt for tweet-taste-as-model -> after/outputs/
# judge: grade both sides -> judgments/{before,after}.jsonl
python3 scripts/run_evals.py grade $D/judgments/before.jsonl --out $D/scores-before.jsonl
python3 scripts/run_evals.py grade $D/judgments/after.jsonl  --out $D/scores-after.jsonl
python3 scripts/run_evals.py join --before $D/scores-before.jsonl --after $D/scores-after.jsonl --out $D/delta-binary.jsonl
python3 scripts/score_delta.py $D/delta-binary.jsonl | tee $D/gate-binary.txt
# add --include-graded to grade for the graded variant
```

## Files

- `run-metadata.json` — model/version capture, source provenance, tool commands, results.
- `before/outputs/tweet-taste-as-model.md` — original essay (verbatim).
- `after/outputs/tweet-taste-as-model.md` — Opus 4.8 skill-applied critique + targeted revision.
- `judgments/before.jsonl`, `judgments/after.jsonl` — judge records (binary + graded).
- `scores-before*.jsonl`, `scores-after*.jsonl` — per-side scores (binary and `--include-graded`).
- `delta-binary.jsonl`, `delta-graded.jsonl` — joined before/after rows.
- `gate-binary.txt`, `gate-graded.txt` — `score_delta.py` output.
