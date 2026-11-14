# Rewrite-only re-judging — prepared, not run

**No extraction or judgment has run.** This directory holds the frozen design:
[PREREGISTRATION.md](PREREGISTRATION.md), `manifest.json` (37 in-scope cases, 444
baseline outputs, opaque ids, output hashes) and `prompt-templates.json`. Nothing here
is a result.

The study re-judges existing baseline outputs in two views, the full response and the
verbatim deliverable alone. It asks whether the skill's judged task-fulfillment
advantage comes from its prose or from the critique the judges also read.

## Run it

Model calls use the baseline's transport: the `claude` CLI for Opus, and the Pi SDK
for GPT-6.1 Sol through `scripts/subscription_model.mjs`. Both need subscription
access on the owner's machine. Work in the ignored `eval-workspace/` so raw attempts
stay out of the tree until they are archived.

```bash
mkdir -p eval-workspace
tar -xzf evals/results/2026-11-14-subscription-baseline/trials.tar.gz -C eval-workspace
cp -R evals/results/2026-11-14-rewrite-only-rejudge eval-workspace/rewrite-only-rejudge
```

```bash
export ASW_PI_SDK=/path/to/pi-coding-agent/dist/index.js
```

```bash
python3 scripts/rewrite_rejudge.py extract --baseline eval-workspace/subscription-baseline --dest eval-workspace/rewrite-only-rejudge
```

```bash
python3 scripts/rewrite_rejudge.py judge --baseline eval-workspace/subscription-baseline --dest eval-workspace/rewrite-only-rejudge
```

```bash
python3 scripts/rewrite_rejudge.py analyze --baseline eval-workspace/subscription-baseline --dest eval-workspace/rewrite-only-rejudge
```

Each stage resumes: completed slots are skipped, and every failed attempt is kept.
The run stops on any access, model or rate-limit failure. `judge` refuses to start
until every extraction has completed or exhausted its three attempts.

## Publishing results

Copy `comparisons.json`, `summary.json`, `scores.json`, `exclusions.json` and the
`*-status.json` files back into this directory. Archive `extract/` and `judge/` as
`trials.tar.gz` with a checksum, as the baseline does. Then replace this README's
status line with the result, apply the interpretation rules exactly as registered, and
record any deviation in an `AMENDMENTS.md`. Report a null or critique-driven result as it
stands.
