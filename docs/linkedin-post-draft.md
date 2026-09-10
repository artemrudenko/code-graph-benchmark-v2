# LinkedIn post draft

I kept noticing the same pattern while working with coding agents: they would trace a relationship in a codebase, then reopen the same files and rediscover it during the next task.

At first I treated this as a token problem. It is also a navigation and working-memory problem.

I started testing persistent code context: tools that can keep a map of symbols, callers, imports, and tests across repeated questions. The goal was not to name a winner. I wanted to understand what could be trusted when an agent is planning a change or refactor.

A few source checks changed the direction of the work:

- In Ktor, one caller query returned 17 results. Only one belonged to the requested parser; the other 16 belonged to another overload with the same name.
- In ripgrep, 24 of 28 callers were tests. The production and test impact needed to be separated.
- In FastAPI, changing only the indexing root changed the same reference lookup from 1 of 4 known references to 4 of 4.

So I stopped treating low output size as the result. A compact answer only helps when it preserves the relationship an agent needs to act on.

The current work is now a practical selection method: start from the questions that recur in your repository, record scope and setup, verify answers in source, test warm queries and refreshes after a change, then measure a full agent task. That is the point where a claim about saved context, time, or rework becomes meaningful.

The source-checked evidence and the pilot framework are here: https://github.com/artemrudenko/code-graph-benchmark-v2

What question does your coding agent keep re-investigating in the same repository?

---

Editorial note: add the final DEV article URL before publishing. Suggested attachment: `assets/diagrams/code-context-lifecycle.png` with the label “A codebase map is useful only if it stays accurate as code changes.” Keep this note out of the post.
