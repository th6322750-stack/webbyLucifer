# webbyLucifer v3.1

`webbyLucifer` is a multi-agent web workflow optimized for two goals at once:

1. **large/new UI work must be asset-complete and implementation-ready before Claude codes**;
2. **small polish/bug-fix work must not be forced through a heavyweight pipeline**.

```text
USER    = FINAL ACCEPTANCE AUTHORITY
CHATGPT = DESIGN / UI / ASSET / STATE / MOTION-FEEL AUTHORITY
CLAUDE  = IMPLEMENTATION / TECHNICAL-MECHANISM AUTHORITY
DRIVE   = HEAVY ASSET STORAGE/DELIVERY WHEN VERIFIED FOR CURRENT SESSION
GITHUB  = CODE + LIGHTWEIGHT CONTRACT/STATE + DELIVERY WHEN GIT/HYBRID MODE IS USED
VERCEL  = OPTIONAL PREVIEW / DEPLOYMENT
```

Canonical entrypoint: [`SKILL.md`](./SKILL.md).

## v3.1 task router

```text
TASK
|
|----- NEW_REDESIGN
|      |----- full asset-first pipeline
|
|----- EXISTING_POLISH
|      |----- fast scoped path
|
|----- BUG_FIX
       |----- targeted defect path
```

This prevents a five-line CSS polish task from paying the same process cost as a new website while preserving strict preparation for major design work.

## Full pipeline for NEW_REDESIGN

```text
GĐ0  Intake + environment/resource readiness
GĐ1  Visual direction/page structure
GĐ2  UI decomposition + Asset Count Plan
GĐ3  Asset classification + high-res production
GĐ4  Productionize + asset QA + transport freeze
GĐ5  Deterministic UI composition + responsive/state/motion feel
GĐ6  User visual approval
GĐ7  IMPLEMENTATION_READY_UI gate
GĐ8  Short implementation contract
GĐ9  Claude implementation
GĐ10 Minimum proportional technical checks
GĐ11 User acceptance
GĐ12 Functional QA → bug IDs → targeted fixes → final handoff
```

## Key v3.1 amendments

- `EXISTING_POLISH` and `BUG_FIX` fast paths avoid replaying the full pipeline.
- Motion is split into **FEEL** (ChatGPT) and **MECHANISM** (Claude).
- A mechanism change that intercepts global wheel/touch/key/default browser behavior is architecturally material even with zero new packages and must be reported before broad application.
- Google Drive access must be proved again in each work session when Drive is used.
- Asset transport modes are `DRIVE`, `GIT`, or `HYBRID`; HYBRID commonly means heavy masters in Drive and web delivery in Git/project paths.
- `ICON` is a UI **role**, not a new classification axis. Visible approved icons must exist in the icon inventory before full-pipeline readiness.
- Drive is a delivery/storage channel, not the default runtime image source. `destinationPath` or the declared runtime source controls where the implementation serves assets.
- Serious data-loss/security findings bypass the normal anti-scope-creep silence rule: report immediately, but do not turn that report into an unauthorized full audit.

Detailed amendments: [`references/V3_1_AMENDMENTS.md`](./references/V3_1_AMENDMENTS.md).

## Asset model

Classification describes the asset's authority/nature:

```text
BRAND
AUTHENTIC
DEMO
EDITORIAL
DECORATIVE
PLACEHOLDER
DATA_VISUAL
```

Role describes what it does in the UI:

```text
HERO
PROJECT_COVER
GALLERY
LOGO
ICON
FLOORPLAN
MAP
...
```

Master vs delivery:

```text
MASTER SOURCE = highest-quality source/archive; FHD/4K/vector as appropriate
WEB DELIVERY  = implementation-ready file the website actually uses
```

## Deterministic UI rule

```text
SPEC → COMPOSITION → RASTER
```

Never:

```text
RASTER → measure pixels → magic numbers → code
```

Raster is for human acceptance and arrangement. Spec/manifest carries implementation values, mappings, states and behavior.

## Claude task model

```text
short contract
→ DRIFT / SCOPE / TOKEN pre-flight
→ read 1–3 relevant implementation files by default
→ code
→ exact mapped assets if needed
→ proportional checks
→ 3–5 line report
```

Blockers:

```text
NEED_ASSET
BLOCKED_SPEC
TECHNICAL_CONSTRAINT
```

## Critical Finding rule

```text
current action is dangerous
→ stop that harmful action + report

existing unrelated critical bug discovered
→ report immediately + continue current task if safe/independent
```

No Critical Finding grants permission for a broad unsanctioned audit/refactor.

## Package

```text
webbyLucifer/
├── SKILL.md
├── VERSION
├── CHANGELOG.md
├── references/
│   ├── V3_1_AMENDMENTS.md
│   ├── ASSET_FIRST_IMPLEMENTATION_READY_PROTOCOL.md
│   ├── INTAKE_DISCOVERY_PROTOCOL.md
│   ├── VISUAL_HANDOFF_PROTOCOL.md
│   ├── GITHUB_HANDOFF_PROTOCOL.md
│   ├── AGENT_OWNERSHIP_PROTOCOL.md
│   ├── QA_PROTOCOL.md
│   └── legacy/supporting references...
├── schemas/
├── templates/
└── scripts/webby-validate.py
```

## Validator

```bash
python scripts/webby-validate.py /path/to/project
```

v3.1 validation distinguishes `NEW_REDESIGN` from fast-path tasks, validates current-session Drive proof when Drive/HYBRID is used, and can verify required icon inventory entries against actual `role=ICON` assets.

## Canonical repository

```text
th6322750-stack/webbyLucifer
```

Generalized changes belong here only with explicit user approval. Never publish client secrets, credentials, private data, proprietary client code or non-redistributable assets into this public skill repository.
