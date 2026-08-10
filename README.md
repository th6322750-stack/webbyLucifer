# webbyLucifer v2.1

`webbyLucifer` is a public multi-agent Design→Code workflow for taking a web project from client brief to **approved full UI → production UI contract → compressed implementation handoff → Claude implementation → ChatGPT visual QA → reusable learning → production website**.

```text
CHATGPT = FULL UI AUTHORITY
WEBBY   = ROUTE + COMPRESS + VERIFY
CLAUDE  = IMPLEMENTATION AUTHORITY
GITHUB  = VERSIONED EXCHANGE LAYER / SHARED PROJECT STATE
```

The canonical entrypoint is [`SKILL.md`](./SKILL.md).

## What changed in v2.1

v2.1 focuses on **lower Claude token usage and lower UI drift**.

- phase/actor-aware protocol loading;
- the legacy v1 baseline is no longer mandatory runtime context;
- Claude receives a minimal `.webby/claude-pack/` instead of the full design knowledge base;
- ChatGPT keeps all material UI decisions;
- Webby compresses those decisions into deterministic implementation facts;
- handoff identity adds optional `contractDigest` / `handoffCommit` semantics;
- semantic validation checks more contract cross-references;
- project QA/request outcomes can feed an evidence-backed learning loop without dumping history into Claude context.

## Core workflow

```text
GĐ1 — DESIGN / FULL-PAGE UI                    ChatGPT
GĐ2 — FULL UI MASTER / DESIGN SYSTEM           ChatGPT
GĐ3 — FULL PRODUCTION UI SETUP / HANDOFF       ChatGPT
                 ↓
        WEBBY VALIDATE + LOCK
                 ↓
        COMPILE CLAUDE PACK
                 ↓
          UI_SETUP_COMPLETE
                 ↓
GĐ4 — STATIC FRONTEND IMPLEMENTATION           Claude
GĐ5 — UX / FRONTEND ENHANCEMENT                Claude
GĐ6 — BACKEND / CMS / LOGIC                    Claude
GĐ7 — QA / PRODUCTION                          ChatGPT QA ↔ Claude fixes
                 ↓
          LEARNING EXTRACTION
```

## Claude minimal handoff

By default Claude should consume only the implementation-relevant subset:

```text
.webby/claude-pack/
├── TASK.md
├── contract.json
├── components.json
├── assets.json
├── responsive.json
└── lock.json
```

Claude does **not** need to read the full legacy workflow, design knowledge pack, SVG design/reconstruction instructions, rejected UI history or unrelated QA history unless an exceptional implementation ambiguity requires it.

The principle is:

```text
CHATGPT = THINK + DESIGN
WEBBY   = COMPRESS + VERIFY
CLAUDE  = IMPLEMENT
```

## Package

```text
webbyLucifer/
├── SKILL.md
├── VERSION
├── CHANGELOG.md
├── references/
│   ├── PHASE_ROUTER.md
│   ├── CLAUDE_MINIMAL_HANDOFF.md
│   ├── LEARNING_LOOP.md
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
│   ├── qa-defects.schema.json
│   └── learning.schema.json
├── templates/
└── scripts/
    └── webby-validate.py
```

## Typical project `.webby/`

```text
.webby/
├── PROJECT_STATE.yaml
├── HANDOFF.json
├── WEBBY_LOCK.json
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
├── claude-pack/
├── implementation/
│   └── IMPLEMENTATION_RECEIPT.json
├── qa/
│   ├── defects.json
│   └── qa-report.json
└── learning/
    ├── PROJECT_LESSONS.json
    ├── UI_PATTERNS.json
    └── FAILURE_PATTERNS.json
```

## Hard handoff gate

Claude does not begin implementation simply because a prompt says the UI is ready.

```text
UI_SETUP_COMPLETE =
approved visual scope
+ complete production UI contract
+ deterministic handoff
+ lock
+ no hard UI blocker
+ non-stale state
+ validation when available
+ compilable minimal Claude pack
```

## Validation

Run the dependency-light semantic validator against a project repository:

```bash
python scripts/webby-validate.py /path/to/project
```

It checks handoff/lock identity, locked files and hashes, selected asset/component/placement cross-references, blocking requests, Claude-pack presence when declared, and learning-ID integrity. JSON Schemas under `schemas/` remain the canonical structural contracts for schema-aware tooling.

## Learning loop

Project lessons are owned by ChatGPT/Webby and are retrieved selectively. They are not copied wholesale into Claude prompts.

```text
requests + QA defects + outcomes
→ concise reusable lessons
→ future ChatGPT design/packaging
→ smaller implementation contract
→ fewer repeated defects
```

## Compatibility

v2.1 preserves the GĐ1→GĐ7 responsibilities and v1 visual/source-first principles. `references/WORKFLOW_BASELINE_V1.md` remains compatibility authority, but it is no longer mandatory runtime context for every actor and phase.

## Canonical repository

```text
th6322750-stack/webbyLucifer
```

Generalized improvements belong in this repository only after explicit user approval. Client secrets, proprietary code, unreleased client designs, credentials, personal data and non-redistributable assets must never be published here.
