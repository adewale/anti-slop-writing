# Pelican conclusion before/after

This example records the failure that added the conclusion rule: a true final sentence can still fail when it leaves the concrete carrier behind.

## Weak ending

```txt
The reusable structure is small and concrete:

- the runbook is source;
- the generated SVG is the build artifact;
- the lineage is the build history;
- the diff is the review surface;
- the judge identity is part of the measurement.

A benchmark is stronger when you can inspect the run that produced it.
```

## Problem

The final sentence is true, but generic. It could end many essays about evaluation observability. It does not return to the pelican as the concrete carrier, so the reader loses the small, inspectable object that made the claim memorable.

## Better ending

```txt
The reusable structure is small and concrete:

- the runbook is source;
- the generated SVG is the build artifact;
- the lineage is the build history;
- the diff is the review surface;
- the judge identity is part of the measurement.

Because the pelican project is small enough to inspect and strange enough to remember, it works as a compact carrier for the larger claim: a benchmark is stronger when you can inspect the run that produced it.
```

## Lesson

The better ending uses hypotaxis to bind the concrete carrier to the transferable claim:

```txt
Because [concrete carrier has useful properties], it can carry [larger claim].
```

A conclusion should do more than restate the thesis. It should show why this example was the right vehicle for the thesis.
