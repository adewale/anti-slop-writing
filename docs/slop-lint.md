# Slop lint: spans for review, not verdicts

`evals/oracles/slop_lint.py` is repo-only triage tooling. Users still install only
`skills/anti-slop-writing/`. It returns character offsets, matched text and counts;
it never decides authorship, writing quality, or whether an earned construction must
go. A hit is a question for a contextual reviewer. No registry or blacklist was added
to the installed skill.

## Run

```bash
python3 evals/oracles/slop_lint.py evals/fixtures/slop-lint-triage/input.md
python3 evals/oracles/slop_lint.py review.md --rewrite-only
printf "Turns out the index was missing.\n" | python3 evals/oracles/slop_lint.py -
```

Exit 0 means the input was analyzed, **including when it contains hits**. There is no
`max_hits: 0` quality gate. Malformed rewrite scope exits 2 instead of returning a
misleading clean result. `--rewrite-only` requires exactly one `Concrete rewrite:`
field, stops at the next critique-format field, accepts a single enclosing code fence,
and reports offsets into the **original** document. Quoted critique, `Rewrite check`
and `Remembered line` are excluded. Missing, duplicate, empty and unclosed rewrite
blocks fail closed; arbitrary output formats are not guessed.

## Eight narrow detector examples

All examples below are synthetic. Facts in a before sentence are the available source;
an after must not invent a measurement or mechanism missing from it.

| Detector | Before / hit | Source-faithful response |
|---|---|---|
| Significance compression | “The checkpoint stores the last ID. That's the whole point.” | “The checkpoint stores the last ID.” |
| Therapy voice | “The job failed at step 4. Sit with that.” | “The job failed at step 4.” |
| Performative honesty | “Let's be honest: the migration failed.” | “The migration failed.” |
| Stage management | “Turns out the index was missing.” | “The index was missing.” |
| Sentence anaphora | “Maybe the alert failed. Maybe the owner slept. Maybe the link broke.” | Ask which hypothesis the incident evidence supports; do not turn one into a verified finding. |
| Stacked questions | “Did the alert fire? Did anyone respond?” | Ask for the alert and acknowledgment log; a pair of questions alone supplies neither event. |
| Negation chain | “No account, no install, no setup.” | Check those claims; do not replace them with an invented runtime or bundle size. An earned list may stay. |
| Stranded auxiliary | “The tool died; the data didn't.” | Ask whether the data remained readable or merely existed before choosing a more explicit sentence. With prior evidence the contrast may already be earned. |

**Earned-use counterexample:** “No allocations in the hot loop, no network calls in
the transaction, no writes before validation” still receives a shape hit. Each item
can express a distinct, testable constraint; the linter must not automatically reject
it. Similarly a trace-backed “turns out” can be correct. These are the boundaries the
historical highlighter branch's global zero-hit assertions failed to preserve.

## Provenance and limits

Pattern discovery was motivated by Simon Willison's
[LLM cliché highlighter](https://github.com/simonw/tools/blob/main/llm-cliche-highlighter.html)
(Apache-2.0) and the repo's historical
`claude/llm-cliche-highlighter-c2qqq8` work. This is a small independent implementation;
no upstream/branch source code or asset was copied. The historical 830-line registry,
its broad lists, runner adapter and automatic rewrite failures were **not imported**.
Any later code adaptation needs its own license/NOTICE review.

Offsets are Python Unicode character offsets, not UTF-8 byte offsets. Phrase matches
may appear in quotations or legitimate voice. Sentence splitting is deliberately
heuristic: abbreviations, dialogue and unusual punctuation can missegment; three
consecutive repeated starts are grouped into one maximal hit, and blank paragraphs
break that run. Absence of hits does not establish good prose or human authorship.
No detector count is substituted for the candidate studies' factual/task outcomes.

Tests use positive, negative and near-miss examples for every detector, check Unicode
span conservation, maximal runs, earned-use reporting and rewrite extraction. The
highlighter coverage study separately quarantines defective historical holdouts and
uses supplied-fact tune twins; its model results, not this deterministic tool, assess
whether the current skill performs a useful source-faithful rewrite.
