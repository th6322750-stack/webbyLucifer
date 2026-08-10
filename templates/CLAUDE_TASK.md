# Claude Implementation Task Template

## Role

You are the implementation executor for a `webbyLucifer` project.

The visual UI has already been designed, approved and prepared by ChatGPT.

Your job is to implement that supplied UI faithfully and then complete the required frontend UX and backend work.

## Mandatory rules

- Do not redesign the approved UI.
- Do not substitute approved visual assets.
- Do not replace approved fonts.
- Do not change approved colors, layout, spacing or component appearance because another option is easier to code.
- Do not invent missing approved UI.
- Read the full `.webby/` handoff and production assets before implementation.
- Implement static visual parity before adding complex UX/backend behavior.
- If an approved visual decision/resource is missing, create a `.webby/requests/REQUEST-###.json` request instead of guessing.

## Read before coding

1. `.webby/HANDOFF.json`
2. `.webby/PROJECT_STATE.yaml`
3. `.webby/route-map.json`
4. `.webby/section-map.json`
5. `.webby/component-map.json`
6. `.webby/asset-manifest.json`
7. `.webby/placement-map.json`
8. `.webby/typography.json`
9. `.webby/tokens.json`
10. `.webby/responsive.json`
11. `.webby/interactions.json`
12. production assets referenced by those files

## Implementation order

```text
consume exact UI handoff state
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
push implementation state for ChatGPT QA
```

## Missing UI request

When required approved UI information is absent, create a request containing:

```json
{
  "type": "UI_OR_ASSET_REQUEST",
  "requestedBy": "CLAUDE",
  "route": "<route>",
  "section": "<section/component>",
  "missing": "<missing approved resource/decision>",
  "reason": "<why implementation cannot be faithful without it>"
}
```

Do not silently substitute another visual solution.

## Project-specific instructions

ChatGPT should replace this section with the actual project routes, implementation constraints, framework/repository notes and required backend/UX scope before handoff.
