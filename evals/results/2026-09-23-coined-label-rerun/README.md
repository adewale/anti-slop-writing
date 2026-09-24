# Powered re-run of the coined-compound-label round

**Status: complete. Pre-registered outcome: ship `candidate-v3`.** Both gates
accepted under both judges and every guard stayed within its over-flag
allowance, so the frozen patch is now in `skills/anti-slop-writing/SKILL.md`. The design was fixed in
`PREREGISTRATION.md` before any trial ran. `SKILL.md` is byte-identical to the
candidate arm's doctrine, 129 words longer than at `53370ff`.

The earlier round, `../2026-09-05-astra-compound-labels/`, was inconclusive: four
valid trials per arm, and a list of design defects. This round tested the same
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
| model versions not recorded | recorded from every transcript in `audit-apply.json` and `judging/audit-judges.json` |

## Result

Primary judge Claude Sonnet 5. "Names it" means the case's first assertion
passed: the critique identified a coined label as coined or undefined. The mean
score is the fraction of the case's three assertions passed.

| Case | Split | Names it, baseline | Names it, candidate | Mean score | Paired delta, 95% CI | Gate |
|---|---|---:|---:|---|---|---|
| `coined-compound-label` | tune | 4/40 | 40/40 | 0.042 to 0.975 | +0.93 [+0.88, +0.98], p=0.0001 | ACCEPT |
| `holdout-coined-compound-label` | holdout | 1/40 | 40/40 | 0.058 to 0.975 | +0.92 [+0.85, +0.97], p=0.0001 | ACCEPT |

The secondary judge, Claude Haiku 4.5, accepted both gates too: +0.66
[+0.55, +0.76] on the tune case and +0.69 [+0.61, +0.78] on the holdout case.

A guard trial over-flags when its first assertion fails. The rule allowed the
candidate one more over-flag than the baseline per guard.

| Guard | Split | Baseline over-flags | Candidate over-flags |
|---|---|---:|---:|
| `coined-label-defined-in-place` | tune | 0/8 | 0/8 |
| `earned-domain-compound` | tune | 5/8 | 3/8 |
| `holdout-coined-label-defined-in-place` | holdout | 0/8 | 0/8 |
| `holdout-earned-domain-compound` | holdout | 2/8 | 1/8 |

All four pre-registered conditions held, so the patch shipped as frozen. Full
gate output is in `results/summary.md`.

## What the numbers say

**The baseline almost never questions a coined label it meets on its own.** It
returned `keep` in 31 of 40 tune trials and 35 of 40 holdout trials. The earlier
round's 2 of 4 does not contradict this. Those trials critiqued the paragraph in
one context beside the guard paragraphs, which the pre-registration flagged as a
cue, and four trials cannot pin a rate. The planning rate of about 0.5 was wrong,
and the effect was about three times the lift the sample size was chosen for.

**The candidate named a coinage in all 80 discriminating trials, under both
judges.** On the tune paragraph it returned `ask-author` 39 times and `revise`
once. On the holdout paragraph it returned `ask-author` 26 times, `revise` 8
times, and `keep` 6 times. The six `keep` critiques still named the labels as
coined. They judged "ledger-fold" earned by the paragraph's ordering and scope
guarantees. Three asked what "invoice drift" measures and one narrowed the
accuracy claim. The other two did neither and failed the third assertion under
both judges.

**No critique in either arm flagged a standard compound as coined.** The
`earned-domain-compound` over-flags come from a flaw in the guard sentence, not
from the rule. "A crash between the enqueue and the fsync replays from the last
checkpoint" claims recovery for the one window a write-ahead log does not yet
cover. Critiques in both arms said so, or asked how the copy-on-write snapshots
relate to "the last checkpoint", and returned `revise` or `ask-author`. The
guard's first assertion counts any verdict other than `keep` as an over-flag,
so it cannot separate a real finding from a false coinage flag. Of the 16
critiques of that sentence, those that mention coinage at all say the terms are
standard. The fixture needs fixing before it guards anything; see `TODO.md`.

**The judges disagree mostly about the baseline.** They agreed on 597 of 672
assertions. Of the 51 discriminating items where they differed, 46 are baseline
critiques, and on those items the Haiku judge passed 66 more assertions than the
Sonnet judge. It credited, for example, a baseline critique that questioned what the
check compares without naming the label as coined. That leniency is why its
deltas are smaller. Both judges are Claude models, so per
`docs/judge-protocol.md` the scores are a coverage signal, not a calibrated
measurement. The apply model and the primary judge are the same model, but both
arms' critiques come from it, and the judge never saw an arm.

## How it ran

- **Apply.** 176 slots, one fresh `general-purpose` agent per slot on the
  `sonnet` alias, launched in the manifest's seeded order. Every agent ran on
  `claude-sonnet-5`. The harness caps concurrent agents at 20, so launches
  rolled: each new trial started when an earlier one finished, still in manifest
  order.
