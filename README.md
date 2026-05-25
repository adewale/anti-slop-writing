# Anti-Slop Writing

Anti-Slop Writing is an agent skill for editing prose so it does not read like generic LLM output.

It is built around one rule:

> Sharp detail beats inflated significance.

The skill is for articles, READMEs, slide copy, wiki pages, emails, posts, scripts, and any important writing where generic cadence, prestige abstractions, and fake structure would weaken the work.

## What it does

The skill helps an agent:

- find vague importance language;
- replace rhythm with relation;
- prefer hypotaxis when the relation matters;
- make paragraphs flow by cause, contrast, dependency, inference, or level change;
- turn generic endings into conclusions that return to the concrete carrier;
- preserve useful compressed lines while removing cadence that pretends to be judgment.

## Repository layout

```txt
skills/anti-slop-writing/SKILL.md     The installable skill
skills/anti-slop-writing/references/  Supporting doctrine and examples
evals/cases.md                        Manual regression cases for hillclimbing
examples/                             Before/after examples
scripts/validate.py                   Lightweight project validation
```

## Install / use

Copy `skills/anti-slop-writing/` into the skill directory for your agent harness, for example:

```bash
cp -R skills/anti-slop-writing /path/to/project/.pi/skills/
```

Then ask the agent to use the `anti-slop-writing` skill when drafting, reviewing, or rewriting important prose.

## Hillclimbing workflow

When improving the skill:

1. Add or update one concrete example in `examples/` or `evals/cases.md`.
2. Update `skills/anti-slop-writing/SKILL.md` or a reference file.
3. Run:

```bash
python3 scripts/validate.py
```

4. Test the skill on the eval case manually with an agent.
5. Record the improvement in the README or eval case if the new rule catches something the old rule missed.

The point is to avoid a skill that only accumulates advice. Each new rule should come from a real failure or a better rewrite.

## Current doctrine

- More detail, earned importance.
- Code fences are for payloads, not emphasis.
- Punch is seasoning. Mechanism is the meal.
- Flow improves when each paragraph makes the next question possible.
- A conclusion should return to the concrete carrier, name what changed, and state what transfers.

## License

MIT. See `LICENSE`.
