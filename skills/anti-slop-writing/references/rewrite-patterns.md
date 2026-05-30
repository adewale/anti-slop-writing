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
