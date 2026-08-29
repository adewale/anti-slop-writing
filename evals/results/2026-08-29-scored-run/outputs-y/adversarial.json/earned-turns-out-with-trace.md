Verdict: keep

Slop tells: Sentence-initial "it turns out" sits on the stage-management watchlist — the phrase usually stages a reveal the content doesn't need. Testing it: does the sentence announce the reversal and then withhold the evidence, or does the evidence land in the same breath? Here the colon after "the cause" delivers proof immediately: a specific profiling number (61% of samples in malloc) and a specific intervention with a specific outcome (pinning the arena removed the spikes). The phrase is reporting a correction to a diagnosis, not building suspense before one.

Specificity missing: None. The note names the wrong hypothesis (GC), the corrected one (allocator), the measurement that discriminated between them (flame graph, 61% in malloc), and the fix that confirmed it (pinning the arena, spikes gone) — a full root-cause chain in one sentence.

Inflated claim: None. "The allocator was the cause" is a causal claim, but it's backed by both a diagnostic number and a confirming intervention — about the strongest evidence an incident note can carry without a full postmortem writeup.

Flow break: None. "We blamed the GC" sets up the wrong hypothesis; the very next sentence corrects it and supplies the evidence in the same breath, so there's no gap between claim and support.

Concrete rewrite: None. Ship as written.

Rewrite check: N/A, no rewrite produced. Original passes self-detectors: the reveal is paid off rather than left hanging, the numbers read as reported measurements rather than invented filler, no banned phrases.

Remembered line: "the flame graph put 61% of samples in malloc" — the number is what makes the correction verifiable, and it's already the line worth remembering.
