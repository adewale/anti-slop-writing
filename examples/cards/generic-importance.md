# Card: Replace importance with mechanism

## Before

```txt
This underscores the importance of durable execution.
```

## After

```txt
The workflow can fail on step 4, retry only that step, and keep the previous outputs.
```

## Why it works

The rewrite names the behavior that makes execution durable. It no longer asks the reader to accept importance as a substitute for evidence.
