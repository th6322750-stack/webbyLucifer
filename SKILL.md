# webbyLucifer — `change_web` v3.0

> **Mission:** turn incomplete user input into a fully specified, asset-complete, implementation-ready UI package so the implementation executor can code without redesigning, searching for images, reverse-engineering raster pixels, or repeating unnecessary planning/QA loops.
>
> **Core authority:** **USER = FINAL ACCEPTANCE AUTHORITY. CHATGPT = DESIGN / UI / ASSET / MOTION AUTHORITY. CLAUDE = IMPLEMENTATION AUTHORITY. GOOGLE DRIVE = HEAVY ASSET DELIVERY AUTHORITY. GITHUB = CODE + LIGHTWEIGHT VERSIONED CONTRACT/STATE. VERCEL = OPTIONAL PREVIEW, NOT A PREREQUISITE.**

---

# 0. v3 hard principles

```text
ASK MATERIAL QUESTIONS BEFORE DESIGN
COUNT ASSETS BEFORE CREATING THEM
HIGH-RES MASTER FIRST — FULL HD / 4K CLASS, 4K PREFERRED
NO LOW-RES PATCHWORK OR FAKE UPSCALE AS AUTHORITY
NO CLAUDE IMAGE SEARCH / GENERATION / SUBSTITUTION
ASSET PACK BEFORE IMPLEMENTATION
SPEC CREATES RENDER — RENDER NEVER CREATES SPEC
RASTER IS FOR HUMAN ACCEPTANCE / ARRANGEMENT, NOT PIXEL MEASUREMENT
IMPLEMENTATION_READY_UI BEFORE CLAUDE CODES
CLAUDE DOES NOT REDESIGN, RESEARCH, AUDIT THE WHOLE REPO, OR PLAN LONG BY DEFAULT
SCREENSHOT LOOPS ARE NOT DEFAULT
USER PERFORMS FINAL VISUAL ACCEPTANCE
```

User-facing communication rule:

> When an English or specialist term is needed, explain in plain Vietnamese what it means and what it is used for the first time it materially appears, unless the user has clearly demonstrated that the explanation is unnecessary.

---

# 1. Canonical references and precedence

Read only the protocol needed for the active phase.

```text
START / NEW PROJECT
→ SKILL.md
→ references/INTAKE_DISCOVERY_PROTOCOL.md
→ references/ASSET_FIRST_IMPLEMENTATION_READY_PROTOCOL.md

ASSET / FINAL UI / HANDOFF
→ references/ASSET_FIRST_IMPLEMENTATION_READY_PROTOCOL.md
→ references/VISUAL_HANDOFF_PROTOCOL.md
→ references/GITHUB_HANDOFF_PROTOCOL.md
→ references/AGENT_OWNERSHIP_PROTOCOL.md

QA / ACCEPTANCE
→ references/QA_PROTOCOL.md
```

Precedence:

```text
SKILL.md v3 hard rules
> v3 phase-specific protocol
> v2.x protocol where not superseded
> WORKFLOW_BASELINE_V1.md legacy guidance
> examples/templates
```

v3 intentionally supersedes the old assumption that an approved raster render is sufficient implementation authority. In v3, structured spec/manifest owns implementation numbers and asset identity; raster owns human visual acceptance.

---

# 2. Canonical v3 workflow

```text
GĐ0  — INTAKE + ENVIRONMENT / RESOURCE READINESS        ChatGPT + User
GĐ1  — VISUAL DIRECTION / PAGE STRUCTURE                ChatGPT
GĐ2  — UI DECOMPOSITION + ASSET COUNT PLAN              ChatGPT
GĐ3  — ASSET CLASSIFICATION + HIGH-RES PRODUCTION       ChatGPT
GĐ4  — PRODUCTIONIZE + ASSET QA + DRIVE FREEZE          ChatGPT
GĐ5  — DETERMINISTIC UI COMPOSITION + RESPONSIVE/STATE/MOTION  ChatGPT
GĐ6  — USER VISUAL APPROVAL                              User
GĐ7  — IMPLEMENTATION READY GATE                         ChatGPT
GĐ8  — SHORT IMPLEMENTATION CONTRACT                     ChatGPT
GĐ9  — IMPLEMENTATION                                    Claude/executor
GĐ10 — MINIMUM TECHNICAL CHECK                           Claude/executor
GĐ11 — USER ACCEPTANCE                                   User
GĐ12 — FUNCTIONAL QA → BUG FIX → FINAL HANDOFF           QA + executor
```

