## P1

Verdict: ask-author

Slop tells: "exact-head checks" is a coined compound term used with full technical confidence but never operationalized. This matches the rhetorical-style-drift pattern of a noun-heavy abstraction carrying informational density without mechanism: the term sounds precise (it names a location — "head" — and asserts a rigor — "exact") but the paragraph never shows what is actually compared. Applying the emphasis-source test by flattening the line ("The indexer checks something before merging, which keeps layouts consistent; because the check happens early, problems appear at merge time instead of later") shows the timing/consequence claim survives intact, but the word "exact" adds nothing that survives the flattening — it was doing rhetorical work, not descriptive work.

Specificity missing: What does the check actually compare to decide a match — a hash of the head revision, a byte-for-byte diff, a row count, a timestamp? What concretely is "the head" (a commit/revision pointer, or something else)? Applying false-positive restraint: the second sentence does earn part of the term — it confirms the check genuinely runs "at the head" and gives a real boundary (drift surfaces at merge time, not read time). So the "head" and the timing claim are supported. Only the "exact" half — the comparison method itself — is unsupported by anything in the paragraph.

Inflated claim: Not an importance-inflation (no "crucial," "seamless," etc.) — it's a narrower precision-inflation: "exact" implies a rigorous, well-defined comparison that the paragraph never demonstrates.

Flow break: None. The two sentences connect cleanly via "because," and the causal relation (check timing → detection timing) is properly hypotactic, not a list-like juxtaposition.

Concrete rewrite: Ask author: what does the exact-head check actually compare to determine a match — a hash of the head revision, a byte-for-byte diff, or something else? Fallback if that detail isn't available: drop the unearned "exact" and describe only what's supported — "The indexer runs a head check before each merge, so editorial-row layouts stay consistent across shards." If the author later confirms the comparison method, the stronger fix is to define the term where it's coined, on the pattern this same source uses elsewhere: "We call this a head check: the indexer [compares/hashes] X on both replicas and refuses the merge when they differ" — filled in only once the mechanism is confirmed, not invented here.

Rewrite check: The ask-author question and the cut-fallback contain no rule-of-three, no X-not-Y / negative parallelism, no em-dash antithesis, no banned avoid-by-default phrases, no prestige adjectives, and no decorative closure. The cut-fallback removes the unsupported "exact" rather than replacing it with an invented mechanism; the pattern-fallback explicitly withholds filling in "hashes" or any other specific verb until the author confirms it, so no fact is invented. Passes self-detectors.

Remembered line: None yet. The paragraph's one distinctive image — "exact-head check" — is currently hollow, so nothing concrete survives once the label is set aside. Supplying the actual comparison method (per the ask-author question) is what would give this paragraph a remembered line.

## P2

Verdict: keep

Slop tells: None. No banned phrases, no importance-inflation words, no copula displacement, no hedged symmetry, no em-dash cadence, no rule-of-three, no X-not-Y / negative parallelism.

Specificity missing: None. "Write-ahead log" and "copy-on-write snapshots" are established, externally-defined technical terms — not labels coined for this paragraph — so the reader isn't being asked to accept a private definition on faith. The paragraph also goes beyond naming the mechanisms: it specifies a precise failure window (a crash between the enqueue and the fsync) and a precise recovery behavior (replay from the last checkpoint), which is exactly the "sharp detail" the doctrine asks for rather than a claim resting on the compound terms alone.

Inflated claim: None. The claim is narrow and falsifiable (one failure scenario, one recovery behavior) rather than a general assertion of quality — nothing like "robust" or "reliable" is asserted that would need separate earning.

Flow break: None. Single sentence, clean hypotaxis via "so": mechanism (WAL + copy-on-write snapshots) leads directly to a named, bounded effect (in-window crash replays from checkpoint instead of dropping the job).

Concrete rewrite: Not needed.

Rewrite check: N/A — no rewrite offered.

Remembered line: "a crash between the enqueue and the fsync replays from the last checkpoint instead of dropping the job" — specific enough that a reader could design a test for it.

## P3

Verdict: keep

Slop tells: None. The paragraph coins a term and defines it in the same breath, which is the inverse of a slop tell — it's the doctrine's own recommended move (name the mechanism, then supply the mechanism) rather than a label left to float.

Specificity missing: None. The definition names the actor (the indexer), the action (hashes the head revision on both replicas), and the boundary condition (refuses the merge when they differ) — this is the exact level of mechanism the doctrine's core principle asks for ("sharp detail beats inflated significance").

Inflated claim: None.

Flow break: None. One sentence; the colon introduces a real definition rather than functioning as decorative or fake structure — content follows it, not a rhythmic pause.

Concrete rewrite: Not needed.

Rewrite check: N/A — no rewrite offered.

Remembered line: "the indexer hashes the head revision on both replicas and refuses the merge when they differ" — concrete and falsifiable, and it doubles as the paragraph's own definition of the term it coins.
