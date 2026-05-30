A 100% pass rate is a measurement problem, not a finish line. The suite has stopped discriminating: it can no longer tell a good skill version from a slightly better or slightly worse one, because every version clears the same bar. That is a ceiling effect, and the correct read is "the cases are too easy or too few," not "the skill is done."

What an all-pass score actually tells you is the lower bound of difficulty you happen to have encoded. It says nothing about the inputs you never wrote a case for. So the next move is to make the suite hurt again.

Concrete steps:

1. Mine real failures, not imagined ones. Pull actual skill outputs from logs or recent runs and find the ones a careful human would reject. Each rejected output becomes a case. Cases grounded in observed misbehavior are the only ones guaranteed to be on-distribution.

2. Add adversarial cases that target the skill's own rules. The skill bans phrases and rewards "concrete mechanism" language. So write inputs that game it: prose that contains the target vocabulary ("checkpoint," "retry," "because") while still saying nothing, and prose that violates a banned phrase but is genuinely the clearest wording. If the suite passes the empty-but-compliant text or rejects the justified violation, you have found the gap.

3. Split tune and holdout, and keep the holdout unseen during iteration. If you tune the skill against the same eight cases you grade it on, 100% measures memorization of those eight cases. Hold a set back so the pass rate reflects generalization.

Measurements the current pass count is hiding:

- Observed trigger rate and false-positive trigger rate. Pass/fail on rewrite quality says nothing about whether the skill fires when it should and stays quiet when it should not. Track invocations on real tasks, including the typo-fix and one-line-edit cases where it should not fire.
- Rewrite quality beyond binary assertions. A case can pass its assertions and still produce worse prose. Add a graded comparison (rewrite vs. original, rewrite vs. human edit), not just a checkbox.
- Judge drift. If a model judges these, re-grade a fixed set of frozen outputs periodically and confirm the scores have not moved. A rising pass rate can mean the judge got more lenient, not that the skill improved.

The reusable rule: when a suite saturates, it has stopped being an instrument and started being a trophy. Treat the ceiling as a signal to add harder, failure-derived, and held-out cases until the score can move again, and add the off-axis measurements (trigger rates, rewrite quality, judge stability) that a pass count was never measuring in the first place.
