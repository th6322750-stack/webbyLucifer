# UI_SETUP_COMPLETE Checklist — webbyLucifer v2

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
- [ ] Stable component IDs are assigned where useful.
- [ ] Desktop/mobile component differences are explicit.
- [ ] Claude does not need to invent a missing visual component.

## Production resources

- [ ] Logos/icons/ornaments/custom vectors are supplied.
- [ ] Production raster images are supplied.
- [ ] Source authority/reconstruction uncertainty is recorded.
- [ ] SVG assets pass canonicalization and visual QA.
- [ ] Fonts or explicit legal/acquisition manifests are supplied.
- [ ] Important asset integrity metadata is recorded when tooling permits.

## UI specifications

- [ ] Typography mapping is complete.
- [ ] Design tokens are defined.
- [ ] Route/section/component/asset/placement maps are complete.
- [ ] Responsive intent is complete.
- [ ] Important crop/overflow/layer/z-index behavior is documented.
- [ ] Visual interaction states are defined.
- [ ] Placement precision is sufficient that implementation does not require visual invention.

## V2 deterministic handoff

- [ ] `.webby/PROJECT_STATE.yaml` exists.
- [ ] `.webby/HANDOFF.json` exists and uses the active UI revision/commit.
- [ ] `.webby/WEBBY_LOCK.json` exists and matches HANDOFF.
- [ ] `.webby/CLAUDE_TASK.md` exists.
- [ ] Required inputs referenced by HANDOFF exist.
- [ ] Required files referenced by WEBBY_LOCK exist.
- [ ] Production assets referenced by manifests exist.
- [ ] Agent ownership boundaries are understood.
- [ ] No stale handoff is being consumed.
- [ ] No known HARD UI BLOCKER remains.
- [ ] No OPEN blocking request conflicts with completion.
- [ ] Validator passes when validator execution is available.

## Gate

Only when all applicable checks pass:

```text
UI_SETUP_COMPLETE = true
```

Then Claude may begin static frontend implementation from the exact locked UI state.
