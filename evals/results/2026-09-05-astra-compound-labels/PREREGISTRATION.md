# Pre-registration — coined compound labels (2026-09-05)

Written before any output was generated, per `runbooks/hillclimb-skill.md`
("Pre-registration (before the round)").

## Source

OpenAI, "Using GPT-6 Astra" prompting guide, section *Personality and writing
style* (fetched 2026-09-05 from
https://developers.openai.com/api/docs/guides/latest-model.md). Its anti-jargon
prompt asks the model to avoid, among other things, "invented compound labels
like 'exact-head checks' and 'editorial-row layouts'".

## Hypothesis

**H1.** The current doctrine does not reliably flag a coined hyphenated noun
phrase that names no established referent and is never defined in context,
because the emphasis-source test asks whether the residual claim "names an
actor, mechanism, or limit" — and a coined label is shaped like a mechanism
name. If true, this is a gap the doctrine's existing tests do not cover.

**H0 (the graveyard outcome).** Existing detectors already flag it, in which
case the import is inert and belongs in `evals/rejected-edits.md`, per the
2026-06-14 lesson: flatten a borrowed rule to the behavior it asks for and
check whether an existing mechanism test already produces that behavior.

## Design

Three fixtures in `probe-fixtures.md`, each stripped of the doctrine's other
tells so a flag can only come from the behavior under test:

- **P1** two coined labels, never defined — should be flagged.
- **P2** established compounds (`write-ahead log`, `copy-on-write`) — must NOT
  be flagged. This is the adversarial guard against a blanket hyphen ban, the
  failure mode `Lessons_learned.md` (2026-06-14) says borrowed surface rules
  introduce.
- **P3** a coined label defined in the same sentence — should be kept, matching
  the existing false-positive-restraint rule.

## Pre-declared accept/reject

- **SESOI** 0.05 on the 0-1 graded scale.
- **N** 3 apply agents (Opus, Sonnet, Haiku), all three fixtures each = 9
  paragraph judgments per doctrine version.
- **Judges** apply/judge separated per `docs/judge-protocol.md`. Only the
  Claude family is reachable from this environment, so per that document's
  "Known limitation: same-family judging" the result is read as a coverage
  signal, not a calibrated number.
- **Rule** ship a doctrine edit only if baseline P1 flag rate is below 3/3 AND
  the edited doctrine raises it without lowering the P2/P3 keep rate. A
  baseline of 3/3 on P1 means H0 holds and the edit goes to the graveyard.

## Second, independent change (not gated by this experiment)

The same guide's *Instruction following* section warns that GPT-6 Astra "can be
more sensitive to instructions contained in skills" and that "unclear or
conflicting guidance in a skill file may cause the model to pause and block work
early", recommending an explicit precedence line. `SKILL.md` currently has no
precedence language and carries an `ask-author` verdict that instructs the model
to stop and ask. That is a packaging fix, tested by behavior (does the skill
still deliver a review?), not by rewrite quality, so it is scored separately.

## Amendment (added after round 1, before round 2 was generated)

Round 1 was underpowered by design, and the design also diluted the signal:
8 of its 12 scored pairs were the P2/P3 guard fixtures, which score 1 under
both doctrines by construction and therefore cannot move. Round 1 result:
mean delta +0.1667, 95% CI [+0.0000, +0.4167], sign-flip p=0.5057 — REJECT.

Round 2 fixes the power problem the honest way rather than by reanalysing
round 1 until it passes: add 4 more paired runs per arm on the discriminating
fixture (P1), for 8 paired observations per arm. The P2/P3 guards are still
run and still reported, but as a no-regression check rather than as scored
pairs that can only contribute zeros.

The accept rule is unchanged and still `score_delta.py` ACCEPT. If round 2
also rejects, the edit does not ship and the entry goes to
`evals/rejected-edits.md`. This amendment is recorded before any round-2
output exists.
