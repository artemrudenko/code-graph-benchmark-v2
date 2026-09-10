# Graph Report - bbolt  (2026-09-09)

## Corpus Check
- 150 files · ~100,495 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 1268 nodes · 3351 edges · 77 communities (47 shown, 12 thin omitted)
- Extraction: 94% EXTRACTED · 6% INFERRED · 0% AMBIGUOUS · INFERRED: 200 edges (avg confidence: 0.85)
- Token cost: 0 input · 0 output

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
- Community 75

## God Nodes (most connected - your core abstractions)
1. `MustCreateDB()` - 138 edges
2. `DB` - 80 edges
3. `Pgid` - 72 edges
4. `Open()` - 65 edges
5. `Bucket` - 64 edges
6. `Page` - 62 edges
7. `NewRootCommand()` - 53 edges
8. `Tx` - 48 edges
9. `MustCreateDBWithOption()` - 41 edges
10. `Meta` - 41 edges

## Surprising Connections (you probably didn't know these)
- `TestBucket_Put_Single()` --calls--> `qconfig()`  [INFERRED]
  bucket_test.go → quick_test.go
- `TestBucket_Put_Multiple()` --calls--> `qconfig()`  [INFERRED]
  bucket_test.go → quick_test.go
- `TestCursor_QuickCheck_Reverse()` --calls--> `revtestdata`  [INFERRED]
  cursor_test.go → quick_test.go
- `Open()` --calls--> `getDiscardLogger()`  [INFERRED]
  db.go → logger.go
- `prepareData()` --calls--> `Open()`  [INFERRED]
  db_whitebox_test.go → db.go

## Import Cycles
- None detected.

## Communities (77 total, 12 thin omitted)

### Community 0 - "Community 0"
Cohesion: 0.06
Nodes (46): batch, call, FreelistType, Info, panicked, Stats, benchFunc(), checkProgress() (+38 more)

### Community 1 - "Community 1"
Cohesion: 0.06
Nodes (58): TestBucketsCommand_Run(), TestCheckCommand_Run(), TestCompactCommand_NoArgs(), TestCompactCommand_Run(), TestDumpCommand_NoArgs(), TestDumpCommand_Run(), TestGetCommand_NoArgs(), TestGetCommand_Run() (+50 more)

### Community 2 - "Community 2"
Cohesion: 0.07
Nodes (40): bytesRange, concurrentConfig, DefaultLogger, duration, historyRecord, historyRecords, Logger, operationChance (+32 more)

### Community 3 - "Community 3"
Cohesion: 0.07
Nodes (41): checkFunc(), newCheckCommand(), newCompactCommand(), inspectFunc(), newInspectCommand(), newSurgeryFreelistAbandonCommand(), newSurgeryFreelistCommand(), newSurgeryFreelistRebuildCommand() (+33 more)

### Community 4 - "Community 4"
Cohesion: 0.06
Nodes (55): meta, ExampleBucket_Delete(), ExampleBucket_ForEach(), ExampleBucket_Put(), ExampleCursor(), ExampleCursor_reverse(), Open(), BenchmarkDBBatchAutomatic() (+47 more)

### Community 5 - "Community 5"
Cohesion: 0.08
Nodes (49): BenchmarkBucket_CreateBucketIfNotExists(), TestBucket_Bucket_IncompatibleValue(), TestBucket_CreateBucket_IncompatibleValue(), TestBucket_Delete(), TestBucket_Delete_Bucket(), TestBucket_Delete_Closed(), TestBucket_Delete_FreelistOverflow(), TestBucket_Delete_Large() (+41 more)

### Community 6 - "Community 6"
Cohesion: 0.08
Nodes (36): dumpFunc(), dumpPage(), newDumpCommand(), getFunc(), newGetCommand(), keysFunc(), newKeysCommand(), newPageItemCommand() (+28 more)

### Community 7 - "Community 7"
Cohesion: 0.09
Nodes (34): featCfg, FeatOpt, FlakeyDevice, flakeyT, createEmptyFSImage(), Flakey, FSType, InitFlakey() (+26 more)

### Community 8 - "Community 8"
Cohesion: 0.08
Nodes (40): failWriter, failWriterError, testing.T, TestPage_dump(), TestPage_typ(), TestPgids_merge(), TestPgids_merge_quick(), TestNode_put() (+32 more)

### Community 9 - "Community 9"
Cohesion: 0.09
Nodes (36): QuickDB, simulateHandler, sync.RWMutex, TestSimulateNoFreeListSync_10000op_1000p(), TestSimulateNoFreeListSync_10000op_100p(), TestSimulateNoFreeListSync_10000op_10p(), TestSimulateNoFreeListSync_10000op_1p(), TestSimulateNoFreeListSync_1000op_100p() (+28 more)

