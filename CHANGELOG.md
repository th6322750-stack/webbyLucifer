# Changelog

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

- canonical workflow is now `GĐ0 → GĐ1 → GĐ2 → GĐ3 → GĐ4 → GĐ5 → GĐ6 → GĐ7`;
- the old baseline `GĐ1.P PROJECT INTAKE / EVIDENCE LOCK` responsibility is absorbed into GĐ0 to avoid duplicate intake;
- `SKILL.md` was condensed into a lower-token orchestration entrypoint while retaining hard rules and phase-specific protocol references;
- GĐ1 may not begin while an unresolved material `HARD_GAP` can change design direction, personalization, conversion logic or scope;
- GĐ0 prioritizes the smallest useful set of high-information questions instead of a fixed generic questionnaire.

### Preserved

- GĐ1→GĐ7 responsibilities and ownership;
- ChatGPT as full visual/UI authority;
- Claude as implementation authority;
- GitHub as versioned exchange/state layer;
- Visual-First Handoff from v2.1;
- approved render as visible UI truth;
- minimal invisible/ambiguous behavior contract;
- route-scoped/context-on-demand token rules;
- source-first production asset rules;
- WEB/MOBILE final UI requirements;
- SVG production pipeline;
- deterministic UI revision and `WEBBY_LOCK.json`;
- stale-handoff protection;
- request lifecycle;
- implementation receipts;
- approved-render ↔ browser-screenshot visual QA loop.

## 2.1.0 — 2026-08-11

### Added

- Visual-First Handoff protocol;
- approved full-page render as primary visible UI truth;
- `.webby/visual-handoff/routes.json` route/viewport mapping;
- `visual-handoff.schema.json`;
- optional `visualHandoff` and scoped-context metadata in `HANDOFF.json` schema;
- route-scoped, component-scoped and on-demand contract loading rules;
- explicit Visual Reconstruction step before implementation;
- CODE implementation target plus optional WordPress + Elementor target;
- approved-render ↔ browser-screenshot QA loop;
- validator checks for visual handoff route mappings, missing renders and optional UI revision/commit mismatches.

### Changed

- handoff principle is now **VISUAL FIRST — CONTRACT SECOND**;
- visible UI should be derived from approved renders instead of duplicated into token-heavy prose/contracts;
- contracts focus on responsive behavior, interactions, dynamic states, navigation, data/CMS/API binding, accessibility and ambiguous/non-visible decisions;
- component/placement contracts remain available when exact deterministic structure or geometry is materially needed;
- `UI_SETUP_COMPLETE` now accounts for required approved renders when Visual-First Handoff is used;
- QA now explicitly treats approved render as expected visual state and browser screenshot as implementation evidence.

### Preserved

- GĐ1→GĐ7 phase ownership and order;
- ChatGPT as full visual/UI authority;
- Claude as implementation authority;
- GitHub as versioned exchange/state layer;
- source-first production asset rules;
- WEB/MOBILE final UI requirements;
- SVG production pipeline;
- deterministic UI revision and `WEBBY_LOCK.json`;
- stale-handoff protection;
- missing-UI request lifecycle;
- implementation receipts;
- ChatGPT visual QA → Claude fix loop.

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

### Changed

- `SKILL.md` became a v2 orchestration entrypoint;
- the full v1 GĐ1→GĐ7 workflow is preserved unchanged as `references/WORKFLOW_BASELINE_V1.md` and incorporated by reference;
- `UI_SETUP_COMPLETE` was strengthened from a human checklist to a machine-verifiable handoff gate when tooling is available.

### Preserved

- ChatGPT remains full visual/UI authority;
- Claude remains implementation authority;
- GitHub remains the versioned exchange/state layer;
- GĐ1→GĐ7 phase ownership and order;
- source-first production asset rules;
- WEB/MOBILE final UI requirements;
- SVG production pipeline;
- missing-UI request loop;
- ChatGPT visual QA → Claude fix loop.
