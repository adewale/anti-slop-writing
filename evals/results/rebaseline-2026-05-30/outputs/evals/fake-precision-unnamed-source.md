Verdict: ask-author

Slop tells: marketing-spec cadence ("delivers X% faster ... and reduces ... by approximately a third"). Two numbers, no provenance — one suspiciously precise (47%), one suspiciously round ("approximately a third"). The mix of false-precision and hand-wave is the tell: it sounds measured without committing to a measurement.

Specificity missing: every load-bearing fact. Faster on which page or route? Measured against which prior version or configuration? Under what traffic mix (cold cache vs. warm, logged-in vs. anonymous, p50 vs. p95 vs. p99)? Over what window and population? "Infrastructure costs" reduced from what to what, on which line items (egress, compute, cache tier itself), at what utilization? "Approximately a third" of which baseline — last month, last quarter, the pre-launch synthetic benchmark?

Inflated claim: the sentence implies a causal, generalizable improvement ("the caching layer delivers"). Without baseline and workload, the numbers cannot support that scope. At best they describe one measurement; at worst they describe a cherry-picked one.

Flow break: not applicable — single sentence.

Concrete rewrite: Ask author, in order: (1) Which page or route was measured? (2) What is the baseline — the previous build, a no-cache control, a different cache strategy? (3) Which percentile of load time improved by 47% — median, p95, p99 — and on which traffic population (cold, warm, logged-in)? (4) Is "approximately a third" cost reduction monthly infra spend on the affected service, or a projected annualized figure? Over what measurement window? (5) Is the comparison apples-to-apples (same traffic shape, same hardware)?

Fallback if those facts are not available: drop the precise numbers and state the effect at the resolution the evidence supports. For example: "On the product detail page, p95 load time dropped after we added the read-through cache; the cache tier also let us scale down two app servers." That keeps the claim survivable.

Fallback with the facts named (template): "On signed-out product pages, p95 load time fell from 1.9s to 1.0s after we added the Redis read-through cache (week-over-week, US traffic). Removing two app servers cut the service's monthly compute bill by about a third."

Rewrite check: passes self-detectors — no rule-of-three, no X-not-Y, no em-dash antithesis, no banned phrases, no decorative closer. The numbers in the template are placeholders to be filled by the author, not invented facts asserted as true; the questions to the author do the work.

Remembered line: a percentage without a baseline and a workload is a vibe, not a measurement.
