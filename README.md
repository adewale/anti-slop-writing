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

With the Skills CLI:

```bash
npx skills add https://github.com/adewale/anti-slop-writing --skill anti-slop-writing
```

Or copy the directory to a shared Agent Skills location:

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

The skill is instruction-only. It gives the agent prose-editing rules and examples; it does not run scripts, install packages, call the network, or require a runtime. The installable unit is a folder named `anti-slop-writing` containing `SKILL.md` with valid frontmatter.

| Client | Status | Install location |
|---|---|---|
| Pi | Compatible | `.pi/skills/anti-slop-writing/` or `~/.pi/agent/skills/anti-slop-writing/` |
| Claude Code | Compatible | `.claude/skills/anti-slop-writing/` or `~/.claude/skills/anti-slop-writing/` |
| Codex | Compatible | `.agents/skills/anti-slop-writing/` or `~/.agents/skills/anti-slop-writing/` |
| OpenCode | Compatible | `.opencode/skills/anti-slop-writing/`, `.agents/skills/anti-slop-writing/`, or global equivalents |
| claude.ai | Compatible as a custom Skill | Upload a zip of `skills/anti-slop-writing/` through custom Skills settings |
| Claude API | Compatible as a custom Skill | Upload through the Skills API and use with code execution |

Notes:

- Codex plugin packaging is not included; direct skill-folder installation works for local/project use.
- OpenCode also discovers Claude-compatible and `.agents/skills` locations.
- The `name` matches the directory, uses lowercase hyphenated form, and stays under 64 characters.
- The `description` is under 1024 characters and front-loads the trigger words Codex/OpenCode/Claude use for skill selection.

## What gets installed vs what is for development

```txt
skills/anti-slop-writing/SKILL.md     Installable skill instructions
skills/anti-slop-writing/references/  Installable supporting doctrine and examples
evals/evals.json                      Repo-only output evals (tune + holdout split)
evals/adversarial.json                Repo-only over-flagging evals (tune + holdout split)
evals/rewrite-evals.json              Repo-only rewrite quality evals (with dynamic_rubric and graded_dimensions)
evals/meta-evals.json                 Repo-only eval-suite health checks (tune + holdout split)
evals/trigger-queries.json            Repo-only trigger accuracy queries with near-neg- near-miss negatives
evals/cases.md                        Human-readable regression cases
evals/failures/                       Curated failure corpus behind the doctrine
evals/rejected-edits.md               Graveyard of doctrine edits that failed an eval
evals/results/                        Recorded smoke eval results
examples/cards/                       Compact before/after cards
examples/                             Repo-only before/after examples
Lessons_learned.md                    Lessons learned and overgeneralization boundaries
CHANGELOG.md                          Doctrine, eval, compatibility, and docs changes
runbooks/hillclimb-skill.md           Runbook for bounded skill-improvement loops
docs/eval-runbook-notes.md            Source notes for runbook/eval-drift ideas
docs/hillclimb-improvements.md        Cited rationale for the 13 hillclimb infrastructure changes
scripts/validate.py                   Repo-only validation
scripts/score_delta.py                Paired-bootstrap / sign-flip gate for accept/reject
.github/workflows/validate.yml        GitHub Actions validation
```

Copy `evals/`, `examples/`, `scripts/`, and `.github/` only when you are working on this repository. They are not part of the runtime skill.

## Current eval status

Latest recorded smoke results are in `evals/results/latest.md`. Each eval suite is split into `tune` cases (used during iteration) and `holdout` cases (scored at end-of-round and at merge only).

| Eval set | Tune cases | Holdout cases |
|---|---:|---:|
| Machine-readable assertions (`evals/evals.json`) | 5 | 3 |
| Adversarial false-positive checks (`evals/adversarial.json`) | 12 | 3 |
| Rewrite quality checks (`evals/rewrite-evals.json`) | 6 | 2 |
| Eval-suite health checks (`evals/meta-evals.json`) | 5 | 2 |
| Trigger-query sanity check (`evals/trigger-queries.json`) | 16 | 10 |
| Manual regression cases (`evals/cases.md`) | 5 cases | n/a |

These results catch regressions in the current doctrine. They are not a full benchmark with persisted `with_skill/` versus `old_skill/` run artifacts. Use `scripts/score_delta.py` for paired-bootstrap and sign-flip-permutation gating on any close-call accept/reject. The full discipline (held-out gate, statistical gating, judge protocol, Pareto-front carryforward, length budget) is documented in `docs/hillclimb-improvements.md`.

## Contributing

See `CONTRIBUTING.md` for the contribution rubric, required eval updates, and PR checklist.

## Development workflow

When improving the skill:

1. Capture a concrete writing failure in `examples/` or `evals/cases.md`.
2. Use `runbooks/hillclimb-skill.md` for changes that touch doctrine, evals, or multiple repo artifacts.
3. Add or update the runnable case in `evals/evals.json`, `evals/rewrite-evals.json`, `evals/adversarial.json`, or `evals/meta-evals.json`.
4. Add the failure to `evals/failures/` or a compact card to `examples/cards/` when it teaches a reusable pattern.
5. If the change affects activation, update `evals/trigger-queries.json`.
6. Record the lesson in `Lessons_learned.md` and the change in `CHANGELOG.md` when doctrine or eval coverage changes.
7. Make the smallest doctrine change in `skills/anti-slop-writing/SKILL.md` or `skills/anti-slop-writing/references/`.
8. Run validation:

```bash
python3 scripts/validate.py
```

The validator also runs `skills-ref validate skills/anti-slop-writing` when `skills-ref` is installed.

If prose rules changed, manually test the skill against at least one affected case in `evals/cases.md`. A rule is not done until it improves a specific rewrite, not just the wording of the doctrine.

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

The doctrine compresses to five rules. The full versions live in `skills/anti-slop-writing/SKILL.md` and the references.

- More detail, earned importance.
- Code fences are for payloads, commands, examples, and fixtures.
- A punchy line without a named mechanism still reads as slop.
- Flow improves when each paragraph makes the next question possible.
- A conclusion should return to the concrete carrier, name what changed, and state what transfers.

## License

MIT. See `LICENSE`.
