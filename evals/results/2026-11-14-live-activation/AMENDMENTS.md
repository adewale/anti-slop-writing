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
