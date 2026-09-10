# Sources and licenses

This archive's own content (the protocol, the dev.to article draft, the reproducibility manifest,
the evidence index, and the token-counting script) is original work by the author and is released
under the MIT license in `LICENSE` at the root of this archive.

The `raw-data/` directory contains **tool output** (query results, JSON, log files) produced by
running code-graph/retrieval tools against 12 third-party open-source repositories, plus one full
packed copy of a repository subset (`raw-data/fastapi/repomix_fastapi.txt`, produced by `repomix`
for the token-count comparison in round 1 — this is the one file in the archive that is a
substantial copy of upstream source, not just a tool's query output). None of the third-party
source code itself is otherwise redistributed here beyond short excerpts (function/class names,
file paths, line numbers, and small code snippets shown inline in raw query responses) that these
tools return as part of answering a query.

Every repository below is used at the exact pinned commit given in `reproducibility-manifest.md`,
under its own license as published by its maintainers. Nothing here modifies or relicenses any
upstream project; this table exists so a reader can see at a glance what each source project's
license permits before relying on or redistributing the corresponding raw-data files.

| Repository | License | License file (at pinned SHA) |
|---|---|---|
| `fastapi/fastapi` | MIT | [LICENSE](https://github.com/fastapi/fastapi/blob/50113da16fec53b66b80d75e80a89296de4fa5a5/LICENSE) |
| `pydantic/pydantic` | MIT | [LICENSE](https://github.com/pydantic/pydantic/blob/831893ed0411d45c20aacae88e067c9c33a89501/LICENSE) |
| `help-me-mom/ng-mocks` | MIT | [LICENSE](https://github.com/help-me-mom/ng-mocks/blob/f5bdf1fc4e7d4b87fbd3b17178cffe65bf036508/LICENSE) |
| `vercel/next.js` | MIT | [license.md](https://github.com/vercel/next.js/blob/4d621240c38ebceeac693951d7c6b04636632adc/license.md) |
| `mockito/mockito` | MIT | [LICENSE](https://github.com/mockito/mockito/blob/9c5f36fb9f2ad89fbaab828d33d144cd398a4079/LICENSE) |
| `justinpbarnett/unity-mcp` | MIT | [LICENSE](https://github.com/justinpbarnett/unity-mcp/blob/2fcc17957823f2494b7b1f7ade92c0fb56f4adb1/LICENSE) |
| `rest-assured/rest-assured` | Apache License 2.0 | [LICENSE](https://github.com/rest-assured/rest-assured/blob/75ef4d541ab126fa0cfb05fdb672bfdf5b8efb20/LICENSE) |
| `n8n-io/n8n` | **Sustainable Use License** (custom, not OSI-approved — see note below) | [LICENSE.md](https://github.com/n8n-io/n8n/blob/b4fee56db391c7f65dec72d0f23e79f07b472423/LICENSE.md) |
| `BurntSushi/ripgrep` | Dual-licensed: MIT **or** Unlicense (public domain) | [LICENSE-MIT](https://github.com/BurntSushi/ripgrep/blob/3fce3b5bb0236da2df6d99672afb8a719642eca7/LICENSE-MIT), [UNLICENSE](https://github.com/BurntSushi/ripgrep/blob/3fce3b5bb0236da2df6d99672afb8a719642eca7/UNLICENSE) |
| `gin-gonic/gin` | MIT | [LICENSE](https://github.com/gin-gonic/gin/blob/dcaa4296d111981ffb31ac3eba90bb63e1eb5ab9/LICENSE) |
| `etcd-io/bbolt` | MIT | [LICENSE](https://github.com/etcd-io/bbolt/blob/c93ba6647e844212948a2064b916360daebc5f50/LICENSE) |
| `ktorio/ktor` | Apache License 2.0 | [LICENSE](https://github.com/ktorio/ktor/blob/166c52b3b6cb548333991efe14bc0852a0e908a2/LICENSE) |

**Note on n8n's license:** n8n's "Sustainable Use License" is source-available but not a standard
permissive open-source license — it restricts certain commercial uses and excludes `.ee.`-named
enterprise files entirely. The raw-data files here (`n8n/n8n_*.txt`, `n8n/n8n_*.json`) contain only
short tool-query excerpts (function names, file paths, line numbers) from `packages/workflow/src`,
not `.ee.` files and not a substantial copy of the source tree — reviewed and believed to fall well
within fair-use/short-excerpt norms, but flagged explicitly here since n8n's terms are the one
license in this list that isn't a standard permissive grant.

**Note on ripgrep's dual license:** where ripgrep is used or excerpted, either the MIT or the
Unlicense terms may be relied on at the user's choice, per ripgrep's own licensing.

All twelve repositories were cloned fresh at their pinned commit for this benchmark and for the
2026-09-10 evidence reconstruction/verification pass documented in `evidence-index.md` — none of
the clones themselves are included in this archive (see `README.md`, "Not included here").
