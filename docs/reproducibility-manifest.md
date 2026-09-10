---
title: "Code-graph tools benchmark v2 — reproducibility manifest"
type: reproducibility-manifest
generated: 2026-09-10
source: code-graph-benchmark-v2-protocol.md (full round-by-round log)
purpose: "One row per (repo × tool × query) with everything needed to re-run this benchmark bit-for-bit: exact commit, exact scope, exact command, exact query text, and which raw file on disk backs the claim."
---

# Reproducibility manifest

Tool versions used throughout (confirmed installed in the benchmark environment, 2026-09-10):

| Tool | Package | Version |
|---|---|---|
| code-review-graph | `code-review-graph` (PyPI, tirth8205/code-review-graph upstream) | 2.3.8 |
| codebase-memory-mcp | `codebase-memory-mcp` (PyPI, DeusData/codebase-memory-mcp upstream) | 0.10.8 |
| graphify | `graphifyy` (PyPI — note double "y", package name `graphify` is a different, unrelated project) | 0.9.57 |
| Serena | `serena-agent` (PyPI, oraios/serena upstream) | 1.7.0 |

All commands below assume the repo has been cloned at the exact SHA in that repo's header and the current working directory is the scope path given. `callers_of`/`importers_of` queries go through CRG's CLI; CBM queries go through its `cli --json search_graph` / `trace_path`; graphify queries go through `graphify query "<text>"` after a build (`graphify . --no-viz` for code-only corpora, or the full `/graphify` agent skill when the corpus has docs/papers/images — noted per repo below).

---

## 1. FastAPI — `fastapi/fastapi`

- Full SHA: `50113da16fec53b66b80d75e80a89296de4fa5a5`
- Commit date: 2026-09-01T20:59:53+00:00
- Scope: `fastapi/` core only — **48 `.py` files / 23,652 LOC**
- Rounds: pilot round 1 (Q1/Q2, `solve_dependencies`), round 2 (Q3/Q6/Q7, `jsonable_encoder` / `resolve_response_model_overrides`), round 3 (graphify live agent run)
- Raw files: `raw-data/fastapi/`

| Tool | Command | Query text | Raw file |
|---|---|---|---|
| Plain Claude Code | `Read` on `utils.py` + `routing.py` | "solve_dependencies: signature, who calls it" | — (baseline, no separate raw file; token count in protocol text) |
| repomix | `npx repomix --include "fastapi/**" --output out.txt` | — (packs whole module) | `repomix_fastapi.txt` |
| code-review-graph | `code-review-graph build --repo fastapi` then `code-review-graph query --repo fastapi callers_of solve_dependencies` / `callers_of jsonable_encoder` | Q1/Q2: `solve_dependencies` · Q3: `jsonable_encoder` | `crg_q1.txt`, `crg_q1_callers.txt`, `crg_search.txt` |
| codebase-memory-mcp | `codebase-memory-mcp cli --json index_repository '{"repo_path":"fastapi"}'` then `search_graph`/`trace_path --direction inbound` | Q1/Q2: `solve_dependencies` · Q3: `jsonable_encoder` | `cbm_q1.txt`, `cbm_q2.txt` |
| Serena | `serena project create --language python` (root = `fastapi/`, not repo root — see errata below) then `find_symbol`/`find_referencing_symbols` via streamable-http MCP | `solve_dependencies`, `jsonable_encoder` | `serena_results.json`, `serena_q3q6q7_raw.json`, `serena_query.py`, `serena_query2.py`, `serena_server.log`, `serena_server2.log`, `serena_query_err.log` |
| graphify | `/graphify fastapi/` (live agent skill run, not CLI — see protocol round 3 for why) | "who calls jsonable_encoder" | `graphify_GRAPH_REPORT.md`, `graphify_q3.txt`, `graphify_q7.txt` |
| Q7 canary target | — | `resolve_response_model_overrides` (0 real hits, grep-confirmed) | included in the Q3/Q7 files above |
| **Control experiment (2026-09-10)** | `serena project create --language python` at **repo root** (`.`, not `fastapi/`), `xvfb-run -a serena start-mcp-server --transport streamable-http --port 8766 --project .`, then `find_symbol` / `find_referencing_symbols` via the same streamable-http MCP client pattern | `solve_dependencies` (`relative_path: fastapi/dependencies/utils.py`) | `serena_fastapi_root_control.json` |

