---
# DEV publishing: upload assets/images/cover-broken-edge-dev.png as the cover image.
title: "My coding agent kept re-reading code. I tested code indexes."
published: false
tags: ai, llm, developertools, agents
description: "A plain-language guide to testing a code index before an AI coding agent uses it to plan a change."
---

I wanted a coding agent to stop rediscovering the same code on every task.

A persistent code index seemed like an answer. It is a saved map of a codebase: where definitions live, who calls them, and which files are connected. An agent can start from that map instead of opening the same files again.

Then I ran a small FastAPI check. On the same source version, one lookup found only 1 of 4 known references to a dependency helper. I changed only where the index started: from a nested package to the repository root. It found all 4.

Nothing in the code changed. The index setup did.

That became the question for this article: **can an index help an agent navigate a codebase without becoming a second source of mistakes?**

My answer is modest. A code index can work as reusable memory. It does not replace current source. Before an agent uses an answer to plan or edit code, it still needs the exact target, the scope of the index, its freshness, and a source check.

I use four source-checked cases as a short tutorial: an index rooted in the wrong folder, callers mixed with tests, an absent symbol that received related suggestions, and an index that became old after a source change. They are observations, not a ranking.

## The problem: repeated questions, repeated searching

Most code changes start with a few ordinary questions:

- What does this function or class do?
- Who uses this exact definition?
- Which callers are tests, and which are production code?
- What will a change affect?
- Is the information still current?

A parser can turn code into an abstract syntax tree (AST): a structured view of functions, imports, and calls. A code index saves some of those relationships for later queries. That can save navigation time. It cannot prove that a result is complete, current, or about the definition you meant.

The safe loop is simple: configure the index, use it to find a starting point, check the source before acting, then refresh after code changes.