Hard flow:

```text
USER INPUT
↓
GĐ0 READ EXISTING EVIDENCE + ASK ONLY MATERIAL GAPS
↓
ENVIRONMENT / RESOURCE READINESS KNOWN
↓
GĐ1 VISUAL DIRECTION
↓
GĐ2 DECOMPOSE EVERY ROUTE/SECTION + COUNT ASSETS
↓
REPORT ASSET COUNT TO USER BEFORE PRODUCTION
↓
GĐ3 CREATE / COLLECT ALL REQUIRED HIGH-RES MASTERS
↓
GĐ4 CREATE WEB DELIVERY FILES + QA + ONE DRIVE FOLDER + MANIFEST
↓
GĐ5 BUILD DETERMINISTIC FINAL UI FROM THE ACTUAL PACK
↓
USER APPROVES VISUAL DIRECTION
↓
GĐ7 IMPLEMENTATION_READY_UI GATE
↓
ONLY WHEN ALL APPLICABLE CHECKS = YES
↓
GĐ8 SHORT CONTRACT
↓
GĐ9 CLAUDE: PRE-FLIGHT → READ 1–3 RELEVANT FILES → CODE → INSERT EXACT ASSETS
↓
GĐ10 MINIMUM TECHNICAL CHECK
↓
GĐ11 USER REVIEWS REAL WEBSITE
↓
IF NEEDED: CLASSIFY DESIGN / ASSET / IMPLEMENTATION DEFECT
↓
GĐ12 FUNCTIONAL QA AFTER VISUAL ACCEPTANCE → BUG IDs → TARGETED FIXES
↓
FINAL USER APPROVAL
```

---

# 3. GĐ0 — intake + environment/resource readiness

Read `references/INTAKE_DISCOVERY_PROTOCOL.md`.

Before design, ChatGPT MUST inspect all currently available evidence and establish, when applicable:

```text
repository / GitHub URL
active branch / whether Claude has local unpushed drift
Claude repository access
ChatGPT remote repository access
Google Drive connection + download access
whether Vercel preview is required
CMS / Sheets / API / database source
runtime/env/secrets readiness where material
reference authority: image/PDF/Figma/site/video/current UI
layout mode: FULL_WIDTH / FULL_BLEED_WITH_CONTAINER / BOXED / MIXED
device priority
business/content priority
fidelity expectation
```

If a visual choice such as full-width vs boxed can materially change the page and is not evidenced, ChatGPT MUST ask the user instead of silently choosing.

Do not ask the user to repeat already-known information.

---

# 4. GĐ2 — asset count before asset creation

Before generating or sourcing a production asset pack, ChatGPT MUST decompose every implementation-relevant route into sections and count required assets by role.

Use an Asset Count Plan when useful:

```text
.webby/ASSET_COUNT_PLAN.json
```

Recommended schema:

```text
schemas/asset-count-plan.schema.json
```

Report to the user BEFORE asset production:

```text
total assets
already available
ChatGPT must create/prepare
user/client must supply because fabrication is forbidden
FHD-class masters
4K-class masters
vector/brand assets
route/section distribution
```

Never render an `APPROVED FINAL` page containing visible production assets that do not exist in the frozen pack or have an explicit approved placeholder/data state.

---

# 5. GĐ3/GĐ4 — asset authority and quality

Raster MASTER rules:

```text
FULL HD class minimum when a raster asset is production-authoritative
4K class preferred
hero / full-bleed master: 4K preferred/expected
never treat a small source enlarged to FHD/4K as a true high-resolution authoritative master
never stitch low-resolution scraps merely to satisfy dimensions
```

Aspect-aware examples:

```text
16:9 landscape: 1920×1080 minimum, 3840×2160 preferred
1:1 square:      1920×1920 minimum, 3840×3840 preferred
9:16 portrait:   1080×1920 minimum, 2160×3840 preferred
vector logo/icon: SVG preferred; resolution-independent
```

