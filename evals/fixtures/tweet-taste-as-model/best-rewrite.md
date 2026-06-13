Reference: best known scoring rewrite of the tweet in `input.md`.
Source tweet: https://x.com/itsreallyvivek/status/2065477778125062177 (@itsreallyvivek)
Produced: 2026-06-13 by claude-opus-4-8 applying the anti-slop-writing skill, hand-tuned against the skill's own self-detectors.
Role: regression floor. This is the minimum bar the case `tweet-best-rewrite-anchor` (evals/rewrite-evals.json) holds future rewrites to — a candidate must score at least as high as this one on every assertion and graded dimension; scoring below it is a regression. It is editable upward: if a reviewer or a future run produces a strictly better rewrite that still clears every assertion and dimension, replace this file and re-record the reference scorecard to raise the floor.

What this version fixes versus the original (the two real weaknesses):
1. Conceit honesty: the original asserts that fast-feedback calibration "transfers upward" to slow, decade-long bets. That transfer is the unproven step. Here it is marked as a wager, not a finding.
2. Parataxis density: the original closes nearly every section on a matched two-part antithesis. Here most closers are converted to named relations (hypotaxis); at most two genuinely earned antithesis lines are kept.
Preserved: the opening, all eight concrete carriers (de Groot/Chase-Simon, Fermi, Tetlock/GJP, Murphy-Winkler, Kahneman-Klein, Sutton/Radford, AlexNet, Hamming), the write-a-numbered-prediction-then-score-it mechanism, and the carrier-bound ledger ending. Fermi's estimate is kept honest (crude, about half the actual yield).

---

nobody flinches when you call debugging a skill. call taste a skill and the room gets uncomfortable, because taste is the one part of research we've agreed to treat as fate. you have it or you don't, and the people who have it were apparently issued it at birth, along with the right advisor. it's a comforting story, and it's wrong. taste is a model in your head that predicts which ideas will work before you've paid for them, and like every model it's only as good as its training data and its training loop. both of those are under your control.

look at what taste is made of

in 1946, adriaan de groot showed chess grandmasters a midgame position for a few seconds and asked them to rebuild it from memory. they placed over ninety percent of the pieces; club players placed a fraction. the obvious reading is that masters have better memory, so in the seventies chase and simon reran the experiment with one change: the pieces were scattered at random. the grandmasters fell to nearly novice level.

the masters never had better memory. they had a library of tens of thousands of real positions, and a random board matched none of them. what looked like perception was retrieval. what looked like a gift was inventory.

so when a senior researcher glances at your method and says "this won't survive a strong baseline," she isn't channeling anything. she's matching your idea against a few thousand stored failures that rhyme with it. taste is a library, and a library is built by shelving, which is the one part of the job anyone can do.

predict before you peek

at the trinity test, enrico fermi stood in the observation bunker dropping scraps of paper. when the blast wave arrived he watched how far it pushed them and put the yield at around ten kilotons, weeks before the instrument readings came back. the estimate was crude — the real number was closer to twice that — but accuracy was never the point. fermi guessed before every measurement on principle, because a measurement you predicted teaches you something a measurement you merely received cannot: it grades your model of the world.

predicting every experiment before you run it is old advice. the part that does the work is writing the prediction down, with a number, before you look. an unwritten prediction is worthless, because your memory will quietly rewrite it to match the result, and you'll walk away confirmed by an experiment that should have stung. psychologists call it hindsight bias. researchers call it "yeah, that's about what i expected," said after every result, forever.

so make it mechanical. before the run: expected delta, confidence, one sentence of reasoning. after the run: what actually happened, and which part of your reasoning broke. when you read a paper, stop at the end of the methods and write down the numbers you expect in the tables. you'll be wrong constantly. that's the point — each miss is a labeled example, and the model being trained is you.

keep score

philip tetlock spent two decades scoring expert predictions and found most experts performed near chance. the interesting part came later. in the good judgment project, ordinary volunteers who practiced forecasting under strict scoring beat intelligence analysts who had access to classified information, by around thirty percent. the winners weren't smarter; they made granular predictions, got scored, and updated. judgment improved like a trained skill because it was trained like one.

the cleanest case is the weather. murphy and winkler found that when american forecasters say seventy percent chance of rain, it rains close to seventy percent of the time. meteorologists are among the best-calibrated professionals ever measured, for a boring reason: they predict daily, in numbers, and reality grades them by morning. a pundit forecasting elections gets feedback twice a decade and never writes the number down. the hardware is identical; what differs is whether anyone closes the loop.

your research judgment is already living one of those two lives. if you call which of this month's releases will matter and go back to the ledger a year later, you're keeping score. if you just trade opinions in group chats, you're the pundit who never gets graded.

shrink the bet

there's a real objection here. in a rare 2009 adversarial collaboration, kahneman and klein asked when intuition can be trusted at all, and their answer was narrow: only in environments with stable regularities and fast, clear feedback. firefighters and chess players develop real intuition because they get both; stock pickers get neither and develop confident noise. research looks like bad terrain, because the feedback on a research bet can take two years and arrives confounded with compute, execution, and luck.

the fix is to shrink the bet until the loop closes. you can't get fast feedback on "is mechanistic interpretability the right decade-long direction." you can get same-day feedback on "this ablation will cost two points," and same-week feedback on "this paper's gains won't replicate at larger scale." the wager — and it is a wager, not a proven theorem — is that calibrating on the small bets sharpens the big ones. that part you can't verify, because the slow bets are exactly the ones reality hasn't graded yet. what you can do is calibrate where reality answers fast, because that's the only place the loop closes at all.

trace the calls, not the credentials

when sutton wrote the bitter lesson, it read less like a prediction than a confession of one principle: general methods that ride compute beat clever methods that ride human insight, eventually. when alec radford bet on generative pretraining for gpt-1, the field's energy was in task-specific supervised models, and the bet looked unfashionable. neither call was a hunch. each came from a small set of load-bearing beliefs, held explicitly, with a clear sense of what evidence would break them.

this is the upper floor of taste. the library gets you pattern-matching: this idea smells like the ones that died. principles get you the calls patterns can't reach, the ones about things nobody has tried yet. so when you study a great call, don't study the person; reconstruct the belief that generated it, then ask what your own load-bearing beliefs are. most researchers, asked to list theirs, recite the consensus of their timeline. that's not taste. that's an rss feed.

retrain on fresh data

in 2012, plenty of researchers with excellent judgment dismissed alexnet. their taste wasn't broken; it was trained on a decade where neural networks genuinely didn't work, and it kept predicting that decade after the data had changed. taste is a model, and models drift. the better your library served you in the last regime, the more confidently it fails you in the next, which is why the people loudest about what can't work are so often the ones who were right last time.

maintenance is the same work as training. keep predicting, keep scoring, and treat a run of surprises as a fire alarm rather than noise: when reality keeps beating your model, the model is stale, however distinguished its past. hamming said knowledge compounds like interest. so does calibration, with one difference: interest never has to be marked down. your taste does, and the researchers who last are the ones who do the markdown themselves, before the field does it for them.

start the ledger this week. it will be embarrassing for six months. it was always going to be embarrassing for six months. the only question is whether you collect the data.
