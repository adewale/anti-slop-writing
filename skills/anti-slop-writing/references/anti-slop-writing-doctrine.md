# Anti-Slop Writing Doctrine

## Core principle

> Sharp detail beats inflated significance.

AI writing fails when it loses specificity and compensates with importance language.

Bad direction:

```txt
less detail, more importance
```

Good direction:

```txt
more detail, earned importance
```

## Default editing pass

Before accepting generated prose:

```txt
1. Delete generic opening.
2. Find prestige vocabulary clusters.
3. Replace abstract nouns with concrete mechanisms.
4. Remove “not just X but Y” unless it is the exact point.
5. Cut superficial “highlighting/underscoring” clauses.
6. Check every claim of importance against evidence.
7. Replace vague actors with named sources or uncertainty.
8. Collapse redundant bullets.
9. Vary sentence rhythm deliberately.
10. Audit paragraph flow: each paragraph should answer the prior question or make the next question necessary.
11. Prefer hypotaxis when the relation matters.
12. Check the conclusion: return to the concrete carrier, name what was made visible or solved, and state what transfers.
13. End with a concrete remembered line.
```

## Flow-by-relation rule

Good prose can still fail if its paragraphs merely sit beside one another. A cleaner test:

> Flow improves when each paragraph makes the next question possible.

At section boundaries, name the relation rather than relying on order or rhythm:

- cause: `Because X, Y becomes possible.`
- contrast: `Although X does not solve the problem, it makes the gap visible.`
- dependency: `Without X, Y cannot be inspected.`
- level change: `The same run can be inspected at three resolutions: aggregate trajectory, lineage, and source diff.`
- carrier-to-claim: `Because the concrete example is small and memorable, it can carry the larger claim.`

A conclusion should return to the concrete carrier and then state the transferable structure. A final thesis sentence is weaker when it could belong to any essay in the category.

## Banned-by-default phrases

Avoid unless there is a specific reason:

```txt
In today's rapidly evolving landscape
In the realm of
When it comes to
At its core
Let's dive into
It's worth noting that
It's important to note that
A testament to
Not just X, but Y
This is where X comes in
In conclusion
Overall
Ultimately
I hope this helps
```

## High-risk words

Review these whenever they appear:

```txt
delve
realm
landscape as metaphor
tapestry
testament
pivotal
crucial
underscore
intricate
meticulous
multifaceted
nuanced as filler
foster
bolster
garner
showcase
highlight
emphasize
encompass
utilize
facilitate
transformative
groundbreaking
seamless
robust outside engineering context
```

## Better replacements

Do not mechanically replace words. Replace the thought.

Instead of:

```txt
This underscores the importance of durable execution.
```

Write:

```txt
The workflow can fail on step 4, retry only that step, and keep the previous outputs.
```

Instead of:

```txt
Cloudflare is not just a CDN, but a platform.
```

Write:

```txt
Cloudflare turns the network boundary into a programmable runtime.
```

Instead of:

```txt
This empowers teams to build seamless experiences.
```

Write:

```txt
The team can ship a WebSocket room without running a room server.
```

Instead of ending with a generic thesis:

```txt
A benchmark is stronger when you can inspect the run that produced it.
```

Write a carrier-bound conclusion:

```txt
Because the pelican project is small enough to inspect and strange enough to remember, it works as a compact carrier for the larger claim: a benchmark is stronger when you can inspect the run that produced it.
```
