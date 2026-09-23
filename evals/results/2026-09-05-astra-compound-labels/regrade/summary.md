# Regrade summary

Primary judge `claude-sonnet-5`; secondary judge `claude-haiku-4-5-20251001`. Case score is the
fraction of the case's assertions passed. `a1` is the first assertion: for the
discriminating cases, naming the coinage as coined or undefined; for the guards, keeping the text.

| Case | Arm | Model | Trials | Status | Mean score, primary | a1, primary | Mean score, secondary | a1, secondary |
|---|---|---|---:|---|---:|---:|---:|---:|
| P1 | baseline | claude-haiku-4-5-20251001 | 1 | valid | 0.67 | 1/1 | 1.00 | 1/1 |
| P1 | baseline | claude-opus-5 | 1 | valid | 1.00 | 1/1 | 1.00 | 1/1 |
| P1 | baseline | claude-sonnet-5 | 4 | excluded | 0.25 | 1/4 | 0.50 | 2/4 |
| P1 | baseline | claude-sonnet-5 | 4 | valid | 0.50 | 2/4 | 0.58 | 2/4 |
| P1 | candidate | claude-sonnet-5 | 4 | excluded | 1.00 | 4/4 | 1.00 | 4/4 |
| P1 | candidate | claude-sonnet-5 | 4 | valid | 0.92 | 4/4 | 1.00 | 4/4 |
| P2 | baseline | claude-haiku-4-5-20251001 | 1 | valid | 1.00 | 1/1 | 1.00 | 1/1 |
| P2 | baseline | claude-opus-5 | 1 | valid | 1.00 | 1/1 | 1.00 | 1/1 |
| P2 | baseline | claude-sonnet-5 | 4 | valid | 1.00 | 4/4 | 1.00 | 4/4 |
| P2 | candidate | claude-sonnet-5 | 4 | valid | 1.00 | 4/4 | 1.00 | 4/4 |
| P3 | baseline | claude-haiku-4-5-20251001 | 1 | valid | 1.00 | 1/1 | 1.00 | 1/1 |
| P3 | baseline | claude-opus-5 | 1 | valid | 1.00 | 1/1 | 1.00 | 1/1 |
| P3 | baseline | claude-sonnet-5 | 4 | valid | 1.00 | 4/4 | 1.00 | 4/4 |
| P3 | candidate | claude-sonnet-5 | 4 | valid | 1.00 | 4/4 | 1.00 | 4/4 |
| P4 | baseline | claude-sonnet-5 | 4 | secondary | 0.42 | 2/4 | 0.58 | 2/4 |
| P4 | candidate-v2 | claude-sonnet-5 | 4 | secondary | 0.75 | 3/4 | 0.83 | 3/4 |

Judge agreement: 127/138 assertions, 43/46 on the first assertion.

### Gate: sonnet round1-design

```txt
Split:         all-cases
Cases:         12
Mean delta:    +0.1389
95% CI:        [+0.0000, +0.3333]
Sign-flip p:   0.5057
SESOI:         +/-0.0500
TOST 90% CI:   [+0.0000, +0.3056]
Equivalence:   NOT SHOWN (CI exceeds +/-0.0500; cannot rule out an effect this large).
Verdict:       REJECT (CI overlaps zero; delta is within noise).
```

### Gate: sonnet round1-p1

```txt
Split:         all-cases
Cases:         4
Mean delta:    +0.4167
95% CI:        [+0.0000, +0.8334]
Sign-flip p:   0.4995
SESOI:         +/-0.0500
TOST 90% CI:   [+0.0000, +0.7500]
Equivalence:   NOT SHOWN (CI exceeds +/-0.0500; cannot rule out an effect this large).
Verdict:       REJECT (CI overlaps zero; delta is within noise).
```

### Gate: sonnet round1-design holdout-only

```txt
Split:         holdout-only
Cases:         4
Mean delta:    +0.0000
95% CI:        [+0.0000, +0.0000]
Sign-flip p:   1.0000
SESOI:         +/-0.0500
TOST 90% CI:   [+0.0000, +0.0000]
Equivalence:   EQUIVALENT (CI within +/-0.0500; no effect of practical size).
Verdict:       REJECT (CI overlaps zero; delta is within noise).
```

### Gate: haiku round1-design

```txt
Split:         all-cases
Cases:         12
Mean delta:    +0.1389
95% CI:        [+0.0000, +0.3334]
Sign-flip p:   0.5057
SESOI:         +/-0.0500
TOST 90% CI:   [+0.0000, +0.3056]
Equivalence:   NOT SHOWN (CI exceeds +/-0.0500; cannot rule out an effect this large).
Verdict:       REJECT (CI overlaps zero; delta is within noise).
```

### Gate: haiku round1-p1

```txt
Split:         all-cases
Cases:         4
Mean delta:    +0.4167
95% CI:        [+0.0000, +0.8334]
Sign-flip p:   0.4995
SESOI:         +/-0.0500
TOST 90% CI:   [+0.0000, +0.7500]
Equivalence:   NOT SHOWN (CI exceeds +/-0.0500; cannot rule out an effect this large).
Verdict:       REJECT (CI overlaps zero; delta is within noise).
```

### Gate: haiku round1-design holdout-only

```txt
Split:         holdout-only
Cases:         4
Mean delta:    +0.0000
95% CI:        [+0.0000, +0.0000]
Sign-flip p:   1.0000
SESOI:         +/-0.0500
TOST 90% CI:   [+0.0000, +0.0000]
Equivalence:   EQUIVALENT (CI within +/-0.0500; no effect of practical size).
Verdict:       REJECT (CI overlaps zero; delta is within noise).
```

