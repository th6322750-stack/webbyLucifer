# GitHub Handoff Protocol

This reference defines the operational bridge between ChatGPT and Claude for `webbyLucifer` projects.

## Core ownership

```text
CHATGPT = FULL UI AUTHORITY
CLAUDE = IMPLEMENTATION AUTHORITY
GITHUB = VERSIONED EXCHANGE LAYER
```

Claude must never be asked to complete missing approved visual design decisions.

## Required project handoff package

Before implementation, ChatGPT should publish at least:

```text
.webby/
├── PROJECT_STATE.yaml
├── HANDOFF.json
├── CLAUDE_TASK.md
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
└── qa/
```

Production assets should be separated from source/reference material.

```text
assets/
├── source/
│   ├── vectors/
│   └── raster/
└── production/
    ├── svg/
    ├── images/
    ├── logos/
    └── ornaments/
```

## Handoff rule

Claude may begin implementation only when the project handoff declares:

```text
status = UI_SETUP_COMPLETE
```

ChatGPT must verify the corresponding hard gate in `SKILL.md` first.

## Commit synchronization

The handoff should identify the UI state/commit Claude is expected to consume.

Claude should record the UI commit it consumed before implementation. This prevents situations where ChatGPT is reviewing asset/spec revision N while Claude is implementing revision N-2.

Recommended state fields:

```json
{
  "producer": "CHATGPT",
  "executor": "CLAUDE",
  "status": "UI_SETUP_COMPLETE",
  "uiCommit": "<sha>",
  "consumedUiCommit": null
}
```

If a metadata file cannot contain the SHA of the same commit that creates it, use the immediately preceding UI-package commit or create a small follow-up metadata commit. The important property is deterministic traceability.

## Claude request loop

When implementation discovers a missing approved UI resource, Claude must not invent it.

Create a request in:

```text
.webby/requests/REQUEST-###.json
```

Minimum request information:

- request type;
- route;
- section/component;
- missing UI resource/decision;
- why implementation is blocked or ambiguous.

Then ChatGPT supplies or clarifies the UI resource, updates manifests/specs, commits it, and Claude pulls the new state.

## QA exchange

After implementation, ChatGPT reviews browser output against the approved UI truth and may publish defects through:

```text
.webby/qa/defects.json
```

A useful visual defect records:

- route;
- viewport;
- section/component;
- severity;
- observed result;
- expected result;
- authoritative source/spec reference.

Claude fixes implementation and pushes again. ChatGPT re-runs acceptance.

## Forbidden shortcuts

- Claude silently replacing missing UI assets.
- Claude choosing a visually similar font/icon.
- Claude changing spacing/layout/colors to simplify implementation.
- ChatGPT handing off screenshots without component/asset/placement context.
- Both agents editing the same visual truth independently.
- Treating browser code as visual authority because it already exists.

## Final model

```text
CHATGPT FULL UI SETUP
        ↓
GITHUB UI COMMIT + HANDOFF
        ↓
UI_SETUP_COMPLETE
        ↓
CLAUDE IMPLEMENTATION
        ↓
GITHUB IMPLEMENTATION COMMIT
        ↓
CHATGPT QA
        ↓
GITHUB DEFECT CONTRACT
        ↓
CLAUDE FIX
        ↓
PRODUCTION READY
```
