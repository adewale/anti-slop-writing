Verdict: revise

Slop tells:
No banned-by-default phrase or high-risk word appears here, and there's no copula displacement, hedged symmetry, rule-of-three, em-dash cadence, or rhetorical staccato — "runs," "finishes," "reads" are all plain, concrete verbs. The one real tell is a coined compound label: "ledger-fold passes" and "invoice-drift totals" are hyphen-flavored compound noun phrases that name a process and a problem the paragraph never defines. Per the coined-compound-labels check, that's fine only when the term is standard in the domain (like "dead-letter queue") or the passage defines it in place. Neither holds: the paragraph gives the fold pass's schedule and output contract (runs after import, finishes before export, produces "folded" rows) but never says what folding computes, and "invoice-drift" is never traced to a cause. The hyphens supply the texture of precision; the mechanism stays out of reach.

Specificity missing:
What does a ledger-fold pass actually compute — re-aggregate ledger entries into a corrected per-invoice total, reconcile against a source system, or something else? And what produces invoice-drift in the first place (late imports, retried imports, out-of-order ledger entries, currency rounding)? Without one of those, "ledger-fold" and "invoice-drift" are names, not mechanisms, and a reader has nothing to check the accuracy claim against.

Inflated claim:
"So invoice-drift totals stay accurate" claims correctness. The only evidence given — the pass finishes before the export starts, and the export reads only folded rows — proves the export never reads a row mid-fold. That's an isolation/consistency guarantee, not a correctness guarantee: a fold pass can finish cleanly and still compute the wrong total, and nothing here rules that out. "Accurate" is carrying more than the stated mechanism earns.

Flow break:
Sentence two reads as the proof of sentence one's claim ("so ... accurate," then here's how), but it proves a narrower thing than it's offered as proof of. The paragraph doesn't mark that narrowing, so the relation it implies ("this is why totals are accurate") is stronger than the relation it actually shows ("this is why the export can't see stale state"). The reader has to notice the gap unaided.

Concrete rewrite:
After each import, the billing job runs a ledger-fold pass that finishes before the nightly export starts, so the export reads only folded rows and never sees an invoice mid-fold. That shows the export is isolated from in-progress folds; it does not show the fold computed the right total. Ask author: what does a fold pass compute, and what specifically causes invoice-drift (late imports, retried imports, out-of-order ledger entries)? Until that's answered, keep the claim scoped to "the export never reads a row mid-fold" and drop "accurate."

Rewrite check:
No banned-by-default phrase, no high-risk word, no em-dash, no decorative closure, and no invented system fact — "late imports, retried imports, out-of-order ledger entries" are offered as candidate answers inside a question to the author, not asserted as what actually happens. Two borderline shapes are worth naming rather than waving past: the three examples inside that question could look like rule-of-three, but they're disambiguating options for the author to pick from, not a claimed tricolon of properties. "That shows X; it does not show Y" could look like negative parallelism, but both sides are evidenced — X is the mechanism just stated, and the limit on Y is the specific gap this critique identifies — so it's an earned distinction, not cadence standing in for one. Passes self-detectors.

Remembered line:
Reading only folded rows proves the export can't see mid-fold state; it doesn't prove the fold got the number right.
