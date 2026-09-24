# Critique

**Paragraph reviewed:**

> The billing job runs ledger-fold passes after each import, so invoice-drift totals stay accurate. Each pass finishes before the nightly export starts, and the export reads only folded rows.

**Verdict:** keep

**Slop tells:** None. No prestige vocabulary (delve, crucial, seamless, transformative, etc.), no displaced copulas ("serves as," "stands as," "represents"), no hedged symmetry ("whether you're X or Y," "while X, Y is also important"), no rule-of-three, no decorative em-dash clusters, no banned avoid-by-default phrases, no "Not X. Y." staccato rhythm, no bullet/bold/table formatting standing in for structure. Every verb is plain and concrete — runs, finishes, starts, reads — doing real work instead of inflating a copula.

**Specificity missing:** None. The paragraph names the actor (the billing job), the mechanism (ledger-fold passes), the trigger (after each import), the ordering guarantee (each pass finishes before the nightly export starts), and the read scope (the export reads only folded rows). That is enough concrete detail to reconstruct the invariant being described; nothing here is a vague actor or an unnamed source that would need an `ask-author` note.

**Inflated claim:** None. "stay accurate" looks like a claim of importance, but it is earned rather than asserted: the second sentence supplies the two mechanisms that back it — a temporal guarantee (folding finishes before export starts) and a scope guarantee (export reads only folded rows). Per the skill's false-positive restraint rule, a claim backed by a stated mechanism in the same or adjacent sentence is kept, not flagged — the same shape as the doctrine's own kept example, "The queue is robust because each job has an idempotency key, a retry receipt, and a dead-letter cutoff," where the qualifier is earned by a named mechanism rather than borrowed cadence.

**Flow break:** None. The two sentences are not independent facts placed side by side; sentence 2 answers the question sentence 1 raises (accurate as of when, and reading what data). "before the nightly export starts" gives the temporal dependency, and "reads only folded rows" gives the scope condition that makes sentence 1's claim true. This passes the flow-by-relation test: sentence 2 makes the next question ("how is that guaranteed?") answered rather than merely following sentence 1 in a plausible order. The relations are already named via "so," "before," and the shared subject — no unstated parataxis to repair.

**Concrete rewrite:** Not needed. No slop tell was flagged, so there is nothing to replace or cut; rewriting an already-concrete sentence would only paraphrase working prose, which the skill's contribution bar (contribution must justify length) argues against.

**Rewrite check:** N/A — mandatory field acknowledged, but since no `Concrete rewrite` text was produced (source stands as-is), there is nothing to run the self-detectors against. If this paragraph had needed a rewrite, the check would confirm the replacement avoids rule-of-three, X-not-Y, em-dash antithesis, banned phrases, prestige adjectives, decorative closure, and invented facts — but that check has no target here.

**Remembered line:** "the export reads only folded rows" — the one clause that states the actual guard condition; a reader who keeps only this still knows why the totals can't be read mid-fold.
