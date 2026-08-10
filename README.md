# webbyLucifer

`webbyLucifer` is a public workflow/skill for taking a web project from client brief to **approved full UI -> complete production UI setup -> GitHub handoff -> Claude implementation -> ChatGPT visual QA -> production website**.

The authoritative operating rules live in [`SKILL.md`](./SKILL.md).

## Core architecture

```text
CHATGPT = FULL UI AUTHORITY
CLAUDE  = IMPLEMENTATION AUTHORITY
GITHUB  = VERSIONED EXCHANGE LAYER / SHARED PROJECT STATE
```

The highest-priority rule is:

> **Claude must never be forced to guess an approved UI decision. ChatGPT must completely prepare the UI before implementation handoff.**

Implementation may begin only after the hard gate:

```text
UI_SETUP_COMPLETE
```

---

# Skill package

The repository is intentionally packaged as one canonical skill with operating rules, deeper references and copy-ready handoff templates.

```text
webbyLucifer/
├── SKILL.md
├── README.md
│
├── references/
│   ├── KNOWLEDGE_PACK.md
│   ├── GITHUB_HANDOFF_PROTOCOL.md
│   └── SVG_PRODUCTION_PIPELINE.md
│
└── templates/
    ├── CLAUDE_TASK.md
    ├── HANDOFF.example.json
    ├── PROJECT_STATE.example.yaml
    ├── ASSET_MANIFEST.example.json
    ├── COMPONENT_MAP.example.json
    ├── PLACEMENT_MAP.example.json
    ├── REQUEST.example.json
    └── UI_SETUP_CHECKLIST.md
```

## File roles

### `SKILL.md`

Canonical workflow and hard rules. This is the first file an agent should read.

It defines:

- ChatGPT/Claude ownership boundaries;
- GĐ1-GĐ7;
- input normalization;
- design research and demo selection;
- full WEB/MOBILE design output;
- Master/design-system setup;
- production asset decomposition;
- SVG/vector rules;
- GitHub handoff;
- `UI_SETUP_COMPLETE`;
- Claude request loop;
- QA/production rules;
- continuous-learning/update policy.

### `references/KNOWLEDGE_PACK.md`

Reference-selection guide for design systems, SVG/vector tooling, frontend/backend tooling, accessibility, QA and agent handoff.

This is not an installation manifest.

```text
REFERENCE != DEPENDENCY
```

### `references/GITHUB_HANDOFF_PROTOCOL.md`

Defines the operational GitHub bridge between ChatGPT and Claude:

```text
CHATGPT UI PACKAGE
→ GITHUB UI COMMIT
→ CLAUDE IMPLEMENTATION
→ GITHUB CODE COMMIT
→ CHATGPT QA
→ DEFECT CONTRACT
→ CLAUDE FIX
```

### `references/SVG_PRODUCTION_PIPELINE.md`

Detailed production-vector contract covering:

- source authority;
- vector/raster/UI classification;
- canonical SVG;
- `viewBox`/aspect-ratio intent;
- collision-safe deterministic IDs;
- script/external-reference inspection;
- color/text/accessibility policy;
- optional SVG-to-component generation;
- placement mapping;
- browser visual QA;
- hard SVG failures that keep `UI_SETUP_COMPLETE = false`.

### `templates/*`

Starter files for real project repositories. Copy/adapt them into the project's `.webby/` handoff area rather than inventing a new contract every time.

---

# Workflow

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

---

# ChatGPT responsibilities

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

If any required approved visual decision is missing:

```text
UI_SETUP_COMPLETE = false
```

ChatGPT must finish the setup rather than asking Claude to complete the design.

---

# Claude responsibilities

Claude owns implementation after the UI handoff:

- frontend code/component architecture;
- responsive code following the supplied visual contract;
- UX/interactions/animation implementation;
- forms/application state;
- API/CMS/database/auth/backend;
- accessibility and performance work that preserves the approved visual system;
- implementation fixes from ChatGPT QA.

Claude is not allowed to silently invent or replace missing approved visual decisions.

If an approved resource/decision is missing, Claude creates a project request and returns that UI responsibility to ChatGPT.

---

# GitHub as the bridge

Each real project should normally use its own project repository.

The public `webbyLucifer` repository contains generalized workflow knowledge. Client production assets/code belong in the private/appropriate project repository.

GitHub acts as:

```text
VERSIONED COMMUNICATION BUS
+ ASSET REGISTRY
+ UI IMPLEMENTATION CONTRACT
+ PROJECT STATE
+ QA EXCHANGE
```

A typical project handoff package contains:

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

Production resources remain separated from authoritative/source files:

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

Claude pulls the exact UI state/commit, implements it, pushes code, then ChatGPT reviews browser output against the approved visual truth.

---

# Quick start for a real project

## 1. Load the skill

Read:

```text
SKILL.md
```

Then use only the reference files relevant to the current phase.

## 2. Start GĐ1

ChatGPT normalizes the client input, verifies delivery access where required, researches the design language, renders requested demo directions and obtains visual approval.

## 3. Complete GĐ2/GĐ3

ChatGPT builds the complete Master/component system and production UI package.

Use the repository templates as starting points for the project `.webby/` package.

## 4. Run the hard gate

Copy/adapt:

```text
templates/UI_SETUP_CHECKLIST.md
```

Do not hand off until all applicable required items pass.

## 5. Publish to the project GitHub repository

ChatGPT commits:

- production assets;
- maps/specs;
- `PROJECT_STATE.yaml`;
- `HANDOFF.json`;
- `CLAUDE_TASK.md`.

Record the deterministic UI commit/state.

## 6. Claude implements

Claude pulls the repo, reads the handoff contract, builds static visual parity first, then UX/frontend behavior and backend/CMS/logic.

## 7. ChatGPT QA

ChatGPT compares browser output against approved visual truth and returns defects through the GitHub QA contract until production acceptance.

---

# Drive vs GitHub

Google Drive remains useful for client-facing full-resolution WEB/MOBILE design delivery and heavy original materials.

GitHub is the operational bridge between ChatGPT and Claude for production assets, implementation specs, code state and QA exchange.

---

# Source-first principle

Never guess production assets when an authoritative source exists.

Do not:

- crop screenshots to fake extractable assets;
- redraw existing vectors by eye;
- replace approved fonts with close alternatives;
- replace custom approved icons with convenient generic icons;
- convert normal UI sections into giant SVG screenshots;
- optimize visual resources before fidelity is verified.

---

# Canonical repository

This repository is the canonical public source of truth for the skill:

```text
th6322750-stack/webbyLucifer
```

Do not create random `v2`, `new`, `final`, or `final-final` replacement repositories.

Generalized improvements are committed here only after explicit user approval.

---

# Privacy

Do not commit client secrets, private URLs, proprietary source code, unreleased designs, personal data, credentials, API keys or non-redistributable font/assets to this public skill repository.
