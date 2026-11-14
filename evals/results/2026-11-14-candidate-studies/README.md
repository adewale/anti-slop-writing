# Candidate screening — completed; no doctrine promoted

**1,122 apply outputs, 2,244 valid judgments, 3,382 unique returned provider responses.**
The extra 16 responses were schema-invalid Opus judgments, retained and replaced under
the fixed policy. All required slots, literal prompts, models, packages, blinding,
word counts and judgment coverage passed audit. Archive replay reproduces the analyses
byte-for-byte without model calls.

**Neither candidate cleared any of its eight standing-holdout co-primary contrasts.**
Five of 64 registered fact-condition point guards failed. Positive target-panel estimates
are one-scaffold observations, not independent replications or a general improvement.
The frozen design prohibited promotion regardless; the installed skill remains unchanged.

## Design and scope

Frozen base: merged #22 at `92d37020c39da5f5f497b550f62997539318137b`. Registration
commit: `8c39ca543e33b8fbabe10424ac11fe7946f4d4b7`. See
[PREREGISTRATION.md](PREREGISTRATION.md), [DESIGN-REVIEW.md](DESIGN-REVIEW.md),
`design-summary.json` and `power-scenarios.json`.

- Apply: Sonnet 5.5 and GPT-6.1 Sol. Judges: Opus 5.5 and GPT-6.1 Sol, every output.
- Standing: 69 cases, four arms, one trial/arm/apply model. It includes 61 review/rewrite
  cases plus eight antithesis/control cases, with 18 conservative families; 15 public
  historical holdout cases span nine families.
- Compound: 7 cases / three arms / three trials. Teaser: 12 / three / three.
  Twitter: 8 / two / three. Highlighter: 11 / two / three.
- Each branch panel is **one source/scaffold family**. Repeats, twins, judges and models
  do not manufacture independent cases. Target-panel exact gate power is zero at this
  allocation. These public historical holdouts are design-visible, not fresh sealed data.
- Compound and teaser are minimal repo-only patches, not wholesale validation of their
  source branches. Twitter and highlighter compare current/no skill: neither adds doctrine.
  Six supplied-fact tune twins test against asking/cutting indiscriminately. Three defective
  highlighter historical holdouts were quarantined before generation, with originals kept.

The two co-primary outcomes are fidelity and substantive task fulfillment, normalized
`(score − 1) / 4`. A third uniformly elicited dimension, rewrite quality, is secondary.
Trials become case means, then equally weighted family means. Template artifacts are
not primary credit. Full-package inline exposure is not live client activation.

## Results

The ranges below span the **four separate apply-model/judge estimates**, not confidence
intervals. Every branch-panel inferential verdict is UNDERPOWERED.

| Panel | Contrast | Fidelity delta range | Task delta range |
|---|---|---:|---:|
| Compound | candidate − current | +.048 to +.131 | +.107 to +.190 |
| Teaser | candidate − current | −.014 to +.042 | −.056 to +.035 |
| Twitter | current − no skill | +.063 to +.198 | +.115 to +.208 |
| Highlighter | current − no skill | .000 to +.129 | +.083 to +.159 |

The compound patch is a directionally positive **bounded lead**, not a validated detector.
The teaser effect is mixed. Coverage gains under the current skill do not establish that
new Twitter/highlighter doctrine is needed. The case-only Twitter port subsequently
landed in #28, preserving all eight original behavioral records and splits; it does not
change this frozen study's allocation or independence.

On all 69 standing cases, candidate-minus-current co-primary estimates were:

| Apply / judge | Compound fidelity | Compound task | Teaser fidelity | Teaser task |
|---|---:|---:|---:|---:|
| Sonnet / Opus | +.030 | +.008 | +.038 | −.003 |
| Sonnet / GPT | −.008 | +.034 | +.023 | +.006 |
| GPT / Opus | +.013 | +.011 | +.007 | +.011 |
| GPT / GPT | −.015 | +.008 | −.028 | −.007 |

All 16 all-case co-primary rows are REJECT; all eight standing-holdout rows per candidate
are also REJECT. Failure to show superiority is not equivalence. `MODEL-TABLES.md`
contains every apply/judge all-case and holdout contrast, including current/no-skill;
`comparisons.json` retains intervals, sign-flip tests and every target/guard/fact selection.

### Required guards and individual losses

Five of 64 point guards failed:
- Compound's supplied-definition case, `coined-compound-label-with-facts`: secondary
  rewrite quality −.083 for Sonnet/GPT-judge, GPT/Opus-judge and GPT/GPT-judge.
- Teaser supplied-fact selection: Sonnet/Opus-judge unsupported-claim rate +.333.
- Standing no-additional-facts selection: GPT/GPT-judge teaser unsupported-claim rate +.118.

These are descriptive point guards, not powered harm tests. Do not conclude a universal
harm mechanism from a small supplied-fact panel. `guard-results.json` gives all passes
and failures. `standing-regressions.json` lists **199 case/model/judge/dimension decreases**
across the two candidates, not 199 independent cases; these one-trial standing decreases
are not replicated estimates of regression risk. Absolute scores remain in `case-scores.json`.

### Length and judge disagreement

Standing raw mean words, no skill → current → compound → teaser:
- Sonnet: **123.0 → 321.4 → 328.7 → 312.2**.
- GPT: **79.8 → 143.0 → 138.8 → 138.7**.

Blinding removes self-check/remembered-line fields but leaves critique/style and length
cues. It does not resolve length confounding. Fidelity exact judge agreement was **45.3%**
on Sonnet outputs and **70.9%** on GPT outputs. Opus minus GPT judge mean fidelity was
+.535 and −.048 ordinal points respectively. This motivates human calibration, not choosing
the more favorable judge. The separate baseline calibration packet still awaits a human.

## Accounting, amendment and reproduction

The run lasted **96m 09s** (09:03:55–10:40:04 UTC). No apply failures occurred. All 16
replacement attempts were Opus judge failures: 15 JSON-parse failures and one incomplete
dimension set. Their complete provider responses and costs remain in the archive;
none were replaced because the writing or score was unfavorable. Returned list-price
counters total **$86.22**, not a subscription invoice or API expenditure. All 3,382 returned
responses have distinct IDs; exactly 3,366 distinct selected responses fill the study.
These counters cover retained trial attempts, not earlier access probes or design/review
calls outside this registered runtime.

[ANALYSIS-AMENDMENT.md](ANALYSIS-AMENDMENT.md), committed before numerical analysis but
after model scoring began, adds an explicit standing-decrease export and verifies complete
point-guard outcome coverage. It does not change scores, thresholds or prompts. Original
generation hashes and actual analysis hashes are both retained. Do not call this an
unamended confirmatory experiment.

```bash
python3 scripts/verify_followthrough.py verify --kind candidate \
  --dest evals/results/2026-11-14-candidate-studies
```

Use the publication commit so code matches `analysis-sources.json`. Verification checks
published checksums, extracts `trials.tar.gz`, checks source hashes and unique response
receipts, reruns raw/prompt/worklist audits, grading, statistical analyses and guard/length/
regression exports, then requires byte-identical reproduced files. The model invocation
entry point is trapped to fail. `reproduction.json` records the checked files; it and the
checksum inventory exclude themselves from self-hashing. No credentials are archived.

**Decision:** do not merge either doctrine candidate or the broad original #18 patch.
Keep the bounded compound lead and all null/harmful observations for a future independently
sourced, prospectively powered study. No metadata or doctrine was tuned to holdout failures.
