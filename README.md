# code-graph-benchmark-v2

Research archive for choosing persistent code context for AI coding agents. The September 9–10, 2026 evidence pack covers source-checked retrieval cases from code-review-graph (CRG), codebase-memory-mcp (CBM), Serena, and graphify across 12 repositories and eight languages. A thirteenth repository, Cobra, was downloaded during selection but not benchmarked.

The question is whether compact retrieval preserves the code relationships an AI agent needs while reducing repeated navigation over time. The archive documents individual successes, omissions, ambiguous results, and a selection pilot. It does not measure end-to-end agent quality, total token savings, or establish a general winner.

## Start here

- [Standalone article draft](docs/devto-article-draft.md)
- [Selection and evaluation framework](docs/selection-and-evaluation-framework.md) — research objective, tool classes, question taxonomy, and the boundary between safe navigation evidence and workflow-payoff claims
- [Common agent questions](docs/agent-code-question-catalog.md) — refactor radius, duplicate code, regression and test decisions, with the evidence each one needs
- [Next benchmark design](docs/benchmark-next-step.md) — a small two-stage plan: valid setup gate, source-checked retrieval, then fixed change tasks in fresh clones
- [Controlled stale-index observation](docs/stale-index-control.md) — a normalized summary of the private FastAPI control: an old index missed one new caller until refresh, while source verification recovered the complete change set
- [Companion skills](skills/README.md) — `verify-code-context` and `maintain-code-context-index` make the article's identity, source-check, and freshness rules reusable in agent work
- [Reproducibility manifest](docs/reproducibility-manifest.md) — exact URL, full 40-char SHA, scope/exclusions, tool version, command, and query text for every (repo × tool × query) cell in the benchmark
- [Evidence index](docs/evidence-index.md) — the four central claims (bbolt/mmap, ktor/parseHeaderValue, ripgrep's 28-result split, all 12 graphify canary queries), each traced from raw tool output to an independently re-verified source-code check
- [Editorial audit and evidence gaps, in Russian](docs/editorial-review-ru.md) — the review that identified the gaps closed by the two files above
- [LinkedIn post draft](docs/linkedin-post-draft.md)
- [Original protocol and evolving run log](docs/code-graph-benchmark-v2-protocol.md)
- [Publication images](assets/README.md) — cover image and five article diagrams, with editable SVG sources and upload-ready PNG files

## Saved material

`raw-data/<repo>/` contains tool responses, Serena logs and query scripts, and graphify health reports. All saved tool outputs use paths relative to each repository root. The missing Q3/Q7 evidence for pydantic, ng-mocks, and Next.js was reconstructed on the pinned revisions on 2026-09-10 (files carry the `reconstructed` suffix); a previously-unsaved alternate-phrasing canary result for ng-mocks (`who calls reflectTemplate` vs `callers of reflectTemplate`) was also captured (`ngm_graphify_q7_altphrasing.txt`). `docs/reproducibility-manifest.md` lists exactly which (repo × tool × query) cells have a saved raw file and which don't (Serena's failed installs on 7 of 12 repos have no raw output to save, by nature — the failure itself is documented in the protocol's prose).

`scripts/count_tokens.js` counts the entire text of a supplied file with `gpt-tokenizer`. It requires that dependency to be installed. This archive has no automated pipeline that extracts comparable response payloads and generates result tables — every numeric claim in the article was read from the raw files by hand and cross-checked against `evidence-index.md`. The selection framework intentionally does not turn these cases into a single score.

## Reproduction

`docs/reproducibility-manifest.md` gives everything needed to re-run any cell of the benchmark: repo URL, full commit SHA, exact scope/exclusions as actually indexed (not just as intended — e.g. Next.js's round 6 accidentally-broad scope is documented, not silently corrected), tool version, install/build command, query text, and which raw file it corresponds to. The source clones, generated graph databases, and full benchmark runner are still not included (see "Not included here" below) — the manifest is what makes them reconstructible.

`docs/evidence-index.md` goes one step further for the four claims central to the article: it re-derives each number from a **fresh, independent clone** made on 2026-09-10 (not the raw files from the original run), so a reader can confirm the raw tool output matches reality, not just that the raw output matches what the protocol said about it.

## Not included here

The actual cloned repositories (~1.9GB total) were not copied into this folder — they're third-party code, not benchmark output, and fully reproducible via the SHAs in `docs/reproducibility-manifest.md`. Generated `node_modules/`, graph databases, and other ephemeral build artifacts were likewise excluded.

## Licensing

This archive's own content (protocol, article, manifest, evidence index, scripts) is MIT-licensed — see `LICENSE`. The 12 benchmarked repositories each keep their own upstream license; `SOURCES.md` links to every license file at the pinned commit, including a flag on n8n's non-standard "Sustainable Use License" and ripgrep's MIT/Unlicense dual license.

## Provenance

Assembled from a Cowork session that recorded the original tool runs on 2026-09-09/10, with an editorial review and evidence-pack backfill (manifest, evidence index, path cleanup, licensing) completed 2026-09-10. The DEV article draft remains unpublished. The public evidence package is available at https://github.com/artemrudenko/code-graph-benchmark-v2 and contains the material needed to inspect the reported cases and reconstruct a run from the manifest.
