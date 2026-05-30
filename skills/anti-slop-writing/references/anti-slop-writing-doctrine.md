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
Whether you're X or Y
While X, Y is also important
Despite ongoing challenges, X continues to thrive
Looking ahead, X will play an increasingly pivotal role
In conclusion
Overall
Ultimately
I hope this helps
```

## Copula displacement

AI prose often replaces plain `is/are` with `serves as`, `stands as`, `features`, `marks`, or `represents`. The verb sounds more substantial but only inflates a copula. Replace with plain `is` or with a specific action verb that names what the subject concretely does.

Keep the displaced verb when it does concrete work — enumeration, definition, or location:

```txt
The retry policy serves three distinct failure modes: connection timeout, oversized payload, and dependency outage.
```

`Serves` is doing the job of introducing an enumeration; replacing it with `is` would lose the enumeration. Flag the verb only when the sentence collapses to a plain copula with no concrete enumeration, definition, or location work.

## Hedged symmetry

Patterns such as `Whether you're a beginner or an expert`, `Whether X or Y, our framework helps`, and `While X is true, Y is also important` address every possible reader and every possible value at once. The symmetry sounds balanced but commits to nothing.

Replace by picking a specific reader and naming a concrete tradeoff. Keep the structure only when the symmetry names a real branching condition with distinct downstream behavior:

```txt
Whether the worker crashes before or after the receipt is written determines whether recovery retries the job or marks it complete.
```

The two branches trigger different concrete behavior, which earns the symmetry.

## Outline-shaped conclusions

Beyond the generic-thesis ending, two specific templates appear so often they qualify as outline shapes:

```txt
Despite ongoing challenges, X continues to thrive in an evolving landscape.
Looking ahead, X will play an increasingly pivotal role.
```

Neither names a specific challenge, a specific future move, or a concrete carrier. Cut both or return to a carrier from the body of the piece followed by a specific next step or claim.

## Em-dash cadence

Em-dashes are not slop on their own. Professional human writers use them. The failure pattern is the decorative cluster: five or six em-dashes in a paragraph, each acting as emphasis instead of bracketing a parenthetical or appositive.

Bad:

```txt
The system is fast — really fast — and reliable — at scale — with a clean API — that just works.
```

Good (one earned em-dash, defining a term inline):

```txt
The orphaned stream — the one where the original readable was lost but the chunks survived in SQLite — can still be finalized and persisted.
```

Reduce the count; keep dashes that bracket inline definitions or genuine asides.

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
serves as (as copula displacement)
stands as (as copula displacement)
```

The list is time-dated. Words enter and leave based on model behavior in a given generation. `delve` peaked in 2023-2024 LLM outputs and, by 2025 reporting, dropped off sharply; it stays on the list because older models and slower-drifting deployments still produce it, but the list itself should be re-profiled against a current human-vs-LLM corpus rather than maintained by taste. The Antislop research reported that some slop patterns appear over 1,000 times more frequently in LLM output than in human text; a frequency-based re-profile is more honest than vibes. (Do not invent a precise drop percentage for `delve`; the public reporting describes the decline qualitatively.)

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
