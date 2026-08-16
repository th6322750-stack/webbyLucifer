# Changelog

## 3.1.0 — 2026-08-17

### Added

- mandatory `TASK ROUTER` with three modes: `NEW_REDESIGN`, `EXISTING_POLISH`, `BUG_FIX`;
- fast path for small existing visual polish so minor CSS/component work does not replay the full asset-first pipeline;
- targeted bug-fix path that avoids redesign/re-audit scope expansion;
- motion ownership split: **ChatGPT owns FEEL**, **Claude owns MECHANISM**;
- explicit global-behavior-surface rule covering site-wide wheel/touch/key interception, browser-scroll replacement, app-wide event capture and similar mechanism changes even when no new dependency is added;
- session-scoped Drive proof: Drive readiness must be re-verified with a real download in the current work session;
- asset transport modes `DRIVE / GIT / HYBRID`;
- `workSessionId` / `verifiedForSessionId` handoff model for non-permanent Drive readiness;
- icon inventory gate: `ICON` remains a UI role, and every visible approved icon must have a real mapped asset before full-pipeline readiness;
- explicit rule that Drive is storage/delivery, not default runtime serving architecture; manifest `destinationPath` or declared runtime source is authoritative;
- `CRITICAL_FINDING` exception with two branches: stop a currently harmful action, or report an existing unrelated critical bug while continuing safe independent work;
- `references/V3_1_AMENDMENTS.md`.

### Changed

- `IMPLEMENTATION_READY_UI` full asset/intake gates apply to `NEW_REDESIGN`; fast-path tasks use lightweight readiness instead of Asset Count/4K/Drive bureaucracy when no new asset pipeline is involved;
- screenshots are explicitly optional for `EXISTING_POLISH`, not a default prerequisite;
- Claude may choose the technical motion implementation without design approval when feel/observable behavior stay unchanged and no material global behavior surface is introduced;
- Drive access is no longer modeled as a permanent project boolean;
- v3.1 validator distinguishes full-pipeline vs fast-path handoffs and validates current-session Drive proof plus icon inventory mappings.

## 3.0.0 — 2026-08-17

### Added

- **Asset-First Implementation-Ready UI** protocol as the new canonical center of the workflow;
- mandatory **Asset Count Plan before asset production**, including user-visible counts for existing, ChatGPT-produced and user-required assets;
- high-resolution raster source policy: Full-HD-class minimum for production-authoritative raster masters, 4K-class preferred, especially hero/full-bleed imagery;
- hard ban on low-resolution patchwork and on presenting simple low-res enlargement as a true high-resolution source authority;
- Google Drive as the default heavy asset delivery store, with GitHub focused on code and lightweight versioned contracts/state;
- asset taxonomy: `BRAND / AUTHENTIC / DEMO / EDITORIAL / DECORATIVE / PLACEHOLDER / DATA_VISUAL`;
- identity mapping (`ITEM`) and `ALLOWED_USAGE` enforcement model;
- master-source vs web-delivery asset separation;
- usage-specific crop/object-position/safe-area model;
- deterministic UI composition rule: **spec creates render; render never creates spec**;
- hard **“look at raster, do not measure raster”** rule for implementation;
- `VISUAL_DIRECTION_APPROVED` vs `IMPLEMENTATION_READY_UI` as distinct states;
- `IMPLEMENTATION_READY_UI` readiness gate covering assets, Drive, mapping, geometry, responsive, state and motion readiness;
- short Claude implementation task contract with only `DRIFT / SCOPE / TOKEN` pre-flight checks;
- explicit blocker vocabulary: `NEED_ASSET / BLOCKED_SPEC / TECHNICAL_CONSTRAINT`;
- user as final visual acceptance authority;
- user-facing terminology rule requiring plain-Vietnamese explanation of material English/specialist terms;
- `references/ASSET_FIRST_IMPLEMENTATION_READY_PROTOCOL.md`;
- `schemas/asset-count-plan.schema.json` and `templates/ASSET_COUNT_PLAN.example.json`;
- v3 asset manifest schema/template with Drive references, master quality, identity, usage, delivery and presentation metadata.

### Changed

