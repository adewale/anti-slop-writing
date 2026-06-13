# Human review: tweet "taste as a trainable model"

This page exists so a human can review the regression anchor without running the
harness. It pairs the original tweet with the best known rewrite and shows the
line-level changes that define "best." If you disagree with the ceiling, edit
`best-rewrite.md` and re-record `evals/results/2026-06-13-tweet-best-anchor/`.

- **Original (verbatim):** [`input.md`](./input.md)
- **Best known rewrite:** [`best-rewrite.md`](./best-rewrite.md)
- **Anchor case:** `tweet-best-rewrite-anchor` in `evals/rewrite-evals.json` (holdout)
- **Reference scorecard:** `evals/results/2026-06-13-tweet-best-anchor/reference-scorecard.jsonl`
- **Source:** https://x.com/itsreallyvivek/status/2065477778125062177 (@itsreallyvivek), captured 2026-06-13
- **Rewrite by:** claude-opus-4-8, 2026-06-13

## What makes it the ceiling (two real fixes, everything else preserved)

### Fix 1 — the conceit, marked as a wager instead of a finding

The original's load-bearing leap is that fast-feedback calibration carries up to slow,
decade-long bets. That is asserted, not shown.

> **Original:** small predictions share machinery with big ones. calibrate where reality
> answers quickly, and the judgment transfers upward to the bets reality grades slowly.

> **Best:** the wager — and it is a wager, not a proven theorem — is that calibrating on
> the small bets sharpens the big ones. that part you can't verify, because the slow bets
> are exactly the ones reality hasn't graded yet. what you can do is calibrate where
> reality answers fast, because that's the only place the loop closes at all.

### Fix 2 — parataxis density broken (section closers varied)

The original ends nearly every section on a matched two-part antithesis. The best version
converts most to named relations and keeps at most two genuinely earned snaps.

> **Original closer (keep score):** same cognitive hardware, opposite training loop.

> **Best:** the hardware is identical; what differs is whether anyone closes the loop.

> **Original (shrink the bet):** firefighters and chess players develop real intuition.
> stock pickers develop confident noise.

> **Best:** firefighters and chess players develop real intuition because they get both;
> stock pickers get neither and develop confident noise.

**Two earned antithesis lines are kept on purpose** (density is about over-reliance, not
abstinence): `what looked like perception was retrieval. what looked like a gift was
inventory.` and the closer `that's not taste. that's an rss feed.` — both sides of each
are evidenced in the lines before them.

### Sharpened fact

> **Original:** the estimate was crude and roughly right

> **Best:** the estimate was crude — the real number was closer to twice that

(Fermi's paper-drop estimate was ~10 kt; Trinity came in around 20 kt. "crude" is now
honest rather than a quiet brag.)

### Deliberately preserved

The opening; all eight carriers (de Groot/Chase-Simon, Fermi, Tetlock/GJP,
Murphy-Winkler, Kahneman-Klein, Sutton/Radford, AlexNet, Hamming); the
write-a-numbered-prediction-then-score-it mechanism; and the ledger ending
(`it will be embarrassing for six months… the only question is whether you collect the
data.`).

## Known soft spot (for reviewers)

The `by around thirty percent` Good Judgment Project figure is the original author's claim
and is widely cited but loosely sourced. It is kept (not introduced) for concreteness.
A future candidate should not be penalized for inheriting it, and should not be rewarded
for inventing a replacement number.
