Verdict: keep
Slop tells: "robust" is on the watch list (robust outside engineering context). Here it is inside engineering context and immediately earned, so the hit is a hypothesis the sentence answers, not a verdict.
Specificity missing: None. The sentence supplies the exact mechanism: every job is leased with a deadline, and the job returns to the queue when the lease expires. That is what makes the queue tolerate worker crashes.
Inflated claim: None. "robust against worker crashes" is bounded to a named failure mode (worker crashes) and backed by lease expiry and requeue, not asserted in general.
Flow break: None. The "because" clause delivers the mechanism in the same sentence as the claim.
Concrete rewrite: Not needed. Replacing "robust" with a vaguer prestige word, or expanding the lease mechanism into generic prose, would lose the earned compression. Keep as written.
Rewrite check: No rewrite applied. Nothing introduced; the kept sentence already names actor (job), mechanism (lease with deadline, requeue on expiry), and failure mode (worker crash). Passes self-detectors.
Remembered line: Every job is leased with a deadline and returns to the queue when the lease expires.
