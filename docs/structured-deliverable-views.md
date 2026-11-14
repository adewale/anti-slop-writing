# Structured deliverable views — offline prototype

**Proposed instrument policy, not a new preregistration or a validated extractor.**
The owner approved implementing this offline design, not adjudicating the 130-item
review packet. No human answers, new model calls, writing scores, or doctrine changes
are produced. The registered revision-2 runner and its stopped checkpoint remain intact.

## Concrete failure and smallest repair

In review item R001, the writer supplies grounded exporter prose, a question about
half-written batches, and a separate “Remembered line” with an explicit qualification:

> A crash costs you only the batch that was in flight.
>
> (Caveat: use this line only once the author confirms the in-progress-batch behavior.
> Otherwise end on "the batches already finished stay on disk.")

Concatenating this into the main rewrite makes an optional, unconfirmed alternative
look like manuscript text. Removing the caveat would be worse. The proposed repair
is to keep **roles and their attached qualifications**, not merely matching words.
In another retained response (`d41b29706ebfbae5be83aecf`), the separate remembered line
has no explicit offer to use it as a replacement or conditional alternative. The
proposed annotation excludes that summary instead of appending a second ending.

## Default policy

| Role | Meaning | What must travel with it |
|---|---|---|
| `prose` | Proposed manuscript text, not a summary of the critique | Material attribution, uncertainty and limitations |
| `author_question` | Information requested from the author | Optional/required status and any publishing condition |
| `decision` | Explicit keep/cut instruction, not manuscript prose | Any scope restriction; a fallback is conditional instead |
| `conditional_alternative` | Prose or an action usable only under a stated condition | The condition, attached to that item, before or after its content |

- A question is not manuscript text just because its `Ask author:` label was removed.
  An optional question must not become a requirement. Retain meaningful label text in
  its content or qualification reference; a neutral role tag does not replace “optional.”
- A separately labelled remembered line is excluded by default. If the writer explicitly
  offers it for use as an alternative, retain it in that role, with every qualification.
  R001's “use this line only once…” is such an explicit conditional offer. This is a
  **proposed annotation**, not a human finding or an automatic rule for all such fields.
- A self-check earns no credit as procedure, but a material qualification inside it
  cannot simply disappear. Select and attach that source passage to the affected item.
- Keep alternatives and decisions separate. There is no aggregate `mixed` disposition
  whose meaning an auditor must guess; several item roles can coexist.
- Empty `items: []` explicitly means no deliverable was identified, not a technical
  extraction failure. Ambiguity is different: nonempty `unresolved` blocks construction.
- These defaults apply equally to labelled and unlabelled responses, without arm/model
  metadata. The script does not infer roles from the presence of template headings.

## Common exposure policy

Both views start from **one identical, unmodified raw response string**:
1. `full.response` is that exact string, including all fields and qualifications.
2. `deliverable.items` contains referenced source passages, with neutral role metadata
   and their attached source qualifications. It never concatenates questions, fallback
   text or a remembered line into a primary manuscript paragraph.

There is no pre-stripping of `Rewrite check`, `Remembered line`, headings or any other
field. No regex rewrites copied text. An annotator may omit a purely cosmetic label
from its span, but deciding that it is cosmetic remains a semantic review obligation.
The full view now differs from revision 2's already-blinded full view; this is an
explicit new design, **not a repair to the old results**. Future full-view judgments
would have to be newly registered and elicited, not borrowed from either prior prompt.

Raw and structured formatting still expose different cues, and source wording can
reveal an arm. This cannot establish a perfectly blinded, pure causal critique or
length effect. A future study must call its estimand view sensitivity and report
these limitations; role tags are experimental presentation, not original prose.

## Mechanical contract

`scripts/deliverable_views.py` consumes JSON with `source` and `annotation`. Other
fixture metadata is ignored and never copied to the views. The annotation has exactly:
- `version: 1` and `source_sha256`, the SHA-256 of the UTF-8-encoded source string;
- `items`, in source order, each with a unique `id`, a `role`, one contiguous `content`
  reference, and a list of `qualifications` references in source order;
- `unresolved: []`, required explicitly. A nonempty list fails closed.

A reference is `{start, end, text}`: zero-based Unicode character indices, end exclusive,
and an exact copy of `source[start:end]`. Offsets refer to characters, not UTF-8 bytes.
Booleans as integers, blank selections, paraphrases and whitespace normalization are rejected. One contiguous
content span avoids internal splicing but does not prove that all context was selected.
Content cannot overlap other items or qualifications. An exact shared qualification
may be attached to multiple items; partially overlapping notes are rejected. This small
contract does not represent every nested or inline condition. If the needed context
cannot be expressed without overlap or splicing, mark it unresolved and stop; do not
force it into `prose` or call it an empty deliverable.

The output contains both views, a private source hash, and every `omitted_spans` range
for inspection. Omissions are not declared harmless. Output status is always
`unvalidated_prototype`; there is no approval field, audit pass, score or launch action.
A conditional alternative without any qualification is rejected. The validator cannot
prove a qualification is relevant, catch an omitted condition falsely annotated as
ordinary prose, or decide that a proposed role assignment is correct. Exact source
coverage is a mechanical property, **not semantic validation**.

Before any future judging, keep the source hash, offsets, omitted passages, fixture
provenance and reference outputs private. Judges would receive only the registered
view payload, task/facts and grading prompt, not annotations or expected fixture data.
This prototype does not implement that orchestration or grant permission to run it.

## Offline fixtures and commands

Three cases in `evals/fixtures/structured-deliverables/` copy retained responses:
- `conditional-remembered-line.json`: R001; prose, author question and conditional
  alternative remain distinct, with the caveat attached to the alternative.
- `unlabelled-prose.json`: R002; the entire four-paragraph prose response stays intact.
- `separate-remembered-line.json`: only proposed prose is selected; the standalone
  remembered-line summary remains visible in the omissions ledger.

All are labelled `split: "tune"`, with archive-member provenance and source hashes.
Their annotations and expected outputs are **model-proposed design fixtures**, not
human answers, independently held-out validation, or writing-quality ground truth.
Tests bind their source strings to the original frozen baseline archive.

```bash
python3 scripts/deliverable_views.py \
  evals/fixtures/structured-deliverables/conditional-remembered-line.json
python3 -m unittest discover -s tests -p test_deliverable_views.py
python3 scripts/review_rewrite_rejudge.py verify \
  --dest evals/results/2026-11-14-rewrite-only-rejudge
```

The renderer has no provider/model dependencies. `--out` exclusively creates a new
file; malformed input exits 2 without emitting a partial view or overwriting an
existing artifact. UTF-8 JSON output preserves the source's decoded characters and
whitespace exactly. A successful exit means mechanical construction only.

## Remaining work

Validate role assignment, contextual completeness and audit specificity independently
before designing a new registered comparison. Resolve disagreements about genuinely
ambiguous source offers rather than regenerating until an auditor passes. Original
extractions and negative audits stay archived; the old gate is not overridden.
The separate human fidelity-judge calibration also remains outstanding. No one is being
asked to decide 130 cases merely to authorize this small offline prototype.
