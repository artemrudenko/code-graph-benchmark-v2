# Graph Report - fastapi  (2026-09-09)

## Corpus Check
- 56 files · ~71,838 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 804 nodes · 2044 edges · 38 communities
- Extraction: 88% EXTRACTED · 12% INFERRED · 0% AMBIGUOUS · INFERRED: 238 edges (avg confidence: 0.9)
- Token cost: 104,712 input · 0 output

## Community Hubs (Navigation)
- FastAPI App & Routing Core
- Pydantic v1/v2 Compat Layer
- OpenAPI Security Schemes
- JSON Encoders
- OpenAPI Models
- Dependency Injection & Concurrency
- Shipped Agent-Skill Docs
- Default Value Placeholders
- Background Tasks
- Exceptions
- Body Params & OpenAPI Examples
- WebSocket Routing
- CLI & Multipart Setup
- Route Matching
- Route Handling & Frontend Specificity
- Server-Sent Events (SSE)
- Lifespan Context Managers
- ORJSON Responses
- Low-Priority Route Matching
- OpenAPI Docs HTML (Swagger/ReDoc)
- Frontend Static Path Routing
- AsyncExitStack Middleware
- EmailStr Pydantic Type
- ASGI App Call Interface

## God Nodes (most connected - your core abstractions)
1. `ModelField` - 43 edges
2. `APIRouter` - 39 edges
3. `Response` - 38 edges
4. `Depends` - 38 edges
5. `APIRoute` - 35 edges
6. `FastAPI` - 33 edges
7. `Dependant` - 27 edges
8. `Example` - 25 edges
9. `lenient_issubclass()` - 24 edges
10. `HTTPException` - 24 edges

## Surprising Connections (you probably didn't know these)
- `get_dependant()` --calls--> `get_path_param_names()`  [INFERRED]
  dependencies/utils.py → utils.py
- `_get_openapi_operation_parameters()` --calls--> `lenient_issubclass()`  [INFERRED]
  openapi/utils.py → _compat/shared.py
- `get_openapi_path()` --calls--> `lenient_issubclass()`  [INFERRED]
  openapi/utils.py → _compat/shared.py
- `get_request_handler()` --calls--> `lenient_issubclass()`  [INFERRED]
  routing.py → _compat/shared.py
- `_populate_api_route_state()` --calls--> `lenient_issubclass()`  [INFERRED]
  routing.py → _compat/shared.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Avoid Ellipsis and RootModel in Pydantic models** — _agents_skills_fastapi_skill_ellipsis_avoidance, _agents_skills_fastapi_skill_rootmodel_avoidance, _agents_skills_fastapi_references_pydantic_ellipsis_avoidance, _agents_skills_fastapi_references_pydantic_rootmodel_avoidance [INFERRED 0.85]
- **Streaming response patterns (JSON Lines, SSE, bytes)** — _agents_skills_fastapi_references_streaming_json_lines, _agents_skills_fastapi_references_streaming_sse, _agents_skills_fastapi_references_streaming_bytes, _agents_skills_fastapi_skill_streaming [EXTRACTED 1.00]
- **Recommended tooling and libraries for FastAPI projects** — _agents_skills_fastapi_references_other_tools_asyncer, _agents_skills_fastapi_references_other_tools_sqlmodel, _agents_skills_fastapi_references_other_tools_httpx, _agents_skills_fastapi_references_other_tools_uv, _agents_skills_fastapi_references_other_tools_ruff, _agents_skills_fastapi_references_other_tools_ty [EXTRACTED 1.00]

## Communities (38 total, 0 thin omitted)

### Community 0 - "FastAPI App & Routing Core"
Cohesion: 0.05
Nodes (67): AbstractAsyncContextManager, FastAPI, Any, ASGIApp, BaseRoute, DecoratedCallable, deprecated, Doc (+59 more)

