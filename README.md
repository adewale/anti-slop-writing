# Anti-Slop Writing

Anti-Slop Writing is an Agent Skill that helps coding agents review, draft, and rewrite prose so it does not read like generic LLM output.

Core rule:

> Sharp detail beats inflated significance.

Use it for READMEs, articles, slide copy, wiki pages, emails, launch posts, scripts, product copy, and DevRel writing where generic cadence, prestige abstractions, or marketing fog would weaken the work.

## Why use it

The skill gives an agent concrete editing tests instead of broad writing advice. It helps the agent:

- replace vague importance language with specific mechanisms;
- detect canned AI-writing rhythms such as decorative contrast and “not just X but Y”;
- improve paragraph flow by naming cause, contrast, dependency, inference, or level change;
- turn generic conclusions into endings that return to the concrete carrier;
- preserve useful compression while removing cadence that pretends to be judgment.

## Quick start

### What to install

Install only the skill directory:

```txt
skills/anti-slop-writing/
├── SKILL.md
└── references/
```

For clients that support the shared `.agents/skills` convention:

```bash
mkdir -p ~/.agents/skills
cp -R skills/anti-slop-writing ~/.agents/skills/
```

Then ask your agent to use `anti-slop-writing` when reviewing or rewriting prose.

Example prompt:

```txt
Use the anti-slop-writing skill to review this README intro. Flag slop tells and give a concrete rewrite.
```

## Compatible agents and clients

The skill is instruction-only: no scripts, package installs, network calls, or runtime dependencies. It follows the Agent Skills directory shape: a folder named `anti-slop-writing` containing `SKILL.md` with valid frontmatter.

| Client | Status | Install location |
|---|---|---|
| Pi | Compatible | `.pi/skills/anti-slop-writing/` or `~/.pi/agent/skills/anti-slop-writing/` |
| Claude Code | Compatible | `.claude/skills/anti-slop-writing/` or `~/.claude/skills/anti-slop-writing/` |
| Codex | Compatible | `.agents/skills/anti-slop-writing/` or `~/.agents/skills/anti-slop-writing/` |
| OpenCode | Compatible | `.opencode/skills/anti-slop-writing/`, `.agents/skills/anti-slop-writing/`, or global equivalents |
| claude.ai | Compatible as a custom Skill | Upload a zip of `skills/anti-slop-writing/` through custom Skills settings |
| Claude API | Compatible if uploaded as a custom Skill | Upload through the Skills API and use with code execution |

Notes:

- Codex plugin packaging is not included; direct skill-folder installation works for local/project use.
- OpenCode also discovers Claude-compatible and `.agents/skills` locations.
- The `name` matches the directory, uses lowercase hyphenated form, and stays under 64 characters.
- The `description` is under 1024 characters and front-loads the trigger words Codex/OpenCode/Claude use for skill selection.

## What gets installed vs what is for development

```txt
skills/anti-slop-writing/SKILL.md     Installable skill instructions
skills/anti-slop-writing/references/  Installable supporting doctrine and examples
evals/evals.json                      Repo-only output evals and assertions
evals/trigger-queries.json            Repo-only trigger accuracy eval queries
evals/cases.md                        Human-readable regression cases
evals/results/latest.md               Latest recorded smoke eval results
examples/                             Repo-only before/after examples
scripts/validate.py                   Repo-only validation
.github/workflows/validate.yml        GitHub Actions validation
```

Do not copy `evals/`, `examples/`, `scripts/`, or `.github/` into a user’s skill directory unless you are developing the skill itself.

## Current eval status

Latest recorded smoke results are in `evals/results/latest.md`.

| Eval set | Result |
|---|---:|
| Manual regression cases (`evals/cases.md`) | 5/5 pass |
| Machine-readable assertions (`evals/evals.json`) | 15/15 pass |
| Trigger-query sanity check (`evals/trigger-queries.json`) | 20/20 pass |

These are smoke evals, not a full benchmark with persisted `with_skill/` versus `old_skill/` run artifacts.

## Development workflow

When improving the skill:

1. Capture a concrete writing failure in `examples/` or `evals/cases.md`.
2. Add or update the runnable case in `evals/evals.json`.
3. If the change affects activation, update `evals/trigger-queries.json`.
4. Make the smallest doctrine change in `skills/anti-slop-writing/SKILL.md` or `skills/anti-slop-writing/references/`.
5. Run validation:

```bash
python3 scripts/validate.py
```

The validator also runs `skills-ref validate skills/anti-slop-writing` when `skills-ref` is installed.

If prose rules changed, manually test the skill against at least one case in `evals/cases.md`.

## Full eval workflow

Use a clean workspace per iteration:

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
5. Summarize pass rate, qualitative feedback, token cost, and time cost in `benchmark.json`.

Trigger evals are separate: run the prompts in `evals/trigger-queries.json` multiple times and compare observed skill-load rate against `should_trigger`.

## Doctrine snapshot

- More detail, earned importance.
- Code fences are for payloads, commands, examples, and fixtures.
- Punch is seasoning. Mechanism is the meal.
- Flow improves when each paragraph makes the next question possible.
- A conclusion should return to the concrete carrier, name what changed, and state what transfers.

## License

MIT. See `LICENSE`.
