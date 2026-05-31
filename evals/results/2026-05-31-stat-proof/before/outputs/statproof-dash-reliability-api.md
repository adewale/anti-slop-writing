Verdict: revise
Slop tells: The repeated em-dashes form a cadence cluster: “reliable — really reliable — under load — even during spikes — with clean errors — and fast retries.” The punctuation is doing the emphasis work.
Specificity missing: Reliability needs measurements: uptime window, p95/p99 latency under load, spike size, error shape, retry policy, and failure behavior.
Inflated claim: “Really reliable” and “developers can trust” are praise labels unless tied to evidence.
Flow break: The sentence lists claims at equal weight instead of showing which fact proves reliability.
Concrete rewrite: “Under a 10k-request-per-minute spike, the API keeps p99 latency under 300 ms, returns typed error codes, and retries idempotent requests with exponential backoff.” If those numbers are not available, ask for them before making the claim.
Remembered line: Dashes are not banned; an earned dash can hold a concrete aside, but this cluster should become evidence.