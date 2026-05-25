# Rewrite Patterns

## Replace importance with mechanism

Weak:

```txt
This underscores the importance of durable execution.
```

Better:

```txt
The workflow can fail on step 4, retry only that step, and keep the previous outputs.
```

## Replace generic contrast with relation

Weak:

```txt
The point is not the pelicans. The point is the process.
```

Better:

```txt
The pelican is useful because it gives the process a small, inspectable carrier.
```

## Replace thesis-only ending with carrier-bound conclusion

Weak:

```txt
A benchmark is stronger when you can inspect the run that produced it.
```

Better:

```txt
Because the pelican project is small enough to inspect and strange enough to remember, it works as a compact carrier for the larger claim: a benchmark is stronger when you can inspect the run that produced it.
```

## Add section hinges

Weak:

```txt
The Climb ranks the models.

Head-to-Head is a filmstrip viewer.

Runbook Diffs compares versions.
```

Better:

```txt
The site exposes the run at three resolutions. The Climb shows the aggregate trajectory, Head-to-Head shows round-by-round lineage, and Runbook Diffs drops to the source level where the prompt and seed SVG changed.
```

## Preserve earned compression

Some short lines work because the mechanism has already been established. Keep them when they name the relation precisely.

Good:

```txt
The pelican is the surface; the inspectable run is the point.
```

Why it works: the prior argument has already established the distinction between the memorable carrier and the reusable structure.
