# Card: Cut the premise nobody raised

## Before

The user's whole message was `why is the deploy slow?`. They never mentioned Docker.

```txt
It would be easy to assume the slowness comes from the Docker build. But the build is not the problem. The problem is that the readiness probe waits a fixed 30 seconds before its first check, so every rollout pays that delay once per pod.
```

## After

```txt
The readiness probe waits a fixed 30 seconds before its first check, so every rollout pays that delay once per pod.
```

## Why it works

The correction has nobody to correct. The writer introduced the Docker build, refuted it, and kept the shape of a rebuttal, which tells the reader — falsely — that they were about to believe something.

The staccato contrast test does not reach this. It asks whether the prior prose evidences both sides, and the writer's own setup sentence supplies the Docker side, so the contrast can pass as earned. Grade it `compressed` instead and the prescribed repair is worse: naming the unsupported side directly sends you to go evidence a build nobody asked about. The classification is about evidence; the defect is about provenance.

Keep the negation when the alternative came from the reader. Asked `is this a memory leak?`, the answer should still open `This is not a memory leak` — dropping it leaves the question hanging.
