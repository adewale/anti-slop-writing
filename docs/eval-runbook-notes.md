# Eval and runbook notes

These notes record the outside ideas that now shape the repo's improvement loop.

## Runbooks for hillclimbing

Source: Jonathan Lebensold, “Runbooks: what agents need to hill-climb” (`https://lebensold.substack.com/p/runbooks-what-agents-need-to-hill`).

Applied idea: a skill-improvement task needs more than a loose instruction and less than a fixed workflow. The repo now has `runbooks/hillclimb-skill.md`, which names:

- the outcome to achieve;
- the output manifest that must exist before the task is done;
- evaluation criteria;
- a bounded judge-refine-rejudge loop;
- common fixes;
- a final checklist and verification commands.

The useful mechanism is not “write more process.” It is preventing premature completion: an agent should not stop after updating one file if the eval, lesson, changelog, and failure corpus also need to change.

## Evals that can break

Source: Lun Wang, “Your Evals Will Break and You Won't See It Coming” (`https://wanglun1996.github.io/blog/your-evals-will-break.html`).

Applied idea: a passing eval suite can still be stale. The repo now treats all-pass scores as a coverage signal, not proof that the skill is finished.

Concrete changes:

- `evals/meta-evals.json` checks for ceiling effects, metric artifacts, trigger drift, judge drift, and new failure modes.
- `evals/rewrite-evals.json` separates rewrite quality from critique labeling.
- `evals/adversarial.json` checks false positives and overgeneralization.
- `LESSONS.md` records what not to overgeneralize.

The practical test is whether a new model could pass the old evals while failing in a new way. If yes, add a meta-eval or failure-corpus entry before changing doctrine.
