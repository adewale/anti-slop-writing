Verdict: keep

Slop tells: "robust" is on the watch list. Flagged as a hypothesis to check.

Specificity missing: None. The sentence immediately supplies the mechanism: lease with a deadline, and automatic return to the queue when the lease expires.

Inflated claim: None. "Robust against worker crashes" is a precise engineering qualifier scoped to one failure mode, not a prestige abstraction.

Flow break: None.

Concrete rewrite: No rewrite needed. "Robust" is earned by the lease/deadline/return mechanics in the same sentence. Keep: "The retry queue is robust against worker crashes because every job is leased with a deadline and returned to the queue when the lease expires."

Rewrite check: passes self-detectors. No change made; confirming the original sentence names the mechanism, actor, and failure mode.

Remembered line: Every job is leased with a deadline and returned to the queue when the lease expires.
