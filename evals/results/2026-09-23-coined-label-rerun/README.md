# Powered re-run of the coined-compound-label round

**Status: running.** The design is fixed in `PREREGISTRATION.md`, committed
before any trial output existed. Apply trials are in progress. No critique has
been judged or read, and the audit and scoring scripts below are committed
before any judge runs.

The earlier round, `../2026-09-05-astra-compound-labels/`, was inconclusive: four
valid trials per arm, and a list of design defects. This round tests the same
rule with each defect removed.

| Earlier defect | This round |
|---|---|
| four trials per arm | 40 per arm on each discriminating case, from a power simulation of the gate |
| doctrine quoted fixture strings | `candidate-v3.patch` quotes no eval prompt, and no eval-prompt coinage appears in either doctrine |
| agents read each other's critiques | one fresh agent per critique, opaque paths, and a transcript audit that excludes and replaces any trial that reads outside its doctrine |
| paragraphs shared a context | each discriminating trial sees one paragraph |
| only one arm could load references | each arm runs from a full copy of the skill directory |
| verdict lines stood in for grades | blinded judge agents grade each case's assertions |
| the holdout guard had been seen | fresh holdout cases written after the candidate was frozen |
| model versions not recorded | resolved from the dry run and recorded in the pre-registration |

## Running it

From the repository root, with the two doctrine directories built as the
pre-registration describes:

```bash
python3 evals/results/2026-09-23-coined-label-rerun/make_manifest.py \
  --doctrine-map <doctrine-dirs.json> --out-dir <output-dir> --out <manifest.json>
```

Launch one `general-purpose` agent on the `sonnet` model per manifest entry, in
`launch_position` order, with the entry's `prompt`. Audit each transcript
before counting its trial. Then judge the pooled critiques blind, score them with
`scripts/run_evals.py grade`, build the paired deltas by slot, and apply the
decision rule.

## Files

```txt
PREREGISTRATION.md    question, arms, cases, protocol, exclusions, scoring, decision rule, sample size
candidate-v3.patch    the candidate doctrine, against SKILL.md at 53370ff
make_manifest.py      deterministic trial manifest and apply prompts, seed 20260923
power_sim.py          the power table in the pre-registration
audit.py              the exclusion rule, applied to each apply agent's transcript
audit_judges.py       the judge prompt, and the check of each judge's transcript and file
score_rerun.py        blinding and batching, then unblinding, grading, pairing, gates, guards
```
