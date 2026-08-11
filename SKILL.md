# webbyLucifer — `change_web` v2.2

> **Mission:** turn incomplete client/user input into a complete personalized brief, then let ChatGPT own the approved visual truth, publish a visual-first implementation handoff through GitHub, let Claude implement without visual invention, and verify the real website against the approved design.
>
> **Core architecture:** **ChatGPT = FULL UI AUTHORITY. Claude = IMPLEMENTATION AUTHORITY. GitHub = VERSIONED EXCHANGE LAYER / SHARED PROJECT STATE.**
>
> **v2.2 operating principles:** **DISCOVER BEFORE DESIGN. VISUAL FIRST — CONTRACT SECOND.**

---

# 0. Compatibility and load order

webbyLucifer v2.2 preserves all GĐ1→GĐ7 responsibilities from the v1 baseline and all v2/v2.1 machine-verifiable handoff safeguards. v2.2 adds one mandatory phase before design:

```text
GĐ0 — INTAKE / DISCOVERY / PERSONALIZATION — ChatGPT
```

Canonical detailed rules:

```text
references/WORKFLOW_BASELINE_V1.md
references/INTAKE_DISCOVERY_PROTOCOL.md
references/VISUAL_HANDOFF_PROTOCOL.md
references/GITHUB_HANDOFF_PROTOCOL.md
references/AGENT_OWNERSHIP_PROTOCOL.md
references/QA_PROTOCOL.md
```

Load only the references needed for the active phase.

Required load behavior:

```text
START / NEW PROJECT
→ SKILL.md
→ INTAKE_DISCOVERY_PROTOCOL.md
→ only then GĐ1-specific rules

GĐ3 / GĐ4
→ VISUAL_HANDOFF_PROTOCOL.md
→ relevant GitHub/ownership rules

GĐ7
→ QA_PROTOCOL.md
```

Precedence:

```text
SKILL.md v2.2 hard rules
> phase-specific v2.2 protocol
> phase-specific v2.1/v2 protocol
> WORKFLOW_BASELINE_V1.md
> examples/templates
```

When the baseline refers to `GĐ1.P PROJECT INTAKE / EVIDENCE LOCK`, v2.2 interprets that work as GĐ0. Do not perform the same intake twice.

---

# 1. Canonical workflow

```text
GĐ0 — INTAKE / DISCOVERY / PERSONALIZATION      ChatGPT
GĐ1 — DESIGN / FULL-PAGE UI                     ChatGPT
GĐ2 — FULL UI MASTER / DESIGN SYSTEM            ChatGPT
GĐ3 — VISUAL-FIRST PRODUCTION UI HANDOFF        ChatGPT
GĐ4 — STATIC FRONTEND / VISUAL RECONSTRUCTION   Claude by default
GĐ5 — UX / FRONTEND ENHANCEMENT                 selected executor
GĐ6 — BACKEND / CMS / LOGIC                     selected executor
GĐ7 — QA / PRODUCTION                           ChatGPT reviews; executor fixes
```

Hard flow:

```text
USER INPUT
↓
GĐ0 DISCOVERY LOOP
↓
INTAKE_COMPLETE
↓
GĐ1 DESIGN
↓
GĐ2 MASTER / DESIGN SYSTEM
↓
USER APPROVAL
↓
APPROVED VISUAL TRUTH
↓
GĐ3 VISUAL-FIRST HANDOFF
↓
UI_SETUP_COMPLETE
↓
GĐ4 IMPLEMENTATION
↓
GĐ5 UX
↓
GĐ6 BACKEND/CMS/LOGIC
↓
GĐ7 VISUAL QA / PRODUCTION
↓
PRODUCTION_READY
```

---

# 2. GĐ0 — mandatory intake/discovery gate

Read `references/INTAKE_DISCOVERY_PROTOCOL.md`.

Before asking questions, ChatGPT MUST inspect all currently available project evidence: user messages, URLs, screenshots, files, logos, references, existing site/repo context, content, assets, audience clues, required features and technical constraints.

Hard rule:

> **Never ask the user to repeat information that is already sufficiently known from supplied context.**

