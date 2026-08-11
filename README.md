# webbyLucifer v2.2

`webbyLucifer` is a public multi-agent web workflow for taking a project from **raw/incomplete user input → personalized intake → approved full UI → visual-first implementation handoff → Claude implementation → ChatGPT visual QA → production website**.

```text
CHATGPT = FULL UI AUTHORITY
CLAUDE  = IMPLEMENTATION AUTHORITY
GITHUB  = VERSIONED EXCHANGE LAYER / SHARED PROJECT STATE
```

Canonical entrypoint: [`SKILL.md`](./SKILL.md).

## What changed in v2.2

v2.2 adds a mandatory phase before design:

```text
GĐ0 — INTAKE / DISCOVERY / PERSONALIZATION
```

GĐ0 is an adaptive discovery loop, not a fixed questionnaire.

Before asking anything, ChatGPT inspects all information the user already supplied: messages, links, screenshots, files, logo/brand assets, existing website/repository context, products/services, audience clues, content, references, features and technical constraints.

Then it asks only the missing questions that can materially improve or constrain the project.

Central GĐ0 rule:

```text
READ EXISTING INPUT FIRST
ASK ONLY WHAT IS MISSING
DO NOT RE-ASK KNOWN INFORMATION
DO NOT START GĐ1 WITH A MATERIAL HARD GAP
```

The normalized state can be stored as:

```text
.webby/PROJECT_INTAKE.json
```

using `schemas/project-intake.schema.json`.

## Core workflow

```text
RAW / PARTIAL USER INPUT
↓
GĐ0 — INTAKE / DISCOVERY / PERSONALIZATION     ChatGPT
↓
INTAKE_COMPLETE
↓
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
GĐ5 — UX / FRONTEND ENHANCEMENT                Claude
GĐ6 — BACKEND / CMS / LOGIC                    Claude
↓
REAL WEBSITE SCREENSHOT
↓
GĐ7 — CHATGPT VISUAL QA ↔ EXECUTOR FIX
↓
PRODUCTION_READY
```

## GĐ0 completion gate

`INTAKE_COMPLETE = true` only when the project has enough evidence to design specifically for that user/project rather than produce a generic template.

Typical required understanding:

- what is being designed;
- who it is for;
- primary goal / conversion goal;
- what makes the project distinct;
- authoritative content/assets/references;
- pages/routes/features in scope;
- important must-have and must-not-have constraints;
- enough personalization signals to guide design;
- no unresolved `HARD_GAP` that can materially change design or scope.

Missing information is classified as:

```text
KNOWN
ASSUMED
SOFT_GAP
HARD_GAP
NOT_APPLICABLE
```

A `SOFT_GAP` does not automatically block design. A material `HARD_GAP` does.

## Visual-first handoff remains active

v2.2 keeps the v2.1 principle:

```text
IMAGE    = VISIBLE FORM
CONTRACT = INVISIBLE / AMBIGUOUS BEHAVIOR
```

Approved WEB/MOBILE renders carry visible UI truth. Contracts focus on responsive behavior, interactions, state, data/CMS/API binding, accessibility, routing and other information that images cannot safely communicate.

## Package

```text
webbyLucifer/
├── SKILL.md
├── VERSION
├── CHANGELOG.md
├── references/
│   ├── WORKFLOW_BASELINE_V1.md
│   ├── INTAKE_DISCOVERY_PROTOCOL.md
│   ├── VISUAL_HANDOFF_PROTOCOL.md
│   ├── GITHUB_HANDOFF_PROTOCOL.md
│   ├── AGENT_OWNERSHIP_PROTOCOL.md
│   ├── BRANCH_COMMIT_PROTOCOL.md
│   ├── QA_PROTOCOL.md
│   ├── KNOWLEDGE_PACK.md
│   └── SVG_PRODUCTION_PIPELINE.md
├── schemas/
│   ├── project-intake.schema.json
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
│   ├── PROJECT_INTAKE.example.json
│   ├── WEBBY_LOCK.example.json
│   ├── IMPLEMENTATION_RECEIPT.example.json
│   ├── QA_DEFECTS.example.json
│   └── existing v1 starter templates
└── scripts/
    └── webby-validate.py
```

## Typical project `.webby/`

```text
.webby/
├── PROJECT_INTAKE.json
├── PROJECT_STATE.yaml
├── HANDOFF.json
├── WEBBY_LOCK.json
├── visual-handoff/
│   ├── routes.json
│   └── approved WEB/MOBILE renders...
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

## Validator

Run:

```bash
python scripts/webby-validate.py /path/to/project
```

For v2.2+ projects declaring `UI_SETUP_COMPLETE`, the validator can reject handoffs when:

- `PROJECT_INTAKE.json` is missing;
- intake is not `INTAKE_COMPLETE`;
- `HARD_GAP` items remain;
- core project/audience/goal/scope intake data is absent;
- no personalization signal is recorded;
- existing Visual-First handoff/lock/render rules fail.

## Compatibility

v2.2 adds GĐ0 before the existing workflow. GĐ1→GĐ7 ownership and responsibilities remain preserved.

The older `GĐ1.P PROJECT INTAKE / EVIDENCE LOCK` from `references/WORKFLOW_BASELINE_V1.md` is absorbed into GĐ0 in v2.2; agents must not run duplicate intake.

Source-first assets, WEB/MOBILE final UI, SVG production, Visual-First Handoff, revision/lock protection, request lifecycle, implementation receipts and visual QA remain active.

## Canonical repository

```text
th6322750-stack/webbyLucifer
```

Generalized improvements belong in this repository only after explicit user approval. Do not publish client secrets, proprietary code, unreleased client designs, credentials, personal data or non-redistributable assets here.
