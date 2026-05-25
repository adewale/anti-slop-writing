# Failure: Product-tour flow

## Original

```txt
The Climb ranks the models.

Head-to-Head is a filmstrip viewer.

Runbook Diffs compares versions.
```

## Why it failed

Each sentence is locally clear, but the sequence reads like a product tour. The reader sees three features, not the relation among them.

## Mechanism

Adjacent paragraphs sit beside each other without a level-of-detail hinge.

## Better rewrite

```txt
The site exposes the run at three resolutions. The Climb shows the aggregate trajectory, Head-to-Head shows round-by-round lineage, and Runbook Diffs drops to the source level where the prompt and seed SVG changed.
```

## Rule added or changed

At section boundaries, name the relation: level of detail, dependency, cause, contrast, or scope change.