**Known caveat on this repo, now resolved by controlled experiment:** the original pilot indexed Serena with project root = `fastapi/` (the nested package), not the repo root. Absolute imports (`from fastapi.dependencies.utils import ...`) failed to resolve against that root, causing Serena to silently undercount references (1/4 and later 0/12).

**Control experiment result:** on 2026-09-10, the same repo at the same pinned SHA was re-cloned fresh and indexed a second time with Serena's project root set to the **repository root** instead of `fastapi/`. Querying `find_referencing_symbols` on the identical symbol (`solve_dependencies`) returned **4/4 real references** — the 3 call sites in `fastapi/routing.py` (lines 480, 782, 2233) plus the self-recursive call in `fastapi/dependencies/utils.py` (line 639) — versus 1/4 recall from the original nested-root pilot. Indexing also completed in ~3 seconds with no timeout, unlike the original attempt. This confirms the root-scope misconfiguration as the established cause of the undercount, not merely a hypothesis: **Serena/pyright needs the actual repository root as its project root to resolve absolute-import references correctly; scoping it to a subpackage silently breaks reference resolution for any code that imports that subpackage by its absolute path.** Raw MCP client output saved as `serena_fastapi_root_control.json`.

---

## 2. pydantic — `pydantic/pydantic`

- Full SHA: `831893ed0411d45c20aacae88e067c9c33a89501`
- Commit date: 2026-09-09T15:58:19+02:00
- Scope: `pydantic/` — **105 `.py` files**
- Round: 4
- Raw files: `raw-data/pydantic/`

| Tool | Command | Query text | Raw file |
|---|---|---|---|
| code-review-graph | `code-review-graph build --repo pydantic` (run one level **above** `pydantic/pydantic/` — running from inside the package dir triggers the stdlib-`types.py`-shadowing bug, see protocol) then `query --repo pydantic callers_of <target>` | Q3 target + `resolve_deferred_annotation_cache` (Q7 canary) | `pyd_crg_q3.txt`, `pyd_crg_q7_reconstructed.txt` |
| codebase-memory-mcp | `index_repository` (same parent-dir caveat as CRG) then `search_graph --project home-claude-benchmark-v2-repos-pydantic-pydantic --name-pattern <target>` | same two targets | `pyd_cbm_q3.txt`, `pyd_cbm_q7_reconstructed.txt` |
| Serena | MCP session, `find_referencing_symbols` | round-4 Q3 target | `pyd_serena_raw.json`, `serena_pydantic.log`, `serena_query_pydantic.py` |
| graphify | `/graphify pydantic/` (real semantic extraction — first live subagent dispatch of the benchmark, see round 3 methodology) | Q3 target + `resolve_deferred_annotation_cache` | `pyd_graphify_q3.txt`, `pyd_graphify_q7.txt` |

