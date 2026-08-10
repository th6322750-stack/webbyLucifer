# Changelog

## 2.1.0 — 2026-08-11

### Added

- actor/phase-aware runtime router to avoid loading the entire legacy workflow by default;
- Claude Minimal Handoff protocol and `.webby/claude-pack/` contract;
- token-efficiency rule: design knowledge is compressed into implementation instructions instead of transferred as rationale;
- optional `contractDigest`, `handoffCommit`, Claude-pack identity and audience metadata;
- project learning loop for evidence-backed UI, implementation and QA lessons;
- learning JSON schema;
- stronger semantic validation for contract identity, component/asset/placement references, Claude-pack presence and duplicate learning IDs.

### Changed

- `WORKFLOW_BASELINE_V1.md` is now legacy/compatibility authority instead of mandatory runtime context;
- Claude is explicitly excluded from full design knowledge, SVG-generation instructions, rejected UI history and unrelated QA/history by default;
- ChatGPT remains responsible for all material UI decisions before implementation;
- Webby now has an explicit `ROUTE + COMPRESS + VERIFY` role;
- handoff identity no longer assumes a Git commit can contain its own final SHA;
- protocol version bumped to `2.1.0`.

### Goal

Reduce Claude context/token usage and UI drift while preserving deterministic implementation and a reusable learning loop.

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
