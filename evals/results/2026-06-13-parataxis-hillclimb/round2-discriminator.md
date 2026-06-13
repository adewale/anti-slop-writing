# Round 2 — discriminating case `parataxis-earned-but-pervasive`

Goal of round 2 (chosen by the maintainer): build a case that *only* the document-level
density rule should catch, to test whether the edit helps where the existing
per-sentence staccato test cannot. The passage is four sections; each closes on an
`X was the problem. Y was the fix.` antithesis whose **both sides are evidenced by the
section's own before/after numbers** — so a per-sentence staccato test passes every
closer, and only a document-level lens sees the repetition.

Apply + judge model: claude-opus-4-8 (self-reported on all 6 sub-agents). N=3 per side.

## Result: the case did NOT discriminate

| Sample | Doctrine | A1 earned-ack | A2 doc-density | A3 keep-one | A4 no-gut | Score |
|---|---|:--:|:--:|:--:|:--:|---:|
| before #1 | snapshot | P | P | P | P | 1.00 |
| before #2 | snapshot | F | P | P | P | 0.75 |
| before #3 | snapshot | F | P | P | P | 0.75 |
| after #1  | edited   | F | P | P | P | 0.75 |
| after #2  | edited   | P | P | P | P | 1.00 |
| after #3  | edited   | P | P | P | P | 1.00 |

- **before mean = 0.833 (N=3)**, **after mean = 0.917 (N=3)**, delta +0.083 — within noise.
- A2 (the document-level over-reliance) was caught by **every** sample on **both** sides.

## Why the pre-edit doctrine already catches it

The snapshot doctrine has two mechanisms that fire on document-level repetition without
any explicit "parataxis density" rule:

1. The **staccato contrast test** ends with "Keep or use once." before #1 applied this
   directly: *"earned antithesis may be kept once. Used four times it stops being a
   distinction and becomes the format. Keep the strongest instance, fold the rest."*
2. The detector list flags **"symmetrical paragraph length, parallel headings"** as an
   AI-editing tell. before #2/#3 invoked exactly this: *"Four in a row makes the passage
   symmetrical and formulaic."*

The edited doctrine reaches the same verdict via the explicit `parataxis density` line.
The naming makes the diagnosis slightly more consistent (after side cited it directly)
but does not produce a separable score gain.

## A note on the case design

Several samples (before #3, after #1) flagged `The disk was the bottleneck` as a mild
overreach — the cold/warm numbers compare Postgres vs Redis but do not isolate disk I/O
as the cause. That is a fair catch and counts against assertion A1 as written. It is a
small flaw in the fixture (the cache closer is the least cleanly earned of the four),
not a doctrine difference; it hits both sides equally.

## Conclusion

Round 2 confirms round 1: parataxis — including the document-level, individually-earned
case the edit was built for — is **already covered** by the existing staccato "use once"
rule and the symmetrical-structure tell. The new rule is redundant, not harmful. Per the
runbook (rule-becomes-redundant; CI overlaps zero), the SKILL.md behavior change is not
promoted. See `evals/rejected-edits.md`.