- GĐ0 now includes repository/branch/remote-local drift/Drive/Vercel/data-source readiness plus the major full-width/boxed/mixed layout decision;
- full-page AI raster is no longer sufficient implementation authority;
- raster is now primarily human acceptance/hierarchy evidence, while spec/manifest carry implementation numbers and mappings;
- Claude no longer performs long planning, repo-wide audit, external design research, asset search/generation/substitution, screenshot matrices or full visual self-QA by default for ordinary scoped UI work;
- default ordinary UI context targets 1–3 relevant implementation files;
- screenshot comparison changed from a default visual reconstruction loop to optional evidence used only when it adds value;
- QA now separates asset QA, proportional technical checks, user visual acceptance and later functional QA;
- Google Drive access is checked before asset handoff; images visible only in chat are not considered delivered;
- asset completeness now requires every visible approved-final production asset to exist in the frozen pack or be an intentional declared placeholder/state;
- v3 validator checks implementation-ready flags, Asset Count Plan reporting, Drive access, v3 asset identity/quality/delivery constraints and max-weight rules;
- handoff schema now uses `NOT_READY / VISUAL_DIRECTION_APPROVED / IMPLEMENTATION_READY_UI / SUPERSEDED`.

### Preserved

- ChatGPT remains Design/UI authority;
- Claude remains implementation authority;
- deterministic revision/lock concepts remain available;
- request/blocker lifecycle remains available;
- implementation receipts and stable defect IDs remain available;
- useful v2.x and v1 reference material remains compatible only where it does not conflict with v3 hard rules.

## 2.2.0 — 2026-08-11

### Added

- mandatory **GĐ0 — Intake / Discovery / Personalization** before GĐ1;
- adaptive discovery loop that inspects existing user/project evidence before asking questions;
- hard rule preventing agents from asking users to repeat already-known information;
- `INTAKE_COMPLETE` gate before design;
- `KNOWN / ASSUMED / SOFT_GAP / HARD_GAP / NOT_APPLICABLE` intake classification;
- `references/INTAKE_DISCOVERY_PROTOCOL.md`;
- `.webby/PROJECT_INTAKE.json` project state convention;
- `schemas/project-intake.schema.json`;
- `templates/PROJECT_INTAKE.example.json`;
- optional intake metadata in `HANDOFF.json` schema;
- v2.2+ validator checks for missing/incomplete intake, remaining `HARD_GAP`, missing core audience/goal/scope data and missing personalization signals.

### Changed

- canonical workflow became `GĐ0 → GĐ1 → GĐ2 → GĐ3 → GĐ4 → GĐ5 → GĐ6 → GĐ7`;
- the old baseline `GĐ1.P PROJECT INTAKE / EVIDENCE LOCK` responsibility was absorbed into GĐ0 to avoid duplicate intake;
- `SKILL.md` was condensed into a lower-token orchestration entrypoint while retaining hard rules and phase-specific protocol references;
- GĐ1 may not begin while an unresolved material `HARD_GAP` can change design direction, personalization, conversion logic or scope;
- GĐ0 prioritizes the smallest useful set of high-information questions instead of a fixed generic questionnaire.

## 2.1.0 — 2026-08-11

### Added

- Visual-First Handoff protocol;
- approved full-page render as primary visible UI truth;
- `.webby/visual-handoff/routes.json` route/viewport mapping;
- `visual-handoff.schema.json`;
- route-scoped, component-scoped and on-demand contract loading rules;
- explicit Visual Reconstruction step before implementation;
- CODE implementation target plus optional WordPress + Elementor target;
- approved-render ↔ browser-screenshot QA loop.

### Changed

- handoff principle became **VISUAL FIRST — CONTRACT SECOND**;
- visible UI was derived from approved renders instead of duplicated into token-heavy prose/contracts.

## 2.0.0 — 2026-08-10

### Added

- machine-readable handoff schemas;
- `WEBBY_LOCK.json` contract;
- deterministic UI revision and stale-handoff rules;
- agent ownership/write-boundary protocol;
- branch/commit guidance for multi-agent exchange;
- implementation receipt contract;
- structured QA defect contract;
- dependency-light `webby-validate.py` validator.
