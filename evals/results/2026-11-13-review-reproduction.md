# Review reproduction — 2026-11-13

The claimed 2026-05-31 proof does not survive correction: removing its version-specific
field assertion gives p≈0.126; seven equal-weight family means give p≈0.245. The
standing baseline has 38/38 scores at 1.0. These checks do not establish whether the
current skill beats no skill.

Reviewed base: `70f9803b4c717a98c713706101638f2406105a40`, matching the handoff.
No new model calls or scoring of generated outputs were used. This is a deterministic
reanalysis of committed records and source code. Original raw run data are preserved.

Run from the repository root with history available:

```bash
python3 evals/results/2026-11-13-review-reproduction/reproduce.py
```

The script reads files from the fixed base commit using `git show`, so subsequent
instrument and case repairs do not change what it reproduces. Full stdout is in
`2026-11-13-review-reproduction/output.txt`.

| Handoff finding | Status | Reproduced evidence |
|---|---|---|
| 1. Invented facts rewarded | Reproduced in the case definitions | Original `weak-conclusion` demands a pelican absent from the prompt; original coordination, hedged-reader, and conclusion assertions demand unsupplied jobs, tradeoffs, or artifacts. The audit file retains every old assertion. Historical model judgments were inspected as stored records, without an independent rejudge. |
| 2. Statistical-proof artifact | Reproduced | Five of nine old-arm failed assertions require `Rewrite check`; removing that assertion from six cases gives N=42, delta +0.0357, bootstrap 95% CI [+0.0079, +0.0714], p=0.1258. Equal-weight means of seven families give p=0.2451. Every after output is longer: 42/42 by whitespace words. Doctrine commit `de3cf59` precedes holdout commit `725d546` by 43m51s. |
| 3. Ceiling and gate defects | Reproduced | Baseline: 38 perfect scores. Five perfect independent gains yield p=0.0614, REJECT. Eight duplicate IDs yield ACCEPT in the original scorer. A ten-case total regression yields REJECT: the regression-direction bug is already fixed on main. |
| 4. Missing no-skill comparison / identical outputs | Partly reproduced | The stop-slop comparison has 30/36 byte-identical A/B output pairs, including its panel subdirectory. This does not prove who generated them. The reported earned-antithesis harm in the shared harness is a small directional observation, not a confirmed effect. Its six-case replication family is present; this review did not run it. |
| 5. Open-book cases | Reproduced, with a narrower count | Prompt-only normalized matching finds 27 cases sharing six words with skill text and 19 sharing eight. The handoff's approximate 32 includes assertions too; this script does not reproduce that exact counting convention. The tweet holdout and tune case point to the same full input. |
| 6. Stated checks absent | Reproduced | Dynamic rubric absent from judge template; apply/judge/assertions combined in prepare; no recorded lengths, beta-binomial intervals, or executable word-growth gate. Rewrite split is 19/5 (79/21). Historical SKILL.md growth is +554 at `48f29fc` and +355 at `de3cf59`. Shared-harness private prompt refs are absent. |
| 7. Deterministic loopholes | Reproduced | Hinge matches `also`; appositive check accepts `Do not keep it.`; original fixture oracle accepts `HMAC retry receipt` and the supplied groundbreaking/seamless/99.99% sample. |
| 8. Contradictions in runtime text | Partly reproduced by inspection | Mandatory `Remembered line`, non-invention versus unsourced worked examples, different editing-pass lengths, decorative fences, and maintainer notes are present. This review does not assign measured failure rates to these features or reproduce the approximate fence percentage. No skill text is changed in this phase. |
| 9. Skill history | Reproduced | Last main commit touching `skills/` is `3cf0e87`, 2026-06-13. |

## Validity changes before new scoring

`2026-11-13-validity-changes.json` retains the full before and after objects for every
changed active case, including assertions, expected outputs, dimensions, and prompts.
**Holdout cases were changed for validity before any new scoring.** Historical scores
cannot be compared directly to scores under these assertions. A missing fact can now
be handled by a precise question or a cut instead of an invented concrete detail.

The public tweet reference anchor was moved to the explicit open-book tune archive,
`evals/ablations/open-book-reference-anchors.json`. Its original artifacts and floor
remain intact. An independent synthetic practice-inbox input now tests transfer and
fidelity in the active holdout suite. Other copied examples were replaced with
independent synthetic inputs. The eight-word gate tolerates short technical terms and
common idioms while rejecting long copied spans, including case/punctuation variants.
It is a lexical contamination check, not a claim that public data are unseen in training.

## Skill examples to repair in Phase 5

The `Rewrite patterns` pairs in SKILL.md add unsupported step-4 retry/output retention,
a programmable network runtime, a WebSocket room/server claim, and the pelican project.
The decorative-antithesis example also asserts why the pelican is useful without source
facts. Give each pair licensing facts or an ask-author/cut repair. Keep this separate
from the measuring-instrument changes; no skill files were edited here.
