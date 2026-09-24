## Trial 5

Verdict: ask-author

Slop tells: Coined compound labels — "exact-head checks" and "editorial-row layouts" are both hyphenated noun phrases that name a process and an artifact the paragraph never defines. These are the same two example terms the doctrine itself uses to illustrate the pattern, which is a strong signal this passage sits squarely in the failure mode rather than near its edge.

Specificity missing: For "exact-head checks," the second sentence supplies only *where* the check runs ("at the head") and *what its timing buys* (catching drift at merge instead of at read time) — it never says *what is compared* to decide two heads match: a content hash, a revision counter, a byte-for-byte diff. For "editorial-row layouts," there is no supporting clause anywhere in the paragraph: not what makes a row "editorial," not what "layout" refers to (schema, column order, rendering), and no return to the term after sentence 1.

Inflated claim: "stay consistent across shards" is stated as an achieved, verifiable outcome, but it rests entirely on a label ("editorial-row layouts") the reader cannot resolve — the sentence claims a guarantee it hasn't shown.

Flow break: The two sentences are well joined — "Because the check happens at the head" is a clean causal subordination, exactly the hypotaxis the doctrine prefers over two flat clauses. The gap isn't structural, it's referential: sentence 2 develops the timing consequence of the check but never comes back to confirm that "editorial-row layout" drift is the same thing as the "drift between replicas" it goes on to describe.

Concrete rewrite: Ask author: what does the exact-head check compare to determine a match (a hash of the head revision, a version number, a full diff), and what is an editorial-row layout — is this a CMS-style content row, and what property of its layout has to hold across shards? Fallback if that's not available before publishing: cut both modifiers and state only what's supported — "The indexer checks each shard's head state before each merge, so row layout stays consistent across shards. Because the check runs at the head, drift between replicas surfaces during the merge rather than at read time."

Rewrite check: The fallback carries no rule-of-three, no X-not-Y construction, no em-dash antithesis, no avoid-by-default phrase, no prestige adjective, and no decorative closing line, and it invents no comparison method or row definition — it removes the unsupported words rather than guessing at them. Passes self-detectors.

Remembered line: The paragraph's one fact that survives any rewrite is real and worth keeping as-is: drift shows up at merge, not at read time.

## Trial 6

Verdict: revise

Slop tells: Two hyphenated compound labels carry the paragraph's whole claim without being defined: "exact-head checks" and "editorial-row layouts." Both read as named internal terminology; neither is glossed, and neither matches a standard, portable term the way "write-ahead log" would.

Specificity missing: "Exact-head check" tells the reader when the check runs (at the head, pre-merge) but not what makes it exact — no comparison basis is named. "Editorial-row layout" is worse off: nothing in either sentence says what an editorial row is or what about its layout is being protected, so the phrase functions as decoration around the real claim rather than as a definition of it.

Inflated claim: The two labels let the sentence sound like it's citing an established internal system component rather than describing an unspecified one — "exact" and "editorial" are precision markers attached to nothing precise.

Flow break: None between the sentences — "Because" correctly ties timing to consequence. The paragraph doesn't need restructuring; it needs its nouns paid for.

Concrete rewrite: Since neither compound label is recoverable from context, the safest edit doesn't require going back to the author — it just stops claiming more precision than the sentence has: "The indexer checks each shard's state at the head before merging it, which keeps row layout consistent across shards. Because that check happens at the head, drift between replicas surfaces during the merge instead of at read time." This keeps every fact the paragraph actually supports (head-time comparison, pre-merge timing, merge-vs-read detection) and drops only "exact" and "editorial," which were carrying no retrievable content.

Rewrite check: No rule-of-three, no negative parallelism, no em-dash antithesis, no avoid-by-default phrase, no prestige adjective, no decorative closer. No fact is invented — "state" replaces "exact" as a neutral description rather than a guess at what exactness meant, and "row layout" drops "editorial" rather than assigning it a made-up sense. Passes self-detectors.

