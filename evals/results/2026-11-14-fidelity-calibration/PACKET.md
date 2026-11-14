# Human fidelity calibration packet

Read README.md before scoring. Do not open PRIVATE-KEY.json until your answers are frozen.

## H01

### Task and supplied source

Review and rewrite this launch sentence: The safety review is not just a checklist. It is how we prove the release is ready.

Facts available:
No additional facts beyond the source text.

### Response to review

Verdict: ask-author

Slop tells:
- "not just X. It is Y." is negative parallelism, split across two sentences. The "not just a checklist" side argues against a claim nobody made.
- "how we prove the release is ready" is the inflated half. "Prove" and "ready" carry the weight without saying what is checked or what counts as proof.
- Flattened version: "The safety review shows the release is ready." It names no actor, mechanism, or limit, so the cadence was carrying the line.
- Syntax-relation test: restating the implied relation with a connective gives "The review is more than a checklist *because* ___." The blank cannot be filled from the source without inventing it.

Specificity missing:
- What the review examines.
- What evidence it produces.
- What outcome blocks a release.
- Who signs off.

Inflated claim:
"Prove the release is ready" overstates what a review can do. A review finds or fails to find problems. Without a named criterion, "ready" is undefined.

Flow break:
None to judge in a single sentence. The second sentence depends on the first only through contrast cadence, with no stated relation.

Concrete rewrite:
Ask author:
- What does the review actually check (for example, which failure modes or test categories)?
- What does it produce (a report, a sign-off, a gate in the release process)?
- What result blocks the release, and who decides?

Fallback 1: cut the sentence if the next lines already describe the review's contents.
Fallback 2: use a plain version that adds no facts: "The safety review decides whether the release ships."

That fallback only restates what the source implies. If the review has no power to block a release, the sentence is wrong and should be corrected.


## H02

### Task and supplied source

Review the cadence: Our route planner is nimble — astonishingly nimble — and safe — in all conditions — with elegant controls — for every journey — without compromise.

Facts available:
No additional facts beyond the source text.

### Response to review

Verdict: revise

Slop tells: Repeated em-dash insertions manufacture emphasis while interrupting the sentence. “Astonishingly” amplifies “nimble” without explaining it; “elegant,” “every journey,” and “without compromise” add praise rather than detail.

Specificity missing: What makes the planner nimble? What makes its controls easy to use? What conditions support the safety claim?

Inflated claim: “Safe in all conditions” promises universal safety. “Without compromise” implies no tradeoffs. Neither is supported. Flattened, the sentence says: “Our route planner is nimble and safe in all conditions, with elegant controls for every journey.” Removing the cadence exposes the unsupported claims.

Flow break: Each dash adds another endorsement instead of explaining how the planner works. The insertions have equal emphasis but no stated relationship.

Concrete rewrite: “Our route planner helps you plan a route.” This conservative fallback removes the unsupported performance, safety, and usability claims. A more informative version requires evidence from the author.


## H03

### Task and supplied source

Review and tighten this passage. Each paragraph ends on a short two-part contrast.

The cache survived the migration. The index did not.

We doubled the workers. The latency held.

The model got bigger. The errors stayed.

The team shipped fast. The users stayed away.

Facts available:
No additional facts beyond the source text.

### Response to review

**Critique:** Every paragraph uses the same device: two clipped sentences, the second flipping or negating the first. The repetition makes the passage read as a formula, and the contrasts are told rather than shown. With no added facts available, the fix is to vary structure and fold some of the contrasts into single sentences, without inventing details.

**Rewrite:**

The cache survived the migration, but the index did not.

We doubled the workers, and latency held where it was.

The model got bigger. The errors stayed.

Although the team shipped fast, the users stayed away.


## H04

### Task and supplied source

Review this product update sentence: The new caching layer delivers 47% faster page loads and reduces infrastructure costs by approximately a third.

Facts available:
No additional facts beyond the source text.

### Response to review

**Critique:** The sentence is concise and benefit-focused, but neither claim includes a comparison baseline or supporting evidence. “47% faster” is also ambiguous: it should not be rewritten as “47% less load time,” which means something different. With no additional facts, the figures cannot be verified.

