Naive baseline rewrite — no skill applied. Model: claude-opus-4-8 (Opus 4.8), self-reported.
Prompt: tighten and de-AI the essay; do NOT read anything under skills/.

---

Nobody flinches when you call debugging a skill. Call taste a skill and the room tightens, because taste is the one part of research we've agreed to treat as fate. You have it or you don't, and whoever has it was issued it at birth along with the right advisor. Comforting story. Also wrong. Taste is a model in your head that predicts which ideas will work before you've paid to find out, and like any model it's only as good as its training data and its training loop. You control both.

Start with what taste is made of.

In 1946, Adriaan de Groot flashed chess grandmasters a midgame position for a few seconds and asked them to rebuild it from memory. They placed over ninety percent of the pieces; club players placed a fraction. Better memory, obviously. So in the seventies Chase and Simon reran it with one change: the pieces scattered at random. The grandmasters dropped to near-novice.

They never had better memory. They had a library of tens of thousands of real positions, and a random board matched none of them. What looked like perception was retrieval. What looked like a gift was inventory.

That's the whole secret. When a senior researcher glances at your method and says "this won't survive a strong baseline," she isn't channeling anything. She's matching your idea against a few thousand stored failures that rhyme with it. Taste is a library, and a library is built by shelving, which is the one part of the job anyone can do.

Predict before you peek.

At the Trinity test, Enrico Fermi stood in the bunker dropping scraps of paper. When the blast wave hit, he watched how far it shoved them and called the yield at around ten kilotons, weeks before the instruments reported. Crude, roughly right, and accuracy was never the point. Fermi guessed before every measurement on principle, because a measurement you predicted teaches you something a measurement you merely receive cannot: it grades your model of the world.

Predicting every experiment before you run it is old advice. The part that does the work is writing the prediction down, with a number, before you look. An unwritten prediction is worthless, because your memory will quietly edit it to match the result and you'll walk away confirmed by an experiment that should have stung. Psychologists call it hindsight bias. Researchers call it "yeah, about what I expected," said after every result, forever.

So make it mechanical. Before the run: expected delta, confidence, one sentence of why. After: what happened, and which part of the why broke. Reading a paper, stop at the end of the methods and write the numbers you expect in the tables. You'll be wrong constantly. That's the product. Each miss is a labeled example, and you're the model being trained.

Keep score.

Philip Tetlock spent two decades scoring expert predictions and found most experts landed near chance. The interesting part came later. In the Good Judgment Project, ordinary volunteers who practiced forecasting under strict scoring beat intelligence analysts with access to classified material, by around thirty percent. The winners weren't smarter. They made granular predictions, got scored, and updated. Judgment improved like a trained skill because they trained it like one.

The cleanest case is weather. Murphy and Winkler found that when American forecasters say seventy percent chance of rain, it rains close to seventy percent of the time. Meteorologists are among the best-calibrated professionals ever measured, for a boring reason: they predict daily, in numbers, and reality grades them by morning. A pundit forecasting elections gets feedback twice a decade and never writes the number down. Same hardware, opposite loop.

Your research judgment is already living one of these lives. Call which of this month's releases will matter, then check the ledger a year out, and you're the meteorologist. Just have opinions in group chats, and you're the pundit.

Shrink the bet.

There's a real objection. In a rare 2009 adversarial collaboration, Kahneman and Klein asked when intuition can be trusted at all. The answer: only in environments with stable regularities and fast, clear feedback. Firefighters and chess players develop real intuition. Stock pickers develop confident noise. Research looks like bad terrain for taste, since a research bet can take two years to resolve and arrives confounded with compute, execution, and luck.

The fix isn't to abandon the loop. It's to shrink the bet until the loop closes. You can't get fast feedback on "is mechanistic interpretability the right decade-long direction." You can get same-day feedback on "this ablation costs two points," and same-week feedback on "these gains won't replicate at larger scale." Small predictions share machinery with big ones. Calibrate where reality answers fast, and the judgment transfers up to the bets reality grades slowly.

Trace the calls, not the credentials.

Sutton's bitter lesson reads less like a prediction than a confession of one principle: general methods that ride compute beat clever methods that ride human insight, eventually, every time. When Alec Radford bet on generative pretraining for GPT-1, the field's energy was in task-specific supervised models and the bet looked unfashionable. Both calls came from the same place, and it wasn't a hunch. It was a small set of load-bearing beliefs, held explicitly, with a clear sense of what evidence would break them.

This is the upper floor of taste. The library gets you pattern-matching: this idea smells like the ones that died. Principles get you the calls patterns can't reach, the ones about things nobody has tried. So when you study a great call, don't study the person. Reconstruct the principle that generated it, then ask what your own load-bearing beliefs are. Most researchers, asked to list theirs, recite the consensus of their timeline. That isn't taste. That's an RSS feed.

Retrain on fresh data.

In 2012, plenty of researchers with excellent judgment dismissed AlexNet. Their taste wasn't broken. It was trained on a decade where neural networks genuinely didn't work, and it kept predicting that decade after the data changed. Taste is a model, and models drift. The better your library served you in the last regime, the more confidently it fails you in the next, which is why the people loudest about what can't work are so often the ones who were right last time.

Maintenance is just more training. Keep predicting, keep scoring, and treat a run of surprises as a fire alarm, not noise. When reality keeps beating your model, the model is stale, however distinguished its past. Hamming said knowledge compounds like interest. So does calibration, with one difference: interest never gets marked down. Your taste does, and the researchers who last are the ones who do the markdown themselves, before the field does it for them.

Start the ledger this week. It'll be embarrassing for six months. It was always going to be embarrassing for six months. The only question is whether you collect the data.
