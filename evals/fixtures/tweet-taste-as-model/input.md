Source: https://x.com/itsreallyvivek/status/2065477778125062177
Author: @itsreallyvivek
Captured: 2026-06-13
Form: long-form X thread (single essay), pasted verbatim by the repo owner because x.com gates unauthenticated fetches (HTTP 402).

Original:

nobody flinches when you call debugging a skill. call taste a skill and the room gets uncomfortable, because taste is the one part of research we've agreed to treat as fate. you have it or you don't, and the people who have it were apparently issued it at birth, along with the right advisor. it's a comforting story, and it's wrong. taste is a model in your head that predicts which ideas will work before you've paid for them, and like every model, it's exactly as good as its training data and its training loop. both of those are under your control.

look at what taste is made of

in 1946, adriaan de groot showed chess grandmasters a midgame position for a few seconds and asked them to rebuild it from memory. they placed over ninety percent of the pieces. club players placed a fraction of that. the obvious conclusion is that masters have better memory, so chase and simon reran the experiment in the seventies with one change: the pieces were scattered at random. the grandmasters collapsed to nearly novice level.

the masters never had better memory. they had a library of tens of thousands of real positions, and a random board matched none of them. what looked like perception was retrieval. what looked like a gift was inventory.

that's the whole secret. when a senior researcher glances at your method and says "this won't survive a strong baseline," they're not channeling anything. they're matching your idea against a few thousand stored failures that rhyme with it. taste is a library, and a library is built by shelving, which is the one part of the job anyone can do.

predict before you peek

at the trinity test, enrico fermi stood in the observation bunker dropping scraps of paper. when the blast wave arrived, he watched how far it pushed them and estimated the yield at around ten kilotons, weeks before the instrument readings came back. the estimate was crude and roughly right, but the point was never accuracy. fermi made a guess before every measurement, on principle, because a measurement you predicted teaches you something a measurement you merely received never can: it grades your model of the world.

the original piece said to predict every experiment before you run it. the part that makes it work is writing the prediction down, with a number, before you look. an unwritten prediction is worthless, because your memory will quietly rewrite it to match the result, and you'll walk away feeling confirmed by an experiment that should have stung. psychologists call it hindsight bias. researchers call it "yeah, that's about what i expected," said after every result, forever.

so make it mechanical. before the run: expected delta, confidence, one sentence of reasoning. after the run: what actually happened, and which part of your reasoning broke. when you read a paper, stop at the end of the methods section and write down the numbers you expect in the tables. you will be wrong constantly. that's the product. each miss is a labeled example, and you're the model being trained.

keep score

philip tetlock spent two decades scoring expert predictions and found most experts performed near chance. the interesting part came later, in the good judgment project, where ordinary volunteers who practiced forecasting with strict scoring beat intelligence analysts who had access to classified information, by around thirty percent. the winners weren't smarter. they made granular predictions, got scored, and updated. judgment improved like a trained skill because it was treated like one.

the cleanest natural experiment is the weather. murphy and winkler found that when american forecasters say seventy percent chance of rain, it rains close to seventy percent of the time. meteorologists are among the best-calibrated professionals ever measured, and the reason is boring: they predict daily, in numbers, and reality grades them by morning. a pundit predicting elections gets feedback twice a decade and never writes the number down. same cognitive hardware, opposite training loop.

your research judgment is currently living one of these two lives. if you call which of this month's releases will matter and check the ledger a year later, you're the meteorologist. if you just have opinions in group chats, you're the pundit.

shrink the bet

there's a real objection here. kahneman and klein wrote a rare adversarial collaboration in 2009 asking when intuition can be trusted at all, and their answer was: only in environments with stable regularities and fast, clear feedback. firefighters and chess players develop real intuition. stock pickers develop confident noise. research looks like bad terrain for taste, because the feedback on a research bet can take two years to arrive and shows up confounded with compute, execution, and luck.

the answer isn't to give up on the loop. it's to shrink the bet until the loop closes. you can't get fast feedback on "is mechanistic interpretability the right decade-long direction," but you can get same-day feedback on "this ablation will cost two points," and same-week feedback on "this paper's gains won't replicate at larger scale." small predictions share machinery with big ones. calibrate where reality answers quickly, and the judgment transfers upward to the bets reality grades slowly.

trace the calls, not the credentials

when sutton wrote the bitter lesson, it read less like a prediction than a confession of one principle: general methods that ride compute beat clever methods that ride human insight, every time, eventually. when alec radford bet on generative pretraining for gpt-1, the field's energy was in task-specific supervised models, and the bet looked unfashionable. both calls came from the same place, and it wasn't a hunch. it was a small set of load-bearing beliefs, held explicitly, with a clear sense of what evidence would break them.

this is the upper floor of taste. the library gets you pattern-matching: this idea smells like the ones that died. principles get you the calls patterns can't reach, the ones about things nobody has tried yet. so when you study a great call, don't study the person. reconstruct the principle that generated it, then ask what your own load-bearing beliefs are. most researchers, asked to list them, produce the consensus of their timeline. that's not taste. that's an rss feed.

retrain on fresh data

in 2012, plenty of researchers with excellent judgment dismissed alexnet. their taste wasn't broken. it was trained on a decade where neural networks genuinely didn't work, and it kept predicting that decade after the data changed. taste is a model, and models drift. the better your library served you in the last regime, the more confidently it will fail you in the next one, which is why the people loudest about what can't work are so often the ones who were right last time.

the maintenance is the same as the training. keep predicting, keep scoring, and treat a string of surprises as a fire alarm rather than noise: when reality keeps beating your model, the model is stale, no matter how distinguished its past. hamming said knowledge compounds like interest. so does calibration, with one difference. interest never has to be marked down. your taste does, and the researchers who last are the ones who do the markdown themselves, before the field does it for them.

start the ledger this week. it will be embarrassing for six months. it was always going to be embarrassing for six months. the only question is whether you collect the data.