GĐ0 is an adaptive discovery loop, not a fixed questionnaire:

```text
INSPECT EXISTING INPUT
↓
NORMALIZE KNOWN FACTS
↓
IDENTIFY MATERIAL GAPS
↓
ASK TARGETED HIGH-VALUE QUESTIONS
↓
MERGE ANSWERS
↓
RE-EVALUATE GAPS
↓
REPEAT ONLY IF NEEDED
↓
INTAKE_COMPLETE
```

When the project repository is available, normalize GĐ0 state into:

```text
.webby/PROJECT_INTAKE.json
```

which SHOULD conform to:

```text
schemas/project-intake.schema.json
```

Important information is classified as:

```text
KNOWN
ASSUMED
SOFT_GAP
HARD_GAP
NOT_APPLICABLE
```

GĐ0 must collect enough evidence to answer, when applicable:

```text
WHAT are we designing?
WHO is it for?
WHY should that audience care?
WHAT should visitors/users do next?
WHAT makes this project distinct?
WHAT content/assets/references are authoritative?
WHAT pages/features are in scope?
WHAT constraints must the design respect?
```

The purpose is personalized completeness, not maximum questioning.

Do not ask low-value questions that do not materially affect design or implementation.

Do not block on a `SOFT_GAP` that can be handled safely later.

Do not silently invent a `HARD_GAP` answer.

---

# 3. INTAKE_COMPLETE hard gate

Set:

```text
INTAKE_COMPLETE = true
```

only when:

```text
[ ] all available project inputs were inspected
[ ] known answers were reused instead of re-asked
[ ] project/business/offer is sufficiently understood
[ ] target audience is known or an explicit safe assumption exists
[ ] primary goal / conversion goal is known
[ ] scope/routes/features are known enough to begin design
[ ] brand/assets/reference status is understood
[ ] important must-have / must-not-have constraints are captured
[ ] enough personalization signals exist to avoid generic design
[ ] assumptions and SOFT_GAP items are recorded
[ ] no unresolved HARD_GAP remains
```

If any unresolved `HARD_GAP` can materially change design direction, personalization, conversion logic or scope:

```text
INTAKE_COMPLETE = false
GĐ1 MUST NOT START
```

When complete, ChatGPT SHOULD summarize the normalized brief concisely and transition into GĐ1 without restarting discovery.

If materially new user information arrives later, update intake state and any affected downstream revision instead of ignoring the change.

---

# 4. GĐ1 / GĐ2 — ChatGPT owns design truth

All existing full UI, design research, source-first asset, WEB/MOBILE, Master/design system, SVG, responsive and approval rules in `references/WORKFLOW_BASELINE_V1.md` remain active.

Highest-priority ownership rule:

```text
CHATGPT OWNS VISUAL TRUTH
CLAUDE OWNS IMPLEMENTATION TRUTH
```

Claude MUST NOT independently:

- invent missing UI;
- choose replacement visual identity;
- replace approved fonts/icons/assets for convenience;
- change approved colors, spacing, typography, imagery or layout;
- reinterpret desktop/mobile composition without authority;
- silently simplify an approved section;
- treat the current browser implementation as visual truth.

Missing material UI must return through the request lifecycle rather than being designed by Claude.

---

# 5. v2.2 visual-first principle

v2.2 preserves the v2.1 rule:

```text
IMAGE = VISIBLE FORM
CONTRACT = INVISIBLE / AMBIGUOUS BEHAVIOR
```

Do not spend tokens describing visible UI that an executor can reliably derive from an approved full-page render.

Use contracts for information a render cannot safely communicate, such as:

- breakpoints and responsive transitions not represented by supplied renders;
- hover/focus/active behavior;
- animation/motion;
- routes and navigation targets;
- loading/empty/error/authenticated/selected states;
- API/CMS/data binding;
- accessibility behavior;
- conditional visibility;
- functional constraints / `mustNot` rules;
- exact geometry only when material to fidelity.

Token efficiency MUST NOT be used as justification to skip required authority or behavior information.

---

# 6. GitHub project state

A project repository SHOULD use `.webby/` as the machine-readable exchange layer:

