# Failure: Borrowed emphasis

## Original

```txt
Durable execution isn't just retry logic. It is a new programming model.
```

## Why it failed

The emphasis comes from the "isn't just X. It is Y" cadence, not from the idea. Flatten the rhythm — "Durable execution is a new programming model" — and nothing concrete is left. The sentence promises a distinction it does not deliver: no actor, no mechanism, no limit. The prior doctrine flagged the banned phrase pattern but did not locate the source of the emphasis, so a rewrite could remove the rhythm and still leave a hollow claim.

## Mechanism

Borrowed-pattern emphasis. The contrast cadence carries the authority while the idea stays generic. The syntax suggests a relation (retry-logic-versus-programming-model) without clarifying it.

## Better rewrite

```txt
Durable execution lets a workflow fail on step 4, retry only that step, and keep the previous outputs, so the programmer writes against a runtime that records state instead of a function that returns once.
```

## Rule added or changed

Added two detectors to `SKILL.md`:

- Emphasis-source test: flatten the cadence in your head; if the line collapses, the rhythm was carrying it.
- Syntax-relation test: ask whether the syntax clarifies the relation or only suggests one.

Paired with an adversarial counter-case so the rule does not flag antithesis whose two halves carry distinct information.