### Community 1 - "Pydantic v1/v2 Compat Layer"
Cohesion: 0.06
Nodes (84): _annotation_is_complex(), annotation_is_pydantic_v1(), _annotation_is_sequence(), field_annotation_is_complex(), field_annotation_is_scalar(), field_annotation_is_scalar_sequence(), field_annotation_is_sequence(), is_bytes_or_nonable_bytes_annotation() (+76 more)

### Community 2 - "OpenAPI Security Schemes"
Cohesion: 0.05
Nodes (41): json_schema_extra, OAuthFlowsModel, HTTPBase, HTTPBearer, OAuthFlows, pattern, HTTPAuthorizationCredentials, HTTPBase (+33 more)

### Community 3 - "JSON Encoders"
Cohesion: 0.05
Nodes (46): date, Decimal, Color, decimal_encoder(), generate_encoders_by_class_tuples(), isoformat(), jsonable_encoder(), Any (+38 more)

### Community 4 - "OpenAPI Models"
Cohesion: 0.07
Nodes (47): APIKey, APIKeyIn, BaseModelWithConfig, Components, Contact, Discriminator, Encoding, ExternalDocumentation (+39 more)

### Community 5 - "Dependency Injection & Concurrency"
Cohesion: 0.11
Nodes (37): AsyncExitStack, contextmanager_in_threadpool(), AbstractContextManager, _T, _CallIdentity, Dependant, _get_cache_key(), _get_computed_scope() (+29 more)

### Community 6 - "Shipped Agent-Skill Docs"
Cohesion: 0.10
Nodes (37): Avoid class dependencies, use factory functions, Dependency Injection Reference, Dependencies with yield and scope (request/function), Asyncer (asyncify/syncify), Other Tools Reference, HTTPX for HTTP communication, Ruff (lint/format), SQLModel for SQL databases (+29 more)

### Community 7 - "Default Value Placeholders"
Cohesion: 0.07
Nodes (20): Default(), DefaultPlaceholder, Any, DefaultType, Doc, GetJsonSchemaHandler, Move to a position in the file. Any next read or write will be done from that…, Close the file. To be awaitable, compatible with async, this is run in… (+12 more)

### Community 8 - "Background Tasks"
Cohesion: 0.15
Nodes (26): args, BackgroundTasks, Any, Doc, A collection of background tasks that will be called after a response has been…, Add a function to be called in the background after the response is sent. Read…, FastAPI framework, high performance, easy to learn, fast to code, ready for…, kwargs (+18 more)

### Community 9 - "Exceptions"
Cohesion: 0.12
Nodes (19): DependencyScopeError, EndpointContext, FastAPIError, Any, Doc, Exception, TypedDict, PydanticV1NotSupportedError (+11 more)

### Community 10 - "Body Params & OpenAPI Examples"
Cohesion: 0.21
Nodes (18): Example, TypedDict, Body, Cookie, File, Form, Header, Param (+10 more)

### Community 11 - "WebSocket Routing"
Cohesion: 0.09
Nodes (23): APIWebSocketRoute, _build_response_args(), _frontend_dependency_endpoint(), get_websocket_app(), _is_frontend_navigation_request(), _iter_accept_media_types(), _iter_included_route_candidates(), iter_route_contexts() (+15 more)

### Community 12 - "CLI & Multipart Setup"
Cohesion: 0.19
Nodes (8): main(), ensure_multipart_is_installed(), HTTPException, An HTTP exception you can raise in your own code to show errors to the client.…, _FrontendStaticFiles, StaticFiles, RuntimeError, stat_result

### Community 13 - "Route Matching"
Cohesion: 0.19
Nodes (6): SolvedDependency, Match, _frontend_path_specificity(), _FrontendRoute, _FrontendRouteGroup, URLPath

### Community 14 - "Route Handling & Frontend Specificity"
Cohesion: 0.32
Nodes (8): _frontend_scope_specificity(), _get_fastapi_scope(), _get_scope_effective_route_context(), _get_scope_included_router(), Receive, Scope, Send, _update_scope()

### Community 15 - "Server-Sent Events (SSE)"
Cohesion: 0.15
Nodes (14): model_validator, _check_event_single_line(), _check_id_valid(), _check_single_line(), EventSourceResponse, format_sse_event(), BaseModel, Doc (+6 more)