**Provenance note:** the two `_reconstructed` files were regenerated 2026-09-10 at the same pinned SHA (original raw Q7 output wasn't saved to disk in the live run) — see the audit section at the end of the protocol.

---

## 3. ng-mocks — `help-me-mom/ng-mocks`

- Full SHA: `f5bdf1fc4e7d4b87fbd3b17178cffe65bf036508`
- Commit date: 2026-09-09T12:43:21+00:00
- Scope: `libs/ng-mocks/src/` — **313 `.ts` files**
- Round: 5
- Raw files: `raw-data/ng-mocks/`

| Tool | Command | Query text | Raw file |
|---|---|---|---|
| code-review-graph | `code-review-graph build --repo libs/ng-mocks/src` then `query --repo libs/ng-mocks/src callers_of MockBuilder` / `callers_of reflectTemplate` | Q3: `MockBuilder` · Q7: `reflectTemplate` (canary — confirmed drift, symbol no longer exists under that name, see protocol "Шаг 0") | `ngm_crg_q3_reconstructed.txt`, `ngm_crg_q7_reconstructed.txt` |
| codebase-memory-mcp | `index_repository` then `search_graph --project home-claude-benchmark-v2-repos-ng-mocks-libs-ng-mocks-src --name-pattern <target>` | same two targets | `ngm_cbm_q3_reconstructed.txt`, `ngm_cbm_q7_reconstructed.txt` |
| Serena | MCP session, `find_symbol`/`find_referencing_symbols` (overload disambiguation required for `MockBuilder`) | `MockBuilder`, `reflectTemplate` | `ngm_serena_raw.json`, `serena_ngmocks.log`, `serena_query_ngmocks.py` |
| graphify | `graphify . --no-viz` (code-only, 0 docs → fast-path, no LLM) then `graphify query "callers of MockBuilder"` / `graphify query "callers of reflectTemplate"` | **Phrasing matters** — `"callers of X"` gives the clean result reported in the protocol; the alternate phrasing `"who calls reflectTemplate"` instead fuzzy-matches on the word "calls" and returns a spurious node — see item 4 below and `ngm_graphify_q7_altphrasing.txt` | `ngm_graphify_q3_reconstructed.txt`, `ngm_graphify_q7_reconstructed.txt`, `ngm_graphify_q7_altphrasing.txt` |

---

## 4. next.js — `vercel/next.js`

- Full SHA: `4d621240c38ebceeac693951d7c6b04636632adc`
- Commit date: 2026-09-09T20:39:37+02:00
- Scope: sparse checkout `packages/next/src` — **methodological note: the actual indexed scope was ~2140–2423 files (includes `compiled/`, 863 vendored files), not the intended clean 1,644**; this over-scoping is faithfully preserved in the reconstruction, not fixed (see protocol round 6)
- Round: 6
- Raw files: `raw-data/nextjs/`

| Tool | Command | Query text | Raw file |
|---|---|---|---|
| code-review-graph | `code-review-graph build --repo packages/next/src` (2140 files / 61,663 nodes / 415,657 edges) then `query --repo packages/next/src callers_of renderToHTMLImpl` (ambiguous — 2 candidates, disambiguate to `server/render.tsx::renderToHTMLImpl`) / `callers_of resolveDeferredHydrationBoundary` | Q3: `renderToHTMLImpl` (real ground truth = 2 files after excluding the `base-server.ts` name collision) · Q7: `resolveDeferredHydrationBoundary` | `nj_crg_q3_reconstructed.txt`, `nj_crg_q7_reconstructed.txt` |
| codebase-memory-mcp | `index_repository` (72,726 nodes / 452,071 edges) then `search_graph --project home-claude-benchmark-v2-repos-nextjs-packages-next-src --name-pattern <target>` | same two targets | `nj_cbm_q3_reconstructed.txt`, `nj_cbm_q7_reconstructed.txt` |
| Serena | MCP session | round-6 targets | `nextjs_serena_raw.json`, `serena_nextjs.log`, `serena_query_nextjs.py` |
| graphify | detect finds 3.63M words → exceeds the 2M-word SKILL.md threshold → auto-narrows to `server/` (556 files, top-1 by file count after `compiled/`) → `graphify . --no-viz` in `server/` (code-only fast-path) then `graphify query "callers of renderToHTMLImpl"` / `"callers of resolveDeferredHydrationBoundary"` | same two targets, narrowed scope | `nj_graphify_q3_reconstructed.txt`, `nj_graphify_q7_reconstructed.txt` |

---

## 5. Mockito — `mockito/mockito`

- Full SHA: `9c5f36fb9f2ad89fbaab828d33d144cd398a4079`
- Commit date: 2026-09-09T08:49:38-05:00
- Scope: `mockito-core/src/main/java/` — **483 `.java` files**
- Round: 7
- Raw files: `raw-data/mockito/`

| Tool | Command | Query text | Raw file |
|---|---|---|---|
| code-review-graph | `code-review-graph build --repo mockito-core/src/main/java` then `query callers_of mockingProgress` / `callers_of resolveDeferredMockChain` | Q3: `ThreadSafeMockingProgress.mockingProgress` · Q7: `resolveDeferredMockChain` | `mockito_crg_q3.txt`, `mockito_crg_q7.txt` |
| codebase-memory-mcp | `index_repository` then `search_graph`/`trace_path` | same two targets | `mockito_cbm_q3.txt`, `mockito_cbm_q7.txt` |
| Serena | **install FAILED** — Gradle bootstrap blocked by sandbox egress (`services.gradle.org` 403) — not a tool defect, a sandbox network-allowlist limitation | — | — (no raw file — install never completed) |
| graphify | `graphify . --no-viz` (fast-path, no LLM) then `graphify query "callers of mockingProgress"` / `"callers of resolveDeferredMockChain"` | same two targets | `mockito_graphify_q3.txt`, `mockito_graphify_q7.txt` |

---

## 6. unity-mcp — `justinpbarnett/unity-mcp`

- Full SHA: `2fcc17957823f2494b7b1f7ade92c0fb56f4adb1`
- Commit date: 2026-09-05T17:16:29-04:00
- Scope: `MCPForUnity/` only — **310 `.cs` files** (explicitly excludes `TestProjects/`, 398 `.cs` files, and the Python `Server/`, 230 `.py` files)
- Round: 8
- Raw files: `raw-data/unity-mcp/`

| Tool | Command | Query text | Raw file |
|---|---|---|---|
| code-review-graph | `code-review-graph build --repo MCPForUnity` (310 files / 3300 nodes / 22602 edges) then `query callers_of ToolParams.Get` / `callers_of ResolveDeferredAssetBinding` | Q3: `ToolParams.Get` (ground truth: 198 call sites / 39 files) · Q7: `ResolveDeferredAssetBinding` | `unity_crg_q3.txt`, `unity_crg_q3_callers.json`, `unity_crg_q7.txt` |
| codebase-memory-mcp | `index_repository` (6319 nodes / 28187 edges, 5 parse_partial files) then `search_graph`/`trace_path` | same two targets | `unity_cbm_q3.txt`, `unity_cbm_q7.txt` |
| Serena | **install FAILED** — requires .NET runtime 10.0, blocked both via `dot.net` (403) and Ubuntu's own `security.ubuntu.com` mirror (403) | — | — |
| graphify | `/graphify MCPForUnity/` — real semantic extraction (README.md + package-icon.png, 83.5s, 80,575 input tokens) + AST (1 partial-parse file, `PhysicsSimulationOps.cs`) then `graphify query "callers of Get"` / `"callers of ResolveDeferredAssetBinding"` | same two targets | `unity_graphify_q3.txt`, `unity_graphify_q7.txt`, `graphify_GRAPH_REPORT.md` |

---

## 7. rest-assured — `rest-assured/rest-assured`

- Full SHA: `75ef4d541ab126fa0cfb05fdb672bfdf5b8efb20`
- Commit date: 2026-07-22T10:35:06+02:00
- Scope: `rest-assured/src/main/` — **191 files (129 `.java` + 62 `.groovy`)**
- Round: 9
- Raw files: `raw-data/rest-assured/`

| Tool | Command | Query text | Raw file |
|---|---|---|---|
| code-review-graph | `code-review-graph build --repo rest-assured/src/main` (parses only the 129 Java files — all 62 Groovy files silently dropped, no build-time warning) then `query importers_of RestAssuredConfig` | Q3: `RestAssuredConfig` (class, not method) · Q7: `resolveDeferredAuthChain` | `ra_crg_q3_importers.json`, `ra_crg_q7.txt` |
| codebase-memory-mcp | `index_repository` (3053 nodes / 13471 edges, 24 parse_partial — all Groovy) then `trace_path --direction inbound` | same two targets | `ra_cbm_q3.txt`, `ra_cbm_q7.txt` |
| Serena | **install FAILED** — same Gradle-bootstrap block as Mockito | — | — |
| graphify | `graphify . --no-viz` (0 real non-code files → fast-path; AST attempts Groovy too, 15/62 files syntax-error, 2 with zero extracted symbols) then `graphify query "callers of RestAssuredConfig"` / `"callers of resolveDeferredAuthChain"` | same two targets | `ra_graphify_q3.txt`, `ra_graphify_q7.txt` |

---

## 8. n8n — `n8n-io/n8n`

- Full SHA: `b4fee56db391c7f65dec72d0f23e79f07b472423`
- Commit date: 2026-09-09T18:59:54+00:00
- Scope: sparse checkout `packages/core`, `packages/workflow`, `packages/cli/src`; actual Q3/Q7 target scope narrowed to `packages/workflow/src` — **124 files**
- Round: 10
- Raw files: `raw-data/n8n/`

| Tool | Command | Query text | Raw file |
|---|---|---|---|
| code-review-graph | `code-review-graph build --repo packages/workflow/src` (124 files / 1533 nodes / 7734 edges) then `query callers_of deepCopy` / `callers_of resolveDeferredNodeBinding` | Q3: `deepCopy` (utils.ts:57, ground truth: 17 call sites / 4 files) · Q7: `resolveDeferredNodeBinding` | `n8n_crg_q3.json`, `n8n_crg_q7.txt` |
| codebase-memory-mcp | `index_repository` (1963 nodes / 5600 edges, 0 parse_partial) then `search_graph`/`trace_path` | same two targets | `n8n_cbm_q3.txt`, `n8n_cbm_q7.txt` |
| Serena | MCP session, clean install (predisposed TS toolchain) — **best Serena result of the benchmark**, full & correct recall on `deepCopy` | `deepCopy`, canary | `n8n_serena_raw.json`, `serena_query_n8n.py` |
| graphify | `graphify . --no-viz` in `packages/workflow/src` (fast-path) then `graphify query "callers of deepCopy"` / `"callers of resolveDeferredNodeBinding"` | same two targets | `n8n_graphify_q3.txt`, `n8n_graphify_q7.txt` |

**n8n `deepCopy` call-site count — reconciled 2026-09-10 (nice-to-have #2, resolved):** the protocol's per-file breakdown ("utils.ts 2, node-helpers.ts 11, global-state.ts 1, workflow-data-proxy.ts 1") sums to 15, not the 17 stated as the total — an internal arithmetic mismatch. Re-verified against a fresh clone at the pinned SHA:
```
$ grep -rn "deepCopy(" packages/workflow/src | grep -v "function deepCopy"
utils.ts: 2 call sites (lines 80, 89 — self-recursive, inside deepCopy's own body)
node-helpers.ts: 13 call sites (lines 861, 869, 886, 892, 903, 937, 941, 972, 983, 986, 999, 1151, 1299)
global-state.ts: 1 call site (line 14)
workflow-data-proxy.ts: 1 call site (line 367, inside an anonymous getter)
```
**Total: 17 real call sites in 4 files — the headline total of 17 was correct; the sub-count of "11" given for node-helpers.ts was the actual error (true count is 13).** This doesn't change anything used in the article, which cites only the 17/4-files headline number, not the per-file breakdown.

---

## 9. ripgrep — `BurntSushi/ripgrep`

- Full SHA: `3fce3b5bb0236da2df6d99672afb8a719642eca7`
- Commit date: 2026-08-04T10:00:08-04:00
- Scope: `crates/` (11 workspace crates) — **95 `.rs` files**
- Round: 11
- Raw files: `raw-data/ripgrep/`

| Tool | Command | Query text | Raw file |
|---|---|---|---|
| code-review-graph | `code-review-graph build --repo crates` (97 files / 3387 nodes / 28345 edges) then `query callers_of add_child` / `callers_of resolve_deferred_ignore_chain` | Q3: `Ignore::add_child` (raw fan-in 40 — 24 are `#[cfg(test)]` self-file calls, production ground truth = 4 calls / 2 files) · Q7: `resolve_deferred_ignore_chain` | `rg_crg_q3.json`, `rg_crg_q7.txt` |
| codebase-memory-mcp | `index_repository` (4464 nodes / 22717 edges) then `search_graph`/`trace_path --include-tests false` **and** `--include-tests true` (documented to filter tests; output is byte-identical either way — the flag does not detect `#[cfg(test)]`) | same target, both flag states | `rg_cbm_q3.txt`, `rg_cbm_q3_withtests.txt`, `rg_cbm_q7.txt` |
| Serena | **install FAILED** — LSP `initialize` crash; root cause `static.rust-lang.org` 403, but the surfaced error is a ~15KB unreadable traceback (least diagnosable Serena failure of the benchmark) | — | — |
| graphify | `graphify . --no-viz` in `crates/` (fast-path, 0 syntax errors) then `graphify query "callers of add_child"` / `"callers of resolve_deferred_ignore_chain"` | Q7 **canary failed here** — `resolve_deferred_ignore_chain` fuzzy-expanded to real nodes `Ignore`/`resolve_git_commondir()` instead of returning "not found" (first canary failure after 6 clean rounds) | `rg_graphify_q3.txt`, `rg_graphify_q7.txt` |

---

## 10. gin — `gin-gonic/gin`

- Full SHA: `dcaa4296d111981ffb31ac3eba90bb63e1eb5ab9`
- Commit date: 2026-08-15T13:44:19+08:00
- Scope: repo root + subpackages `binding/`, `render/`, `internal/`, `codec/` — **99 `.go` files (59 production + 40 test)**
- Round: 12
- Raw files: `raw-data/gin/`

| Tool | Command | Query text | Raw file |
|---|---|---|---|
| code-review-graph | `code-review-graph build --repo .` (110 files / 1630 nodes / 18010 edges) then `query callers_of validate` (target has 2 build-tag-exclusive definitions: `binding.go` `//go:build !nomsgpack` vs `binding_nomsgpack.go` `//go:build nomsgpack`) / `callers_of resolveBindingChain` | Q3: `binding.validate` (ground truth: 16 callers = 11 production/9 files + 5 test) · Q7: `resolveBindingChain` | `gin_crg_q3.json`, `gin_crg_q7.txt` |
| codebase-memory-mcp | `index_repository` (2328 nodes / 11786 edges) then `search_graph`/`trace_path --include-tests false` and `true` | same target, both flag states | `gin_cbm_q3.txt`, `gin_cbm_q3_withtests.txt`, `gin_cbm_q7.txt` |
| Serena | **install FAILED** — `go.mod` requires go1.25.0, local toolchain 1.24.7, `GOTOOLCHAIN=auto` blocked by `proxy.golang.org` 403; Serena's own diagnostic misreports this as "Go is not installed" | — | — |
| graphify | `/graphify .` — real semantic extraction (21 doc files, 183K input tokens) + AST (1673 nodes/4599 edges) then `graphify query "who calls validate in binding"` / query mentioning the word "function" (unintentionally triggers a second, unrelated fuzzy match on a real `function()` node in `recovery.go`) | Q3 **extraction-level failure**: the single `calls` edge to `validate()` is missing from `graph.json` entirely (confirmed by direct inspection, not a query-traversal bug) · Q7 clean | `gin_graphify_q3.txt`, `gin_graphify_q7.txt`, `GRAPH_REPORT.md` |

---

## 11. bbolt — `etcd-io/bbolt`

- Full SHA: `c93ba6647e844212948a2064b916360daebc5f50`
- Commit date: 2026-09-07T16:51:28+01:00
- Scope: repo root — **121 `.go` files (75 production + 46 test)**
- Round: 13
- Raw files: `raw-data/bbolt/`

| Tool | Command | Query text | Raw file |
|---|---|---|---|
| code-review-graph | `code-review-graph build --repo .` (143 files / 1232 nodes / 15363 edges) then `query callers_of mmap` (5-way OS-tag-duplicated free function `mmap(db *DB, sz int) error`, distinct from method `(db *DB) mmap(minsz int) error`) / `callers_of resizeMmapRegion` | Q3: free-function `mmap` (ground truth: 1 caller, `DB.mmap` at db.go:516) and method `DB.mmap` (ground truth: 2 callers — `Open`, `DB.allocate`) · Q7: `resizeMmapRegion` | `bbolt_crg_q3.json`, `bbolt_crg_q7.txt` |
| codebase-memory-mcp | `index_repository` (1523 nodes / 10728 edges, 0 parse_partial) then `search_graph`/`trace_path --include-tests false` and `true` | same targets, both flag states | `bbolt_cbm_q3.txt`, `bbolt_cbm_q3_withtests.txt`, `bbolt_cbm_q7.txt` |
| Serena | **install FAILED** — identical `proxy.golang.org` block, reproduced independently on a second, unrelated Go repo/go.mod version | — | — |
| graphify | `graphify . --no-viz` (fast-path, 125 code + 25 doc → mostly CI workflows, AST-only) then `graphify query "callers of mmap"` / `"callers of resizeMmapRegion"` | same targets — **this is the source for evidence item bbolt/mmap below** | `bbolt_graphify_q3.txt`, `bbolt_graphify_q7.txt`, `GRAPH_REPORT.md` |

**mmap ground-truth verification command (bbolt):**
```
grep -rn 'mmap(' --include='*.go' . | grep -v '_test.go'
```

---

## 12. ktor-http — `ktorio/ktor`

- Full SHA: `166c52b3b6cb548333991efe14bc0852a0e908a2`
- Commit date: 2026-09-09T12:22:52+00:00
- Scope: `ktor-http` module (includes nested `ktor-http-cio`) — **136 `.kt` files** (out of a 2,415-file monorepo — repo root is unusable as a single-round scope)
- Round: 14
- Raw files: `raw-data/ktor-http/`

| Tool | Command | Query text | Raw file |
|---|---|---|---|
| code-review-graph | `code-review-graph build --repo ktor-http` (136 files / 1513 nodes / 10782 edges) then `query callers_of parseHeaderValue` — target has **3-way name ambiguity**: 1-arg overload (HttpHeaderValueParser.kt:85), 2-arg overload (line 96), and an unrelated same-name function in a different module (`ktor-http-cio/.../HttpParser.kt:277`) | Q3: `parseHeaderValue` (ground truth: 1-arg = 5 callers/4 files, 2-arg = 1 caller, CIO version = 1 caller) · Q7: `resolveHeaderValueCache` | `ktor_crg_q3.json`, `ktor_crg_q7.txt` |
| codebase-memory-mcp | `index_repository` (2056 nodes / 9926 edges, 0 parse_partial) then `search_graph`/`trace_path --include-tests false` and `true` | same target, both flag states | `ktor_cbm_q3.txt`, `ktor_cbm_q3_withtests.txt`, `ktor_cbm_q7.txt` |
| Serena | **install FAILED** — `download-cdn.jetbrains.com` 403 (5th independent sandbox-egress block of the benchmark) | — | — |
| graphify | `/graphify ktor-http/` — real semantic extraction of 1 PDF (job-hierarchy diagram, vision subagent, 9 nodes/17 edges) + AST (1 syntax-error file, `CommonHeadersTest.kt`, backtick test names) then `graphify query "callers of parseHeaderValue"` (both overloads) and against the CIO version — **only tool of the three that correctly kept all 3 candidate nodes distinct AND resolved both queries correctly** | same targets — **this is the source for evidence item ktor/parseHeaders below** | `ktor_graphify_q3.txt`, `ktor_graphify_q7.txt`, `GRAPH_REPORT.md` |

**parseHeaderValue ground-truth verification commands (ktor-http):**
```
grep -rn 'parseHeaderValue(' --include='*.kt' ktor-http/
```
Manual read of each call site to classify by which of the 3 overload/module candidates it targets (grep alone can't disambiguate — see evidence index below for the actual classification and the direct `graph.json` node check).

---

## Corpus-wide notes

- All "0 hits" Q7 canary targets were confirmed via `grep -rn` across the full indexed scope before being used, per protocol §5 Step 0 ("hallucination canary" selection recipe) — this grep is the ground-truth check, not the tool being tested.
- Where a tool's install failed outright (Serena on Mockito/unity-mcp/rest-assured/ripgrep/gin/bbolt/ktor-http), no raw query file exists for that cell — the failure itself (error text, blocked host, confirmed via `$HTTPS_PROXY/__agentproxy/status`) is documented in prose in the corresponding protocol round, not as a separate raw file, since there was no successful run to capture output from.
- `graphify`'s `GRAPH_REPORT.md` files are the tool's own Step 4.5 health-check output (dangling-edge percentage etc.) — one per round where it was generated, referenced above per repo where present.
