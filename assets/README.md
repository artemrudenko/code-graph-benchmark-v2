# Publication images

| File | Purpose | Placement in the DEV article |
|---|---|---|
| images/cover-broken-edge-dev.png | Cover image, "The Broken Edge" concept, composed for DEV's 1000×420 recommendation | Upload as the DEV cover. It deliberately has no text or logo. The earlier `cover-broken-edge.png` is retained as the source concept. |
| images/cover-index-scope-dev-v2.png | DEV cover: an incomplete relationship map becomes a verified connected map | Upload as the DEV cover. It supports the article's question about whether compact context is safe to use, and its central composition is safe for a DEV page and a link-preview crop. |
| images/cover-index-scope-linkedin.png | Earlier standalone LinkedIn visual about a scope-control audit | Retained as an archive asset. Do not use it to promote the current article. |
| diagrams/code-context-lifecycle.png | A persistent-context lifecycle: configure, query, verify, change, refresh | After the opening problem statement. |
| diagrams/code-context-tool-jobs.png | Four code-context tool classes, grouped by the developer job they do | Retained in the evidence archive; no longer used by the article. |
| diagrams/evidence-at-a-glance.png | Four independently checked numeric findings, with their own denominators | Retained in the evidence archive; no longer used by the article. |
| diagrams/ktor-caller-disambiguation.png | Ktor: one true caller and 16 cross-attributed results | Retained as a benchmark artifact; no longer used by the article. |
| diagrams/fastapi-project-root-control.png | FastAPI setup audit: a nested package root finds 1 of 4 references; the repository root finds 4 of 4 for the same commit and symbol | Retained in the evidence archive; no longer used by the article. |
| diagrams/retrieval-trust-checks.png | Four checks before acting on compact code context | In "A small tutorial: test a code index in your repository." |
| diagrams/stale-index-control.png | A controlled source change adds a fifth caller after an index was built; compare freshness, verify source, then refresh | In "A map can become old." |
| diagrams/code-context-lifecycle-dark.png | Dark source version of the persistent-context lifecycle | Retained with its Mermaid and Excalidraw sources. |
| diagrams/code-context-lifecycle-article-dark.png | First large-type editorial iteration of the persistent-context lifecycle | Kept for provenance. |
| diagrams/code-context-lifecycle-article-large-dark.png | Mobile-readable editorial version of the persistent-context lifecycle | Used in the DEV article after the opening problem statement. |
| diagrams/code-context-tool-jobs-dark.png | Dark version of the tool-job map | Available as the matching dark alternative. |
| diagrams/stale-index-control-dark.png | Dark source version of the stale-index control | Retained with its Mermaid and Excalidraw sources. |
| diagrams/stale-index-control-article-dark.png | First large-type editorial iteration of the stale-index control | Kept for provenance. |
| diagrams/stale-index-control-article-large-dark.png | Mobile-readable editorial version of the stale-index control | Used in the DEV article in "An index can be correct and still be old." |

The Mermaid files and Excalidraw files are editable structural sources. The SVG and PNG are the publication figures; PNG is the upload-ready form for DEV. The article uses raw GitHub URLs for diagrams so the current unpublished DEV draft can display them. The cover must be uploaded through DEV.

The original light figures remain available. The article uses the dark variants
where a light diagram was previously embedded, so the evidence figures share a
single dark editorial palette.

## Standard for future diagrams

Use the installed `diagram` skill for a flow, architecture map, or evidence diagram. Its normal deliverable is Mermaid source, an editable Excalidraw scene for flowcharts, and rendered SVG and PNG. For a data-sensitive article figure, use that structure and finish typography in the SVG if needed. Inspect the PNG before publication, and keep labels short enough to fit their nodes.

Use image generation only for the cover and editorial illustrations, never for diagrams that state evidence. The evidence figures use exact research wording and values; keep their source wording synchronized with `docs/evidence-index.md`.

The reader-run testbench is text and tables rather than another diagram. Its
prompts, answer contract, and record sheet live in `docs/reader-run-testbench.md`.
