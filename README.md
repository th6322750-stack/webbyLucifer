# webbyLucifer v2

`webbyLucifer` is a public multi-agent Design→Code workflow for taking a web project from client brief to **approved full UI → complete production UI setup → machine-verifiable GitHub handoff → Claude implementation → ChatGPT visual QA → production website**.

```text
CHATGPT = FULL UI AUTHORITY
CLAUDE  = IMPLEMENTATION AUTHORITY
GITHUB  = VERSIONED EXCHANGE LAYER / SHARED PROJECT STATE
```

The canonical entrypoint is [`SKILL.md`](./SKILL.md).

## What changed in v2

The GĐ1→GĐ7 workflow is preserved. v2 strengthens the exchange layer with:

- machine-readable schemas;
- deterministic UI revision/commit tracking;
- `WEBBY_LOCK.json`;
- stale-handoff detection;
- agent ownership/write boundaries;
- implementation receipts;
- structured QA defects;
- a dependency-light handoff validator.

The full v1 workflow is preserved unchanged in `references/WORKFLOW_BASELINE_V1.md` and incorporated by the v2 skill.

## Core workflow

```text
GĐ1 — DESIGN / FULL-PAGE UI                    ChatGPT
GĐ2 — FULL UI MASTER / DESIGN SYSTEM           ChatGPT
GĐ3 — FULL PRODUCTION UI SETUP / HANDOFF       ChatGPT
                 ↓
       SCHEMA + LOCK + VALIDATION
                 ↓
          UI_SETUP_COMPLETE
                 ↓
GĐ4 — STATIC FRONTEND IMPLEMENTATION           Claude
GĐ5 — UX / FRONTEND ENHANCEMENT                Claude
GĐ6 — BACKEND / CMS / LOGIC                    Claude
GĐ7 — QA / PRODUCTION                          ChatGPT QA ↔ Claude fixes
```

## Package

```text
webbyLucifer/
├── SKILL.md
├── VERSION
├── CHANGELOG.md
├── references/
│   ├── WORKFLOW_BASELINE_V1.md
│   ├── GITHUB_HANDOFF_PROTOCOL.md
│   ├── AGENT_OWNERSHIP_PROTOCOL.md
│   ├── BRANCH_COMMIT_PROTOCOL.md
│   ├── QA_PROTOCOL.md
│   ├── KNOWLEDGE_PACK.md
│   └── SVG_PRODUCTION_PIPELINE.md
├── schemas/
│   ├── handoff.schema.json
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

## Hard handoff gate

Claude does not begin implementation simply because a prompt says the UI is ready. The project must satisfy the applicable visual setup rules and publish a deterministic active UI state.

```text
UI_SETUP_COMPLETE =
approved visual scope
+ complete production UI contract
+ deterministic handoff
+ lock
+ no hard UI blocker
+ non-stale state
+ validation when available
```

## Typical project `.webby/`

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
│   └── IMPLEMENTATION_RECEIPT.json
└── qa/
    ├── defects.json
    └── qa-report.json
```

## Validation

Run the dependency-light semantic validator against a real project repository:

```bash
python scripts/webby-validate.py /path/to/project
```

JSON Schemas under `schemas/` provide stronger machine contracts for schema-aware tooling.

## Compatibility

v2 is an infrastructure/protocol upgrade, not a redesign of the workflow. Existing GĐ1–GĐ7 responsibilities, source-first rules, full WEB/MOBILE design requirements, SVG pipeline, request loop and visual QA principles remain active through the preserved baseline.

## Canonical repository

```text
th6322750-stack/webbyLucifer
```

Generalized improvements belong in this repository only after explicit user approval. Client secrets, proprietary code, unreleased client designs, credentials, personal data and non-redistributable assets must never be published here.
