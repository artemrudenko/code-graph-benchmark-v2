---
title: "Controlled stale-index observation"
type: derived-evidence-summary
status: private-control-derived-summary
---

# Controlled stale-index observation

This is a narrow, normalized summary of a private control. It exists to make
the article's workflow claim inspectable without publishing raw files that
contain local path metadata. It is not a tool ranking or a claim about
production FastAPI history.

## Question

If code changes after a context index is built, can an agent safely use the
old relationship map to complete a refactor?

The control begins at FastAPI upstream revision
`50113da16fec53b66b80d75e80a89296de4fa5a5`, where `solve_dependencies` has
four direct callers. A local, unpushed synthetic revision adds a fifth direct
caller in an existing FastAPI source file. The task renames a keyword-only
argument and requires all five callers to be updated. The synthetic change is
deliberately disclosed; it is never presented as an upstream FastAPI commit.

## Tool preflight

Each tool indexed the four-caller revision, then operated on the five-caller
source without a refresh. Its documented update path was then run.

| Tool and version | Old index on changed source | Freshness signal | After refresh |
| --- | --- | --- | --- |
| code-review-graph 2.3.3 | 4 `CALLS` edges; new caller absent | saved build revision remained old; no automatic warning | 5 edges, including the new caller |
| codebase-memory-mcp 0.10.8 | new helper absent; 2 inbound caller groups | coverage check reported `metadata_changed` and `read_source_and_reindex` | helper found; 3 inbound caller groups |
| graphify 0.9.57 | 3 non-self incoming edges; new caller absent | no code-revision signal | 4 non-self incoming edges, including the new caller |

The graph values are not source caller totals. Graphify omits the recursive
self-call and codebase-memory-mcp groups callers differently. The source
ground truth is four direct callers before the local change and five after it.

## Agent control

Three fresh candidate sessions received the same changed source and a
deterministic evaluator. One had no index, one queried Graphify built before
the change, and one queried Graphify rebuilt after the change. Each session
was accepted once. The stale Graphify query omitted the extra caller, but the
agent then searched the current source and updated all five callers.

This supports one operational rule: use a graph as a starting point, then
verify current source before changing a relationship-sensitive symbol. It does
not show that stale indexes are harmless, that every agent will compensate,
or that any tool improves correctness, time, cost, or token use. The local
change was intentionally easy to identify, so it cannot estimate performance
on a subtle production change.

## Publication boundary

The complete private run, including raw Graphify JSON and candidate
transcripts, remains outside the public package while it contains local path
metadata. A future public release must rebuild the raw artifacts under neutral
paths or publish path-neutral derivatives with a documented provenance chain.