**Rewrite:** The new caching layer delivers 47% faster page loads and reduces infrastructure costs by about one-third.


## H05

### Task and supplied source

Rewrite by committing to a position: While speed matters, correctness is also important. Whether you're shipping a prototype or production code, our linter helps.

Facts available:
No additional facts beyond the source text.

### Response to review

Move fast, but don’t compromise on correctness. Our linter helps whether you’re shipping a prototype or production code.


## H06

### Task and supplied source

Review and rewrite this paragraph:

Most teams treat observability as a tool problem. Better teams treat it as a culture problem. The best teams treat it as a design problem. Each shift moves observability earlier in the system lifecycle, until the question becomes how to design systems that can be inspected at all.

Facts available:
No additional facts beyond the source text.

### Response to review

**Critique**

- **Strength:** The three-step escalation (tool → culture → design) is clear, and the closing idea, systems designed to be inspectable, is the real insight.
- **Repetition:** "Treat it as a... problem" appears three times. It builds rhythm but feels formulaic, and the labels "better" and "best" are asserted rather than earned.
- **Vague claim:** "Each shift moves observability earlier in the system lifecycle" is abstract. Earlier than what, and how? Tools come after deployment, culture during operation, design before build, but this isn't stated.
- **Weak ending:** "Inspected at all" is slightly muddy. The question isn't really whether systems can be inspected, but whether they are built to be.
- **Tone:** "Most teams... better teams... best teams" reads as a mild generic hierarchy. Concrete contrast would persuade more.

**Rewrite**

Most teams treat observability as a tool problem: they buy a platform and wire it in after the system ships. Better teams see it as a culture problem and build habits of instrumentation, on-call review, and shared ownership. The best teams treat it as a design problem. Each step moves observability earlier in the lifecycle, from after deployment, to during operation, to before the first line is written, until the real question becomes how to build systems that can be inspected from the start.


## H07

### Task and supplied source

Review and rewrite this paragraph:

Most teams treat observability as a tool problem. Better teams treat it as a culture problem. The best teams treat it as a design problem. Each shift moves observability earlier in the system lifecycle, until the question becomes how to design systems that can be inspected at all.

Facts available:
- The paragraph is from an engineering guide written by a payments team.
- The team now requires every new service to attach a request ID that is passed to every downstream call.
- They added the rule after an incident in which they could not trace a failed payment across five services.

### Response to review

### Critique
The tool–culture–design progression is memorable, but “most,” “better,” and “best” create an unsupported ranking. It also frames these approaches as alternatives when they can reinforce one another. The final phrase, “inspected at all,” is vague. For a payments engineering guide, the incident and resulting design requirement make the point more concrete and useful.

### Rewrite
Observability requires tools and shared practices, but it also needs to be designed into a system. After we could not trace a failed payment across five services, we began requiring every new service to attach a request ID and pass it to every downstream call. That requirement makes tracing a design concern from the start, rather than something we try to add during an incident.


## H08

### Task and supplied source

Tighten this without inventing a cause: We opened the help desk. We published the hours. Nobody came.

Facts available:
No additional facts beyond the source text.

### Response to review

We opened the help desk and published the hours, but nobody came.


## H09

### Task and supplied source

Review and tighten this passage.

We measured the cache cold and warm. Cold, every request hit Postgres and p99 sat at 800ms. Warm, the same requests came from Redis at 12ms. The disk was the bottleneck. The cache was the fix.

The job failed nine times in the first hour. Every failure was a timeout to the same host, and every retry fired instantly. We added a two-second backoff and failures dropped to one an hour. The retries were the load. The backoff was the relief.

The report query scanned four million rows in six seconds. We added an index on the timestamp column and the same query returned in forty milliseconds. The scan was the cost. The index was the cure.

The 3am rollout broke with no owner online. We added a health check that auto-reverts on a 5xx spike, and the next bad deploy rolled itself back in ninety seconds. The manual step was the gap. The health check closed it.

Facts available:
No additional facts beyond the source text.

### Response to review

Verdict: revise

