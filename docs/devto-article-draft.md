---
# DEV publishing: upload assets/images/cover-broken-edge.png as the cover image.
title: "I wanted my coding agent to stop re-reading the same code"
published: false
tags: ai, llm, developertools, opensource
description: "I was looking for a reusable map of a codebase, not a leaderboard. Here is what I tested, what the evidence says, and how I would choose a tool for daily work."
---

An AI coding agent can trace a function today, then reopen the same files and rediscover the same relationships tomorrow.

At first I called that a token problem. It is also a navigation and memory problem. When an agent has to repeatedly answer “what calls this?”, “what breaks if I change it?”, and “which tests cover it?”, work becomes slower and changes become harder to reason about.

I started looking for a reusable map of a codebase: something an agent could query across a session and after a pause, instead of rebuilding its understanding from file reads. I did **not** need a tool to win a leaderboard. I needed a tool, or a small combination of tools, that could be trusted during real changes and refactors.

That changed how I read my own earlier comparison. A short answer is valuable only if it keeps the relationship needed to act. A short wrong caller list is worse than a long source search.

![A code-context lifecycle: first configure scope and build a reusable index; then ask recurring questions about symbols, callers, paths, and tests; check the source before acting; after code changes, refresh the index and repeat.](https://raw.githubusercontent.com/artemrudenko/code-graph-benchmark-v2/main/assets/diagrams/code-context-lifecycle.png)

## What "code context" means here

There is no single kind of code-context tool. They solve different parts of the same workflow.

| What I need | Plain-language job | Tool class | Examples |
|---|---|---|---|
| Read a bounded area | Put selected files or a module into the agent's context | Context packager | Repomix |
| Navigate a symbol | Ask the project's language tooling for definitions, references, or rename support | IDE language-server bridge | Serena |
| Follow relationships | Keep an index of code entities and links such as calls and imports | Parsed-code or graph index | code-review-graph, codebase-memory-mcp, graphify |
| Change a repeated code shape | Find syntax patterns and apply a constrained transformation | Structural pattern tool | ast-grep |

An **AST** (abstract syntax tree) is simply the parsed structure of code: functions, classes, calls, imports, and their positions, rather than raw text. An **LSP** (language server protocol) is the language tooling behind an IDE's “go to definition” and “find references.” Both can help an agent, but neither replaces source checks when the project setup or target is ambiguous.

A packer is useful for a bounded reading task. An LSP can be strong at symbol navigation. A graph index can support repeated relationship queries. A pattern tool can make a mechanical change. Treating these as one race produces a neat chart and a bad buying decision.

## The questions an agent keeps asking

I now start selection from the questions that recur during work, not from a list of tool names.

| Repeated question | What a usable answer needs |
|---|---|
| What does this symbol do? | The exact definition and its local responsibility |
| Who uses it? | Callers or references tied to the right definition |
| What is the change radius? | A bounded set of affected modules and entry points |
| How does execution reach it? | A path across handlers, adapters, and boundaries |
| Which tests protect it? | Test relationships separated from production impact |
| What did this change affect? | Connections that make a code review actionable |

Before any of these, I ask two smaller questions: **is this the exact target?** and **did the tool search the repository, module, and build configuration I intended?**

![Four tool classes shown by job: pack a bounded context; navigate a symbol; follow repeated code relationships; find or transform a syntax pattern. All return to source checks when an answer is uncertain.](https://raw.githubusercontent.com/artemrudenko/code-graph-benchmark-v2/main/assets/diagrams/code-context-tool-jobs.png)

## Why I tried several tools

I was not comparing six interchangeable products. I was checking whether different ways of building context could answer the questions above without making an agent confidently wrong.

The persistent tools I exercised in the current evidence pack take different routes to the same apparent answer. An index may join nodes by name. A language server resolves symbols within a project configuration. A natural-language graph query may offer nearby code when it has no exact match. The answer can look equally compact in each case while meaning something very different.

## What the source checks found

I kept four findings because each is independently checked against source at a pinned commit. They are not a ranking.

| Check | Tool response | Source-checked result | Why it matters in daily work |
|---|---|---|---|
| Ktor function name collision | code-review-graph returned 17 callers | 1 caller belonged to the low-level parser; 16 belonged to a public overload with the same name | A name is not an identity. Confirm the definition before estimating refactor impact. |
| ripgrep test boundary | code-review-graph returned 28 callers | 24 were test functions; 4 were production functions | “All callers” needs a test/production split. |
| Deliberately absent symbols | graphify gave a related result in 3 of 12 fixed canary queries | 9 returned a clear no-match response | An approximate suggestion must not look like an exact match. |
| FastAPI indexing scope | Serena found 1 of 4 known references from a nested package root | The same commit returned 4 of 4 when indexed from repository root | Setup is part of the answer, not housekeeping. |

![Four source-checked observations: Ktor 17 results versus 1 real caller; ripgrep 28 callers split into 24 tests and 4 production; graphify 3 substitutions out of 12 absent-symbol checks; Serena 4 of 4 references at repository root versus 1 of 4 at a nested package root.](https://raw.githubusercontent.com/artemrudenko/code-graph-benchmark-v2/main/assets/diagrams/evidence-at-a-glance.png)

The Ktor case is the one that made the problem concrete. The low-level `parseHeaderValue` function has one real caller, `parseHeaders`. code-review-graph returned that caller plus 16 real calls to another `parseHeaderValue` overload. The response was compact and almost entirely wrong for the requested target.

![Ktor's low-level parser has one real incoming caller, parseHeaders. A graph query returned it plus 16 callers of a different public overload.](https://raw.githubusercontent.com/artemrudenko/code-graph-benchmark-v2/main/assets/diagrams/ktor-caller-disambiguation.png)

None of this means that graph or LSP tools are a bad idea. It means their answers need a trust contract: exact target, correct scope, explicit test boundary, and a distinction between exact match, candidate, and no match.

## The cost that matters is a lifecycle

A persistent index has a cost before the first question: installation, project configuration, scope choice, and a build. It has another cost when code changes: refresh or rebuild. Its payoff appears only if it saves repeated work afterward.

That is why I no longer use a single score made from answer tokens and a quality judgment. It mixes things that should stay separate: one-time setup, warm queries, rebuilds, different question types, and whether the agent completed the actual task correctly.

The current evidence does **not** show that an agent uses fewer total tokens, finishes faster, or writes a better patch. It only shows that compact retrieval can preserve or lose important relationships. I would need a fixed end-to-end change task, the same project configuration, source checks, test results, and a record of retries before claiming a payoff.

## How I would choose a tool for a real codebase

I would run a small pilot on the repository where the tool will live.

1. Pick three recurring tasks from active work, including one ordinary lookup and one hard target: an overload, a build-tagged implementation, generated boundary, or test-heavy API.
2. Write the source-grounded expected answer before running a tool. Decide whether tests count and whether “caller” means a call expression or a distinct calling function.
3. Record the project root, dependencies, exclusions, build flags, index time, and errors. This makes the setup repeatable.
4. Keep each raw answer and check it in source before an agent uses it to plan a change.
5. Repeat the queries while the index is warm. Then make a small code change, refresh the index, and check one affected relationship again.
6. Only then let an agent complete a fixed change task and compare total context, time, retries, tests, and patch correctness.

The outcome should be a capability profile: which tool earns trust for which recurring question in this codebase, what it needs to stay fresh, and when the agent should fall back to reading source. It may be one tool. It may be a small stack.

![Before acting on compact code context, check the exact symbol, indexed scope, test boundary, and whether the response is an exact match, a candidate, or no match.](https://raw.githubusercontent.com/artemrudenko/code-graph-benchmark-v2/main/assets/diagrams/retrieval-trust-checks.png)

The [public evidence archive](https://github.com/artemrudenko/code-graph-benchmark-v2) contains the [source-checked cases](https://github.com/artemrudenko/code-graph-benchmark-v2/blob/main/docs/evidence-index.md), [reproduction details](https://github.com/artemrudenko/code-graph-benchmark-v2/blob/main/docs/reproducibility-manifest.md), and the full [selection and pilot framework](https://github.com/artemrudenko/code-graph-benchmark-v2/blob/main/docs/selection-and-evaluation-framework.md). It does not claim a universal winner or a measured token saving.

My result so far is narrower, and more useful: persistent code context is worth testing as a working memory for an agent, but it must be configured, verified, refreshed, and chosen by the work it will actually do.

What question does your coding agent keep re-investigating in the same repository?
