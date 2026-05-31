# Before — rewrite-self-check iteration

Date: 2026-05-28
Baseline commit (doctrine before the `Rewrite check` field): `38bdbd0`
Source under review: https://joe.dev/posts/thinking-out-loud/

This iteration's "before" is the previous iteration's "after." The
2026-05-28 ask-author iteration eliminated major inventions but the
rewrites themselves still contained slop the doctrine flags. Counts
below come from a re-read of
`evals/results/2026-05-28-joe-beda-after.md`.

## Slop the rewrites contained

| Item (from 2026-05-28-joe-beda-after.md) | Slop pattern in the rewrite |
|---|---|
| Item 2 | Negative-parallelism cadence: "the kind that don't fit in a Slack message or a Bluesky post" |
| Item 4 | Heavy rule-of-three with parenthetical examples; items 3–5 invented |
| Item 6 | Em-dash closure + parallel "no X, no Y" cadence mirroring the source's flagged pattern |
| Item 10 fallback | X-not-Y cadence ("portability and moderation tooling, not growth loops or ad inventory") + invented topic pairs inside an `ask-author` fallback |
| Item 13 | Rule-of-three list inventing a standard.site schema enumeration |
| Item 21 | Em-dash rule-of-three list + the decorative closer "That was the point." — a stand-in for the banned "In conclusion / Overall / Ultimately" phrases |

Counts:

| Metric | Value |
|---:|---:|
| Rewrites containing rule-of-three with invented or parenthetical list members | 2 (Items 4, 13) |
| Rewrites containing X-not-Y / negative parallelism cadence | 3 (Items 2, 6, 10 fallback) |
| Rewrites containing em-dash rule-of-three list as closer | 1 (Item 21) |
| Rewrites ending on a banned decorative closer ("That was the point", etc.) | 1 (Item 21) |
| `ask-author` fallbacks that themselves invent or use the flagged cadence | 1 (Item 10) |
| `Rewrite check` field uses (the field did not exist) | 0 |

## Why this happened

The previous iteration added the `ask-author` verdict and a triggering
rule. It did not require the model to grade its own rewrite. The Final
self-check at the end of `SKILL.md` includes a question about reusing
the flagged cadence, but the model writes the critique linearly,
item-by-item, and never circles back. Without a per-item slot for the
self-grade, the slop check does not fire.

The case is sharpest at Item 21. The skill explicitly flagged the
source's lack of carrier-bound ending, then produced a Concrete rewrite
that ends on "That was the point." — a phrase the doctrine's
Avoid-by-default list bans by name as a disguised "Ultimately /
In conclusion." The detector that fires on the source does not fire
on the rewrite.

It is also sharpest at Item 10. The model correctly used `ask-author`
at the verdict level (the win from the previous iteration), then
ignored the same rule when writing the fallback. The fallback fabricates
topic pairs ("portability and moderation tooling, not growth loops or
ad inventory") and uses X-not-Y cadence. The fallback that was meant
to soften the absence of a fact carries the same failure modes the
verdict is supposed to prevent.

## Full captured critique

Stored in `evals/results/2026-05-28-joe-beda-after.md` and the matching
after-run in `evals/results/2026-05-28-rewrite-check-after.md` for
side-by-side comparison.
