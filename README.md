# webbyLucifer v3.0

`webbyLucifer` is a multi-agent web workflow designed to minimize visual rework by making UI **asset-complete and implementation-ready before the implementation executor starts coding**.

```text
USER    = FINAL ACCEPTANCE AUTHORITY
CHATGPT = DESIGN / UI / ASSET / STATE / MOTION AUTHORITY
CLAUDE  = IMPLEMENTATION AUTHORITY
DRIVE   = HEAVY ASSET DELIVERY AUTHORITY
GITHUB  = CODE + LIGHTWEIGHT VERSIONED CONTRACT/STATE
VERCEL  = OPTIONAL PREVIEW / DEPLOYMENT
```

Canonical entrypoint: [`SKILL.md`](./SKILL.md).

## Why v3 exists

Previous visual-first flows could still create expensive loops:

```text
AI full-page render
→ missing/ambiguous asset pack
→ executor reverse-engineers pixels and chooses substitutes
→ implementation looks different
→ screenshot/fix/re-render loop
```

v3 changes the center of gravity:

```text
read/ask material inputs
→ decompose UI
→ count assets before producing them
→ create/collect high-res masters
→ productionize web delivery assets
→ freeze one Drive pack + manifest
→ build deterministic final UI from those exact assets and declared geometry
→ user approves
→ implementation-ready gate
→ short Claude contract
→ Claude codes without redesign/search/measurement
→ user accepts real website
```

## Core v3 rules

- Asset Count Plan happens before production.
- Raster masters are Full-HD-class minimum when production-authoritative; 4K-class is preferred, especially hero/full-bleed imagery.
- Do not use low-resolution patchwork or pretend a small enlarged file is a true high-resolution source.
- Heavy masters/asset packs go to one Google Drive project folder by default; GitHub is not the default 4K asset dump.
- Every visible final production asset must exist in the frozen pack or be an intentional declared placeholder/state.
- Asset identity must map to real `ITEM`s when identity matters; no index-based image guessing.
- Claude may not search/generate/substitute visual assets.
- Deterministic values create the final UI reference; Claude may not measure raster pixels to create implementation numbers.
- `VISUAL_DIRECTION_APPROVED` is not the same as `IMPLEMENTATION_READY_UI`.
- Claude does no long planning/audit/research for ordinary scoped UI tasks.
- Screenshot matrices are not a default implementation loop.
- The user performs final visual acceptance.

## Canonical v3 workflow

```text
GĐ0  Intake + environment/resource readiness
GĐ1  Visual direction/page structure
GĐ2  UI decomposition + Asset Count Plan
GĐ3  Asset classification + high-res production
GĐ4  Productionize + asset QA + Drive freeze
GĐ5  Deterministic UI composition + responsive/state/motion
GĐ6  User visual approval
GĐ7  IMPLEMENTATION_READY_UI gate
GĐ8  Short implementation contract
GĐ9  Claude implementation
GĐ10 Minimum proportional technical checks
GĐ11 User acceptance of real website
GĐ12 Functional QA → bug IDs → targeted fixes → final handoff
```

## New/updated v3 protocols

```text
references/ASSET_FIRST_IMPLEMENTATION_READY_PROTOCOL.md
references/INTAKE_DISCOVERY_PROTOCOL.md
references/VISUAL_HANDOFF_PROTOCOL.md
references/GITHUB_HANDOFF_PROTOCOL.md
references/AGENT_OWNERSHIP_PROTOCOL.md
references/QA_PROTOCOL.md
```

Legacy references remain for historical/compatible guidance where they do not conflict with v3.

## Asset classification

```text
BRAND       exact brand/logo/identity material
AUTHENTIC   real asset belonging to the exact item
DEMO        prototype/demo-only asset
EDITORIAL   content/article imagery
DECORATIVE  visual decoration without factual item identity
PLACEHOLDER intentional missing-data visual
DATA_VISUAL floorplan/map/progress/diagram tied to real data
```

## Master vs delivery

```text
MASTER SOURCE
= highest-quality source/archive; FHD/4K-class raster or vector as appropriate

WEB DELIVERY
= implementation-ready file copied/downloaded for the website
```

The executor normally uses the web delivery file, not the oversized master.

## Deterministic UI handoff

v3 separates:

```text
ASSET MANIFEST = which visual belongs where
SPEC/CONTRACT  = implementation values/behavior
RASTER         = human acceptance + hierarchy/arrangement reference
```

Core rule:

```text
SPEC → COMPOSITION → RASTER
```

Never:

```text
RASTER → measure pixels → magic numbers → code
```

If a number is missing, Claude returns `BLOCKED_SPEC` instead of measuring the screenshot.

## Claude task model

Default ordinary UI task:

```text
short contract + exact asset references
→ DRIFT / SCOPE / TOKEN pre-flight
→ read 1–3 relevant implementation files by default
→ code
→ minimum proportional checks
→ 3–5 line report
```

Blocker signals:

```text
NEED_ASSET
BLOCKED_SPEC
TECHNICAL_CONSTRAINT
```

## Package

```text
webbyLucifer/
├── SKILL.md
├── VERSION
├── CHANGELOG.md
├── references/
│   ├── ASSET_FIRST_IMPLEMENTATION_READY_PROTOCOL.md
│   ├── INTAKE_DISCOVERY_PROTOCOL.md
│   ├── VISUAL_HANDOFF_PROTOCOL.md
│   ├── GITHUB_HANDOFF_PROTOCOL.md
│   ├── AGENT_OWNERSHIP_PROTOCOL.md
│   ├── QA_PROTOCOL.md
│   └── legacy/supporting references...
├── schemas/
│   ├── project-intake.schema.json
│   ├── asset-count-plan.schema.json
│   ├── asset-manifest.schema.json
│   ├── handoff.schema.json
│   └── existing supporting schemas...
├── templates/
│   ├── PROJECT_INTAKE.example.json
│   ├── ASSET_COUNT_PLAN.example.json
│   ├── ASSET_MANIFEST.example.json
│   ├── HANDOFF.example.json
│   ├── CLAUDE_TASK.md
│   ├── UI_SETUP_CHECKLIST.md
│   └── existing supporting templates...
└── scripts/
    └── webby-validate.py
```

## Validator

```bash
python scripts/webby-validate.py /path/to/project
```

For v3 `IMPLEMENTATION_READY_UI`, the validator can catch important machine-verifiable failures such as:

- asset count not reported to user;
- incomplete readiness flags;
- missing Drive access declaration;
- missing asset manifest;
- AUTHENTIC/DATA_VISUAL without item mapping;
- master marked low-res-derived;
- missing web delivery mapping;
- delivery usage outside `allowedUsage`;
- delivery file exceeding declared max weight;
- remaining blocking requests.

The validator cannot judge artistic quality. Asset/UI quality and final acceptance remain human/design-authority responsibilities.

## Canonical repository

```text
th6322750-stack/webbyLucifer
```

Generalized changes belong here only with explicit user approval. Never publish client secrets, credentials, private data, proprietary client code or non-redistributable assets into this public skill repository.
