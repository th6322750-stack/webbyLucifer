# webbyLucifer

`webbyLucifer` is a public workflow/skill for taking a web project from client brief to **approved full UI -> complete production UI setup -> GitHub handoff -> Claude implementation -> ChatGPT visual QA -> production website**.

The core skill lives in [`SKILL.md`](./SKILL.md).

## Core architecture

```text
CHATGPT = FULL UI AUTHORITY
CLAUDE  = IMPLEMENTATION AUTHORITY
GITHUB  = VERSIONED EXCHANGE LAYER / SHARED PROJECT STATE
```

The most important rule is simple:

> **Claude must never be forced to guess an approved UI decision. ChatGPT must completely prepare the UI before implementation handoff.**

Implementation may begin only after the hard gate:

```text
UI_SETUP_COMPLETE
```

## Workflow

```text
GĐ1 — DESIGN / FULL-PAGE UI
ChatGPT
Input normalization -> design research -> demo directions -> approved WEB/MOBILE routes

GĐ2 — FULL UI MASTER / DESIGN SYSTEM
ChatGPT
Full Master + typography + colors/tokens + spacing + responsive intent + complete visual component system

GĐ3 — FULL PRODUCTION UI SETUP / GITHUB HANDOFF
ChatGPT
SVG/vector/raster/font assets + component states + asset placement + route/section/component maps + CLAUDE_TASK.md + HANDOFF.json

              ↓

        UI_SETUP_COMPLETE

              ↓

GĐ4 — STATIC FRONTEND IMPLEMENTATION
Claude by default
Translate the supplied visual system into real frontend code without redesigning it

GĐ5 — UX / FRONTEND ENHANCEMENT
Claude
Interactions + motion + application behavior + responsive implementation

GĐ6 — BACKEND / CMS / LOGIC
Claude
Only what the project requires

GĐ7 — QA / PRODUCTION
ChatGPT reviews visual truth; Claude fixes implementation
```

## ChatGPT responsibilities

Before handoff, ChatGPT owns the complete visual system:

- art direction;
- every required WEB/MOBILE route;
- Admin/CMS visual screens when required;
- full component visual system;
- applicable states such as hover/active/focus/loading/error/success;
- logos/icons/ornaments;
- SVG/vector and raster production resources;
- fonts and typography mapping;
- colors/tokens/spacing/radii/shadows/gradients;
- responsive visual intent;
- asset/component placement;
- route/section/component maps;
- Claude implementation prompt/handoff;
- visual QA.

If any required approved visual decision is missing, `UI_SETUP_COMPLETE` must remain false.

## Claude responsibilities

Claude owns implementation after the UI handoff:

- frontend code/component architecture;
- responsive code following the supplied visual contract;
- UX/interactions/animation implementation;
- forms/application state;
- API/CMS/database/auth/backend;
- accessibility and performance work that preserves the approved visual system;
- implementation fixes from ChatGPT QA.

Claude is not allowed to silently invent or replace missing approved visual decisions.

## GitHub as the bridge

Each real project should normally use its own project repository.

GitHub acts as:

```text
VERSIONED COMMUNICATION BUS
+ ASSET REGISTRY
+ UI IMPLEMENTATION CONTRACT
+ PROJECT STATE
+ QA EXCHANGE
```

A typical handoff package contains:

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

Claude pulls the exact UI state/commit, implements it, pushes code, then ChatGPT reviews browser output against the approved visual truth.

If Claude encounters a missing approved UI resource, it should create a request in the project handoff area rather than inventing the UI itself.

## Drive vs GitHub

Google Drive remains useful for client-facing full-resolution WEB/MOBILE design delivery and heavy original materials.

GitHub is the operational bridge between ChatGPT and Claude for production assets, implementation specs, code state and QA exchange.

## Source-first principle

Never guess production assets when an authoritative source exists. Do not crop screenshots to fake extractable assets, redraw existing vectors by eye, replace approved fonts with close alternatives, or convert normal UI sections into giant SVG screenshots.

## Canonical repository

This repository is the canonical public source of truth for the skill:

```text
th6322750-stack/webbyLucifer
```

Do not create random `v2`, `new`, `final`, or `final-final` replacement repositories. Generalized improvements are committed here only after explicit user approval.

## Privacy

Do not commit client secrets, private URLs, proprietary source code, unreleased designs, personal data, credentials, API keys or non-redistributable font/assets to this public skill repository.
