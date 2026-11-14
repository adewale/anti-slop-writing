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
7. Replace vague actors with named sources, named uncertainty, or an ask-author note; do not invent missing facts to fill a rewrite.
8. Collapse redundant bullets.
9. Vary sentence rhythm deliberately.
10. Audit paragraph flow: each paragraph should answer the prior question or make the next question necessary.
11. Prefer hypotaxis when the relation matters.
12. Check the conclusion: return to the concrete carrier, name what was made visible or solved, and state what transfers.
13. Replace displaced copulas with plain `is/are` or a specific action verb unless the verb enumerates, defines, or locates.
14. Cut hedged symmetry and commit to a specific reader/tradeoff unless the symmetry names a real branch.
15. Thin decorative em-dash clusters; keep dash insertions/pairs only when they bracket real asides or definitions.
16. End with a concrete remembered line.
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

## Parataxis and hypotaxis

Parataxis places clauses or sentences side by side and leaves the relation between them unstated: `I came, I saw, I conquered`; `The cache is warm. The query is slow.`; `We shipped the API. We wrote the docs. Adoption stalled.` Hypotaxis names the relation with subordination — `because`, `although`, `yet`, `once`, `where`, `so that`, `which means`.

Parataxis is a real device, not a defect. Keep it when:

- the sequence or speed is the point (`The pager fired. The dashboard went red. The on-call rolled back.`);
- both sides of a contrast are already evidenced by the surrounding prose (`What looked like perception was retrieval. What looked like a gift was inventory.`).

Repair two failure modes:

1. **Unstated relation.** A single juxtaposition where the relation is load-bearing but only implied. The reader has to guess whether the second clause is the cause, the contrast, or the consequence of the first.

   ```txt
   Before: The benchmark is saturated. The model still fails in production.
   After:  Although the benchmark is saturated, the model still fails in production, which means the benchmark no longer measures what ships.
   ```

2. **Density / over-reliance.** The same paratactic move is the dominant structural device — every section closing on a two-part contrast, or a chain of coordinate `and`s. Each instance may pass the staccato contrast test on its own, yet the piece as a whole leans on rhythm to imply relations it never argues. This is a document-level failure the per-sentence test misses. Convert most instances to hypotaxis and keep at most one earned paratactic line for effect.

The density check is not a new rule; it is the staccato contrast test's "keep or use once" applied across a whole piece, reinforced by the "symmetrical paragraph length, parallel structure" tell. Name it explicitly so a reviewer who has passed each closer individually still asks whether the piece leans on the same move four times.

Two cautions. Do not subordinate every clause into one connective-heavy sentence; that trades staccato slop for noun-heavy mush, and the reader loses the beats that made the prose readable. And do not apply the density check to a single earned instance: it is about the dominant device across the piece, not about any one short sentence.

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

Em-dashes are not slop on their own. Professional human writers use them. The failure pattern is the decorative cluster: several em-dash insertions in a paragraph, each acting as emphasis instead of bracketing a parenthetical or appositive.

Bad:

```txt
The system is fast — really fast — and reliable — at scale — with a clean API — that just works.
```

Good (one earned em-dash pair defining a term inline):

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
```

The list is time-dated. Words enter and leave based on model behavior in a given generation. `delve` peaked in 2023-2024 LLM outputs and, by 2025 reporting, dropped off sharply; it stays on the list because older models and slower-drifting deployments still produce it, but the list itself should be re-profiled against a current human-vs-LLM corpus rather than maintained by taste. The Antislop research reported that some slop patterns appear over 1,000 times more frequently in LLM output than in human text; a frequency-based re-profile is more honest than vibes. Do not invent a precise drop percentage for `delve`; the public reporting describes the decline qualitatively.

Copula constructions such as `serves as` and `stands as` are deliberately kept out of this words list. They are two-word templates whose verdict is context-dependent: keep when the verb does concrete enumeration, definition, or location work; replace when it only inflates a copula. Placing them in a flat words list would lose that context and risk over-flagging earned uses such as `The retry policy serves three distinct failure modes: ...`.

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
