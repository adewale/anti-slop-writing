# Evaluation integrity review — 2026-11-13

The evaluation instrument had reproducible validity defects. The proposed repair
withdraws the old proof claim, separates apply/judge inputs, checks independent sample
units, and stops rewarding invented facts. **Whether the current skill beats no skill
remains unmeasured.** No model trial completed: the available Codex CLI failed
authentication. No installable skill file was changed.

Base: `70f9803b4c717a98c713706101638f2406105a40`. Work branch: `sol/eval-integrity`.
Phase 0 is reproduced, Phase 1 has owner-review recommendations, Phase 2 is prepared
for review, and Phase 3 has an unrun plan. Phases 4–5 remain pending. The handoff's
merge/close/delete/existing-branch-push boxes and spend ceiling are blank; existing
PRs and remote branches were retained.

## Findings and repairs

[The reproduction](2026-11-13-review-reproduction.md) records all nine findings,
commands, disagreements with the brief, and the original scorer's behavior.
Its fixed-ref script preserves repeatability after repairs.

- Corrected historical proof: N=42, binary delta +0.0357, bootstrap 95% CI
  [+0.0079, +0.0714], p≈0.126 after removing the template-only assertion. Seven
  equal-weight family means give p≈0.245. Original outputs and judgments are retained.
- Standing baseline: 38/38 cases at 1.0. Five perfect independent improvements cannot
  clear the default two-sided sign-flip gate. Regression direction was already fixed;
  this change adds ID, numeric, sample-size, and cluster safeguards.
- `prepare` writes apply-only and judge-only files and embeds facts/source inputs.
  `--no-skill` preserves task/facts while omitting skill instructions. The caller must
  still isolate each worker's filesystem. Dynamic rubric instructions reach judges.
- `blind` removes version-specific fields, randomizes filenames, and records raw/judged
  word counts. Keys and raw counts must remain outside the judge directory; stale
  output directories are refused. Grade/join preserve case/family/length metadata.
- Every case in the main review and rewrite suites now declares facts and a non-invention assertion.
  Unsupported mechanisms, readers, results, and tradeoffs may be handled by a precise
  question or cut. All original and changed case objects, including holdout validity
  changes made before new scoring, are in
  [the audit record](2026-11-13-validity-changes.json). Historical scores are not
  directly comparable after these changes.
- Copied worked examples were replaced; the exposed tweet anchor moved into the
  open-book regression archive with its original assertions/artifacts. A separate
  synthetic support-ticket practice essay tests transfer/fidelity in holdout.
  The validator rejects normalized eight-word overlap with skill files, checks
  holdout inputs, and rejects sharing a fixture across tune and holdout.
- Word growth is checked against the recorded baseline with a +200 allowance and a
  documented consolidation-note route. No beta-binomial or automatic length-adjusted
  scoring is claimed. The two-tier runbook distinguishes regression coverage from a
  pre-registered powered improvement claim. Example-only changes need factual review
  and validation, without a powered model run.
- Deterministic checks reject substring hinges, negated keeps, bare keyword stuffing,
  and the cited marketing/reliability samples. These remain limited deterministic
  screens; semantic fidelity and causality require the qualitative judges too.

## PR decisions prepared for the owner

