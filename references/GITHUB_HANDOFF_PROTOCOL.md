# GitHub Handoff Protocol

This reference defines the operational bridge between ChatGPT and Claude for `webbyLucifer` projects.

## Core ownership

```text
CHATGPT = FULL UI AUTHORITY
CLAUDE = IMPLEMENTATION AUTHORITY
GITHUB = VERSIONED EXCHANGE LAYER
```

Claude must never be asked to complete missing approved visual-design decisions.

The canonical workflow rules remain in `SKILL.md`. This document explains the project-repository exchange contract in more operational detail.

---

# 1. Required project handoff package

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

Use `references/SVG_PRODUCTION_PIPELINE.md` for production-vector rules.

---

# 2. Starter templates

The canonical skill repository provides starter files under:

```text
templates/
├── CLAUDE_TASK.md
├── HANDOFF.example.json
├── PROJECT_STATE.example.yaml
├── ASSET_MANIFEST.example.json
├── COMPONENT_MAP.example.json
├── PLACEMENT_MAP.example.json
├── REQUEST.example.json
└── UI_SETUP_CHECKLIST.md
```

Copy/adapt these into the real project repository. Do not keep placeholder values when handing off to Claude.

Templates are examples of the contract, not a reason to omit project-specific routes, components, assets, responsive rules or implementation constraints.

---

# 3. Handoff rule

Claude may begin implementation only when the project handoff declares:

```text
status = UI_SETUP_COMPLETE
```

ChatGPT must verify the corresponding hard gate in `SKILL.md` first.

If an applicable UI requirement is missing:

```text
UI_SETUP_COMPLETE = false
```

Do not use handoff wording such as:

```text
choose something suitable
use a similar icon
make it premium
adjust visually as needed
```

for an approved visual decision.

---

# 4. Commit synchronization

The handoff must identify the UI state/commit Claude is expected to consume.

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

Claude must not silently continue from a stale handoff when the UI package has changed materially.

---

# 5. ChatGPT publish contract

Before declaring `UI_SETUP_COMPLETE`, ChatGPT publishes and verifies:

- approved production assets;
- source-authority information;
- route/section/component maps;
- asset manifest;
- placement map;
- typography/tokens;
- responsive intent;
- visual interaction states;
- project state;
- Claude implementation task;
- handoff state;
- required hard-gate checklist.

ChatGPT must verify the actual GitHub commit/upload rather than merely claiming the files were created.

---

# 6. Claude consume contract

Claude begins by:

```text
git pull
↓
read .webby/HANDOFF.json
↓
verify expected UI commit/state
↓
read .webby/CLAUDE_TASK.md
↓
read route/section/component/asset/placement/typography/responsive specs
↓
inspect production assets
↓
implement static visual parity
```

After static parity, Claude may continue with the project-required:

- UX/interactions;
- motion;
- application state;
- forms;
- CMS;
- APIs;
- database;
- auth;
- backend/integrations;
- accessibility/performance improvements that preserve visual truth.

Claude may improve code architecture but does not gain visual-design authority by doing so.

---

# 7. Claude request loop

When implementation discovers a missing approved UI resource, Claude must not invent it.

Create a request in:

```text
.webby/requests/REQUEST-###.json
```

Use `templates/REQUEST.example.json` as the starter structure.

Minimum request information:

- request ID/type/status;
- consumed UI commit when relevant;
- route;
- section/component;
- missing UI resource/decision;
- why implementation is blocked or ambiguous;
- requested resolution;
- forbidden substitutions when relevant.

Then:

```text
CLAUDE REQUEST
↓
GITHUB
↓
CHATGPT supplies/clarifies UI resource
↓
CHATGPT updates manifests/specs
↓
CHATGPT commits new UI state
↓
GITHUB
↓
CLAUDE pulls and continues
```

Hard rule:

```text
MISSING APPROVED UI != CLAUDE DESIGNS IT
```

---

# 8. QA exchange

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
- authoritative source/spec reference;
- implementation commit when useful.

Claude fixes implementation and pushes again. ChatGPT re-runs acceptance.

The browser implementation does not become visual truth merely because it exists.

---

# 9. Forbidden shortcuts

- Claude silently replacing missing UI assets.
- Claude choosing a visually similar font/icon.
- Claude changing spacing/layout/colors to simplify implementation.
- Claude inventing mobile behavior when the approved responsive contract exists or should exist.
- ChatGPT handing off screenshots without component/asset/placement context.
- ChatGPT declaring `UI_SETUP_COMPLETE` with known hard UI blockers.
- Both agents independently editing the same visual truth.
- Treating browser code as visual authority because it already exists.
- Mixing client/private assets into the public canonical skill repository.

---

# 10. Final model

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
