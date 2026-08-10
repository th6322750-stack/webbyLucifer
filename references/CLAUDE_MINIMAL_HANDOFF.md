# Claude Minimal Handoff — webbyLucifer v2.1

## Purpose

Claude is an implementation executor, not a second UI designer. The handoff must minimize context while preserving deterministic implementation facts.

## Canonical pack

Before Claude begins, Webby/ChatGPT SHOULD compile:

```text
.webby/claude-pack/
├── TASK.md
├── contract.json
├── components.json
├── assets.json
├── responsive.json
└── lock.json
```

Only add another file when it contains implementation-critical information that cannot be represented in the files above.

## What belongs in the pack

### TASK.md

- current implementation goal;
- allowed implementation scope;
- forbidden visual invention;
- commands/tests relevant to the milestone;
- exact completion/receipt requirements.

### contract.json

- handoffId;
- uiRevision;
- uiCommit;
- contractDigest when available;
- routes/sections in scope;
- interaction requirements;
- implementation constraints.

### components.json

Only components needed for current scope, using stable IDs and implementation-ready properties.

### assets.json

Only assets required by current scope, with production path and integrity/placement metadata needed by code.

### responsive.json

Only active breakpoints and composition changes used by current scope.

### lock.json

Exact identity/digest of the pack Claude consumed.

## Excluded by default

Do not copy these into Claude context by default:

- full `WORKFLOW_BASELINE_V1.md`;
- `KNOWLEDGE_PACK.md`;
- SVG reconstruction/design-generation instructions;
- client ideation history;
- rejected UI alternatives;
- long design rationale;
- unrelated routes/components/assets;
- closed QA history;
- project lessons that do not change implementation behavior.

## Compression principle

ChatGPT makes the visual decision. Webby converts it into deterministic implementation instructions. Claude consumes the compressed contract.

```text
Design knowledge != implementation input
```

Prefer this:

```json
{
  "componentId": "hero-main",
  "height": 760,
  "assetId": "hero-01",
  "objectPosition": "68% center",
  "headingMaxWidth": 620,
  "mobileLayout": "stack"
}
```

over prose explaining why the hero should feel premium.

## Missing fact rule

If Claude cannot implement without inventing a visual decision:

```text
STOP THAT SUBTASK
→ create blocking request
→ wait for resolved contract state
```

Claude may make normal engineering decisions that do not alter approved visual truth.
