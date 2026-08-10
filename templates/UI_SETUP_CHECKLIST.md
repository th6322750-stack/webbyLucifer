# UI_SETUP_COMPLETE Checklist

Use this checklist before handing implementation to Claude.

If an applicable required item is not satisfied, `UI_SETUP_COMPLETE` remains `false`.

## Approved visual scope

- [ ] Route list is complete.
- [ ] Required WEB full-page designs exist and are approved.
- [ ] Required MOBILE full-page designs exist and are approved.
- [ ] Admin/CMS visual routes exist when required.
- [ ] Structured Master matches the approved designs.

## Component system

- [ ] All reusable visual components are defined.
- [ ] Applicable component states are defined.
- [ ] Desktop/mobile component differences are explicit.
- [ ] Claude does not need to invent a missing visual component.

## Production resources

- [ ] Logos are supplied.
- [ ] Icons are supplied.
- [ ] Ornaments/custom vectors are supplied.
- [ ] Production raster images are supplied.
- [ ] Source authority/reconstruction uncertainty is recorded.
- [ ] SVG assets pass canonicalization and visual QA.
- [ ] Fonts or explicit legal/acquisition manifests are supplied.

## UI specifications

- [ ] Typography mapping is complete.
- [ ] Design tokens are defined.
- [ ] Route map is complete.
- [ ] Section map is complete.
- [ ] Component map is complete.
- [ ] Asset manifest is complete.
- [ ] Placement map is complete.
- [ ] Responsive intent is complete.
- [ ] Important crop/overflow/layer/z-index behavior is documented.
- [ ] Visual interaction states are defined.

## GitHub handoff

- [ ] `.webby/PROJECT_STATE.yaml` exists.
- [ ] `.webby/HANDOFF.json` exists.
- [ ] `.webby/CLAUDE_TASK.md` exists.
- [ ] Required maps/specs referenced by HANDOFF exist.
- [ ] Production assets are committed to the project repository.
- [ ] Handoff/UI commit is deterministic and verified.
- [ ] No known HARD UI BLOCKER remains.

## Gate

Only when all applicable checks pass:

```text
UI_SETUP_COMPLETE = true
```

Then Claude may begin:

```text
STATIC FRONTEND IMPLEMENTATION
→ UX / INTERACTIONS / MOTION
→ BACKEND / CMS / LOGIC
```

Claude remains implementation authority, not visual-design authority.
