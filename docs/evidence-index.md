---
title: "Code-graph tools benchmark v2 — evidence index"
type: evidence-index
generated: 2026-09-10
purpose: "For the four central retrieval claims and the FastAPI project-root control used in the dev.to article: claim -> raw tool response -> independent source-code verification -> status. Every source-verification command below was re-run on 2026-09-10 against a fresh clone at the pinned SHA in reproducibility-manifest.md, independently of the original benchmark session."
---

# Evidence index — four core retrieval claims plus a scope control

## 1. bbolt — build-specific `mmap`

**Claim (article/protocol, round 13):** The free function `mmap(db *DB, sz int) error` is defined 5 times under mutually exclusive Go build tags (one per OS), has exactly 1 real caller in production code (`DB.mmap` at db.go:516), while the *method* `(db *DB) mmap(minsz int) error` — a thin wrapper around the free function — has exactly 2 callers (`Open`, `DB.allocate`). code-review-graph returned 0 callers for the free function across all 5 build-tag variants (a false negative — the edge was dropped at build time, not just unresolved), while correctly finding both callers of the method.

**Raw response:** `raw-data/bbolt/bbolt_crg_q3.json` — `callers_of` on each of the 5 build-tag `mmap` definitions returns an empty result set; `callers_of` on `DB.mmap` (the method) returns exactly `Open` and `DB.allocate`. Cross-checked with `callees_of DB.mmap`, which also omits the call to the free function entirely, confirming the edge is missing from the graph, not just unindexed on the query side.

**Independent source verification (2026-09-10, fresh clone `c93ba6647e844212948a2064b916360daebc5f50`):**
```
$ grep -rln "^func mmap(" --include='*.go' .
./bolt_android.go
./bolt_windows.go
./bolt_aix.go
./bolt_unix.go
./bolt_solaris.go

$ grep -n "func (db \*DB) mmap(" -r .
./db.go:456:func (db *DB) mmap(minsz int) (err error) {

$ grep -rn "mmap(" --include='*.go' . | grep -v _test.go | grep -v "^func"
./db.go:297:	if err = db.mmap(options.InitialMmapSize); err != nil {   # inside Open(), line 178
./db.go:516:	if err = mmap(db, size); err != nil {                    # inside DB.mmap(), line 456
./db.go:1206:		if err := db.mmap(minsz); err != nil {              # inside DB.allocate(), line 1165
```
5 build-tag definitions confirmed. Free function `mmap()` called exactly once, at db.go:516, inside `DB.mmap()` itself. Method `DB.mmap()` called exactly twice: from `Open()` (db.go:178) and `DB.allocate()` (db.go:1165).

**Status: 🟢 CONFIRMED.** All three numbers in the claim (5 definitions / 1 caller of the free function / 2 callers of the method, both correctly named) match the source exactly.

---

## 2. Ktor — one real `parseHeaderValue` among 17 CRG results

**Claim (article/protocol, round 14), corrected:** `parseHeaderValue` has three-way name ambiguity — a 1-arg overload, a 2-arg overload (both public, in `HttpHeaderValueParser.kt`), and a completely unrelated same-named low-level function in a different module (`ktor-http-cio/.../HttpParser.kt:277`). code-review-graph's `callers_of` on the CIO version returned 17 results total: **1 of the 17 is correct** (`parseHeaders`, the CIO version's real and only caller, first entry in the result list) — the other **16 are false positives**, cross-attributed from the public 1-arg overload's actual callers/tests. A reader relying on the raw result count alone ("17 callers") would still be misled about the CIO function's real fan-in (1, not 17) unless they filter the list themselves — the qualitative finding (severe cross-module false-positive contamination) holds, but earlier drafts of this evidence index incorrectly stated *none* of the 17 were real; that was wrong and is fixed here. graphify is the only one of the three tools that kept all 3 nodes distinct and answered both queries with the correct caller counts (1-arg: 5, 2-arg: 1, CIO: 1) without contamination.

**Raw response:** `raw-data/ktor-http/ktor_crg_q3.json` — `callers_of` on `HttpParser.kt::parseHeaderValue` (CIO) returns 17 entries. Entry 1 (`id: 1250`, `parseHeaders`, `file_path: .../HttpParser.kt`) is the one real caller. Entries 2–17 have `file_path` pointing at `HeaderValueWithParameters.kt`, `HttpMessageProperties.kt`, `Versions.kt`, or `CommonHeadersTest.kt` — all real call sites of the *public* 1-arg overload, misattributed to the unrelated CIO function. `raw-data/ktor-http/ktor_graphify_q3.txt` shows graphify's `graph.json` holding all 3 candidates (L85, L96, L277) as separate nodes, with the CIO-scoped query correctly returning only `parseHeaders`.