Slop tells:
- All four paragraphs end on the same two-part closer: "The X was the Y. The Z was the W." (bottleneck/fix, load/relief, cost/cure, gap/closed it). Taken one at a time, most pass the staccato test, because the prior sentences give both sides. As a set, the rhythm is supplying the relation four times. This is the document-level density failure.
- Flattened, each closer restates the numbers just given. "The disk was the bottleneck. The cache was the fix." reduces to "the cache fixed the slow disk reads," which the 800ms-to-12ms comparison already shows. Only the retry closer adds a claim.
- Nouns like "relief," "cure," and "gap" are decorative labels for results already shown.

Specificity missing: Nothing needed. The numbers carry the passage. The closers only repeat them.

Inflated claim: "The index was the cure" and "the cache was the fix" are mild. The closers imply causal proof the paragraphs only half argue. The retry paragraph claims the retries were the load, but the evidence is only that backoff reduced failures.

Flow break: The four paragraphs are parallel in length and shape, and none says why it follows the last. Whether they are four examples of one claim is unstated. Ask author: what is the claim these four cases support (for example, "measure before fixing" or "each fix targeted one named cause")? If there is none, the passage can stay as four independent cases.

Concrete rewrite:

We measured the cache cold and warm. Cold, every request hit Postgres and p99 sat at 800ms. Warm, the same requests came from Redis at 12ms, so serving from the cache took the disk out of the request path.

The job failed nine times in the first hour. Every failure was a timeout to the same host, and every retry fired instantly, so the retries kept adding load to the host that was timing out. After we added a two-second backoff, failures dropped to one an hour.

The report query scanned four million rows in six seconds. With an index on the timestamp column, the same query returned in forty milliseconds.

The 3am rollout broke with no owner online, because reverting it needed a person to do a manual step. We added a health check that auto-reverts on a 5xx spike, and the next bad deploy rolled itself back in ninety seconds.


## H10

### Task and supplied source

Review and rewrite, or cut if unsupported: Amid an era of ceaseless disruption, organizations require transformative offerings that cultivate frictionless progress.

Facts available:
No additional facts beyond the source text.

### Response to review

Verdict: ask-author (fallback: cut)

Slop tells:
- Generic opener: "Amid an era of ceaseless disruption" fits any product in any decade.
- Prestige cluster: "transformative," "cultivate," "frictionless progress."
- Vague actors: "organizations" and "offerings" name no buyer and no product.
- Abstract nouns in place of mechanisms: "progress" and "disruption" never become an event, a delay, or a cost.
- Flattened version: "Companies need products that help them move without obstacles." That names no actor, mechanism, or limit, so the cadence and vocabulary were carrying the line.
- Syntax-relation test: "require" implies disruption causes the need, but "because" can't be filled without inventing which disruption and which need.

Specificity missing:
- Which organizations (size, industry, role of the reader)?
- What offering?
- What friction (approval queues, deploy time, handoffs, data access)?
- What changed because of it, and by how much?

Inflated claim:
"Transformative" and "frictionless" assert a large effect with no evidence, scope, or limit. "Frictionless" is also an absolute no real product can meet.

Flow break:
As an opener, it names a vague problem and promises a vague solution, so the reader has no concrete next question. Nothing follows from it.

Concrete rewrite:
Ask author:
- Who is the reader, and what is the product?
- What specific task slows them down today, and what does the product change about it?
- Is there a measured result, a customer, or a before/after you can cite?

Fallback: cut the sentence. Start with the first sentence that names the product and the task it changes. The source supplies no facts, so any rewrite here would invent a buyer, a pain point, or a number.


## H11

### Task and supplied source

Review this draft in the Critique output format. It describes a personal site.

The visitors were remarkably authentic. Makers, teachers, people curious about publishing. Their interest was beyond commerce. It was about community.

The site stores articles in a repository that the owner can copy to another host. That portability was no accident. It was the plan.

Facts available:
No additional facts beyond the source text.

### Response to review

## Critique

