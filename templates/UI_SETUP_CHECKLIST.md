# IMPLEMENTATION_READY_UI Checklist — webbyLucifer v3.0

Legacy name: `UI_SETUP_COMPLETE`. For v3, the canonical readiness state is `IMPLEMENTATION_READY_UI`.

If any applicable required item is not satisfied, Claude MUST NOT begin ordinary UI implementation.

## User approval

- [ ] The user has reviewed and approved the visible direction (`VISUAL_DIRECTION_APPROVED`).
- [ ] Any material user choice not safely inferable from the reference is locked, including full-width/boxed/mixed behavior where relevant.

## Intake / environment

- [ ] `PROJECT_INTAKE.json` is complete enough for the active scope.
- [ ] Authoritative GitHub repo/branch is known when an existing repo is used.
- [ ] Remote/local drift risk is known when Claude has local unpushed changes.
- [ ] Google Drive asset delivery is available and Claude access/download has been verified.
- [ ] Vercel/preview need is known; lack of Vercel is not a blocker unless deployment behavior is required.

## Asset count plan

- [ ] The UI was decomposed route-by-route/section-by-section.
- [ ] `ASSET_COUNT_PLAN.json` exists when the scope needs asset production.
- [ ] Total asset count was reported to the user before production.
- [ ] Assets that must come from the user/client are identified.
- [ ] Assets that ChatGPT must create/prepare are identified.

## High-resolution source quality

- [ ] Production-authoritative raster masters meet the approved FHD-class minimum.
- [ ] 4K-class masters are used where required/preferred, especially hero/full-bleed imagery.
- [ ] Low-resolution images were not merely enlarged and misrepresented as true high-resolution masters.
- [ ] Low-resolution patchwork was not used to fake source quality.
- [ ] Brand/logo/icon assets use authoritative/vector sources where appropriate.

## Asset completeness and identity

- [ ] Every visible production asset in the approved final reference exists in the frozen pack, or the reference intentionally shows a declared placeholder/data state.
- [ ] `asset-manifest.json` exists.
- [ ] Every identity-bearing asset maps to the correct `ITEM`.
- [ ] `AUTHENTIC` and `DATA_VISUAL` assets have the correct owner/item/data association.
- [ ] `DEMO` assets cannot silently appear as authentic live data.
- [ ] `ALLOWED_USAGE` is declared where misuse would be harmful.
- [ ] Claude does not need to pick/search/generate/substitute a missing visual resource.

## Master vs web delivery

- [ ] Master source and web delivery asset are distinguished where applicable.
- [ ] Required web delivery files exist.
- [ ] Delivery dimensions/formats/weight constraints are recorded where material.
- [ ] Destination paths for implementation are known.
- [ ] Heavy masters are stored in the approved Drive project folder rather than dumped into Git by default.

## Responsive image treatment

- [ ] Usage-specific aspect ratios are declared.
- [ ] `object-position` is declared per usage/breakpoint where needed.
- [ ] Safe areas are declared for subject-sensitive crops where needed.
- [ ] Separate mobile delivery files exist where one master cannot survive the required crop.

## Deterministic UI geometry

- [ ] The final UI composition was generated from declared values rather than being reverse-engineered from a raster.
- [ ] Container/full-width rules are locked.
- [ ] Column counts/gaps/section paddings are locked where material.
- [ ] Aspect ratios use semantic values unless an intentional exception is documented.
- [ ] Typography size/weight/line-height hierarchy is locked.
- [ ] Claude will not need to measure the raster to obtain implementation numbers.

## Responsive layout

- [ ] Real project breakpoints/constraints are known.
- [ ] Critical breakpoint boundaries are covered by spec/reference where needed.
- [ ] Wide/full-bleed behavior is defined when relevant.

## Content and states

- [ ] Real/representative content is used where wrapping matters.
- [ ] Content envelopes such as max lines/clamp/no-wrap are defined where data may vary.
- [ ] Required layout-changing states are defined: missing image/partial/empty/few items/loading/etc. as applicable.
- [ ] Claude does not need to invent a runtime state.

## Motion / interaction

- [ ] Motion is specified or explicitly `N/A`.
- [ ] If motion exists, trigger/duration/easing/distance/stagger/orchestration/never-animate/reduced-motion are defined only to the level needed.
- [ ] Required interactions are specified.

## Handoff state

- [ ] `HANDOFF.json` status is `IMPLEMENTATION_READY_UI`.
- [ ] `WEBBY_LOCK.json` matches the active UI revision/commit when used.
- [ ] The short `CLAUDE_TASK.md` exists for the active task/scope.
- [ ] No unresolved `NEED_ASSET`, `BLOCKED_SPEC` or blocking request remains for the active scope.
- [ ] Validator passes when validator execution is available, or the reason it cannot run is recorded.

## Gate

Only when all applicable checks pass:

```text
IMPLEMENTATION_READY_UI = true
```

Then Claude may implement from the exact locked package without redesigning, searching for assets or measuring raster pixels.
