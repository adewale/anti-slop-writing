# Rate study — case `parataxis-pervasive-closers`

Why: in the round-1 single-sample A/B this case produced the only negative delta
(before 1.0, after 0.5), driving the whole-suite mean negative. The runbook warns
that single runs are noisy and that run-to-run-varying behavior needs a rate study
(blinded-eval-harness.md). So we drew 3 samples per side on this one case. All
samples are claude-opus-4-8 (self-reported).

Scored against the 4 assertions for the case (A1 names document-level over-reliance;
A2 converts >=2 closers to a relation-naming construction; A3 keeps variety / at most
one earned line; A4 the rewrite does not reproduce the flagged 'X. Y.' cadence).

| Sample | Doctrine | A1 | A2 | A3 | A4 | Score |
|---|---|:--:|:--:|:--:|:--:|---:|
| before #1 (round 1) | snapshot | P | P | P | P | 1.00 |
| before #2 | snapshot | P | P | P | P | 1.00 |
| before #3 | snapshot | P | P | P | P | 1.00 |
| after #1 (round 1) | edited | P | F | P | F | 0.50 |
| after #2 | edited | P | P | P | P | 1.00 |
| after #3 | edited | P | P | P | P | 1.00 |

- **before mean = 1.000 (N=3)**
- **after mean  = 0.833 (N=3)**

Reading:

- The round-1 `after #1` (0.50) is an outlier. It converted only one of four closers
  and kept three paratactic lines. The other two `after` samples converted or cut all
  four via `because` / `which means` / `so` / `which says` and kept exactly one earned
  line — which is the behavior the edit prescribes.
- Both doctrines flag this passage reliably. The pre-edit doctrine already catches it
  through its existing **staccato contrast test** and **hypotaxis preference**; the
  edited doctrine catches it through the new **parataxis density** framing. The score
  difference is one noisy sample, not a doctrine effect.
- Conclusion: on this case both doctrines are at/near ceiling. The edit does not move
  the score because the behavior it targets was already present for obviously-bad,
  bare (unevidenced) parataxis.