- **Audit.** `audit.py` checked each transcript's tool calls before its trial
  counted, then ran once more with `--final`. It excluded 3 of 179 attempts,
  each replaced by a fresh agent in the same slot. Two candidate trials tried to
  Read their own output path before writing it, and the read returned "File does
  not exist". One baseline guard trial listed the shared output directory, which
  showed other trials' file names and no content. The rule makes no allowance
  for harmless reads, so all three went. Two against one across arms is too few
  events to call lopsided.
- **Judge.** `score_rerun.py batches` pooled 224 critiques: 160 discriminating
  trials, plus 16 guard trials split into their four answers each. It gave every
  critique an opaque id, shuffled across arms, and wrote 38 batches of at most
  six. The key went to a path outside the batch directory. One Sonnet 5 judge
  and one Haiku 4.5 judge graded each batch with the prompt in
  `audit_judges.py`, and `audit_judges.py` checked each judge's transcript and
  file. It rejected 9 of 85 judgment files, each re-judged by a fresh agent on
  the same batch. Six Sonnet judges ran `mkdir -p` on the output directory
  before writing, and one of those also ran a Python check of its own file.
  Three Haiku judges left the graded dimensions empty for one or more items.
  One batch took three re-judges before a Sonnet judge wrote its file without
  a `mkdir`.
- **Score.** `score_rerun.py score` read the file the judge audit accepted for
  each batch, unblinded it, graded with `scripts/run_evals.py grade`, paired by
  slot, and ran `scripts/score_delta.py --sesoi 0.05`.

## Changes made during the run

None of these touched a score, and each was made before any judgment was
scored.

- `audit.py` first counted in-flight agents as having no write, and first
  excluded a trial that listed its own `references/` directory. The rule
  excludes reads outside the doctrine directory, so both were fixes to the
  implementation, not to the rule.
- `scripts/score_delta.py` prints `ACCEPT` for any delta that clears the noise
  floor, including a significant regression. `score_rerun.py` counts only an
  improving `ACCEPT` as a passed gate, which is what "returns ACCEPT" in the
  pre-registration's decision rule means. A synthetic run with a planted
  regression caught this before any judge ran.
- The pre-registration did not say what happens to a malformed judgment file.
  Before any judge ran, `audit_judges.py` set the rule: a rejected file is
  re-judged by a fresh agent on the same batch, and `score_rerun.py` reads only
  the accepted file for each batch.

## Manual check on `evals/cases.md`

Per `AGENTS.md`, a fresh Sonnet 5 agent applied the shipped `SKILL.md` once
each to Case 1 and Case 10, using the prompts of `generic-importance` and
`holdout-copula-hedged-outline-combo`. Both critiques meet every expected point
in `evals/cases.md`, and both are in `manual-check/`.

- **Case 1** flagged "underscores the importance", asked what makes the
  execution durable, and gave a retry-based fallback marked as conditional on
  the real system. It called "durable execution" a standard term that needs no
  definition.
- **Case 10** flagged copula displacement, hedged symmetry, and both
  outline-conclusion templates separately. It asked for the specific data
  sources, customer tier, and decision the console serves, and fell back to
  cutting the closing. It did not flag "decision-making", a standard compound.

## Cost

By the pre-registration's measure, the final context of each agent, the apply
agents used about 14 million tokens and the judges about 6 million, against an
estimate of 18 million.

## Reproducing it

From the repository root, these rebuild the judge batches and key byte for byte
and recompute every number above:

```bash
R=evals/results/2026-09-23-coined-label-rerun
python3 $R/score_rerun.py batches --manifest $R/manifest.json --audit $R/audit-apply.json \
  --outputs $R/outputs --out /tmp/batches --key /tmp/key.json
python3 $R/score_rerun.py score --key $R/judging/key.json --judgments $R/judging/judgments \
  --judge-audit $R/judging/audit-judges.json --out /tmp/results
```

## Files

```txt
PREREGISTRATION.md    question, arms, cases, protocol, exclusions, scoring, decision rule, sample size
candidate-v3.patch    the candidate doctrine, against SKILL.md at 53370ff; shipped
make_manifest.py      deterministic trial manifest and apply prompts, seed 20260923
power_sim.py          the power table in the pre-registration
manifest.json         every slot: arm, case, opaque id, launch position, exact prompt
doctrine-map.json     which opaque doctrine directory held which arm
attempts.json         the output file of every attempt, by slot
audit.py              the exclusion rule, applied to each apply agent's transcript
audit-apply.json      audit.py --final, with transcript names removed
outputs/              all 179 attempts, including the three excluded ones
audit_judges.py       the judge prompt, and the check of each judge's transcript and file
judging/key.json      opaque critique id to arm, case, and slot
judging/judgments/    every judgment file, including the nine rejected ones
judging/audit-judges.json   audit_judges.py --final, with transcript names removed
score_rerun.py        blinding and batching, then unblinding, grading, pairing, gates, guards
results/              unblinded judgments, per-judge scores, paired deltas, summary.md
manual-check/         the two evals/cases.md critiques from the shipped SKILL.md
run-metadata.json     models, dates, counts, and exclusions
```
