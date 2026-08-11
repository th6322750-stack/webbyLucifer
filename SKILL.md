# webbyLucifer — `change_web` v2.1

> **Mission:** turn a client brief into approved full UI prepared by ChatGPT, publish implementation-ready approved visual truth plus only the contracts needed for invisible/ambiguous behavior through GitHub, let Claude implement without visual invention, then verify the real website against the approved visual truth.
>
> **Core architecture:** **ChatGPT = FULL UI AUTHORITY. Claude = IMPLEMENTATION AUTHORITY. GitHub = VERSIONED EXCHANGE LAYER / SHARED PROJECT STATE.**
>
> **v2.1 principle:** **VISUAL FIRST — CONTRACT SECOND. Images carry visible form; contracts carry behavior, state, responsive rules, data and ambiguity.**

## 0. Compatibility and load order

webbyLucifer v2.1 keeps the complete GĐ1→GĐ7 workflow from v1 and all machine-verifiable safeguards introduced in v2. The previous canonical design/workflow rules remain preserved unchanged in:

```text
references/WORKFLOW_BASELINE_V1.md
```

An agent using this skill MUST read this file first, then read the v1 baseline, then only the phase-specific references needed for the current task.

For GĐ3/GĐ4 visual transfer, also read:

```text
references/VISUAL_HANDOFF_PROTOCOL.md
```

For final visual verification, read:

```text
references/QA_PROTOCOL.md
```

Precedence when rules conflict:

```text
SKILL.md v2.1 hard rules
> phase-specific v2.1 protocol
> phase-specific v2 protocol
> WORKFLOW_BASELINE_V1.md
> examples/templates
```

The seven stages remain unchanged:

```text
GĐ1 — DESIGN / FULL-PAGE UI — ChatGPT
GĐ2 — FULL UI MASTER / DESIGN SYSTEM — ChatGPT
GĐ3 — FULL PRODUCTION UI SETUP / GITHUB HANDOFF — ChatGPT
GĐ4 — STATIC FRONTEND IMPLEMENTATION — Claude by default
GĐ5 — UX / FRONTEND ENHANCEMENT — selected implementation executor
GĐ6 — BACKEND / CMS / LOGIC — selected implementation executor
GĐ7 — QA / PRODUCTION — ChatGPT reviews; executor fixes
```

All design, source-first asset, Drive, Master, SVG, responsive, production packaging, request-loop and QA rules in the v1 baseline continue to apply unless this file explicitly strengthens them.

---

# 1. V2.1 operating principle

v2 made the handoff machine-verifiable. v2.1 keeps that infrastructure and optimizes how visible UI truth reaches the executor.

```text
RULES
+ APPROVED VISUAL TRUTH
+ MINIMAL CONTRACT
+ SCHEMAS
+ STATE
+ LOCK
+ OWNERSHIP
+ VALIDATION
+ RECEIPTS
+ QA CONTRACT
```

The highest-priority rule remains:

> **Claude must never be forced to guess an approved UI decision. ChatGPT must completely prepare the UI before implementation handoff.**

v2 machine-verification rule remains:

> **A declaration is not enough. Critical handoff facts must be machine-verifiable whenever the project environment allows it.**

v2.1 adds:

> **Do not spend tokens describing visible UI that an executor can reliably derive from an approved full-page render. Use contracts for information the render cannot safely communicate.**

Hard shorthand:

```text
IMAGE = VISIBLE FORM
CONTRACT = INVISIBLE / AMBIGUOUS BEHAVIOR
```

---

# 2. GitHub contract layers

Each project repository SHOULD contain:

```text
.webby/
├── PROJECT_STATE.yaml
├── HANDOFF.json
├── WEBBY_LOCK.json
├── CLAUDE_TASK.md
├── visual-contract.json
├── asset-manifest.json
├── component-map.json
├── placement-map.json
├── route-map.json
├── section-map.json
├── typography.json
├── tokens.json
├── responsive.json
├── interactions.json
├── visual-handoff/
│   ├── routes.json
│   └── approved route renders...
├── requests/
├── implementation/
│   └── IMPLEMENTATION_RECEIPT.json
└── qa/
    ├── defects.json
    └── qa-report.json
```

Not every optional contract must be verbose or present when the same information is already authoritative and unambiguous elsewhere. Required inputs are project-specific and declared by the active handoff.

Production resources remain separated from authoritative/source files exactly as defined by the baseline workflow.

## Machine contract

