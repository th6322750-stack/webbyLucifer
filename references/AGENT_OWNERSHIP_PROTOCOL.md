# Agent Ownership Protocol — webbyLucifer v3.1

## Purpose

Prevent user, ChatGPT and Claude from silently owning the same decision layer while separating **visual intent** from **technical mechanism**.

```text
USER    = FINAL ACCEPTANCE AUTHORITY
CHATGPT = DESIGN / UI / ASSET / STATE / MOTION-FEEL AUTHORITY
CLAUDE  = IMPLEMENTATION / TECHNICAL-MECHANISM AUTHORITY
```

Ownership is decision authority, not Git permission.

---

## 1. User-owned decisions

The user owns final approval of the real website and explicit product/business preferences, including major full-width/boxed/mixed choices when references do not decide them, business/content priority and approval of material experience tradeoffs.

---

## 2. ChatGPT-owned decisions

Claude read-only unless explicitly reassigned:

- approved visual direction/page composition;
- asset count/requirements;
- asset classification, ROLE, ITEM mapping and icon inventory;
- master/delivery asset authority;
- typography/color/spacing/semantic geometry intent;
- responsive visual intent;
- crop/object-position/safe-area rules;
- visual states/placeholders;
- **motion FEEL**: trigger, duration, easing, distance, stagger, order, never-animate and reduced-motion intent;
- approved raster references;
- implementation contracts for visual scope;
- design/asset defect resolution.

Claude MUST NOT change these simply because another implementation is easier.

---

## 3. Claude-owned decisions

Within the approved observable experience, Claude owns technical implementation details such as:

- framework-native component/code structure;
- safe refactors required to implement the contract;
- data/backend wiring within agreed requirements;
- accessibility/semantics implementation;
- targeted tests;
- implementation configuration;
- **motion MECHANISM**: CSS vs JS, observer/scroll strategy, requestAnimationFrame/interpolation, listeners, cleanup and technical fallbacks.

Claude may change motion mechanism without asking only when visual feel and observable behavior remain unchanged and no material new global behavior surface is introduced.

A material global behavior surface includes site-wide wheel/touch/key interception, preventing/replacing browser default scroll across routes, app-wide event capture, cross-route focus/navigation behavior or a global scroll/provider engine. This must be reported before broad application even if it adds zero npm dependencies.

---

## 4. Claude forbidden authority

Claude must not independently:

```text
redesign approved UI
choose another full-width/boxed strategy
search/generate/substitute assets
map identity-bearing images by array index
fake a missing approved icon with CSS/Unicode/another library asset
invent visual states
invent motion FEEL
measure raster screenshots to derive geometry
rewrite visual contract to match easier code
silently broaden a small task into repo-wide redesign/audit
```

---

## 5. Missing information signals

```text
NEED_ASSET
BLOCKED_SPEC
TECHNICAL_CONSTRAINT
```

Continue unaffected work when safe; never invent a replacement.

---

## 6. Critical Finding exception

Anti-scope-creep does not permit silence about credible serious data-loss/security findings.

```text
CURRENT ACTION causing/about to cause harm
→ stop only that harmful action + report CRITICAL_FINDING immediately

EXISTING unrelated critical bug discovered
→ report immediately + continue current task when safe/independent
```

A Critical Finding never grants permission for a broad unauthorized audit/refactor.

---

## 7. Error ownership after user review

```text
DESIGN ERROR         → ChatGPT revises design/spec
ASSET ERROR          → ChatGPT fixes/creates asset package
IMPLEMENTATION ERROR → Claude fixes code to existing contract
```

---

## 8. Conflict state

If both agents changed the same authoritative design/asset contract without explicit reassignment:

```text
OWNERSHIP_CONFLICT
```

Return to user-approved intent and the authoritative owner rather than choosing the newest file automatically.
