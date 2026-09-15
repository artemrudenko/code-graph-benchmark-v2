---
title: "Questions an agent must answer before it changes code"
type: task-catalog
status: active
---

# Questions an agent must answer before it changes code

This catalog starts with developer work, not tool names. It helps choose a
context tool for the question at hand and shows what must still be checked in
source, tests, or coverage data.

A code graph is useful for relationships that are already present in code. It
is not a general proof engine for behavior, runtime paths, test coverage, or
semantic duplication.

| Developer question | What a useful answer contains | Authority before a patch | Useful tool class | Important limit |
|---|---|---|---|---|
| Which definition is this? | Qualified name, file, signature, and candidates when names collide | Current source | Language server or code graph | A name alone can select the wrong overload or generated copy. |
| Is this logic already duplicated? | Matching structure, scope searched, and why the match is comparable | Source review and tests | Structural pattern or clone-detection tool | A graph follows references; it cannot prove two pieces of code mean the same thing. |
| What changes if I refactor this API? | Direct production callers, tests, implementations, interfaces, and excluded paths | Current source and project build | Language server or code graph | Dynamic dispatch, reflection, generated code, and configuration can leave relationships outside a static map. |
| Which code is at risk after this patch? | Affected contracts, entry points, downstream modules, and uncertainty | Diff plus current source | Graph or dependency navigation | The graph suggests a change radius; it does not prove runtime behavior. |
| Which tests should I run, change, or add? | Existing related tests, test boundary, and behavior that still lacks proof | Test runner and coverage data | Test discovery, coverage, source search | A static reference from a test is not proof that a behavior is covered. |
| Is this index still usable? | Index revision, current revision, root, configuration, and refresh status | Current source and manifest | Index manifest and tool health check | A successful query does not prove an old index is fresh. |

## Three Stage 2 tasks to start with

Use real, small changes from the codebase where the agent will work. Freeze
one task brief and its evaluator before each run.

| Task | Prompt shape | What must be true for the patch to pass |
|---|---|---|
| API refactor radius | Rename or change a small public parameter or method, then update all direct production callers and relevant tests | The exact target is changed; required callers and tests are updated; project tests pass. |
| Regression and test decision | Change a rule or validation branch, then identify affected behavior and add or update tests | The intended behavior changes; relevant existing tests still pass; a test covers the changed branch or the record explicitly says why coverage is unavailable. |
| Structural duplicate decision | Find a known duplicated code shape and either extract it safely or explain why consolidation is unsafe | The candidate list is source-checked; the patch preserves behavior; tests pass; semantic similarity is not asserted from syntax alone. |

Run each task in a fresh clone with the same model, prompt, permissions, and
revision twice: source search only, then source search plus the candidate
context setup. The index-assisted condition still verifies relationships in
current source.

## What to record

For every task, retain:

- the user-facing question and fixed task brief;
- expected files, relationships, and test or coverage evidence;
- the tool calls and returned context;
- the source checks and fallbacks the agent used;
- the final diff and deterministic evaluator result; and
- elapsed time, model context, retries, plus build or refresh time.

Patch correctness comes first. A lower context total is not an improvement if
the agent misses a caller, changes a different symbol, or leaves behavior
without a test decision.

## Language boundary

A finding applies only to the language, build configuration, and task shape
that were actually run. A Python result does not establish behavior for a
TypeScript or C# project. Start with the languages in daily use, and use each
project's own build and test command as part of the evaluator.
