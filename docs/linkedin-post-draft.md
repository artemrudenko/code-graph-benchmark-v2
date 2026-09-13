# LinkedIn post draft

**Status:** Prepare now. Publish only after the DEV article is public and replace the link placeholder below.

I wanted coding agents to stop re-reading the same code in every session.

In one FastAPI control, the same reference lookup found 1 of 4 known references to `solve_dependencies`.

I changed only the index root: from a nested package to the repository root.

It found all 4.

The source did not change. The symbol did not change. The setup did.

That was a useful reminder: a code index can make navigation faster, but it is not authority. Before an agent uses a relationship to plan a change, it still needs to know:

- the exact symbol;
- the indexed scope;
- whether the index is fresh; and
- what the current source says.

I wrote down four cases I checked against source code: an index with the wrong scope, test callers that look like production impact, an absent symbol that received related suggestions, and a stale index.

The goal was not to rank tools or make token-saving claims. It was to find a safer way to give an agent reusable code context.

Read the full article: **[replace with public DEV URL]**

If you use a code graph with an agent, does it show which revision it knows and what it did not index?
