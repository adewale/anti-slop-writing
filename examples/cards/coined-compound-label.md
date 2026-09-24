# Card: A name is not a mechanism

## Before

```txt
The indexer runs exact-head checks before each merge, so editorial-row layouts
stay consistent across shards.
```

## After

```txt
Ask author: what does the check compare, and by what operation? What is an
editorial-row layout?

Fallback until answered: The indexer runs its check before each merge, so drift
between replicas surfaces at merge time instead of at read time.
```

## Why it works

`exact-head checks` reads as sharp detail because it is hyphenated and specific
in shape. The reader cannot resolve it: the term is not standard in the domain
and the paragraph never defines it, so the consistency claim rests on a name.
The fallback drops the claim the source never supported rather than inventing a
definition to make the sentence sound sharper. The visible hole is the honest
form of the gap.

## Boundary

Do not read this as a rule against hyphenated terms. `write-ahead log` and
`copy-on-write` are standard, and a coinage defined in the sentence that
introduces it — "we call this an exact-head check: the indexer hashes the head
revision on both replicas and refuses the merge when they differ" — is earned on
first use.