| Item | Observed state | Recommendation / action taken |
|---|---|---|
| [#25](https://github.com/adewale/anti-slop-writing/pull/25) | Mergeable; head `85b6ccc5e695e05e431ea1771939fcb2cae6b859` has five successful checks, including action pinning | Ready for owner merge at that checked head. Left open. |
| [#21](https://github.com/adewale/anti-slop-writing/pull/21) | Draft, superseded by merged #23; head-to-main tree comparison would remove Dependabot and action-pinning files | Close as superseded. Prepared explanation below; no comment or closure posted. |
| [#22](https://github.com/adewale/anti-slop-writing/pull/22) | Draft, mergeable; synthetic source explicitly supplies retained checks, local-lint revision, pending-head CI, and documented incident reason | Examples checked against their supplied facts; no unsupported intent needed. Ready for owner promotion/merge after the instrument lands, with current-head CI checked then. Left draft. |
| [#18](https://github.com/adewale/anti-slop-writing/pull/18) | Conflicted; pre-registered Claude-family run exists | Leave unmerged. Preserve frozen patch and recreate on a new branch after Phase 2. Needs cross-family/no-skill replication and independent-case design; forty trials on one case do not become forty independent cases. No existing branch changed. |
| [#17](https://github.com/adewale/anti-slop-writing/pull/17) | Conflicted; no SKILL.md edit | Recreate after Phase 2; retain Phase 0 write-up, then measure no-skill/current-skill cases before deciding which belong in standing coverage. No branch changed. |
| `claude/llm-cliche-highlighter-c2qqq8` | No PR | Pending Phase 4: split lint and grounded examples from doctrine word lists. No new detector shipped. |
| `claude/cataphoric-teasers-handling-sele9m` | No PR | Pending Phase 4: pre-register candidate measurement; preserve results even if null. No doctrine shipped. |

Prepared #21 closure explanation:

> Superseded by #23, which applied the push-event restriction on main. The current
> branch is based before subsequent CI maintenance; its tree compared with main
> would also remove Dependabot and action-pinning configuration. Retain #23's merged
> implementation and close this duplicate proposal. No additional trigger change is needed.

The deletion observation for #21 comes from a two-tree diff. Its three-dot PR patch
contains only two workflow trigger edits; normal merge behavior requires a separate
check. Supersession by #23 is the reason to close it.

Live metadata and #25 check URLs are retained in
`2026-11-13-review-reproduction/pr-snapshot.json`.

## Remote branch checks

No remote branch was deleted. Commands and counts are in
`2026-11-13-review-reproduction/branch-checks.json`.

| Branch | Deletion test against original main |
|---|---|
| `agent/upgrade-ruff-0.16` | Pass: `git cherry` has one minus, no plus |
| `ci/no-extra-cost-optimisations-20261102` | Pass: one minus, no plus |
| `codex/pin-github-actions-2026-11-05` | Pass: one minus, no plus |
| `claude/tweet-audit-l4yq2z` | Pass: all 40 added files are identical on main |
| `claude/test-audit-campaign` | Pass: zero commits ahead |
| `claude/verification-audit-fixes` | Pass: zero commits ahead |
| `claude/stop-slop-review-61fuj1` | **Fail**: four plus commits; only 104/105 added files match main. `scripts/saturation_index.py` differs. Retain and investigate. |

The final branch failure disagrees with the handoff's blanket merged/deletable label.
The additional remote branch `claude/affectionate-knuth-gyju7x` was also discovered;
it has one unmerged commit adding the handoff brief, was absent from the branch inventory, and is retained without a deletion recommendation.

## Model runs, cost, and efficacy

[Model inventory](2026-11-13-model-inventory.md): no exact model ID returned; no apply
or judge panel used. A tiny default Codex probe failed before generation after its
models endpoint returned 401. Anthropic and open-weights access were not configured.
Completed eval calls: **0**. No returned token usage or billing data are available.
No new scores, CIs, length differences, or judge-agreement numbers are asserted.

[The baseline plan](2026-11-13-no-skill-baseline/PLAN.md) starts with earned antithesis,
then the corrected rewrite/review suites. It is explicitly unrun and is not a
preregistration. The per-apply-model answer is unavailable because no apply model
was confirmed callable. The owner budget remains unset.

## Validation and remaining work

All seven handoff checks are run before committing, using skills-ref 0.1.1, Ruff
0.16.0, and skill-eval-harness 0.6.0. The baseline had 46 passing unit tests and
30 passing checked example gradings. The repair adds good/bad/near-miss coverage;
final validation passes all seven required checks: 76 unit tests, 36 checked example
gradings, reference/spec validation, install boundary, Ruff, strict harness/ablation
validation, and a blocker-free manifest audit. Command outputs are retained under
`2026-11-13-review-reproduction/validation/`.
No manual doctrine trial is claimed because the installable prose rules are unchanged.

Next, in order:

1. Review and land the instrument PR; owner-only housekeeping can follow the concrete
   recommendations above. Investigate the stop-slop branch mismatch before deletion.
2. Restore callable model access, fix exact apply/judge IDs, estimate baseline cost,
   simulate power using independent units, then commit the baseline preregistration.
   The blank-ceiling handoff permits Phase 3, then requires a cost report and stop;
   set a ceiling before Phase 4.
3. Run earned-antithesis and rewrite no-skill baselines; report harm or null findings
   without editing doctrine to fit them. Run saturation_index on completed results.
4. Recreate/evaluate branch candidates under that protocol. The single-case #18 design
   needs resolution before a general improvement claim can pass the repaired gate.
5. Repair the skill's examples and contradictions in separately measured rounds.

The empty merge/close/delete authorizations prevent backlog mutations; unavailable
model access prevents the baseline studies. The blank spend ceiling sets a stopping
boundary after Phase 3, rather than preventing the authorized baseline work. No merger, closure, deletion, or doctrine promotion
is represented as completed.

## Review follow-up — 2026-11-14

A review of this branch found two problems with the case repair, and both are fixed in a
follow-up commit.

- **Most cases rewarded asking.** After the repair, 36 of the 40 review and rewrite
  cases had `facts: []`. About 23 of those could be passed only by asking for facts or
  cutting, and 4 cases tested turning supplied facts into a concrete rewrite. A model
  that answered every prompt with "cut it and tell me which workflow you mean" would have
  passed most of the suite. The follow-up adds 19 `paired_with` twins: 10 in `evals.json`,
  9 in `rewrite-evals.json`, each in the same split as its partner. A twin gives the same
  task (or, for `holdout-ask-author-ai-tooling`, a prompt that no longer says no notes
  exist) plus the facts the partner withholds. It requires those facts in the rewrite and
  fails an ask-author answer or a cut. The 5 new holdout twins were written by a reviewer
  who has not tuned doctrine. `validate.py` checks pair integrity.
- **The apply prompt gave every arm the answer.** With empty facts, `prepare` added "Ask
  for missing facts or cut unsupported claims." to every apply prompt, including
  `--no-skill`. The no-skill arm therefore received the skill's key behavior as an
  instruction. The empty-facts block now reads only "No additional facts beyond the source
  text."

The follow-up also stops the runbook relying on the one-off handoff for spending
authority, and the bare-`so` hinge check no longer passes "so-called" or intensifier "so".


## Pair review — 2026-11-14

The [fact-pair audit](2026-11-14-fact-pair-review/README.md) reviews all nineteen twins,
preserves their facts/prompts, corrects remaining graded-rubric inconsistencies, and
keeps pairs together through scoring. It records grading clarifications made before
new scoring, including the five holdout twins. No doctrine or model result changed.
