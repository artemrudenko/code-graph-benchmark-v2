---
name: verify-code-context
description: Verify an answer from a code graph, language server, or search tool before using it to plan or change code. Use for callers, references, execution paths, change radius, and test coverage questions.
---

# Verify code context

Use an index or language tool to navigate quickly. Treat current source as the
authority before an answer changes a plan, a patch, or a review conclusion.

## Start with the target

State the requested symbol as precisely as the repository allows: module or
file, enclosing type, signature, and language. If two definitions could fit,
resolve them in source before interpreting callers or references. A name alone
is not a stable identity.

Record the repository root and the scope the tool actually searched. If the
tool uses a project configuration, build flags, generated sources, or ignored
paths, retain the relevant setting with the answer. Also record whether the
agent actually called the context tool. A source-only answer is useful, but it
is not evidence that the configured index helped.

## Ask, then verify

Use the available graph, language-server, pattern, or search capability to
find a starting set. For each relationship that matters to a change:

1. Open the referenced definition or call site in the current source.
2. Confirm that it refers to the resolved target, rather than an overload or a
   similarly named symbol.
3. State the counting unit: call sites or distinct calling functions.
4. Split test code from production code when the task is impact analysis or a
   refactor.
5. If the index state is stale or unknown, use source verification for the
   complete answer; a graph result can still be a useful lead.

An exact-name query that returns related code is a candidate, not a match. A
clear absence in the searched scope is useful only when the scope is stated.

## Return an answer contract

Use this compact structure in the final response or plan:

```text
Status: VERIFIED | CANDIDATE | NOT FOUND | STALE | BLOCKED
Target: <qualified symbol, file, signature>
Scope: <repository root and relevant configuration>
Freshness: FRESH | STALE | UNKNOWN | NOT APPLICABLE
Completeness: COMPLETE | PARTIAL | TRUNCATED | UNKNOWN
Index result: <tool called? result, limits, and tool quality signal>
Source check: <file:line@revision and relationship evidence>
Boundary: <production only | tests included | split shown>
Next action: <safe next step>
```

`VERIFIED` requires an exact target, known enough scope, and a current-source
check for every relationship used to act. `CANDIDATE` means the output may be
relevant but identity, scope, or source evidence is incomplete. `NOT FOUND`
means the target was absent from the stated scope; it is not evidence about
other scopes. `STALE` means the index does not describe the current source.
`BLOCKED` means a required source, configuration, or permission boundary is
unavailable.

`COMPLETE` requires that the tool did not signal truncation or an excluded
path, and that source checks cover the relationships used for the decision.
When either point is unknown, say `UNKNOWN` rather than inferring completeness
from a short response.

Do not convert a candidate into a patch instruction or a claim about complete
change impact. Say what would resolve it instead.
