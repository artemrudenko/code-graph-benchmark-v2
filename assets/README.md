# Publication images

| File | Purpose | Placement in the DEV article |
|---|---|---|
| images/cover-broken-edge.png | Cover image, "The Broken Edge" concept | Upload as the DEV cover. It deliberately has no text or logo. |
| diagrams/code-context-lifecycle.png | A persistent-context lifecycle: configure, query, verify, change, refresh | After the opening problem statement. |
| diagrams/code-context-tool-jobs.png | Four code-context tool classes, grouped by the developer job they do | After the question taxonomy. |
| diagrams/evidence-at-a-glance.png | Four independently checked numeric findings, with their own denominators | In "What the source checks found." |
| diagrams/ktor-caller-disambiguation.png | Ktor: one true caller and 16 cross-attributed results | After the Ktor explanation. |
| diagrams/retrieval-trust-checks.png | Four checks before acting on compact code context | In the selection-pilot section. |

The Mermaid files and Excalidraw files are editable structural sources. The SVG and PNG are the publication figures; PNG is the upload-ready form for DEV. The article uses raw GitHub URLs for diagrams so the current unpublished DEV draft can display them. The cover must be uploaded through DEV.

## Standard for future diagrams

Use the installed `diagram` skill for a flow, architecture map, or evidence diagram. Its normal deliverable is Mermaid source, an editable Excalidraw scene for flowcharts, and rendered SVG and PNG. For a data-sensitive article figure, use that structure and finish typography in the SVG if needed. Inspect the PNG before publication, and keep labels short enough to fit their nodes.

Use image generation only for the cover and editorial illustrations, never for diagrams that state evidence. The evidence figures use exact research wording and values; keep their source wording synchronized with `docs/evidence-index.md`.
