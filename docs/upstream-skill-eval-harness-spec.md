# Upstream proposals for skill-eval-harness

Five proposals from a downstream repo, written for an agent working in the harness repo to evaluate against its in-progress PRs, issues, and `docs/eval-framework-roadmap-spec.md`. Each one comes from a concrete incident in this repo's 2026-08-29 eval rounds, with the evidence committed here.

| | |
|---|---|
| Proposing repo | `adewale/anti-slop-writing`, branch `claude/llm-cliche-highlighter-c2qqq8` |
| Target repo | `adewale/skill-eval-harness` |
| Harness commit audited | `2297000ffa91b63266e15c50fab6bfbd1f14441e` (main, shallow clone, 2026-08-29) |
| Downstream evidence | commits `b7e2bd0` (manifest fixes, oracle bridge) and `3fd94db` (scored run + disclosures); run dir `evals/results/2026-08-29-scored-run/` |
| Motivating context | This repo added a deterministic slop-lint oracle (`evals/oracles/slop_lint.py`, 22 detectors, self-testing) and bridged it into `evals/shared-benchmark.json` via a `script` assertion. Doing that end-to-end — including re-validating the manifest against harness main and running a 26-output judged A/B — surfaced these five. |

## Instructions for the harness-repo agent

1. Anchors below are **symbol names** in `skill_benchmark.py` at the audited commit; line numbers will have drifted — resolve by symbol, and re-verify each "current behavior" claim against your HEAD before acting.
2. Reconcile every proposal against open PRs, open issues, and `docs/eval-framework-roadmap-spec.md` (the migrate/oracle-tier code already cites its sections 1.7, 2.2, 3.3). An in-flight design that covers the same ground wins; these proposals describe problems and acceptance criteria, not required implementations.
3. Produce a disposition per proposal — `adopt` / `duplicate-of <PR/issue>` / `conflicts-with <PR/issue>` (say what conflicts) / `defer (reason)` — and report it back to the proposing repo so `TODO.md` there can be closed out.
4. Priority order: P1 and P2 are the substantial design items; P3, P4, P5 are small maintenance fixes, each with a one-session reproduction.

---

## P1 — Script assertions should be able to carry their checks (kill the per-oracle CHECKS table)

**Problem.** A `script` assertion names an oracle command, but what the oracle actually verifies for a given case lives in a Python table inside the oracle (`CHECKS: dict[case_id, ...]`). The truth about one case is split across two files that nothing keeps in sync: rename a case id in the manifest and its checks silently orphan; add a case and you must edit Python. Both oracles in this repo (`evals/oracles/fixture_oracle.py`, `evals/oracles/slop_lint_oracle.py`) carry such a table, and any participating repo's oracle will grow one.

**Current harness behavior.** `run_script_assertion` substitutes exactly two placeholders into the command argv: `{output_dir}` and `{output_path}`. The assertion payload has no way to reach the oracle.

**Proposed change.** Two new substitutions in `run_script_assertion` (and their documentation in `validate_script_assertion` / authoring docs):

- `{case_id}` — the enclosing case's id.
- `{checks_json}` — `json.dumps` of an optional free-form `checks` field on the assertion. Safe to pass as one argv element since script commands are exec'd as a list, not through a shell.

An assertion then becomes self-contained, and the oracle becomes a stateless check-runner:

```json
{
  "name": "slop-lint-script-oracle",
  "type": "script",
  "command": ["python3", "oracles/slop_lint_oracle.py", "{output_dir}", "{case_id}", "{checks_json}"],
  "checks": [
    {"detector": "no-chain", "max_hits": 0},
    {"detector": "performative-honesty", "max_hits": 0}
  ],
  "pass_exit_code": 0
}
```

The harness does not interpret `checks` — it stays an opaque contract between manifest author and oracle, preserving the existing "repo-owned oracle" boundary.

**Acceptance criteria.**
- `{case_id}` and `{checks_json}` substitute in `run_script_assertion`; `{checks_json}` with no `checks` field substitutes `null` (or validation rejects the combination — either, but documented).
- `validate_script_assertion` continues to accept unknown `{...}` tokens or begins rejecting them — decide explicitly; today unknown placeholders pass through silently, which is how a typo like `{output_dr}` would reach the oracle as a literal string.
- One example oracle in the harness's docs/examples consumes `{checks_json}`.

