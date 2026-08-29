# Scored A/B run over the 2026-08-29 additions

Date: 2026-08-29. Pre-registered in `2026-08-29-scored-run/pre-registration.md` (committed before any output was generated): SESOI 0.05, 13 paired cases (8 tune / 5 holdout), Sonnet apply in both arms, blinded Opus+Haiku judge panel, deterministic checks merged, gate = `score_delta.py` ACCEPT on holdout for both judges.

Arms: **A** = doctrine at `53370ff` (pre-mining snapshot, `doctrine-A/`); **B** = post-mining doctrine. Judges graded neutral `outputs-x`/`outputs-y` dirs; mapping (`x`=A, `y`=B) recorded in `arm-mapping.json`, withheld from judge prompts.

## Verdict under the pre-registered rule

**No measured improvement is claimed.** All four gates REJECT (95% CI on the mean per-case delta overlaps zero):

| Gate | Cases | Mean delta | 95% CI | p (sign-flip) | Verdict |
|---|---:|---:|---|---:|---|
| Opus, all | 13 | +0.1346 | [+0.0000, +0.2757] | 0.1251 | REJECT |
| Opus, holdout | 5 | +0.0500 | [-0.1500, +0.2500] | 0.7447 | REJECT |
| Haiku, all | 13 | +0.1026 | [+0.0000, +0.2179] | 0.2512 | REJECT |
| Haiku, holdout | 5 | +0.1000 | [+0.0000, +0.3000] | 1.0000 | REJECT |

Equivalence is **also not shown** (TOST at SESOI ±0.05): the 90% CIs are entirely positive — Opus [+0.0192, +0.2564], Haiku [+0.0256, +0.1923]. The honest reading is a *suggestive positive effect that this N cannot confirm at the pre-registered bar*: every mean is positive, both judges independently move the same three cases, and only one of 26 per-case deltas is negative — but 13 paired cases (5 holdout) is underpowered for a 95% paired-bootstrap gate, exactly the small-N behavior the runbook's cited literature predicts. Per pre-registration, the claim this round makes is **coverage, not measured improvement**; the run doubles as the recorded baseline for the next round.

## Where the movement is (both judges agree)

| Case | Split | Opus Δ | Haiku Δ | What changed |
|---|---|---:|---:|---|
| `strip-new-register-launch` | tune | +0.500 | +0.500 | Arm A's rewrite kept "Zero config", "fits in your head", and the negation chain (deterministic FAILs); arm B's is clean and checkable. |
| `structural-cadence-run` | tune | +0.333 | +0.333 | Arm A kept the stranded auxiliary ("; the fix didn't.") — flagged by lint and by Opus independently. |
| `holdout-stage-managed-postmortem` | holdout | +0.333 | +0.500 | Arm A opened on "Turns out" and kept the "is dead" obituary (0/3 with Opus); arm B removed the reveal framing. |

The deterministic layer alone separates the arms with zero judge tokens: **arm A passes 3/7 deterministic-check cases, arm B 6/7** (`judgments-*/lint.jsonl`), and Opus's textual findings on arm A name the same reused phrases the regexes caught — the two graders corroborate each other from independent evidence.

Adversarial keep-cases: 1.000 in both arms under both judges — non-discriminating, as pre-registered. That is the intended reading: the new detectors did **not** introduce over-flagging; the old doctrine's restraint already kept earned uses, and the new one still does.

## Findings the gate does not capture

1. **Arm B holdout miss (deterministic):** `holdout-devblog-boilerplate` — the new-doctrine rewrite still reused "fits in your head" (lint FAIL; 0.800 with both judges). Per the runbook, no doctrine edit this round; queued as a next-round tune case in `TODO.md`.
2. **One negative delta:** Opus scored arm B's `holdout-oracle-drift-review` 0.667 vs arm A's 1.000 (B's answer skipped the re-profiling recommendation; Haiku disagreed and passed it). Holdout → logged, not acted on.
3. **Mis-specified tune assertion (our bug, exposed by the run):** `structural-cadence-run` assertion 3 demands "at least one verified finding" from a source excerpt that contains no evidence to verify — satisfiable only by inventing, which the doctrine forbids. Opus failed arm B for honestly declining to invent. Fix the assertion wording next round (tune case, so editable) to accept verified-or-explicitly-requested findings.
4. **Reference contamination (our bug, disclosed):** the 2026-08-29 additions to `references/rewrite-patterns.md` used the same source passages as two tune cases, so arm B's references contained worked answers for them. Observed effect: none visible (`performative-honesty-stage-management` Δ=0 under both judges; the arm-B apply agent reported declining to copy the reference rewrites because they invent facts) — but the two tune deltas are discounted on principle. No holdout passage appears in any reference, so the gate is unaffected. Fixed post-scoring: the reference examples now use non-eval passages with invention-honest specifics.
5. **Judge disagreements (flagged, not averaged):** arm x — `new-register-significance-compression`, `holdout-therapy-voice-retro`, `deterministic-vs-judge-split`; arm y — `new-register-significance-compression`, `structural-cadence-run`, `holdout-oracle-drift-review`. Haiku is uniformly the more lenient judge; both judges are Claude-family (pre-registered limitation).
6. **Saturation:** arm-B panel index 0.615 — 8/13 cases at ceiling across judges (`saturation-y.txt`), including all four adversarial guards. Zero-deltas there are no-regression evidence only; the suite needs harder variants before the next scored round can detect anything on them.
7. **Repair note:** one Haiku judgment line contained unescaped quotes and was repaired to parse (escaping only; judgment content untouched). Recorded in `run-metadata.json`.

## Artifacts

Everything under `evals/results/2026-08-29-scored-run/`: `pre-registration.md`, `doctrine-A/` snapshot, `apply-work/`, `outputs-x|y/` (26 outputs), `judgments-x|y/` (per-judge JSONL + `lint.jsonl`), `scores-*-{opus,haiku}[-graded].jsonl`, `delta-{opus,haiku}.jsonl`, `gate-*.txt`, `saturation-y.txt`, `arm-mapping.json`, `run-metadata.json`.

Commands: `run_evals.py lint` → `grade` (judge + lint rows merged per case) → `join` → `score_delta.py [--holdout-only|--sesoi 0.05]` → `saturation_index.py`.

## Next round (queued in TODO.md)

- Harden or vary the 8 ceiling cases; add a second generation per case so run-to-run variance is measurable.
- Fix `structural-cadence-run` assertion 3 (verified-or-requested wording).
- New tune case from the `holdout-devblog-boilerplate` miss ("fits in your head" reuse under the new doctrine).
- More cases or a repeat-run design before re-attempting the 95% gate: at the observed effect size (~+0.10), N=13 cannot clear it.
