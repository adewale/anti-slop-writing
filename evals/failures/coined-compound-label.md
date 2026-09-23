# Failure: Coined compound label

## Original

```txt
The indexer runs exact-head checks before each merge, so editorial-row layouts
stay consistent across shards. Because the check happens at the head, drift
between replicas surfaces during the merge rather than at read time.
```

## Why it failed

`exact-head checks` and `editorial-row layouts` are coined. Neither is standard
in the domain, and the paragraph never defines either one. The hyphens supply
the texture of precision while the referent stays out of reach: the reader
cannot look the terms up and cannot find them defined, so the consistency claim
rests on a name rather than on a mechanism.

The paragraph is otherwise nearly clean. It has no importance language, no
`not X but Y`, no em-dash cluster, no displaced copula, and its second sentence
uses the hypotaxis the doctrine prefers. Its one other weak point is the
closing "rather than at read time": nothing shows what read time would have
looked like. One baseline critique flagged that and kept both coined labels.
So a flag alone does not show the coinage was caught, which is why the case's
assertions check for the coinage directly. The holdout version,
`holdout-coined-compound-label`, has no such contrast.

## Mechanism

A coined compound label is shaped like a mechanism name, so it satisfies the
existing tests at the level of surface form. Two rules can launder it:

- **Emphasis-source test.** Flattening the line leaves "the indexer checks
  something before each merge, so things stay consistent." The residual claim
  appears to name an actor and a mechanism, so the test reads as passed.
- **False-positive restraint.** The rule says to keep a flagged term when the
  same sentence supplies the mechanism that earns it. A coined label supplies
  something mechanism-shaped, so restraint fires and returns `keep`.

The gap is not a missing word on a list. It is that neither rule asks whether
the supporting term is itself resolvable. A name that refers to nothing can
satisfy both.

## Observed rate

Graded blind against this case's assertions, on the valid trials of the
2026-09-05 round: the Claude Sonnet 5 baseline named the coinage in 2 of 4
trials, with a mean case score of 0.50. When it missed, it returned `keep`, once
writing "the mechanism (exact-head checks run before each merge)", which reads
the coinage as the mechanism outright. Claude Opus 5 passed every assertion in
its one trial. Claude Haiku 4.5 named the coinage and then invented a definition
for it. Full record in `evals/results/2026-09-05-astra-compound-labels/regrade/`.

Four trials cannot say whether the candidate rule helps. The earlier claim that
it transfers to unseen coinages came from a hand check that counted the
candidate doctrine's own vocabulary. Graded blind, that probe is 2 of 4 against
3 of 4.

## Better critique

Name the coinage, say the referent is unavailable, and ask the author rather
than inventing a definition:

```txt
Verdict: ask-author
Slop tells: "exact-head checks" and "editorial-row layouts" are coined and never
defined; the hyphen is doing the work a definition should do.
Concrete rewrite: Ask author — what does the check compare, and by what
operation? What is an editorial-row layout? Fallback if unavailable: "The
indexer runs its check before each merge, so drift between replicas surfaces at
merge time instead of at read time." This drops the layout-consistency claim
rather than guessing at a definition.
```

## Rule added or changed

None yet. The candidate `SKILL.md` edit adds a coined-compound-label detector,
an editing-pass step, and a resolvability clause on false-positive restraint.
It has not been adequately tested, so it is neither shipped nor in
`evals/rejected-edits.md`. A pre-registered test is ready in
`evals/results/2026-09-23-coined-label-rerun/`.

Regression coverage: `evals/evals.json` -> `coined-compound-label` (tune) and
`holdout-coined-compound-label` (holdout, fresh coinages), and the boundary
guards in `evals/adversarial.json`: `earned-domain-compound` and
`holdout-earned-domain-compound` (standard compounds must not be flagged), and
`coined-label-defined-in-place` and `holdout-coined-label-defined-in-place` (a
coinage defined where it is introduced is earned).
