# Flow by Relation

## Rule

Paragraphs should not merely sit beside one another in plausible order. Each paragraph should answer the prior question or make the next question necessary.

> Flow improves when each paragraph makes the next question possible.

## Common relations

Use sentence machinery to name the relation:

| Relation | Useful forms |
|---|---|
| Cause | `Because X, Y.` |
| Contrast | `Although X, Y.` |
| Dependency | `Without X, Y cannot happen.` |
| Time / state change | `Once X is visible, Y becomes inspectable.` |
| Scope change | `At that level, Y changes from A into B.` |
| Level of detail | `The same object appears at three resolutions: A, B, and C.` |
| Carrier-to-claim | `Because this example is small and memorable, it can carry the larger claim.` |

## Diagnosis

A section needs a hinge when:

- headings do all the organizing work;
- each paragraph is locally clear but the sequence feels like a list;
- the piece jumps from example to general claim without naming what transfers;
- the conclusion states the thesis but does not return to the concrete object;
- the reader can understand every paragraph but cannot predict why the next one follows.

## Repair pattern

1. Name the level or relation that connects the next section.
2. Add one hinge sentence before the list or section shift.
3. Make the hinge factual rather than grand.
4. Prefer “because,” “although,” “without,” “once,” “where,” and “at that level” over decorative contrast.

## Example

Weak transition:

```txt
The Climb ranks the models. Head-to-Head is a filmstrip viewer. Runbook Diffs compares versions.
```

Better transition:

```txt
The site exposes the run at three resolutions. The Climb shows the aggregate trajectory, Head-to-Head shows round-by-round lineage, and Runbook Diffs drops to the source level where the prompt and seed SVG changed.
```

## Conclusion pattern

A conclusion should usually do four jobs:

1. return to the concrete carrier;
2. admit the limit or scope;
3. state the reusable structure;
4. end with the transferable claim.

Weak ending:

```txt
A benchmark is stronger when you can inspect the run that produced it.
```

Better ending:

```txt
Because the pelican project is small enough to inspect and strange enough to remember, it works as a compact carrier for the larger claim: a benchmark is stronger when you can inspect the run that produced it.
```
