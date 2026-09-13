---
# DEV publishing: upload assets/images/cover-broken-edge-dev.png as the cover image.
title: "My coding agent kept re-reading code. I tested code graphs."
published: false
tags: ai, llm, developertools, agents
description: "I checked code graphs and context tools against source code to learn when an AI coding agent can safely rely on their answers."
---

A reference lookup on the same FastAPI commit found 1 of 4 known references to `solve_dependencies`. I changed only the indexing root, from a nested package to the repository root. It found all 4.

The source did not change. The symbol did not change. The configured scope did.

That is why I started this work. I wanted a coding agent to stop doing a mundane thing: reopening the same files and finding the same relationships in every session. Reusable code context could mean less repeated navigation, safer plans for changes and refactors, and fewer missed relationships.

I did not start with a goal of saving tokens. A short answer is useful only when it is correct enough to act on. Saving context by omitting the caller that must change is not a saving.

The question became: **can an index help an agent navigate without becoming a second source of mistakes?**

My answer so far is modest. A code index can be useful as working memory. It is not authority. Before a relationship changes a plan or a patch, the agent should know the exact target, the scope it searched, the freshness of the index, and what current source says.

This article shows four cases I checked against source code: an index rooted in the wrong folder, test calls that look like production impact, an absent symbol that received related suggestions, and an index that became old after a source change. It ends with a small test you can run before adopting a tool in your own repository.

