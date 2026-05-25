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
skills/anti-slop-writing/SKILL.md     The installable skill instructions
skills/anti-slop-writing/references/  Installable supporting doctrine and examples
evals/evals.json                      Repo-only output evals and assertions
evals/trigger-queries.json            Repo-only trigger accuracy eval queries
evals/cases.md                        Human-readable regression cases for hillclimbing
examples/                             Repo-only before/after examples
scripts/validate.py                   Repo-only project and skill validation
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
2. Add or update the runnable case in `evals/evals.json`; this JSON is the source of truth for output evals.
3. If the change affects activation, add or update `evals/trigger-queries.json`.
4. Update `skills/anti-slop-writing/SKILL.md` or a reference file.
5. Run:

```bash
python3 scripts/validate.py
```

The validator also runs `skills-ref validate skills/anti-slop-writing` when `skills-ref` is installed.

6. Test the skill on the eval case manually with an agent.
7. Record the improvement in the README or eval case if the new rule catches something the old rule missed.

The point is to avoid a skill that only accumulates advice. Each new rule should come from a real failure or a better rewrite.

## Eval workflow

Use a clean workspace per iteration, for example:

```txt
eval-workspace/iteration-1/
├── eval-generic-importance/
│   ├── with_skill/
│   │   ├── outputs/
│   │   ├── grading.json
│   │   └── timing.json
│   └── old_skill/
│       ├── outputs/
│       ├── grading.json
│       └── timing.json
└── benchmark.json
```

For each case in `evals/evals.json`:

1. Run the prompt with the current skill and save the result under `with_skill/outputs/`.
2. Run the same prompt with the previous committed skill, a copied snapshot, or no skill and save the result under `old_skill/outputs/`.
3. Grade each assertion as pass/fail with quoted evidence in `grading.json`.
4. Record tokens/duration in `timing.json` when the harness exposes them.
5. Summarize pass-rate, qualitative feedback, token cost, and time cost in `benchmark.json`.

Trigger evals are separate: run the prompts in `evals/trigger-queries.json` multiple times and compare observed skill-load rate against `should_trigger`. Use near-miss negatives as well as obvious positives.

## Current doctrine

- More detail, earned importance.
- Code fences are for payloads, not emphasis.
- Punch is seasoning. Mechanism is the meal.
- Flow improves when each paragraph makes the next question possible.
- A conclusion should return to the concrete carrier, name what changed, and state what transfers.

## License

MIT. See `LICENSE`.
