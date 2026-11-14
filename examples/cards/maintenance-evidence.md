# Card: Explain maintenance history without inventing intent

Synthetic audit example. The commit and local lint result are known; author intent
and current-head CI are unknown.

## Before

The rushed rollout blindly copied CI everywhere. Everything passes. Confidence: 10/10.

## After

The rollout commit introduced push and PR validation, which can both run for an
open PR branch. The change removes that extra branch run while retaining PR, main,
and tag checks. Local workflow lint passed; current-head CI is pending. The record
does not explain the original choice of triggers.

## Boundary

Dates and diffs can explain accumulation without proving intent. Preserve an
author's stated reason when a linked issue or incident record supplies it. Scope
verification to the checks and revision actually observed.