Remembered line: A label earns its hyphen when the next clause says what it compares; "at the head" names a place, not a method.

## Trial 7

Verdict: revise

Slop tells: "Editorial-row layouts" is the clearer offender — a coined artifact name with no supporting clause anywhere in the paragraph. "Exact-head checks" is milder: at least its timing is explained, even if its comparison method isn't.

Specificity missing: The paragraph never says what "editorial" distinguishes a row as, or what "layout" means for a row (order, schema, rendering) — sentence 2 spends its entire follow-up on timing (head, merge, read) and never returns to defend either word. Separately, "exact" in "exact-head check" is asserted, not shown: matching how, exactly?

Inflated claim: Small but real — "layouts stay consistent" reads as a settled, checkable property, when the paragraph gives no way to check it because the property itself (what a layout is here) is undefined.

Flow break: Worth flagging a second, smaller gap: sentence 1 frames the guarantee as holding "across shards," and sentence 2 frames the failure mode as "between replicas." If shards and replicas are the same unit here, the paragraph should use one word for it; if they're different scopes, the switch is silently changing what's being compared.

Concrete rewrite: "The indexer checks each shard's head state before merging it, so row layout stays consistent across shards. Because that check runs at the head, a replica that has drifted out of sync is caught during the merge rather than surfacing later, at read time." (Also normalizes to "shard" throughout rather than switching to "replicas" mid-paragraph, since the paragraph gives no signal the two terms mean different things.)

Rewrite check: No rule-of-three, no "X, not Y," no em-dash antithesis, no avoid-by-default phrase, no prestige adjective, no decorative closer. No invented fact — "state" and "row layout" are neutral holdovers of what the source already claimed, not new specifics. Passes self-detectors.

Remembered line: Name the row before you name its layout — "editorial" is doing no work until something in the paragraph says what an editorial row is.

## Trial 8

Verdict: ask-author

Slop tells: Both labels named in the doctrine's own compound-label example show up here almost verbatim — "exact-head checks," "editorial-row layouts" — which makes this less a borderline judgment call than a direct instance of the pattern the detector was written to catch.

Specificity missing: Two gaps, and they compound. First, nothing says what the exact-head check compares — a hash, a revision counter, a row count — so "exact" is asserted rather than demonstrated. Second, "editorial-row layout" is introduced in sentence 1 and then abandoned; sentence 2 talks about "drift between replicas" as though it's continuing the same claim, but nothing confirms that layout inconsistency and replica drift are the same failure rather than two related things this check happens to catch.

Inflated claim: The paragraph doesn't reach for importance language, so this isn't significance-inflation in the usual sense — but "exact" and "editorial" both promise a level of definition the sentences never deliver, which is the same move aimed at precision instead of importance.

Flow break: The causal link between the sentences ("Because...") is sound as syntax, but it's a timing link, not an identity link — it explains *when* the check catches problems without confirming *what* problem "editorial-row layout" inconsistency actually is relative to "drift."

Concrete rewrite: Ask author: what does the exact-head check compare to call two heads a match (hash, revision number, full diff), and is "editorial-row layout" consistency the same thing as the "drift" named in the next sentence, or a separate property this check happens to also protect? Fallback if unavailable: drop both modifiers and let the supported claim stand on its own — "The indexer checks each shard's state at the head before merging it, so row layout stays consistent across shards. Because that check runs at the head, drift between replicas surfaces during the merge rather than at read time."

Rewrite check: The question names two distinct missing facts (comparison method; whether drift and layout inconsistency are one failure or two) without supplying either. The fallback has no rule-of-three, no negative parallelism, no em-dash antithesis, no avoid-by-default phrase, no prestige adjective, no decorative closer, and invents nothing beyond what the source already states. Passes self-detectors.

Remembered line: Two undefined compound labels in one two-sentence paragraph isn't a coincidence worth explaining away — it's the pattern, not an edge case of it.
