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
