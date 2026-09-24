## Paragraph reviewed

The billing job runs ledger-fold passes after each import, so invoice-drift totals stay accurate. Each pass finishes before the nightly export starts, and the export reads only folded rows.

## Critique

Verdict: keep

Slop tells: None of the standard tells are present — no banned phrases, no copula displacement, no rule-of-three, no em-dash cadence, no hedged symmetry, no negative parallelism, no outline-shaped conclusion. The one hypothesis worth testing is coined compound labels, on "ledger-fold" and "invoice-drift." Checked against the false-positive restraint (does nearby context supply a mechanism, failure mode, measurement, or boundary?):
- "ledger-fold" is earned by boundary support in the same paragraph: a temporal boundary ("after each import," "before the nightly export starts") and a scope boundary ("the export reads only folded rows"). A reader can verify the pass's place in the pipeline even without the fold's internal computation spelled out. Keep.
- "invoice-drift" is weaker: the paragraph states its effect ("stay accurate") but gives no boundary, measurement, or failure mode for what drift actually is. That's a real gap, tracked below, but not a blocking one — "drift" is a standard divergence-from-expected-state term in this domain (clock drift, config drift, schema drift), so the compound reads as a normal extension of that pattern rather than an invented placeholder.

Specificity missing: What "invoice-drift" measures — a rounding gap, a late-arriving credit, an out-of-order import row, a duplicate entry — is never named. Everything else in the paragraph is independently checkable against the system (does the pass run after import, does export wait for it, does export filter to folded rows); "stay accurate" is the one claim a reader can't verify without that definition.

Inflated claim: None. "stay accurate" is a scoped, modest claim, backed by a stated mechanism (the pass completes before export runs, and export reads only its output) rather than asserted alone.

Flow break: None. Sentence 1 names its relation directly with "so" (result). Sentence 2 opens with the subordinator "before" (temporal precedence) and closes with "and the export reads only folded rows" — two distinct guarantees, ordering and scope, stated side by side rather than one dressed up as explaining the other. That's parataxis used honestly for two co-occurring facts, not an unstated relation the reader has to guess at.

Concrete rewrite: None required. Optional, only if "invoice-drift" isn't already defined elsewhere in the source this paragraph is drawn from: Ask author: what counts as invoice drift here — a rounding gap, a late-arriving credit, an out-of-order row, something else? If there's an answer, add it as a short in-line gloss; if not, leave the paragraph as written rather than guessing.

Rewrite check: The ask-author note above contains no rule-of-three, no X-not-Y / negative parallelism, no em-dash antithesis, no banned avoid-by-default phrases, no prestige adjectives, no decorative closure, and no invented facts — it asks rather than asserts. Passes self-detectors.

Remembered line: "the export reads only folded rows" — the most concrete, checkable detail in the paragraph, and the one a reader could go confirm directly against the code.
