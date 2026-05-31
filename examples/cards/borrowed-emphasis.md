# Card: Flatten the cadence to find the idea

## Before

```txt
Durable execution isn't just retry logic. It is a new programming model.
```

## After

```txt
Durable execution lets a workflow fail on step 4, retry only that step, and keep the previous outputs, so the programmer writes against a runtime that records state instead of a function that returns once.
```

## Why it works

Flatten the "isn't just X. It is Y" cadence in the original and the claim disappears. The rewrite sources its emphasis from a named mechanism — step-level retry and preserved outputs — rather than from contrast rhythm.
