# Card: Discharge the promise or cut it

## Before

```txt
Here's what most people get wrong about retries. Retrying is harder than it looks,
and the consequences of getting it wrong can be severe.
```

## After

```txt
Teams retry a charge endpoint that is not idempotent and bill the customer twice.
```

## Why it works

The teaser promises withheld content and the sentence after it never delivers — it restates
that retries are hard and asserts severity without naming a failure. Run the discharge test:
what payload does the line promise, and do the next one or two sentences supply it? Here the
answer is no, so the frame goes and the withheld thing gets said. Forward reference itself is
fine: `We report three robustness checks: held-out scoring, a paired bootstrap, and a
sign-flip permutation test` keeps its colon because the payload arrives in the same breath.