### Community 10 - "Community 10"
Cohesion: 0.11
Nodes (6): BucketStats, BucketStructure, cloneBytes(), Bucket, Tx, newBucket()

### Community 11 - "Community 11"
Cohesion: 0.11
Nodes (4): os.FileMode, PageInfo, Tx, DB

### Community 12 - "Community 12"
Cohesion: 0.08
Nodes (27): TestBucket_Delete_Quick(), TestCursor_Bucket(), TestCursor_Delete(), TestCursor_EmptyBucket(), TestCursor_EmptyBucketReverse(), TestCursor_First_EmptyPages(), TestCursor_Iterate_Leaf(), TestCursor_Last_EmptyPages() (+19 more)

### Community 13 - "Community 13"
Cohesion: 0.13
Nodes (4): unsafe.Pointer, Page, UnsafeAdd(), UnsafeIndex()

### Community 14 - "Community 14"
Cohesion: 0.17
Nodes (3): node, Assert(), TestTx_releaseRange()

### Community 16 - "Community 16"
Cohesion: 0.22
Nodes (25): NewPage(), LoadPage(), newTestFreelist(), requirePages(), Test_freelist_ReadIDs_and_getFreePageIDs(), TestFreelist_E2E_HappyPath(), TestFreelist_E2E_MultiSpanOverflows(), TestFreelist_E2E_Reload() (+17 more)

### Community 17 - "Community 17"
Cohesion: 0.16
Nodes (5): shared, txPending, Txid, allPendingPages(), newShared()

### Community 18 - "Community 18"
Cohesion: 0.14
Nodes (10): testing.TB, DB, truncDuration(), createBucketAndPopulateData(), openBucket(), populateSampleDataInBucket(), prepareBuckets(), TestBucket_MoveBucket_DiffDB() (+2 more)

### Community 20 - "Community 20"
Cohesion: 0.13
Nodes (3): branchPageElement, Pgid, XRay

### Community 21 - "Community 21"
Cohesion: 0.20
Nodes (10): checkConfig, CheckOption, hexKvStringer, KVStringer, Tx, HexKVStringer(), verifyKeyOrder(), verifyPageReachable() (+2 more)

### Community 22 - "Community 22"
Cohesion: 0.10
Nodes (10): revtestdata, testdata, testdataitem, reflect.Value, testing.M, randByteSlice(), TestMain(), TestMain() (+2 more)

### Community 23 - "Community 23"
Cohesion: 0.21
Nodes (18): GetActiveMetaPage(), GetRootPage(), ReadPage(), ReadPageAndHWMSize(), WritePage(), ClearFreelist(), clearFreelistInMetaPage(), ClearPage() (+10 more)

### Community 25 - "Community 25"
Cohesion: 0.20
Nodes (17): testing.B, BenchmarkFastCheck(), benchmark_FreelistRelease(), Benchmark_FreelistRelease10000K(), Benchmark_FreelistRelease1000K(), Benchmark_FreelistRelease100K(), Benchmark_FreelistRelease10K(), randomPgids() (+9 more)

### Community 26 - "Community 26"
Cohesion: 0.14
Nodes (4): leafPageElement, NewLeafPageElement(), UnsafeByteSlice(), TestNode_read_LeafPage()

### Community 27 - "Community 27"
Cohesion: 0.14
Nodes (4): Pages, array, Pgids, Mergepgids()

### Community 28 - "Community 28"
Cohesion: 0.18
Nodes (17): createFilledDB(), fileSize(), fillDBWithKeys(), TestDB_Concurrent_WriteTo_and_ConsistentRead(), TestDB_MaxSizeExceededCanOpen(), TestDB_MaxSizeExceededCanOpenWithHighMmap(), TestDB_MaxSizeExceededDoesNotGrow(), TestDB_MaxSizeNotExceeded() (+9 more)

### Community 29 - "Community 29"
Cohesion: 0.20
Nodes (12): TestTx_allocatePageStats(), newFreelist(), Interface, ReadWriter, NewArrayFreelist(), newTestArrayFreelist(), Test_Freelist_Array_Rollback(), TestFreelistArray_allocate() (+4 more)

### Community 31 - "Community 31"
Cohesion: 0.15
Nodes (3): InBucket, NewInBucket(), LoadBucket()

### Community 32 - "Community 32"
Cohesion: 0.35
Nodes (5): Inode, Inodes, ReadInodeFromPage(), UsedSpaceInPage(), WriteInodeToPage()

### Community 33 - "Community 33"
Cohesion: 0.21
Nodes (6): newSafeWriter(), TestBenchCommand_Run(), ConcurrentBuffer, safeWriter, bytes.Buffer, sync.Mutex

### Community 34 - "Community 34"
Cohesion: 0.29
Nodes (5): os.File, time.Duration, atomicAddDuration(), atomicLoadDuration(), sameFile()

