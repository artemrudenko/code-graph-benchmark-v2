# Graph Report - gin  (2026-09-09)

## Corpus Check
- 121 files · ~93,292 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 1711 nodes · 4051 edges · 102 communities (65 shown, 31 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 671 edges (avg confidence: 0.85)
- Token cost: 183,158 input · 0 output

## Community Hubs (Navigation)
- Context Abort/Status Tests
- Plain Text Binding
- Filesystem + Handler Chain
- Router Method Tree
- Context Get/Set + ResponseWriter
- Form Mapping (reflection binding)
- Engine Handler Dispatch
- Binding Content-Type Selection Tests
- Form Mapping Tests
- Render (JSON/XML/YAML/ASCII)
- Route Info + Param Binding
- Logger Middleware
- Protobuf Reflection Types
- Context.Next + H Map
- JSON Binding Custom Codec
- Community 16
- Community 17
- Community 18
- Community 19
- Community 20
- Community 21
- Community 22
- Community 23
- Community 24
- Community 25
- Community 26
- Community 27
- Community 28
- Community 29
- Community 30
- Community 31
- Community 32
- Community 33
- Community 34
- Community 35
- Community 36
- Community 37
- Community 38
- Community 39
- Community 40
- Community 41
- Community 42
- Community 43
- Community 44
- Community 45
- Community 46
- Community 47
- Community 48
- Community 49
- Community 51
- Community 52
- Community 53
- Community 54
- Community 55
- Community 56
- Community 57
- Community 58
- Community 59
- Community 60
- Community 61
- Community 62
- Community 63
- Community 64
- Community 65
- Community 66
- Community 67
- Community 68
- Community 69
- Community 70
- Community 71
- Community 72
- Community 73
- Community 74
- Community 75
- Community 76
- Community 77
- Community 78
- Community 79
- Community 80
- Community 81
- Community 82
- Community 83
- Community 84
- Community 85
- Community 86
- Community 87
- Community 88
- Community 89
- Community 90
- Community 91
- Community 92
- Community 93
- Community 94
- Community 96
- Community 97
- Community 100

## God Nodes (most connected - your core abstractions)
1. `CreateTestContext()` - 180 edges
2. `Context` - 156 edges
3. `New()` - 146 edges
4. `PerformRequest()` - 72 edges
5. `mappingByPtr()` - 60 edges
6. `Engine` - 51 edges
7. `requestWithBody()` - 35 edges
8. `IRoutes` - 35 edges
9. `SetMode()` - 31 edges
10. `RouterGroup` - 27 edges

## Surprising Connections (you probably didn't know these)
- `init()` --calls--> `SetMode()`  [INFERRED]
  response_writer_test.go → mode.go
- `init()` --calls--> `SetMode()`  [INFERRED]
  routergroup_test.go → mode.go
- `init()` --calls--> `SetMode()`  [INFERRED]
  utils_test.go → mode.go
- `Trusted Proxies Security Default` --semantically_similar_to--> `Trivy Security Scan Workflow`  [INFERRED] [semantically similar]
  docs/doc.md → .github/workflows/trivy-scan.yml
- `Contributor Covenant Code of Conduct` --semantically_similar_to--> `golangci-lint Config`  [INFERRED] [semantically similar]
  CODE_OF_CONDUCT.md → .golangci.yml

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **CI, Lint & Security Pipeline** — _github_workflows_gin_workflow, _github_workflows_codeql_workflow, _github_workflows_trivy_scan_workflow, _github_dependabot_config, _golangci_config [INFERRED 0.85]
- **Issue Reporting Workflow** — _github_issue_template_bug_report_template, _github_issue_template_feature_request_template, _github_issue_template_config_config, contributing_guide [INFERRED 0.85]
- **Release Pipeline** — _github_workflows_goreleaser_workflow, _goreleaser_config, changelog_log, concept_gin_v1_12_0 [INFERRED 0.75]

## Communities (102 total, 31 thin omitted)

### Community 0 - "Context Abort/Status Tests"
Cohesion: 0.03
Nodes (176): TestContextAbortWithError(), TestContextAbortWithStatus(), TestContextAbortWithStatusJSON(), TestContextAbortWithStatusPureJSON(), TestContextAddParam(), TestContextAutoBindJSON(), TestContextAutoShouldBindJSON(), TestContextBadAutoBind() (+168 more)

### Community 1 - "Plain Text Binding"
Cohesion: 0.05
Nodes (37): decodePlain(), plainBinding, net/http.ResponseWriter, BytesToString(), StringToBytes(), BenchmarkBytesConvBytesToStr(), BenchmarkBytesConvBytesToStrRaw(), BenchmarkBytesConvStrToBytes() (+29 more)

### Community 2 - "Filesystem + Handler Chain"
Cohesion: 0.05
Nodes (45): FileSystem, HandlersChain, IRouter, Any(), DELETE(), GET(), Group(), Handle() (+37 more)

### Community 3 - "Router Method Tree"
Cohesion: 0.07
Nodes (49): methodTree, methodTrees, node, nodeType, nodeValue, Param, Params, skippedNode (+41 more)

### Community 4 - "Context Get/Set + ResponseWriter"
Cohesion: 0.05
Nodes (9): getTyped(), Context, responseWriter, mime/multipart.Form, net/http.Cookie, net/http.SameSite, net/url.Values, sync.RWMutex (+1 more)

### Community 5 - "Form Mapping (reflection binding)"
Cohesion: 0.08
Nodes (43): BindUnmarshaler, head(), mapFormByTag(), MapFormWithTag(), mapping(), mapURI(), setArray(), setBoolField() (+35 more)

### Community 6 - "Engine Handler Dispatch"
Cohesion: 0.10
Nodes (49): header, New(), TestEngineHandleContext(), TestEngineHandleContextManyReEntries(), TestEngineHandleContextNoRouteWithEngineMiddleware(), TestEngineHandleContextNoRouteWithGroupMiddleware(), TestEngineHandleContextPreventsMiddlewareReEntry(), TestEngineHandleContextUseEscapedPathOverride() (+41 more)

### Community 7 - "Binding Content-Type Selection Tests"
Cohesion: 0.05
Nodes (49): appkey, TestBindingDefault(), TestBindingForm(), TestBindingForm2(), TestBindingFormDefaultValue(), TestBindingFormDefaultValue2(), TestBindingFormEmbeddedStruct(), TestBindingFormEmbeddedStruct2() (+41 more)

### Community 8 - "Form Mapping Tests"
Cohesion: 0.08
Nodes (46): bindTestData, mappingByPtr(), TestMappingArray(), TestMappingCollectionFormat(), TestMappingCollectionFormatInvalid(), TestMappingCustomPointerStructTypeUnmarshalTextForm(), TestMappingCustomPointerStructTypeUnmarshalTextUri(), TestMappingCustomPointerStructTypeWithFormTag() (+38 more)

### Community 9 - "Render (JSON/XML/YAML/ASCII)"
Cohesion: 0.07
Nodes (42): fail, TestRenderAsciiJSON(), TestRenderAsciiJSONFail(), TestRenderBSON(), TestRenderBSONError(), TestRenderBSONWriteError(), TestRenderData(), TestRenderDataContentLength() (+34 more)

### Community 10 - "Route Info + Param Binding"
Cohesion: 0.07
Nodes (41): Birthday, RouteInfo, assertRoutePresent(), compareFunc(), Context, handlerTest1(), handlerTest2(), parseCIDR() (+33 more)

### Community 11 - "Logger Middleware"
Cohesion: 0.09
Nodes (35): consoleColorModeValue, HandlerFunc, LogFormatter, LoggerConfig, Skipper, net/http.Handler, net/http.HandlerFunc, DisableConsoleColor() (+27 more)

### Community 12 - "Protobuf Reflection Types"
Cohesion: 0.08
Nodes (13): google.golang.org/protobuf/reflect/protoreflect.EnumDescriptor, google.golang.org/protobuf/reflect/protoreflect.EnumNumber, google.golang.org/protobuf/reflect/protoreflect.EnumType, google.golang.org/protobuf/reflect/protoreflect.Message, google.golang.org/protobuf/runtime/protoimpl.MessageState, google.golang.org/protobuf/runtime/protoimpl.SizeCache, google.golang.org/protobuf/runtime/protoimpl.UnknownFields, FOO (+5 more)

### Community 13 - "Context.Next + H Map"
Cohesion: 0.08
Nodes (26): bindTestStruct, H, testStruct, encoding/xml.Encoder, encoding/xml.StartElement, xmlmap, Bind(), chooseData() (+18 more)

### Community 14 - "JSON Binding Custom Codec"
Cohesion: 0.11
Nodes (15): customReq, TestCustomJsonCodec(), TestJSONBindingBindBody(), TestJSONBindingBindBodyMap(), timeCodec, TimeEx, timePointerCodec, TimePointerEx (+7 more)

### Community 16 - "Community 16"
Cohesion: 0.14
Nodes (24): RecoveryFunc, CustomRecovery(), CustomRecoveryWithWriter(), defaultHandleRecovery(), function(), Context, readNthLine(), RecoveryWithWriter() (+16 more)

### Community 17 - "Community 17"
Cohesion: 0.12
Nodes (23): isWindows(), TestBadFileDescriptor(), TestBadListener(), TestBadTrustedCIDRs(), TestBadUnixSocket(), TestConcurrentHandleContext(), TestEscapedColon(), TestFileDescriptor() (+15 more)

### Community 18 - "Community 18"
Cohesion: 0.11
Nodes (20): createDefaultFormPostRequest(), createFormFilesMultipartRequest(), createFormFilesMultipartRequestFail(), createFormMultipartRequest(), createFormMultipartRequestForMap(), createFormMultipartRequestForMapFail(), createFormPostRequest(), createFormPostRequestForMap() (+12 more)

### Community 19 - "Community 19"
Cohesion: 0.18
Nodes (21): debugPrintRoute(), captureOutput(), TestDebugPrint(), TestDebugPrintError(), TestDebugPrintFunc(), TestDebugPrintLoadTemplate(), TestDebugPrintRouteFunc(), TestDebugPrintRoutes() (+13 more)

### Community 21 - "Community 21"
Cohesion: 0.13
Nodes (15): Dir(), mockFileSystem, Test_neuteredReaddirFile_Readdir(), TestDir(), TestDir_listDirectory(), TestOnlyFilesFS_Open(), TestOnlyFilesFS_Open_err(), mockFileSystem (+7 more)

### Community 23 - "Community 23"
Cohesion: 0.24
Nodes (19): Benchmark404(), Benchmark404Many(), Benchmark5Params(), BenchmarkLoggerMiddleware(), BenchmarkManyHandlers(), BenchmarkManyRoutesFirst(), BenchmarkManyRoutesLast(), BenchmarkOneRoute() (+11 more)

### Community 24 - "Community 24"
Cohesion: 0.22
Nodes (17): authorizationHeader(), BasicAuth(), BasicAuthForProxy(), BasicAuthForRealm(), processAccounts(), TestBasicAuth(), TestBasicAuth401(), TestBasicAuth401WithCustomRealm() (+9 more)

### Community 25 - "Community 25"
Cohesion: 0.14
Nodes (20): requestWithBody(), TestBindingFormForTime(), TestBindingFormForTime2(), TestBindingFormInvalidName(), TestBindingFormInvalidName2(), TestBindingFormStringSliceMap(), TestBindingQueryStringMap(), testFormBindingForTime() (+12 more)

### Community 26 - "Community 26"
Cohesion: 0.15
Nodes (18): mapNoValidationSub, Object, structCustomValidation, structModifyValidation, structNoValidationPointer, structNoValidationValues, substructNoValidation, testInterface (+10 more)

### Community 27 - "Community 27"
Cohesion: 0.16
Nodes (3): Error, errorMsgs, ErrorType

### Community 28 - "Community 28"
Cohesion: 0.20
Nodes (10): Context, RoutesInfo, iterate(), OptionFunc, redirectFixedPath(), redirectRequest(), redirectTrailingSlash(), sanitizePathChars() (+2 more)

### Community 29 - "Community 29"
Cohesion: 0.16
Nodes (16): Default(), route, TestCreateDefaultRouter(), TestCustomUnmarshalStruct(), TestH2c(), BenchmarkParallelGithub(), BenchmarkParallelGithubDefault(), exampleFromPath() (+8 more)

### Community 30 - "Community 30"
Cohesion: 0.15
Nodes (5): ResponseWriter, net/http.CloseNotifier, net/http.Flusher, net/http.Hijacker, net/http.Pusher

### Community 31 - "Community 31"
Cohesion: 0.12
Nodes (17): Binding, TestBindingJSONDisallowUnknownFields(), TestBindingJSONSlice(), TestBindingJSONUseNumber(), TestBindingJSONUseNumber2(), TestBindingProtoBuf(), TestBindingProtoBufFail(), TestBindingTOMLFail() (+9 more)

### Community 32 - "Community 32"
Cohesion: 0.12
Nodes (6): bodyAllowedForStatus(), escapeQuotes(), getMapFromFormData(), BenchmarkGetMapFromFormData(), ContextKeyType, Negotiate

### Community 33 - "Community 33"
Cohesion: 0.18
Nodes (5): Engine, parseIP(), html/template.FuncMap, net.IP, sync.Pool

### Community 34 - "Community 34"
Cohesion: 0.13
Nodes (12): BenchmarkMapFormFull(), BenchmarkMapFormName(), mapForm(), TestMappingForm(), TestMappingFormFieldNotSent(), TestMappingFormWithEmptyToDefault(), TestMappingTime(), TestMappingTimeDuration() (+4 more)

### Community 35 - "Community 35"
Cohesion: 0.14
Nodes (9): FooBarStructForTimeType, FooStructForTimeTypeFailFormat, FooStructForTimeTypeFailLocation, FooStructForTimeTypeNotFormat, FooStructForTimeTypeNotUnixFormat, LogFormatterParams, formatAsDate(), time.Duration (+1 more)

### Community 36 - "Community 36"
Cohesion: 0.18
Nodes (12): nonPusherResponseWriter, init(), TestPusherWithoutPusher(), TestPusherWithPusher(), TestResponseWriterFlush(), TestResponseWriterFlushWithFlusher(), TestResponseWriterFlushWithNonFlusher(), TestResponseWriterReset() (+4 more)

### Community 37 - "Community 37"
Cohesion: 0.18
Nodes (13): Gin Benchmark Report, dkron, Fiber Benchmark Comparability Caveat, fnproject / fn, gin-contrib Middleware Collection, gin-gonic/contrib, gorush, HttpRouter (+5 more)

### Community 38 - "Community 38"
Cohesion: 0.19
Nodes (4): customJsonApi, Encoder, io.Writer, Core

### Community 39 - "Community 39"
Cohesion: 0.26
Nodes (7): debugPrintLoadTemplate(), debugPrintWARNINGDefault(), debugPrintWARNINGNew(), debugPrintWARNINGSetHTMLTemplate(), getMinVer(), IsDebugging(), TestGetMinVer()

### Community 40 - "Community 40"
Cohesion: 0.28
Nodes (11): cleanPathTest, bufApp(), cleanPath(), removeRepeatedChar(), BenchmarkPathClean(), BenchmarkPathCleanLong(), genLongPaths(), TestPathClean() (+3 more)

### Community 41 - "Community 41"
Cohesion: 0.15
Nodes (8): mockHijacker, net/http/httptest.ResponseRecorder, errorWriter, failWriter, TestRenderMsgPack(), TestRenderMsgPackError(), TestWriteMsgPack(), TestRenderJsonpJSONError()

### Community 42 - "Community 42"
Cohesion: 0.18
Nodes (12): init(), performRequestInGroup(), TestRouterGroupBadMethod(), TestRouterGroupBasic(), TestRouterGroupBasicHandle(), TestRouterGroupCombineHandlersEmptySliceNotNil(), TestRouterGroupCombineHandlersTooManyHandlers(), TestRouterGroupInvalidStatic() (+4 more)

### Community 43 - "Community 43"
Cohesion: 0.17
Nodes (12): gin-gonic/examples Repository, go-playground/validator, Request Binding & Validation, Build Tags, Gin Quick Start Guide, Logging, Middleware, Response Rendering (+4 more)

### Community 44 - "Community 44"
Cohesion: 0.21
Nodes (9): DisableBindValidation(), EnableJsonDecoderDisallowUnknownFields(), EnableJsonDecoderUseNumber(), init(), Mode(), TestDisableBindValidation(), TestEnableJsonDecoderDisallowUnknownFields(), TestEnableJsonDecoderUseNumber() (+1 more)

### Community 45 - "Community 45"
Cohesion: 0.45
Nodes (3): debugPrint(), debugPrintError(), net.Listener

### Community 46 - "Community 46"
Cohesion: 0.27
Nodes (4): defaultValidator, SliceValidationError, sync.Once, validator.Validate

### Community 47 - "Community 47"
Cohesion: 0.20
Nodes (3): formBinding, formMultipartBinding, formPostBinding

### Community 48 - "Community 48"
Cohesion: 0.40
Nodes (7): html/template.Template, HTML, Delims, HTMLRender, HTMLDebug, HTMLProduction, Render

### Community 49 - "Community 49"
Cohesion: 0.14
Nodes (5): TestDefaultValidator(), TestSliceValidationError(), TestTOMLBindingBindBody(), TestXMLBindingBindBody(), TestYAMLBindingBindBody()

### Community 51 - "Community 51"
Cohesion: 0.28
Nodes (6): bufio.ReadWriter, net.Conn, TestResponseWriterHijack(), TestResponseWriterHijackAfterWrite(), TestResponseWriterHijackAfterWriteHeaderNow(), TestResponseWriterWrite()

### Community 52 - "Community 52"
Cohesion: 0.29
Nodes (8): Goreleaser Release Workflow, GoReleaser Config, Gin ChangeLog, Gin v1.11.0 Release, Gin v1.12.0 Release, Gin Web Framework, GoReleaser, ginS Default Server Example

### Community 54 - "Community 54"
Cohesion: 0.29
Nodes (7): convertToOidUnmarshalText(), TestMappingCustomArrayOfArrayUnmarshalTextDefault(), TestMappingCustomArrayOfArrayUnmarshalTextForm(), TestMappingCustomArrayOfArrayUnmarshalTextUri(), TestMappingCustomArrayUnmarshalTextForm(), TestMappingCustomArrayUnmarshalTextUri(), objectIDUnmarshalText

### Community 55 - "Community 55"
Cohesion: 0.32
Nodes (3): mockWriter, nonFlusherWriter, net/http.Header

### Community 56 - "Community 56"
Cohesion: 0.29
Nodes (7): Dependabot Config, Gin CI Test Workflow, golangci-lint Config, Contributor Covenant Code of Conduct, Codecov Config, Codecov Coverage Reporting, golangci-lint

### Community 57 - "Community 57"
Cohesion: 0.38
Nodes (5): Default(), Binding, BindingBody, BindingUri, StructValidator

### Community 58 - "Community 58"
Cohesion: 0.33
Nodes (6): convertTo(), TestMappingCustomArrayForm(), TestMappingCustomArrayOfArrayForm(), TestMappingCustomArrayOfArrayUri(), TestMappingCustomArrayUri(), objectID

### Community 60 - "Community 60"
Cohesion: 0.33
Nodes (5): CreateTestResponseRecorder(), TestContextResetInHandler(), TestContextStream(), TestContextStreamWithClientGone(), TestResponseRecorder

### Community 61 - "Community 61"
Cohesion: 0.40
Nodes (4): Binding, BindingBody, BindingUri, StructValidator

### Community 62 - "Community 62"
Cohesion: 0.33
Nodes (6): TestBindingBSON(), TestBindingJSON(), TestBindingTOML(), TestBindingXML(), TestBindingYAML(), testBodyBinding()

### Community 71 - "Community 71"
Cohesion: 0.40
Nodes (4): TestError(), TestErrorSlice(), TestErrorUnwrap(), TestErr

### Community 72 - "Community 72"
Cohesion: 0.50
Nodes (5): Bug Report Issue Template, Issue Template Chooser Config, Feature Request Issue Template, Pull Request Checklist Template, Contributing Guide

### Community 73 - "Community 73"
Cohesion: 0.40
Nodes (5): Trivy Security Scan Workflow, Trivy Security Scan, Graceful Shutdown, Server Configuration, Trusted Proxies Security Default

### Community 74 - "Community 74"
Cohesion: 0.50
Nodes (4): Binding, TestBindingDefaultMsgPack(), TestBindingMsgPack(), testMsgPackBodyBinding()

### Community 77 - "Community 77"
Cohesion: 0.50
Nodes (5): Context, handlerNameTest(), handlerNameTest2(), resetContextForClientIPTests(), TestContextClientIP()

### Community 78 - "Community 78"
Cohesion: 0.50
Nodes (4): TestBindingFormStringMap(), TestBindingJSONStringMap(), TestBindingYAMLStringMap(), testBodyBindingStringMap()

### Community 79 - "Community 79"
Cohesion: 0.50
Nodes (4): createMultipartRequest(), must(), TestContextCopyShouldNotCancel(), TestContextPostFormMultipart()

### Community 80 - "Community 80"
Cohesion: 0.50
Nodes (3): TestContextRenderIfErr(), TestContextRenderSSE(), TestRender

## Knowledge Gaps
- **61 isolated node(s):** `authPair`, `BindingBody`, `BindingUri`, `StructValidator`, `BindingUri` (+56 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 231 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **31 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Context` connect `Context Get/Set + ResponseWriter` to `Community 32`, `Community 33`, `Filesystem + Handler Chain`, `Router Method Tree`, `Form Mapping (reflection binding)`, `Community 38`, `Logger Middleware`, `Context.Next + H Map`, `Community 15`, `Community 81`, `Community 50`, `Community 18`, `Community 20`, `Community 53`, `Community 22`, `Community 27`?**
  _High betweenness centrality (0.165) - this node is a cross-community bridge._
- **Why does `Engine` connect `Community 33` to `Context Abort/Status Tests`, `Filesystem + Handler Chain`, `Router Method Tree`, `Context Get/Set + ResponseWriter`, `Engine Handler Dispatch`, `Community 39`, `Route Info + Param Binding`, `Community 45`, `Community 46`, `Community 48`, `Community 17`, `Community 23`, `Community 28`, `Community 29`?**
  _High betweenness centrality (0.132) - this node is a cross-community bridge._
- **Why does `CreateTestContext()` connect `Context Abort/Status Tests` to `Community 96`, `Community 33`, `Plain Text Binding`, `Engine Handler Dispatch`, `Community 77`, `Community 79`, `Community 80`, `Community 17`, `Community 84`, `Community 60`?**
  _High betweenness centrality (0.074) - this node is a cross-community bridge._
- **Are the 176 inferred relationships involving `CreateTestContext()` (e.g. with `TestContextFileNotFound()` and `TestContextFileSimple()`) actually correct?**
  _`CreateTestContext()` has 176 INFERRED edges - model-reasoned connections that need verification._
- **Are the 141 inferred relationships involving `New()` (e.g. with `TestBasicAuth401()` and `TestBasicAuth401WithCustomRealm()`) actually correct?**
  _`New()` has 141 INFERRED edges - model-reasoned connections that need verification._
- **Are the 41 inferred relationships involving `PerformRequest()` (e.g. with `TestRaceParamsContextCopy()` and `TestEngineHandleContext()`) actually correct?**
  _`PerformRequest()` has 41 INFERRED edges - model-reasoned connections that need verification._
- **What connects `authPair`, `BindingBody`, `BindingUri` to the rest of the system?**
  _61 weakly-connected nodes found - possible documentation gaps or missing edges._