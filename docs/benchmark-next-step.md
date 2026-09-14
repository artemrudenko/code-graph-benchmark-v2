---
title: "The next benchmark: safe code context in a real change"
type: benchmark-design
status: proposed
---

# The next benchmark: safe code context in a real change

## The decision this benchmark should support

Choose a context setup for one real codebase and its recurring work. The setup
may be a language-server bridge, a code graph, ordinary source search, or a
small combination. It should help an agent find the right code and make a
correct change with less repeated navigation.

This is not a universal tool ranking. A compact answer is not a win if the
agent makes an incomplete patch or must repeat the same work in source.

## Gate 0: a valid run, not a score

Before any comparison, write down the repository revision, actual project
root, build configuration, indexed files and exclusions, tool version, build
command, and index outcome.

For a repository-wide task, start at the repository root. A smaller module is
valid only when the task is explicitly module-scoped and that module has its
own configuration. A failed, partial, stale, or wrongly scoped build belongs
in the setup log. Repair it and rebuild before the query is compared. It is not
recall, precision, speed, or a tool result.

This gate prevents the benchmark from measuring our own configuration mistake.
It also makes a negative result useful: the candidate may need a better
installer, a different configuration, or a source-search fallback.

## Stage 1: can the index give safe navigation context?

Use a pinned commit and source-derived expected answers. Keep each target small
enough to inspect by hand. The current archive already has examples of these
four checks:

| Check | What a safe result must do |
|---|---|
| Exact identity | Return the qualified target, or list candidates without choosing one. |
| Callers and tests | State the counting unit and separate production callers from tests. |
| Exact absence | Say `NOT FOUND` for an absent target; label related code as a candidate. |
| Freshness | Expose a changed revision or source relationship as stale until refresh. |

Record `VERIFIED`, `CANDIDATE`, `NOT FOUND`, `STALE`, `PARTIAL`, or `BLOCKED`.
Do not collapse these into one headline percentage. A count remains useful only
with its target, scope, and source check.

An LLM judge may help find unclear queries, but it is not ground truth. Source
checks decide Stage 1.

## Stage 2: does the setup help complete a real change?

This is the missing evidence if we want to discuss token or time savings. Use
three small, representative change tasks from the intended codebase. Each task
must have a fixed brief, a clean starting revision, a known expected change
radius, and a deterministic evaluator such as project tests plus a narrow
diff/source check.

For each promising setup, run the same task in fresh clones:

1. **Source baseline:** an agent has normal file reading and source search.
2. **Index-assisted:** the same agent also has the candidate context tool. It
   must still verify the relationships that drive its patch in current source.

Keep the model, task brief, permissions, repository revision, and evaluator
the same. Freeze the task set and scoring notes before the runs. Alternate run
order when practical so a warmed environment or an earlier failure does not
quietly favor one setup.

Record these facts for each run:

| Question | Evidence |
|---|---|
| Was the patch correct? | Tests, required source/diff checks, and a short human review of the changed relationship. |
| Did the agent use the index? | Tool-call trace and the exact context returned. |
| Did it preserve safety? | Source verification, target identity, test boundary, and index freshness. |
| What did it cost? | Elapsed time, model context, retries, and rebuild or refresh time. |

Patch correctness is a gate. Do not call a lower context total a saving when
the patch fails, misses a required caller, or needs an unrecorded recovery.

## How to make a small decision

After Stage 2, write a short capability note for each candidate:

- where it gives verified navigation context;
- where it returns a candidate or needs source fallback;
- its installation and refresh cost;
- whether it improved any correct completed task; and
- which languages, modules, or task shapes were actually checked.

The likely result is a practical stack, not a winner: source search as the
authority, a fast graph or language tool for repeated navigation, and a
manifest that detects stale or incomplete indexes.

## What the current archive proves and does not prove

The current evidence pack supports narrow Stage 1 observations about identity,
test boundaries, exact absence, and stale indexes. It also has one
source-verified stale-index task in which each condition passed once because
the agent checked source.

It does not yet support a claim that any candidate improves final agent work,
saves total tokens, or wins across repositories. The three-task Stage 2 pilot
above is the smallest next experiment that could support a local, useful
choice.
