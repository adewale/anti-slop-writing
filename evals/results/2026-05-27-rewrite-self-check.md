# Rewrite self-check — A/B result

Date: 2026-05-27
Branch: `claude/thinking-out-loud-feedback-acAqK`
Baseline commit (without-skill artifact): `6137ab9`
Change commit (with-skill artifact): `50df33e`

## Method

Two fresh-context subagents produced rewrites for the two new rewrite-eval
prompts:

- `rewrite-reuses-flagged-pattern`
- `rewrite-asks-or-cuts-when-fact-missing`

The **without-skill** agent received only the eval prompts and was told
not to read any repository files. The **with-skill** agent was told to
read `skills/anti-slop-writing/SKILL.md` and
`skills/anti-slop-writing/references/rewrite-patterns.md` in full and
apply the doctrine, including the extended Final self-check added in
this branch. Both agents replied with rewrites only, in a fixed format.

Each rewrite was then judged against the four assertions in
`evals/rewrite-evals.json` for its case.

## Captured rewrites

### Case 1 — `rewrite-reuses-flagged-pattern`

Prompt: *"You correctly flagged this line as compressed antithesis hiding
the mechanism: 'That's not incidental. It's the design.' Now produce a
rewrite that names the mechanism. Do not reuse the same contrast shape
with different punctuation."*

Without-skill:

```txt
The system routes every failed request through the same retry queue
that handles new traffic, which is what produces the latency spikes
during partial outages.
```

With-skill:

```txt
The repo ships with a failing test for the exact bug it patches, so
anyone reviewing can run it red, apply the fix, and watch it go green.
```

### Case 2 — `rewrite-asks-or-cuts-when-fact-missing`

Prompt: *"Rewrite this sentence so it is concrete: 'Current coding tools
made it practical to add features that would otherwise get cut.' You have
no information about which tool the author used or what the timing was
before and after."*

Without-skill:

```txt
Please tell me which coding tool you used and roughly how long the
relevant tasks took before and after adopting it, so I can rewrite the
sentence with concrete numbers; without that, the honest version is
simply "We added features we would otherwise have cut."
```

With-skill:

```txt
Current coding tools made it practical to add features that would
otherwise get cut. [Author: which tool, and how much faster was the
relevant task? Without that, recommend cutting this sentence.]
```

## Scores

| Case | Assertion | Without skill | With skill |
|---|---|:---:|:---:|
| 1 | A1: no `X isn't A — it's B` shape | pass | pass |
| 1 | A2: no substituted parallel-clause contrast | pass | pass |
| 1 | A3: names a mechanism | pass | pass |
| 1 | A4: asks/cuts when fact missing | **fail** | **fail** |
| 2 | A1: no invented tool name | pass | pass |
| 2 | A2: no invented timing/benchmark | pass | pass |
| 2 | A3: asks for missing fact or recommends cutting | pass | pass |
| 2 | A4: no vague-abstraction substitute | pass | pass |
| **Total** | | **7/8** | **7/8** |

## Assessment

The new doctrine did not move the metric on this run. Both agents scored
7/8, failing the same assertion (Case 1, A4) for the same reason: the
source line "That's not incidental. It's the design." has no referent
for "design" in the prompt, so the correct behavior under the new
doctrine is to ask the author what design is being referred to, or
recommend cutting. Both agents instead invented a concrete carrier and
ran with it. The with-skill agent picked a different invented carrier
(failing test for a bug fix) than the without-skill agent (retry queue
under partial outage), but both substituted invention for inquiry.

This is a useful negative result. Two follow-ups worth pursuing:

1. **Eval-prompt weakness.** Both eval prompts embed the rule directly
   ("Do not reuse the same contrast shape"; "You have no information").
   A strong model can comply with the in-prompt instruction without
   needing the SKILL.md doctrine, which compresses the gap the eval was
   meant to detect. Case 2's perfect score on both arms is consistent
   with this: the prompt named the missing facts explicitly, so both
   agents asked or cut. A harder variant would strip the rule from the
   prompt and rely on the doctrine to supply it.

2. **Case 1 caught a real gap the new doctrine did not close.** The
   added self-check question asks whether a rewrite needs a fact the
   source did not supply. Neither agent escalated "what does 'design'
   refer to?" to that question — both treated "name the mechanism" as
   permission to invent one. The doctrine rule may need to be stricter,
   or a separate detector is needed for the case where the source line
   itself is missing the referent, not just the supporting numbers.

## What moved, what didn't

- **Score:** unchanged (7/8 vs 7/8 on this two-case A/B).
- **Eval coverage:** moved. The suite now contains two cases that
  previously had no equivalent assertions, and one of them
  (`rewrite-reuses-flagged-pattern` A4) is currently being failed by
  both arms, which means the suite distinguishes desired behavior from
  observed behavior.
- **Doctrine surface:** moved. The Final self-check now carries two new
  questions, even though the questions did not translate into observed
  behavior on this run.

## Next step

Author a tighter Case 1 variant whose prompt removes the embedded
instruction and tests whether the doctrine alone produces ask-or-cut
behavior when the source line itself is missing a referent. File the
result under `evals/results/` and link it from `LESSONS.md` if the
stricter variant exposes a doctrine gap.
