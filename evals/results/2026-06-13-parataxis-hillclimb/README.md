# 2026-06-13 — Parataxis hillclimb (round 1)

Goal: improve the skill at repairing **parataxis** — clauses placed side by side with
the relation left unstated (`I came, I saw, I conquered`) — motivated by the
`tweet-taste-as-model` case, where the skill rewrite *defended* the tweet's pervasive
paratactic closers instead of repairing them.

## The change under test

- `SKILL.md`: a new `Parataxis density` detector line + a `Parataxis repair` subsection
  (unstated-relation repair; document-level density/over-reliance check; guards against
  over-correction). +200 words (the round budget; consolidated to fit).
- `references/anti-slop-writing-doctrine.md`: a `Parataxis and hypotaxis` section with
  before/after examples and two cautions.
- `references/flow-by-relation.md`: a diagnosis bullet for "every section closes on the
  same paratactic two-part contrast".

Before doctrine = pre-edit snapshot at `/tmp/asw-before-parataxis` (commit `615d671`).
After doctrine = edited tree. Apply + judge model: **claude-opus-4-8** (self-reported on
every sub-agent). Single-family judging — see Limitations.

## New eval cases

- `evals/rewrite-evals.json` (tune): `parataxis-pervasive-closers`,
  `parataxis-unstated-relation`, `parataxis-coordination-hides-cause`,
  `parataxis-chained-and`.
- `evals/adversarial.json` (tune, earned-parataxis guards):
  `earned-parataxis-sequence`, `earned-parataxis-evidenced-contrast`.

## Result: REJECT (within noise)

Round-1 full-suite A/B (N=6, one sample per side):

| Case | Before | After |
|---|---:|---:|
| parataxis-pervasive-closers | 1.000 | 0.500 |
| parataxis-unstated-relation | 1.000 | 1.000 |
| parataxis-coordination-hides-cause | 1.000 | 1.000 |
| parataxis-chained-and | 0.667 | 1.000 |
| earned-parataxis-sequence | 1.000 | 1.000 |
| earned-parataxis-evidenced-contrast | 1.000 | 1.000 |
| **mean** | **0.944** | **0.917** |

```txt
Mean delta: -0.0278   95% CI: [-0.2500, +0.1667]   sign-flip p: 1.0000
Verdict: REJECT (CI overlaps zero; delta is within noise).
```

Rate study on the pivotal case (`parataxis-pervasive-closers`, N=3/side, see
`ratestudy/`): before **1.000**, after **0.833**. The round-1 `after` 0.500 was an
outlier; the gap is one noisy sample, not a doctrine effect. De-noising it flips the
whole-suite delta to roughly **+0.03**, still well within noise.

## Interpretation

- **The existing doctrine already covers parataxis** on these cases. The pre-edit
  staccato-contrast test and hypotaxis preference reliably flag and repair bare,
  unevidenced paratactic contrasts; both doctrines sit at/near ceiling.
- **The tune cases do not isolate the real gap.** The documented failure (the tweet)
  is parataxis that is *pervasive yet individually earned* — each closer has prior
  evidence, so the per-sentence staccato test defends it, and only the document-level
  density check would fire. The four repair cases here are bare contrasts with no
  prior evidence, so the per-sentence test already catches them. They confirm
  no-regression but cannot measure the document-level addition.
- **One directional signal, unverified:** on `parataxis-chained-and` the before agent
  *invented* a missing mechanism (asserted "nothing checks the output between them" as
  fact) while the after agent named the relation without fabricating (after 1.0 vs
  before 0.667). Possibly the strengthened repair framing, possibly noise; N=1.

## Disposition (after round 2)

The maintainer chose "round 2 first": build a discriminating case before deciding. Round 2
(`round2-discriminator.md`) showed the pre-edit doctrine already catches the document-level
case, so the `SKILL.md` behavior change is **redundant**, not merely unvalidated. Final state:

- **Reverted** the `SKILL.md` `Parataxis density` detector + `Parataxis repair` subsection
  to the pre-edit snapshot (gated runtime behavior unchanged). Logged in
  `evals/rejected-edits.md`.
- **Kept** the `Parataxis and hypotaxis` teaching section in
  `references/anti-slop-writing-doctrine.md` (reference-only; names the concept and
  consolidates the existing "use once" + symmetrical-structure guidance) and the
  flow-by-relation bullet.
- **Kept** all seven new tune cases (six parataxis + the discriminator) and the failure
  record `evals/failures/tweet-parataxis-density.md` as regression coverage.

Net: the hillclimb's honest result is "stayed at ceiling — no rule needed; the gap was
application, not doctrine," with new cases locking that in.

Round 3 (`round3-multimodel.md`) re-ran the A/B across every available model
(Opus 4.8, Sonnet 4.6, Haiku 4.5; Fable 5 was unavailable). It did not change the
disposition: every model on both doctrines caught the document-level over-reliance.
The only directional benefit was a single Haiku cell on the discriminator (0.75 -> 1.00),
a noise-prone N=1 hypothesis flagged for a future rate-studied round.

## Limitations

- **Single-family judging.** Apply and judge are both claude-opus-4-8; the runbook
  requires a cross-family judge before trusting a delta. Same-family agreement is not
  evidence. A GPT/other-family judge pass is the missing step.
- **Small N.** N=6 whole-suite, N=3 on the rate-studied case. CIs are wide by design.

## Files

- `before/round1-all-cases.md`, `after/round1-all-cases.md` — round-1 outputs (6 cases each).
- `ratestudy/pervasive-closers-ratestudy.md` — 3-per-side study of the pivotal case.
- `judgments/before.jsonl`, `judgments/after.jsonl` — per-assertion judgments.
- `scores-before.jsonl`, `scores-after.jsonl`, `delta.jsonl`, `gate.txt`.
