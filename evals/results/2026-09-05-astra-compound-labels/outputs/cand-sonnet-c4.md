## P1

Verdict: ask-author

Slop tells: Coined compound labels, two instances, neither defined. "Exact-head checks" names a check; "editorial-row layouts" names an artifact. Per the doctrine: "The hyphen supplies the texture of precision while the referent stays out of reach." The second sentence ("Because the check happens at the head...") confirms only *where* the check runs, not *what* "exact" compares or *how* a match/mismatch is determined — so "exact-head" gets a partial gesture but no real cash-out. "Editorial-row layouts" gets zero support anywhere in the paragraph: nothing says what makes a row "editorial," or what "layout" means in this context (a schema? a rendering order? a file format?).

Specificity missing: What does the check actually compare to be "exact" — a hash of the head revision, a timestamp, byte-for-byte content? What is an "editorial-row," and what does "layout" refer to (row order, row schema, row rendering)? Secondary note: sentence 1 says consistency holds "across shards," sentence 2 says drift appears "between replicas" — if shards and replicas are the same referent here, the paragraph should use one term; if they're different scopes (e.g., a shard containing multiple replicas), the paragraph is silently switching what's being compared.

Inflated claim: None of the classic significance-inflation vocabulary is present, but the two compounds function the same way: "exact" and "editorial" assert a precision and a domain-specificity the passage doesn't back up.

Flow break: None. The two sentences are causally linked ("Because the check happens at the head, drift... surfaces during the merge") — that's earned hypotaxis, not a list. The flow itself isn't the problem; the undefined nouns it's carrying are.

Concrete rewrite: Ask author: What does the exact-head check actually compare — a hash of the head revision, a version/timestamp field, or full content? And what is an "editorial-row layout" — a row schema in a specific table, a rendering order, something else? Fallback, without inventing the mechanism: "The indexer verifies that shards agree at the head before each merge, so rows stay consistent across them." This keeps the causal claim and drops "exact" and "editorial-row" down to what the paragraph actually supports (agreement at the head; rows stay consistent), rather than asserting an unconfirmed comparison method.

Rewrite check: The fallback contains no rule-of-three, no X-not-Y, no em-dash antithesis, no avoid-by-default phrases, no prestige adjectives, no decorative closure, and no invented facts — it deliberately declines to guess the comparison mechanism rather than fabricate one. Passes self-detectors.

Remembered line: Not yet available. The paragraph's only potentially memorable content — what "exact" and "editorial-row" actually mean — is exactly what's missing. Once the author supplies the comparison mechanism, that mechanism is the line worth keeping.

## P2

Verdict: keep

Slop tells: None. "Write-ahead log" and "copy-on-write" are standard domain terms — the doctrine names both explicitly as the exception to the coined-compound-label tell: "Keep the coinage... when the term is standard in the domain ('write-ahead log,' 'copy-on-write')." These aren't the passage's invention; they're load-bearing, looked-up-able terms of art, so the hyphens aren't doing any borrowed-precision work here.

Specificity missing: None. The paragraph names the exact failure window ("a crash between the enqueue and the fsync"), the recovery action ("replays from the last checkpoint"), and the specific outcome avoided ("instead of dropping the job"). That's a real mechanism, not a label standing in for one.

Inflated claim: None.

Flow break: None. One sentence, clean cause-and-effect hypotaxis ("so a crash... replays... instead of dropping the job").

Concrete rewrite: Not needed.

Rewrite check: N/A — no rewrite produced, so there is nothing to self-check for reused cadence or invented facts.

Remembered line: "a crash between the enqueue and the fsync replays from the last checkpoint instead of dropping the job" — already concrete and specific; nothing to strengthen.

## P3

Verdict: keep

Slop tells: None. "Exact-head check" is a coined term, but it's defined in the same sentence via the colon: "the indexer hashes the head revision on both replicas and refuses the merge when they differ." This is the doctrine's stated exception in direct application: "Keep the coinage when the passage defines it in place." There's no gap between the name and the referent — the definition arrives immediately, in the same breath as the coinage.

Specificity missing: None. The definition names the actor (the indexer), the exact mechanism (hashes the head revision), the scope (both replicas), and the consequence (refuses the merge when they differ) — all four of what/who/where/then are answered.

Inflated claim: None.

Flow break: None. Single sentence; naming and definition are adjacent, so there's no room for a gap to open between them.

Concrete rewrite: Not needed.

Rewrite check: N/A — no rewrite produced.

Remembered line: "the indexer hashes the head revision on both replicas and refuses the merge when they differ" — this is what "exact-head check" cashes out to, and it's the part worth remembering.
