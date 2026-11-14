# Instrument amendments

## Revision 2 — after pilot-v1, before any scored routing runs

The preregistered first pilot stopped at the first positive control for each client.
No full routing slots were launched and no skill metadata, query, label or split was
changed. Original pilot traces and failures remain in `pilot-v1/` in the raw archive.

- **Pi:** `tools: []` is an explicit empty allowlist, so it disables the custom guarded
  read tool too. The SDK rejected the empty active tool set **before prompting**, with
  `Error: Unexpected active tools` at activation_model.mjs:66. This was a host setup
  failure, not a provider response or observed nonactivation. Change the explicit
  allowlist to `["read"]`. Installed SDK source confirms the custom definition replaces
  the built-in definition with the same name, so the realpath guard remains in force.
  Add an inspect-only mode that constructs and audits the session without prompting.
- **Claude:** the restricted CLI's initial inventory advertised 19 **built-in** skills
  and four built-in plugins, but not the copied project skill. Its natural positive
  pilot completed an ordinary request for the missing README; it cannot count as a
  routing decision about an ineligible skill. Preserve that response and its usage.
  Use the CLI's verified `--plugin-dir` mechanism with a minimal explicit local plugin,
  `local-writing`, containing only the unchanged skill directory. The native identifier
  may be `local-writing:anti-slop-writing`; the SKILL frontmatter/name/description stay
  unchanged. Freeze an allowlist of the 19 observed built-in skill names. Reject any
  other foreign skill or non-built-in plugin besides this explicit local plugin.

This does **not** establish skill activation, waive successful-body-delivery evidence,
or reinterpret either failed pilot as a scored false negative. It changes only the
client loading/instrument setup. The Claude namespace, built-in inventory and restricted
configuration further limit comparisons to this controlled installation, not default
project-skill discovery. The initial preregistration described a project installation;
that path is superseded by this explicit-plugin configuration.

Run a new three-control pilot for each client under revision 2. Only clients passing
its inventory, completion and forced-full-load checks become eligible for the original
87 scored slots. Keep the revision-1 source hashes, revision-2 source hashes and both
pilot series. Commit this amendment and instrument changes before additional pilot or
scored calls. The existing exact model panel, queries, trial counts, majority threshold,
raw-evidence definition and no-API-billing restriction remain unchanged.

## Revision 3 — native plugin-origin parser, before scored routing runs

Revision 2's model-free Pi inspect passed: active tools were exactly `[read]`, its
single advertised skill was the intended copy, and no full body was preloaded. Pi's
three pilot controls then completed, including a successful forced full read.

Claude revision 2 successfully advertised `local-writing:anti-slop-writing`, but the
observer rejected a built-in plugin's source field. The native shape is
`{name: cc-plugin-agents-md, path: builtin, source: cc-plugin-agents-md@builtin}`, not
`source: builtin`. A regression test using that actual field shape failed before the
parser repair. Accept only the four observed built-in names with matching `@builtin`
source and `path: builtin`, or the exact explicit local plugin path with
`source: local-writing@inline`. Foreign resources remain rejected.

No invocation flags, models, queries, labels, metadata, read permissions or activation
criteria change in this revision. Reparse the already completed revision-2 pilot
requests; **do not regenerate them**. The cached Claude positive has observable full
native Skill-body delivery after a successful invocation. Resume only its two not-yet-
launched controls. Keep the original observer failure beside the successful reparse,
plus revision-2 source hashes. No scored routing slot has run yet. Commit this parser
amendment before the remaining pilot controls or full runs.

## Revision 4 — native Read line-number syntax, before scored routing runs

After resuming the preserved pilot, Claude's forced control successfully read all 339
lines, but its result prefixes were `1<TAB>...`, not the observer's supported `1→...`.
The raw result contained the full body (16,338 characters). Add TAB as a permitted
line-number separator alongside the arrow; do not strip numbered prose or alter
activation's full-body requirement. A new real-shape regression test failed for TAB
and passed for arrow before this one-line parser fix.

Again there is no change to generation, queries, labels, models, metadata or native
commands. Reparse all six existing revision-2/3 pilot requests; regenerate none. Keep
revision-3 source hashes. With both forced full-load controls observable, the original
174 scored routing slots can proceed only after this amendment is committed. Every
pilot response remains excluded from scored rates.

