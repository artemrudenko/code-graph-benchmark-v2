---
title: "A small code-context testbench you can run in your own repository"
type: reader-guide
status: active
---

# A small code-context testbench you can run in your own repository

This guide helps you check a code graph, language-server bridge, or other
code-context tool before you rely on it for an agent's plan or patch. It does
not produce a universal ranking. It helps you decide whether a tool is useful
for the recurring questions in one repository.

The central rule is simple: a smaller answer is only a benefit if it preserves
the relationship needed to make the change. Current source and project tests
remain the authority.

## Set up a small, comparable run

Use a clean clone at a pinned revision. Pick a repository where you can read
the source and run the relevant tests. Keep the test small enough to inspect
by hand.

Before invoking a candidate, make one record:

```text
Repository and revision: <URL and commit>
Repository root: <path relative to the clone>
Candidate and version: <tool name and version>
Build/update command: <exact command>
Configuration: <build flags, language-server settings, exclusions>
Baseline: <plain source search and file reading>
```

Write the expected result from source before asking the tool. For a
repository-wide question, resolve the repository root from version control or
the project workspace before building an index. A package root is appropriate
only when the question is explicitly package-scoped. If you started from the
wrong root, fix it and rebuild; do not count that run when you compare tools.

For caller questions, say whether the unit is a call site or a distinct caller
function, and whether tests count. This prevents a compact but differently
scoped answer from looking correct by accident.

Run the same test with plain source reading and each candidate. Save every raw
tool answer. Also record whether the agent actually called the context tool;
otherwise a good result does not show that the index helped.

## Test 1: exact identity

Choose an overload, a similarly named symbol, generated copy, or another case
where a name alone is not enough.

Use this prompt:

```text
Find the definition of <symbol>.

Return its qualified name, file, and signature. If more than one definition
fits, list the candidates and do not choose one. State the repository root and
configuration used for this search.
```

Check the returned definition in current source. A good outcome is either the
one exact target or an explicit list of candidates. A bare name is not enough.

## Test 2: callers and the test boundary

Choose a function with a manageable caller set and at least one test caller,
if the project has one.

Use this prompt:

```text
For <qualified target, file, signature>, list direct callers.

State whether each result is a caller function or a call site. Split production
code from test code. State excluded paths, capped results, missing language
coverage, or other limits. If identity or completeness is uncertain, return
CANDIDATE or PARTIAL rather than presenting a complete caller set.
```

Open every relationship that would affect a refactor. Confirm that it calls the
resolved target, rather than another overload or a same-name symbol. Compare
the test and production groups with the expected source result.

## Test 3: freshness after one source change

Build the index at the pinned revision. In a disposable branch or copy, add one
small isolated relationship that is easy to see in source. For example, add a
direct caller to a helper. Do not use a production bug for this test.

Before rebuilding the index, use this prompt:

```text
For <qualified target>, state the index revision, current repository revision,
repository root, and relevant exclusions.

If the index revision, root, configuration, or coverage is different or cannot
be checked, return STALE or UNKNOWN. Do not claim a complete relationship set
from the index alone. Verify the requested relationship in current source
before giving a final answer.
```

Then run the candidate's documented refresh path. Repeat the query and source
check. A successful build is not itself proof that the result is current or
complete.

## Optional test: exact absence

Use a symbol that you know is absent from the stated scope.

```text
Find the exact symbol <deliberately absent qualified name> in this repository.

Return NOT FOUND if it is absent from the stated scope. You may list related
symbols only under CANDIDATES. Do not present a related symbol as an exact
match.
```

This test checks whether a natural-language query turns a helpful suggestion
into a misleading answer.

## Optional Stage 2: test one real change

The checks above establish whether a tool can supply safe navigation context.
They do not show that it helps an agent complete work. Before claiming saved
time or context, choose one small change with a fixed brief, expected affected
files, and a deterministic evaluator.

Run it in fresh clones at least twice per condition: once with normal source
reading and search, and once with the same agent plus the candidate index. Keep
the revision, prompt, model, permissions, and evaluator the same. Require a
known-good control, a pristine control, and an incomplete-patch control before
comparing agents. In both runs, require current-source inspection, a runnable
candidate test, and a mutation that the test must fail. Record whether the
index was actually called, as well as the patch result, source checks, retries,
elapsed time, and context. A smaller run that produces a wrong patch is not a
saving.

For a ready-to-use task protocol, start with the
[change-task skill](../skills/run-code-context-change-task/SKILL.md). For a
three-task version of this experiment, use [the next benchmark
design](benchmark-next-step.md) and its [catalog of common developer
questions](agent-code-question-catalog.md). It separates graph questions from
duplicate detection and test-coverage questions, which need different evidence.

## Record the answer in one small contract

Use this record for every result that will affect a plan, a patch, or a review:

```text
Status: VERIFIED | CANDIDATE | NOT FOUND | STALE | BLOCKED
Target: <qualified symbol, file, signature>
Scope: <repository root and relevant configuration>
Freshness: FRESH | STALE | UNKNOWN | NOT APPLICABLE
Completeness: COMPLETE | PARTIAL | TRUNCATED | UNKNOWN
Index result: <tool called? result, limits, and provider signal>
Source check: <file:line@revision and relationship evidence>
Boundary: <production only | tests included | split shown>
Next action: <safe next step>
```

`VERIFIED` requires the exact target, known enough scope, and a current-source
check for each relationship that drives a decision. A concise answer with an
unknown scope or an old index is useful as a lead, but it is not verified
context.

## Make a choice without a headline score

Keep three separate notes for each candidate:

| Question | What to record |
|---|---|
| Is it ready to use? | Installation and index time, project root, prerequisites, exclusions, and failures |
| Can I trust this answer? | Exact identity, source-checked callers, test boundary, freshness, and limits |
| Does it help real work? | A fixed change task, tests, patch correctness, retries, time, and context |

Do not call a smaller response a saving if the patch is wrong or source checks
recreate the same work. Measure time and context only after the answer is safe
enough to use. A useful outcome may be a small stack: one tool for navigation,
another for repeated relationships, and source reading when either one is
uncertain.
