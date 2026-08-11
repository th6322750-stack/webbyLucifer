# Changelog

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

- `SKILL.md` is now a v2 orchestration entrypoint;
- the full v1 GĐ1→GĐ7 workflow is preserved unchanged as `references/WORKFLOW_BASELINE_V1.md` and incorporated by reference;
- `UI_SETUP_COMPLETE` is strengthened from a human checklist to a machine-verifiable handoff gate when tooling is available.

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
