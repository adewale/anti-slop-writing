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

The paragraph is otherwise clean. It has no importance language, no `not X but
Y`, no em-dash cluster, no displaced copula, and its second sentence uses the
hypotaxis the doctrine prefers. That is what makes it a useful probe: any flag
has to come from the coinage.

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

Measured 2026-09-05 with apply/judge separation, Sonnet, baseline doctrine,
8 independent trials on this paragraph. Opus and Haiku flagged it on their
single baseline trials; Sonnet flagged it about half the time and otherwise
returned `keep`, once writing "the mechanism (exact-head checks run before each
merge)" — reading the coinage as the mechanism outright. Full run in
`evals/results/2026-09-05-astra-compound-labels/`.

## Does the rule generalize?

Tested on a second paragraph whose coinages (`soft-quorum drains`,
`tenant-affinity pools`) appear in neither doctrine, four trials per arm. The
baseline identified neither term as coined in any trial (0/4). The candidate did
in 2/4, and invoked the earned-side boundary on its own: "Neither is standard
shorthand the way `write-ahead log` or `copy-on-write` is." So the behavior
transfers to unseen coinages, but at roughly half the rate it shows when the
doctrine names the strings — which is the measure of how much the round-1
contamination inflated the result.

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

None shipped. A candidate `SKILL.md` edit — a coined-compound-label detector, an
editing-pass step, and a resolvability clause on false-positive restraint —
raised the Sonnet flag rate but did not clear `scripts/score_delta.py`. Rejected
and recorded in `evals/rejected-edits.md`.

Kept as regression coverage: `evals/evals.json` -> `coined-compound-label`, and
the two boundary guards `evals/adversarial.json` -> `earned-domain-compound`
(established compounds such as `write-ahead log` must not be flagged) and
`coined-label-defined-in-place` (a coinage defined in the same sentence is
earned).
