# Graph Report - ktor-http  (2026-09-09)

## Corpus Check
- 139 files · ~56,695 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 1531 nodes · 2844 edges · 88 communities (42 shown, 31 thin omitted)
- Extraction: 77% EXTRACTED · 23% INFERRED · 0% AMBIGUOUS · INFERRED: 651 edges (avg confidence: 0.85)
- Token cost: 73,767 input · 0 output

## Community Hubs (Navigation)
- Community 0
- Community 1
- Community 2
- Community 3
- Community 4
- Community 5
- Community 6
- Community 7
- Community 8
- Community 9
- Community 10
- Community 11
- Community 12
- Community 13
- Community 14
- Community 15
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
- Community 50
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
- Community 72
- Community 73

## God Nodes (most connected - your core abstractions)
1. `HttpHeaders` - 103 edges
2. `URLBuilderTest` - 48 edges
3. `ContentType` - 44 edges
4. `parseHeaders()` - 41 edges
5. `UrlTest` - 37 edges
6. `CharArrayBuilder` - 37 edges
7. `RangesTest` - 35 edges
8. `HeaderValueParam` - 30 edges
9. `parseRequest()` - 30 edges
10. `HttpHeadersMap` - 28 edges

## Surprising Connections (you probably didn't know these)
- `takeFrom()` --calls--> `ParametersBuilder`  [INFERRED]
  jvm/src/io/ktor/http/URLUtilsJvm.kt → common/src/io/ktor/http/Parameters.kt
- `takeFrom()` --calls--> `parseQueryString()`  [INFERRED]
  jvm/src/io/ktor/http/URLUtilsJvm.kt → common/src/io/ktor/http/Query.kt
- `defaultForFile()` --references--> `ContentType`  [EXTRACTED]
  jvm/src/io/ktor/http/FileContentTypeJvm.kt → common/src/io/ktor/http/ContentTypes.kt
- `defaultForPath()` --references--> `ContentType`  [EXTRACTED]
  jvm/src/io/ktor/http/FileContentTypeJvm.kt → common/src/io/ktor/http/ContentTypes.kt
- `CIOHeaders` --implements--> `Headers`  [EXTRACTED]
  ktor-http-cio/common/src/io/ktor/http/cio/CIOHeaders.kt → common/src/io/ktor/http/Headers.kt

## Import Cycles
- None detected.

## Communities (88 total, 31 thin omitted)

### Community 1 - "Community 1"
Cohesion: 0.06
Nodes (47): ContentDisposition, encodeContentDispositionAttribute(), Parameters, AcceptEncoding, HeaderValue, HeaderValueParam, T, nextIsDelimiterOrEnd() (+39 more)

### Community 2 - "Community 2"
Cohesion: 0.06
Nodes (28): EmptyParameters, StringValues, StringValuesBuilder, StringValuesBuilderImpl, StringValuesImpl, StringValuesSingleImpl, Parameters, ParametersBuilder (+20 more)

### Community 3 - "Community 3"
Cohesion: 0.05
Nodes (18): contentRangeHeaderValue(), LongRange, Bounded, ContentRange, LongRange, mergeRangesKeepOrder(), parseRangesSpecifier(), RangeUnits (+10 more)

### Community 4 - "Community 4"
Cohesion: 0.07
Nodes (11): Appendable, CharSequence, dumpTo(), HeadersData, HttpHeadersMap, parseHeaderValue(), CharArrayBuilder, CharArray (+3 more)

### Community 5 - "Community 5"
Cohesion: 0.06
Nodes (46): A, AsciiBitSet, appendPercentEncoded(), charToHexDigit(), decodeImpl(), decodeScan(), decodeURLPart(), decodeURLQueryComponent() (+38 more)

### Community 6 - "Community 6"
Cohesion: 0.07
Nodes (33): assertCookieName(), clientCookies(), Cookie, CookieEncoding, BASE64_ENCODING, DQUOTES, RAW, URI_ENCODING (+25 more)

### Community 7 - "Community 7"
Cohesion: 0.06
Nodes (28): Attributes, compressed(), CompressedReadChannelResponse, CompressedWriteChannelResponse, AttributeKey, CoroutineContext, T, ByteArrayContent (+20 more)

