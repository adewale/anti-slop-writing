# Latest eval results

Date: 2026-05-29 (infrastructure baseline) + 2026-05-28 doctrine added on top

These smoke evals check that the skill catches the repo's regression failures, avoids adversarial false-positive cases, satisfies rewrite-quality assertions, notices eval-suite health problems such as ceiling effects and metric artifacts, and triggers correctly on prose-edit queries while declining on adjacent non-prose ones. They are not a full benchmark with persisted `with_skill/` versus `old_skill/` artifacts or observed multi-run trigger rates.

The 2026-05-29 infrastructure update (tune/holdout split, paired-bootstrap gating, `dynamic_rubric` / `graded_dimensions` schema, judge protocol, rejected-edits graveyard) is now in place. The 2026-05-29 baseline scores were captured against the pre-change doctrine. This PR adds doctrine on top of that baseline — `ask-author` verdict, mandatory `Rewrite check` field, both-sides Staccato test — anchored on real failures from joe.dev/posts/thinking-out-loud and validated for false-positive resistance on a Paul Graham essay. A re-baseline against the new doctrine has not yet been run; the per-iteration counts in `2026-05-28-joe-beda-after.md`, `2026-05-28-rewrite-check-after.md`, and `2026-05-28-generalization-pg.md` are the current evidence.

## Schema and infrastructure (from 2026-05-29 baseline merge)

| Suite | Old count | Tune count | Holdout count (with PG additions) |
|---|---:|---:|---:|
| `evals/evals.json` | 5 | 5 | 3 |
| `evals/adversarial.json` | 12 | 12 | 6 |
| `evals/rewrite-evals.json` | 6 | 6 | 2 |
| `evals/meta-evals.json` | 5 | 5 | 4 |
| `evals/trigger-queries.json` | 20 | 16 | 10 |

Six new `near-neg-` near-miss negatives were added to `trigger-queries.json` (fact-check, link-check, draft-from-bullets, storyboard, slide-export, docx-from-dataset). The docx case is taken from a real production bug, [anthropics/claude-code#43259](https://github.com/anthropics/claude-code/issues/43259).

## Held-out and rewrite-eval additions

- `evals/evals.json` holdout: `fake-precision-unnamed-source`, `stacked-rule-of-three`, `abstract-system-noun-stack`.
- `evals/adversarial.json` holdout: `earned-importance-immediate-mechanism`, `cost-benefit-not-just-earning-the-contrast`, `research-methods-staccato`, `earned-antithesis-synthesis-pg`, `cataphoric-label-defined-in-paragraph`, `escalating-magnitude-triple`.
- `evals/rewrite-evals.json` holdout: `fake-precision-rewrite-finance`, `product-tour-rewrite-developer-tools` — both with `dynamic_rubric` and `graded_dimensions`.
- `evals/meta-evals.json` holdout: `noise-vs-signal-on-small-suite`, `judge-self-preference`, `single-source-overfitting`, `earned-rhetoric-false-positive-rate`.

## Doctrine added on top of the 2026-05-29 baseline (this PR)

The 2026-05-28 sequence is a four-iteration real-content hillclimb on Joe Beda's [Thinking out loud, with a URL I own](https://joe.dev/posts/thinking-out-loud/), followed by a generalization check on Paul Graham's [How to Write Usefully](https://paulgraham.com/useful.html).

| Iteration | Change | Measured effect |
|---|---|---|
| 1 (ask-author verdict) | Added `ask-author` to the Critique output format and a triggering rule in the Default editing pass | Major inventions dropped from ~10 events to 0 on the same post; three worst sites became `ask-author` calls with the actual question stated |
| 2 (Rewrite check field) | Made `Rewrite check` mandatory in the per-item format; added "Rewrites must pass the same detectors" section to `references/rewrite-patterns.md` | Every category of slop the rewrites themselves contained went to 0: rule-of-three with invented members, X-not-Y cadence, em-dash rule-of-three closers, banned decorative closers, ask-author fallbacks that invent. 100% adoption of the new field (7/7 produced rewrites). |
| 3 (retraction) | Clarified the Staccato contrast test with the both-sides rule; retracted a framing error in two earlier result notes | No model behavior change; doctrine made unambiguous. Eval assertion that previously expected `keep` on `That's not incidental. It's the design.` corrected to require `revise` with mechanism-naming rewrite, or `ask-author`. |
| 4 (generalization check) | Ran current doctrine against unseen PG essay; no doctrine change | 0/15 paragraphs over-flagged with per-item both-sides reasoning that still discriminates. Locked in 3 adversarial cases and 2 meta-evals as regression coverage. |

## Assessment

The infrastructure baseline (2026-05-29) put the field's standard defenses in place — tune/holdout split, paired-bootstrap gating, cross-family judging — and the new doctrine on top (this PR) is the first real doctrine work since that baseline. The doctrine changes were tuned against one document (joe.dev) and explicitly stress-tested against unseen prose (PG) for false-positive resistance.

Remaining gaps: a complementary calibration test on a deliberately sloppy real document (true-positive sensitivity); invention by elaboration as a directly-targeted rule; observed multi-run trigger rates in Pi, Claude Code, Codex, and OpenCode; and an end-to-end scored run of the new holdout cases against an actual skill execution under the updated doctrine.

## Previous results

| Date | File |
|---|---|
| 2026-05-25 | `2026-05-25-before.md`, `2026-05-25-after.md`, `2026-05-25-adversarial-expansion.md`, `2026-05-25-runbook-eval-drift.md` |
| 2026-05-27 | `2026-05-27-rewrite-self-check.md` (failed iteration on synthetic prompts, superseded by 2026-05-28 sequence on real content) |
| 2026-05-28 | `2026-05-28-joe-beda-before.md`, `2026-05-28-joe-beda-after.md`, `2026-05-28-rewrite-check-before.md`, `2026-05-28-rewrite-check-after.md`, `2026-05-28-generalization-pg.md` |
| 2026-05-29 | `2026-05-29-baseline.md` and `baseline-2026-05-29/` |
| 2026-05-30 | `2026-05-30-rebaseline.md` and `rebaseline-2026-05-30/` (holdout-only re-baseline under updated doctrine: 15/15 cases all-pass, no regression on the 10 joinable cases, the 5 net-new cases pass) |
