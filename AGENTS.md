# Agent instructions

This repo packages `anti-slop-writing` as an installable Agent Skill plus repo-only eval machinery. Keep that boundary visible: users copy `skills/anti-slop-writing/`; contributors work in `evals/`, `examples/`, `scripts/`, and root docs.

## Rules

- Do not add broad writing advice without a concrete failure case or before/after example.
- Prefer small, testable doctrine changes over large rewrites.
- Keep `skills/anti-slop-writing/SKILL.md` usable as a standalone skill file.
- Resolve reference paths relative to `skills/anti-slop-writing/`.
- When adding a new detector, add an eval case or example that proves why it belongs.
- Avoid decorative code fences. Code fences are for commands, payloads, examples, and fixtures.

## Validation

Run before committing:

```bash
python3 scripts/validate.py
```

If you change prose rules, also manually test the skill against at least one case in `evals/cases.md`.

## Hillclimbing pattern

Use `runbooks/hillclimb-skill.md` when a change touches doctrine, evals, rubric, lessons, changelog, or multiple repo artifacts.

1. Capture a real writing failure.
2. Name the failure mechanism.
3. Add the smallest rule that catches it.
4. Add a before/after example.
5. Add adversarial or meta-eval coverage when the rule could overgeneralize or the suite looks too easy.
6. Re-run validation.

Do not optimize for sounding wise. Optimize for the next agent producing a better concrete rewrite.
