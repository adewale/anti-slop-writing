The reviewer is describing LLM-as-judge self-preference: when the grader and the candidate come from the same model family, the grader systematically rates outputs that share its own cadence, vocabulary, and structural habits higher than equally-correct outputs that do not. The judge-protocol doc already names this as a known limitation of the current setup; the reviewer's observation is the predicted failure mode showing up in the data. Treat it as a bias mechanism, not a quirk of these particular cases.

What the suite should do:

1. Add at least one judge from a different model family and rerun the affected cases. The pass/fail signal that counts for promotion is the cross-family judgment, or the intersection of judgments across families. Same-family agreement does not rule out same-family bias; it is consistent with it. If a different-family judge is not reachable, substitute a human spot-check on a sampled subset of the disputed cases (Claude-drafted and human-drafted candidates that the binary assertions cannot separate) and have the human pick blind, with the source of each candidate stripped.

2. Until that cross-family or human signal exists, do not promote doctrine changes whose evidence rests on the single-judge ranking between two candidates that already meet the binary assertions. The binary assertions are the calibrated part of the grader; the preference ordering between two passing candidates is exactly the part most exposed to self-preference. Read the rest of the score as coverage, not as a calibrated comparison.

3. Record the bias as a standing risk in the run note for every suite still graded by a single Claude judge, so downstream readers know which numbers are coverage signals rather than calibrated comparisons. The judge-protocol doc already prescribes this; enforce it on every run, not only when someone notices.

4. Track the disagreement rate between same-family and cross-family judges over time as its own metric. A drift up is a sign the apply and judge models are converging on a shared style that the suite is no longer able to discriminate from quality.

What the suite should not do:

Treat "rewrite the judge prompt to be stricter about self-preference" as a sufficient fix. The judge prompt cannot reliably correct for a bias the model itself carries; asking the same model to grade its own family without preference is the bias mechanism, not the cure. A prompt change can help around the edges, but it does not substitute for an independent grader. Likewise, do not treat blinding the judge to which candidate is which as sufficient — the bias operates on the style of the text, which the blinding does not remove.

The shortest defensible path is: cross-family judge or human review, applied to the disputed subset, before any doctrine change that depends on the single-judge preference is merged.
