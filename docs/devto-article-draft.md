---
# DEV publishing: upload assets/images/cover-broken-edge-dev.png as the cover image.
title: "I wanted my coding agent to stop re-reading the same code"
published: false
tags: ai, llm, developertools, opensource
description: "I was looking for a reusable map of a codebase, not a leaderboard. Here is what I tested, what the evidence says, and how I would choose a tool for daily work."
---

An AI coding agent can trace a function today, then reopen the same files and find the same relationships again tomorrow.

At first I saw this as a token problem. It is also a navigation and memory problem. The agent keeps asking: “What calls this?”, “What breaks if I change it?”, and “Which tests cover it?” Repeating that work makes changes slower and harder to check.

**My goal was simple:** find a dependable way to give an agent reusable context about a codebase. I want less repeated searching, safer plans for changes and refactors, and a clear rule for when an index is worth keeping fresh.

I was not trying to name a winning tool. I wanted a tool, or a small set of tools, that I could trust during real work. A short answer is useful only when it keeps the relationship needed to act. A short list of the wrong callers is worse than a longer source search.

![A code-context lifecycle: first configure scope and build a reusable index; then ask recurring questions about symbols, callers, paths, and tests; check the source before acting; after code changes, refresh the index and repeat.](https://raw.githubusercontent.com/artemrudenko/code-graph-benchmark-v2/main/assets/diagrams/code-context-lifecycle.png)

## What "code context" means here

There is no single kind of code-context tool. Different tools help with different parts of the same work.

| What I need | Plain-language job | Tool class | Examples |
|---|---|---|---|
| Read a limited area | Put selected files or a module into the agent's context | Context packager | Repomix |
| Navigate a symbol | Ask project language tools for definitions, references, or rename support | IDE language-server bridge | Serena |
| Follow relationships | Keep an index of code entities and links such as calls and imports | Parsed-code or graph index | code-review-graph, codebase-memory-mcp, graphify |
| Change a repeated code shape | Find a syntax pattern and make a limited transformation | Structural pattern tool | ast-grep |

An **AST** (abstract syntax tree) is the parsed structure of code: functions, classes, calls, imports, and their positions. It is more than raw text. An **LSP** (language server protocol) is the language tooling behind an IDE's “go to definition” and “find references.” Both can help an agent, but neither removes the need to check source when the project setup or target is unclear.

A packer helps with a focused reading task. An LSP can help find a symbol. A graph index can support repeated relationship questions. A pattern tool can make a mechanical change. Putting them in one ranking gives a neat chart, but it can lead to a bad choice.

## The questions an agent keeps asking

I now start with the questions that repeat during work, not with a list of tool names.

| Repeated question | What a usable answer needs |
|---|---|
| What does this symbol do? | The exact definition and its local responsibility |
| Who uses it? | Callers or references for the right definition |
| What is the change radius? | A small, relevant set of affected modules and entry points |
| How does execution reach it? | A path across handlers, adapters, and boundaries |
| Which tests protect it? | Test relationships separated from production impact |
| What did this change affect? | Connections that make a code review useful |

Before any of these, I ask two smaller questions: **Is this the exact function or class?** And: **Did the tool search the repository, module, and build configuration I intended?**

![Four tool classes shown by job: pack a bounded context; navigate a symbol; follow repeated code relationships; find or transform a syntax pattern. All return to source checks when an answer is uncertain.](https://raw.githubusercontent.com/artemrudenko/code-graph-benchmark-v2/main/assets/diagrams/code-context-tool-jobs.png)

## Why I tried several tools

These tools are not all direct competitors. I tried several because each builds context in a different way, and each can fail in a different way.

A graph index may connect code by name. A language server resolves symbols inside a project configuration. A natural-language graph query may offer related code when it has no exact match. Each answer can look short and convincing while meaning something different.

The public archive contains a broader exploration. This article keeps only four cases that I checked again against a fixed version of the source code. They explain the limits that matter when an agent uses compact context to plan a change.

## What the source checks found

These four checks are observations, not a ranking.

| Check | Tool response | Source-checked result | Why it matters in daily work |
|---|---|---|---|
| Ktor function name collision | code-review-graph returned 17 callers | 1 caller belonged to the low-level parser; 16 belonged to a public overload with the same name | A name is not an identity. Confirm the definition before estimating refactor impact. |
| ripgrep test boundary | code-review-graph returned 28 callers | 24 were test functions; 4 were production functions | “All callers” needs a test/production split. |
| Deliberately absent symbols | graphify returned related code in 3 of 12 fixed queries for symbols that do not exist | 9 returned a clear no-match response | A related suggestion must not look like an exact match. |
| FastAPI indexing scope | Serena found 1 of 4 known references from a nested package root | The same code version returned 4 of 4 when indexed from repository root | Setup is part of the answer, not housekeeping. |

![Four source-checked observations: Ktor 17 results versus 1 real caller; ripgrep 28 callers split into 24 tests and 4 production; graphify 3 substitutions out of 12 absent-symbol checks; Serena 4 of 4 references at repository root versus 1 of 4 at a nested package root.](https://raw.githubusercontent.com/artemrudenko/code-graph-benchmark-v2/main/assets/diagrams/evidence-at-a-glance.png)

The Ktor case made the problem concrete. The low-level `parseHeaderValue` function has one real caller: `parseHeaders`. code-review-graph returned that caller plus 16 real calls to another public `parseHeaderValue` function. The response was compact and almost entirely wrong for the target I asked about.

![Ktor's low-level parser has one real incoming caller, parseHeaders. A graph query returned it plus 16 callers of a different public overload.](https://raw.githubusercontent.com/artemrudenko/code-graph-benchmark-v2/main/assets/diagrams/ktor-caller-disambiguation.png)

This does not mean graph or LSP tools are a bad idea. It means an answer needs a trust contract: the exact target, the right search scope, a clear test boundary, and a label that says whether the result is an exact match, a possible match, or no match.

## What I trust in these results

I used an LLM judge in an earlier experiment. A Sonnet model read each tool answer and gave it a quality score against a plain file-reading answer. That helped me find questions worth testing. It did not prove that an answer was correct.

An LLM judge can prefer an answer that is short or well written. It can miss that the answer names the wrong function. It can also repeat a mistake in the comparison answer it received. The older scorecard also mixed different tool types, setup costs, and response formats in one ranking. The files needed to recheck every old quality score are not all part of this public evidence pack. I no longer use those scores or its winners as evidence.

For this article, I use a stricter rule. Every number above has:

- a fixed repository and code version;
- saved raw tool output;
- a separate source check in a fresh clone of the repository; and
- the exact query and indexed scope written down.

This is why I trust these four observations. It is not enough to say which tool is best in every repository, how many total tokens an agent saves, or whether it will finish a change correctly.

## The cost that matters is a lifecycle

A persistent index has a cost before the first question: installation, project configuration, scope choice, and a build. It has another cost after code changes: refresh or rebuild. Its value appears only if it saves repeated work after that.

The next step is not another headline score. It is a fixed end-to-end change task with the same project configuration, source checks, test results, and a record of retries. Only that can show whether a maintained index saves time or total context in daily work.

## How I would choose a tool for a real codebase

I would run a small pilot in the repository where the tool will live.

1. Pick three recurring tasks from active work. Include one ordinary lookup and one hard target: an overload, a build-tagged implementation, generated code, or a test-heavy API.
2. Write the expected answer from source before running a tool. Decide whether tests count and whether “caller” means a call location or a distinct calling function.
3. Record the project root, dependencies, exclusions, build flags, index time, and errors. This makes the setup repeatable.
4. Keep every raw answer and check it in source before an agent uses it to plan a change.
5. Repeat the questions while the index is warm. Then make a small code change, refresh the index, and check one affected relationship again.
6. Only then let an agent complete one fixed change task. Compare total context, time, retries, tests, and patch correctness.

The outcome should be a capability profile: which tool earns trust for which recurring question in this codebase, what it needs to stay fresh, and when the agent should fall back to reading source. It may be one tool. It may be a small stack.

![Before acting on compact code context, check the exact symbol, indexed scope, test boundary, and whether the response is an exact match, a candidate, or no match.](https://raw.githubusercontent.com/artemrudenko/code-graph-benchmark-v2/main/assets/diagrams/retrieval-trust-checks.png)

## My conclusion

Persistent code context is worth testing as working memory for an agent. It can reduce repeated investigation and make relationship questions easier to ask. But it must be configured, checked, refreshed, and chosen for the work the agent will actually do.

The [public evidence archive](https://github.com/artemrudenko/code-graph-benchmark-v2) contains the [source-checked cases](https://github.com/artemrudenko/code-graph-benchmark-v2/blob/main/docs/evidence-index.md), [reproduction details](https://github.com/artemrudenko/code-graph-benchmark-v2/blob/main/docs/reproducibility-manifest.md), and the full [selection and pilot framework](https://github.com/artemrudenko/code-graph-benchmark-v2/blob/main/docs/selection-and-evaluation-framework.md). It does not claim a universal winner or a measured token saving.

What question does your coding agent keep re-investigating in the same repository?
