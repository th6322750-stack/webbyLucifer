# GitHub Handoff Protocol — webbyLucifer v2

## Core ownership

```text
CHATGPT = FULL UI AUTHORITY
CLAUDE = IMPLEMENTATION AUTHORITY
GITHUB = VERSIONED EXCHANGE LAYER / SHARED PROJECT STATE
```

The full design/implementation workflow is defined by `SKILL.md` plus `references/WORKFLOW_BASELINE_V1.md`. This document defines the v2 GitHub exchange contract.

## 1. Required project handoff

Before implementation, ChatGPT SHOULD publish:

```text
.webby/
├── PROJECT_STATE.yaml
├── HANDOFF.json
├── WEBBY_LOCK.json
├── CLAUDE_TASK.md
├── visual-contract.json
├── asset-manifest.json
├── component-map.json
├── placement-map.json
├── route-map.json
├── section-map.json
├── typography.json
├── tokens.json
├── responsive.json
├── interactions.json
├── requests/
├── implementation/
└── qa/
```

## 2. Active UI identity

The active handoff SHOULD identify:

```text
handoffId
uiRevision
uiCommit
parentUiCommit
createdAt
status
```

The lock file repeats the active identity and lists contract files/assets that belong to that handoff.

## 3. UI_SETUP_COMPLETE

The baseline visual checklist remains mandatory. v2 additionally requires deterministic handoff state, lock consistency, no known hard UI blocker and validation when available.

If validation fails:

```text
UI_SETUP_COMPLETE = false
```

## 4. Lock contract

`.webby/WEBBY_LOCK.json` records the exact contract state expected by the executor. File entries may include `sha256` when tooling can calculate it.

A lock is not a substitute for Git commit identity; it complements Git history with explicit handoff scope.

## 5. Claude consume protocol

```text
git pull
↓
read HANDOFF.json
↓
read WEBBY_LOCK.json
↓
compare active UI revision/commit with previously consumed UI state
↓
run validator when available
↓
read CLAUDE_TASK + maps/assets
↓
record consumed UI state
↓
implement static parity
```

If current active UI changed materially after Claude's consumed revision:

```text
STALE_HANDOFF
```

Do not silently continue from the obsolete UI state.

## 6. Ownership boundaries

Read `references/AGENT_OWNERSHIP_PROTOCOL.md`.

Claude must not modify active ChatGPT-owned visual contracts/assets merely to simplify implementation. ChatGPT should not rewrite Claude-owned implementation code during ordinary visual QA.

## 7. Missing UI request lifecycle

Recommended lifecycle:

```text
OPEN → ACKNOWLEDGED → RESOLVED → CONSUMED → CLOSED
```

A resolution SHOULD identify the resolution commit/revision and affected files.

Hard rule:

```text
MISSING APPROVED UI != CLAUDE DESIGNS IT
```

## 8. Implementation receipt

After a meaningful implementation milestone Claude SHOULD publish:

```text
.webby/implementation/IMPLEMENTATION_RECEIPT.json
```

It records consumed UI state, implementation commit, implemented scope, build/test state and unresolved requests/blockers.

## 9. QA exchange

ChatGPT reviews the browser against approved visual truth and writes stable defect IDs to `.webby/qa/defects.json` or an equivalent contract conforming to the v2 QA schema.

Claude fixes against defect IDs and marks them `FIXED_PENDING_QA`. ChatGPT re-tests and closes or reopens them.

## 10. Commit traceability

Recommended commit prefixes:

```text
webby(ui):
webby(lock):
webby(request):
webby(impl):
webby(qa):
webby(fix):
```

See `references/BRANCH_COMMIT_PROTOCOL.md`.

## 11. Forbidden shortcuts

- handoff without deterministic active UI state when Git state is available;
- Claude silently substituting missing UI assets/fonts/icons;
- Claude mutating visual contracts to make code easier;
- ChatGPT declaring UI setup complete despite known hard blockers;
- continuing from a materially stale UI handoff;
- self-closing visual QA defects without ChatGPT re-acceptance;
- publishing client/private material to the public canonical skill repository.

## 12. Final model

```text
CHATGPT UI PACKAGE
↓
HANDOFF + LOCK + VALIDATION
↓
UI_SETUP_COMPLETE
↓
CLAUDE CONSUMES EXACT UI STATE
↓
IMPLEMENTATION + RECEIPT
↓
CHATGPT QA DEFECT CONTRACT
↓
CLAUDE FIX
↓
CHATGPT ACCEPTANCE
↓
PRODUCTION_READY
```