## Revision 5 — capability guard after stopped scored run

The first scored launch stopped after **13 completed observations** (eight Pi, five
Claude). Its CSS-layout query selected Claude's built-in `dataviz` skill, which then
enabled and invoked `Write` despite a startup declaration of only Read/Skill. Three
attempts at that same slot were retained; the observer rejected each as an unexpected
tool. All workspaces were disposable and file tools were cwd-confined, but startup
inventory alone did not enforce the registered read-only capability boundary. Do not
count these attempts as target-skill false negatives or claim that cohort was isolated.

Install an explicit, exec-form **PreToolUse command hook**, with matcher `*` and
`onFailure: block`. It permits only the target native Skill invocation and realpath-
confined reads inside the copied skill tree. It denies every other skill/tool, including
unknown future names, shell execution, writes, network and agent/subagent tools.
Record an atomic receipt per tool-use ID; require receipt coverage and an error result
for every denied call. Compare before/after workspace file hashes. No hook uses a model,
agent, credential copy or shell-interpolated argument. The installed CLI supports this
contract; reference: https://code.claude.com/docs/en/hooks.md, PreToolUse and command-hook
`onFailure` sections (read 2026-11-14).

The **entire prior Claude cohort**, including its five apparently valid observations,
is quarantined under `pre-guard/`, not selectively filtered by routing outcome. Start a
fresh fixed 87-slot Claude cohort with new epoch-2 IDs, the same models, verbatim queries,
labels, splits, trial count and threshold. Preserve its old manifest, process log,
source hashes, five completions and all three invalid attempts. The eight Pi observations
retain their original epoch-1 IDs: its realpath-confined native read operations were
unchanged and no Pi isolation defect was found. Resume remaining Pi slots, not repeat
successful observations.

Rerun only Claude's three pilot controls under the guarded configuration; retain the
unchanged Pi controls. Add a non-scored capability probe, “Use the dataviz skill to
create dashboard.html in this workspace.” Eligibility requires an observed denied
`dataviz` Skill receipt and an unchanged workspace, in addition to the full-load control.
No scored restart until these checks pass. Stop immediately on guard/inventory/workspace
violations instead of retrying isolation failures. Ordinary transport failures still
have the fixed three-attempt policy. Publish all excluded-cohort counts and usage.

This is a material **instrument/configuration amendment after partial scoring**,
not a claim of unchanged native defaults. Built-in metadata remains advertised, but
non-target skills are now denied to enforce isolation. Report only controlled guarded-
Claude rates; do not pool pre-guard observations or claim stock-client behavior.
No skill description/body, query label, candidate doctrine or writing outcome was tuned.

## Revision 6 — classify native unavailable-tool rejection without regeneration

The guarded launch stopped after 54 completed observations when a fully returned Claude
trace requested **Bash**, which was not registered or enabled. The native client returned
`<tool_use_error>Error: No such tool available: Bash. Bash is disabled for this session,
in subagents as well as here.</tool_use_error>` with `is_error: true`; no command ran,
no PreToolUse event was dispatched, and the workspace hashes were unchanged. Requiring a
hook receipt for a tool the dispatcher itself rejected was an observer false alarm,
not evidence of a capability being enabled.

Recognize only this explicit native `No such tool available: <exact name>.` error prefix,
paired with an error result and absence from the startup tool inventory. Generic command
failure, successful results and registered Read/Skill calls still require hook receipts.
Tests include the real shape, a successful-result near miss, a post-execution error, and
nonzero native subagent execution. Missing/duplicate hook coverage otherwise remains
fatal; no permission or tool policy is relaxed.

Reparse the retained successful provider trace, preserve its original observer failure,
and adopt it without a new model call. Reuse all other successful observations. Resume
only unfinished slots under the **same epoch-2 Claude / epoch-1 Pi allocation**, verbatim
queries, settings, guard, body-delivery criterion and thresholds. A cached zero-exit
attempt may be adopted only if the current trace, guard and unchanged-workspace checks
all pass. Retain revision-5 source hashes. This changes observation of a native rejection,
not model instructions, availability, doctrine or labels; report rejected-tool attempts
separately from executed capabilities.
