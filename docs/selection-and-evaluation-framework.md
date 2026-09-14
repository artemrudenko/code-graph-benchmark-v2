---
title: "Choosing persistent code context: research objective and pilot protocol"
type: research-framework
generated: 2026-09-10
status: active
---

# Choosing persistent code context: research objective and pilot protocol

## The objective

Choose a dependable way for an AI coding agent to reuse knowledge of a codebase across repeated work. The intended outcome is less repeated navigation, better planning of changes and refactors, and fewer missed relationships. A smaller response is useful only when it still preserves the relationship needed to act safely.

This is **not** a contest to name a universal winner. The useful result may be one primary tool plus a fallback: for example, semantic navigation for exact references, a graph index for relationship exploration, and ordinary source search when the index cannot establish an answer.

## What counts as code context

| Need during work | Plain-language description | Tool class | Examples in the landscape | What it cannot establish by itself |
|---|---|---|---|---|
| Read a bounded area | Give the agent the relevant files or module in one package | Context packager | Repomix | A reliable cross-repository caller or reference graph |
| Navigate a symbol | Ask the project's language tooling for a definition, references, or rename | Language-server bridge | Serena | A useful answer when the project root, dependencies, or language server are misconfigured |
| Follow relationships | Store code entities and links such as calls, imports, and ownership for repeated queries | AST or code-graph index | CRG, CBM, graphify | That every edge has the semantic meaning a refactor requires |
| Find or change a syntax shape | Match code structure and apply a constrained transformation | Structural pattern tool | ast-grep | Runtime flow, dynamic dispatch, or all callers of a symbol |
| Resolve uncertainty | Read the source and run its own checks | Ordinary search, file reading, tests | repository tools | A reusable map without repeated investigation |

The classes overlap in a real workflow, but they do not answer the same question. A single score that ranks a packer, an LSP bridge, and a graph query as though they did the same job hides that difference.

## The questions that recur in agent work

A selection should start from work the agent actually repeats, not from tool names.

| Question | What the agent needs before acting | Typical failure if the answer is weak |
|---|---|---|
| What is this symbol for? | The exact definition, signature, and local responsibilities | It edits an overload, generated copy, or similarly named function |
| Who uses it? | Direct callers or references, with a stable identity | It changes a supposedly isolated API and misses a consumer |
| What is the change radius? | Relevant downstream modules, interfaces, and entry points | It underestimates a refactor or reads unrelated files |
| How does execution reach it? | A path through handlers, adapters, and boundaries | It fixes a local symptom without seeing the route into it |
| Which tests protect this behavior? | Test callers separated from production callers | It treats tests as runtime impact, or forgets to update coverage |
| What changed in this review? | The affected relationships and a way to verify them | It reviews a diff line by line and misses a broken dependency |

Before all six questions comes a validity gate: the tool must have a stated project scope, build configuration, and usable index. Repair an invalid setup before comparing tools. Then ask: **is this the exact target?** A response must be marked as an exact match, a candidate, or no match. These are properties of an answer, not separate user workflows.

## The research model: readiness, answer trust, and payoff

The decision has three independent layers. Do not merge them into a headline score.

| Layer | Measure | Evidence to retain |
|---|---|---|
| First-use readiness | Install and index time, required project root, language/build prerequisites, files excluded | Command, project configuration, commit, index log, known omissions |
| Answer trust | Exact-target resolution, source-checked recall and precision, test/production split, traceability to files and lines | Fixed query, raw response, independent source check, explicit result status |
| Workflow payoff | Time and context used on the first task, warm repeated tasks, and after a code change; retries; correctness of the completed task | Fixed task brief, agent transcript or telemetry, code/test result, rebuild log |

The first two layers determine whether an answer is safe to use. The third measures whether maintaining the index pays for itself. Output-token count alone measures neither safety nor long-term payoff.

## A small pilot that can make a real choice

Run the pilot on the codebase where the tool will be used, at a pinned commit and with the real build configuration.

1. Select three recurring tasks from current work. Include one ordinary lookup and one hard target, such as an overload, build-tagged implementation, generated code boundary, test-heavy API, or cross-package import.
2. Write the expected source-grounded answer before invoking any candidate. For caller questions, define whether tests count and whether the unit is call sites or distinct calling functions.
3. Resolve the repository root before building an index for a repository-wide question. A package root is valid only for an explicitly package-scoped task. Treat a wrongly scoped build as a setup failure, rebuild it, and do not include it in a comparison.
4. Record the valid setup: project root, language server or index version, exclusions, build flags, index command, completion time, and errors.
5. Run the fixed queries against each candidate and retain the raw outputs. Check each answer against source before the agent acts.
6. Repeat the same work after the index is warm. Then make a small representative code change, refresh or rebuild the index, and repeat one affected query.
7. For a final decision, let an agent complete three fixed change tasks with each promising setup. Compare an ordinary source-search baseline with an index-assisted run in fresh clones. Record total context, elapsed time, source checks, tests, retries, and whether the patch is correct. This is the first point where a claim about total token or time savings is justified.

Use a capability profile and decision note, not a winner column. A candidate can be acceptable for a narrow task even when another is better for a different language or refactor shape.

## Verified observations from the current evidence pack

The current archive verifies three narrow retrieval checks. They establish why the trust gates above are needed; they do not choose a tool for every codebase.

| Check | Verified result | Selection implication |
|---|---|---|
| Ktor name collision | CRG returned 17 callers for a low-level `parseHeaderValue`; 1 was the real CIO caller and 16 belonged to a public overload | A name is not a stable identity; inspect the resolved definition |
| ripgrep test boundary | CRG returned 28 callers of `Ignore::add_child`: 24 test functions and 4 production functions | Preserve the test flag or split the answer before using it for impact analysis |
| Exact absence | graphify substituted related real nodes in 3 of 12 deliberately absent-symbol queries; 9 returned a clear no-match response | Treat fuzzy suggestions and exact matches as separate result types |
The full claims, raw output references, and independent source checks are in the [evidence index](evidence-index.md). The separate FastAPI project-root control is retained there as a setup-audit record. It is excluded from the retrieval findings because its original nested-root run was not a valid repository-wide configuration.

## How to read the older scorecard

An earlier exploratory scorecard used a Sonnet LLM judge. It read a tool response and gave it a quality score against a plain file-reading answer. This was useful for finding questions that deserved more investigation. It was not a source check and it was not ground truth.

A judge can prefer an answer that is concise or well written. It can miss that the answer points to the wrong function. It can also repeat an error in the comparison answer it was given. The scorecard also mixed tools that do different jobs, and it did not compare their setup cost, rebuild cost, or full agent-task outcome in one controlled study. The current archive does not include the files needed to audit every historical quality score.

For these reasons, the numerical winners, combined quality-and-token score, and tool-stack recommendations from that earlier scorecard are withdrawn. They should not be cited as current results.

## Why the current claims are stronger, but still narrow

The three retrieval observations have a fixed repository and commit, saved raw tool output, a recorded query and index scope, and a separate source check in a fresh clone. This is enough to support the narrow claim written for each retrieval case. The separate FastAPI setup control remains in the archive as an audit record, not as retrieval evidence.

It is not enough to prove a universal ranking, total token savings, or better final patches from coding agents. A first controlled stale-index task is now recorded in [the derived control summary](stale-index-control.md): its baseline, stale-Graphify, and fresh-Graphify sessions each passed once only because the workflow required current-source verification. That supports the source-first safety rule, not a ranking or a gain claim. Broader claims still need repeated fixed tasks, the same project configuration, independent source checks, test results, and recorded retries for every candidate.
