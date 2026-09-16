---
# DEV publishing: upload assets/images/cover-broken-edge-dev.png as the cover image.
title: "I wanted my coding agent to remember the codebase"
published: false
tags: ai, llm, developertools, agents
description: "Can persistent code context reduce repeated agent work without making product changes less safe? I tested the question instead of trusting the tool demo."
---

An AI coding agent can look fast on its first task. The expensive part often appears on the fifth.

It opens the same files again. It traces the same call chain. It rediscovers where a value is assembled, and it can still miss one screen or one boundary that needs to change. The cost is not only tokens. A change takes longer, and the reviewer has more places where an incomplete patch can hide.

I wanted to give the agent a useful kind of working memory: a reusable map of the codebase that makes repeated investigation cheaper **without making the next product change less safe**.

That last condition changed the whole experiment. A short answer is a saving only when the resulting patch is correct. If an index helps the agent find four files quickly but it misses the fifth file that carries the contract, the saved tokens simply become rework.

This article is about how I tested that idea. It is not a leaderboard for code graph tools. My aim was more practical: learn when a saved code map earns a place in day-to-day product work, and when current source and tests must take over.

## How the investigation became more specific

This did not start with two tools and three tasks. I began by looking for practical ways an agent could keep code context between questions. The original selection protocol lists eight candidates, including ordinary source search, context packers, language-service bridges, graph indexes, and semantic search. They do different jobs, so they should not share one headline score.

The work then narrowed in three stages:

| Stage | Scope | Question it could answer |
|---|---|---|
| Find candidates and failure modes | 12 public repositories, 8 languages, and 4 candidates with source-checkable records | Can a compact answer safely help an agent navigate a particular codebase? |
| Make navigation answers trustworthy | Exact identity, test boundaries, absence, scope, and freshness checks | When should an answer be treated as a lead, rather than as evidence for a patch? |
| Test the delivered change | 3 fixed product tasks × 3 conditions × 5 fresh agent sessions | Does adding persistent context preserve the quality of a completed change? |

The broad first stage gives examples of failure modes. The narrow third stage checks a real outcome. Neither is a universal ranking or a token-saving claim. Together they support a more useful decision: which recurring question a tool can help with in *this* repository, what must still be verified, and whether it ever lowers the total work without lowering patch quality.

