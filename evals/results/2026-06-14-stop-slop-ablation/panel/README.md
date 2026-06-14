# Multi-judge panel + promoted-case validation

Two jobs, run with all four repo tools (`validate.py`, `run_evals.py prepare/grade`, `score_delta.py`, and the blinded-harness discipline of separating apply from judge) and a 3-model judge panel (Opus 4.8, Sonnet 4.6, Haiku 4.5).

## 1. Validate the promoted stop-slop-derived cases under the live doctrine

`run_evals.py prepare` built `worklist.json` from `promoted-cases.json` (the 3 cases now in the live suites). An Opus apply agent ran the live `SKILL.md` on each (`outputs/opus/`). All three judges then graded every output.

Result — every promoted case passes, with **unanimous agreement across all three judges**:

| case | opus | sonnet | haiku | unanimous assertions |
|---|---|---|---|---|
| stopslop-divergence-no-mechanism-closer | 1.00 | 1.00 | 1.00 | 3/3 |
| stopslop-divergence-compressed-antithesis | 1.00 | 1.00 | 1.00 | 3/3 |
| stopslop-thin-content-cut-or-ask | 1.00 | 1.00 | 1.00 | 3/3 |

The live doctrine produces the asserted divergence behavior (it flags stop-slop's punch-first golds and asks/cuts on thin content rather than inventing), and the cases are well-calibrated — no judge split on any assertion.

## 2. Harden the ablation null with a cross-family panel

The round-1 caveat was single-family judging (Opus also produced some outputs → self-preference risk). 15 of 18 A/B pairs were byte-identical, so they are judge-invariant by construction; only the 3 `h2-earned-quotable-closer` pairs differed textually. The panel re-judged those 6 outputs (A/B × 3 apply-models) with all 3 judges = 9 paired comparisons:

```
score_delta.py panel-ablation-delta.jsonl --sesoi 0.05
Cases:         9
Mean delta:    +0.0000
TOST 90% CI:   [+0.0000, +0.0000]
Equivalence:   EQUIVALENT (CI within +/-0.0500; no effect of practical size).
```

Every judge scored A=B=1.00. The "no effect" verdict no longer depends on a single judge family: it holds under Opus, Sonnet, and Haiku judges, on the only pairs where a judge *could* have seen a difference.

## Files

```
promoted-cases.json        the 3 promoted cases extracted from the live suites
worklist.json              run_evals.py prepare output
outputs/opus/*.md          live-doctrine outputs for the 3 promoted cases
judgments/{opus,sonnet,haiku}.jsonl   27 panel judgments (9 outputs x 3 judges)
panel-ablation-delta.jsonl 9 paired rows for the differing ablation pairs
```
