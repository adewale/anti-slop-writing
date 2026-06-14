# Provenance: stop-slop examples as eval data

Source: `references/examples.md` from [hardikpandya/stop-slop](https://github.com/hardikpandya/stop-slop), MIT License, Copyright (c) 2025 Hardik Pandya. Reused here under MIT with attribution.

## Why these are useful to us

stop-slop optimizes for punch and brevity; we optimize for **named mechanism and earned compression**. The two aesthetics diverge, and the divergence is exactly where these examples earn their place in our suite. Several of stop-slop's gold "after" rewrites trip our own detectors:

- Example 1 after — "Building products is hard. Technology is manageable. People aren't." — is short antithesis / staccato parataxis. Under our staccato-contrast test it is at best *compressed* (the "People aren't" pole is asserted, not evidenced) unless prior context earns it.
- Example 3 after — "Move faster. Your competition is." — is a punchy closer with **no named mechanism** and it deletes the original content. Our doctrine: "a punchy line without a named mechanism still reads as slop."
- Example 5 after — "The best teams optimize for learning, not productivity." — is X-not-Y negative parallelism, a pattern we watch.

So we do **not** import stop-slop's "after" texts as our gold. We use them two ways:

1. **Boundary / divergence cases (highest value):** review stop-slop's gold "after" and assert that our skill flags or qualifies it, documenting where the two doctrines disagree.
2. **Fresh rewrite/cut inputs in domains we under-cover** (product, management, business, leadership) using the stop-slop "before" texts, with **our own** assertions — including cases whose content is so thin that the correct move is cut or `ask-author`, not a confident rewrite.

These are staged as candidates in `candidate-cases.json`. Promote into `evals/adversarial.json` and `evals/rewrite-evals.json` (with `validate.py` split-count updates) only after a maintainer agrees the divergence is the behavior we want to lock in.
