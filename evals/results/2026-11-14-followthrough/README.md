# Authorized review follow-through

## Scope and current state

- PRs #25, #26, #22 and case-only #28 were merged after their relevant checks; #21
  was closed as superseded by #23, and #17 by #28. Candidate reports remain in PR #27,
  with no installed doctrine promotion from the completed underpowered screen. #18 was
  closed as not adopted: the minimal positive one-scaffold lead does not validate its
  broad patch or pass the standing/quality guards. Source candidate branches remain
  available for provenance, not as endorsed merge candidates.
- All eight Twitter cases from #17 were ported intact into the separately validated
  `evals/twitter-evals.json` in merged #28, with facts/source metadata and examples.
  They remain coverage-only inputs to the frozen candidate study, not a detector change.
  Their original historical holdouts are public, design-visible evidence, not sealed
  new validation.
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
worktrees and the owner's original `stash@{0}`. **All eleven audited stale remote heads were deleted**, with archive targets and
absence independently verified; actual actions are recorded in `branch-actions.json`.
The later, fully merged temporary #28 branch was also deleted with an expected-head
lease and is recorded separately there; no local branch or worktree was deleted. `pr-state-before.json` is the historical pre-action snapshot,
not a live claim that those PRs remain open.

## Final verification

All seven pinned repository gates pass, including **133 unit tests** and **39 assertion
example gradings**; logs are in `validation/`. Both study archives reproduce their
statistical/guard or activation outputs byte-for-byte without model calls. The installed
package is byte-identical to the frozen #22 base.

`supplemental-audit.json` records an additional check: the prior baseline's 2,412 selected
provider response IDs and this screen's 3,366 selected IDs have **zero overlap**. No old
trial was reused as a new response. Archive symlinks, credential filenames and obvious
credential-value markers are absent; this is a bounded scan, not a universal secret
scanner. The quarantined Claude cohort used Read/Skill/Write and reports zero native
subagents; it is not pooled into routing rates.

## Still not supported

Neither the historical saturated suite nor a single-source candidate panel proves a
general writing improvement. The fresh screen cannot promote doctrine under its frozen
power/independence decision. Live-client observations measure the registered controlled
configurations, not stock-client routing or separately billed API access. Baseline
fidelity disagreement is unresolved until the human annotations exist.
