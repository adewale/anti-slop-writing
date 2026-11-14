# Candidate model/judge tables

Normalized after−before deltas. Full intervals, exact tests and all fact/target/guard selections remain in comparisons.json. One-family panels are UNDERPOWERED; their bootstrap intervals do not establish precision.

## compound: current → compound, all

| Apply | Judge | Cases | Families | Δ fidelity | Δ task | Δ rewrite quality | Fidelity gate | Task gate |
|---|---|---:|---:|---:|---:|---:|---|---|
| sonnet | opus | 7 | 1 | +0.131 | +0.190 | +0.131 | UNDERPOWERED | UNDERPOWERED |
| sonnet | sol | 7 | 1 | +0.048 | +0.107 | +0.071 | UNDERPOWERED | UNDERPOWERED |
| sol | opus | 7 | 1 | +0.095 | +0.143 | +0.107 | UNDERPOWERED | UNDERPOWERED |
| sol | sol | 7 | 1 | +0.107 | +0.143 | +0.167 | UNDERPOWERED | UNDERPOWERED |

## compound: current → compound, holdout

| Apply | Judge | Cases | Families | Δ fidelity | Δ task | Δ rewrite quality | Fidelity gate | Task gate |
|---|---|---:|---:|---:|---:|---:|---|---|
| sonnet | opus | 3 | 1 | +0.167 | +0.250 | +0.167 | UNDERPOWERED | UNDERPOWERED |
| sonnet | sol | 3 | 1 | +0.028 | +0.139 | +0.083 | UNDERPOWERED | UNDERPOWERED |
| sol | opus | 3 | 1 | +0.111 | +0.139 | +0.139 | UNDERPOWERED | UNDERPOWERED |
| sol | sol | 3 | 1 | +0.111 | +0.167 | +0.194 | UNDERPOWERED | UNDERPOWERED |

## compound: no-skill → current, all

| Apply | Judge | Cases | Families | Δ fidelity | Δ task | Δ rewrite quality | Fidelity gate | Task gate |
|---|---|---:|---:|---:|---:|---:|---|---|
| sonnet | opus | 7 | 1 | +0.071 | +0.119 | +0.167 | UNDERPOWERED | UNDERPOWERED |
| sonnet | sol | 7 | 1 | +0.214 | +0.167 | +0.107 | UNDERPOWERED | UNDERPOWERED |
| sol | opus | 7 | 1 | +0.060 | +0.071 | +0.083 | UNDERPOWERED | UNDERPOWERED |
| sol | sol | 7 | 1 | -0.095 | -0.083 | -0.179 | UNDERPOWERED | UNDERPOWERED |

## compound: no-skill → current, holdout

| Apply | Judge | Cases | Families | Δ fidelity | Δ task | Δ rewrite quality | Fidelity gate | Task gate |
|---|---|---:|---:|---:|---:|---:|---|---|
| sonnet | opus | 3 | 1 | -0.028 | +0.111 | +0.167 | UNDERPOWERED | UNDERPOWERED |
| sonnet | sol | 3 | 1 | +0.167 | +0.139 | +0.111 | UNDERPOWERED | UNDERPOWERED |
| sol | opus | 3 | 1 | +0.000 | +0.139 | +0.139 | UNDERPOWERED | UNDERPOWERED |
| sol | sol | 3 | 1 | -0.167 | -0.028 | -0.167 | UNDERPOWERED | UNDERPOWERED |

## highlighter: no-skill → current, all

| Apply | Judge | Cases | Families | Δ fidelity | Δ task | Δ rewrite quality | Fidelity gate | Task gate |
|---|---|---:|---:|---:|---:|---:|---|---|
| sonnet | opus | 11 | 1 | +0.114 | +0.098 | +0.114 | UNDERPOWERED | UNDERPOWERED |
| sonnet | sol | 11 | 1 | +0.129 | +0.083 | +0.045 | UNDERPOWERED | UNDERPOWERED |
| sol | opus | 11 | 1 | +0.061 | +0.144 | +0.167 | UNDERPOWERED | UNDERPOWERED |
| sol | sol | 11 | 1 | +0.000 | +0.159 | +0.189 | UNDERPOWERED | UNDERPOWERED |

## highlighter: no-skill → current, holdout