```text
.webby/
├── PROJECT_INTAKE.json
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

Not every optional contract must be verbose or present when the information is authoritative and unambiguous elsewhere. Active required inputs are declared by the handoff.

Canonical schemas live under `schemas/`.

---

# 7. GĐ3 — Visual-First Handoff

Read `references/VISUAL_HANDOFF_PROTOCOL.md`.

After user approval, ChatGPT SHOULD publish implementation-relevant full-page renders for required routes/viewports.

Recommended visual authority order when applicable:

```text
1. approved original/source asset
2. approved full-page render
3. approved structured Master/design source
4. explicit visual/behavior contract
5. browser implementation
```

Source-first asset rules remain mandatory; an approved render does not replace an authoritative original logo/SVG/native asset.

Hard rule:

```text
BROWSER != APPROVED VISUAL TRUTH
→ FIX BROWSER IMPLEMENTATION
```

GĐ3 packages:

```text
APPROVED RENDERS
+ ROUTE/VIEWPORT MAPPING
+ AUTHORITATIVE ASSETS
+ MINIMAL NON-VISIBLE CONTRACT
+ HANDOFF / LOCK / REVISION STATE
```

`visual-handoff/routes.json`, when used, SHOULD conform to `schemas/visual-handoff.schema.json`.

---

# 8. UI_SETUP_COMPLETE hard gate

The baseline gate and v2/v2.1 safeguards remain active.

For new v2.2 project flows, applicable checks include:

```text
[ ] INTAKE_COMPLETE is true before GĐ1-derived visual work is considered authoritative
[ ] PROJECT_INTAKE has no unresolved HARD_GAP affecting active scope
[ ] HANDOFF identifies deterministic UI revision/commit
[ ] WEBBY_LOCK exists
[ ] required handoff files exist
[ ] lock entries resolve
[ ] production assets referenced by manifests exist
[ ] required route/viewport approved renders exist
[ ] visual-handoff mappings resolve
[ ] active visual package is not stale
[ ] required non-visible behavior is contracted
[ ] no unresolved HARD UI BLOCKER remains
[ ] no OPEN blocking request conflicts with readiness
[ ] ownership boundaries are declared
[ ] validation passes or validator-unavailable reason is recorded
```

Only then:

```text
UI_SETUP_COMPLETE = true
```

---

# 9. Revision, lock and ownership

A handoff SHOULD identify:

```text
handoffId
uiRevision
uiCommit
parentUiCommit
createdAt
```

`WEBBY_LOCK.json` identifies the exact contract and approved visual state the executor consumes.

If active UI or approved renders change materially after implementation begins:

```text
STALE_HANDOFF
```

Claude MUST consume the new handoff/revision or create a request when migration is ambiguous.

Typical ChatGPT-owned content:

```text
PROJECT_INTAKE / visual specs / maps
visual-handoff approved renders/mappings
HANDOFF / WEBBY_LOCK
source + production visual assets
design/master outputs
visual QA defects/acceptance
```

Typical executor-owned content:

```text
src/**
app/**
components/**
server/backend implementation
implementation configuration
.webby/requests/**
.webby/implementation/**
```

Read `references/AGENT_OWNERSHIP_PROTOCOL.md` for detailed write boundaries.

---

# 10. Context/token policy

Executors SHOULD load only the active scope plus required shared dependencies.

Preferred policy:

```text
ROUTE-SCOPED CONTEXT
COMPONENT-SCOPED CONTEXT
ON-DEMAND CONTRACT LOADING
```

Example for `/product`:

```text
product approved render(s)
+ product-specific assets
+ product responsive rules
+ product interactions/states
+ shared tokens/components actually used
```

Do not dump the entire `.webby/` package into model context by default.

Likewise, GĐ0 SHOULD ask the smallest useful set of questions rather than dumping a giant intake form on the user.

---

# 11. GĐ4 — Visual Reconstruction

Before implementation, Claude/executor SHOULD reconstruct visible UI directly from approved visual truth:

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

Hard rules:

```text
VISIBLE APPROVED UI MUST BE DERIVED FROM APPROVED VISUAL TRUTH WHEN AVAILABLE.
VISIBLE IN APPROVED RENDER != MISSING UI.
MISSING MATERIAL UI != CLAUDE DESIGNS IT.
```

If a material UI decision is unclear in both render and contract, use the request lifecycle.

Implementation targets remain flexible:

```text
MODE A — CODE
React / Next.js / Vue / HTML/CSS / selected stack

MODE B — ELEMENTOR
only when project explicitly targets WordPress + Elementor
```

Elementor is an implementation target, not the default architecture.

---

# 12. Request lifecycle

Recommended lifecycle:

```text
OPEN
→ ACKNOWLEDGED
→ RESOLVED
→ CONSUMED
→ CLOSED
```

A resolved request SHOULD record the affected revision/commit/files.

Claude consumes the resolved state before closing the request.

---

# 13. Implementation receipt

After an implementation milestone, Claude SHOULD publish:

```text
.webby/implementation/IMPLEMENTATION_RECEIPT.json
```

At minimum it identifies:

```text
consumedUiCommit / consumedUiRevision
implementationCommit
implemented routes/components
build/test status when available
open requests/blockers
preview/deployment reference when available
```

---

# 14. GĐ7 — Visual QA

Read `references/QA_PROTOCOL.md`.

Normal loop:

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

Approved render = expected visual state.

Browser screenshot = implementation evidence.

Claude fixes defects; ChatGPT closes visual defects only after re-review/acceptance.

---

# 15. Validation

Canonical validator:

```bash
python scripts/webby-validate.py /path/to/project
```

The validator verifies machine-readable handoff structure and cross-references. It cannot prove artistic quality or pixel parity; visual acceptance remains ChatGPT's responsibility.

---

# 16. Versioned evolution

Current protocol version:

```text
2.2.0
```

Generalized skill changes require explicit user approval before being committed to this canonical repository.

Do not create random replacement repositories such as `webbyLucifer-v2`, `final` or `new`. Version this same canonical repository.

---

# 17. Final v2.2 model

```text
RAW / PARTIAL USER INPUT
↓
GĐ0 INSPECT EVERYTHING ALREADY PROVIDED
↓
ADAPTIVE QUESTIONS FOR MATERIAL GAPS ONLY
↓
PERSONALIZED PROJECT BRIEF
↓
INTAKE_COMPLETE
↓
GĐ1 DESIGN / FULL-PAGE UI
↓
GĐ2 MASTER / DESIGN SYSTEM
↓
USER APPROVAL
↓
APPROVED VISUAL TRUTH — WEB / MOBILE
↓
GĐ3 VISUAL-FIRST HANDOFF
↓
APPROVED RENDERS + MINIMAL CONTRACT
↓
SCHEMAS + LOCK + VALIDATION + OWNERSHIP
↓
UI_SETUP_COMPLETE
↓
GĐ4 VISUAL RECONSTRUCTION → CODE / ELEMENTOR
↓
IMPLEMENTATION RECEIPT
↓
GĐ5 UX
↓
GĐ6 BACKEND / CMS / LOGIC
↓
RUN WEBSITE + MATCHING SCREENSHOTS
↓
GĐ7 CHATGPT VISUAL QA
↓
DEFECTS ↔ EXECUTOR FIX ↔ RE-QA
↓
PRODUCTION_READY
```

Central rules:

> **Đọc hết dữ kiện người dùng đã đưa trước khi hỏi. Chỉ hỏi phần còn thiếu và có ảnh hưởng thật sự.**

> **Không bắt đầu GĐ1 khi còn HARD_GAP có thể làm thay đổi hướng thiết kế hoặc mức cá nhân hoá.**

> **Ảnh/approved render truyền tải phần giao diện nhìn thấy. Contract truyền tải hành vi, trạng thái, responsive, dữ liệu và phần ảnh không thể hiện rõ.**

> **Claude triển khai UI; Claude không thiết kế UI.**

> **Approved render là expected visual state; browser screenshot là implementation evidence.**

For detailed GĐ1→GĐ7 visual and implementation rules not repeated here, `references/WORKFLOW_BASELINE_V1.md` remains incorporated by reference.