# Re-run results

Primary judge `claude-sonnet-5`, secondary judge `claude-haiku-4-5-20251001`.

| Case | Split | Arm | Trials | Mean score, primary | First assertion, primary | Mean score, secondary | First assertion, secondary |
|---|---|---|---:|---:|---:|---:|---:|
| coined-compound-label | tune | baseline | 40 | 0.042 | 4/40 | 0.342 | 7/40 |
| coined-compound-label | tune | candidate | 40 | 0.975 | 40/40 | 1.000 | 40/40 |
| coined-label-defined-in-place | tune | baseline | 8 | 1.000 | 8/8 | 1.000 | 8/8 |
| coined-label-defined-in-place | tune | candidate | 8 | 1.000 | 8/8 | 1.000 | 8/8 |
| earned-domain-compound | tune | baseline | 8 | 0.750 | 3/8 | 0.792 | 3/8 |
| earned-domain-compound | tune | candidate | 8 | 0.792 | 5/8 | 0.792 | 5/8 |
| holdout-coined-compound-label | holdout | baseline | 40 | 0.058 | 1/40 | 0.283 | 3/40 |
| holdout-coined-compound-label | holdout | candidate | 40 | 0.975 | 40/40 | 0.975 | 40/40 |
| holdout-coined-label-defined-in-place | holdout | baseline | 8 | 1.000 | 8/8 | 1.000 | 8/8 |
| holdout-coined-label-defined-in-place | holdout | candidate | 8 | 1.000 | 8/8 | 1.000 | 8/8 |
| holdout-earned-domain-compound | holdout | baseline | 8 | 0.875 | 6/8 | 0.917 | 6/8 |
| holdout-earned-domain-compound | holdout | candidate | 8 | 0.958 | 7/8 | 0.917 | 7/8 |

Judge agreement: 597/672 assertions.

### Gate: coined-compound-label (tune), sonnet judge

```txt
Split:         all-cases
Cases:         40
Mean delta:    +0.9333
95% CI:        [+0.8833, +0.9750]
Sign-flip p:   0.0001
SESOI:         +/-0.0500
TOST 90% CI:   [+0.8917, +0.9750]
Equivalence:   NOT SHOWN (CI exceeds +/-0.0500; cannot rule out an effect this large).
Verdict:       ACCEPT (improvement clears the noise floor).
```

### Gate: holdout-coined-compound-label (holdout), sonnet judge

```txt
Split:         holdout-only
Cases:         40
Mean delta:    +0.9167
95% CI:        [+0.8500, +0.9667]
Sign-flip p:   0.0001
SESOI:         +/-0.0500
TOST 90% CI:   [+0.8667, +0.9667]
Equivalence:   NOT SHOWN (CI exceeds +/-0.0500; cannot rule out an effect this large).
Verdict:       ACCEPT (improvement clears the noise floor).
```

### Gate: coined-compound-label (tune), haiku judge

```txt
Split:         all-cases
Cases:         40
Mean delta:    +0.6583
95% CI:        [+0.5500, +0.7583]
Sign-flip p:   0.0001
SESOI:         +/-0.0500
TOST 90% CI:   [+0.5667, +0.7500]
Equivalence:   NOT SHOWN (CI exceeds +/-0.0500; cannot rule out an effect this large).
Verdict:       ACCEPT (improvement clears the noise floor).
```

### Gate: holdout-coined-compound-label (holdout), haiku judge

```txt
Split:         holdout-only
Cases:         40
Mean delta:    +0.6917
95% CI:        [+0.6083, +0.7750]
Sign-flip p:   0.0001
SESOI:         +/-0.0500
TOST 90% CI:   [+0.6167, +0.7583]
Equivalence:   NOT SHOWN (CI exceeds +/-0.0500; cannot rule out an effect this large).
Verdict:       ACCEPT (improvement clears the noise floor).
```

## Guards

| Guard | Baseline over-flags | Candidate over-flags | Within limit |
|---|---:|---:|---|
| coined-label-defined-in-place | 0/8 | 0/8 | yes |
| earned-domain-compound | 5/8 | 3/8 | yes |
| holdout-coined-label-defined-in-place | 0/8 | 0/8 | yes |
| holdout-earned-domain-compound | 2/8 | 1/8 | yes |

## Decision

- Tune gate, primary judge: ACCEPT
- Holdout gate, primary judge: ACCEPT
- Guards within limit: yes
- Secondary judge's gate verdicts agree: yes
- Pre-registered outcome: SHIP candidate-v3
