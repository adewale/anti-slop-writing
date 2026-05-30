# Rejected edits

This file is the graveyard of doctrine edits that failed an eval before being merged. One entry per rejection. The point is to stop relitigating the same failed move in a future round.

`Lessons_learned.md` records durable "what not to overgeneralize" lessons that survived. This file records the per-attempt rejects that did not. See `docs/hillclimb-improvements.md` (item 10) for the rationale, including SkillOpt's rejected-edit buffer ([arXiv 2605.23904](https://arxiv.org/abs/2605.23904)).

## Entry format

```
## YYYY-MM-DD — short label

### Edit attempted
The smallest description of the doctrine change.

### Eval that rejected it
The case id and suite (`evals/<file>.json` -> `<id>`), plus the holdout/tune split.

### Why it was rejected
Quoted evidence from the failing case.

### Lesson (if any)
Optional. Only fill in if the rejection generalizes. Otherwise leave blank and let the entry stand as a graveyard marker.
```

## Entries

_None yet. The first rejected edit from a hillclimb round goes here._
