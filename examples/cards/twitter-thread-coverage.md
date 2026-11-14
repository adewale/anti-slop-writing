# Hollow modifiers and self-planted strawmen — coverage only

Synthetic examples from PR #17, now in `evals/twitter-evals.json`. They illustrate
existing specificity/non-invention guidance; no detector or installed reference changed.
The suite keeps five tune and three **public historical** holdout labels. Its shared
thread/scaffold is one conservative source family, not eight independent validations.

## Unestablished comparison

**Before:** “My actual recommendation is to ship the migration behind a flag. The real
reason is that the backfill takes eleven hours and cannot be paused once it starts.
The key issue is deciding who owns the rollback.”

The task specifies that nothing precedes this opening: no competing recommendation,
misleading reason or ranking was established.

**After:** “I recommend shipping the migration behind a flag. The backfill takes eleven
hours and cannot be paused once it starts. Decide who owns the rollback.”

The source's duration and interruption limit remain; the edit does not replace hollow
emphasis with invented measurements or an invented reason for the flag.

## An answer refutes its own invention

**Before:** User: “Should I add an index on user_id?” Reply: “The instinct in cases like
this is to reach for a bigger instance. But throwing hardware at it is not the fix.
The fix is an index on user_id, which turns the sequential scan over 40 million rows
into a lookup.”

The task supplies no user proposal about hardware or scaling up.

**After:** “Add an index on user_id. It turns the sequential scan over 40 million rows
into a lookup.”

This retains the draft's supplied mechanism, not an independently verified benchmark.
It adds neither a latency claim nor a position for the user to have held. The suite's
counterexamples also retain negation that answers an actual user hypothesis, measured
vs advertised distinctions, and a key issue supported by an explicit ranking. Merely
containing “actual,” “not” or “key” is not an automatic failure.

Prepare an isolated worklist without exposing expected assertions to the apply worker:

```bash
python3 scripts/run_evals.py prepare evals/twitter-evals.json --split tune \
  --out /tmp/twitter-apply.json --judge-out /tmp/twitter-judge.json
```

This prepares worklists only; it makes no model calls. The candidate screen reports its
current/no-skill results separately. These new files are case/example coverage, not a
claim that a new behavior passed an improvement gate.