### Community 35 - "Community 35"
Cohesion: 0.22
Nodes (9): idToBytes(), TestFailpoint_LackOfDiskSpace(), TestFailpoint_MapFail(), TestFailpoint_mLockFail(), TestFailpoint_mLockFail_When_remap(), TestFailpoint_ResizeFileFail(), TestFailpoint_UnmapFail_DbClose(), TestIssue72() (+1 more)

### Community 36 - "Community 36"
Cohesion: 0.33
Nodes (7): NewXRay(), TestFindPathsToKey(), TestFindPathsToKey_Bucket(), TestFindPathsToKey_CycleDetected(), TestFindPathsToKey_MultipleBuckets(), TestTx_RecursivelyCheckPages_CorruptedLeaf(), TestTx_RecursivelyCheckPages_MisplacedPage()

### Community 37 - "Community 37"
Cohesion: 0.50
Nodes (7): VerificationType, DisableVerifications(), EnableAllVerifications(), EnableVerifications(), getEnvVerify(), IsVerificationEnabled(), Verify()

### Community 38 - "Community 38"
Cohesion: 0.48
Nodes (6): fdatasync(), flock(), funlock(), DB, mmap(), munmap()

### Community 41 - "Community 41"
Cohesion: 0.67
Nodes (5): walkFunc, Compact(), DB, walk(), walkBucket()

### Community 42 - "Community 42"
Cohesion: 0.53
Nodes (5): flock(), funlock(), DB, mmap(), munmap()

### Community 43 - "Community 43"
Cohesion: 0.53
Nodes (5): flock(), funlock(), DB, mmap(), munmap()

### Community 44 - "Community 44"
Cohesion: 0.53
Nodes (5): flock(), funlock(), DB, mmap(), munmap()

### Community 45 - "Community 45"
Cohesion: 0.53
Nodes (5): flock(), funlock(), DB, mmap(), munmap()

### Community 47 - "Community 47"
Cohesion: 0.50
Nodes (4): createAndPutKeys(), createDb(), DB, TestManyDBs()

### Community 48 - "Community 48"
Cohesion: 0.83
Nodes (3): fdatasync(), DB, msync()

### Community 49 - "Community 49"
Cohesion: 0.83
Nodes (3): prepareData(), TestMethodPage(), TestOpenWithPreLoadFreelist()

### Community 50 - "Community 50"
Cohesion: 0.67
Nodes (3): DB, mlock(), munlock()

### Community 51 - "Community 51"
Cohesion: 0.67
Nodes (3): DB, mlock(), munlock()

### Community 52 - "Community 52"
Cohesion: 0.83
Nodes (3): bench(), main(), compare_benchmarks.sh script

### Community 53 - "Community 53"
Cohesion: 0.83
Nodes (3): get_gpg_key(), main(), release.sh script

## Knowledge Gaps
- **5 isolated node(s):** `meta`, `go.etcd.io/bbolt`, `testdataitem`, `fix.sh script`, `simulateHandler`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 136 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **12 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `DB` connect `Community 0` to `Community 33`, `Community 2`, `Community 34`, `Community 4`, `Community 9`, `Community 11`, `Community 15`, `Community 18`, `Community 20`, `Community 23`, `Community 29`?**
  _High betweenness centrality (0.140) - this node is a cross-community bridge._
- **Why does `Pgid` connect `Community 20` to `Community 0`, `Community 32`, `Community 10`, `Community 11`, `Community 13`, `Community 14`, `Community 15`, `Community 16`, `Community 17`, `Community 19`, `Community 21`, `Community 23`, `Community 25`, `Community 27`, `Community 30`, `Community 31`?**
  _High betweenness centrality (0.123) - this node is a cross-community bridge._
- **Why does `Bucket` connect `Community 10` to `Community 1`, `Community 6`, `Community 41`, `Community 11`, `Community 12`, `Community 13`, `Community 14`, `Community 18`, `Community 19`, `Community 20`, `Community 21`, `Community 56`, `Community 31`?**
  _High betweenness centrality (0.119) - this node is a cross-community bridge._
- **Are the 5 inferred relationships involving `Open()` (e.g. with `getDiscardLogger()` and `prepareData()`) actually correct?**
  _`Open()` has 5 INFERRED edges - model-reasoned connections that need verification._
- **What connects `meta`, `go.etcd.io/bbolt`, `testdataitem` to the rest of the system?**
  _5 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Community 0` be split into smaller, more focused modules?**
  _Cohesion score 0.056158385684370836 - nodes in this community are weakly interconnected._
- **Should `Community 1` be split into smaller, more focused modules?**
  _Cohesion score 0.06027306027306027 - nodes in this community are weakly interconnected._