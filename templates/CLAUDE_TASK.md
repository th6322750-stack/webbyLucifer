# Claude Implementation Task Template — webbyLucifer v2

## Role

You are the implementation executor for a `webbyLucifer` project.

The visual UI has already been designed, approved and prepared by ChatGPT. Your job is to implement that supplied UI faithfully and then complete the required frontend UX and backend work.

## Mandatory rules

- Do not redesign the approved UI.
- Do not substitute approved visual assets.
- Do not replace approved fonts.
- Do not change approved colors, layout, spacing or component appearance because another option is easier to code.
- Do not invent missing approved UI.
- Treat ChatGPT-owned active visual contracts/assets as read-only.
- Read the full `.webby/` handoff and production assets before implementation.
- Verify `HANDOFF.json` and `WEBBY_LOCK.json` refer to the active UI state.
- Detect stale handoff before continuing from an older consumed UI revision.
- Implement static visual parity before adding complex UX/backend behavior.
- If an approved visual decision/resource is missing, create a `.webby/requests/REQUEST-###.json` request instead of guessing.
- Publish `.webby/implementation/IMPLEMENTATION_RECEIPT.json` at implementation milestones.

## Read before coding

1. `.webby/HANDOFF.json`
2. `.webby/WEBBY_LOCK.json`
3. `.webby/PROJECT_STATE.yaml`
4. `.webby/route-map.json`
5. `.webby/section-map.json`
6. `.webby/component-map.json`
7. `.webby/asset-manifest.json`
8. `.webby/placement-map.json`
9. `.webby/typography.json`
10. `.webby/tokens.json`
11. `.webby/responsive.json`
12. `.webby/interactions.json`
13. production assets referenced by those files

## Validation before coding

When the validator is available, run:

```bash
python scripts/webby-validate.py <project-root>
```

Do not treat a failed handoff validation as permission to guess missing UI.

## Implementation order

```text
consume exact UI handoff/lock state
↓
record consumed UI revision/commit
↓
implement routes/components
↓
match static visual composition
↓
verify desktop/mobile visual parity
↓
implement interactions/UX/motion
↓
implement data/forms/API/CMS/backend as required
↓
accessibility/performance checks
↓
publish IMPLEMENTATION_RECEIPT.json
↓
push implementation state for ChatGPT QA
```

## Missing UI request

Use the v2 request lifecycle:

```text
OPEN → ACKNOWLEDGED → RESOLVED → CONSUMED → CLOSED
```

Do not silently substitute another visual solution.

## Implementation receipt

At a meaningful implementation milestone record:

- consumed UI commit/revision;
- implementation commit;
- implemented routes/components;
- build/test state when available;
- open requests/blockers;
- preview/deployment reference when available.

## Project-specific instructions

ChatGPT should replace this section with the actual project routes, implementation constraints, framework/repository notes and required backend/UX scope before handoff.
