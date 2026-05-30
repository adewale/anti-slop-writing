This is LLM-as-judge self-preference. When the same model family drafts the candidate and grades it, the judge systematically favors text that matches its own family's style, phrasing, and structure, independent of quality. The tell here is precise: the suite prefers the Claude-drafted candidate even when both candidates already satisfy the binary assertions. The assertions are doing their job; the residual preference is the bias, not a quality signal. A single-family judge cannot tell "this is better" apart from "this looks like what I would have written."

The risk is sharpest for this skill specifically, because its whole job is style. A style judge that shares a family with the drafter will reward in-family stylistic habits and penalize equally good out-of-family prose, which means the suite would quietly select for "sounds like Claude" over "is well written." That biases every future doctrine change in the same direction and makes human-written candidates look worse than they are.

What the suite should do:

1. Break the family monoculture in grading. Add at least one judge from a different model family and require agreement, or escalate disagreements. Cross-family grading is the direct control for self-preference: a bias that survives across families is more likely to be real quality; a preference that only the same-family judge holds is the artifact.

2. Add human spot-checks on the contested cases, especially Claude-draft vs. human-draft pairs where both pass the assertions. Humans are the ground truth for "is this actually better prose," and these are exactly the cases the binary assertions cannot separate.

3. Run a blind A/B with source labels stripped and order randomized, and measure the preference rate. If the judge still prefers the Claude candidate above chance when it cannot see who wrote it and both meet the bar, you have quantified the self-preference and can track whether mitigations reduce it.

4. Flag single-family grading as a known, documented bias risk in the runbook, and do not promote a change on single-family grading alone when the change is about style.

What does not fix it: rewording the judge prompt. "Be objective" or "ignore authorship" instructions do not remove same-family preference; the bias lives in the model's learned notion of good text, not in a missing instruction. Prompt tweaks may help at the margin, but on their own they are not sufficient, and treating them as the fix would leave the artifact in place while claiming it was solved.

The reusable structure: when the drafter and the judge come from the same model family, the judge's preference is confounded with self-recognition. Resolve it with a cross-family judge ensemble and human review on the cases that the binary bar leaves tied, treat single-family grading as a flagged limitation, and never accept a judge-prompt edit as the standalone cure.