The canonical schemas live under:

```text
schemas/
```

When a schema exists for a project file, agents SHOULD conform to that schema and validators SHOULD reject structurally invalid handoffs.

`visual-handoff/routes.json`, when used, SHOULD conform to:

```text
schemas/visual-handoff.schema.json
```

---

# 3. Approved visual truth and authority

After user approval, ChatGPT SHOULD publish implementation-relevant full-page renders for required routes and required viewports.

Example:

```text
.webby/visual-handoff/
├── routes.json
├── home-desktop.png
├── home-mobile.png
├── product-desktop.png
└── product-mobile.png
```

These approved renders become the primary visual reference for visible layout and presentation.

Recommended authority order when applicable:

```text
1. approved original/source asset
2. approved full-page render
3. approved structured Master/design source
4. explicit visual/behavior contract
5. browser implementation
```

This ordering does not mean an image overrides an authoritative original logo/SVG/native asset. Source-first asset rules remain mandatory.

Hard rule:

```text
BROWSER != APPROVED VISUAL TRUTH
→ FIX BROWSER IMPLEMENTATION
```

Do not modify approved design merely because another implementation is easier.

---

# 4. Visual-First Handoff — GĐ3

Read `references/VISUAL_HANDOFF_PROTOCOL.md`.

GĐ3 SHOULD package:

```text
APPROVED RENDERS
+ ROUTE/VIEWPORT MAPPING
+ AUTHORITATIVE ASSETS
+ MINIMAL NON-VISIBLE CONTRACT
+ HANDOFF / LOCK / REVISION STATE
```

The contract SHOULD focus on things a static approved render cannot safely define, including:

- breakpoints and responsive transitions not represented by supplied renders;
- hover/focus/active behavior;
- animation/motion;
- navigation targets;
- loading/empty/error/authenticated/selected states;
- data/API/CMS binding;
- accessibility behavior;
- conditional visibility;
- functional constraints and `mustNot` rules;
- exact geometry only when material to fidelity.

Do not duplicate obvious visible layout into long prose merely to make the handoff look detailed.

Component maps and placement maps remain available when deterministic structure or geometry is materially useful. v2.1 reduces redundant description; it does not ban precision.

---

# 5. UI_SETUP_COMPLETE v2.1 hard gate

The baseline checklist and v2 checks still apply. v2.1 additionally requires, when approved renders are part of the active scope:

```text
[ ] HANDOFF.json identifies a deterministic UI revision/commit
[ ] WEBBY_LOCK.json exists
[ ] required handoff files referenced by HANDOFF exist
[ ] lock entries resolve to existing files
[ ] production assets referenced by manifests exist
[ ] required route/viewport approved renders exist
[ ] visual-handoff route mappings resolve to existing files
[ ] active renders belong to the current UI revision/commit when revision metadata is used
[ ] no stale approved render is referenced by the active handoff
[ ] non-visible behavior required for implementation is explicitly contracted
[ ] no unresolved HARD UI BLOCKER remains
[ ] no OPEN blocking request makes the handoff incomplete
[ ] agent ownership boundaries are declared
[ ] handoff is not stale
[ ] validation passes or an explicit validator-unavailable reason is recorded
```

Only then:

```text
UI_SETUP_COMPLETE = true
```

If validation is available and fails, `UI_SETUP_COMPLETE` MUST remain false.

If a required render is missing and implementation would require visual invention, the affected scope is not ready.

---

# 6. Deterministic UI revision and stale-handoff prevention

A handoff SHOULD identify:

```text
handoffId
uiRevision
uiCommit
parentUiCommit
createdAt
```

`WEBBY_LOCK.json` SHOULD identify the exact contract and approved visual state the executor is expected to consume.

Claude records the consumed UI commit/revision before implementation.

Before continuing implementation after pulling new repository state, compare:

```text
consumed UI revision/commit
vs
current active UI revision/commit
```

If the active UI package or its approved renders changed materially:

```text
STALE_HANDOFF
```

Claude MUST NOT silently continue against an obsolete visual package. Pull and consume the new handoff or create a request when migration is ambiguous.

---

# 7. Agent ownership / write boundaries

Read `references/AGENT_OWNERSHIP_PROTOCOL.md`.

Default model:

```text
CHATGPT OWNS VISUAL TRUTH
CLAUDE OWNS IMPLEMENTATION TRUTH
```

Typical ChatGPT-owned paths/content:

