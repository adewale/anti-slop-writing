# Card: Delete the modifier, do not upgrade it

## Before

```txt
My actual recommendation is to ship the migration behind a flag. The real reason is that the backfill takes eleven hours and cannot be paused once it starts.
```

## After

```txt
My recommendation is to ship the migration behind a flag. The backfill takes eleven hours and cannot be paused once it starts.
```

## Why it works

Drop `actual` and `real` and nothing about the recommendation or the reason changes, which is the test. What they were adding was an implication: that an earlier recommendation had been offered and was not the genuine one. Nothing precedes the paragraph, so the alternatives they point at do not exist.

The repair runs opposite to the usual one. A prestige adjective inflates its noun and is fixed by naming a mechanism, which adds words. A hollow modifier says nothing about its noun, so the fix is deletion and the line gets shorter. A rewrite that grows to justify `actual` has gone the wrong way.

Keep the word when the alternative is on the page. After a paragraph quoting a vendor's advertised p99 of 40 ms, `The actual p99 during the incident was 2.3 seconds` needs it.
