# Code-context companion skills

These two folders are reusable operating rules for an agent working with a
code graph, language server, or ordinary source search. They do not install or
select a particular provider.

Copy the folders into the skill directory configured for your Codex
environment, then invoke the relevant skill when the task needs it:

| Skill | Use it when |
| --- | --- |
| [`verify-code-context`](verify-code-context/) | An answer about callers, references, execution path, test coverage, or change radius will affect a plan, patch, or review. |
| [`maintain-code-context-index`](maintain-code-context-index/) | An index is being built, reused in a later session, or checked after source or configuration changes. |

The skills deliberately make three known failure modes visible: a same-named
but different symbol, test callers mixed with production callers, and a graph
that was built before the relevant source change. A useful result states its
scope, freshness, completeness, and source anchor instead of presenting a
compact graph response as complete.