**Size.** Small (one function plus validation plus docs). Downstream, this deletes both CHECKS tables.

---

## P2 — `oracle: "strong"` should be earnable, not just declarable (a verify hook)

**Problem.** `oracle_tier` deliberately defaults `script` to `demo` because the harness "cannot see" a script oracle's truthfulness, and `migrate_manifest_data`'s checklist tells authors to mark `strong` "only for a verified … oracle" — but the harness has no mechanism to verify one (no self-test hook exists at the audited commit; grepped). This repo's manifest currently claims `"oracle": "strong"` on `pos-new-register-launch-strip` purely on the honor system, even though the backing detector module has a 160-check embedded self-test (`python3 oracles/slop_lint.py --self-test`) that `scripts/validate.py` runs on every downstream CI pass.

**Proposed change.** An optional `verify` command on `script` assertions (or, if preferred, a manifest-level oracle registry so several assertions share one verification):

```json
{
  "type": "script",
  "command": ["python3", "oracles/slop_lint_oracle.py", "{output_dir}", "pos-new-register-launch-strip"],
  "oracle": "strong",
  "verify": ["python3", "oracles/slop_lint.py", "--self-test", "--quiet"]
}
```

`skill-benchmark validate` executes `verify` (same path rules and cwd as `command`; no output placeholders — there is no run yet; bounded by `timeout_s` or its own timeout). Suggested policy: `verify` present and failing → validation FAIL; `oracle: "strong"` on a `script` assertion without any `verify` → validation warning, so existing manifests keep validating while the tier stops being free to claim. This also gives the "demo fixture trips every detector exactly once" self-test pattern (borrowed from simonw/tools' llm-cliche-highlighter, working well downstream) a first-class home: the fixture assertion lives inside the oracle's self-test, and the harness only demands the self-test pass.

**Acceptance criteria.**
- A failing `verify` fails `validate` with the script's output in the message.
- A `strong` script assertion without `verify` produces a visible warning (or a documented decision not to).
- Docs state what `strong` now means for scripts: deterministic *and* attested by a green verify at validation time.
- Interaction with roadmap-spec §1.7 reviewed (the tier ladder is already specified there; this adds the attestation edge).

**Size.** Medium (new validation path, sandbox/timeout considerations, docs). Highest leverage of the five: it converts the oracle-tier ladder from self-description into a checkable contract.

---

## P3 — `migrate` should stamp `should_trigger` when it is machine-derivable

**Problem.** Harness main requires trigger cases to carry a boolean `should_trigger`; this repo's version-1 manifest had five trigger cases with `should_trigger: null` — and every one stated the intended answer verbatim in `expected_behavior` ("Should return TRIGGER for this skill." / "Should return NO_TRIGGER for this skill."). Validation failed (`trig-readme-sounds-ai: trigger cases require an explicit boolean should_trigger`) on information the manifest already contained; the downstream fix was a five-line script (commit `b7e2bd0`).

**Current harness behavior.** `migrate_manifest_data` stamps version, default `severity`, default `oracle` tier, and a `graded?` marker, and emits a judgment-call checklist for what it will not decide — but does not touch trigger cases.

**Proposed change.** In `migrate_manifest_data`: for a trigger case with `should_trigger` missing or null, scan `expected_behavior` — match `NO_TRIGGER` **before** `TRIGGER` (substring trap: `TRIGGER` occurs inside `NO_TRIGGER`) → stamp `False`/`True`. No match, or conflicting matches → leave unstamped and append a checklist entry, consistent with the function's existing mechanical-half/judgment-half split.

**Acceptance criteria.** The five-case pattern above migrates cleanly with zero checklist entries; a trigger case whose `expected_behavior` names neither label produces a checklist entry, not a guess.

**Size.** Small.

---

## P4 — Reconcile validate-vs-grade strictness on version-1 manifests

**Problem.** At the audited commit, a version-1 manifest that *grades* fine *fails validation* on rules that postdate it. Observed sequence on this repo's unchanged v1 manifest: `validate` hard-failed twice —

```
FAIL: trig-readme-sounds-ai: trigger cases require an explicit boolean should_trigger
FAIL: holdout-fresh-llm-readme-2026-01: answer variant 'with_skill' needs at least one applicable gate or critical grading oracle
```

— and, once fixed, the success path itself printed the tension:

```
note: version-1 manifest grades with behavior-preserving defaults; `skill-benchmark migrate --check` shows the version-2 upgrade
```

So grading is version-aware and tolerant while validation is not: a participating repo's CI (which runs `validate`) rots on a harness upgrade with no manifest change. The second failure also forced a semantic decision on downstream judge-only hidden cases (their reviews are now `"severity": "gate"`), which a version boundary should have owned.

**Proposed change** (either satisfies the acceptance criteria):
- (a) `validate` applies the same behavior-preserving defaults to version-1 manifests that grading applies, demoting post-v1 requirements to warnings, with `migrate` as the documented path to strict mode; or
- (b) new-requirement failures on v1 manifests say so explicitly: `this rule applies to version >= 2 manifests — run skill-benchmark migrate`, so the fix is discoverable and the breakage is a versioning decision rather than an accident.

**Acceptance criteria.** A v1 manifest that graded green under the previous release either validates green (with warnings) under the next one, or fails only with messages that name the version boundary and the migrate command.

**Size.** Small-to-medium depending on the option; mostly policy.

---

## P5 — Quarantine malformed stored-verdict rows instead of failing the run

**Problem.** LLM judges emit almost-JSON: in this repo's 2026-08-29 scored run, one Haiku judge wrote an evidence string containing unescaped inner double quotes; that single line aborted the entire grade step, and the repair (escaping two characters, judgment content untouched) had to be done by hand and disclosed (`evals/results/2026-08-29-scored-run/run-metadata.json` → `repairs`). The incident was in this repo's private runner, but the harness's own read-back path has the same fail-the-run shape.

**Current harness behavior.** `load_result_rows` parses JSONL line-by-line; on any `json.JSONDecodeError` it falls back to parsing the *entire text* as a single object — for a multi-row file with one bad line, that fallback raises too, so one malformed row fails the whole load. `load_judge_results` then `die`s on the first invalid row it sees. Meanwhile the grading path already has the right vocabulary for partial evidence: skipped script assertions set `availability: "partial"`.

**Proposed change.** Per-row quarantine in `load_result_rows`/`load_judge_results`: a row that fails to parse or fails `validated_result_row` is rejected *individually*; the affected judge task grades as `passed: null` with `availability: "partial"` and evidence naming the file, line, and parse error; the run summary lists quarantined rows. Strictness stays where it protects correctness: duplicate ids, conflicting `judge_task_id`/`id`, and out-of-range scores in rows that *did* parse should still fail loudly. Optionally, a conservative pre-pass that repairs the one empirically common defect (unescaped interior quotes inside a string value) before quarantining — but quarantine alone meets the bar.

**Acceptance criteria.** A judge-results file with one malformed line among N: the run completes, N−1 rows grade normally, the malformed row's task reports `availability: "partial"` with file/line/error, and the summary counts quarantined rows. Duplicate-id detection still fails the run.

**Size.** Small.

---

## Explicit non-goals (stays downstream, do not upstream)

- The 22 slop detectors and their word lists (`evals/oracles/slop_lint.py`) — doctrine-coupled to this skill and expected to drift with it; other skills' oracles verify entirely different things. The harness's job is the contract (P1/P2), not the detectors.
- This repo's `deterministic_checks` schema on its private suites and the `run_evals.py lint`/merge pipeline — the private judge-protocol counterpart of capability the harness already has (`benchmark --allow-scripts --judge-results`). Nothing missing upstream there.
- An `oracle_kit` shared library was considered and ranked below all five: P1 shrinks oracles enough that shared scaffolding stops mattering.

## Downstream evidence index (all on `adewale/anti-slop-writing`, branch `claude/llm-cliche-highlighter-c2qqq8`)

- `evals/oracles/slop_lint.py` — self-testing detector registry (P2's verify target).
- `evals/oracles/slop_lint_oracle.py`, `evals/oracles/fixture_oracle.py` — the two CHECKS tables P1 eliminates.
- `evals/shared-benchmark.json` — the `strong`-claiming script assertion (P2), stamped trigger booleans (P3), gate-marked judge-only cases (P4); maintenance note in `evals/shared-harness.md`.
- `evals/results/2026-08-29-scored-run/run-metadata.json` (`repairs`) and the run note's disclosure §7 — the malformed-judge-row incident (P5).
- `docs/deterministic-graders.md` — the division-of-labor doc these proposals extend.
