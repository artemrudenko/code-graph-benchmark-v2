---
name: maintain-code-context-index
description: Build, record, check, and refresh a persistent code-context index so an agent can tell whether a graph describes the current repository. Use before relying on an index across coding sessions or after source changes.
---

# Maintain a code-context index

An index is reusable navigation memory. Its successful build does not prove
that it is fresh, complete, or safe to treat as the source of truth.

## Choose the project root before building

For a repository-wide question, the index root must be the repository root.
Find it before invoking the candidate: use the version-control top level when
available, then check the repository workspace or build configuration. Do not
guess from the directory where an agent happened to start.

A package root is valid only when the question is explicitly limited to that
package and it has its own independent project configuration. Record that
smaller scope in the manifest. A package-level index must not answer a
repository-wide caller or impact question as if it were complete.

Treat a build at the wrong root as a setup failure. Fix the root and rebuild
before comparing the tool with another candidate or relying on its answer.

## Record the build context

When creating or refreshing an index, save a small manifest next to the
project or index artifact. Start from
[the template](assets/index-manifest.template.json). Record:

- repository root, repository revision, and whether the working tree was
  clean;
- tool name and version;
- the actual build or update command, configuration, build flags, exclusions,
  and language-server prerequisites; and
- the time and outcome of the build, including omissions or errors; and
- one smoke query that crosses a relevant relationship, with any tool status,
  truncation, or coverage signal it returns.

Use an absolute root only in the local manifest. Do not publish local path
metadata in shared evidence or examples.

## Check freshness before a relationship answer

Compare the current repository revision and relevant configuration with the
manifest. A different revision, root, config, build flag, or exclusion makes
the index `STALE`. A dirty working tree makes freshness `UNKNOWN` unless the
tool can prove it re-indexed every changed file. Preserve any provider result
such as `degraded`, `partial`, or `truncated`; a fresh revision does not turn a
partial graph into a complete one.

A tool-specific status such as `ready` only describes that tool's artifact. It
does not override a revision mismatch. If the tool offers its own coverage or
change check, record that signal separately.

| Index condition | Safe use |
| --- | --- |
| Fresh and matching configuration | Use it to navigate; still verify relationships that drive a change. |
| Stale | Refresh it, or use current source as the complete answer. |
| Unknown | Do not present graph completeness; resolve from source or rebuild. |
| Build failed or partial | State the omitted scope and use an appropriate fallback. |

## Refresh after a change

After a patch, merge, dependency update, or configuration change, refresh the
index through the tool's documented update path. Re-run one relationship query
that crosses the changed boundary and check its answer in source. Update the
manifest only after the refresh succeeds.

If a user did not authorize a build or update, report the stale state and the
exact refresh that would be needed. Do not create a false `fresh` state from a
successful query alone.
