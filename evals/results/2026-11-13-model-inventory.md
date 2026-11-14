# Model access inventory — 2026-11-13

No callable apply or judge model was confirmed. No model ID was returned by an API,
no trial completed, and no judge panel was used. The no-skill baseline remains unrun.

| Provider | Interface checked | Exact model ID returned | Outcome |
|---|---|---|---|
| OpenAI | `codex-cli 0.167.0-alpha.4`, ChatGPT login, default model | None | Tiny `OK` probe failed: models endpoint returned HTTP 401; the turn failed because its access token could not be refreshed. |
| Anthropic | `claude` executable and Anthropic credential variable names | None | No CLI or key configured; no request could be made. |
| Open weights | Ollama/LM Studio clients and configured endpoint/key variable names | None | No client or endpoint configured; no request could be made. |

Probe command (no case, skill, assertions, or repository files supplied):

```bash
codex exec --ephemeral --skip-git-repo-check --sandbox read-only --json \
  -C /workspace/review-scratch -o /workspace/review-scratch/model-probe.txt \
  'Model access probe only. Use no tools, read no files, and reply with exactly OK.'
```

The first attempt failed during local initialization because the Codex runtime directory
was read-only. A retry with write access to that runtime directory reached authentication
and failed before generation. The failed turn events are retained in
`2026-11-13-review-reproduction/model-probe.jsonl`; there is no generated response.
`codex login status` reported a ChatGPT login, which did not imply usable credentials.
No explicit model ID was guessed or selected.

Completed eval calls: **0**. Completed inventory generations: **0**. Token usage and
billing were not returned for the failed requests; no dollar cost is asserted.
The owner spend ceiling in the handoff is blank. Before baseline runs, establish working
access, record returned model IDs and sampling controls, and estimate cost. The handoff
permits Phase 3 with a blank ceiling, then requires stopping and reporting cost;
Phase 4 needs a stated ceiling.
`TODO.md`'s cross-family judge item stays open. This chat's own assistant context is not
an independent apply trial or judge panel.
