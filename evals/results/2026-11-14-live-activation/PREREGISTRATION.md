# Live initial-turn activation — preregistration

Registered before this campaign's live pilot or scored routing requests. This is a
routing measurement, **not writing efficacy**, and not the tool-free baseline's
hypothetical routing classifier. Installed skill/base is merged #22 at
`92d37020c39da5f5f497b550f62997539318137b`; freeze its complete directory unchanged.
The owner authorized these subscription-backed model studies without a cost concern.
No API-key billing, credential copying, provider fallback or quota bypass is authorized.

## Clients and scope

- **Pi 1.4.0 controlled SDK AgentSession**, `openai/gpt-6.1-sol`, low thinking.
  Use Pi's standard system-prompt/skill-metadata construction and native read-tool
  definition, explicit single-skill resources, no extensions/context files/templates,
  in-memory settings/history, no compaction/retry and no tools except `read`.
  The read operations resolve real paths before access and can open only the isolated
  skill tree, including references; symlink escapes fail closed. ModelRuntime uses the
  existing subscription credential store directly, with an explicit subscription check.
  This is a live Pi agent, **not stock CLI/TUI default configuration**.
- **Claude Code 2.1.323 restricted CLI**, `claude-sonnet-5-5`, low effort, provider-default
  sampling. Fresh UUID and empty temporary workspace, one project skill in
  `.claude/skills/anti-slop-writing`, native default system prompt and Skill/Read tools
  only. `--restricted` confines file tools to the workspace and ignores user/project/
  local settings; strict empty MCP config, no persistence and dontAsk permissions.
  API-key/token environment overrides are removed. Do not use `--bare`: it disables
  subscription/keychain auth. Do not use safe mode: it disables skill discovery.
- **Codex 0.145.0** is subscription-authenticated but the recorded native CLI access
  probe rejects `gpt-6.1-sol` with “not supported ... with a ChatGPT account.” Its Pi
  ModelRuntime availability does not prove native Codex availability. No Codex routing
  rate is claimed without an independently fixed supported model/instrument.
- **OpenCode** is absent on PATH and the checked conventional installation paths.
  Do not install it or invent supported flags/authentication for this experiment.

Client and model effects are confounded; do not interpret different routing rates as
pure client differences. Filesystem capability restrictions limit model access; they
are not a general OS sandbox around trusted host code or the provider connection.

## Pilot and eligibility

Before full runs, make exactly three fresh pilot requests per proposed available client:
`pos-readme-polish`, `neg-em-dash-mechanical`, then a forced-read positive control
(“Read <canonical SKILL.md> in full, then state its first heading. Do not edit any file.”).
Natural positive/negative pilot outcomes are never included in scored rates. Do not
require correct natural routing for eligibility: only complete observable traces,
correct model/resources, and successful full instruction delivery in the forced control.
The forced request is an instrument check, not natural activation evidence.

Preflight found no user skill directories at `~/.claude/skills` or `~/.agents/skills`,
no user `~/.claude/CLAUDE.md`, and no CLAUDE.md in the temporary directory's ancestors.
Fresh opaque workspaces cannot inherit an existing project memory. Restricted CLI
settings and initial skill/tool/MCP inventories are audited. Any unexpected resource
inventory blocks that client; do not silently count it as nonactivation. Claude's
complete hidden built-in prompt is not exported, a residual client limitation.
If a native loader hides body delivery, classify the instrument as unobservable and
leave full rates unmeasured rather than substitute a prose self-report.

## Scored allocation and observables

Freeze all **29 unchanged queries**, labels and splits from `evals/trigger-queries.json`:
12 positives, 17 negatives, including six deliberate `near-neg-` queries. Three new
processes/contexts per query per eligible client, **87 runs/client**, maximum 174 runs
for the two proposed clients. Seed **261116** randomizes submission order, not provider
sampling. Two concurrent slots maximum. A failed pilot leaves that client's 87 slots
explicitly unrun. Preserve the full intended manifest and eligibility decision.

Submit the literal query, not a routing question or explicit skill command. Queries
lack source documents; models may ask for them before reading the skill. Measure
**initial-user-turn loading**, not eventual multi-turn activation or task completion.
A fresh isolated skill copy accompanies each session. No labels, assertions, expected
routing decisions, other traces, or repository instructions are accessible to it.

Record separately:
1. Skill metadata advertised and eligible.
2. Attempted native Skill invocation or canonical SKILL.md read.
3. Successful delivery of the **full instruction body** to model context (primary).

Pi requires a matched canonical read call and non-error tool-result body. Claude
requires either a successful canonical Read result containing the body (line-number
prefixes may be normalized), or a matched successful native Skill invocation plus
observable injected body in tool/user context. Normalize whitespace only for body
matching. Metadata scanning, a call without a successful result, partial reads, a
“Launching skill” acknowledgment without its body, a final rewrite, and “I used it”
are insufficient. Failed skill loads are invalid/blocked observations, not negatives.
Partial successful reads are reported as attempts, not full-body activation.

## Analysis, failures and publication

Report each query's observed count/3 and majority activation (≥2/3; frozen threshold .5).
Report positive sensitivity, negative specificity, six-near-miss specificity, tune and
historical holdout selections separately. A query without three valid runs gets no
majority correctness value. Repeats are not independent query units: do not call 87
runs 87 independent cases. This is descriptive routing evidence, with no inferential
promotion or writing-quality claim and no tuning of metadata from holdout outcomes.

Retain raw structured stdout/stderr, process status/duration, exact commands, query,
model identity, session IDs, frozen tree/query hashes, tool results and normalized
receipts. Reparse every scored trace during analysis and require raw/receipt equality.
Completed valid/nonactivating outcomes are not regenerated for preference. Pilot
attempts are one each. For scored technical transport/incomplete-trace failures allow
up to three attempts at the same slot, retain each; stop on auth/quota/model/inventory
failures instead of substituting a client. A completed blocked read is retained as
invalid, not retried as a way to change routing. Stop after three exhausted attempts.

Estimated 6 pilot requests plus up to 174 agent turns, typically 1–3 provider calls per
turn; approximately 10–30 minutes at two workers and $5–$25 list-price-equivalent, not
a subscription invoice. Actual usage/durations and inaccessible clients are disclosed.
Any instrument amendment after pilot is committed before scored runs and may repair
only observability/transport, never query labels or skill metadata. Publish nulls and
false positives as well as successful activations. Human fidelity calibration remains
separate; another model is not a human reviewer.