![A code-context lifecycle: configure scope and build an index; ask about symbols, callers, paths, and tests; check source before acting; refresh after code changes.](https://raw.githubusercontent.com/artemrudenko/code-graph-benchmark-v2/main/assets/diagrams/code-context-lifecycle-article-large-dark.png)

## First check: did the index see the whole repository?

The FastAPI control made this question concrete. `solve_dependencies` has four reference sites in the pinned source: three in `fastapi/routing.py` and one recursive call in `fastapi/dependencies/utils.py`.

I indexed the same pinned commit twice. The symbol and query stayed the same. Only the project root changed.

| Index root | Source-checked result |
|---|---|
| Nested `fastapi/` package | Serena found 1 of 4 reference sites. |
| Repository root `.` | Serena found all 4 reference sites. |

![FastAPI project-root control: with the same pinned commit and solve_dependencies lookup, a nested fastapi package root found 1 of 4 reference sites; the repository root found all 4. Only the index root changed.](https://raw.githubusercontent.com/artemrudenko/code-graph-benchmark-v2/7408b5fac5f27fa7496a7d5e35cc1fded1336aba/assets/diagrams/fastapi-project-root-control.png)

The incomplete answer looked reasonable. Its scope was incomplete. The lesson is simple: **project setup is part of the answer.** Before trusting a reference count, check that the tool started at the repository root and knows your language configuration.

## Three more checks before an agent acts

The FastAPI result was one kind of problem. I kept three more checks because they answer common questions an agent will meet during a refactor.

| Question to test | What I observed in a fixed source version | Rule it led to |
|---|---|---|
| Does a caller list separate tests from production? | In the ripgrep repository, code-review-graph returned 28 calling functions for `Ignore::add_child`: 24 test functions and 4 production functions. | Split tests from production before impact analysis. |
| Does a related result mean an exact result? | In 3 of 12 deliberate absent-symbol checks, graphify returned unrelated but plausible code instead of `not found`. The other 9 answers clearly said no match. | A related item is a candidate, not a found symbol. |
| Does the index notice a source change? | After a local change added a fifth direct caller in FastAPI, old graphs missed the new relationship. | Refresh the index or check current source before a change that depends on callers. |

Each case points to the same four checks: exact target, search scope, test boundary, and a clear status such as **verified**, **candidate**, **not found**, or **stale**.

## A map can become old

An index can be correct when it is built and wrong after the source changes.

For a small control, I built indexes while the FastAPI helper had four direct callers. Then I added a fifth caller in a local test change and asked the same question before refresh. The old graph did not include the new relationship. After the documented refresh path, the tools found it. This local change is not presented as FastAPI history.

The graph counts differ by tool: one omits the recursive self-call and another groups callers. The source result was consistent: after the change, there were five direct callers.

![A stale-index control: build an index when source has four callers; source changes to five callers; the old graph misses the new relationship; compare freshness, check current source, then refresh the index before relying on it.](https://raw.githubusercontent.com/artemrudenko/code-graph-benchmark-v2/main/assets/diagrams/stale-index-control-article-large-dark.png)

I also ran one small rename task in three fresh sessions: no index, Graphify with the old graph, and Graphify rebuilt on the changed source. Each session passed the same deterministic evaluator once. In the stale-graph session, the graph missed the fifth caller, but the agent checked current source and updated all five.

This is a narrow control. It does not show that stale indexes are safe, that a tool improves an agent, or that a setup saves tokens. It supports one rule: **use a graph to find a starting point; use current source to decide a change.** The [normalized control record](https://github.com/artemrudenko/code-graph-benchmark-v2/blob/main/docs/stale-index-control.md) describes the exact boundary.

## How I checked the answers

An earlier experiment used an LLM judge. A Sonnet model compared tool answers with plain file-reading answers and gave them quality scores. That helped me find questions worth checking. It did not prove that an answer was correct.

For this article, the LLM helped screen questions. Source code decided the result. Each public number above has a fixed repository and revision, saved raw tool output, a separate source check in a fresh clone, and the recorded query and index scope.

The stale-index control has a fixed task and deterministic evaluator, but its raw records remain private because they contain local-path metadata. The article does not claim token savings or better final agent quality.

## A small tutorial: test a code index in your repository

You do not need a large benchmark. A clean clone, a few fixed questions, and a separate source check can tell you whether a candidate tool helps in your repository.

1. Start with the source answer. Pick a pinned revision and one small question you can inspect by hand. Record the repository root, tool version, build command, exclusions, and the answer you expect from source.

2. Test identity. Choose an overload or another same-name symbol. Ask the tool for the qualified name, file, and signature. A safe result is the exact definition or an explicit list of candidates. A bare name is not enough.

3. Test callers. Ask for direct callers of that qualified target. Require the tool to separate production code from tests and say whether it lists call sites or calling functions. Check every relationship that would change your plan.

4. Test freshness. Build the index, then add one small relationship in a temporary branch, such as a direct caller. Before refresh, ask the tool for its index revision, repository root, configuration, and current repository revision. If it cannot compare them, the result is stale or unknown until source is checked.

5. Test an absent symbol. Ask for an exact symbol that you know does not exist. A safe tool says `NOT FOUND` in the stated scope. It may suggest related code, but it must label that code as a candidate.

The [reader-run testbench](https://github.com/artemrudenko/code-graph-benchmark-v2/blob/main/docs/reader-run-testbench.md) has copyable prompts, a small record sheet, and an answer contract. It is deliberately tool-neutral. It will not choose a winner for you. It will show uncertainty, setup errors, and stale indexes before an agent turns them into a patch.

![Before acting on compact code context, check the exact symbol, indexed scope, test boundary, and whether the response is verified, a candidate, not found, or stale.](https://raw.githubusercontent.com/artemrudenko/code-graph-benchmark-v2/main/assets/diagrams/retrieval-trust-checks.png)

## When I would use a code index

I would build a persistent index when relationship questions repeat often enough to repay its setup and refresh cost. I would keep a record of how it was built. Before using it to change code, I would require the exact target, scope, freshness, completeness, and a source location such as `file:line@revision`.

I turned those rules into two small, tool-neutral companion skills: [verify-code-context](https://github.com/artemrudenko/code-graph-benchmark-v2/tree/main/skills/verify-code-context) and [maintain-code-context-index](https://github.com/artemrudenko/code-graph-benchmark-v2/tree/main/skills/maintain-code-context-index). They do not make an index correct. They help an agent show what it knows, what it cannot prove, and what it should verify next.

The [public evidence archive](https://github.com/artemrudenko/code-graph-benchmark-v2) includes the [source-checked cases](https://github.com/artemrudenko/code-graph-benchmark-v2/blob/main/docs/evidence-index.md), [reproduction details](https://github.com/artemrudenko/code-graph-benchmark-v2/blob/main/docs/reproducibility-manifest.md), the [reader-run testbench](https://github.com/artemrudenko/code-graph-benchmark-v2/blob/main/docs/reader-run-testbench.md), and the full [selection framework](https://github.com/artemrudenko/code-graph-benchmark-v2/blob/main/docs/selection-and-evaluation-framework.md).

If you use a code index with an agent, does the tool tell you which revision it knows and what it left out?
