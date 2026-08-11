# webbyLucifer v2.1

`webbyLucifer` is a public multi-agent Design→Code workflow for taking a web project from client brief to **approved full UI → visual-first production handoff → Claude implementation → ChatGPT visual comparison → production website**.

```text
CHATGPT = FULL UI AUTHORITY
CLAUDE  = IMPLEMENTATION AUTHORITY
GITHUB  = VERSIONED EXCHANGE LAYER / SHARED PROJECT STATE
```

The canonical entrypoint is [`SKILL.md`](./SKILL.md).

## What changed in v2.1

The GĐ1→GĐ7 workflow and all v2 safety/verification infrastructure are preserved. v2.1 optimizes the UI→implementation bridge with:

- **Visual-First Handoff** — approved full-page renders carry visible UI truth;
- **Minimal Contract** — contracts focus on behavior, state, responsive rules, data and ambiguity rather than repeating obvious visible layout;
- route/viewport render mapping through `.webby/visual-handoff/routes.json`;
- route-scoped and component-scoped context loading to reduce unnecessary Claude token usage;
- visual reconstruction before implementation;
- implementation targets for normal code stacks and optional WordPress + Elementor;
- browser screenshot → approved render visual QA loop;
- validator checks for visual handoff mapping and missing approved renders.

Central rule:

```text
IMAGE    = VISIBLE FORM
CONTRACT = INVISIBLE / AMBIGUOUS BEHAVIOR
```

## Core workflow

```text
GĐ1 — DESIGN / FULL-PAGE UI                    ChatGPT
GĐ2 — FULL UI MASTER / DESIGN SYSTEM           ChatGPT
                 ↓
          USER APPROVAL
                 ↓
        APPROVED VISUAL TRUTH
                 ↓
GĐ3 — VISUAL-FIRST PRODUCTION HANDOFF          ChatGPT
                 ↓
 APPROVED RENDERS + MINIMAL CONTRACT
                 ↓
       SCHEMA + LOCK + VALIDATION
                 ↓
          UI_SETUP_COMPLETE
                 ↓
GĐ4 — VISUAL RECONSTRUCTION / IMPLEMENTATION   Claude
                 ↓
        REAL WEBSITE SCREENSHOT
                 ↓
        CHATGPT VISUAL COMPARISON
                 ↓
          DEFECTS ↔ CLAUDE FIX
                 ↓
GĐ5 — UX / FRONTEND ENHANCEMENT                Claude
GĐ6 — BACKEND / CMS / LOGIC                    Claude
GĐ7 — FINAL QA / PRODUCTION                    ChatGPT QA ↔ Claude fixes
```

## Package

```text
webbyLucifer/
├── SKILL.md
├── VERSION
├── CHANGELOG.md
├── references/
│   ├── WORKFLOW_BASELINE_V1.md
│   ├── VISUAL_HANDOFF_PROTOCOL.md
│   ├── GITHUB_HANDOFF_PROTOCOL.md
│   ├── AGENT_OWNERSHIP_PROTOCOL.md
│   ├── BRANCH_COMMIT_PROTOCOL.md
│   ├── QA_PROTOCOL.md
│   ├── KNOWLEDGE_PACK.md
│   └── SVG_PRODUCTION_PIPELINE.md
├── schemas/
│   ├── handoff.schema.json
│   ├── visual-handoff.schema.json
│   ├── webby-lock.schema.json
│   ├── asset-manifest.schema.json
│   ├── component-map.schema.json
│   ├── placement-map.schema.json
│   ├── request.schema.json
│   ├── implementation-receipt.schema.json
│   └── qa-defects.schema.json
├── templates/
│   ├── WEBBY_LOCK.example.json
│   ├── IMPLEMENTATION_RECEIPT.example.json
│   ├── QA_DEFECTS.example.json
│   └── existing v1 starter templates
└── scripts/
    └── webby-validate.py
```

## Visual-first handoff

A typical project can now publish:

```text
.webby/
├── HANDOFF.json
├── WEBBY_LOCK.json
├── visual-handoff/
│   ├── routes.json
│   ├── home-desktop.png
│   ├── home-mobile.png
│   ├── product-desktop.png
│   └── product-mobile.png
├── responsive.json
├── interactions.json
├── asset-manifest.json
├── requests/
├── implementation/
│   └── IMPLEMENTATION_RECEIPT.json
└── qa/
    ├── defects.json
    └── qa-report.json
```

The package does **not** require token-heavy text that restates every visible element. Optional component/placement contracts remain available when exact structure or geometry is materially needed.

## Hard handoff gate

Claude does not begin implementation simply because a prompt says the UI is ready. The project must satisfy applicable visual setup rules and publish a deterministic active UI state.

```text
UI_SETUP_COMPLETE =
approved visual scope
+ required approved route renders
+ minimal non-visible behavior contract
+ deterministic handoff
+ lock
+ no hard UI blocker
+ non-stale state
+ validation when available
```

## Implementation targets

### CODE — default

```text
Approved Render
→ Visual Reconstruction
→ React / Next.js / Vue / HTML/CSS / selected stack
```

### ELEMENTOR — only when required

```text
Approved Render
→ Visual Reconstruction
→ Elementor-compatible JSON/template
→ WordPress import
```

Elementor is only an implementation target. It does not replace webbyLucifer's authority, lock, revision, request, receipt or QA rules.

## Visual QA

```text
Approved Render = expected visual state
Browser Screenshot = implementation evidence
```

ChatGPT compares the real website at the matching viewport, publishes actionable defects, Claude fixes them, and ChatGPT re-checks before closure.

## Validation

Run the dependency-light semantic validator against a real project repository:

```bash
python scripts/webby-validate.py /path/to/project
```

The v2.1 validator also checks a declared Visual-First handoff's `routesFile`, route mappings, referenced render files, and UI revision/commit metadata when present.

JSON Schemas under `schemas/` provide stronger machine contracts for schema-aware tooling.

## Compatibility

v2.1 is an optimization of the handoff/implementation bridge, not a redesign of the workflow. Existing GĐ1–GĐ7 responsibilities, source-first rules, full WEB/MOBILE design requirements, SVG pipeline, revision/lock protection, request loop, implementation receipts and visual QA remain active.

The full v1 workflow is preserved unchanged in `references/WORKFLOW_BASELINE_V1.md` and incorporated by the current skill.

## Canonical repository

```text
th6322750-stack/webbyLucifer
```

Generalized improvements belong in this repository only after explicit user approval. Client secrets, proprietary code, unreleased client designs, credentials, personal data and non-redistributable assets must never be published here.