```text
.webby visual specs/maps
.webby visual-handoff approved renders/mappings
.webby HANDOFF/LOCK state
assets/source visual authority
assets/production visual resources
design/master outputs
.webby/qa visual acceptance/defects
```

Typical Claude-owned paths/content:

```text
src/**
app/**
components/**
server/backend implementation
implementation configuration
.webby/requests/**
.webby/implementation/**
```

Claude must treat ChatGPT-owned approved visual truth and contract files as read-only unless the user explicitly changes authority.

ChatGPT must not casually rewrite implementation code merely because it is performing visual QA; it should publish defects for the implementation executor.

---

# 8. Asset integrity

Every important production asset SHOULD have a stable asset ID and, when tooling permits, integrity metadata such as:

```text
sha256
mime
byteSize
width/height or SVG viewBox
source authority
reconstruction status
license/redistribution status when relevant
usedBy
```

If an approved production asset changes unexpectedly, validation SHOULD flag the change before implementation or QA consumes it.

The source-first and canonical-SVG rules from the baseline remain mandatory.

---

# 9. Precision without redundant tokens

Component maps SHOULD use stable IDs rather than relying only on human-readable names when a component contract is required.

Useful fields may include:

```text
componentId
implementationTarget when known
parentComponentId
slots/children
states
variants
dataContract when applicable
requiredAssets
interactionIds
responsive composition
mustNot
```

Placement maps SHOULD describe enough geometry for the executor to implement without visual invention when the render alone is insufficient or exact geometry is material.

Useful fields may include:

```text
placementId
assetId/componentId
containerId
referenceViewport
coordinateSpace
anchor/offset
width/maxWidth/minWidth
aspectRatio
objectFit/objectPosition/focalPoint
zIndex/layer relationship
breakpoint behavior
mustNot
```

Exact geometry is required only where material to approved visual fidelity. Do not manufacture meaningless precision and do not restate obvious render information simply to increase contract size.

---

# 10. Route-scoped context loading

Executors SHOULD load only the active implementation scope plus required shared dependencies.

For a `/product` route, prefer:

```text
product approved render(s)
+ product-specific assets
+ product responsive rules
+ product interactions/states
+ shared tokens/components actually used
```

Preferred context policy:

```text
ROUTE-SCOPED CONTEXT
COMPONENT-SCOPED CONTEXT
ON-DEMAND CONTRACT LOADING
```

Do not dump the entire `.webby/` package into model context by default.

Token efficiency MUST NOT be used as justification to skip a required authority source, state, asset or behavior contract.

---

# 11. GĐ4 Visual Reconstruction

Before implementing an approved route, Claude/executor SHOULD inspect the approved render(s) and reconstruct the visible system directly from visual truth:

```text
APPROVED RENDER
↓
VISUAL ANALYSIS
↓
SECTION / COMPONENT DETECTION
↓
LAYOUT RECONSTRUCTION
↓
ASSET MAPPING
↓
MINIMAL CONTRACT MERGE
↓
IMPLEMENTATION
```

Claude SHOULD derive visible evidence such as:

- section hierarchy;
- containers and grids;
- typography hierarchy;
- spacing relationships;
- cards and controls;
- imagery treatment;
- borders, radii and shadows;
- alignment and layering;
- visible differences between supplied desktop/mobile renders.

Hard rule:

```text
VISIBLE APPROVED UI MUST BE DERIVED FROM APPROVED VISUAL TRUTH WHEN AVAILABLE.
```

Claude MUST NOT say a visible decision is undefined merely because it is absent from text when it is clear in an approved render.

If a material UI decision is unclear in both render and contract, use the request lifecycle. Do not invent it.

---

# 12. Implementation targets

Visual reconstruction is implementation-target agnostic.

## MODE A — CODE

Default for coded projects:

```text
Approved Render
→ Visual Reconstruction
→ React / Next.js / Vue / HTML/CSS / selected stack
→ Website
```

## MODE B — ELEMENTOR

Only when the project explicitly targets WordPress + Elementor:

```text
Approved Render
→ Visual Reconstruction
→ Elementor-compatible JSON/template
→ WordPress import
→ Website
```

Elementor is an implementation target, not the default architecture. It does not bypass handoff, visual authority, source assets, revision locking, requests, receipts or QA.

---

# 13. Claude request lifecycle

The baseline request loop remains. v2 standardizes lifecycle where practical:

```text
OPEN
→ ACKNOWLEDGED
→ RESOLVED
→ CONSUMED
→ CLOSED
```

