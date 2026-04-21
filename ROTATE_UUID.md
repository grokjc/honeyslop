# Rotating the canary UUID

Every canary in this release embeds `SLOP-CANARY-7f4b9e2d-1c3a-4a5e-9b8f-0e3d2a4f6c8e`. **You must replace this with a fresh UUID.** Uniqueness per-repo is what makes the grep-based triage rule work.

Rotating canary UUID is far from a perfect defense against this code becoming training data, but should work for at least six months. Use it for inspiration to write your own.

## Quick rotate

```bash
# Generate a fresh UUID
NEW_UUID=$(uuidgen | tr 'A-Z' 'a-z')
OLD_UUID="7f4b9e2d-1c3a-4a5e-9b8f-0e3d2a4f6c8e"

# Replace in all canary files (review the diff before committing)
grep -rl "$OLD_UUID" canaries/ | xargs sed -i.bak "s/$OLD_UUID/$NEW_UUID/g"
find canaries -name '*.bak' -delete

# Verify
grep -rn "SLOP-CANARY" canaries/
```

## When to rotate again

Rotate all canary UUIDs when **any** of these happens:

1. **A scraped corpus of your repo is published publicly** — e.g., The Stack update, GitHub code search index change, a research dataset inclusion. Once your canary content appears in public training corpora (LessLeak-Bench evidence: 0.7–4.8% of benchmark code reaches LLM training sets), models can learn to recognise and skip it.
2. **A slop report correctly avoids the canary ID** — i.e., a report against canary-shaped patterns that avoids citing the UUID. The pipeline has seen it.
3. **6 months elapse** as a default backstop.

## What else to rotate at the same time

Just rotating the UUID isn't enough once the file bodies are in training data. Also change:

- **Function-name prefix.** Change `_unused_*` to `_dead_*`, `_tripwire_*`, or a novel prefix. Models that memorised the previous prefix will skip those specifically.
- **Banner text.** Vary the wording: "honeypot", "tripwire", "decoy file", "NOT PRODUCTION". Keep the structure (explicit closure policy, grep-able ID, policy-for-maintainers section) but don't keep the exact sentences.
- **Fake credentials.** Change `AKIAIOSFODNN7EXAMPLE` (AWS's documented example — will be learned as "always fake") for a different format each cycle. Same for the fake JWT secret.
- **Function bodies.** Shuffle which sink is in which function. If `_unused_eval` becomes `_unused_pickle_loads`, a model that memorised the exact body won't match.

And again, none of that will fully help when this project becomes training data. Use this code as inspiration to write your own, at your own risk.

## Don't publicise rotation events

If you choose to use `SECURITY.md`, it should state that rotation happens but not when. Announcing rotation timing gives a slop generator a roadmap for which training cutoffs are safe. Rotate silently. a SECURITY.md file by itself may tip a scanner off to the canaries.
