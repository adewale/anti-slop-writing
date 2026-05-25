---
name: anti-slop-writing
description: Use this skill to review, draft, and rewrite prose so it does not read like generic LLM output. Apply it to articles, slide copy, wiki pages, README text, emails, posts, scripts, product/DevRel copy, and important writing with AI tropes, inflated significance language, generic cadence, weak flow, or marketing fog.
license: MIT
compatibility: Agent Skills clients including Pi, Claude Code, Codex, and OpenCode. Instruction-only skill; no scripts, package installs, or network access required.
---

# Anti-Slop Writing

Use this skill for any important writing or rewriting task.

Load local references only when the task needs them:

```txt
references/anti-slop-writing-doctrine.md — read for a full prose review or when changing the doctrine.
references/flow-by-relation.md — read when paragraphs are locally clear but list-like, or when fixing transitions/conclusions.
references/rewrite-patterns.md — read when producing multiple concrete rewrites or adding a new failure pattern.
```

## Core principle

```txt
Sharp detail beats inflated significance.
```

AI writing often fails by doing this:

```txt
less detail, more importance
```

Fix by doing this:

```txt
more detail, earned importance
```

## Before writing

Answer:

```txt
What is the exact point?
What concrete detail proves it?
What sentence machinery is making it feel true?
What should the reader remember?
```

If those are unclear, ask or inspect sources before drafting.

## Source-backed detectors

Use these checks before rewriting:

```txt
AI-writing signs: superficial analysis, undue significance language, canned emphasis, negative parallelisms, rule-of-three overuse, formulaic dashes, table/bold formatting as fake structure.
Rhetorical-style drift: watch noun-heavy abstractions, nominalizations, phrasal coordination, and informational density without mechanism.
Practical AI-editing tells: repeated “Not X. Y.” rhythm, symmetrical paragraph length, parallel headings, and bullet + bold-header + colon patterns.
Rhetorical staccato: do not ban antithesis/parallelism; watch antithetical parataxis where rhythm implies the relation before evidence is unpacked.
Hypotaxis preference: when the relation matters, prefer subordination and connective syntax over side-by-side clauses; use “because,” “although,” “when,” “while,” “where,” “once,” or an explicit summary noun to show which idea modifies which.
Flow-by-relation test: paragraphs should make the next question possible, not merely sit beside each other in a plausible order. At section boundaries, name the relation: cause, contrast, dependency, inference, resolution, scope change, or level-of-detail change.
Conclusion test: a conclusion should return to the concrete carrier, admit the limit if needed, and state the reusable structure. Avoid ending with a generic thesis sentence that could belong to any essay in the category.
Unseeing frame: unsee the polished sentence into the machinery that made it feel true; inspect cadence, contrast, omitted relation, evidence scope, and abstraction leaks.
Contribution bar: contribution must justify length; add judgment, framing, depth, or cut.
DevRel pressure test: durable prose needs judgment, evidence, runnable artifacts, and taste.
```

## Default editing pass

Before finalizing prose:

```txt
1. Delete generic opening.
2. Find prestige vocabulary clusters.
3. Replace abstract nouns with concrete mechanisms.
4. Remove “not just X but Y” unless it is the exact point.
5. Cut superficial “highlighting/underscoring” clauses.
6. Check every claim of importance against evidence.
7. Replace vague actors with named sources or uncertainty.
8. Collapse redundant bullets.
9. Vary sentence rhythm deliberately.
10. Audit staccato contrast cadence by identifying the hidden relation: contrast, evidence scope, cause, consequence, exception, or scope control.
11. Prefer hypotaxis to parataxis when the relation matters: subordinate the secondary idea instead of placing equal-weight clauses side by side.
12. Check paragraph flow: each paragraph should answer the prior question or make the next question necessary. Add hinge sentences when sections read like a list.
13. Check the conclusion: return to the concrete carrier, name what was made visible or solved, state what transfers, and avoid a generic final sentence.
14. Replace rhythm with relation when the line still sounds good but has not named the mechanism.
15. End with a concrete remembered line.
```

## Avoid by default

Phrases:

```txt
In today's rapidly evolving landscape
In the realm of
When it comes to
At its core
Let's dive into
It's worth noting that
It's important to note that
A testament to
Not just X, but Y
Not only X, but also Y
Same X. Same Y. Different Z.
Not X. Y.
This is where X comes in
In conclusion
Overall
Ultimately
I hope this helps
```

Words to review:

```txt
delve
realm
landscape as metaphor
tapestry
testament
pivotal
crucial
underscore
intricate
meticulous
multifaceted
nuanced as filler
foster
bolster
garner
showcase
highlight
emphasize
encompass
utilize
facilitate
transformative
groundbreaking
seamless
robust outside engineering context
```

## Staccato contrast test

Do not treat every short contrast as slop. First classify it:

```txt
Earned antithesis: the contrast names a real distinction already evidenced. Keep or use once.
Compressed antithesis: the contrast is true but hides the mechanism. Expand into the relation.
Decorative antithesis: the contrast supplies closure without evidence. Cut or replace.
```

Rewrite rules:

```txt
replace rhythm with relation
prefer hypotaxis to parataxis
```

Typical moves:

```txt
Although X, Y.
Because X, Y.
When X changes, Y no longer means the same thing.
Where X only shows final state, Y records process.
X matters because it changes Y.
Once X is visible, Y becomes inspectable.
Because the concrete example is small/memorable/inspectable, it can carry the larger claim.
```

## Rewrite patterns

Bad:

```txt
This underscores the importance of durable execution.
```

Better:

```txt
The workflow can fail on step 4, retry only that step, and keep the previous outputs.
```

Bad:

```txt
Cloudflare is not just a CDN, but a platform.
```

Better:

```txt
Cloudflare turns the network boundary into a programmable runtime.
```

Bad:

```txt
This empowers teams to build seamless experiences.
```

Better:

```txt
The team can ship a WebSocket room without running a room server.
```

Weak ending:

```txt
A benchmark is stronger when you can inspect the run that produced it.
```

Better ending:

```txt
Because the pelican project is small enough to inspect and strange enough to remember, it works as a compact carrier for the larger claim: a benchmark is stronger when you can inspect the run that produced it.
```

## Critique output format

When reviewing existing prose, use:

```txt
Verdict: keep / revise / reject
Slop tells:
Specificity missing:
Inflated claim:
Flow break:
Concrete rewrite:
Remembered line:
```

## Tone target

Prefer:

```txt
specific
source-grounded
direct
varied rhythm
concrete mechanisms
named tradeoffs
memorable line
```

Avoid:

```txt
safe essay voice
prestige abstraction
balanced filler
fake profundity
marketing fog
```