### Community 16 - "Lifespan Context Managers"
Cohesion: 0.14
Nodes (8): BaseException, _AsyncLiftContextManager, _DefaultLifespan, AbstractContextManager, _T, Wraps a synchronous context manager to make it async. This is vendored from…, Default lifespan context manager that runs on_startup and on_shutdown handlers.…, TracebackType

### Community 17 - "ORJSON Responses"
Cohesion: 0.19
Nodes (10): _OrjsonModule, ORJSONResponse, Any, deprecated, JSONResponse, Protocol, JSON response using the ujson library to serialize data to JSON.…, JSON response using the orjson library to serialize data to JSON.… (+2 more)

### Community 18 - "Low-Priority Route Matching"
Cohesion: 0.28
Nodes (3): _EffectiveRouteContext, _IncludedRouter, _restore_fastapi_scope_key()

### Community 19 - "OpenAPI Docs HTML (Swagger/ReDoc)"
Cohesion: 0.24
Nodes (11): HTMLResponse, get_redoc_html(), get_swagger_ui_html(), get_swagger_ui_oauth2_redirect_html(), _html_safe_json(), Any, Doc, Serialize a value to JSON with HTML special characters escaped. This prevents… (+3 more)

### Community 20 - "Frontend Static Path Routing"
Cohesion: 0.31
Nodes (6): _get_resolved_absolute_path(), _join_frontend_paths(), _normalize_frontend_path(), PathLike, Serve a static frontend build as low-priority routes. Use this for frontend…, _resolve_frontend_check_dir()

### Community 21 - "AsyncExitStack Middleware"
Cohesion: 0.25
Nodes (5): AsyncExitStackMiddleware, ASGIApp, Receive, Scope, Send

### Community 22 - "EmailStr Pydantic Type"
Cohesion: 0.36
Nodes (4): EmailStr, Any, GetJsonSchemaHandler, str

### Community 23 - "ASGI App Call Interface"
Cohesion: 0.50
Nodes (3): Receive, Scope, Send

## Knowledge Gaps
- **4 isolated node(s):** `Color`, `PyExtraColor`, `Serve Frontend Apps (app.frontend/router.frontend)`, `fastapi CLI (dev/run)`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 208 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `HTTPException` connect `CLI & Multipart Setup` to `FastAPI App & Routing Core`, `OpenAPI Security Schemes`, `JSON Encoders`, `OpenAPI Models`, `Background Tasks`, `Exceptions`, `Route Matching`, `Route Handling & Frontend Specificity`?**
  _High betweenness centrality (0.142) - this node is a cross-community bridge._
- **Why does `Response` connect `FastAPI App & Routing Core` to `JSON Encoders`, `OpenAPI Models`, `Dependency Injection & Concurrency`, `WebSocket Routing`, `CLI & Multipart Setup`?**
  _High betweenness centrality (0.106) - this node is a cross-community bridge._
- **Why does `get_request_handler()` connect `FastAPI App & Routing Core` to `Pydantic v1/v2 Compat Layer`, `Dependency Injection & Concurrency`, `Default Value Placeholders`, `Exceptions`, `WebSocket Routing`, `CLI & Multipart Setup`, `Route Handling & Frontend Specificity`, `Server-Sent Events (SSE)`?**
  _High betweenness centrality (0.087) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `APIRouter` (e.g. with `DefaultPlaceholder` and `FastAPIError`) actually correct?**
  _`APIRouter` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Color`, `PyExtraColor`, `Serve Frontend Apps (app.frontend/router.frontend)` to the rest of the system?**
  _4 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `FastAPI App & Routing Core` be split into smaller, more focused modules?**
  _Cohesion score 0.054758800521512385 - nodes in this community are weakly interconnected._
- **Should `Pydantic v1/v2 Compat Layer` be split into smaller, more focused modules?**
  _Cohesion score 0.05689548546691404 - nodes in this community are weakly interconnected._