# Contributing

This project improves by hillclimbing from real writing failures. Do not add advice because it sounds reasonable; add doctrine only when an example proves the old skill missed something.

## Contribution bar

A useful contribution does at least one of these:

- adds a real before/after writing failure;
- names a failure mechanism the skill does not currently catch;
- tightens an existing rule so future rewrites get better;
- improves eval coverage or validation without bloating the installable skill.

Avoid contributions that only add broad writing advice, synonym lists, or taste claims without a concrete failure case.

## Rubric

Current eval dimensions:

| Dimension | What a passing answer does |
|---|---|
| Generic importance | Flags inflated importance language and replaces it with a concrete mechanism. |
| Decorative contrast | Distinguishes earned contrast from cadence that hides the relation. |
| Weak conclusion | Returns to the concrete carrier instead of ending on a generic thesis. |
| Product-tour flow | Adds a relation or level-of-detail hinge when paragraphs read like a list. |
| Safe essay voice | Replaces vague actors and marketing fog with concrete action/result, or cuts the line. |

The machine-readable assertions live in `evals/evals.json`. The companion explanations live in `evals/cases.md`.

## What to update

| Change type | Required updates |
|---|---|
| New detector or doctrine rule | Add/update `evals/evals.json` and usually `evals/cases.md` or `examples/`. |
| Trigger/activation wording | Add/update `evals/trigger-queries.json`. |
| Reference-only clarification | Update the relevant file in `skills/anti-slop-writing/references/`. |
| Install/runtime compatibility | Update `README.md` and, if needed, `skills/anti-slop-writing/SKILL.md` frontmatter. |
| Validation behavior | Update `scripts/validate.py` and document the check if contributors need to know it. |

Keep `skills/anti-slop-writing/SKILL.md` useful as a standalone skill file. Repo-only material belongs in `evals/`, `examples/`, `scripts/`, or docs at the repository root.

## Development loop

1. Capture a concrete failure.
2. Name the failure mechanism.
3. Add the smallest rule that catches it.
4. Add or update a before/after example or eval assertion.
5. Run validation:

```bash
python3 scripts/validate.py
```

If you changed prose rules, manually test the skill against at least one affected case in `evals/cases.md`.

## PR checklist

- [ ] The change is tied to a concrete failure, example, or eval gap.
- [ ] New doctrine has a matching eval case or before/after example.
- [ ] The installable skill remains limited to `skills/anti-slop-writing/`.
- [ ] `python3 scripts/validate.py` passes.
- [ ] Any changed docs say what to do, not just what to value.