The full candidate history, pinned revisions, and raw records are in the [selection framework](https://github.com/artemrudenko/code-graph-benchmark-v2/blob/main/docs/selection-and-evaluation-framework.md) and [reproducibility manifest](https://github.com/artemrudenko/code-graph-benchmark-v2/blob/main/docs/reproducibility-manifest.md). I keep that detail in the archive so the article can explain the decision without asking every reader to audit a tool catalogue first.

![A code-context lifecycle: configure scope and build a reusable index; ask recurring questions about symbols, callers, paths, and tests; check the source before acting; refresh the index after code changes.](https://raw.githubusercontent.com/artemrudenko/code-graph-benchmark-v2/main/assets/diagrams/code-context-lifecycle-article-large-dark.png?v=compact-20260916)

## The problem I was actually trying to solve

An agent repeatedly needs answers to a small set of questions:

| Question before a change | Why the answer matters |
|---|---|
| What is the exact function, class, or endpoint? | A familiar name can point to the wrong implementation. |
| Where else does this value or decision travel? | The visible UI is often only the last step of a longer path. |
| What could break if I change it? | This defines the change radius and review plan. |
| Which tests protect the behaviour? | A passing local check does not prove the intended behaviour. |
| Is the saved map still current? | A correct index from yesterday can be incomplete today. |

Tools answer these questions in different ways. Some ask the same language services used by an IDE. Others keep a parsed map of symbols, imports, calls, and tests. I call that map an *index* in this article. It is saved navigation, not a replacement for the source of truth.

The promise is attractive. The agent should spend less time reopening code and more time making a useful change. But the promise only matters if quality stays level or improves.

## The rule I refused to break

I did not count a small response, a convincing explanation, or a passing frontend check as success. A patch had to satisfy a source-derived behaviour contract. Its focused test had to pass. Then the same test had to fail again after I deliberately reintroduced a relevant defect.

That last step matters. It checks that the test is able to catch the mistake we care about, such as a wrong calculation or an update missing from the mobile layout. A green test that does not fail when the defect returns gives false confidence.

I used an LLM as a judge in an earlier exploration to help decide which questions were worth investigating. I do not use an LLM score to decide whether a patch is correct. A model can prefer a short, plausible answer that names the wrong function. For the change tasks below, source checks and deliberate mutations are the final gate.

## The result that changed my mind

I ran three fixed change tasks in one private Python and TypeScript product. Each condition used five fresh agent sessions. I compared ordinary source navigation with Code Review Graph and Serena, two tools that give an agent structured help finding code relationships.

Before each batch, I froze the task and an independent evaluator. A known-good patch had to pass. An untouched fixture and an incomplete patch had to fail. Only then did I count fresh agent runs.

| Product change | Ordinary source navigation | Code Review Graph | Serena | What it tells me |
|---|---:|---:|---:|---|
| Stop an inactive signed-in user from resolving a department through a shared SQL helper | 5/5 | 5/5 | 5/5 | Direct source navigation was enough. The indexes preserved quality, but showed no correctness advantage. |
| Show an honest delivery count in the existing desktop row and mobile card | 5/5 | 5/5 | 5/5 | A small change across two layouts was also reliable without an index. |
| Carry a machine category through SQL, pagination, TypeScript contracts, and two reader surfaces | 1/5 | 1/5 | 0/5 | A navigation index did not make a difficult cross-layer contract reliable. |

![Three fixed product tasks, with five fresh sessions per condition. Ordinary source navigation, Code Review Graph, and Serena all achieved 5 of 5 on two contained tasks. On the hard cross-layer task, they achieved 1 of 5, 1 of 5, and 0 of 5. This is task-specific evidence, not a tool ranking.](https://raw.githubusercontent.com/artemrudenko/code-graph-benchmark-v2/main/assets/diagrams/task-quality-gate-article-large-dark.png?v=compact-20260916)

The last row was the useful surprise. I expected a structured map to help most on the hard task. Instead, many patches looked plausible but were incomplete: a paginated field was absent, a closed vocabulary was changed incorrectly, or an uncertain state was left unprotected.

This does not mean that one condition is better than another. Five out of five still has a wide exact 95% interval, from 47.8% to 100%. These are small, task-specific observations. They do show something important for tool choice: an index can give an agent a faster starting point, but it does not supply a missing product contract or prove that every layer was changed.

I also threw away an early UI batch. Its fixture accidentally left an inverse historical patch visible in Git, so an agent could reconstruct the solution instead of understanding the current code. I rebuilt a clean one-commit fixture, reran the controls, and counted only the 15 fresh runs. The mistake was uncomfortable, but it is part of the lesson: a benchmark must not quietly provide its own answer.

The [quality-gate summary](https://github.com/artemrudenko/code-graph-benchmark-v2/blob/main/docs/info-radar-quality-gate-summary.md) and [redacted UI task record](https://github.com/artemrudenko/code-graph-benchmark-v2/blob/main/docs/info-radar-source-delivery-summary.md) describe the method and its limits. They do not measure token saving, elapsed time, index build cost, refresh cost, full browser behaviour, or general agent quality.

The product source is private, so these task records are deliberately redacted. They let a reader inspect the behaviour contract, controls, and evaluator boundary, but they are not a package that an outside reader can rerun exactly. That limits their weight, and is one reason I do not use them to claim a winner.

## A map must also be trustworthy

The change tasks tell me whether the final patch survives a quality gate. I also checked four smaller retrieval questions against fixed source versions. This matters because an agent can act on a compact answer long before a test has a chance to correct it.

| Check | Tool response | Source-checked result | Practical lesson |
|---|---|---|---|
| Ktor function name collision | Code Review Graph returned 17 callers | 1 caller belonged to the requested low-level parser; 16 belonged to another public overload with the same name | A name is not an identity. Check the exact definition before estimating refactor impact. |
| ripgrep test boundary | Code Review Graph returned 28 callers | 24 were tests; 4 were production functions | “All callers” needs a visible test and production boundary. |
| Deliberately absent symbols | graphify returned related code in 3 of 12 fixed queries | 9 returned a clear no-match response | A related suggestion must not look like an exact match. |
| FastAPI indexing scope | Serena found 1 of 4 known references from a nested package root | The same version returned 4 of 4 when indexed from repository root | Scope is part of the answer, not a detail to hide in setup. |

[Ktor](https://ktor.io/docs/server-create-a-new-project.html) is an open-source Kotlin framework for building server applications. Its result is a good example of why a small answer can be dangerous. The low-level `parseHeaderValue` function has one direct caller, `parseHeaders`. The tool also returned 16 callers of a different public function with the same name. The response was compact, but almost all of it was wrong for the target I asked about.

![Ktor's low-level CIO parseHeaderValue has one direct caller, parseHeaders. Code Review Graph returned 17 results labelled as the CIO target: one correct caller and 16 callers of a public overload or its tests.](https://raw.githubusercontent.com/artemrudenko/code-graph-benchmark-v2/main/assets/diagrams/ktor-caller-disambiguation-article-large-dark.png?v=compact-20260916)

This is not an argument against a graph or language tool. It is a reason to give the answer a trust contract: the exact target, the indexed scope, a clear test boundary, and a label for exact match, possible match, or no match.

## Memory that does not refresh is old memory

I then checked what happened after source changed. In a controlled FastAPI case, an index was built when the helper `solve_dependencies` had four direct callers. I added a fifth caller in a local source revision. The existing indexes still reported yesterday’s relationships until their refresh path ran.

| Behaviour on changed source | Safe response from an agent |
|---|---|
| Code Review Graph still returned four edges and gave no automatic warning | Compare the saved revision with the repository; refresh or check source. |
| codebase-memory-mcp reported `metadata_changed` through its coverage check | Treat this as a rebuild request, even if general status says ready. |
| graphify retained its old incoming-edge view without a code-revision signal | Rebuild or use source search before treating the caller set as complete. |

![A stale-index control: build an index when source has four callers; source changes to five callers; the old graph misses the new relationship; compare freshness, check current source, then refresh before relying on it again.](https://raw.githubusercontent.com/artemrudenko/code-graph-benchmark-v2/main/assets/diagrams/stale-index-control-article-large-dark.png?v=compact-20260916)

I ran one small rename task with ordinary source navigation, Graphify with the old graph, and Graphify rebuilt after the change. Each condition passed the same deterministic evaluator once. The stale-graph run still succeeded because the agent searched current source before editing all five callers.

That is a workflow observation, not a performance result. The control was small, each condition ran once, and the baseline passed too. It supports one rule only: use a saved map to start the search, then verify a relationship-sensitive change against current source. The [normalized control record](https://github.com/artemrudenko/code-graph-benchmark-v2/blob/main/docs/stale-index-control.md) has the precise boundary.

## How I would test a tool in my own repository

Vendor demonstrations are useful for discovering possibilities. They cannot tell us whether a tool fits a particular architecture, build, codebase age, or team workflow. The test can be small and still be much more useful than a generic ranking.

1. Pick two or three questions that genuinely repeat in current work. Include one ordinary lookup and one hard case: an overload, generated code, a build-specific implementation, or a test-heavy API.
2. Write the expected answer from source before running the tool. Decide whether tests count and what “caller” means in this case.
3. Record the project root, exclusions, dependencies, build flags, index time, and any errors. A wrong root can make a correct tool appear broken.
4. Save every raw answer. Check it against source before using it to plan a change. State whether the answer is exact, a candidate, or no match.
5. Make a small source change, refresh the index, and repeat one affected relationship question.
6. Give the agent one fixed change task. Require the patch, a focused test, and a failed mutation before measuring time, tool calls, context, or tokens.

I turned this into three small, tool-neutral companion skills: [verify-code-context](https://github.com/artemrudenko/code-graph-benchmark-v2/tree/main/skills/verify-code-context), [maintain-code-context-index](https://github.com/artemrudenko/code-graph-benchmark-v2/tree/main/skills/maintain-code-context-index), and [run-code-context-change-task](https://github.com/artemrudenko/code-graph-benchmark-v2/tree/main/skills/run-code-context-change-task). They do not make an index correct. They make its scope, freshness, and uncertainty visible before the agent acts.

![Five checks before a compact answer guides a code change: exact target, scope and build, test boundary, match type, and freshness. If any answer is unclear, verify current source before acting.](https://raw.githubusercontent.com/artemrudenko/code-graph-benchmark-v2/main/assets/diagrams/retrieval-trust-checks-article-large-dark.png?v=compact-contrast-20260916)

## What I would measure next

The real value of persistent context will not appear in a single answer. It will appear, if it appears at all, across a sequence of independent tickets: the agent asks fewer repeated questions, reuses safe navigation, and still delivers patches that meet the same quality gate.

That next experiment needs a baseline and an indexed condition on comparable tickets. It should measure the whole lifecycle: setup, index build, refresh, tool calls, retries, context, elapsed time, and patch quality. Quality comes first. Only after it stays level can lower overhead become a useful result.

My conclusion is deliberately modest. Persistent code context is worth trying as working memory for an agent. It can make repeated navigation easier. It does not make the agent understand a product automatically, and it cannot replace a clear behaviour contract, current source, or tests that can expose a regression.

The [public evidence archive](https://github.com/artemrudenko/code-graph-benchmark-v2) contains the [source-checked cases](https://github.com/artemrudenko/code-graph-benchmark-v2/blob/main/docs/evidence-index.md), [reproduction details](https://github.com/artemrudenko/code-graph-benchmark-v2/blob/main/docs/reproducibility-manifest.md), the [three companion skills](https://github.com/artemrudenko/code-graph-benchmark-v2/tree/main/skills), the [reader-run testbench](https://github.com/artemrudenko/code-graph-benchmark-v2/blob/main/docs/reader-run-testbench.md), and the [redacted quality-gate summaries](https://github.com/artemrudenko/code-graph-benchmark-v2/blob/main/docs/info-radar-quality-gate-summary.md).

What does your coding agent keep re-investigating in the same repository?
