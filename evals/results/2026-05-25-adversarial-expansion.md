# Results — adversarial eval expansion

Date: 2026-05-25

This run added seven adversarial cases to `evals/adversarial.json` to reduce false positives and overgeneralization.

## Added cases

- `exact-not-just-distinction` — allows `not just X but Y` when it marks a real severity distinction backed by mechanism.
- `controlled-variable-staccato` — allows `Same X. Same Y. Different Z.` when it records an established controlled-variable comparison.
- `concrete-comparison-table` — allows table formatting when rows compare concrete failure modes and behavior changes.
- `legitimate-three-step-sequence` — allows a three-part sequence when the parts are ordered operations.
- `direct-warning-with-evidence` — allows `Important:` when it introduces a specific destructive consequence and action.
- `specific-source-backed-highlight` — allows `highlights` when it points to concrete trace evidence.
- `concise-imperative-runbook-step` — allows concise imperative runbook style without requiring a named actor.

## Score

| Eval set | Score |
|---|---:|
| Adversarial assertions (`evals/adversarial.json`) | 36/36 assertions |

## Assessment

The adversarial suite is stronger. It now protects against the main way a phrase-based anti-slop skill can go wrong: overcorrecting text that is concise, technical, quoted, structured, or contextually earned.
