Verdict: keep
Slop tells: "not just X; it is Y" matches the "Not just X, but Y" pattern, which is normally suspect. Here it is the exact point: the contrast reclassifies the bug from cache invalidation to data loss, and the "because" clause supplies the mechanism that justifies the reclassification.
Specificity missing: None. The mechanism is named precisely: expired sessions can overwrite the newer profile record during replay.
Inflated claim: None. The severity escalation is backed by a concrete failure mode, not asserted for emphasis.
Flow break: None. "because" subordinates the mechanism to the claim — the preferred hypotactic structure.
Concrete rewrite: Keep as written. The "not just" is earned because it marks a genuine change in failure class. Optional light tighten only: "This is a data-loss bug, not just a cache-invalidation bug: expired sessions can overwrite the newer profile record during replay." This keeps the distinction and mechanism while leading with the more severe class.
Remembered line: Expired sessions can overwrite the newer profile record during replay.
