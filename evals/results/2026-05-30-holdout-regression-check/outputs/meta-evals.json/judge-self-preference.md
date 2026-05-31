Verdict: reject the current evaluation setup as load-bearing evidence; the suite needs a structural change, not a prompt tweak.

Slop tells: none in the question itself, but the failure mode it describes is the eval equivalent of borrowed-pattern emphasis — the judge is rewarding rhythm and lexical choices it would itself produce, not the underlying quality the binary assertions are trying to capture.

Specificity missing: nothing in the framing; the reviewer has already named the gap (Claude judge, Claude drafts, preference observed even when both candidates meet the assertions). The work is to name what the suite must do, not what it must ask.

Inflated claim: the suite, as constituted, cannot distinguish "the Claude-drafted candidate is better" from "the Claude judge prefers prose that looks Claude-drafted." Any score the suite reports today is contaminated by that confound.

Flow break: the bias the reviewer flagged is not a prompt problem; it is a judge-identity problem. A prompt change can move where the bias shows up but cannot remove it, because the judge model is itself the source of the preference.

What the eval suite should do:

1. Name the mechanism. This is LLM-as-judge self-preference: same-family bias, where a judge model systematically scores higher candidates produced by its own family because the surface features it learned to value are the surface features its own family produces. It is a known failure mode of single-judge, same-family evaluation, and the suite should document it as a known bias risk rather than treat it as a tuning issue.

2. Add a cross-family judge. At minimum, route every rewrite case through one judge from a different model family (a non-Claude judge), and gate merges on agreement between the Claude judge and the cross-family judge. Disagreements go to human review. A single-judge result, of any family, is not enough for a change that is itself a candidate the judge family helped draft.

3. Add a human spot-check on a sampled holdout. Even with a cross-family ensemble, the suite needs periodic human grading on a randomly sampled subset of cases, with the human blinded to which candidate is Claude-drafted. This is the only check that catches a bias the model ensemble shares.

4. Track agreement rate as a first-class metric. Report Claude-judge / cross-family-judge agreement and Claude-judge / human agreement on the spot-check. A drop in agreement is itself a signal, independent of the underlying pass rate.

5. Do not accept "rewrite the judge prompt" as a sufficient fix. Prompt edits can re-weight what the judge attends to, but they cannot remove the judge's prior over what good prose looks like. The bias is in the judge's weights, not in the rubric the judge was given.

6. Until the cross-family judge is wired in, mark the current suite results as provisional and do not use them to gate doctrine changes that themselves rewrite the prose the judge was trained to prefer.

Concrete rewrite of the reviewer's note as a runbook entry: "Before any doctrine change is merged on the strength of the rewrite suite, the suite must report agreement between the Claude judge and at least one non-Claude judge, plus a human spot-check on a sampled holdout. Single-family grading is a known self-preference risk and is not sufficient evidence on its own."

Remembered line: a judge that shares a family with the drafter is grading the family, not the writing.
