# Rewrite-only re-judging — stopped at the extraction-audit gate

**No writing judgments ran. No rewrite-quality, fidelity, task-fulfillment or
critique-effect result is available.** The extraction instrument needs review first.
The installed skill and original baseline scores are unchanged.

Revision 2 was committed as `d6cee815f95f3b4300373b83d9fc5306e8bf5c18` before the
first call. See [PREREGISTRATION.md](PREREGISTRATION.md) and [AMENDMENTS.md](AMENDMENTS.md).
The comparison would reuse 444 baseline outputs from 37 cases/13 families; no new
writing outputs were generated. All cases are public, design-visible historical data.

## Observed checkpoint

- **488 valid extractions:** 444 primary GPT-6.1 Sol extractions and the preregistered
  44 independent Opus 5.5 reliability extractions.
- **444 independent Opus audits:** all technically valid, with **93 outputs flagged**
  by at least one audit check (20.9%). These are model flags, not human-confirmed defects.
- **Zero** schema-invalid replacements, missing audits, empty-deliverable dispositions,
  or new writing judgments. No flagged extraction was regenerated, replaced or excluded.
- **932 distinct selected provider responses**, all bound to exact retained requests and
  re-audited raw responses. No response-id overlap with the baseline's 2,412 selected responses.
- Returned list-price counters total **$13.36**. These are not subscription invoices or
  separately billed API expenditure. Only the existing subscription transports were used.
- Model calls ran **16:33:37–16:53:24 UTC** (19m47s), 2026-11-14. All remaining
  work was model-free publication, receipt checking and replay.

| Apply model | Arm | Audited | Flagged |
|---|---|---:|---:|
| Sonnet 5.5 | No skill | 111 | 10 |
| Sonnet 5.5 | Skill | 111 | 60 |
| GPT-6.1 Sol | No skill | 111 | 6 |
| GPT-6.1 Sol | Skill | 111 | 17 |

Failed checks overlap: qualification preservation **60**, completeness **27**,
deliverable-only scope **16**, disposition **5**. These are dependent outputs, not
93 independent cases. Differential flags make silently dropping them especially unsafe.

The 44 reliability pairs had **38/44 exact text matches**, mean token-set Jaccard
**0.9841**, and **43/44 disposition agreement**. High extractor agreement does not prove
faithfulness: both extractors can share a boundary mistake, and token overlap can hide
a missing qualification.

## What the flags reveal—and do not establish

The retained artifacts show why a substring check alone is insufficient:
- In `d41b29706ebfbae5be83aecf`, the extracted view appends the separate `Remembered line`
  to the rewrite. Its words are verbatim, but the proposed manuscript now has an extra ending.
- In `fb9f758af058a9c81245def6`, label removal deletes `Fallback:` before a cut instruction.
  The auditor flags a lost conditional role. Whether a label is cosmetic or meaningful
  cannot be settled by stripping every template label identically.
- Some flags may be auditor overreach. In `c4782a1995c09f5586191d0c`, it treats `mixed`
  as requiring different dispositions across items, although the extraction contains
  author questions plus conditional cuts. The registered categories did not define that
  distinction. Bare questions are also sometimes flagged just for losing `Ask author:`.

These are instrument-review examples, **not human adjudication**. The counts cannot be
read as skill failure rates. The strict prospective gate has blocked interpretation,
including potentially spurious flags; it was not relaxed after seeing them.

Another boundary to resolve: extraction reads the raw response, while the planned full
view uses the baseline's already-blinded response. Qualification context inside a removed
`Rewrite check` can therefore be unavailable in the full view but eligible for extraction.
Any future repair must specify a common exposure policy rather than call the contrast a
pure critique effect. The existing baseline is retained, not silently rescored or corrected.

## Next: human review of the instrument

[REVIEW-PACKET.md](REVIEW-PACKET.md) contains **130 blinded items**: all 93 flagged
outputs union the 44 independently preselected reliability outputs, with seven overlaps.
Copy `REVIEW-ANSWERS.template.json`; record evidence and freeze/date the answers **before
opening `REVIEW-PRIVATE-KEY.json` or the model audit file**. The packet deliberately
contains unflagged controls, but is enriched and cannot estimate population error.

First settle what constitutes the deliverable, which role labels carry meaning, and how
qualifications outside a rewrite field must travel with it. Any subsequent instrument
repair needs a visible amendment and must preserve these successful responses; this
checkpoint has no automatic override or permission to regenerate until the flags vanish.
This review is separate from the outstanding [18-item human fidelity-judge calibration](../2026-11-14-fidelity-calibration/README.md).
No model has supplied either set of human answers.

## Evidence and offline reproduction

`checkpoint.json`, `extraction-audit.json`, `reliability.json`, `receipts.json`, process
logs/status and `trials.tar.gz` retain the checkpoint. The archive contains every raw
request/response and audit, the original frozen manifest/prompts and registration receipt.
`checksums.json`, `publication-sources.json` and `reproduction.json` record integrity and
byte-identical, model-free reconstruction. The frozen baseline archive is a separate input.

```bash
python3 scripts/review_rewrite_rejudge.py verify \
  --dest evals/results/2026-11-14-rewrite-only-rejudge
```

Use the publication commit. Verification traps model invocation, checks all 932 selected
provider receipts and exact slot coverage, and reconstructs the checkpoint, reliability
report and blind review packet without network access. Repository validation logs are
in `validation/`; the extraction-audit gate was also tested with model invocation trapped.
