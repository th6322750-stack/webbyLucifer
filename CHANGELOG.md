# Changelog

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