- **The audience description is vague and evaluative.** “Remarkably authentic” does not explain what distinguished these visitors. “Makers, teachers, people curious about publishing” gives a clearer sense of the audience without judging their sincerity.
- **The draft overstates visitors’ motives.** “Their interest was beyond commerce” and “It was about community” present a single, definite motivation. With no supporting details available, these claims should be qualified or omitted.
- **The clipped rhythm becomes repetitive.** Both paragraphs end with short declarations that tell readers how to interpret the preceding material. “It was the plan” largely repeats “That portability was no accident.” Combining those sentences would make the prose more direct.
- **The portability detail is the strongest material.** The repository and the owner’s ability to copy articles to another host provide a concrete explanation of the site’s design. Keep the scope precise: the text establishes that the articles are portable, not necessarily the entire site.
- **The paragraphs need a clearer relationship.** The move from community to content storage is abrupt. Present them as separate aspects of the site unless the source can establish a connection between them.


## H12

### Task and supplied source

Review and tighten this passage. Each paragraph ends on a short two-part contrast.

The cache survived the migration. The index did not.

We doubled the workers. The latency held.

The model got bigger. The errors stayed.

The team shipped fast. The users stayed away.

Facts available:
No additional facts beyond the source text.

### Response to review

Verdict: revise

Slop tells: Each paragraph uses the same two-sentence contrast. The individual contrasts are supported by the text, but repeating the device four times makes cadence do too much of the organizing work.

Specificity missing: “The latency held” and “The errors stayed” leave the measurements unclear. The source supplies no cause for any outcome, so tightening should preserve that uncertainty.

Inflated claim: None. These are restrained observations; the problem is repetition, not exaggerated significance.

Flow break: The passage moves from migration to worker count, model size, and user uptake without establishing a connection. No available fact supports adding a causal hinge between those cases.

Concrete rewrite:
The cache survived the migration, but the index did not.

Doubling the workers left latency unchanged.

Although the model got bigger, the errors persisted.

The team shipped fast, but users stayed away.


## H13

### Task and supplied source

Review this product update sentence: The new caching layer delivers 47% faster page loads and reduces infrastructure costs by approximately a third.

Facts available:
No additional facts beyond the source text.

### Response to review

Verdict: ask-author

Slop tells:
- "delivers" is a mild inflated verb for what is a measured result; "approximately a third" next to "47%" mixes a precise figure with a rounded one, so the reader can't tell how firmly either is measured.
- Two benefits joined by "and" read as a launch-copy pair. Nothing links them: a cache could cut load time without cutting cost, or the reverse.
- "new caching layer" names no layer. It could be a CDN, an application cache, or a database cache.

Specificity missing:
- Baseline and measure for "47% faster": median or p95, which pages, measured where (lab or real users), and compared with what.
- Whether "faster page loads" means time to first byte, largest contentful paint, or full load.
- What "infrastructure costs" covers (compute, bandwidth, database) and over what period.
- The mechanism: what is cached, and why that reduces both load time and cost.

Inflated claim:
Both figures carry the sentence's weight, and neither has a baseline, so the importance comes from the numbers alone. "Approximately a third" also invites the reader to ask whether it is 30% or 36%.

Flow break:
As a single sentence, none. In a product update, though, the reader's next question is "faster than what, measured how?", and the sentence doesn't answer it.

Concrete rewrite:
Ask author:
1. What does the layer cache (API responses, rendered pages, database queries), and where does it sit?
2. For the 47%: which metric (median, p95), which pages, lab or field data, and compared with which previous release?
3. For the cost drop: which line items, what period, and is the figure measured or projected? Give the exact number if there is one.

Fallback if none of that is available: cut the cost claim and keep only the figure the author can back, with its measure attached. Do not fill in the metric, the cache type, or the cost basis. Once the author supplies them, the shape is: "[Cache type] now serves [what], so [metric] on [pages] dropped 47% ([baseline], [measure]). Because fewer requests reach [origin component], [named cost line] fell from X to Y."


## H14

### Task and supplied source

Review and rewrite this line: Durable execution isn't just retry logic. It is a new programming model.

Facts available:
No additional facts beyond the source text.

### Response to review

Verdict: ask-author

Slop tells: “Isn't just” sets up a familiar escalation from a concrete feature to an abstract claim. The short second sentence supplies emphasis without explaining the distinction.

Specificity missing: What does durable execution let a programmer express or do beyond retries? What makes that programming model new?

Inflated claim: “A new programming model” claims novelty without evidence. Flattened: “Durable execution extends beyond retry logic and constitutes a new programming model.” The claim remains unsupported once the cadence is removed.