| Apply | Judge | Cases | Families | Δ fidelity | Δ task | Δ rewrite quality | Fidelity gate | Task gate |
|---|---|---:|---:|---:|---:|---:|---|---|
| sonnet | opus | 1 | 1 | +0.000 | -0.167 | -0.083 | UNDERPOWERED | UNDERPOWERED |
| sonnet | sol | 1 | 1 | +0.000 | -0.167 | +0.000 | UNDERPOWERED | UNDERPOWERED |
| sol | opus | 1 | 1 | +0.250 | +0.167 | +0.083 | UNDERPOWERED | UNDERPOWERED |
| sol | sol | 1 | 1 | +0.167 | +0.083 | +0.083 | UNDERPOWERED | UNDERPOWERED |

## standing: current → compound, all

| Apply | Judge | Cases | Families | Δ fidelity | Δ task | Δ rewrite quality | Fidelity gate | Task gate |
|---|---|---:|---:|---:|---:|---:|---|---|
| sonnet | opus | 69 | 18 | +0.030 | +0.008 | +0.025 | REJECT | REJECT |
| sonnet | sol | 69 | 18 | -0.008 | +0.034 | +0.058 | REJECT | REJECT |
| sol | opus | 69 | 18 | +0.013 | +0.011 | +0.001 | REJECT | REJECT |
| sol | sol | 69 | 18 | -0.015 | +0.008 | +0.007 | REJECT | REJECT |

## standing: current → compound, holdout

| Apply | Judge | Cases | Families | Δ fidelity | Δ task | Δ rewrite quality | Fidelity gate | Task gate |
|---|---|---:|---:|---:|---:|---:|---|---|
| sonnet | opus | 15 | 9 | +0.014 | +0.021 | +0.042 | REJECT | REJECT |
| sonnet | sol | 15 | 9 | -0.049 | +0.056 | +0.111 | REJECT | REJECT |
| sol | opus | 15 | 9 | -0.028 | -0.014 | +0.007 | REJECT | REJECT |
| sol | sol | 15 | 9 | -0.014 | +0.014 | +0.014 | REJECT | REJECT |

## standing: current → teaser, all

| Apply | Judge | Cases | Families | Δ fidelity | Δ task | Δ rewrite quality | Fidelity gate | Task gate |
|---|---|---:|---:|---:|---:|---:|---|---|
| sonnet | opus | 69 | 18 | +0.038 | -0.003 | -0.004 | REJECT | REJECT |
| sonnet | sol | 69 | 18 | +0.023 | +0.006 | +0.036 | REJECT | REJECT |
| sol | opus | 69 | 18 | +0.007 | +0.011 | +0.019 | REJECT | REJECT |
| sol | sol | 69 | 18 | -0.028 | -0.007 | -0.014 | REJECT | REJECT |

## standing: current → teaser, holdout

| Apply | Judge | Cases | Families | Δ fidelity | Δ task | Δ rewrite quality | Fidelity gate | Task gate |
|---|---|---:|---:|---:|---:|---:|---|---|
| sonnet | opus | 15 | 9 | -0.028 | +0.028 | -0.007 | REJECT | REJECT |
| sonnet | sol | 15 | 9 | -0.069 | +0.028 | +0.042 | REJECT | REJECT |
| sol | opus | 15 | 9 | -0.042 | -0.028 | +0.035 | REJECT | REJECT |
| sol | sol | 15 | 9 | -0.069 | -0.014 | -0.014 | REJECT | REJECT |

## standing: no-skill → current, all

| Apply | Judge | Cases | Families | Δ fidelity | Δ task | Δ rewrite quality | Fidelity gate | Task gate |
|---|---|---:|---:|---:|---:|---:|---|---|
| sonnet | opus | 69 | 18 | +0.103 | +0.114 | +0.103 | ACCEPT | ACCEPT |
| sonnet | sol | 69 | 18 | +0.078 | +0.057 | +0.047 | REJECT | REJECT |
| sol | opus | 69 | 18 | +0.047 | +0.140 | +0.135 | REJECT | ACCEPT |
| sol | sol | 69 | 18 | +0.000 | +0.100 | +0.107 | REJECT | ACCEPT |

## standing: no-skill → current, holdout

| Apply | Judge | Cases | Families | Δ fidelity | Δ task | Δ rewrite quality | Fidelity gate | Task gate |
|---|---|---:|---:|---:|---:|---:|---|---|
| sonnet | opus | 15 | 9 | +0.208 | +0.111 | +0.104 | ACCEPT | REJECT |
| sonnet | sol | 15 | 9 | +0.257 | +0.153 | +0.111 | REJECT | REJECT |
| sol | opus | 15 | 9 | +0.076 | +0.215 | +0.208 | REJECT | ACCEPT |
| sol | sol | 15 | 9 | -0.056 | +0.104 | +0.132 | REJECT | REJECT |

## teaser: current → teaser, all

