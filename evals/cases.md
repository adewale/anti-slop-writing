# Manual eval cases

Use these cases when hillclimbing the skill. A good answer should identify the failure mechanism and produce a concrete rewrite.

The runnable source of truth is `evals/evals.json`; keep this file aligned as the human-readable explanation of those cases.

## Case 1 — generic importance

Input:

```txt
This underscores the importance of durable execution in modern software systems.
```

Expected critique:

- Flags `underscores the importance`.
- Asks what mechanism makes execution durable.
- Rewrites with a concrete failure/retry/receipt mechanism.

## Case 2 — decorative contrast

Input:

```txt
The point is not the pelicans. The point is the process.
```

Expected critique:

- Does not ban contrast automatically.
- Flags that the relation is implied rather than explained.
- Rewrites by naming how the pelican carries or exposes the process.

## Case 3 — weak conclusion

Input:

```txt
The reusable structure is small and concrete: the runbook is source, the generated SVG is the build artifact, the lineage is the build history, the diff is the review surface, and the judge identity is part of the measurement.

A benchmark is stronger when you can inspect the run that produced it.
```

Expected critique:

- Says the ending is accurate but generic.
- Notes that it does not return to the concrete carrier.
- Produces a carrier-bound conclusion using a relation such as `Because the pelican project is small enough to inspect and strange enough to remember...`.

## Case 4 — product-tour flow

Input:

```txt
The Climb ranks the models.

Head-to-Head is a filmstrip viewer.

Runbook Diffs compares versions.
```

Expected critique:

- Says the sequence reads like a list/product tour.
- Adds a hinge that names the level-of-detail relation.
- Rewrites around aggregate trajectory, round-by-round lineage, and source-level change.

## Case 5 — safe essay voice

Input:

```txt
In today's rapidly evolving landscape, teams need robust solutions that empower developers to build seamless experiences.
```

Expected critique:

- Flags banned/default slop phrases and vague actors.
- Asks what team, what solution, what action, what result.
- Rewrites with a concrete capability or cuts the sentence.

## Case 6 — copula displacement

Input:

```txt
The dashboard serves as the central hub for user activity and stands as a testament to the platform's capabilities.
```

Expected critique:

- Flags `serves as` and `stands as a testament` as copula displacement plus prestige inflation.
- Distinguishes from legitimate `serves` that introduces a concrete enumeration.
- Rewrites with plain `is` or a specific action verb naming what the dashboard concretely shows or does.

## Case 7 — hedged symmetry

Input:

```txt
Whether you're a beginner or an expert, our framework scales to your needs. While simplicity matters, power is also important.
```

Expected critique:

- Flags `Whether you're X or Y` and `While X, Y is also important` as hedged symmetry that refuses to commit.
- Distinguishes from `Whether X or Y` that names a real branching condition (such as crash-before vs crash-after).
- Rewrites by picking a specific reader and naming the concrete tradeoff between simplicity and power.

## Case 8 — outline-shaped conclusion

Input:

```txt
Despite ongoing challenges, the team continues to thrive in an evolving landscape. Looking ahead, the platform will play an increasingly pivotal role in the AI ecosystem.
```

Expected critique:

- Flags the two template shapes as outline conclusions, not earned closings.
- Notes that no specific challenge, future move, or concrete carrier is named.
- Either recommends cutting both sentences or rewrites to return to a concrete carrier plus a specific next step.

## Case 9 — em-dash cluster

Input:

```txt
The system is fast — really fast — and reliable — at scale — with a clean API — and a great developer experience — that just works.
```

Expected critique:

- Flags the cluster as decorative cadence-for-emphasis, not earned parenthetical insertion.
- Does not claim em-dashes are always slop; names the failure as the cluster.
- Rewrites by reducing the dash count and keeping at most one earned parenthetical or appositive.
