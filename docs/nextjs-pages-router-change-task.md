---
title: "A repeated change task: Pages Router trace metadata"
type: controlled-change-task
status: active
---

# A repeated change task: Pages Router trace metadata

This is a small change-task experiment. It asks whether ordinary source
navigation, a code graph, and a language-server bridge can each help an agent
complete the same real code change without losing correctness.

The task starts from Next.js revision
[`3113d808a0cd3513d8806085efec0d853ff5ede7`](https://github.com/vercel/next.js/commit/3113d808a0cd3513d8806085efec0d853ff5ede7).
The expected behavior comes from [the later upstream change](https://github.com/vercel/next.js/commit/47072bf4c52c7cda63b37ef051550da9c76f7449).

The Pages Router did not expose configured OpenTelemetry trace metadata in the
HTML head. The agent had to move a shared filter out of the App Router, carry
the configuration through the Pages rendering path, render only allowed values
as `<meta>` tags, and add a focused runnable test.

## What decided a result

A patch was accepted only when it passed all five checks:

1. It changed only the expected production boundary and one focused test.
2. Source inspection showed a complete route from configuration to `Document.Head`.
3. The candidate's own TypeScript contract test passed.
4. That test failed when the allow-list filter was replaced with an unfiltered return.
5. The diff passed hygiene checks.

The known-good upstream implementation was accepted. A pristine checkout and a
patch that added only the shared helper were rejected.

## Results

| Condition | Fresh runs | Accepted | Verified tool use |
| --- | ---: | ---: | --- |
| Ordinary source navigation | 2 | 2/2 | No index MCP calls |
| Code Review Graph | 2 | 2/2 | Graph MCP was called in both runs |
| Serena | 2 | 2/2 | Serena MCP was called in both runs |

Each condition ran twice in a fresh checkout. All six accepted patches passed
the same source, test, mutation, and diff checks. They used several valid
internal routes: some filtered trace metadata in `Document.Head`; another
filtered it earlier in the Pages renderer. One route received configuration
through `BaseServer`; others used the existing render options path. The check
evaluates the required behavior, not a copied upstream diff.

Serena indexed TypeScript files only and logged one index failure. Its two
accepted runs used verified Serena calls, but this is still a partial-index
condition, not proof that its full project index was complete.

## What this result means

On this one real TypeScript task, no condition won. A graph or language server
can make navigation easier, but neither replaced current-source reading or a
test that catches the regression.

This does not measure tokens, time, cost, full browser E2E behavior, or the
quality of an agent's final explanation. It is not a ranking. The task proves a
smaller point: patch correctness is the gate before a claim about any efficiency
benefit.

The evaluator was adjusted after validation runs found behaviorally equivalent
implementations. All six primary runs and all controls were re-run under the
same final evaluator. The task description and result summary are public; the
raw candidate workspaces and evaluator code are not, because they contain
local-workspace metadata. This is a documented engineering experiment, not a
preregistered blind trial.
