# Agent Ownership Protocol — webbyLucifer v3.0

## Purpose

Prevent user, ChatGPT and Claude from silently owning the same decision layer.

```text
USER    = FINAL ACCEPTANCE AUTHORITY
CHATGPT = DESIGN / UI / ASSET / STATE / MOTION AUTHORITY
CLAUDE  = IMPLEMENTATION AUTHORITY
```

Ownership is about decision authority, not Git permissions.

---

## 1. User-owned decisions

The user owns final approval of the real website and any explicit product/business preference, including when applicable:

- whether the final interface is accepted;
- whether a major layout should be full-width, boxed or mixed when the reference does not decide it;
- business/content priority;
- whether a visual direction change is approved;
- whether a technical tradeoff that changes the approved experience is acceptable.

ChatGPT may recommend; it must not silently overwrite an explicit user decision.

---

## 2. ChatGPT-owned decisions

Claude read-only unless explicitly reassigned:

- approved visual direction and page composition;
- asset count/requirements;
- asset classification and identity mapping;
- master/delivery asset authority;
- Drive asset package and manifest;
- typography/color/spacing/geometry intent;
- full-width/boxed/mixed layout decision after user confirmation/evidence;
- responsive design intent;
- image crop/object-position/safe-area rules;
- visual states and placeholders;
- motion language;
- approved raster references;
- implementation contracts for visual scope;
- design/asset defect resolution.

Claude MUST NOT change these simply because another implementation is easier.

---

## 3. Claude-owned decisions

Within the approved contract, Claude owns implementation details that do not change the approved experience, for example:

- framework-native component/code structure;
- safe refactors needed to implement the contract;
- data wiring and backend architecture within agreed requirements;
- technical implementation of accessibility/semantics;
- targeted tests;
- implementation-only configuration;
- implementation receipts/commit history.

If a technical decision would visibly change the approved design, responsive behavior, content state or motion, it is no longer implementation-only.

---

## 4. Claude forbidden authority

Claude must not independently:

```text
redesign approved UI
choose a different full-width/boxed strategy
search the web for replacement assets
generate missing images
substitute a “similar” asset
map identity-bearing images by array index
invent a brand icon or redraw one for convenience
invent loading/empty/missing states when not specified
invent premium motion/animation
measure raster screenshots to derive geometry
rewrite the visual contract to match easier code
silently broaden a small UI task into a repo-wide redesign/audit
```

---

## 5. Missing information signals

Use concise blocker categories:

```text
NEED_ASSET
= a required asset/file is missing from the authoritative pack

BLOCKED_SPEC
= the design/spec is missing, ambiguous or contradictory

TECHNICAL_CONSTRAINT
= the spec is clear, but current code/stack/assets/performance/runtime cannot satisfy it as written
```

Claude should continue unaffected work when safe, but must not invent a replacement for the blocked item.

---

## 6. Error ownership after user review

When the user rejects the real implementation, classify before editing:

```text
DESIGN ERROR
→ ChatGPT revises design/spec and obtains user approval as needed

ASSET ERROR
→ ChatGPT creates/fixes/productionizes the asset and updates Drive/manifest

IMPLEMENTATION ERROR
→ Claude fixes the code to the existing approved contract
```

This classification prevents every visual complaint from becoming another redesign/audit loop.

---

## 7. Conflict state

If both agents changed the same authoritative design/asset contract without explicit reassignment:

```text
OWNERSHIP_CONFLICT
```

Do not pick the newest file automatically. Return to the user-approved intent and the authoritative owner.
