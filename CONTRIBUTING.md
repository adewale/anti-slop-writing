# Contributing

This project improves by hillclimbing from real writing failures. Do not add advice because it sounds reasonable. Add doctrine when an example shows the current skill missing, over-flagging, or producing a weaker rewrite.

## Contribution bar

A useful contribution does at least one of these:

- adds a real before/after writing failure;
- names a failure mechanism the skill does not currently catch;
- tightens an existing rule so future rewrites get better;
- improves eval coverage or validation without bloating the installable skill.

Avoid PRs that only add broad writing advice, synonym lists, or taste claims. “Avoid vague wording” is not enough; show the vague line, name the failure, and give the rewrite the skill should produce.

## Rubric

Current eval dimensions:

| Dimension | What a passing answer does |
|---|---|
| Generic importance | Flags inflated importance language and replaces it with a concrete mechanism. |
| Decorative contrast | Distinguishes earned contrast from cadence that hides the relation. |
| Weak conclusion | Returns to the concrete carrier instead of ending on a generic thesis. |
| Product-tour flow | Adds a relation or level-of-detail hinge when paragraphs read like a list. |
| Safe essay voice | Replaces vague actors and marketing fog with concrete action/result, or cuts the line. |

The machine-readable assertions live in `evals/evals.json`. Rewrite-specific checks live in `evals/rewrite-evals.json`; false-positive checks live in `evals/adversarial.json`; eval-suite health checks live in `evals/meta-evals.json`. The companion explanations live in `evals/cases.md` and `evals/failures/`.

Every eval case carries a `split` field: `tune` (used to diagnose and iterate doctrine) or `holdout` (scored only at end-of-round and at merge). Never edit doctrine in response to a holdout failure — write a new tune case for the next round instead. See `docs/hillclimb-improvements.md` for the rationale and `runbooks/hillclimb-skill.md` for the loop.

## What to update

| Change type | Required updates |
|---|---|
| New detector or doctrine rule | Add/update `evals/evals.json`, `evals/rewrite-evals.json`, `evals/failures/`, and usually `evals/cases.md` or `examples/cards/`. New cases must carry `split: "tune"` or `split: "holdout"`. |
| False-positive or over-flagging fix | Add/update `evals/adversarial.json`. |
| Eval-suite weakness or ceiling effect | Add/update `evals/meta-evals.json` and record the lesson in `LESSONS.md`. |
| Trigger/activation wording | Add/update `evals/trigger-queries.json`. Near-miss false positives must use the `near-neg-` id prefix. |
| Rejected doctrine edit | Add an entry to `evals/rejected-edits.md` so the same failed move is not retried. |
| Reference-only clarification | Update the relevant file in `skills/anti-slop-writing/references/`. |
| Install/runtime compatibility | Update `README.md` and, if needed, `skills/anti-slop-writing/SKILL.md` frontmatter. |
| Validation behavior | Update `scripts/validate.py` and document the check if contributors need to know it. |
| Score-delta gating | Use `scripts/score_delta.py` for any close-call accept/reject. Report the CI and verdict in the PR. |

Keep `skills/anti-slop-writing/SKILL.md` useful as a standalone skill file. A user who copies only `skills/anti-slop-writing/` should get the runtime behavior. Repo-only material belongs in `evals/`, `examples/`, `scripts/`, or root docs.

## Development loop

1. Capture a concrete failure.
2. Name the failure mechanism.
3. Use `runbooks/hillclimb-skill.md` when the change affects multiple artifacts.
4. Add the smallest rule that catches it.
5. Add or update a before/after example or eval assertion.
6. Record the lesson in `LESSONS.md` and the change in `CHANGELOG.md` when doctrine or eval coverage changes.
7. Run validation:

```bash
python3 scripts/validate.py
```

If you changed prose rules, manually test the skill against at least one affected case in `evals/cases.md`. Quote the before/after in the PR so reviewers can see what improved. If all evals pass, ask whether that is success or a ceiling effect; add a harder case when the suite no longer distinguishes good from merely compliant output.

## PR checklist

- [ ] The change is tied to a concrete failure, example, or eval gap.
- [ ] New doctrine has a matching eval case or before/after example.
- [ ] New eval cases carry a `split` of `tune` or `holdout`.
- [ ] If an attempt was rejected, the entry is in `evals/rejected-edits.md`.
- [ ] `scripts/score_delta.py` ACCEPTs on the holdout split for any close-call doctrine change (CI and verdict quoted in the PR).
- [ ] The installable skill remains limited to `skills/anti-slop-writing/`.
- [ ] `python3 scripts/validate.py` passes.
- [ ] Any changed docs say what to do, not just what to value.
