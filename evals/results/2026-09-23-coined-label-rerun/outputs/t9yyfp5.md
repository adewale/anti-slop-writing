Paragraph reviewed:
> The billing job runs ledger-fold passes after each import, so invoice-drift totals stay accurate. Each pass finishes before the nightly export starts, and the export reads only folded rows.

Verdict: keep

Slop tells: None. No banned phrases or watch-list words (no "underscore," "highlight," "seamless," "robust," etc.), no copula displacement (plain verbs "runs," "finishes," "reads" instead of "serves as" or "represents"), no hedged symmetry, no rule-of-three or negative parallelism, no decorative em-dashes, no bullet/bold-header fake structure.

Specificity missing: Minor, non-blocking. The paragraph doesn't say what enforces "finishes before the nightly export starts": whether a scheduler dependency blocks the export job until the pass completes, or the two are simply scheduled far enough apart that they don't collide. That gap would matter if a fold pass ever ran long, but it doesn't undercut the stated claim, since the second mechanism, the export reading only folded rows, protects accuracy independent of timing. Worth confirming with the author only if the ordering claim is relied on elsewhere.

Inflated claim: None. "So invoice-drift totals stay accurate" functions as a significance claim, earned the same way the skill's own "robust queue" example is earned. Two named mechanisms carry it: fold passes run after every import, and the export's read path is filtered to folded rows only. Remove either one and the claim would be inflated; both are present in the source.

Flow break: None. Sentence two answers the question sentence one raises: it supplies the ordering guarantee and the read-path filter that back "stay accurate." The relation is claim-then-evidence, tied together with hypotactic connectives ("so," "before") rather than sequential parataxis.

Concrete rewrite: Not needed. The original already functions as the concrete carrier. It names the actors (the billing job, the export) and the mechanisms (ledger-fold passes, folded rows) that stand behind the causal "so," rather than asserting importance on rhythm alone.

Rewrite check: N/A. No rewrite was produced; the source paragraph is kept as written. Checked anyway: it contains no rule-of-three, no X-not-Y or negative parallelism, no em-dash antithesis, no avoid-by-default phrases, no prestige adjectives, no decorative closure, and no invented facts. Passes self-detectors.

Remembered line: "The export reads only folded rows."