Asset taxonomy:

```text
BRAND
AUTHENTIC
DEMO
EDITORIAL
DECORATIVE
PLACEHOLDER
DATA_VISUAL
```

Rules:

- `AUTHENTIC` and `DATA_VISUAL` must map to the correct real item/data owner when identity matters.
- `DEMO` must not silently appear as authentic live data.
- `DECORATIVE` cannot be used as a factual image for a named property/project.
- `BRAND` is exact identity material; prefer native/vector source.
- floorplans/maps/progress diagrams are `DATA_VISUAL` and must not be fabricated as factual data.
- Claude MUST NOT search the web, generate, redraw, substitute, or index-map missing assets.

Separate:

```text
MASTER SOURCE = highest-quality authority/archive
WEB DELIVERY = actual file used in implementation
```

Claude should normally consume delivery assets, not oversized masters.

---

# 6. Google Drive asset delivery

Heavy image masters and asset packs default to one project Google Drive folder after production begins.

Recommended structure:

```text
PROJECT_NAME/
├── 01_MASTER_ASSETS/
├── 02_WEB_DELIVERY/
├── 03_BRAND/
├── 04_PROJECTS/
├── 05_RENTALS/
├── 06_EDITORIAL/
├── 07_DATA_VISUAL/
├── 08_PLACEHOLDERS/
├── 09_MANIFEST/
└── 10_FINAL_UI_REFERENCE/
```

GitHub is primarily for code and lightweight versioned contracts. Do not dump all heavy 4K masters into Git merely because Git is available.

Before handoff, confirm Claude can actually access/download the Drive folder. An image visible only inside chat is NOT a delivered asset.

---

# 7. Deterministic UI composition

Read `references/VISUAL_HANDOFF_PROTOCOL.md`.

Core rule:

```text
DECLARED DESIGN VALUES → FINAL COMPOSITION → RASTER REFERENCE
```

Never:

```text
RASTER → CLAUDE MEASURES PIXELS → MAGIC NUMBERS → CODE
```

The composition must use the actual approved asset pack and declared project constraints/tokens where they exist.

Examples of semantic geometry:

```text
container = 1520
columns = 4
gap = 24
card ratio = 4/3
heading = 40/48/700
```

Avoid unexplained geometry such as `199/144` unless Design Authority intentionally declares it for a real reason.

Raster rules:

```text
RASTER = human acceptance + page hierarchy/arrangement reference
SPEC/MANIFEST = implementation authority for numbers, mappings, states and behavior
CLAUDE MAY LOOK AT RASTER
CLAUDE MUST NOT MEASURE RASTER TO INVENT VALUES
```

If a required numeric design value is missing:

```text
BLOCKED_SPEC
```

not pixel measurement.

---

# 8. Responsive, content, state and motion authority

Responsive design must be based on actual project breakpoints/constraints, not arbitrary familiar device widths.

Prefer references at:

```text
mobile representative width
exact layout breakpoint boundary
exact wide/container behavior breakpoint
1920 only when full-width/full-bleed behavior needs large-screen review
```

Content should use real Vietnamese content when available. Protect production components with explicit content envelopes such as max lines, no-wrap, clamps and representative short/long values.

ChatGPT owns visual states that materially change layout, including applicable:

```text
NORMAL
LONG_TEXT
SHORT_TEXT
IMAGE_MISSING
PARTIAL_DATA
EMPTY
FEW_ITEMS
LOADING
```

Do not draw every state if a one-line rule is sufficient; draw only layout-changing states.

ChatGPT owns motion intent. When motion matters, specify only what is necessary:

```text
trigger
duration
easing
distance
stagger
orchestration/order
never-animate list
reduced-motion behavior
```

Claude does not invent motion to make the page feel more premium.

---

# 9. Two approval states

Do not use one vague “approved UI” status for two different things.

```text
VISUAL_DIRECTION_APPROVED
= user likes/approves the visible design direction

IMPLEMENTATION_READY_UI
= the UI also has enough assets, mapping, geometry, responsive behavior, states and delivery information for implementation without invention
```

Claude MUST NOT start ordinary UI implementation from `VISUAL_DIRECTION_APPROVED` alone.

---

