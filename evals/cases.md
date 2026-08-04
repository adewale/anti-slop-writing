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
- Distinguishes from `Whether X or Y` that names a real branching condition, such as crash-before vs crash-after.
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
- Rewrites by reducing the dash count and keeping at most one earned dash insertion or pair.

## Case 10 — fresh holdout: combined detector paragraph

Input:

```txt
The analytics console serves as a unified hub for operational excellence. Whether you're a startup founder or an enterprise leader, it scales with your needs. Despite ongoing challenges in the data landscape, the platform continues to thrive. Looking ahead, it will play an increasingly pivotal role in decision-making.
```

Expected critique:

- Separately identifies copula displacement, hedged symmetry, and outline-shaped conclusion templates.
- Chooses a specific user/use case or recommends cutting unsupported sentences.
- Rewrites with concrete behavior the console performs, not another all-purpose product claim.

## Case 11 — hollow modifier with a false implicature

Input, as the opening of a design doc with nothing before it:

```txt
My actual recommendation is to ship the migration behind a flag. The real reason is that the backfill takes eleven hours and cannot be paused once it starts.
```

Expected critique:

- Applies the deletion test: `actual` and `real` can go without changing what the sentences say.
- Names what the modifiers falsely imply — that an earlier recommendation or reason was given and was not the genuine one.
- Does not excuse them because the sentence around them is already concrete (eleven hours, no pause).
- Repairs by deleting, not by swapping in another adjective or adding a clause. The line should get shorter.

Boundary: keep `actual` when a competing figure was given — after a vendor's advertised p99 of 40 ms, `The actual p99 during the incident was 2.3 seconds` needs the word.

## Case 12 — self-planted strawman contrast

Input, where the user's entire message was `why is the deploy slow?` and they never mentioned Docker:

```txt
It would be easy to assume the slowness comes from the Docker build. But the build is not the problem. The problem is that the readiness probe waits a fixed 30 seconds before its first check, so every rollout pays that delay once per pod.
```

Expected critique:

- Flags the Docker-build hypothesis as an alternative the writer introduced and then refuted, which no one raised.
- Does not grade the contrast as earned antithesis just because the writer's own prior sentence supplies the Docker side.
- Rewrites to state the readiness-probe finding directly, with no replacement negation.

Boundary: when the user asks `is this a memory leak?`, `This is not a memory leak` is a required correction, not an invented contrast.