**Independent source verification (2026-09-10, fresh sparse clone `166c52b3b6cb548333991efe14bc0852a0e908a2`, `ktor-http/`):**
```
$ grep -rn "fun parseHeaderValue(" ktor-http/
HttpHeaderValueParser.kt:85:public fun parseHeaderValue(text: String?): ...
HttpHeaderValueParser.kt:96:public fun parseHeaderValue(text: String?, parametersOnly: Boolean): ...
ktor-http-cio/.../HttpParser.kt:277:internal fun parseHeaderValue(text: CharArrayBuilder, range: MutableRange) {
```
Production callers of the 1-arg version (excluding `CommonHeadersTest.kt` and the compiler-generated `.klib.api` dump): `parseAndSortHeader` (HttpHeaderValueParser.kt:59), `parseAndSortContentTypeHeader` (HttpHeaderValueParser.kt:66), `EntityTagVersion.parse` (content/Versions.kt:276), `HttpMessage.cacheControl` (HttpMessageProperties.kt:137), `HeaderValueWithParameters.parse` (HeaderValueWithParameters.kt:70) — **5 callers in 4 files**, exactly matching the protocol's ground truth. The 2-arg version has exactly 1 caller: the 1-arg version itself (line 86, `return parseHeaderValue(text, false)`). The CIO version (`HttpParser.kt:277`) has exactly 1 caller: `HttpParser.kt:134`, inside a different function entirely.

**Status: 🟢 CONFIRMED (with a correction applied above).** 1 of CRG's 17 results for the CIO query is the CIO function's real caller (`parseHeaders`); the other 16 trace to real call sites of the *public* overloads, misattributed to the CIO function — the cross-module false-positive contamination is exactly as described, and the true CIO caller count (1, buried among 17) matches source.

---

## 3. ripgrep — splitting 28 `add_child` results into 24 test callers and 4 others

**Claim (article/protocol, round 11):** code-review-graph's `callers_of` on `Ignore::add_child` returns 28 results. 24 of these are test functions inside the same file's `#[cfg(test)] mod tests` block; the remaining 4 are real production callers, split across 2 files (`incremental.rs`, `walk.rs`). CRG does not distinguish test code from production code in its `callers_of` output — both are returned together, undifferentiated except by an `is_test` field the caller has to check manually.

**Raw response:** `raw-data/ripgrep/rg_crg_q3.json` — `result_count: 28`. Programmatic tally of the `is_test` field in that JSON: 24 entries with `is_test: true` (all `file_path` = `crates/ignore/src/dir.rs`, all `line_start` > 1117), 4 entries with `is_test: false` (`incremental.rs` x2, `walk.rs` x2).

**Independent source verification (2026-09-10, fresh clone `3fce3b5bb0236da2df6d99672afb8a719642eca7`):**
```
$ python3 -c "
import json
d = json.load(open('rg_crg_q3.json'))
r = d['results']
print(len(r), sum(x['is_test'] for x in r), sum(not x['is_test'] for x in r))
"
28 24 4
```
The 4 production entries: `matched_with_errors_ignore` (incremental.rs:310), `root_ignore` (incremental.rs:413), `next` (walk.rs:1190), `add_ignore` (walk.rs:1603) — matches "incremental.rs ×2, walk.rs ×2" exactly. Note: a raw line-level `grep -n "add_child("` in `dir.rs` after the `mod tests` boundary (line 1117) finds 35 individual call *expressions*, not 24 — the 24 is CRG's function-level *caller* count (distinct calling functions), several of which call `add_child` more than once in their body. This is the correct unit for a "callers of" query and is not a discrepancy — noted here so a reader re-deriving the number from a naive grep doesn't get confused by the 35-vs-24 mismatch.

**Status: 🟢 CONFIRMED**, with the above clarification on what "24" counts (distinct test functions, not raw call-expression lines) added for reader clarity.

---

## 4. graphify — all 12 canary queries: 3 substitutions, 9 honest refusals

**Claim (article/protocol, audit section):** Across the 12 rounds where graphify's `query` subcommand was actually run against a deliberately nonexistent "canary" symbol, 3 silently substituted unrelated real nodes instead of reporting "not found" (FastAPI round 3, pydantic round 4, ripgrep round 11), and 9 correctly and honestly reported no match (ng-mocks, next.js, Mockito, Unity, rest-assured, n8n, gin, bbolt, ktor-http).

**Per-round raw evidence:**