![A code-context lifecycle: first configure scope and build a reusable index; then ask recurring questions about symbols, callers, paths, and tests; check the source before acting; after code changes, refresh the index and repeat.](https://raw.githubusercontent.com/artemrudenko/code-graph-benchmark-v2/main/assets/diagrams/code-context-lifecycle-article-large-dark.png)

## What an agent needs before it changes code

The problem is not one kind of tool. It is a repeated set of questions in normal coding work:

| Question from the agent | A useful answer must include |
|---|---|
| What does this symbol do? | The exact definition and local responsibility |
| Who uses it? | Callers or references for that definition |
| What will this change affect? | Relevant modules and entry points, not a random long list |
| How does execution reach it? | A path through the parts of the system that matter |
| Which tests protect it? | Test relationships separated from production impact |

Before any of them, two smaller questions matter: **Is this the right function or class?** And: **Did the tool search the repository and configuration I intended?**

This is why I looked at several kinds of code-context tool. They do different jobs.

| Job | What the tool gives an agent | Example class |
|---|---|---|
| Read a focused area | A selected package or files | Context packager |
| Find a definition or reference | Help from the project's language tooling | Language-server bridge |
| Follow repeated code relationships | A saved map of functions, imports, and calls | Parsed-code or graph index |
| Change a repeated code shape | A safe match for a syntax pattern | Structural pattern tool |

An AST, or abstract syntax tree, is the parsed structure of code: functions, calls, imports, and their locations. A code graph stores some of these relationships so they can be queried again. It can save navigation work. It cannot prove that every relationship is complete, current, or the one you meant.

I did not treat these tools as direct competitors. A packer, a language server, and a graph index can work together. The useful choice may be one tool plus source search when the tool is uncertain.

## Four checks that changed how I use code graphs

I kept four retrieval cases that I checked again against fixed source versions. They are observations, not a leaderboard.

| Check | Tool response | Source-checked result | Rule it led to |
|---|---|---|---|
| FastAPI indexing scope | Serena found 1 of 4 known references from a nested package root | The same source version returned 4 of 4 when indexed from the repository root. | Project setup is part of the answer. |
| ripgrep test boundary | code-review-graph returned 28 callers | 24 were test functions and 4 were production functions. | Split tests from production before impact analysis. |
| Deliberately absent symbols | graphify returned related code in 3 of 12 fixed queries for symbols that do not exist | 9 answers clearly said no match. | A related suggestion is a candidate, not an exact match. |
| FastAPI index freshness | A stale graph still showed 4 callers after a local source change | Current source had 5 direct callers. | Refresh or check source before a relationship-sensitive change. |

![FastAPI project-root control: with the same pinned commit and solve_dependencies lookup, a nested fastapi package root found 1 of 4 reference sites; the repository root found all 4. Only the index root changed.](https://raw.githubusercontent.com/artemrudenko/code-graph-benchmark-v2/7408b5fac5f27fa7496a7d5e35cc1fded1336aba/assets/diagrams/fastapi-project-root-control.png)

The FastAPI case made the risk concrete. `solve_dependencies` has four reference sites in the pinned source: three in `fastapi/routing.py` and one recursive call in `fastapi/dependencies/utils.py`. With a nested package as the index root, Serena returned one. With the repository root, the same lookup returned all four. The short answer looked reasonable. Its scope was incomplete.

None of these cases says that graph or language tools are bad. They say that an answer needs a small trust contract: exact target, search scope, test boundary, and a clear status such as exact match, candidate, or no match.

## A correct index can still be old

Then I tested the part that matters after the first query. I built indexes while a FastAPI helper had four direct callers. I added a fifth caller in a local source revision and asked the same question before refresh.

| Tool behaviour after the source change | Safe next step |
|---|---|
| code-review-graph still returned four edges without an automatic warning | Compare index revision with repository revision, then refresh or check source. |
| codebase-memory-mcp reported `metadata_changed` in its coverage check | Treat it as a rebuild request, even when a general status says ready. |
| graphify kept its old incoming-edge view without a revision signal | Rebuild it or use source search for the complete caller set. |

The graph counts differ by tool because one omits a recursive self-call and another groups callers. The source fact did not: after the change, there were five direct callers.

![A stale-index control: build an index when source has four callers; source changes to five callers; the old graph misses the new relationship; compare freshness, check current source, then refresh the index before relying on it again.](https://raw.githubusercontent.com/artemrudenko/code-graph-benchmark-v2/main/assets/diagrams/stale-index-control-article-large-dark.png)

I also ran one small rename task in three fresh sessions: no index, Graphify with the old graph, and Graphify rebuilt on the changed source. Each passed the deterministic evaluator once. In the stale-graph session, the graph missed the fifth caller, but the agent checked current source and updated all five.

This was an intentionally small control. It does not show that a stale index is harmless, that Graphify improves an agent, or that any setup saves tokens. It supports one working rule: a graph can help find a starting point; current source must decide a relationship-sensitive change. The [normalized control record](https://github.com/artemrudenko/code-graph-benchmark-v2/blob/main/docs/stale-index-control.md) states the exact boundary.

## Three checks to run in your own repository

You do not need to trust my cases or set up a large benchmark. A fresh clone, three fixed questions, and a separate source check can tell you whether a candidate tool is useful for your work.

First, choose a pinned revision and write the answer you expect from source. Record the repository root, tool version, build command, exclusions, and build flags. Run each question with plain source search as a baseline and with the candidate tool. Save the raw answers.

Then use these three tests:

1. **Identity test.** Choose an overload or another same-name symbol. Ask: `Find the definition of <symbol>. Return its qualified name, file, and signature. If several definitions fit, list them as candidates and do not choose one.` The expected result is an exact identity or an explicit ambiguity.
2. **Caller-boundary test.** Ask: `For <qualified target>, list direct callers. State whether the unit is a caller function or a call site. Split production code from tests, and state excluded paths or limits.` Check every relationship used for a decision in current source.
3. **Freshness test.** Build the index, then make one small isolated change in a disposable branch, such as adding a direct caller. Ask: `State the index revision, repository root, relevant exclusions, and current repository revision. If they differ or cannot be checked, return STALE or UNKNOWN. Verify the relationship in current source before answering.`

An optional fourth test catches a common presentation problem: ask for an exact symbol that you know does not exist. A safe answer says `NOT FOUND` in the stated scope. It may offer related items, but it must label them as candidates.

The [reader-run testbench](https://github.com/artemrudenko/code-graph-benchmark-v2/blob/main/docs/reader-run-testbench.md) has the full prompts, an answer contract, and a small record sheet. It is deliberately tool-neutral. It will not choose a winner for you. It will make uncertainty, setup errors, and stale indexes visible before an agent turns them into a patch.

![Before acting on compact code context, check the exact symbol, indexed scope, test boundary, and whether the response is an exact match, a candidate, or no match.](https://raw.githubusercontent.com/artemrudenko/code-graph-benchmark-v2/main/assets/diagrams/retrieval-trust-checks.png)

## Why I did not use an LLM judge as proof

An earlier experiment used an LLM judge. A Sonnet model compared each tool answer with a plain file-reading answer and gave it a quality score. That was useful for finding questions worth checking. It was not proof that an answer was correct.

An LLM can prefer a concise answer, miss a wrong overload, or inherit an error from the comparison answer. That scorecard also mixed different tool types, setup costs, and response formats. I do not use its winners or scores as evidence.

For the four retrieval observations, each number has a fixed repository and code version, saved raw output, a separate source check in a fresh clone, and the recorded query and index scope. The stale-index control has a fixed task and deterministic evaluator, but its raw records remain private because they contain local-path metadata. These are useful boundaries, not universal claims about token savings or final agent quality.

## The practical rule I would keep

Build a persistent index when relationship questions repeat often enough to repay its setup and refresh cost. Keep a record of how it was built. Before using it to change code, require an answer that names the target, scope, freshness, completeness, and a source anchor such as `file:line@revision`.

I turned those rules into two small, tool-neutral companion skills: [verify-code-context](https://github.com/artemrudenko/code-graph-benchmark-v2/tree/main/skills/verify-code-context) and [maintain-code-context-index](https://github.com/artemrudenko/code-graph-benchmark-v2/tree/main/skills/maintain-code-context-index). They do not make a graph correct. They help an agent show what it knows, what it cannot prove, and what it should verify next.

The [public evidence archive](https://github.com/artemrudenko/code-graph-benchmark-v2) includes the [source-checked cases](https://github.com/artemrudenko/code-graph-benchmark-v2/blob/main/docs/evidence-index.md), [reproduction details](https://github.com/artemrudenko/code-graph-benchmark-v2/blob/main/docs/reproducibility-manifest.md), the [reader-run testbench](https://github.com/artemrudenko/code-graph-benchmark-v2/blob/main/docs/reader-run-testbench.md), and the full [selection framework](https://github.com/artemrudenko/code-graph-benchmark-v2/blob/main/docs/selection-and-evaluation-framework.md).

More people can run this kind of check now. That makes a healthy form of skepticism practical: use the tool, write down what it claims, and verify the relationship that would change your decision.

If you use a code index with an agent, I would be interested in one thing: does the tool tell you which revision it knows and what it left out?
