# Live initial-turn skill activation — completed controlled measurement

**174 valid scored sessions: 29 verbatim queries × three fresh contexts × two clients.**
Activation means successful delivery of the full instruction body, not metadata discovery,
a tool attempt, a launch acknowledgment, self-report or a final rewrite. Both clients
passed forced-full-load controls. All scored traces were reparsed and reproduced offline.

## Query-majority results

A query activates when at least two of its three sessions load the full body. Repeats
are not independent queries. These are descriptive rates, not a writing-efficacy gate.

| Configuration | Positive sensitivity | Negative specificity | Near-negative specificity |
|---|---:|---:|---:|
| Pi 1.4.0 controlled SDK / GPT-6.1 Sol | **7/12 (58.3%)** | **16/17 (94.1%)** | **5/6 (83.3%)** |
| Claude Code 2.1.323 guarded restricted CLI / Sonnet 5.5 | **7/12 (58.3%)** | **17/17 (100%)** | **6/6 (100%)** |

| Configuration / selection | Positive sensitivity | Negative specificity |
|---|---:|---:|
| Pi tune | 3/7 (42.9%) | 10/10 (100%) |
| Pi historical holdout | 4/5 (80%) | 6/7 (85.7%) |
| Claude tune | 5/7 (71.4%) | 10/10 (100%) |
| Claude historical holdout | 2/5 (40%) | 7/7 (100%) |

Pi loaded the body in **26/87** sessions; Claude in **20/87**. Pi's false-positive query
was `near-neg-fact-check-blog` (3/3 loads). `rates.json` publishes every query, its labels,
split, count/3 and majority result. All 29 queries per client had three valid sessions.
No label or skill description was changed in response to these results.

**Interpretation:** initial-turn body loading is incomplete under these configurations.
Queries do not include source documents; an agent can legitimately ask for the document
before loading a writing skill. This does not measure eventual multi-turn activation,
completed editing, skill quality, default-client routing, or a pure client effect:
client and model are confounded. Public historical holdouts are not newly sealed data.

## Instruments and material deviations

See [PREREGISTRATION.md](PREREGISTRATION.md) and **all six revisions** in
[AMENDMENTS.md](AMENDMENTS.md). The installed tree and all query text remain unchanged.

Pi uses a real native AgentSession, standard metadata/system-prompt construction,
in-memory history/settings, explicit resources and a single native read tool with
realpath-confined operations. The body is not preloaded. Claude uses native Read/Skill
with an explicit minimal plugin; built-in metadata remains visible and inventoried.
Neither instrument inherits repo/user writing instructions or other project skills.
Trusted host/provider connections are outside the file-tool restriction; this is not
a general OS sandbox.

Two deviations occurred **after partial scoring**, not merely before collection:
- **Capability boundary repair:** declaring Read/Skill at startup did not stop built-in
  `dataviz` from enabling and invoking Write. The first launch stopped after 13 completed
  observations (eight Pi, five Claude); three invalid CSS-layout attempts were retained.
  The entire original Claude cohort, including all five apparently valid observations,
  was quarantined, never counted as false negatives. Start a fresh fixed 87-slot Claude
  epoch-2 cohort. Preserve the unchanged Pi epoch-1 observations.
- **Native-rejection observer repair:** the guarded launch stopped at 54 completions
  when Claude requested unavailable Bash. The native dispatcher rejected it with an
  explicit error before hook dispatch; no command ran and workspace hashes were unchanged.
  Reparse that original trace without regeneration. Four later sessions exhibited the
  same native unavailable-tool rejection. Their attempts are not executed capabilities.

The enforced Claude guard intercepts every available tool via a `PreToolUse` exec hook,
matcher `*`, `onFailure: block`. It permits only the target skill and reads inside its
real directory; all other skills/tools, including writes/agents/network tools, are denied.
Audit receipts per tool-use ID and unchanged-workspace hashes. Eligibility includes a
fresh probe that **actually selected and was denied dataviz**, with no file written.
These are **guarded controlled-Claude rates**, not stock behavior. The amendment is a
material configuration change, not an invisible cleanup. Original logs, hashes and
excluded observations remain in `pre-guard/` inside the archive.

Earlier pilot-only repairs concerned Pi's read allowlist, explicit Claude discovery,
built-in plugin-origin parsing and Read line-prefix normalization. All pilot controls
are excluded from rates. Startup-inventory checks alone were insufficient; the failure
and the fail-closed repair are preserved rather than silently erased.

## Unmeasured clients

- **Codex 0.145.0:** the native subscription probe rejects the registered `gpt-6.1-sol`
  model as unsupported with a ChatGPT account. Pi availability does not establish native
  Codex availability. This study makes **no Codex routing claim**, not a claim that every
  other native Codex model is unusable; another model needs a separately fixed instrument.
- **OpenCode:** absent at the recorded preflight; not installed or substituted. No rate.

## Retention, accounting and reproduction

The archive retains **194 distinct traces**, including scored sessions, all pilots and
the excluded cohort, with **318 distinct returned provider response IDs**. One Pi pilot
failed its active-tool assertion before `session.prompt()` and produced no provider
receipt/cost counter; it is not a hidden zero-score observation. Returned list-price
counters total **$3.12**, not an invoice or separately billed API spend. Exact commands,
queries, model/session IDs, resource inventories, guard decisions, stdout/stderr, process
statuses and historical source hashes are retained. No credentials were copied.

The last resume ran 10:09:40–10:16:53 UTC; that is **not the full campaign duration**:
it reused valid earlier Pi/guarded-Claude observations and includes no replacement of
successful routing outcomes. Earlier phase/pilot logs are retained separately.

```bash
python3 scripts/verify_followthrough.py verify --kind activation \
  --dest evals/results/2026-11-14-live-activation
```

Use the publication commit so instrument source hashes match. Verification checks the
published inventory, safely extracts `trials.tar.gz`, audits all 174 raw traces and exact
query/model/slot identities, independently reconstructs query-majority counts, reproduces
`rates.json` and `summary.json` byte-for-byte, and recomputes retained usage accounting.
It performs no model calls. `reproduction.json` and `checksums.json` exclude themselves
from self-hashing; the rest of the published report is inventoried.

These observations do not settle the separate baseline fidelity-judge disagreement.
The 18-item human calibration packet is ready, but human scoring is still pending.