### Community 8 - "Community 8"
Cohesion: 0.07
Nodes (26): ContentTypeMatcher, Application, Audio, BadContentTypeFormatException, charset(), ContentType, Font, Image (+18 more)

### Community 9 - "Community 9"
Cohesion: 0.07
Nodes (23): EntityTagVersion(), GMTDate, LastModifiedVersion, Version, VersionCheckResult, NOT_MODIFIED, OK, PRECONDITION_FAILED (+15 more)

### Community 11 - "Community 11"
Cohesion: 0.06
Nodes (20): ByteArray, JvmSerializable, JvmSerializer, Url, UrlJvmSerializer, UrlSerializer, JvmSerializable, URLProtocol (+12 more)

### Community 12 - "Community 12"
Cohesion: 0.12
Nodes (24): CookieDateBuilder, CookieDateParser, handleToken(), InvalidCookieDateException, isDelimiter(), isDigit(), isNonDelimiter(), isNonDigit() (+16 more)

### Community 14 - "Community 14"
Cohesion: 0.19
Nodes (23): grammar(), GrammarBuilder, anyOf(), AnyOfGrammar, AtLeastOne, ComplexGrammar, flatten(), Grammar (+15 more)

### Community 15 - "Community 15"
Cohesion: 0.13
Nodes (9): appendParam(), Parameters, parse(), parseQueryString(), trimEnd(), trimStart(), withEmptyStringForValuelessKeys(), Parameters (+1 more)

### Community 16 - "Community 16"
Cohesion: 0.11
Nodes (9): Parser, ParseResult, RegexParser, add(), buildRegexParser(), GrammarRegex, toRegex(), CIOHeaders (+1 more)

### Community 17 - "Community 17"
Cohesion: 0.15
Nodes (14): asFlow(), BinaryChannelItem, BinaryItem, Empty, FileItem, forEachPart(), FormItem, MultiPartData (+6 more)

### Community 18 - "Community 18"
Cohesion: 0.21
Nodes (19): characterIsNotAllowed(), isDelimiter(), IllegalStateException, noColonFound(), parseHeaderName(), parseHeaderNameFailed(), parseHttpMethod(), parseHttpMethodFull() (+11 more)

### Community 19 - "Community 19"
Cohesion: 0.15
Nodes (3): HeaderParserTest, test(), RequestParserTest

### Community 20 - "Community 20"
Cohesion: 0.12
Nodes (9): ChannelWriterContent, WriteChannelContent, IOException, WriterContent, skipCrLf(), UnsupportedMediaTypeExceptionCIO, ByteWriteChannel, discardBlocking() (+1 more)

### Community 22 - "Community 22"
Cohesion: 0.14
Nodes (9): Closeable, ConnectionOptions, expectHttpUpgrade(), isTransferEncodingChunked(), ByteReadChannel, parseHttpBody(), HttpMessage, Request (+1 more)

### Community 25 - "Community 25"
Cohesion: 0.13
Nodes (10): CoroutineDispatcher, ByteArray, Charset, nonClosing(), NonClosingOutputStream, withBlockingOutputStream(), withBlockingWriter(), OutputStreamContent (+2 more)

### Community 26 - "Community 26"
Cohesion: 0.17
Nodes (3): expectHttpBody(), parseRequest(), MultipartTest

### Community 27 - "Community 27"
Cohesion: 0.17
Nodes (5): ByteBuffer, ByteArray, Source, RequestResponseBuilder, RequestResponseBuilderTest

### Community 28 - "Community 28"
Cohesion: 0.25
Nodes (12): ByteString, discardBlocking(), Epilogue, ByteReadChannel, ReceiveChannel, MultipartPart, parseMultipart(), parsePartBodyImpl() (+4 more)

### Community 29 - "Community 29"
Cohesion: 0.13
Nodes (7): CacheControl, MaxAge, NoCache, NoStore, Visibility, Private, Public

### Community 33 - "Community 33"
Cohesion: 0.24
Nodes (3): DecoderJob, decodeChunked(), ChunkedTest

### Community 34 - "Community 34"
Cohesion: 0.21
Nodes (6): HttpAuthHeader, Charset, nextChallengeIndex(), Parameterized, Parameters, parseAuthorizationHeaders()

