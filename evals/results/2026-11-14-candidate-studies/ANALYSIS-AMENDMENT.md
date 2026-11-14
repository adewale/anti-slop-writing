# Analysis export amendment 1 — explicit guards and standing decreases

Before the first numerical analysis, materialize every standing case/model/judge/
candidate decrease in `standing-regressions.json`, instead of requiring readers to
reconstruct them from absolute case scores. Include both co-primary dimensions and
the secondary rewrite-quality dimension already elicited in the uniform judge rubric.
All original absolute scores remain available.

Extract the existing fact-condition point-guard calculation into a tested helper and
require both unsupported-claim and rewrite-quality outcomes exactly once per eligible
contrast. Missing/duplicate outcomes must fail instead of silently producing an
incomplete guard report. Test the inclusive ±.05 boundaries and just-outside near misses.
The existing quality and unsupported-claim calculations and thresholds are unchanged;
no measure is missing and no primary outcome is being used as a proxy.

This is an **analysis-code/export amendment after model scoring started**, committed
before the first numerical analysis, not an unamended confirmatory protocol. The
original generation-source hashes remain; `analysis-sources.json` records the actual
analysis implementation. Cases, allocation, packages, prompts, models, effort, all
rubric dimensions, aggregation, SESOI, statistical gates and no-promotion decision are
unchanged. No responses are regenerated and no extra model calls are introduced.
The amendment arose from code inspection, not numerical outcome selection. The public
screen remains underpowered; no result can turn it into a promotion study.
