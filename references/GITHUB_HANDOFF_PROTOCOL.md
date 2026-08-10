# GitHub Handoff Protocol — webbyLucifer v2.1

## Core ownership

```text
CHATGPT = FULL UI AUTHORITY
WEBBY = ROUTE + COMPRESS + VERIFY
CLAUDE = IMPLEMENTATION AUTHORITY
GITHUB = VERSIONED EXCHANGE LAYER / SHARED PROJECT STATE
```

The source UI contract may be rich. The implementation executor should receive only the subset required for the current implementation scope.

## 1. Source handoff

Before implementation, ChatGPT/Webby SHOULD publish the applicable source truth under `.webby/`, including handoff/lock identity, visual contracts, maps, production assets and request state.

## 2. Compiled implementation handoff

For Claude, compile:

```text
.webby/claude-pack/
├── TASK.md
├── contract.json
├── components.json
├── assets.json
├── responsive.json
└── lock.json
```

Read `references/CLAUDE_MINIMAL_HANDOFF.md`.

The pack contains implementation facts, not the full design knowledge base.

## 3. Active UI identity

The active handoff SHOULD identify:

```text
handoffId
uiRevision
uiCommit
parentUiCommit
handoffCommit when known
contractDigest when available
createdAt
status
```

`uiCommit` identifies the UI package state. A later handoff commit may reference that commit; do not require a Git commit to contain its own final SHA.

The lock repeats active identity and may include a Claude-pack digest.

## 4. UI_SETUP_COMPLETE

The applicable visual checklist remains mandatory. v2.1 additionally requires deterministic handoff state, lock consistency, no known hard UI blocker, validation when available, and a compilable implementation pack for the requested scope.

If available validation fails:

```text
UI_SETUP_COMPLETE = false
```

## 5. Claude consume protocol

```text
git pull
↓
read compiled Claude pack
↓
verify pack/handoff identity
↓
compare with previously consumed state
↓
run validator when available
↓
record consumed identity
↓
implement current scope
```

Claude MUST NOT load the full legacy workflow, design knowledge pack, SVG design-generation material, rejected UI history or unrelated QA/learning history by default.

If active UI changed materially:

```text
STALE_HANDOFF
```

Consume the new pack or create a request when migration is ambiguous.

## 6. Ownership boundaries

Read `references/AGENT_OWNERSHIP_PROTOCOL.md`.

Claude must not modify active ChatGPT-owned visual contracts/assets merely to simplify implementation. ChatGPT should publish QA defects rather than casually rewriting Claude-owned implementation code.

## 7. Missing UI request lifecycle

```text
OPEN → ACKNOWLEDGED → RESOLVED → CONSUMED → CLOSED
```

Hard rule:

```text
MISSING APPROVED UI != CLAUDE DESIGNS IT
```

A resolution SHOULD identify the affected UI revision/commit and files. Webby then recompiles affected implementation facts.

## 8. Implementation receipt

After a meaningful implementation milestone Claude SHOULD publish:

```text
.webby/implementation/IMPLEMENTATION_RECEIPT.json
```

It records consumed UI/pack identity, implementation commit, implemented scope, build/test state and unresolved requests/blockers.

## 9. QA exchange

ChatGPT reviews the browser against approved visual truth and writes stable defect IDs to `.webby/qa/defects.json` or an equivalent v2 contract.

Claude fixes against defect IDs and marks them `FIXED_PENDING_QA`. ChatGPT re-tests and closes or reopens them.

## 10. Learning exchange

After QA, ChatGPT/Webby MAY extract evidence-backed lessons according to `references/LEARNING_LOOP.md`.

Learning is used to improve future design/packaging. It is not copied wholesale into Claude context.

## 11. Commit traceability

Recommended prefixes:

```text
webby(ui):
webby(lock):
webby(pack):
webby(request):
webby(impl):
webby(qa):
webby(fix):
webby(learn):
```

See `references/BRANCH_COMMIT_PROTOCOL.md`.

## 12. Forbidden shortcuts

- handoff without deterministic active UI state when Git state is available;
- Claude silently substituting missing UI assets/fonts/icons;
- Claude loading full design history by default when the compiled pack is sufficient;
- Claude mutating visual contracts to make code easier;
- ChatGPT declaring UI setup complete despite known hard blockers;
- continuing from a materially stale UI handoff;
- self-closing visual QA defects without ChatGPT re-acceptance;
- dumping raw learning/history into implementation context without relevance filtering;
- publishing client/private material to the public canonical skill repository.

## 13. Final model

```text
CHATGPT UI SOURCE CONTRACT
↓
WEBBY VALIDATE + LOCK + COMPILE
↓
MINIMAL CLAUDE PACK
↓
CLAUDE IMPLEMENTATION + RECEIPT
↓
CHATGPT QA DEFECT CONTRACT
↓
CLAUDE FIX
↓
CHATGPT ACCEPTANCE
↓
LEARNING EXTRACTION
↓
PRODUCTION_READY
```
