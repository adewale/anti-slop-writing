# Round 3 — multi-model A/B ("use every model we have")

Re-ran the parataxis doctrine A/B (pre-edit snapshot vs reconstructed edited doctrine)
across every model the harness exposes, to test whether the "doctrine already covers
parataxis" conclusion — drawn only from Opus — holds for weaker models, where the
explicit `Parataxis density` rule might add capability the model lacks on its own.

- Before doctrine: `/tmp/asw-before-parataxis` (no parataxis rule).
- After doctrine: `/tmp/asw-after-parataxis` (snapshot + the reverted `Parataxis density`
  detector and `Parataxis repair` subsection re-applied).
- Cases: `parataxis-pervasive-closers` (bare, unevidenced contrasts) and
  `parataxis-earned-but-pervasive` (the discriminator: every closer individually earned).
- Apply: one sub-agent per (model × doctrine × case), N=1. Judge: held constant (the
  parent Opus session) for comparability.

## Models

| Requested | Ran as | Status |
|---|---|---|
| opus | claude-opus-4-8 | ok |
| sonnet | claude-sonnet-4-6 | ok |
| haiku | claude-haiku-4-5 | ok |
| fable | claude-fable-5 | **unavailable** ("Claude Fable 5 is currently unavailable" — gated access) |

## Scores

`parataxis-pervasive-closers` (bare):

| Model | before | after |
|---|---:|---:|
| claude-opus-4-8 | 1.00 | 1.00 |
| claude-sonnet-4-6 | 1.00 | 1.00 |
| claude-haiku-4-5 | 1.00¹ | 1.00 |

`parataxis-earned-but-pervasive` (discriminator):

| Model | before | after |
|---|---:|---:|
| claude-opus-4-8 | 1.00 | 1.00 |
| claude-sonnet-4-6 | 0.75² | 0.75² |
| claude-haiku-4-5 | **0.75** | **1.00** |

Per-model mean over both cases: Opus 1.00/1.00, Sonnet 0.875/0.875, Haiku 0.875/1.00.
Overall before 0.917, after 0.958 (+0.04) — within noise, driven entirely by one Haiku cell.

## Findings

1. **The core conclusion generalizes across models.** Every available model, on both
   doctrines, caught the document-level over-reliance. Even Haiku with the no-rule
   doctrine flagged it: *"Rule of four: four identical sentence pairs feel like a
   structure imposed on diverse failures rather than a structure that emerges from
   them."* The existing staccato "keep or use once" guidance and the
   "symmetrical paragraph length, parallel structure" tell are enough.

2. **One directional benefit, single-sample.** ² Haiku on the discriminator improved
   0.75 → 1.00. With the no-rule doctrine it mislabeled the individually-earned `disk`
   and `retries` closers as "compressed/decorative." With the edited doctrine it wrote:
   *"each couplet passes the per-sentence staccato test (both sides are evidenced), yet
   the piece as a whole leans on the pattern as its only structural device"* — correctly
   earned-individually + over-relied-collectively. The explicit "even when each line is
   defensible alone" framing appears to help a weaker model hold both truths at once.
   Sonnet did not replicate the gain (it kept flagging the `disk` closer regardless of
   doctrine — consistent model behavior, not a doctrine effect). N=1; noise-prone.

3. **¹ A separate Haiku quality issue the rule does not target.** Haiku tends to invent
   mechanisms when repairing parataxis. Before-doctrine pervasive-closers rewrites
   fabricated causes absent from the source ("the new schema changed how documents were
   looked up," "queued on database locks," "404 errors on uncovered routes," a
   "navigation menu"). Its after-doctrine sample used bracketed `ask-author` placeholders
   instead. This could be the edit nudging toward structure-over-fabrication, or
   variance; either way invention is a bigger Haiku problem than parataxis and is not
   what this edit addresses.

## Disposition

Unchanged: the SKILL.md behavior edit stays reverted. The cross-model run does not
overturn it — overall delta is within noise and every model already catches the target
behavior. It does surface a narrow, testable hypothesis for a future round: the
"individually earned yet collectively over-relied" framing may specifically help weaker
models (Haiku) avoid mislabeling earned instances. That deserves a rate-studied round
(Haiku, discriminator, N>=5 per side) before any promotion — not enough signal here.

## Limitations

- **Fable 5 missing** — the matrix is three models, all Claude. Still single-family.
- **Single judge** (parent Opus), N=1 per cell. A cross-family judge and a rate study are
  the documented next steps.
