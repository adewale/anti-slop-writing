# Rewrite-only re-judging — revised design, not run

**No extraction, audit or judgment has run.** Revision 2 prospectively repairs
PR #29; see [AMENDMENTS.md](AMENDMENTS.md) and [PREREGISTRATION.md](PREREGISTRATION.md).
The frozen manifest covers 37 cases, 444 baseline outputs, hashes and opaque ids.
No new writing outputs or installed doctrine changes are planned.

The study compares the full blinded response with a verbatim deliverable-only view.
It measures view sensitivity, not a pure causal critique or length effect. Empty
deliverables remain outcomes. An independent extraction audit must pass **before any
judging**; flagged extractions cannot be silently removed, regenerated or replaced
with the reliability extractor's answer.

## Run

Use only existing subscription access: Claude CLI for Opus and the Pi SDK through
`scripts/subscription_model.mjs` for GPT. No credential copying or separately billed
API access. Work in ignored `eval-workspace/`; retain every attempt.

```bash
mkdir -p eval-workspace/rewrite-rejudge-input
python3 - <<'PY'
import tarfile
with tarfile.open('evals/results/2026-11-14-subscription-baseline/trials.tar.gz') as archive:
    archive.extractall('eval-workspace/rewrite-rejudge-input', filter='data')
PY
cp -R evals/results/2026-11-14-rewrite-only-rejudge eval-workspace/rewrite-only-rejudge
export ASW_PI_SDK=/path/to/pi-coding-agent/dist/index.js
python3 scripts/rewrite_rejudge.py extract --baseline eval-workspace/rewrite-rejudge-input/subscription-baseline --dest eval-workspace/rewrite-only-rejudge
python3 scripts/rewrite_rejudge.py audit --baseline eval-workspace/rewrite-rejudge-input/subscription-baseline --dest eval-workspace/rewrite-only-rejudge
```

Inspect `extraction-audit.json`. If any check fails or is missing, **stop for review**.
This is an automated instrument audit, not the outstanding human fidelity calibration.
Only with a complete passing audit:

```bash
python3 scripts/rewrite_rejudge.py judge --baseline eval-workspace/rewrite-rejudge-input/subscription-baseline --dest eval-workspace/rewrite-only-rejudge
python3 scripts/rewrite_rejudge.py analyze --baseline eval-workspace/rewrite-rejudge-input/subscription-baseline --dest eval-workspace/rewrite-only-rejudge
```

Completed slots are cached with request hashes. Schema failures allow up to three
attempts. Transport/access/model/rate-limit failures stop; an existing fatal attempt
requires explicit review rather than an automatic retry. A retained complete raw
response can be reparsed without another provider call.

## Publication

Archive all primary/reliability extractions, audits, judgments (if reached), failed
attempts, frozen inputs and process logs. Publish hashes, selected-response audits,
returned cost counters, and model-free reproduction. If the audit blocks judging,
publish that measurement failure and a review packet; do not call it a skill result.
If scoring completes, publish case-wide attrition, original/full/deliverable contrasts,
prompt shift, view attenuation, both fact conditions, lengths and reliability. Apply
the registered uncertainty labels; a zero-crossing interval does not show equivalence.
