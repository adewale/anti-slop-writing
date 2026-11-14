# Authorized review follow-through

## Scope and current state

- PRs #25, #26 and #22 were merged after their relevant checks; #21 was closed as
  superseded by #23. Candidate reports remain in PR #27, with no installed doctrine
  promotion from the underpowered screen.
- The eight Twitter cases from #17 are coverage-only inputs to the frozen candidate
  study, not evidence of a detector change. Its original historical holdouts are public,
  design-visible regression evidence, not sealed new validation.
- The highlighter contribution is a repo-only span/count CLI, with contextual limits,
  positive/negative/near-miss tests and explicit rewrite scope. Its historical automatic
  zero-hit grading was not imported. See `docs/slop-lint.md`.
- `../2026-11-14-fidelity-calibration/` contains an 18-item blind review packet and blank
  answers. **Human calibration is pending**, not delegated to another model. Real
  discourse-layer failures must still come from a human source.

## Branch audit before deletion

`branch-audit-before.json` records full heads, current main, graph/patch equivalence,
changed paths and each branch's added-file retention. It is model-free, reproducible with:

```bash
python3 scripts/review_followthrough.py branches --dest /tmp/branch-audit
```

Run it before deleting refs; afterwards use the recorded heads or archive tags. No script
automatically classifies an unmatched patch as safe or deletes a branch.

Evidence reviewed:
- Ruff, CI-cost and action-pin branches have patch-equivalent changes on main; the Ruff
  workflow has since been updated, so its original file is not byte-identical.
- Test-audit, verification-audit, dependency, maintenance and eval-integrity heads are
  ancestors of main.
- Tweet-audit has 39/40 identical added files. The remaining file,
  `docs/reference-anchor-tests.md`, was deliberately corrected on main: exposed anchors
  are tune/open-book regression, not independent holdout. Keep that correction, not the
  old categorical holdout claim.
- Stop-slop has 104/105 identical added files. The remaining saturation script differs
  only by an unused `from statistics import pstdev` import; exact normalized comparison
  is recorded. Its historical statistical proof claim remains withdrawn.
- Closed #21's push-on-main restriction is already present; current main additionally
  removes tag-triggered validation, pins updated actions and cancels superseded runs.

Before deletion, retain full source history for the three unmatched historical branches
(tweet-audit, stop-slop and closed #21) under annotated `archive/2026-11-14-*` tags.
Delete only the audited heads with **atomic expected-SHA leases**, then independently
check remote heads and archive targets. Preserve open candidate branches and local refs,
worktrees and the owner's original `stash@{0}`. Actual remote actions, when completed,
are recorded separately in `branch-actions.json`; this pre-action document is not a
claim that deletions have already happened.

## Still not supported

Neither the historical saturated suite nor a single-source candidate panel proves a
general writing improvement. The fresh screen cannot promote doctrine under its frozen
power/independence decision. Live-client observations measure the registered controlled
configurations, not stock-client routing or separately billed API access. Baseline
fidelity disagreement is unresolved until the human annotations exist.
