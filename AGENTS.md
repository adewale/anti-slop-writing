# Agent instructions

This repo packages the `anti-slop-writing` skill as an independent, hillclimbable project.

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

1. Capture a real writing failure.
2. Name the failure mechanism.
3. Add the smallest rule that catches it.
4. Add a before/after example.
5. Re-run validation.

Do not optimize for sounding wise. Optimize for making future rewrites better.
