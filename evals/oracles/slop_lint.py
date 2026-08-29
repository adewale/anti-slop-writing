#!/usr/bin/env python3
"""Deterministic slop-lint oracle: regex and structural detectors for LLM-cliche tells.

Division of labor (see docs/deterministic-graders.md): this oracle is the recall
layer. It flags surface forms mechanically, at zero token cost, with no judge in
the loop — so its verdicts carry no self-preference bias. It cannot decide
whether a hit is earned (that judgment stays with the skill and the LLM judge
panel), which is why eval integration uses it almost exclusively for FORBID
checks on rewrite output ("the rewrite reuses no flagged cadence"), not for
require checks that would reward keyword stuffing.

Detector groups:
  structural    cadence shapes (chains, anaphora, echo skeletons, stacked
                questions, stranded auxiliaries). Shapes drift slower than
                vocabulary.
  new-register  the post-2025 conversational voice (significance compression,
                therapy voice, performative honesty, stage management, dev-blog
                boilerplate).
  wikipedia     the older essay register catalogued in Wikipedia's "Signs of
                AI writing" guide.

Severity: "hard" detectors are a finding on one hit; "soft" detectors (the
vocabulary list) are dose-response — one hit can be coincidence, `threshold`
hits in one text is the tell. Either way a hit is a hypothesis, not a verdict.

Provenance: detector regexes, the structural finder algorithms (chain / echo /
anaphora / question-chain finders), and many self-test sentences are ported or
adapted from Simon Willison's llm-cliche-highlighter
(https://github.com/simonw/tools/blob/main/llm-cliche-highlighter.html,
Apache-2.0, Copyright Simon Willison), whose second pattern group is in turn
adapted from Wikipedia's "Signs of AI writing"
(https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing). Several of the
highlighter's noisier detectors (colon-into-a-triple, "don't VERB it",
"is real ... and") are deliberately not ported; see docs/deterministic-graders.md.

Usage:
  python3 evals/oracles/slop_lint.py FILE [FILE...]      lint files (or - for stdin)
  python3 evals/oracles/slop_lint.py --json FILE         machine-readable findings
  python3 evals/oracles/slop_lint.py --scope rewrite F   lint only the last
                                                         "Concrete rewrite:" block
  python3 evals/oracles/slop_lint.py --list              list detector ids
  python3 evals/oracles/slop_lint.py --self-test         run embedded tests

Exit codes for linting: 0 = clean, 1 = findings (any hard hit, or a soft
detector at/over its threshold), 2 = usage error.
`scripts/run_evals.py lint` imports this module to grade `deterministic_checks`
blocks on eval cases.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Callable

ROOT = Path(__file__).resolve().parents[2]
DEMO_FIXTURE = ROOT / "evals" / "fixtures" / "slop-lint-demo" / "input.md"

Span = tuple[int, int, "int | None"]  # start, end, item count (chains/runs only)


@dataclass
class Finding:
    detector: str
    start: int
    end: int
    text: str
    count: int | None = None

    def as_dict(self) -> dict:
        d = {"detector": self.detector, "start": self.start, "end": self.end, "text": self.text}
        if self.count is not None:
            d["count"] = self.count
        return d


# --- structural finders -------------------------------------------------------
# Ported from makeChainFinder / makeEchoFinder / makeQuestionChainFinder /
# makeAnaphoraFinder in the llm-cliche-highlighter (see module docstring).

CHAIN_BODY = r"[^,.;:!?\n–—…]*"
CHAIN_SEP = r"(?:\s*,\s*(?:and\s+|or\s+)?|\s+(?:and|or)\s+|\s*[;&–—]\s*(?:and\s+|or\s+)?|\s+-{1,2}\s+)"
CHAIN_SPLIT = re.compile(CHAIN_SEP, re.IGNORECASE)


def make_chain_finder(head: str, head_test: str) -> Callable[[str], list[Span]]:
    item = head + CHAIN_BODY
    chain = re.compile(rf"\b{item}(?:{CHAIN_SEP}{item})+", re.IGNORECASE)
    head_re = re.compile(head_test, re.IGNORECASE)

    def find(text: str) -> list[Span]:
        found: list[Span] = []
        for m in chain.finditer(text):
            end = m.end()
            while end > m.start() and text[end - 1].isspace():
                end -= 1
            count = sum(1 for part in CHAIN_SPLIT.split(m.group(0)) if head_re.match(part.strip()))
            found.append((m.start(), end, count))
        return found

    return find


ECHO_SENT = re.compile(r"[^.!?\n]+[.!?]?")
ECHO_WORD = re.compile(r"[a-z0-9'’-]+")


def make_echo_finder(min_gram: int = 4, min_run: int = 2) -> Callable[[str], list[Span]]:
    def grams(s: str, n: int) -> set[str]:
        w = ECHO_WORD.findall(s.lower())
        return {" ".join(w[i : i + n]) for i in range(len(w) - n + 1)}

    def find(text: str) -> list[Span]:
        sents = [
            (m.start(), m.end(), m.group(0))
            for m in ECHO_SENT.finditer(text)
            if len(m.group(0).split()) >= 4
        ]
        found: list[Span] = []
        i = 0
        while i < len(sents):
            j = i
            shared = None
            while j + 1 < len(sents):
                if sents[j + 1][0] - sents[j][1] > 3:  # adjacent prose only
                    break
                common = grams(sents[j][2], min_gram) & grams(sents[j + 1][2], min_gram)
                if not common:
                    break
                shared = max(common, key=len)
                j += 1
            run = j - i + 1
            if run >= min_run and shared:
                end = sents[j][1]
                while end > sents[i][0] and text[end - 1].isspace():
                    end -= 1
                found.append((sents[i][0], end, run))
                i = j + 1
            else:
                i += 1
        return found

    return find


QUESTION_CHAIN = re.compile(r"[^.!?\n]+\?(?:\s+[^.!?\n]+\?)+")


def make_question_chain_finder(min_run: int = 2) -> Callable[[str], list[Span]]:
    def find(text: str) -> list[Span]:
        found: list[Span] = []
        for m in QUESTION_CHAIN.finditer(text):
            count = m.group(0).count("?")
            if count < min_run:
                continue
            start = m.start()
            while start < m.end() and text[start].isspace():
                start += 1
            found.append((start, m.end(), count))
        return found

    return find


ANAPHORA_SKIP = re.compile(
    r"^(?:i|it|the|a|an|this|that|we|you|they|he|she|there|but|and|so|in|as|if"
    r"|my|his|her|their|its|these|those|for|at|on|of|to|is|was)$",
    re.IGNORECASE,
)
ANAPHORA_SENT = re.compile(r"[^.!?\n]+[.!?]")
ANAPHORA_WORD = re.compile(r"[A-Za-z'’-]+")


def make_anaphora_finder(min_run: int = 3) -> Callable[[str], list[Span]]:
    def find(text: str) -> list[Span]:
        sents = []
        for m in ANAPHORA_SENT.finditer(text):
            w = ANAPHORA_WORD.search(m.group(0))
            if w:
                sents.append((m.start() + w.start(), m.end(), w.group(0).lower()))
        found: list[Span] = []
        i = 0
        while i < len(sents):
            j = i
            while j + 1 < len(sents) and sents[j + 1][2] == sents[i][2] and sents[j + 1][0] - sents[j][1] < 4:
                j += 1
            run = j - i + 1
            if run >= min_run and not ANAPHORA_SKIP.match(sents[i][2]):
                found.append((sents[i][0], sents[j][1], run))
                i = j + 1
            else:
                i += 1
        return found

    return find


def make_regex_finder(pattern: str, flags: int = re.IGNORECASE) -> Callable[[str], list[Span]]:
    rx = re.compile(pattern, flags)

    def find(text: str) -> list[Span]:
        return [(m.start(), m.end(), None) for m in rx.finditer(text)]

    return find


# --- detector registry ---------------------------------------------------------

@dataclass
class Detector:
    id: str
    name: str
    group: str
    severity: str  # "hard" | "soft"
    description: str
    find: Callable[[str], list[Span]]
    threshold: int = 1  # for soft detectors: hits at/over this are the tell


HIGHLIGHTER = "simonw/tools llm-cliche-highlighter (Apache-2.0)"

DETECTORS: list[Detector] = [
    # structural — cadence shapes; these drift slower than word lists.
    Detector(
        "no-chain", "“No X, no Y” chains", "structural", "hard",
        "Two or more “no …” items in a row (“No fluff, no filler, no jargon”). Count = items.",
        make_chain_finder(r"no[-\s]", r"^no[-\s]"),
    ),
    Detector(
        "did-not-chain", "“Did not X, did not Y” chains", "structural", "hard",
        "Two or more “did not / didn’t …” items in a row. Count = items.",
        make_chain_finder(r"(?:did\s+not|didn['’]t)\s", r"^(?:did\s+not|didn['’]t)\s"),
    ),
    Detector(
        "sentence-anaphora", "Repeated sentence openers", "structural", "hard",
        "Three or more consecutive sentences opening on the same word (“Maybe X. Maybe Y. Maybe Z.”); pronouns and articles are skipped. Count = sentences.",
        make_anaphora_finder(min_run=3),
    ),
    Detector(
        "stacked-questions", "Stacked rhetorical questions", "structural", "hard",
        "Two or more question sentences fired in a row. Count = questions.",
        make_question_chain_finder(min_run=2),
    ),
    Detector(
        "echo-skeleton", "Echoing sentence skeletons", "structural", "hard",
        "Adjacent sentences repeating the same multi-word skeleton (“The parser is a state machine. The renderer is a state machine.”). Count = sentences.",
        make_echo_finder(min_gram=4, min_run=2),
    ),
    Detector(
        "stranded-auxiliary", "Stranded auxiliary contrast", "structural", "hard",
        "A clause landing on a bare auxiliary for the reversal: “The tool died; the data didn’t.”, “Maybe it wouldn’t have.”",
        make_regex_finder(
            r"[;:,]\s+[^.;:!?\n]{2,50}\s(?:did|does|do|was|were|is|are|has|have|had|can|could|would|will)(?:n['’]t)?\s*[.;]"
            r"|\b(?:Maybe|Perhaps)\s+\w+[^.!?\n]{0,40}\s(?:would|could|might|should|did|had|was|is)(?:n['’]t)?\s+(?:have\s*)?\.",
            flags=0,  # case-sensitive on purpose: sentence-initial Maybe/Perhaps
        ),
    ),
    # new-register — the post-2025 conversational voice.
    Detector(
        "significance-compression", "Significance compression", "new-register", "hard",
        "Importance asserted by compression instead of mechanism: “that’s the whole point/game”, “is the entire business model”, “that’s not nothing”, “the punchline is”, “that’s why X mattered”.",
        make_regex_finder(
            r"(?:\b(?:is|was|are|were)|['’]s)\s+the\s+(?:whole|entire)\b(?:\s+\w+)?"
            r"|\bhere(?:['’]s|\s+is)\s+the\s+whole\b(?:\s+\w+)?"
            r"|\bthe\s+entire\s+[\w'’-]+(?:\s+[\w'’-]+){0,4}?\s+(?:is|was|are|were)\b"
            r"|\b(?:that|this|it|which)(?:['’]s|\s+(?:is|was))\s+not\s+nothing\b"
            r"|\bthe\s+punchline(?:\s+(?:is|was|being)\b|\s*[:?])"
            r"|\b(?:that|this)(?:['’]s|\s+(?:is|was))\s+why\b[^.!?\n]{0,80}?\b(?:matter(?:s|ed)?|count(?:s|ed)?)\b"
        ),
    ),
    Detector(
        "therapy-voice", "Therapy voice", "new-register", "hard",
        "Reflective-counselor cadence: “sit with that”, “worth naming”, “you already know (the answer)”.",
        make_regex_finder(
            r"\bsit(?:s|ting)?\s+with\s+(?:that|this|it|(?:the|your)\s+(?:discomfort|feelings?|tension|weight|uncertainty|ambiguity|grief|silence|unease))\b(?:\s+for\s+a\s+\w+)?"
            r"|(?:\b(?:is|are|was|were|feels?|felt|seems?|seemed)|['’]s)\s+(?:\w+\s+){0,2}?worth\s+naming\b(?!\s+names\b)|\bworth\s+naming\s*:"
            r"|\byou\s+already\s+knows?\s+(?:the\s+answer|what|how|why|this|that|it|who|where)\b|\byou\s+already\s+knows?\b(?![ \t]+\w)"
        ),
    ),
    Detector(
        "performative-honesty", "Performative honesty", "new-register", "hard",
        "Sincerity announced rather than demonstrated: “I won’t pretend”, “let’s be honest”, “to be clear”, sentence-initial “Honestly,” / “Look,”.",
        make_regex_finder(
            r"\bI\s+(?:will\s+not|won['’]t)\s+pretend\b"
            r"|\b(?:I['’]ll|let['’]s|to)\s+be\s+(?:honest|clear|blunt|real)\b"
            r"|(?:^|[.!?–—]\s+|\n)(?:Honestly|Look|Truthfully|Frankly)\s*,"
        ),
    ),
    Detector(
        "stage-management", "Stage management", "new-register", "hard",
        "The stage-managed reveal and its props: “here’s the thing/catch/kicker”, sentence-initial “Turns out”, “don’t take my word for it”, “the only X I trust”, “X is dead” / “long live X”.",
        make_regex_finder(
            r"\bhere(?:['’]s|\s+is)\s+(?:the|a|my|one)\s+(?:twist|thing|catch|kicker|rub|problem|first|second|third|next|recent|real|best|worst|surprising|interesting|key|important)\b[\w\s-]{0,20}[:.]"
            r"|(?:^|[.!?–—]\s+|\n)Turns\s+out\b|\bit\s+turns\s+out\s+that\b"
            r"|\b(?:you\s+)?(?:do\s+not|don['’]t)\s+(?:have\s+to\s+)?take\s+my\s+word\s+for\s+(?:it|any\s+of\s+(?:it|this|that))\b"
            r"|\bthe\s+only\s+[\w'’-]+(?:\s+[\w'’-]+){0,2}?\s+(?:I|you|we|it|he|she|they)\s+(?:trust|need|needs|care|want|wants|use|uses|believe)\b"
            r"|\bthe\s+only\s+[\w'’-]+\s+that\s+(?:matters|counts|works|survives)\b"
            r"|\b[\w][\w\s]{2,29}\s+(?:is|are)\s+dead\b|\blong\s+live\s+\w+\b"
        ),
    ),
    Detector(
        "devblog-boilerplate", "Dev-blog boilerplate", "new-register", "hard",
        "Stock simplicity claims: “fits in your head”, “batteries included”, “it just works”, “zero config”, “sane defaults”.",
        make_regex_finder(
            r"\b(?:hold|fit|fits|holds|held)\s+(?:it\s+)?in\s+your\s+head\b"
            r"|\bbatteries[-\s]included\b|\bit\s+just\s+works\b|\bzero[-\s]config(?:uration)?\b|\bsane\s+defaults\b"
        ),
    ),
    # wikipedia — the older essay register from "Signs of AI writing".
    Detector(
        "ai-vocabulary", "AI vocabulary words", "wikipedia", "soft",
        "Words LLMs lean on far more than people do (delve, tapestry, pivotal, interplay, vibrant, bustling, commendable, ever-evolving, …). One hit can be coincidence; several is the tell.",
        make_regex_finder(
            r"\b(?:delv(?:e|es|ed|ing)|tapestr(?:y|ies)|meticulous(?:ly)?|pivotal|intricate(?:ly)?|intricacies|interplay"
            r"|underscor(?:e|es|ed|ing)|garner(?:s|ed|ing)?|bolster(?:s|ed|ing)?|vibrant|bustling|multifaceted"
            r"|seamless(?:ly)?|commendable|ever-evolving)\b"
        ),
        threshold=2,
    ),
    Detector(
        "not-just-but", "“Not just X, but Y”", "wikipedia", "hard",
        "Negative parallelism: “not just/only X but (also) Y” and the “it’s not X — it’s Y” contrast.",
        make_regex_finder(
            r"\bnot\s+(?:just|only|merely|simply)\s+[^.!?\n;]*?\bbut(?:\s+also)?\b"
            r"|\b(?:it|this|that)(?:['’]s|\s+(?:is|was))\s+not\s+[^.!?\n,;—–]{1,60}[,;—–]\s*(?:it|this|that)(?:['’]s|\s+(?:is|was))\b"
        ),
    ),
    Detector(
        "importance-hedging", "“It’s important to note”", "wikipedia", "hard",
        "Didactic hedging: “it is important to note that”, “it’s worth noting”, “it should be noted”.",
        make_regex_finder(
            r"\bit(?:['’]s|\s+(?:is|was))\s+(?:also\s+)?(?:important|worth|crucial|essential|vital)\s+"
            r"(?:to\s+(?:note|remember|understand|recognize|mention|pause|consider|ask)|noting|mentioning|remembering|pausing|considering|asking)\b(?:\s+that\b)?"
            r"|\bit\s+should\s+be\s+noted\b"
        ),
    ),
    Detector(
        "testament", "“Stands as a testament”", "wikipedia", "hard",
        "“Stands/serves as a testament (or reminder)”, “is a testament to”.",
        make_regex_finder(
            r"\b(?:stand|stands|stood|serve|serves|served|standing|serving)\s+as\s+(?:a|an)\s+(?:\w+\s+)?(?:testament|reminder)\b"
            r"|\b(?:is|was|are|were|remain|remains)\s+a\s+(?:\w+\s+)?testament\s+to\b"
        ),
    ),
    Detector(
        "crucial-role", "“Plays a crucial role”", "wikipedia", "hard",
        "“Plays a crucial/pivotal/vital/key/significant role in …”.",
        make_regex_finder(
            r"\bplay(?:s|ed|ing)?\s+(?:a|an)\s+(?:\w+\s+)?(?:crucial|pivotal|vital|key|significant|central|critical|important)\s+role\b"
        ),
    ),
    Detector(
        "landscape-boilerplate", "“Ever-evolving landscape”", "wikipedia", "hard",
        "Scene-setting boilerplate: “the ever-evolving/changing/shifting landscape”, “in today’s fast-paced world”.",
        make_regex_finder(
            r"\b(?:ever-)?(?:evolving|changing|shifting)\s+landscape\b"
            r"|\bin\s+today['’]s\s+(?:fast-paced|ever-changing|ever-evolving|digital|modern|competitive)\s+\w+"
        ),
    ),
    Detector(
        "vague-experts", "“Experts argue”", "wikipedia", "hard",
        "Vague attribution to unnamed authorities: “experts argue”, “some critics have noted”, “industry reports indicate”. Named attribution does not match.",
        make_regex_finder(
            r"\b(?:many|some|several|most|numerous)?\s*(?:experts|critics|observers|scholars|analysts|commentators)\s+"
            r"(?:have\s+|often\s+|widely\s+)?(?:argu(?:e|es|ed)|not(?:e|es|ed)|suggest(?:s|ed)?|believ(?:e|es|ed)|agree[ds]?"
            r"|contend(?:s|ed)?|observ(?:e|es|ed)|caution(?:s|ed)?|claim(?:s|ed)?|cit(?:e|es|ed)|point(?:s|ed)?\s+out)\b"
            r"|\bindustry\s+reports?\s+(?:suggest|indicate|show)\w*\b"
        ),
    ),
    Detector(
        "despite-challenges", "“Despite these challenges”", "wikipedia", "hard",
        "The challenges-and-outlook formula: “despite these challenges”, “challenges remain”, “remains to be seen”, “time will tell”.",
        make_regex_finder(
            r"\bdespite\s+(?:these|those|such|its|their|the|numerous|significant|ongoing)\s+(?:\w+\s+)?challenges\b"
            r"|\bfac(?:e|es|ed|ing)\s+(?:several|numerous|many|significant|various|a\s+number\s+of)\s+challenges\b"
            r"|\bchallenges\s+remain\b|\bremains\s+to\s+be\s+seen\b|\b(?:only\s+)?time\s+will\s+tell\b"
        ),
    ),
    Detector(
        "participle-tail", "Participle sentence tails", "wikipedia", "hard",
        "Superficial analysis bolted onto a sentence end: “…, highlighting/underscoring/showcasing the …”.",
        make_regex_finder(
            r",\s+(?:highlighting|underscoring|emphasizing|showcasing|reflecting|demonstrating|illustrating|signaling"
            r"|solidifying|cementing|reinforcing|underlining)\s+(?:its|his|her|their|our|the|a|an|how|that|what|both)\b[^.!?\n]*"
        ),
    ),
    Detector(
        "promo-boilerplate", "Promotional boilerplate", "wikipedia", "hard",
        "Travel-brochure tone: “nestled in”, “in the heart of”, “hidden gem”, “boasts a”, “breathtaking”, “rich tapestry/heritage”.",
        make_regex_finder(
            r"\bnestled\s+(?:in|on|among|between|along|at)\b|\bin\s+the\s+heart\s+of\b"
            r"|\brich\s+(?:cultural\s+|historical\s+)?(?:heritage|history|tapestry)\b|\bhidden\s+gem\b"
            r"|\bmust-(?:visit|see|try)\b|\bbreathtaking\b|\bboasts?\s+(?:a|an|the)\b"
            r"|\bstunning\s+(?:views?|scenery|architecture|backdrop)\b"
        ),
    ),
    Detector(
        "chatbot-leftovers", "Chatbot leftovers", "wikipedia", "hard",
        "Artifacts pasted straight from a chatbot: “as an AI language model”, “as of my last update”, “knowledge cutoff”, plus markup debris (oaicite, contentReference, turn0search, utm_source=).",
        make_regex_finder(
            r"\bas\s+an\s+ai(?:\s+language)?\s+model\b|\bas\s+of\s+my\s+last\s+(?:update|training)\b|\bknowledge\s+cutoff\b"
            r"|\bI\s+(?:cannot|can['’]t|do\s+not|don['’]t)\s+(?:browse\s+the\s+internet|access\s+real-?time)\b"
            r"|contentReference|oaicite|turn0(?:search|news|image)\d*|attributableIndex|utm_source="
        ),
    ),
]

DETECTORS_BY_ID = {d.id: d for d in DETECTORS}


# --- lint API -------------------------------------------------------------------

def lint(text: str, detector_ids: "list[str] | None" = None) -> list[Finding]:
    """Run detectors over text; returns findings sorted by position."""
    findings: list[Finding] = []
    for d in DETECTORS:
        if detector_ids is not None and d.id not in detector_ids:
            continue
        for start, end, count in d.find(text):
            findings.append(Finding(d.id, start, end, text[start:end], count))
    findings.sort(key=lambda f: (f.start, -f.end))
    return findings


def hit_counts(findings: list[Finding]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for f in findings:
        counts[f.detector] = counts.get(f.detector, 0) + 1
    return counts


def is_failing(findings: list[Finding]) -> bool:
    """True when any hard detector hit, or a soft detector reached its threshold."""
    counts = hit_counts(findings)
    for det_id, n in counts.items():
        d = DETECTORS_BY_ID[det_id]
        if d.severity == "hard" or n >= d.threshold:
            return True
    return False


# --- deterministic_checks engine --------------------------------------------------
# Eval cases may carry a `deterministic_checks` list. Each check is one of:
#   {"detector": "<id>", "max_hits": N}        forbid (default max_hits=0)
#   {"detector": "<id>", "min_hits": N}        require (use sparingly; see docs)
#   {"regex": "<pattern>", "expect": "present"|"absent"}   format checks
# plus optional "scope": "full" (default) | "rewrite" — "rewrite" runs the check
# only on the last `Concrete rewrite:` block of the critique format, so quoting
# a tell in the critique body does not fail a forbid check on the rewrite.

SLOT_RE = re.compile(
    r"^(Verdict|Slop tells|Specificity missing|Inflated claim|Flow break|Concrete rewrite|Rewrite check|Remembered line)\s*:",
    re.MULTILINE | re.IGNORECASE,
)


def extract_rewrite_scope(text: str) -> "str | None":
    """Text of the last `Concrete rewrite:` block, or None when absent."""
    rewrites = [m for m in SLOT_RE.finditer(text) if m.group(1).lower() == "concrete rewrite"]
    if not rewrites:
        return None
    m = rewrites[-1]
    nxt = SLOT_RE.search(text, m.end())
    return text[m.end() : nxt.start()] if nxt else text[m.end() :]


def snippet(s: str, limit: int = 80) -> str:
    clean = " ".join(s.split())
    return clean if len(clean) <= limit else clean[: limit - 1] + "…"


def run_checks(text: str, checks: list[dict]) -> list[dict]:
    """Grade deterministic_checks against output text.

    Returns one {"index", "pass", "evidence"} per check, in the judgment shape
    scripts/run_evals.py grade consumes.
    """
    results: list[dict] = []
    for i, check in enumerate(checks, start=1):
        scope = check.get("scope", "full")
        scoped = text
        if scope == "rewrite":
            extracted = extract_rewrite_scope(text)
            if extracted is None:
                results.append({
                    "index": i, "pass": False,
                    "evidence": "no 'Concrete rewrite:' section found in output (scope=rewrite)",
                })
                continue
            scoped = extracted
        if "detector" in check:
            det_id = check["detector"]
            if det_id not in DETECTORS_BY_ID:
                results.append({"index": i, "pass": False, "evidence": f"unknown detector: {det_id}"})
                continue
            findings = lint(scoped, [det_id])
            hits = len(findings)
            max_hits = check.get("max_hits", None if "min_hits" in check else 0)
            min_hits = check.get("min_hits")
            ok = (max_hits is None or hits <= max_hits) and (min_hits is None or hits >= min_hits)
            if findings:
                evidence = f"{det_id}: {hits} hit(s), e.g. “{snippet(findings[0].text)}”"
            else:
                evidence = f"{det_id}: 0 hits"
            results.append({"index": i, "pass": ok, "evidence": evidence})
        elif "regex" in check:
            expect = check.get("expect", "present")
            m = re.search(check["regex"], scoped, re.IGNORECASE | re.MULTILINE)
            present = m is not None
            ok = present if expect == "present" else not present
            evidence = (
                f"regex {check['regex']!r} matched “{snippet(m.group(0))}”" if present
                else f"regex {check['regex']!r} not found"
            )
            results.append({"index": i, "pass": ok, "evidence": evidence})
        else:
            results.append({"index": i, "pass": False, "evidence": f"malformed check: {check!r}"})
    return results


def validate_check(check: object) -> "str | None":
    """Return an error string when a deterministic_checks entry is malformed, else None."""
    if not isinstance(check, dict):
        return "check must be an object"
    has_detector = "detector" in check
    has_regex = "regex" in check
    if has_detector == has_regex:
        return "check must have exactly one of 'detector' or 'regex'"
    if has_detector:
        if check["detector"] not in DETECTORS_BY_ID:
            return f"unknown detector: {check['detector']!r}"
        for bound in ("max_hits", "min_hits"):
            if bound in check and (not isinstance(check[bound], int) or check[bound] < 0):
                return f"{bound} must be a non-negative integer"
    if has_regex:
        if not isinstance(check["regex"], str) or not check["regex"].strip():
            return "regex must be a non-empty string"
        try:
            re.compile(check["regex"])
        except re.error as exc:
            return f"invalid regex: {exc}"
        if check.get("expect", "present") not in {"present", "absent"}:
            return "expect must be 'present' or 'absent'"
    if check.get("scope", "full") not in {"full", "rewrite"}:
        return "scope must be 'full' or 'rewrite'"
    return None


# --- self-tests -------------------------------------------------------------------
# Positive AND negative cases per detector; most sentences are adapted from the
# highlighter's own patternCases table (Apache-2.0), with expectations remapped
# to this module's merged detector families.

SELF_TEST_CASES: list = [
    # (detector, text, expected match count, expected item counts or None)
    ("no-chain", "No sign-ups, no downloads, no hassle — just paste and go.", 1, [3]),
    ("no-chain", "The plan has no hidden fees and no long-term contracts.", 1, [2]),
    ("no-chain", "No fluff, no filler, no jargon, no corporate buzzwords.", 1, [4]),
    ("no-chain", "There is no catch here, honestly.", 0, []),
    ("no-chain", "No, no, I insist.", 0, []),
    ("no-chain", "no no no", 0, []),
    ("no-chain", "NO FEES, NO CONTRACTS, NO SURPRISES", 1, [3]),
    ("no-chain", "no-code, no-fuss setup", 1, [2]),
    ("no-chain", "I know nothing, notice nothing.", 0, []),
    ("no-chain", "No breaking changes, no new dependencies.", 1, [2]),
    ("did-not-chain", "Did not flinch, did not blink, did not apologize.", 1, [3]),
    ("did-not-chain", "He didn't call and didn't write.", 1, [2]),
    ("did-not-chain", "She did not go.", 0, []),
    ("sentence-anaphora", "Maybe nobody needed it. Maybe the timing was off. Maybe both of those.", 1, [3]),
    ("sentence-anaphora", "Maybe nobody needed it. Maybe the timing was off.", 0, []),
    ("sentence-anaphora", "The parser is small. The renderer is small. The scheduler is small.", 0, []),
    ("sentence-anaphora", "Everything changed. Everything slowed down. Everything cost more.", 1, [3]),
    ("stacked-questions", "Do I know how it works? Where it breaks? Which corners it cut?", 1, [3]),
    ("stacked-questions", "Was it worth it? Would I do it again?", 1, [2]),
    ("stacked-questions", "Did it work? Yes, and then some.", 0, []),
    ("stacked-questions", "What changed?", 0, []),
    ("echo-skeleton", "A shopping cart is an object in the system. A chat room is an object in the system.", 1, [2]),
    ("echo-skeleton", "The parser is a state machine. The renderer is a state machine. The scheduler is a state machine.", 1, [3]),
    ("echo-skeleton", "The parser is fast today. The renderer is fast today.", 0, []),
    ("echo-skeleton", "The parser is fast. The tests are slow.", 0, []),
    ("stranded-auxiliary", "The tool died; the data didn't.", 1, None),
    ("stranded-auxiliary", "Reading mostly passed, writing didn't.", 1, None),
    ("stranded-auxiliary", "Maybe it wouldn't have.", 1, None),
    ("stranded-auxiliary", "The test passed and the build was green.", 0, None),
    ("significance-compression", "That's the whole point.", 1, None),
    ("significance-compression", "This is the whole game, really.", 1, None),
    ("significance-compression", "The whole team showed up.", 0, None),
    ("significance-compression", "Consistency is the entire game.", 1, None),
    ("significance-compression", "He toured the entire factory.", 0, None),
    ("significance-compression", "The entire point is that nobody reads.", 1, None),
    ("significance-compression", "The entire business model is built on churn.", 1, None),
    ("significance-compression", "He ate the entire pizza.", 0, None),
    ("significance-compression", "The entire history of the modern industrial world economy is complex.", 0, None),
    ("significance-compression", "That's not nothing.", 1, None),
    ("significance-compression", "She insisted that nothing was wrong.", 0, None),
    ("significance-compression", "There is nothing left to say.", 0, None),
    ("significance-compression", "The punchline is that nobody laughed.", 1, None),
    ("significance-compression", "He forgot the punchline entirely.", 0, None),
    ("significance-compression", "That's why the export button mattered.", 1, None),
    ("significance-compression", "That is why we left early.", 0, None),
    ("significance-compression", "Distribution is the whole game.", 1, None),
    ("significance-compression", "Here's the whole pitch in one slide.", 1, None),
    ("therapy-voice", "Sit with that for a moment.", 1, None),
    ("therapy-voice", "Just sit with it.", 1, None),
    ("therapy-voice", "She was sitting with the discomfort.", 1, None),
    ("therapy-voice", "Come sit with us at lunch.", 0, None),
    ("therapy-voice", "That loss is real and it's worth naming.", 1, None),
    ("therapy-voice", "Worth naming: nobody asked for this.", 1, None),
    ("therapy-voice", "It's not worth naming names here.", 0, None),
    ("therapy-voice", "The naming convention is worth documenting.", 0, None),
    ("therapy-voice", "You already know the answer.", 1, None),
    ("therapy-voice", "Deep down, you already know.", 1, None),
    ("therapy-voice", "If you already know Python, skip ahead.", 0, None),
    ("performative-honesty", "I won't pretend the migration was painless.", 1, None),
    ("performative-honesty", "Let's be honest: nobody reads the docs.", 1, None),
    ("performative-honesty", "To be clear, the API is unchanged.", 1, None),
    ("performative-honesty", "Honestly, it was fine.", 1, None),
    ("performative-honesty", "She answered honestly.", 0, None),
    ("performative-honesty", "Look at the diagram.", 0, None),
    ("stage-management", "Here's the twist: nobody clicked it.", 1, None),
    ("stage-management", "Here is the thing. The demo was fake.", 1, None),
    ("stage-management", "Here's the door code.", 0, None),
    ("stage-management", "Turns out the cache was never warm.", 1, None),
    ("stage-management", "It turns out that nobody tested it.", 1, None),
    ("stage-management", "She turns out solid work every week.", 0, None),
    ("stage-management", "You don't have to take my word for it.", 1, None),
    ("stage-management", "He kept his word.", 0, None),
    ("stage-management", "It's the only marketing I trust.", 1, None),
    ("stage-management", "The only benchmark that matters is retention.", 1, None),
    ("stage-management", "She was the only engineer on call.", 0, None),
    ("stage-management", "Peer code review is dead.", 1, None),
    ("stage-management", "He played dead until the bear left.", 0, None),
    ("devblog-boilerplate", "The design is small enough to hold in your head.", 1, None),
    ("devblog-boilerplate", "It ships with sane defaults and zero config.", 2, None),
    ("devblog-boilerplate", "Install it and it just works.", 1, None),
    ("devblog-boilerplate", "We choose boring technology on purpose.", 0, None),
    ("devblog-boilerplate", "The helmet fits your head.", 0, None),
    ("ai-vocabulary", "We delve into the intricacies of the interplay.", 3, None),
    ("ai-vocabulary", "Her vibrant tapestry hung in the bustling hall.", 3, None),
    ("ai-vocabulary", "A meticulously curated, seamless experience.", 2, None),
    ("ai-vocabulary", "The report was thorough and well organized.", 0, None),
    ("not-just-but", "This is not just a tool, but a philosophy.", 1, None),
    ("not-just-but", "Not only fast but also reliable.", 1, None),
    ("not-just-but", "It's not a bug — it's a feature.", 1, None),
    ("not-just-but", "He did not buy it.", 0, None),
    ("importance-hedging", "It is important to note that timing matters.", 1, None),
    ("importance-hedging", "It's worth noting the fees are separate.", 1, None),
    ("importance-hedging", "It should be noted that this changed in 2020.", 1, None),
    ("importance-hedging", "Please note the door code.", 0, None),
    ("testament", "The building stands as a testament to postwar optimism.", 1, None),
    ("testament", "Her career is a testament to persistence.", 1, None),
    ("testament", "It serves as a stark reminder that nothing lasts.", 1, None),
    ("testament", "He read from the Old Testament.", 0, None),
    ("crucial-role", "Volunteers play a crucial role in the program.", 1, None),
    ("crucial-role", "She played a truly pivotal role in the merger.", 1, None),
    ("crucial-role", "He plays the role of the villain.", 0, None),
    ("landscape-boilerplate", "Adapting to an ever-evolving landscape.", 1, None),
    ("landscape-boilerplate", "In today's fast-paced world, attention is scarce.", 1, None),
    ("landscape-boilerplate", "The landscape outside the window was gray.", 0, None),
    ("vague-experts", "Experts argue that the policy failed.", 1, None),
    ("vague-experts", "Some critics have noted a decline in quality.", 1, None),
    ("vague-experts", "Industry reports suggest strong demand.", 1, None),
    ("vague-experts", "Dr. Chen argued the opposite in her paper.", 0, None),
    ("despite-challenges", "Despite these challenges, growth continued.", 1, None),
    ("despite-challenges", "Whether it works remains to be seen.", 1, None),
    ("despite-challenges", "Only time will tell whether it sticks.", 1, None),
    ("despite-challenges", "He arrived on time and will tell you himself.", 0, None),
    ("despite-challenges", "The climb was a challenge.", 0, None),
    ("participle-tail", "The bridge reopened in June, highlighting the city's investment in infrastructure.", 1, None),
    ("participle-tail", "Sales doubled, underscoring the strength of the brand.", 1, None),
    ("participle-tail", "She kept highlighting passages in yellow.", 0, None),
    ("participle-tail", "The team, reflecting on the loss, regrouped.", 0, None),
    ("promo-boilerplate", "The inn is nestled in a quiet valley.", 1, None),
    ("promo-boilerplate", "The museum boasts a rich tapestry of exhibits.", 2, None),
    ("promo-boilerplate", "A hidden gem with breathtaking views.", 2, None),
    ("promo-boilerplate", "The soup was rich and hearty.", 0, None),
    ("chatbot-leftovers", "As of my last update, the API was in beta.", 1, None),
    ("chatbot-leftovers", "As an AI language model, I cannot form opinions.", 1, None),
    ("chatbot-leftovers", "See example.com/page?utm_source=chatgpt.com for details.", 1, None),
    ("chatbot-leftovers", "contentReference[oaicite:0]{index=0}", 2, None),
    ("chatbot-leftovers", "The last update shipped on Tuesday.", 0, None),
]


def run_self_tests(quiet: bool = False) -> int:
    failures: list[str] = []

    def check(name: str, cond: bool, detail: str = "") -> None:
        if not cond:
            failures.append(f"{name}{': ' + detail if detail else ''}")

    for det_id, text, expected_n, expected_counts in SELF_TEST_CASES:
        findings = lint(text, [det_id])
        label = f"{det_id} · {snippet(text, 48)!r}"
        check(label, len(findings) == expected_n, f"expected {expected_n} matches, got {len(findings)}")
        if expected_counts:
            got = [f.count for f in findings]
            check(label + " counts", got == expected_counts, f"expected {expected_counts}, got {got}")

    # The demo fixture trips every detector exactly once (the highlighter's
    # "example text trips every pattern exactly once" idea).
    if DEMO_FIXTURE.exists():
        fixture = DEMO_FIXTURE.read_text(encoding="utf-8")
        counts = hit_counts(lint(fixture))
        for d in DETECTORS:
            check(
                f"demo fixture trips {d.id} exactly once",
                counts.get(d.id, 0) == 1,
                f"got {counts.get(d.id, 0)}",
            )
        check("demo fixture has no unexpected detectors", set(counts) == {d.id for d in DETECTORS})
    else:
        failures.append(f"missing demo fixture: {DEMO_FIXTURE}")

    # Scope extraction + check engine.
    critique = (
        "Verdict: revise\n"
        "Slop tells: opens with “Let's be honest”, closes on “that's the whole game”.\n"
        "Concrete rewrite:\n"
        "The importer failed on 3 of 40 files, all with BOM headers; the fix strips the BOM before parsing.\n"
        "Rewrite check: passes self-detectors\n"
    )
    scoped = extract_rewrite_scope(critique)
    check("rewrite scope extracted", scoped is not None and "BOM headers" in (scoped or ""))
    check("rewrite scope excludes critique body", "whole game" not in (scoped or ""))
    r = run_checks(critique, [
        {"detector": "performative-honesty", "max_hits": 0, "scope": "rewrite"},
        {"detector": "significance-compression", "max_hits": 0, "scope": "rewrite"},
        {"detector": "performative-honesty", "max_hits": 0, "scope": "full"},
        {"regex": "^Rewrite check:", "expect": "present"},
    ])
    check("forbid passes on clean rewrite scope", r[0]["pass"] and r[1]["pass"])
    check("forbid fails on full scope quoting the tell", not r[2]["pass"])
    check("format regex check passes", r[3]["pass"])
    r2 = run_checks("No rewrite block here.", [{"detector": "no-chain", "scope": "rewrite"}])
    check("missing rewrite section fails scoped check", not r2[0]["pass"])
    check("validate_check accepts detector forbid", validate_check({"detector": "no-chain", "max_hits": 0}) is None)
    check("validate_check rejects unknown detector", validate_check({"detector": "bogus"}) is not None)
    check("validate_check rejects detector+regex", validate_check({"detector": "no-chain", "regex": "x"}) is not None)
    check("is_failing: soft below threshold is clean", not is_failing(lint("A vibrant afternoon.")))
    check("is_failing: soft at threshold fails", is_failing(lint("A vibrant, bustling afternoon.")))

    total = len(SELF_TEST_CASES) + len(DETECTORS) + 12
    if failures:
        for f in failures:
            print(f"FAIL {f}")
        print(f"{total - len(failures)} passed, {len(failures)} failed")
        return 1
    if not quiet:
        print(f"OK slop_lint self-tests: {total} passed, 0 failed")
    return 0


# --- CLI ---------------------------------------------------------------------------

def line_col(text: str, pos: int) -> tuple[int, int]:
    line = text.count("\n", 0, pos) + 1
    col = pos - (text.rfind("\n", 0, pos) + 1) + 1
    return line, col


def lint_source(name: str, text: str, detector_ids: "list[str] | None", scope: str, as_json: bool) -> int:
    if scope == "rewrite":
        scoped = extract_rewrite_scope(text)
        if scoped is None:
            print(f"{name}: no 'Concrete rewrite:' section found (scope=rewrite)", file=sys.stderr)
            return 1
        text = scoped
    findings = lint(text, detector_ids)
    if as_json:
        print(json.dumps({
            "source": name,
            "findings": [f.as_dict() for f in findings],
            "hit_counts": hit_counts(findings),
            "failing": is_failing(findings),
        }, ensure_ascii=False))
    else:
        for f in findings:
            line, col = line_col(text, f.start)
            extra = f" (count {f.count})" if f.count is not None else ""
            print(f"{name}:{line}:{col} [{f.detector}] “{snippet(f.text)}”{extra}")
        counts = hit_counts(findings)
        summary = ", ".join(f"{k}={v}" for k, v in sorted(counts.items())) or "clean"
        print(f"{name}: {len(findings)} finding(s) · {summary}", file=sys.stderr)
    return 1 if is_failing(findings) else 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Deterministic slop-lint oracle.")
    parser.add_argument("files", nargs="*", help="Files to lint, or - for stdin.")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable findings.")
    parser.add_argument("--detectors", help="Comma-separated detector ids to run (default: all).")
    parser.add_argument("--scope", choices=["full", "rewrite"], default="full",
                        help="rewrite = lint only the last 'Concrete rewrite:' block.")
    parser.add_argument("--list", action="store_true", help="List detector ids and exit.")
    parser.add_argument("--self-test", action="store_true", help="Run embedded self-tests.")
    parser.add_argument("--quiet", action="store_true", help="Self-test: print nothing on success.")
    args = parser.parse_args()

    if args.list:
        for d in DETECTORS:
            thr = f" threshold={d.threshold}" if d.severity == "soft" else ""
            print(f"{d.id}\t{d.group}\t{d.severity}{thr}\t{d.name}")
        return 0
    if args.self_test:
        return run_self_tests(quiet=args.quiet)
    if not args.files:
        parser.print_usage(sys.stderr)
        return 2

    detector_ids = None
    if args.detectors:
        detector_ids = [x.strip() for x in args.detectors.split(",") if x.strip()]
        unknown = [x for x in detector_ids if x not in DETECTORS_BY_ID]
        if unknown:
            print(f"unknown detectors: {', '.join(unknown)}", file=sys.stderr)
            return 2

    status = 0
    for name in args.files:
        text = sys.stdin.read() if name == "-" else Path(name).read_text(encoding="utf-8", errors="replace")
        status = max(status, lint_source(name, text, detector_ids, args.scope, args.json))
    return status


if __name__ == "__main__":
    raise SystemExit(main())
