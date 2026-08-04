# Failure: Self-planted strawman contrast

Source: [@stanine, 2026-08-03](https://x.com/stanine/status/2084385000959701146).

## Original

The user's entire message was `why is the deploy slow?`. They did not mention Docker.

```txt
It would be easy to assume the slowness comes from the Docker build. But the build is not the problem. The problem is that the readiness probe waits a fixed 30 seconds before its first check, so every rollout pays that delay once per pod.
```

## Why it failed

Nobody proposed the Docker build. The assistant introduced it, refuted it, and kept the shape of a correction without anyone to correct. The reader is told, falsely, that they were about to believe something.

The staccato contrast test asks the wrong question here, and every answer it can give leads somewhere other than the fix. Its three classifications and their prescribed repairs:

- **Earned** (`both sides evidenced in the prior sentences ... keep or use once`). The assistant's own first sentence supplies the Docker side, and `SKILL.md` adds `read the prior sentence of the same paragraph first. If it supplies the mechanism the contrast points at, the contrast is earned.` Keeping it is wrong.
- **Compressed** (`one side is evidenced; the other side is a leap ... expand into the relation by naming the unsupported side directly`). This is the likelier grade, since the Docker side is hypothesized rather than shown — and its repair is the actively harmful one. It sends the agent to go supply evidence about a build nobody asked about, growing the strawman instead of cutting it.
- **Decorative** (`neither side is evidenced ... cut or replace`). Lands in roughly the right place, for the wrong reason, and `replace` invites swapping in a better-supported version of the same invented contrast.

The classification is about evidence. The defect is about provenance. A premise can be perfectly well evidenced and still be one the writer put in the reader's mouth.

The gap is one of scope. Every contrast case in the suite judges a contrast against the document under review. When the agent is writing a reply, what determines whether Y was ever on the table is the user's message, which sits outside the prose being checked.

## Mechanism

The evidence test asks whether both sides are supported in the prior prose. It never asks who introduced the opposing side. A writer who supplies the opposition themselves can pass the evidence test at any grade, and no grade's repair is "cut the invented premise."

## Better rewrite

```txt
The readiness probe waits a fixed 30 seconds before its first check, so every rollout pays that delay once per pod.
```

## Boundary

When the alternative came from the user, the negation is required, not manufactured. If the user asks `is this a memory leak?`, the answer should say `This is not a memory leak` and then give the arena-allocator explanation. Dropping the negation leaves the question unanswered.

## Eval coverage

- `evals/evals.json` -> `self-planted-strawman-contrast` (holdout)
- `evals/rewrite-evals.json` -> `invented-contrast-cut-the-strawman` (holdout)
- `evals/adversarial.json` -> `negation-answers-the-users-hypothesis` (tune)

## Rule added or changed

None yet. If the A/B in `TODO.md` shows the gap is real, the candidate edit is a dialogic scope for the staccato contrast test: before grading a contrast earned, ask who introduced the opposing side, and treat a side the writer supplied themselves as unearned regardless of local evidence.
