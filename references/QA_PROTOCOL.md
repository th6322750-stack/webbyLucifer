# QA / Acceptance Protocol — webbyLucifer v3.0

## Purpose

QA must verify implementation/functionality without becoming another design loop.

Authority:

```text
USER    = final visual acceptance
CHATGPT = design/asset/spec authority and defect classification support
CLAUDE  = implementation fixes
```

---

## 1. Asset QA happens before implementation handoff

ChatGPT must verify applicable asset quality before `IMPLEMENTATION_READY_UI`:

- source/master is genuinely high resolution or vector;
- no low-resolution patchwork presented as a high-resolution authority;
- asset identity/usage is correct;
- crop/safe-area behavior is defined where material;
- master and delivery files are distinguished;
- Drive files are accessible;
- asset manifest matches the frozen pack;
- AUTHENTIC/DATA_VISUAL content is not fabricated;
- DEMO/DECORATIVE content is not silently presented as authentic live data.

Do not push unresolved asset selection onto Claude.

---

## 2. Claude technical checks are proportional to the task

Do not run every possible check for every tiny UI change.

Examples:

```text
static text/color/spacing/asset insertion
→ typecheck/lint/build only as relevant

new responsive layout
→ technical checks + one quick browser smoke check when useful

complex interaction (drawer/modal/scroll lock/carousel/autoplay)
→ targeted interaction test

backend/data/security change
→ targeted tests appropriate to that scope
```

A full test suite is not mandatory for a trivial visual-only change unless project policy/CI requires it.

---

## 3. Screenshot policy

Screenshot comparison is NOT the default implementation workflow.

Use browser screenshots when they provide real value:

- the user explicitly wants a preview/evidence image;
- diagnosing a visual/runtime bug;
- checking a new responsive layout boundary;
- an explicit QA phase requires stored evidence.

Do not create automatic multi-viewport screenshot matrices after every task merely to let Claude self-review the UI.

The user is the final visual acceptance authority.

---

## 4. User acceptance of the real website

After implementation, the user reviews the available real environment: local browser, preview deployment or production as appropriate.

Applicable review dimensions:

```text
page hierarchy
full-width / boxed behavior
container/gutters
assets and identity mapping
image crop
font and wrapping
spacing
responsive behavior
motion
interactions
```

If rejected, classify first:

```text
DESIGN ERROR
ASSET ERROR
IMPLEMENTATION ERROR
```

Then route the fix to the correct owner.

---

## 5. Functional QA comes after visual acceptance by default

Functional QA checks behavior, not whether the design should be reinvented.

Examples:

### Customer side

- navigation/routes;
- search/filter/sort;
- tabs/gallery;
- forms/contact flows;
- loading/error behavior;
- responsive interactions.

### Admin/CMS side

- login/authentication;
- create/read/update/delete operations;
- draft/publish;
- uploads;
- validation;
- data persistence/integration.

If the user explicitly asks for earlier functional testing, it may happen earlier, but it still must not silently redesign approved UI.

---

## 6. Defect lifecycle

Use stable bug/defect IDs for actionable issues.

Recommended:

```text
OPEN → FIXED_PENDING_REVIEW → CLOSED
          ↘ REOPENED ↗
```

Each defect should contain only what is useful:

- `defectId`;
- route/component;
- observed result;
- expected contract/behavior;
- owner type: DESIGN / ASSET / IMPLEMENTATION / FUNCTIONAL;
- acceptance criterion when needed.

Claude fixes the named implementation/functional defect. Do not use bug fixing as permission for a new repo-wide audit or redesign.

---

## 7. No self-approval

Claude cannot close a visual concern merely because code changed.

Final visible acceptance belongs to the user. ChatGPT may help classify/evaluate against the approved design, but must not pretend the user has accepted a result they have not reviewed.

---

## 8. Smoke check definition

A **smoke check** is a quick check that the route starts and no obvious runtime/layout failure is present. It is not a pixel-perfect review.

Its purpose is to catch failures such as:

- route crashes;
- completely missing section;
- broken responsive branch;
- unusable interaction;
- major overflow/hide bug.

Keep it short.