Flow break: The second sentence asserts a distinction that the first sentence has not established. A “because” connecting them would require facts absent from the source.

Concrete rewrite: Ask author: what specific behavior distinguishes durable execution from retry logic, and what supports calling it new? Without those facts, cut the novelty claim and use this restrained fallback: “Durable execution involves more than retry logic.” This preserves the source’s narrower claim but still needs an explanation in the surrounding text.


## H15

### Task and supplied source

Review this paragraph for AI rhythm tells: We instrumented the pipeline, we tightened the rubric, and we shipped a new judge. We measured before, we measured after, and we measured the gap. The result is a system that learns from its own runs, scales with the workload, and improves with each iteration.

Facts available:
No additional facts beyond the source text.

### Response to review

Verdict: ask-author

Slop tells:
- Sentence 1 is a rule-of-three of parallel "we [verb]" clauses (instrumented / tightened / shipped). The cadence implies a sequence of causes without saying how they connect.
- Sentence 2 repeats the same device: "we measured before, we measured after, and we measured the gap." Three clauses, one verb, with the third restating the first two. Flattened, it says "we compared before and after," and the measurement count adds nothing.
- Sentence 3 is another rule-of-three ("learns from its own runs, scales with the workload, and improves with each iteration"). The three claims overlap, and none names an actor, mechanism, or limit.
- Document-level density: all three sentences use the same triadic, paratactic structure. The paragraph's rhythm, not its argument, supplies the relations (density failure in the doctrine).
- "The result is a system that..." is an outline-style payoff sentence.

Specificity missing:
- What was instrumented, and what the instrumentation recorded.
- What changed in the rubric.
- What the new judge does differently from the old one.
- The measured metric, its before and after values, and the size of the gap.
- What "learns from its own runs" means mechanically (does anything feed back into the rubric, judge, or pipeline automatically?).
- What "scales with the workload" was tested against.
- What "improves with each iteration" is based on (how many iterations, which measure).

Inflated claim:
- "A system that learns from its own runs, scales with the workload, and improves with each iteration" is unsupported by the preceding sentences. They describe a one-time change and a single before/after measurement. That is evidence for one improvement, not for continuous learning, scaling, or iterative gains.

Flow break:
- Sentence 1 to 2: the relation between shipping the judge and measuring is not named. Syntax-relation test: "We shipped a new judge, and then we measured" works, but whether the measurement validated the judge or motivated the rubric change cannot be supplied without inventing it.
- Sentence 2 to 3: "The result" implies the measured gap led to the learning/scaling claims. Supplying "because" would require facts the source lacks (e.g., "because the gap shrank over repeated runs"). The syntax stands in for a relation that is not shown.

Emphasis-source test: flattened version: "We changed the pipeline, rubric, and judge, compared results before and after, and the system is better." The residual claim names no actor, mechanism, or limit, so the rhythm was carrying it.

Concrete rewrite: Ask author:
- What metric did you compare before and after, and what were the two values?
- What did the new judge or tightened rubric change (a specific criterion, a score threshold, a failure case it now catches)?
- Is there an actual feedback loop where run outputs change the rubric or judge? If so, what triggers it?
- Is there evidence for scaling (a workload size tested) and for repeated improvement (more than one iteration measured)?

Fallback: cut the third sentence's "learns / scales / improves" claims unless the author supplies evidence for each. Keep one sentence naming the metric and the gap, with the changes subordinated to it, in the form "Because [change], [metric] moved from [before] to [after]." The bracketed slots need author facts; do not fill them.


## H16

### Task and supplied source

Review this paragraph using the Critique output format. The piece is a personal blog post by Joe Beda about publishing his blog over ATproto.

The actual implementation took about a working day. Hugo for static site generation, Cloudflare Pages for hosting, and Sequoia to handle the ATproto publishing step. The pipeline: write a post, push to GitHub, CI publishes the ATproto record, builds the site, deploys it.

Current coding tools made it practical to add features that would otherwise get cut. The cover images on each post (the 1200x630 cards used for social previews and Bluesky thumbnails) are generated by a Node.js script using Satori and the same brand fonts as the site. Title and description go in, image comes out, with a sidecar file so they can be regenerated if the branding changes. Without good tooling that kind of thing stays on the 'someday' list.

