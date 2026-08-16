# QA / Acceptance Protocol — webbyLucifer v3.1

## Purpose

QA verifies implementation/functionality without becoming another design loop or forcing full-pipeline work onto tiny fixes.

Authority:

```text
USER    = final visual acceptance
CHATGPT = design/asset/spec + motion-FEEL authority
CLAUDE  = implementation/technical-MECHANISM fixes
```

---

## 1. Task-mode aware QA

```text
NEW_REDESIGN     → full asset/readiness QA where applicable
EXISTING_POLISH  → proportional checks only
BUG_FIX          → targeted reproduction/test only
```

Do not replay asset count/4K/Drive gates for a small polish or bug fix unless that task actually introduces new assets requiring them.

---

## 2. Asset QA before full-pipeline handoff

For `NEW_REDESIGN`, ChatGPT verifies applicable:

- source/master is genuinely high resolution or vector;
- no low-resolution patchwork/fake authority;
- asset identity/usage is correct;
- icon inventory is complete for visible required icons;
- crop/safe-area behavior is defined where material;
- master and delivery files are distinguished;
- Drive/Git/HYBRID transport is declared;
- Drive proof matches the current work session when Drive/HYBRID is used;
- runtime `destinationPath`/source is declared rather than assuming Drive is the live image origin;
- AUTHENTIC/DATA_VISUAL is not fabricated;
- DEMO/DECORATIVE is not silently authentic live data.

Do not push unresolved asset selection onto Claude.

---

## 3. Claude checks are proportional

```text
small static polish
→ typecheck/lint/build only as relevant

new responsive layout
→ technical checks + quick browser smoke check when useful

complex interaction/motion mechanism
→ targeted runtime test

backend/data/security
→ targeted tests appropriate to scope
```

A full test suite is not mandatory for a trivial visual-only change unless CI/project policy requires it.

---

## 4. Screenshot policy

Screenshot comparison is NOT the default implementation workflow.

Use screenshots only when they add evidence:

- user explicitly wants preview/evidence;
- diagnosing a visual/runtime bug;
- checking a new responsive boundary;
- explicit QA requires stored evidence.

Existing polish does not require a new screenshot when the user-provided screenshot/link/description is already sufficient.

The user is final visual acceptance authority.

---

## 5. Motion QA — FEEL vs MECHANISM

Evaluate motion in two layers:

```text
FEEL
→ does the visible/observable experience match approved trigger/duration/easing/order/etc.?

MECHANISM
→ is the technical implementation safe and robust?
```

A mechanism that introduces a site-wide behavior surface (global wheel/touch/key interception, browser-scroll replacement, app-wide event capture, global scroll engine/provider) requires targeted runtime testing and must have been reported before broad application.

---

## 6. User acceptance

After implementation, the user reviews the available real environment: local browser, preview or production as appropriate.

If rejected, classify first:

```text
DESIGN ERROR
ASSET ERROR
IMPLEMENTATION ERROR
```

Then route the fix to the correct owner.

---

## 7. Functional QA

Functional QA checks behavior, not whether the design should be reinvented.

Examples:

```text
customer: navigation/search/filter/tabs/gallery/forms/loading/error
admin: login/auth/CRUD/draft-publish/upload/validation/persistence
```

Use stable bug IDs for actionable defects. Claude fixes the named defect and must not use bug fixing as permission for a broad redesign/audit.

---

## 8. Critical Finding escalation

During any QA/task:

```text
CURRENT ACTION is causing/about to cause serious harm
→ stop only that harmful action
→ report CRITICAL_FINDING immediately

EXISTING unrelated critical bug discovered
→ report immediately
→ continue the current task if safe and independent
```

Critical examples include credible silent data loss/overwrite, auth bypass, secret exposure, severe authorization failure, unintended destructive behavior and serious security vulnerabilities.

A Critical Finding does not authorize a broad unrequested audit/refactor.

---

## 9. Smoke check definition

A **smoke check** is a quick route/runtime sanity check, not a pixel-perfect review. Its purpose is to catch crashes, completely missing sections, broken responsive branches, unusable interactions or major overflow/hide bugs.
