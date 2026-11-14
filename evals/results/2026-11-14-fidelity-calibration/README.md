# Human fidelity calibration — awaiting a human

**No human adjudication has been performed.** This packet prepares the outstanding
human-review task; it does not replace it with another model or claim a calibrated
judge. The completed subscription baseline's joint criterion failed, with substantial
Opus/GPT fidelity disagreement. No doctrine is promoted pending this review.

## Review procedure

1. Open `PACKET.md`, but not `PRIVATE-KEY.json` or the original baseline outputs.
2. Copy `ANSWERS.template.json` to an answers file. Give each of the 18 responses a
   factual-fidelity score and quote the evidence or describe precisely what is missing.
   Use only that item's task/source/facts; do not search for an author or model.
3. Freeze/date your answers **before** opening the key. The key reveals apply model,
   arm, original case/trial and both judges' scores/evidence.
4. Adjudicate the disagreements: unsupported new fact, lost qualification, harmless
   phrasing difference, unsupported demand by a judge, or unresolved ambiguity. Keep
   any disputed items disputed. A human opinion is not infallible ground truth.
5. Publish the human annotations and a calibration note separately. Do not overwrite
   original judgments or silently change the baseline's reported decision. Any future
   rubric/instrument change needs its own version, tests and prospective study.

Factual fidelity, 1–5, matching the registered baseline anchors:
- **5:** no unsupported factual assertions; all material qualifications preserved.
- **4:** minor imprecision without a material new claim.
- **3:** one material unsupported implication or lost qualification.
- **2:** material invented details.
- **1:** central fabrication or reversal.

A necessary question, justified cut, explicitly hypothetical conditional or earned keep
can score 5. Supplied observations do not establish causation. A named self-check,
critique template, confidence claim or additional length is not evidence of fidelity.
Do not invent facts to rescue either the response or a judge's expectation.

## Selection and limitations

Six largest absolute ordinal fidelity disagreements per apply model, at most one
response per case/model; ties use opaque output IDs. Three low/median/high agreement
controls per model come from other distinct cases. Shuffle with seed 261117. Exact
selection, counts and identities are in `selection.json` and the key. Both original
arms are eligible; no arm is favored in selection. Fact twins and families can overlap.

This deliberately oversamples disagreement. Eighteen items are not 18 independent
replications, a random accuracy audit, or a population judge-error estimate. Public
historical holdouts are included as frozen evidence, not fresh blind data. Do not
adapt doctrine to them. Cooperative reviewer blinding is limited: the key and public
archive are available, and style/length may suggest an arm even without labels.

The packet can be regenerated without model calls from the retained baseline runtime:

```bash
python3 scripts/review_followthrough.py packet \
  --baseline eval-workspace/subscription-baseline \
  --dest /tmp/fidelity-calibration
```

If runtime files are absent, extract the baseline's checked-in `trials.tar.gz` first
and point `--baseline` at its directory containing `manifest.json`, `cases.json`,
`apply/` and `judge/`. Do not read or copy credentials; they are not in the archive.
Real discourse-layer failure examples remain a separate human-supplied dependency.
