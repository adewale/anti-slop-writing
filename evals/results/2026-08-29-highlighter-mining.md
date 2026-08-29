# Eval results — highlighter mining and the deterministic grading layer

Date: 2026-08-29

## What changed

Diffing an external detector catalog — Simon Willison's llm-cliche-highlighter (simonw/tools, Apache-2.0) — against the doctrine showed all 27 of its conversational-register patterns absent from `SKILL.md`: the lists tracked the 2023-24 essay register while the model register had moved. The round followed the 2026-05-27 TDD sequence (eval contract first, doctrine second) and additionally ported the highlighter's design as a deterministic grading layer.

### New evals (RED step)

- `evals/evals.json`: `new-register-significance-compression`, `performative-honesty-stage-management`, `structural-cadence-run` (tune); `holdout-devblog-boilerplate`, `holdout-therapy-voice-retro` (holdout)
- `evals/adversarial.json`: `earned-negation-chain-changelog`, `earned-turns-out-with-trace`, `earned-anaphora-invariant-chain` (tune); `holdout-earned-honesty-clarification` (holdout)
- `evals/rewrite-evals.json`: `strip-new-register-launch` (tune); `holdout-stage-managed-postmortem` (holdout)
- `evals/meta-evals.json`: `deterministic-vs-judge-split` (tune); `holdout-oracle-drift-review` (holdout)
- `evals/cases.md`: cases 11 (new-register conversational slop), 12 (structural cadence run)
- `evals/failures/new-register-conversational-slop.md`, `examples/cards/new-register-launch-copy.md`

### Doctrine updates (GREEN step)

- `skills/anti-slop-writing/SKILL.md`: two detector entries (new-register families with dose-response framing; structural cadence with the earned-use boundary), nine avoid-phrases, five high-risk words, drift-note extension. Net +197 words against the +200/round budget after consolidating the `Not just/only X` near-duplicates.
- `skills/anti-slop-writing/references/anti-slop-writing-doctrine.md`: "New-register tells and structural cadence" section with the four earned-use keep examples and provenance.
- `skills/anti-slop-writing/references/rewrite-patterns.md`: fact-extraction and cadence-to-findings rewrite moves.

### Deterministic grading layer

- `evals/oracles/slop_lint.py`: 22 detectors (6 structural, 5 new-register, 11 Wikipedia-register), dose-response severity, ~130 embedded positive+negative self-test cases, demo fixture that must trip every detector exactly once.
- `scripts/run_evals.py lint` + `deterministic_checks` blocks on cases + judge/lint row merging in `grade`; validation of check shapes and oracle self-tests in `scripts/validate.py`; protocol in `docs/judge-protocol.md` Phase 2.5 and `docs/deterministic-graders.md`.

## Deterministic verification captured in this round

All of the following are reproducible from the repo with no model call:

- `python3 evals/oracles/slop_lint.py --self-test` — 160 checks pass: ~130 positive/negative pattern cases (negatives pin the false-positive boundaries: "Old Testament", "real estate", "naming names", "Dr. Chen argued"), the demo-fixture assertion (every detector trips exactly once on `evals/fixtures/slop-lint-demo/input.md`), and the check-engine/scope-extraction tests. Runs inside `scripts/validate.py`.
- The card `examples/cards/new-register-launch-copy.md` is lint-verified: 6 findings on the Before text (no-chain, devblog-boilerplate ×3, performative-honesty, significance-compression), 0 on the After.
- The hypothesis-vs-verdict division is demonstrated on the four earned-use adversarial inputs: each trips exactly its corresponding detector (`no-chain`, `stage-management`, `sentence-anaphora`, `performative-honesty`) under the oracle, while the adversarial assertions require the skill's judgment to keep the line. The oracle supplies recall; the judgment layer supplies the verdict.
- Pipeline behavior was verified end-to-end on synthetic outputs: a clean rewrite passes its five forbid checks; a deliberately sloppy rewrite fails with quoted evidence ("Turns out", "That's not nothing"); a critique that quotes the tells it flags passes its `scope: "rewrite"` checks while the same checks at full scope fail; `grade` merges a judge row and a lint row for one case into a single scored record.

## Deterministic smoke run over the new tune cases

Recorded in `evals/results/2026-08-29-highlighter-mining/` (outputs, judgments/lint.jsonl, scores.jsonl). Two fresh apply sub-agents (per `docs/judge-protocol.md` Phase 1: one per suite, SKILL.md and references only, assertions withheld — both confirmed they read nothing under `evals/`) produced outputs for the four new tune cases carrying `deterministic_checks`; `run_evals.py lint --split tune` graded them with no judge.

Result: **4/4 cases pass all 12 deterministic checks** (tune mean 1.000, all_pass 4/4).

| Case | Suite | Checks | Result |
|---|---|---|---|
| `new-register-significance-compression` | evals.json | significance-compression, therapy-voice = 0 hits in rewrite scope | 2/2 |
| `performative-honesty-stage-management` | evals.json | performative-honesty, stage-management = 0 hits in rewrite scope | 2/2 |
| `structural-cadence-run` | evals.json | sentence-anaphora, stacked-questions, stranded-auxiliary = 0 hits in rewrite scope | 3/3 |
| `strip-new-register-launch` | rewrite-evals.json | no-chain, devblog-boilerplate, performative-honesty, significance-compression, not-just-but = 0 hits | 5/5 |

Read as: with the updated doctrine loaded, fresh outputs do not reuse the flagged cadence — the executable form of the `Rewrite check` rule, verified at zero token cost on the grading side. This is a tune-split smoke, not the round's score gate; holdout cases were not run (they are scored at end-of-round/merge under the full protocol).

## What is and is not measured here

`python3 scripts/validate.py` is green over the expanded suites, and every deterministic claim above is machine-checked. What this round does **not** claim: a measured doctrine improvement. The natural-language assertions on the 13 new cases still need the full apply/judge/grade pass with the cross-family discipline, a `score_delta.py` gate for any close call, and holdout scoring at end-of-round — tracked in `TODO.md`. Per the 2026-05-27 precedent, this note records coverage expansion; the scored baseline over the new cases is the next measurement step.

## Source attribution

- Detector regexes, structural finder algorithms, and many self-test sentences: [simonw/tools llm-cliche-highlighter](https://github.com/simonw/tools/blob/main/llm-cliche-highlighter.html) (Apache-2.0, Copyright Simon Willison), attributed in the `slop_lint.py` module docstring.
- The highlighter's second pattern group derives from [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), which the 2026-05-27 round had already mined for the essay-register detectors; the conversational-register families are the delta.
- Eval-case provenance uses the `source` field convention introduced by the stop-slop imports (2026-06-14).
