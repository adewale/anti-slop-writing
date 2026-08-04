# Failure: Hollow modifier with a false implicature

Source: [@stanine, 2026-08-03](https://x.com/stanine/status/2084385000959701146).

## Original

```txt
My actual recommendation is to ship the migration behind a flag. The real reason is that the backfill takes eleven hours and cannot be paused once it starts.
```

## Why it failed

`actual` and `real` say nothing about the recommendation or the reason. Deleting them leaves the meaning unchanged, which is the test. What they add is an implication: that an earlier recommendation was offered and was not the genuine one, that an earlier reason was given and was false. Nothing precedes the paragraph, so the alternatives the modifiers point at do not exist.

This is not the failure the existing detectors are built for. Prestige adjectives (`crucial`, `pivotal`, `transformative`) inflate the thing being described, and the repair is to name the mechanism. A hollow modifier makes no claim about its noun at all; it makes a claim about a set of alternatives the reader was never shown. The mechanism tests do not fire, because the sentence around the modifier is already concrete — eleven hours, no pause once started.

The repair also runs the other way from the usual one. The default editing pass replaces abstraction with mechanism, which adds words. Here the correct edit is deletion, and a rewrite that grows to justify the modifier has made the line worse.

## Mechanism

An emphasis modifier that carries no information about its noun asserts a contrast with unnamed alternatives. When those alternatives were never given, the assertion is false.

## Better rewrite

```txt
My recommendation is to ship the migration behind a flag. The backfill takes eleven hours and cannot be paused once it starts.
```

## Boundary

`actual` is earned when a competing figure was given: after a paragraph quoting a vendor's advertised p99 of 40 ms, `The actual p99 during the incident was 2.3 seconds` needs the word. `key` is earned when it ranks among alternatives the reader was actually shown and the criterion is stated: `We found three regressions ... The key issue is the lock; the other two do not change throughput.`

## Eval coverage

- `evals/evals.json` -> `hollow-modifier-false-implicature` (tune)
- `evals/rewrite-evals.json` -> `hollow-modifier-delete-not-expand` (tune)
- `evals/adversarial.json` -> `substantive-actual-measured-vs-advertised` (tune), `key-issue-earned-by-stated-ranking` (holdout)

## Rule added or changed

None yet. The cases are coverage for an untested hypothesis; see `TODO.md` for the A/B that decides whether doctrine is needed.