### Community 35 - "Community 35"
Cohesion: 0.19
Nodes (10): CoroutineScope, EncoderJob, encodeChunked(), ByteArray, ByteReadChannel, CoroutineContext, parseChunkSize(), rethrowCloseCause() (+2 more)

### Community 36 - "Community 36"
Cohesion: 0.30
Nodes (10): isToken(), isToken68(), matchParameter(), matchParameters(), matchToken68(), skipDelimiter(), skipSpaces(), unescaped() (+2 more)

### Community 37 - "Community 37"
Cohesion: 0.33
Nodes (9): append(), escapeIfNeeded(), escapeIfNeededTo(), HeaderValueWithParameters, isQuoted(), needQuotes(), quote(), quoteTo() (+1 more)

### Community 38 - "Community 38"
Cohesion: 0.17
Nodes (3): ByteArray, Source, RequestResponseBuilder

### Community 39 - "Community 39"
Cohesion: 0.17
Nodes (3): ByteArray, Source, RequestResponseBuilder

### Community 42 - "Community 42"
Cohesion: 0.31
Nodes (4): HeaderValueEncoding, QUOTED_ALWAYS, QUOTED_WHEN_REQUIRED, URI_ENCODE

### Community 46 - "Community 46"
Cohesion: 0.39
Nodes (9): Acceptor Job, HTTP Pipeline Failure Isolation Policy, HTTP Pipeline Job, HTTP Pipeline Writer Job, Parent Job Attachment and Cancellation Propagation, Pipeline Job Launching Writer and Request Handler Jobs, Pipeline Jobs Parented to Root Job Instead of Acceptor Job, Server Root Job (+1 more)

### Community 48 - "Community 48"
Cohesion: 0.36
Nodes (3): ByteReadChannel, parseResponse(), ResponseParserTest

### Community 49 - "Community 49"
Cohesion: 0.43
Nodes (6): equalsLowerCase(), hashCodeLowerCase(), numberFormatException(), parseDecLong(), parseDecLongWithCheck(), toLowerCase()

### Community 52 - "Community 52"
Cohesion: 0.38
Nodes (4): IllegalHeaderNameException, IllegalHeaderValueException, IllegalArgumentException, UnsafeHeaderException

### Community 54 - "Community 54"
Cohesion: 0.48
Nodes (6): date(), expires(), formatHttpDate(), ifModifiedSince(), lastModified(), parseHttpDate()

### Community 55 - "Community 55"
Cohesion: 0.33
Nodes (3): ByteArrayContent, ByteArray, TextContent

### Community 56 - "Community 56"
Cohesion: 0.47
Nodes (3): AsciiCharTree, T, Node

### Community 57 - "Community 57"
Cohesion: 0.47
Nodes (3): CharArray, Pool, NoPoolImpl

### Community 61 - "Community 61"
Cohesion: 0.50
Nodes (3): findBoundary(), ByteArray, parseBoundaryInternal()

### Community 64 - "Community 64"
Cohesion: 0.50
Nodes (3): LinkHeader, Parameters, Rel

## Knowledge Gaps
- **27 isolated node(s):** `Public`, `Private`, `Parameters`, `RAW`, `DQUOTES` (+22 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 427 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **31 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `ContentType` connect `Community 8` to `Community 17`, `Community 37`, `Community 7`?**
  _High betweenness centrality (0.112) - this node is a cross-community bridge._
- **Why does `Headers` connect `Community 9` to `Community 16`, `Community 4`, `Community 7`?**
  _High betweenness centrality (0.088) - this node is a cross-community bridge._
- **Why does `HttpMethod` connect `Community 31` to `Community 38`, `Community 39`, `Community 18`, `Community 22`, `Community 26`, `Community 27`?**
  _High betweenness centrality (0.082) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `ContentType` (e.g. with `.testCharsetForText()` and `.testNoCharsetForNonText()`) actually correct?**
  _`ContentType` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Are the 31 inferred relationships involving `parseHeaders()` (e.g. with `parsePartHeadersImpl()` and `.parseHeadersDelimitersInHeaderNameShouldBeProhibited()`) actually correct?**
  _`parseHeaders()` has 31 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Public`, `Private`, `Parameters` to the rest of the system?**
  _27 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Community 0` be split into smaller, more focused modules?**
  _Cohesion score 0.019801980198019802 - nodes in this community are weakly interconnected._