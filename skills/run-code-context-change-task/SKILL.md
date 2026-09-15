---
name: run-code-context-change-task
description: Compare ordinary source navigation with one or more code-context tools on a small real code change. Use only after a source-grounded expected behavior and evaluator are ready.
---

# Run a code-context change task

Use this skill when you need to decide whether code context improves an
agent's real work. A shorter answer is not a result. A correct patch is the
first gate.

## Prepare the task before running any agent

Choose a small real change with a clear behavior. Pin the repository revision.
Write the task without naming files or the expected patch. Create an evaluator
outside candidate checkouts.

The evaluator should require:

1. a bounded set of allowed production and test files;
2. a source check across the change boundary;
3. a runnable candidate test; and
4. one mutation that the candidate test must fail.

Run three controls first: a known-good patch must pass; a pristine checkout
must fail; and an incomplete patch that fixes only one layer must fail. Repair
the evaluator before comparing candidates if any control has the wrong result.

## Run comparable conditions

Use a fresh checkout for each run. Keep the repository revision, task,
evaluator, model, and permissions fixed. Record the tool version, index root,
exclusions, build/update command, and whether the agent actually called the
tool.

For index-assisted conditions, build at the repository root before the agent
starts. Keep generated indexes, dependency trees, evaluator files, and oracle
patches outside the candidate's allowed diff. If indexing fails, is partial, or
requires interactive setup, record `BLOCKED` or `PARTIAL`; do not treat it as
a normal run.

Interleave at least two runs for every condition. Do not count a run as
tool-assisted merely because an index existed: the transcript must show the
tool call.

## Report narrowly

Report accepted patches, rejected patches, controls, actual tool use, and any
setup failures. State whether the test and mutation ran. Keep time, tokens,
and cost separate from correctness; do not call them savings until correct
patches are already comparable.

Do not announce a winner from one task. A useful outcome is a capability
profile: which tool helped on which question, under what setup, and when the
agent returned to source or tests.