| Apply | Judge | Cases | Families | Δ fidelity | Δ task | Δ rewrite quality | Fidelity gate | Task gate |
|---|---|---:|---:|---:|---:|---:|---|---|
| sonnet | opus | 12 | 1 | +0.042 | +0.021 | +0.042 | UNDERPOWERED | UNDERPOWERED |
| sonnet | sol | 12 | 1 | +0.000 | -0.056 | +0.035 | UNDERPOWERED | UNDERPOWERED |
| sol | opus | 12 | 1 | +0.007 | +0.035 | +0.035 | UNDERPOWERED | UNDERPOWERED |
| sol | sol | 12 | 1 | -0.014 | +0.035 | +0.007 | UNDERPOWERED | UNDERPOWERED |

## teaser: current → teaser, holdout

| Apply | Judge | Cases | Families | Δ fidelity | Δ task | Δ rewrite quality | Fidelity gate | Task gate |
|---|---|---:|---:|---:|---:|---:|---|---|
| sonnet | opus | 4 | 1 | +0.125 | +0.104 | +0.083 | UNDERPOWERED | UNDERPOWERED |
| sonnet | sol | 4 | 1 | +0.104 | +0.000 | +0.063 | UNDERPOWERED | UNDERPOWERED |
| sol | opus | 4 | 1 | +0.000 | +0.083 | +0.021 | UNDERPOWERED | UNDERPOWERED |
| sol | sol | 4 | 1 | -0.042 | +0.021 | +0.000 | UNDERPOWERED | UNDERPOWERED |

## teaser: no-skill → current, all

| Apply | Judge | Cases | Families | Δ fidelity | Δ task | Δ rewrite quality | Fidelity gate | Task gate |
|---|---|---:|---:|---:|---:|---:|---|---|
| sonnet | opus | 12 | 1 | +0.167 | +0.181 | +0.194 | UNDERPOWERED | UNDERPOWERED |
| sonnet | sol | 12 | 1 | +0.243 | +0.181 | +0.271 | UNDERPOWERED | UNDERPOWERED |
| sol | opus | 12 | 1 | +0.069 | +0.104 | +0.174 | UNDERPOWERED | UNDERPOWERED |
| sol | sol | 12 | 1 | +0.076 | +0.125 | +0.132 | UNDERPOWERED | UNDERPOWERED |

## teaser: no-skill → current, holdout

| Apply | Judge | Cases | Families | Δ fidelity | Δ task | Δ rewrite quality | Fidelity gate | Task gate |
|---|---|---:|---:|---:|---:|---:|---|---|
| sonnet | opus | 4 | 1 | +0.229 | +0.271 | +0.312 | UNDERPOWERED | UNDERPOWERED |
| sonnet | sol | 4 | 1 | +0.292 | +0.229 | +0.375 | UNDERPOWERED | UNDERPOWERED |
| sol | opus | 4 | 1 | +0.125 | +0.229 | +0.312 | UNDERPOWERED | UNDERPOWERED |
| sol | sol | 4 | 1 | +0.125 | +0.229 | +0.250 | UNDERPOWERED | UNDERPOWERED |

## twitter: no-skill → current, all

| Apply | Judge | Cases | Families | Δ fidelity | Δ task | Δ rewrite quality | Fidelity gate | Task gate |
|---|---|---:|---:|---:|---:|---:|---|---|
| sonnet | opus | 8 | 1 | +0.198 | +0.156 | +0.146 | UNDERPOWERED | UNDERPOWERED |
| sonnet | sol | 8 | 1 | +0.062 | +0.115 | +0.135 | UNDERPOWERED | UNDERPOWERED |
| sol | opus | 8 | 1 | +0.115 | +0.208 | +0.115 | UNDERPOWERED | UNDERPOWERED |
| sol | sol | 8 | 1 | +0.083 | +0.125 | +0.062 | UNDERPOWERED | UNDERPOWERED |

## twitter: no-skill → current, holdout

| Apply | Judge | Cases | Families | Δ fidelity | Δ task | Δ rewrite quality | Fidelity gate | Task gate |
|---|---|---:|---:|---:|---:|---:|---|---|
| sonnet | opus | 3 | 1 | +0.194 | +0.194 | +0.167 | UNDERPOWERED | UNDERPOWERED |
| sonnet | sol | 3 | 1 | +0.250 | +0.250 | +0.333 | UNDERPOWERED | UNDERPOWERED |
| sol | opus | 3 | 1 | +0.194 | +0.222 | +0.278 | UNDERPOWERED | UNDERPOWERED |
| sol | sol | 3 | 1 | +0.111 | +0.194 | +0.194 | UNDERPOWERED | UNDERPOWERED |