A resolved request SHOULD record the resolution commit/revision and affected files. Claude consumes the resolved UI state before closing the request.

Hard rule remains:

```text
MISSING APPROVED UI != CLAUDE DESIGNS IT
```

v2.1 clarification:

```text
VISIBLE IN APPROVED RENDER != MISSING UI
```

---

# 14. Implementation receipt

After an implementation milestone, Claude SHOULD publish:

```text
.webby/implementation/IMPLEMENTATION_RECEIPT.json
```

The receipt identifies at minimum:

```text
consumedUiCommit / consumedUiRevision
implementationCommit
implemented routes/components
build/test status when available
open requests/blockers
preview/deployment reference when available
```

This receipt is the executor-to-ChatGPT delivery contract. It does not replace Git history; it makes the consumed UI state and implementation scope explicit.

---

# 15. Visual QA contract

Read `references/QA_PROTOCOL.md`.

For routes with approved visual truth, the normal loop is:

```text
IMPLEMENTATION
↓
RUN REAL WEBSITE
↓
CAPTURE BROWSER SCREENSHOT AT MATCHING VIEWPORT
↓
CHATGPT COMPARES WITH APPROVED RENDER
↓
PUBLISH DEFECTS
↓
EXECUTOR FIXES
↓
RE-CAPTURE / RE-QA
```

Machine-readable QA defects SHOULD use stable defect IDs and identify:

```text
defectId
implementationCommit
route
viewport
section/componentId
severity
observed
expected
authoritative render/spec/evidence
status
acceptance criteria when useful
```

Claude fixes defects against those IDs. ChatGPT re-tests and closes defects only after acceptance.

Approved render = expected visual state.

Browser screenshot = implementation evidence.

Browser implementation remains lower visual authority than approved source assets, approved Master and approved renders/specs.

---

# 16. Validation

The canonical repository provides:

```text
scripts/webby-validate.py
```

The validator is intentionally dependency-light. It performs structural and cross-reference checks that can be run without external packages. JSON Schemas remain the canonical structural contracts for fuller schema-aware tooling.

Recommended project use:

```bash
python scripts/webby-validate.py /path/to/project
```

A validator cannot prove artistic quality or full pixel parity. It verifies the handoff contract; visual acceptance remains ChatGPT's responsibility.

---

# 17. Versioned evolution

Current protocol version:

```text
2.1.0
```

Generalized skill changes still require explicit user approval before being committed to the canonical repository.

Do not create random replacement repositories such as `webbyLucifer-v2`, `final`, or `new`. Version this same canonical repository.

---

# 18. Final v2.1 model

```text
CLIENT BRIEF
↓
GĐ1 DESIGN / FULL-PAGE UI
↓
GĐ2 MASTER / DESIGN SYSTEM
↓
USER APPROVAL
↓
APPROVED VISUAL TRUTH — WEB / MOBILE
↓
GĐ3 VISUAL-FIRST PRODUCTION HANDOFF
↓
APPROVED RENDERS + MINIMAL CONTRACT
↓
SCHEMAS + LOCK + VALIDATION + OWNERSHIP
↓
UI_SETUP_COMPLETE
↓
CLAUDE VERIFIES ACTIVE UI STATE
↓
GĐ4 VISUAL RECONSTRUCTION → CODE / ELEMENTOR TARGET
↓
IMPLEMENTATION RECEIPT
↓
RUN WEBSITE + MATCHING SCREENSHOT
↓
CHATGPT VISUAL COMPARISON
↓
DEFECT CONTRACT ↔ CLAUDE FIX ↔ RE-QA
↓
GĐ5 UX
↓
GĐ6 BACKEND/CMS/LOGIC
↓
GĐ7 FINAL QA / PRODUCTION
↓
PRODUCTION_READY
```

Central v2.1 rules:

> **Ảnh/approved render truyền tải phần giao diện nhìn thấy. Contract truyền tải hành vi, trạng thái, responsive, dữ liệu và những gì ảnh không thể hiện rõ.**

> **Không tiêu token để mô tả lại những gì executor có thể nhìn trực tiếp từ approved visual truth.**

> **Claude triển khai UI; Claude không thiết kế UI.**

> **Approved render là expected visual state; browser screenshot là implementation evidence.**

For all detailed GĐ1–GĐ7 visual and implementation rules not repeated here, `references/WORKFLOW_BASELINE_V1.md` remains incorporated into this skill by reference.
