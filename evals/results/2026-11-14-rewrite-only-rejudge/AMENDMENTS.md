# Prospective amendment — revision 2

Original preparation: `57f3c68d4e52079c762b7d7765e3df4d2f39d725` (PR #29).
**All changes below precede the first extraction, audit or judgment call.** The
original design remains available in Git; no original baseline score is changed.

## Review findings and repairs

1. **Outcome-dependent exclusions.** `none` removed the entire case/model. A writer
   offering no deliverable is a substantive failure, not an extraction error. Retain
   and judge the empty deliverable. Only exhausted technical extraction failures cause
   matched case-wide exclusions. Count every dropped slot, not only its root failure,
   against the original model/arm denominator. Report the conditional estimand.
2. **Null is not equivalence.** Replace “critique-driven” with “attenuated; deliverable
   benefit uncertain.” Positive intervals are descriptive, not promotion evidence.
   Rename the difference in differences `view_attenuation`: extraction and formatting
   change alongside critique. No pure causal critique/length claim.
3. **Verbatim can still be misleading.** Require complete sentences/items and retained
   qualification context. Add a fresh Opus audit of every primary extraction before
   any judging. Any missing or negative audit blocks scoring; retain the original
   extraction and negative audit, do not regenerate or choose the other extractor.
   This automated instrument check is not human fidelity calibration. The budget
   estimate rises from ~$55 to ~$80 list-price equivalent, not API expenditure.
4. **Missing registered outputs.** Export the original baseline comparison on the same
   retained cases and `prompt_shift`, as promised but not implemented in revision 1.
   Export fact conditions separately and retain pair identities.
5. **Resume and input integrity.** Check exact slot coverage, source/prompt hashes,
   original-score hashes and cached request identity. Stop on transport/response-audit
   failure, including non-auth failures; do not turn it into a technical exclusion.
   Recover an existing complete raw response without another provider call. Never
   automatically resume a previously recorded transport failure.

## Validation discipline

Added failing tests first: the original implementation produced eight errors and one
failure across the initial 22-test revision (missing audit/interpretation machinery,
missing audit gate). After implementation these passed. Additional tests cover exact
slot coverage, changed prompts, no retry after transport failure, and raw-response
recovery without regeneration. Full repository gates are run before registration.

## Frozen limits

Scope, baseline source responses, 37 cases/13 families, public historical holdout
status, model panel, three trials, and dimension anchors do not change. No skill
instructions change. Human calibration is still outstanding. An audit block means
there are **no writing-score results**, not a null or negative skill result.