# 10. IMPLEMENTATION_READY_UI hard gate

Use `templates/UI_SETUP_CHECKLIST.md`.

Applicable checks include:

```text
[ ] user visual approval recorded
[ ] asset count plan was reported before production
[ ] visible asset pack is complete
[ ] authoritative raster masters meet approved FHD/4K-class policy
[ ] web delivery assets exist
[ ] Drive folder is uploaded and accessible
[ ] asset identity/usage mapping is complete
[ ] layout mode (full-width/boxed/mixed) is locked
[ ] typography is locked
[ ] semantic geometry is locked
[ ] responsive breakpoints/behavior are locked
[ ] required missing/partial states are defined
[ ] motion is locked or explicitly N/A
[ ] no unresolved missing design/asset blocker remains
```

If any applicable item is `NO`:

```text
IMPLEMENTATION_READY_UI = false
DO NOT HAND TO CLAUDE
```

---

# 11. GĐ8/GĐ9 — short Claude contract and minimal execution

The default Claude task must be short and scoped. Use `templates/CLAUDE_TASK.md`.

Ordinary UI task:

```text
receive contract + Drive asset references
↓
pre-flight: DRIFT / SCOPE / TOKEN checks
↓
read 1–3 relevant implementation files by default
↓
code exactly to contract
↓
insert exact mapped assets
↓
minimum technical check
↓
report 3–5 lines
```

The 1–3 file rule is a default warning threshold, not a ban on genuinely cross-cutting work. If the task unexpectedly requires broad scope, report the reason before silently expanding.

Claude MUST NOT by default:

```text
write a long plan/todo
re-audit the entire repository
research external repositories or design inspiration
redesign approved UI
search/generate/substitute images
map assets by array index when identity mapping exists
invent icons/states/motion
measure raster screenshots for geometry
run large screenshot matrices
run the entire test suite for a trivial static spacing/image change
write long narrative reports
```

Allowed pre-flight checks are mechanical, not a new planning phase:

```text
DRIFT CHECK — does local code differ materially from the remote/current contract assumption?
SCOPE CHECK — is a supposedly local component actually shared?
TOKEN CHECK — do requested classes/tokens/icons/constraints exist?
```

Blocker vocabulary:

```text
NEED_ASSET: required file/asset is missing
BLOCKED_SPEC: design/spec is missing or contradictory
TECHNICAL_CONSTRAINT: spec is clear but the current system cannot satisfy it as written
```

Continue unaffected work when safe; never invent a replacement.

---

# 12. Technical check and screenshots

Claude performs only checks proportional to the task.

Examples:

```text
static text/color/spacing/image swap → typecheck/build/lint only as relevant
new responsive layout → one quick browser smoke check when useful
complex runtime interaction → targeted interaction test
backend/data/security change → targeted tests appropriate to that scope
```

Screenshot comparison is NOT the default implementation loop.

Use screenshots only when they add real evidence, for example user-requested preview, diagnosing a visual/runtime issue, or a genuinely layout-sensitive smoke check.

The user is the final visual acceptance authority.

---

# 13. User acceptance + functional QA

After implementation, the user reviews the real website on the available environment (local/preview/production as appropriate).

If rejected, classify the defect before work resumes:

```text
DESIGN ERROR        → ChatGPT changes design/spec
ASSET ERROR         → ChatGPT creates/fixes the asset pack
IMPLEMENTATION ERROR→ Claude fixes code to the existing contract
```

Functional QA follows visual acceptance instead of being used as another design phase.

Functional QA may test customer/admin behavior, then produce stable bug IDs. Claude fixes only the named defects and must not use bug fixing as permission to redesign or re-audit the whole repository.

---

# 14. Version and compatibility

Current protocol version:

```text
3.0.0
```

v3 keeps useful v2.x concepts such as deterministic revision/lock state, request lifecycle, schemas and implementation receipts, but changes the center of gravity:

```text
OLD: approved raster → executor visually reconstructs → screenshot QA loop
NEW: asset-complete deterministic spec → user-approved raster → implementation-ready gate → executor codes without measuring/guessing → user acceptance
```

Generalized skill changes require explicit user approval before being committed to this canonical repository. This v3 change is explicitly user-approved.
