# LinkedIn post draft

The code graph said 17 functions called a parser. The source had one.

I was testing whether compact code context is safe enough for an AI agent to act on. A short result can save context, but only if it keeps the relationship that matters.

I checked 14 retrieval runs across 12 repositories and found four questions I now ask before trusting the answer:

1. Did it resolve the exact function?
2. Did the index cover the right repository and module?
3. Are production callers and test callers separated?
4. Is this an exact match or only a related suggestion?

In the Ktor case, 16 of 17 reported callers belonged to another overload. In ripgrep, 24 of 28 callers were tests. A FastAPI control changed the same lookup from 1 of 4 references to 4 of 4 by indexing the repository root.

This does not measure whether an agent finishes work faster or better. It shows why a low token count is not enough evidence that the context is safe.

The full article and source-checked evidence archive are linked below.

What do you check before trusting a "no callers found" answer from an AI coding tool?

---

Editorial note: add the verified article and evidence-repository links before publishing. Keep this note out of the post. Suggested attachment: the Ktor diagram, labelled "Expected: 1 caller / Returned: 1 correct + 16 unrelated." Do not present it as a screenshot of the tool.
