# Protocol amendments

## A1 — stdin transport repair, before any judging

Original registration: `28e36b2`. The first antithesis apply stage completed 72 of
96 logical outputs. The other 24 slots (all GPT skill-arm slots) each exhausted
three host-process attempts with Node `readFileSync(0)` reporting `EAGAIN` on the
large inline package. All 72 failed processes have empty stdout, a Node stdin-read
stack trace, and no provider response. These are **pre-request infrastructure
failures**, not 72 model generations or 24 bad writing responses.

Before any judge request or score inspection:

- Replace synchronous stdin reading in `scripts/subscription_model.mjs` with an
  asynchronous stream reader. The model, credentials, prompt, effort, and cap are
  unchanged. A regression test sends and roundtrips a 320 KB prompt through an
  actual subprocess pipe without invoking any provider.
- Retain the original failed slot directories under `infrastructure-failures/`
  and the first stage-status file. Restart only these 24 ungenerated slots with
  the repaired transport and the same frozen manifest. The 72 completed outputs
  are retained verbatim and skipped by resume.
- The three-attempt model-generation/schema-replacement policy still applies.
  These 72 proven pre-request failures do not consume that cap. No successful
  response is excluded or regenerated. No prompt, rubric, sampling, family,
  outcome, guard, or analysis rule changes.

The original helper remains reproducible from the registration commit. The
amendment commit is made before restarting; the final archive retains both the
failed transport evidence and successful generation attempts. Report these
failures separately from provider calls and judgment-schema replacements.
