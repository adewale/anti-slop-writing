# Deterministic graders

How and when this repo grades eval assertions mechanically instead of with an LLM judge. The oracle is `evals/oracles/slop_lint.py`; the runner integration is `scripts/run_evals.py lint`.

## Why a deterministic layer

The judge protocol (`docs/judge-protocol.md`) has two standing costs: every graded assertion spends sub-agent tokens, and every LLM-graded assertion inherits judge bias — self-preference when apply and judge share a model family (the open cross-family item in `TODO.md`), plus length bias, which for an anti-slop skill rewards exactly the failure the skill targets.

A regex/structural oracle has neither cost. It is free to run, produces identical verdicts on every run, and has no model family to prefer. The 2026-08 source for the approach is Simon Willison's llm-cliche-highlighter (simonw/tools), a single-file tool whose 38 detectors ship with ~190 embedded positive and negative test cases — a deterministic mirror of this repo's `evals.json` + `adversarial.json` split, executed at zero cost.

## Division of labor

The oracle is the recall layer; judgment is the verdict layer.

| Assertion kind | Grader | Why |
|---|---|---|
| The rewrite reuses no flagged surface pattern | oracle (forbid check) | Absence of a surface form is mechanically decidable; this is the `Rewrite check` discipline made executable. |
| Required format slots present (`Verdict:`, `Rewrite check:`) | oracle (regex check) | Format compliance is not a judgment call. |
| The hit is earned vs decorative | judge | Requires reading the evidence around the hit; the four earned-use adversarial cases exist precisely because the oracle flags them. |
| Mechanism named, relation clarified, compression preserved | judge | Quality judgments regex cannot make. |

Two design rules keep the layer honest:

- **Forbid-shaped, not require-shaped.** Deterministic checks almost always assert absence (`max_hits: 0`). A deterministic require check ("output must contain the word retry") is a keyword-stuffing incentive — the exact failure `evals/meta-evals.json` → `metric-artifact-check` guards against. `min_hits` exists in the schema but should stay rare and justified.
- **A hit is a hypothesis.** The oracle flags `no breaking changes, no new dependencies` (a chain) and `Every request… Every trace id…` (anaphora) exactly as it flags their decorative twins. On source text, oracle output is triage input for judgment, never a verdict. Only on *rewrite output*, where the doctrine already forbids reusing flagged cadence, does a hit fail a check directly.

## Wiring

Eval cases opt in with a `deterministic_checks` block (validated by `scripts/validate.py` against the oracle's detector registry):

```json
"deterministic_checks": [
  {"detector": "performative-honesty", "max_hits": 0, "scope": "rewrite"},
  {"regex": "^Rewrite check:", "expect": "present"}
]
```

`scope: "rewrite"` runs the check only on the last `Concrete rewrite:` block of the critique format, so a critique that quotes the tell it is flagging does not fail its own forbid check. Bare-rewrite prompts (`Rewrite without AI slop: …`) use the default full scope.

The run loop gains one phase, between apply and judge (both can also run alone):

```bash
python3 scripts/run_evals.py lint --outputs run/outputs evals/evals.json evals/rewrite-evals.json \
  --out run/judgments/lint.jsonl
python3 scripts/run_evals.py grade run/judgments/*.jsonl --out run/scores.jsonl
```

`lint` emits judgment-shaped rows marked `"deterministic": true`; `grade` merges a lint row with the judge row for the same case id, scoring the checks as additional assertions. A case whose assertions are all deterministic needs no judge at all.

## The oracle itself

22 detectors in three groups (`--list` prints them): six structural finders (negation/did-not chains with item counting, sentence anaphora, stacked questions, echo skeletons, stranded auxiliaries), five new-register families (significance compression, therapy voice, performative honesty, stage management, dev-blog boilerplate), and eleven Wikipedia-register detectors (vocabulary, not-just-but, importance hedging, testament, crucial role, landscape, vague experts, despite-challenges, participle tails, promo boilerplate, chatbot leftovers).

Severity is dose-response where the source data says it should be: `ai-vocabulary` is `soft` with `threshold: 2` — one hit can be coincidence, several is a tell. Hard detectors fail the CLI on one hit; all thresholds are visible in `--list`.

Self-verification, borrowed directly from the highlighter's design:

- ~130 embedded positive **and negative** cases (`--self-test`), the negatives pinning known false-positive boundaries ("Old Testament", "real estate", "naming names", "Dr. Chen argued" — named attribution never matches `vague-experts`).
- A demo fixture (`evals/fixtures/slop-lint-demo/input.md`) engineered to trip **every detector exactly once**, asserted by the self-test — the highlighter's "example text trips every pattern exactly once" idea, which makes the demo a regression test.
- `scripts/validate.py` runs the self-test on every validation, so CI fails if a detector regresses.

## What was deliberately not ported

Three highlighter detectors stayed out: `colon-triple` (its own description warns it is noisy on technical writing — this corpus — and the doctrine's rule-of-three detector covers the judgment-requiring version), `dont-verb-it` (backreference matching, low expected volume), and `is-real` (high false-positive rate on ordinary prose). Adding a detector requires the same discipline as doctrine: a positive case, a negative case, and an eval that proves it belongs.

## Relation to the shared Skill Eval Harness

The shared harness (adewale/skill-eval-harness, manifest `evals/shared-benchmark.json`) already ships the generic mechanism this layer needs externally: `script` assertions — repo-owned oracle commands run with `--allow-scripts`, `{output_dir}` substitution, `pass_exit_code` deciding pass, and an optional `{"score": N, "max_score": M}` stdout line feeding the graded channel. Audit result, 2026-08-29: nothing invented here duplicates missing harness machinery; the split is:

- **Repo-side (stays here)**: the detector registry and self-tests (`evals/oracles/slop_lint.py` — doctrine-coupled, drifts with the skill), the `deterministic_checks` schema on the private suites, and `run_evals.py lint`/merge, which give the sub-agent judge protocol the same capability the harness's `benchmark --allow-scripts` gives shared-benchmark runs.
- **Harness integration (done)**: `evals/oracles/slop_lint_oracle.py`, a thin adapter following `fixture_oracle.py`'s calling convention (`oracle.py {output_dir} CASE_ID`, per-case `CHECKS` table, score line), wired into `evals/shared-benchmark.json` → `pos-new-register-launch-strip` with `"oracle": "strong"` (the harness's tier for deterministic, self-verified oracles; plain `script` defaults to `demo`). Paired with `neg-earned-negation-chain` so the shared benchmark also pins the earned-use boundary.
- **Upstream candidates (proposals only, different repo)**: a declarative detector-check assertion (checks in the assertion payload instead of a per-oracle `CHECKS` table), and consolidating the two oracles' shared scaffolding. Neither blocks anything; both are noted here so the idea is not lost.

## Drift

The word-list detectors are time-dated (see the `delve` note in `SKILL.md`); the structural detectors are the slow-drifting core. `evals/meta-evals.json` → `holdout-oracle-drift-review` pins the correct reading of a detector whose hits fall to zero: probable register drift, not victory. Re-profile before trusting either direction.

## Provenance and license

Detector regexes, the structural finder algorithms, and many self-test sentences are ported or adapted from `llm-cliche-highlighter.html` in [simonw/tools](https://github.com/simonw/tools) (Apache-2.0, Copyright Simon Willison), with the second group tracing to [Wikipedia's "Signs of AI writing"](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing). The port carries attribution in the module docstring; this repo remains MIT, with the adapted material used under Apache-2.0's terms. Eval-case provenance uses the same `source` field convention as the stop-slop imports.
