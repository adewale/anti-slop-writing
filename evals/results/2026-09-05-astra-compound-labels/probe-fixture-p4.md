# Fresh fixture P4 — coinages that appear nowhere in either doctrine

Rollout gating relies on soft-quorum drains, so tenant-affinity pools never see a
partial config. Because the drain completes before the flip, a bad config is
caught in staging rather than in production.
