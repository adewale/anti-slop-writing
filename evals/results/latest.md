# Latest eval results

Updated: 2026-11-13

Whether the current skill improves writing over no skill remains unmeasured in this
repository. The 2026-05-31 statistical-proof claim is withdrawn: removing a
version-specific template assertion gives p≈0.126, and testing seven family means
gives p≈0.245. See [the reproduction](2026-11-13-review-reproduction.md).

The newest completed model comparison on main is
[2026-06-14-stop-slop-ablation](2026-06-14-stop-slop-ablation/README.md): current skill
versus an appended candidate block, three Claude apply models, zero paired score
deltas on both reported rounds. It contains no no-skill arm and remains subject to
the validity concerns in the November review. It cannot settle absolute efficacy.

Other completed work includes
[2026-06-13-parataxis-hillclimb](2026-06-13-parataxis-hillclimb/README.md)
and [the public tweet anchor](2026-06-13-tweet-best-anchor/README.md).
The latter is open-book regression coverage; its source was already a tune input.
The anchor now lives in `evals/ablations/open-book-reference-anchors.json`.

Standing baseline: 38/38 cases scored 1.0 in
`baseline-2026-05-29/scores.jsonl`. Ceiling results establish only no regression.
No new model outputs or efficacy scores were generated during the November repairs.
The current work and access limits are in
[the review report](2026-11-13-eval-integrity.md).