Facts available:
No additional facts beyond the source text.

### Response to review

Verdict: ask-author

Slop tells:
- "Current coding tools made it practical to add features that would otherwise get cut" is a vague actor ("current coding tools") with a general claim about practicality. It names no tool and no feature that was nearly cut.
- "Without good tooling that kind of thing stays on the 'someday' list" is a generic closer. "Good tooling" repeats "current coding tools" without adding anything. The sentence is also mildly hedged symmetry: it is true of any project and any feature.
- The first paragraph is mostly fine. "The pipeline: write a post, push to GitHub, CI publishes the ATproto record, builds the site, deploys it" is a plain, ordered list of actions, so it is earned compression. The only wobble is the sentence fragment "Hugo for static site generation, Cloudflare Pages for hosting, and Sequoia to handle..." which is a rule-of-three, but here it enumerates real tools with real jobs, so it is keep.

Specificity missing:
- Which coding tool? Cursor, Claude Code, Copilot, Aider, other?
- What did the tool do in the Satori script: write it, debug font loading, design the sidecar format?
- Which features would have been cut, other than cover images? The paragraph gives one example and generalizes from it.
- How long did the cover-image script take compared with the "working day" for the whole build?

Inflated claim:
"Made it practical" and "would otherwise get cut" claim a causal effect (tool changed what got built) with no evidence. The reader cannot tell whether the tool saved ten minutes or four hours. The "someday list" line asserts the counterfactual without support.

Flow break:
The paragraph moves from the pipeline to the claim about tools without a hinge. The cover-image example is concrete and good, but the claim sentence precedes it, and the closing sentence restates the claim instead of using the example. The relation (this script is the case where tooling changed the decision) is implied by order only.

Concrete rewrite:
Ask author: which coding tool did you use, and what specifically did it do for the cover-image script (write the Satori layout, handle font loading, build the sidecar regeneration)? How long did it take?

Fallback without those facts: cut the opening claim and the closing "someday" sentence, and let the example carry the point. Keep the example sentences as written, then end on the sidecar detail:

"The cover images on each post (the 1200x630 cards used for social previews and Bluesky thumbnails) are generated by a Node.js script using Satori and the same brand fonts as the site. Title and description go in, image comes out, with a sidecar file so they can be regenerated if the branding changes."

Optional, once the author supplies the tool name: "Because [tool] wrote most of the Satori script, the cover images, which I would have skipped, cost [time] instead of an afternoon of font and layout debugging." The bracketed slots must come from the author.


## H17

### Task and supplied source

Rewrite by replacing borrowed-pattern emphasis with a clarifying relation: Durable execution isn't just retry logic. It is a new programming model.

Facts available:
- In this framework a workflow's state is saved after every step.
- If the process crashes, the workflow resumes from the last saved step instead of starting over.
- Developers write the workflow as ordinary sequential code; the framework does the saving and resuming.

### Response to review

Durable execution lets developers write workflows as ordinary sequential code because the framework saves state after every step and, after a crash, resumes from the last saved step instead of starting over.


## H18

### Task and supplied source

Review and rewrite, or cut if unsupported: Amid an era of ceaseless disruption, organizations require transformative offerings that cultivate frictionless progress.

Facts available:
No additional facts beyond the source text.

### Response to review

Verdict: reject

Slop tells: “Amid an era of ceaseless disruption” is a generic opening. “Transformative offerings” and “frictionless progress” promise benefits without naming what changes or how.

Specificity missing: Which organizations, what disruption, what offering, and what obstacle it removes.

Inflated claim: “Ceaseless,” “transformative,” and “frictionless” assert scope and effectiveness without evidence. Flattened, the sentence says: “Organizations need offerings that help them progress.” The cadence supplies emphasis, but the claim supplies no mechanism.

Flow break: The sentence implies that disruption creates a need for these offerings, but neither the disruption nor the connection is explained.

Concrete rewrite: Cut. To replace it, ask the author which organizations face what specific problem and how the offering addresses it. With no additional facts, a substantive rewrite would require invention.