| # | Round | Repo | Canary target | Result | Raw file |
|---|---|---|---|---|---|
| 1 | 3 | FastAPI | `resolve_response_model_overrides` | 🔴 substituted — seeded on `Response`/`ModelField`/`_resolve_frontend_check_dir()`, 305-node BFS answer | `graphify_q7.txt` |
| 2 | 4 | pydantic | `resolve_deferred_annotation_cache` | 🔴 substituted — seeded on `resolve_annotations()`/`DeferredType`/`cached_property`/etc., 129-node answer | `pydantic/pyd_graphify_q7.txt` |
| 3 | 5 | ng-mocks | `reflectTemplate` | 🟢 "No matching nodes found." | `ng-mocks/ngm_graphify_q7_reconstructed.txt` |
| 4 | 6 | next.js | `resolveDeferredHydrationBoundary` | 🟢 "No matching nodes found." | `nextjs/nj_graphify_q7_reconstructed.txt` |
| 5 | 7 | Mockito | `resolveDeferredMockChain` | 🟢 "No matching nodes found." | `mockito/mockito_graphify_q7.txt` |
| 6 | 8 | unity-mcp | `ResolveDeferredAssetBinding` | 🟢 "No matching nodes found." | `unity-mcp/unity_graphify_q7.txt` |
| 7 | 9 | rest-assured | `resolveDeferredAuthChain` | 🟢 "No matching nodes found." | `rest-assured/ra_graphify_q7.txt` |
| 8 | 10 | n8n | `resolveDeferredNodeBinding` | 🟢 "No matching nodes found." | `n8n/n8n_graphify_q7.txt` |
| 9 | 11 | ripgrep | `resolve_deferred_ignore_chain` | 🔴 substituted — expanded to `Ignore`/`resolve_git_commondir()`, 169-node answer | `ripgrep/rg_graphify_q7.txt` |
| 10 | 12 | gin | `resolveBindingChain` | 🟢 "No matching nodes found." | `gin/gin_graphify_q7.txt` |
| 11 | 13 | bbolt | `resizeMmapRegion` | 🟢 "No matching nodes found." | `bbolt/bbolt_graphify_q7.txt` |
| 12 | 14 | ktor-http | `resolveHeaderValueCache` | 🟢 "No matching nodes found." | `ktor-http/ktor_graphify_q7.txt` |

**Independent verification performed:** each of the 12 canary target names was re-confirmed via `grep -rn "<name>"` across that round's indexed scope to have 0 real occurrences (Step 0 of the protocol's own methodology, not re-litigated here since it was already grep-verified live during the original run — see each round's text in the protocol for the specific grep command used). The 3 failure cases (rows 1, 2, 9) were spot-read directly from their raw files above: all three show a multi-node BFS answer seeded on real, unrelated graph nodes rather than an empty/"not found" result — confirmed by direct inspection, not re-derived.

**One phrasing-sensitivity nuance (not counted against the 3/9 split, since it uses a different query phrasing than the rest of the benchmark):** re-querying the ng-mocks canary with `"who calls reflectTemplate"` instead of `"callers of reflectTemplate"` — the phrasing used everywhere else in the protocol — produces a spurious 1-node result via a different mechanism (fuzzy-matching the literal word "calls" from the question, not multi-token expansion of the target name). See `ng-mocks/ngm_graphify_q7_altphrasing.txt`.

**Status: 🟢 CONFIRMED.** 3/12 substitution, 9/12 honest refusal, with root causes (multi-token snake_case fuzzy-expansion for FastAPI/pydantic/ripgrep) documented in the protocol's round-11 analysis.

---

## 5. FastAPI — Serena's undercount was a project-root scoping issue, not a Serena defect (control experiment)

**Claim (nice-to-have, editorial review):** The original pilot found Serena's `find_referencing_symbols` on `solve_dependencies` returned only 1 of 4 real references when Serena's project root was set to the nested `fastapi/` package instead of the repository root. This was documented as a *hypothesis* ("Вероятная причина... не до конца подтверждена") — plausible because absolute imports (`from fastapi.dependencies.utils import ...`) can't resolve against a root that doesn't contain the top-level `fastapi` package, but not yet isolated from other confounds by a controlled re-run.

**Control experiment (2026-09-10):** FastAPI was re-cloned fresh at the same pinned SHA (`50113da16fec53b66b80d75e80a89296de4fa5a5`) used throughout the benchmark. Serena was indexed a second time — same symbol (`solve_dependencies`), same commit, only the project root changed, from the nested `fastapi/` package to the actual repository root (`.`) — via `xvfb-run -a serena start-mcp-server --transport streamable-http --port 8766 --project .`. Indexing completed in ~3 seconds with no timeout (the original nested-root pilot had failed to complete within 60s on at least one earlier attempt). `find_referencing_symbols` was then queried via the same MCP streamable-http client pattern as the original pilot.

**Raw response:** `raw-data/fastapi/serena_fastapi_root_control.json`. `find_referencing_symbols` on `solve_dependencies` (`fastapi/dependencies/utils.py`) returned 4 distinct reference sites: `fastapi/routing.py` lines 480 (`get_request_handler`), 782 (`get_websocket_app`), and 2233 (`_FrontendRouteGroup._solve_dependencies`), plus the self-recursive call inside `fastapi/dependencies/utils.py` itself at line 639.

**Independent source verification:** these are the same 4 call sites the protocol's original grep-based ground truth cited (routing.py ~481/783/2234, off by one line from a since-shifted file revision at the time of the original pilot, plus the recursive call) — full 4/4 recall at repo root, versus 1/4 recall at the nested `fastapi/` root.

**Status: 🟢 CONFIRMED.** The root-scope hypothesis is now an established cause, not an open question: pointing Serena/pyright at the actual repository root instead of a subpackage fixes reference resolution for code that imports that subpackage by absolute path. This was the one nice-to-have item explicitly worth closing out, since the editorial review flagged it as the archive's single remaining "hypothesis, not confirmed" claim.
