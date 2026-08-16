# IMPLEMENTATION_READY_UI Checklist — webbyLucifer v3.1

This checklist is **task-mode aware**. Do not apply the full NEW_REDESIGN gate to a five-line existing polish or a targeted bug fix.

## 0. Task Router

- [ ] `TASK_MODE` is classified as `NEW_REDESIGN`, `EXISTING_POLISH`, or `BUG_FIX`.
- [ ] If classification materially changes cost/scope and is ambiguous, the user was asked once.

---

# A. NEW_REDESIGN — full pipeline readiness

If any applicable item below fails, Claude MUST NOT begin full-pipeline UI implementation.

## User approval

- [ ] User approved visible direction (`VISUAL_DIRECTION_APPROVED`).
- [ ] Material choices such as full-width/boxed/mixed are locked.

## Intake / environment

- [ ] `PROJECT_INTAKE.json` is complete for active scope.
- [ ] Repo/branch is known when used.
- [ ] Remote/local drift risk is known.
- [ ] Current `workSessionId` is recorded.
- [ ] Vercel/preview need is known; Vercel is not mandatory unless deployment behavior is required.

## Asset count plan

- [ ] UI was decomposed route/section by route/section.
- [ ] `ASSET_COUNT_PLAN.json` exists.
- [ ] Total asset count was reported before production.
- [ ] User-required vs ChatGPT-created/prepared assets are identified.

## High-resolution quality

- [ ] Production-authoritative raster masters meet FHD-class minimum.
- [ ] 4K-class is used where required/preferred, especially hero/full-bleed.
- [ ] Low-res enlargement is not misrepresented as authoritative high-res.
- [ ] Low-res patchwork is not used to fake quality.
- [ ] Brand/logo/icon uses authoritative/vector source where appropriate.

## Asset completeness / identity

- [ ] Every visible production asset exists in the frozen pack or is an intentional declared placeholder/data state.
- [ ] `asset-manifest.json` exists.
- [ ] Identity-bearing assets map to correct `ITEM`.
- [ ] `AUTHENTIC` / `DATA_VISUAL` owner/data mapping is correct.
- [ ] `DEMO` cannot silently appear as authentic live data.
- [ ] `ALLOWED_USAGE` exists where misuse matters.
- [ ] Claude does not need to pick/search/generate/substitute a missing asset.

## Icon inventory

- [ ] Every visible required icon appears in `iconInventory`.
- [ ] Every required inventory icon has an actual asset entry with `role = ICON`.
- [ ] No approved icon requires Claude to fake it with CSS/Unicode/another library.

## Asset transport — session scoped

- [ ] Transport mode is `DRIVE`, `GIT`, or `HYBRID`.
- [ ] If `DRIVE` or `HYBRID`, Claude successfully downloaded a real file in the **current work session**.
- [ ] `verifiedForSessionId` matches the current `workSessionId`.
- [ ] `sessionVerifiedAt` is recorded.
- [ ] If current Drive session failed/expired, readiness was reset instead of reusing an old true flag.

## Master vs delivery / runtime

- [ ] Master source and web delivery are distinguished.
- [ ] Required web delivery files exist.
- [ ] Destination paths/runtime sources are known.
- [ ] Drive is treated as storage/delivery, not default live runtime origin.
- [ ] Heavy masters are not dumped into Git by default merely to bypass Drive.

## Responsive images

- [ ] Usage-specific aspect ratios are declared.
- [ ] `object-position` is declared where needed.
- [ ] Safe area is declared where needed.
- [ ] Separate mobile delivery exists where one crop cannot survive.

## Deterministic geometry

- [ ] Final composition is generated from declared values, not reverse-engineered raster measurements.
- [ ] Container/full-width rules are locked.
- [ ] Columns/gaps/paddings are locked where material.
- [ ] Aspect ratios are semantic unless intentional exception is documented.
- [ ] Typography hierarchy is locked.
- [ ] Claude does not need to measure raster.

## Responsive / content / state

- [ ] Real project breakpoints/constraints are known.
- [ ] Critical boundary behavior is covered where needed.
- [ ] Real/representative content is used where wrapping matters.
- [ ] Content envelopes are defined where data varies.
- [ ] Required layout-changing states are defined.

## Motion

- [ ] Motion FEEL is specified or N/A.
- [ ] FEEL covers only necessary trigger/duration/easing/distance/stagger/order/reduced-motion rules.
- [ ] Motion MECHANISM remains Claude's implementation choice.
- [ ] Any mechanism requiring a material new global behavior surface has been reported before broad application.

## Handoff

- [ ] `HANDOFF.json` taskMode = `NEW_REDESIGN`.
- [ ] status = `IMPLEMENTATION_READY_UI`.
- [ ] `WEBBY_LOCK.json` matches active UI state when used.
- [ ] Short `CLAUDE_TASK.md` exists.
- [ ] No blocking `NEED_ASSET` / `BLOCKED_SPEC` remains.
- [ ] Validator passes when available, or unavailable reason is recorded.

---

# B. EXISTING_POLISH — fast path readiness

Do **not** require Asset Count/4K/Drive full-pipeline gates when no new asset pipeline is involved.

- [ ] Existing approved/current baseline is sufficiently known.
- [ ] Exact target is scoped.
- [ ] Local/shared impact is known.
- [ ] New asset is either not required or already prepared/mapped.
- [ ] If a new Drive asset is used, current-session Drive proof is valid.
- [ ] Motion FEEL, if changed, is specified by ChatGPT.
- [ ] Material global motion/scroll mechanism expansion is either absent or reported.
- [ ] No blocking spec gap remains.
- [ ] Short task contract is ready.

Screenshot is optional; use only if current visual/runtime evidence is actually needed.

---

# C. BUG_FIX — targeted readiness

- [ ] Bug/defect is named or reproducible enough to target.
- [ ] Affected scope is known enough to begin.
- [ ] No redesign is required unless explicitly reclassified.
- [ ] Required asset/spec for the fix is available or the appropriate blocker is reported.
- [ ] Targeted test strategy is clear enough for the defect risk.

---

# D. CRITICAL_FINDING exception

At all task modes:

```text
current action is dangerous → stop only that harmful action + report
existing unrelated critical bug → report immediately + continue safe independent task
```

A Critical Finding never grants permission for a broad unauthorized audit/refactor.
