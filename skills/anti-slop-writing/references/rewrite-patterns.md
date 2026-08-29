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

## Rewrites must pass the same detectors as the source

A rewrite is also prose. The rule-of-three, X-not-Y cadence, em-dash antithesis, prestige adjective, and decorative closure are slop whether they appear in the source or in the fix. Run the same detectors on the rewrite before shipping it.

Common failure: an `ask-author` verdict is correct, but the fallback rewrite invents specifics or reuses the flagged cadence.

Weak (real example from a joe.dev review):

```txt
Verdict: ask-author
Concrete rewrite: Ask author: which person, talk, or project at
ATmosphere made the non-ad-platform character of the crowd legible?
Fallback: "At ATmosphere most of the hallway conversations were about
portability and moderation tooling, not growth loops or ad inventory."
```

The fallback invents what the conversations were about ("moderation tooling", "growth loops", "ad inventory") and uses X-not-Y cadence — the same cadence the source paragraph was flagged for.

Better:

```txt
Verdict: ask-author
Concrete rewrite: Ask author: which person, talk, or project at
ATmosphere made the non-ad-platform character of the crowd legible?
Fallback without that name: cut the "unusually authentic" paragraph;
the next paragraph already names the specific thing that makes the
community visible (PDS records, standard.site running on this site).
Rewrite check: passes self-detectors — no invented topics, no X-not-Y.
```

Common failure: a closing rewrite that decorates rather than carrying.

Weak:

```txt
Verdict: revise
Concrete rewrite: The whole stack — Hugo, standard.site, my PDS —
means the URL at the top of this page survives me losing interest
in any one of them. That was the point.
```

`That was the point` is an "In conclusion / Overall / Ultimately" decorative closer in disguise. The em-dash rule-of-three list is the same cadence pattern the doctrine flags in source prose.

Better:

```txt
Verdict: revise
Concrete rewrite: A standard.site post is just a record on a PDS, so
the URL at the top of this page keeps working if any one piece of the
stack — Hugo, the host, even standard.site itself — goes away.
Rewrite check: passes self-detectors — one em-dash aside is naming the
pieces, no rule-of-three closer, no decorative final sentence.
```

## Strip the new-register voice, keep the facts

The conversational register (significance compression, therapy voice, performative honesty, stage management, dev-blog boilerplate) usually decorates one or two real facts. The rewrite move is extraction: find the facts that survive when the cadence is cut, and let them open the passage. Do not invent replacements for what the cadence was hiding; use the skill's ask-author rule.

Bad:

```txt
Let's be real: most changelogs are noise. I won't sugarcoat it — the upgrade had rough edges. But here's the kicker: builds now finish in 90 seconds, down from six minutes. Turns out the cache key was wrong the whole time.
```

Better:

```txt
The upgrade cut build time from six minutes to 90 seconds. The cause was a wrong cache key. Ask author: what did the key hash before and after the fix? That one sentence would carry the piece.
```

Every fact in the rewrite comes from the source; the missing mechanism is requested, not invented. The candor opener and the staged reveals were padding around two numbers and a cause.

## Resolve structural cadence into findings

Anaphora runs, question stacks, and stranded-auxiliary reversals carry unresolved uncertainty as rhythm. In analytical prose (postmortems, design docs, reviews), the rewrite move is resolution: state what was checked and what the evidence showed. When the source supplies no evidence, resolution means naming the specific checks and their order — never inventing findings to fill the shape.

Bad:

```txt
Maybe the index was cold. Maybe the query planner changed. Maybe the traffic mix shifted. Do we know which? Do we even trust the dashboards? The graphs recovered; our confidence didn't.
```

Better:

```txt
The slowdown has three candidate causes: a cold index, a planner change, or a shifted traffic mix. The index stats and the plan diff are one query each; check those first and record which candidates the evidence eliminates. Until then the incident stays open, whatever the graphs show.
```

The speculation cadence becomes an ordered checklist with named evidence sources. Nothing is asserted that the source cannot support.

Keep the repetition only when it is doing enumeration work each item can defend — a changelog's "no breaking changes, no new dependencies", an invariant chain's "Every request… Every trace id…". The deterministic lint (`evals/oracles/slop_lint.py`, repo-only) flags the shape either way; the keep/cut verdict is judgment about whether each repeated item is independently checkable.

Note (2026-08-29): the first versions of these two examples reused the exact source passages of two tune eval cases and their rewrites invented specifics (counts, dates, mechanisms) not present in the sources. Both flaws were caught during the scored A/B run — the apply agent refused to copy the inventing rewrites, and the run note discounts the affected tune deltas. Worked examples in installable references must never reuse eval-case inputs, and a "Better" rewrite may only contain facts its own "Bad" source supplies.
