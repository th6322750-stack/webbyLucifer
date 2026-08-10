# webbyLucifer — `change_web`

> **Mission:** Turn a client brief into an approved, fully specified UI system prepared by ChatGPT, publish that system and its production assets/specs through GitHub, let Claude implement frontend/UX/backend without making visual-design decisions, then verify the real website against the approved visual truth.
>
> **Core architecture:** **ChatGPT = FULL UI AUTHORITY. Claude = IMPLEMENTATION AUTHORITY. GitHub = VERSIONED EXCHANGE LAYER / SHARED PROJECT STATE.**
>
> **Operating principle:** Claude must never be forced to guess an approved UI decision. ChatGPT must not hand off implementation until the complete UI setup passes `UI_SETUP_COMPLETE`.

---

# 0. NON-NEGOTIABLE OPERATING MODEL

`webbyLucifer` is a gated seven-stage workflow.

1. **GĐ1 — DESIGN / FULL-PAGE UI** — ChatGPT
2. **GĐ2 — FULL UI MASTER / DESIGN SYSTEM** — ChatGPT
3. **GĐ3 — FULL PRODUCTION UI SETUP / GITHUB HANDOFF** — ChatGPT
4. **GĐ4 — STATIC FRONTEND IMPLEMENTATION** — Claude by default; Codex only when explicitly selected
5. **GĐ5 — UX / FRONTEND ENHANCEMENT** — selected implementation executor
6. **GĐ6 — BACKEND / CMS / LOGIC** — selected implementation executor
7. **GĐ7 — QA / PRODUCTION** — ChatGPT reviews visual truth; executor fixes implementation

The default input is one client brief. Ask only questions that genuinely block useful progress, except mandatory gates explicitly defined below.

## Highest-priority rule

Before implementation handoff, ChatGPT MUST completely define and prepare the visual UI system.

Claude is an implementation executor, not a visual designer.

Claude MAY:

- translate the approved UI into React/Next/Vue/HTML/CSS or the chosen frontend stack;
- implement responsive behavior according to the supplied contract;
- implement interactions, motion and application UX;
- connect data, forms, APIs, CMS, authentication and backend logic;
- improve code architecture, accessibility, performance and maintainability without changing the approved visual identity.

Claude MUST NOT independently:

- invent missing UI;
- choose a replacement font;
- choose a replacement icon;
- redraw a supplied visual asset;
- change approved colors, spacing, radii, typography, layout or imagery because another choice is easier to code;
- reinterpret desktop/mobile composition without an explicit responsive rule;
- silently simplify an approved section;
- use a generic component-library look in place of the approved design;
- treat the current browser implementation as the visual source of truth.

When approved UI information is missing, Claude must request it through the project handoff/request mechanism rather than designing it itself.

---

# 1. TWO-REPOSITORY MODEL

## Canonical skill repository

```text
th6322750-stack/webbyLucifer
```

This public repository contains generalized workflow knowledge only.

Never publish client secrets, private URLs, proprietary source code, unreleased client designs, personal data, credentials, API keys or non-redistributable assets/fonts here.

## Project repository

Each real project SHOULD use its own project repository. This project repository is the operational exchange layer between ChatGPT and Claude.

```text
CHATGPT
  ↓ visual assets + UI specs + handoff state
PROJECT GITHUB REPOSITORY
  ↓ git pull / read handoff
CLAUDE
  ↓ implementation commits
PROJECT GITHUB REPOSITORY
  ↓ browser build / screenshots / code state
CHATGPT QA
```

GitHub is not merely file storage in this workflow.

```text
GITHUB =
VERSIONED COMMUNICATION BUS
+ ASSET REGISTRY
+ UI IMPLEMENTATION CONTRACT
+ PROJECT STATE
+ QA EXCHANGE
```

Google Drive remains the preferred client-delivery workspace for large approved WEB/MOBILE renders and client-facing packages when Drive access is available.

---

# GĐ1 — DESIGN / FULL-PAGE UI

## Owner

**ChatGPT — mandatory visual authority.**

## Goal

Understand the brief, normalize inputs, research the correct design language, render meaningful directions, obtain user selection, then produce approved full-page WEB/MOBILE designs for all required routes.

Required order:

```text
CLIENT BRIEF
↓
DRIVE GATE
↓
GĐ1.P PROJECT INTAKE / EVIDENCE LOCK
↓
PROJECT TYPE GATE
↓
GĐ1.0 DESIGN RESEARCH & KNOWLEDGE GATE
↓
GĐ1.1 DEMO-DIRECTION PREVIEW GATE
↓
USER SELECTS DIRECTION
↓
FULL-PAGE FINAL UI PRODUCTION
↓
DRIVE DELIVERY
↓
CLIENT / USER APPROVAL
```

---

# GĐ1.P — PROJECT INTAKE / EVIDENCE LOCK

Before design research, normalize all available project inputs into an internal `PROJECT_INPUT_MANIFEST`.

Inspect:

- client brief;
- business/domain;
- audience and conversion goal;
- logo/brand assets;
- brand colors;
- supplied copy/content;
- product/service/property imagery;
- references/screenshots;
- existing website if supplied;
- required routes/features;
- admin/CMS requirements;
- cultural/brand constraints;
- WEB/MOBILE expectations;
- source asset formats and usage rights where known.

Example working structure:

```yaml
project:
  name: null
  type: UNDECIDED
  goal: null
  conversion_goal: null
  audience: null
brand:
  logo: null
  colors: []
  fonts: []
content:
  status: PARTIAL
assets: []
references: []
requirements:
  routes: []
  features: []
  admin_required: false
constraints:
  must_have: []
  must_not_have: []
unknowns: []
assumptions: []
blockers: []
```

Each uncertainty is classified as exactly one of:

- `READY` — authoritative enough to use;
- `ASSUMED` — safe working assumption, explicitly recorded;
- `SOFT_GAP` — may continue with placeholder/temporary handling;
- `HARD_BLOCKER` — useful work cannot continue without user input/access.

Do not invent fake percentage readiness scores.

## Asset authority hierarchy

Prefer visual sources in this order when applicable:

1. original vector/native source such as AI/SVG/Figma/EPS/PDF vector;
2. original raster/native image source such as PSD/PNG/TIFF/high-resolution source;
3. approved structured Master;
4. approved WEB/MOBILE render;
5. derived/reconstructed helper asset.

Rules:

- if an original logo vector exists, do not crop the logo from a screenshot;
- if an original source image exists, do not recreate it from the final page render;
- reference-only material must be marked `production_allowed: false`;
- never pretend a source was inspected when it was not.

State:

```text
DESIGN → INPUT_NORMALIZED
```

---

## Mandatory Google Drive gate

Before final GĐ1 packaging:

1. verify Drive is connected with a minimal read;
2. verify Drive is writable before promising automatic packaging;
3. when writable, create the required project folders automatically;
4. never claim an upload/folder exists unless the connector confirms it;
5. if Drive is disconnected/read-only, stop only the final Drive packaging step and explain the access blocker.

Rough selection previews do not need Drive upload unless requested.

---

## Mandatory project-type gate

Classify the project as exactly one of:

- `LANDING_PAGE`
- `WEBSITE`

If the brief clearly determines the type, classify automatically.

If genuinely ambiguous, ask:

> Thiết kế này là **Landing Page một trang** hay **Website nhiều trang**?

For a website, infer a concise sitemap before final route production. Add Admin/CMS design screens only when required by the brief.

---

# GĐ1.0 — DESIGN RESEARCH & KNOWLEDGE GATE

Research comes before visual generation.

ChatGPT must determine:

- brand mood;
- visual hierarchy;
- layout system;
- typography direction;
- imagery treatment;
- component language;
- spacing rhythm;
- trust/conversion elements;
- important WEB/MOBILE differences;
- project-specific patterns to avoid.

Use strong public repositories and maintained design knowledge as references, not mandatory dependencies.

`REFERENCE != DEPENDENCY`

Primary reference families may include:

- `superdesigndev/superdesign-skill`;
- `alexpate/awesome-design-systems`;
- `radix-ui/primitives`;
- `shadcn-ui/ui`;
- `fontsource/fontsource`;
- `lucide-icons/lucide`;
- `w3c/aria-practices`;
- `dequelabs/axe-core`.

Select references according to the project domain. Do not apply the same layout/look to unrelated businesses.

## Anti-generic test

Before showing a direction, ask internally:

```text
Could this be swapped onto an unrelated company by changing only the logo?
Is this merely a generic Hero + cards + CTA AI template?
Are the proposed directions just recolors?
Does the typography support the actual brand character?
Does the information hierarchy reflect the client's business?
Is mobile intentionally designed rather than shrunken desktop?
```

If the direction fails this test, revise before presenting it.

Form an internal `DESIGN_RESEARCH_SUMMARY`.

State:

```text
INPUT_NORMALIZED → DESIGN_RESEARCH_READY
```

---

# GĐ1.1 — DEMO-DIRECTION PREVIEW GATE

Unless the user already supplied the number, ask:

> **Bạn muốn mình render trước bao nhiêu phương án giao diện demo để chọn? 1, 2, 3 hay số khác?**

Do not silently default to one design.

Each direction must differ meaningfully in composition, typography, Hero concept, image treatment, navigation, spacing, components and/or brand mood. Trivial recolors are not separate directions.

Preview enough of each direction to judge the system. For a landing page this normally means Header + Hero + 1–2 representative sections. For a website, normally preview the homepage/primary route plus shared system elements. Include mobile preview when mobile materially changes the concept.

Do NOT begin complete full-page production until at least one direction is explicitly selected/approved.

```text
DESIGN_RESEARCH_READY
→ DEMO_PREVIEWS_RENDERED
→ USER_DIRECTION_SELECTED
→ FULL_UI_PRODUCTION
```

Rejected directions must not leak into later Master/assets/implementation.

---

# GĐ1 FINAL OUTPUT CONTRACT

## Landing page

For one selected direction:

```text
TEN-DU-AN/
├── bản WEB/
│   └── WEB_TenDuAn.png
├── bản MOBILE/
│   └── MOBILE_TenDuAn.png
└── Document fonts/
```

WEB and MOBILE final renders must each be one continuous full page from Header to Footer.

## Website

Every route must be its own separate continuous full-page render.

```text
TEN-DU-AN/
├── bản WEB/
│   ├── 01_TrangChu_WEB.png
│   ├── 02_TenTrang_WEB.png
│   └── ...
├── bản MOBILE/
│   ├── 01_TrangChu_MOBILE.png
│   ├── 02_TenTrang_MOBILE.png
│   └── ...
├── bản ADMIN/              # only when required
│   └── ...
└── Document fonts/
```

Never combine all final routes into one promotional board.

## Resolution

Final GĐ1 PNGs must be sharp, readable and exported from the final composition rather than enlarged previews.

WEB minimum:

```text
width: 1920 px
height: natural full-page height
```

MOBILE minimum:

```text
width: 1080 px
height: natural full-page height
```

Mobile must be an intentional mobile composition.

Hard failures include first-viewport-only outputs, collages, presentation boards, cropped pages, visibly blurry output, broken text, aggressive compression and unexplained missing fonts.

## Fonts

`Document fonts/` is mandatory for final GĐ1 packaging.

Include actual used font files when redistribution is permitted and files are available. If a required font binary cannot legally/technically be uploaded, include a manifest with exact family, style/weight, source/acquisition requirement, affected UI roles and reason the binary is absent.

```text
FULL_UI_PRODUCTION → DESIGN_APPROVED
```

---

# GĐ2 — FULL UI MASTER / DESIGN SYSTEM

## Owner

**ChatGPT — mandatory.**

## Goal

Convert the approved design into a structured visual Master and define the complete design system so downstream implementation does not need to infer visual decisions from screenshots alone.

If Master strategy is not already selected, ask:

> Giai đoạn 2 muốn theo hướng nào: **A — Figma Master, B — SVG Master, hay C — cả hai để benchmark?**

Allowed:

- `FIGMA_MASTER`
- `SVG_MASTER`
- `BOTH_BENCHMARK`

Do not silently choose when this gate applies.

## Master must preserve

- every approved route/frame;
- desktop and mobile geometry;
- typography;
- colors/tokens;
- spacing/grid;
- radii/borders;
- shadows/glows/gradients;
- image identity and crop;
- component anatomy;
- component variants/states where relevant;
- layer order/z-index intent;
- masks/clips;
- reusable decorative systems;
- responsive intent.

## Full UI system requirement

ChatGPT must define all visual components needed by the approved routes, not just the page screenshots.

Examples may include:

```text
Header
MobileHeader
Navigation
Hero
SearchBar
FilterPanel
PropertyCard
ProjectCard
NewsCard
Badges
Gallery
Breadcrumb
Pagination
Forms
CTA
Footer
AdminSidebar
AdminHeader
AdminTable
AdminForm
Uploader
Modal
Drawer
Tabs
Accordion
Toast
Empty/Error/Loading states
```

Only components actually required by the project should be created, but every required visual component must be covered.

For applicable components define visual states such as:

- default;
- hover;
- active/selected;
- focus;
- disabled;
- loading;
- empty;
- error;
- success.

GĐ2 is incomplete if the implementation executor still needs to choose how a visible UI element should look.

```text
DESIGN_APPROVED → MASTER_READY
```

---

# GĐ3 — FULL PRODUCTION UI SETUP / GITHUB HANDOFF

## Owner

**ChatGPT — mandatory owner of all production UI setup.**

This stage is not merely “extract some assets.” Its purpose is to make the visual system implementation-ready in GitHub.

> ChatGPT must fully prepare the UI. Claude should receive a complete visual implementation contract and then perform implementation work, not design work.

## GĐ3 required responsibilities

ChatGPT must identify, create/extract, normalize and map:

- all routes and sections;
- all reusable UI components;
- all component states required for implementation;
- backgrounds;
- foreground/product/property imagery;
- transparent assets;
- SVG/vector assets;
- logos/wordmarks;
- icons;
- ornaments;
- masks/alpha/gradients/shadows/glows where they are visual assets;
- every visible text string;
- CTA labels;
- exact typography roles;
- design tokens;
- desktop/mobile differences;
- responsive intent;
- asset placement;
- component placement;
- layer/z-index rules where material;
- image crop/focal-point rules;
- visual interaction states;
- implementation constraints and `mustNot` rules.

Claude must not receive a handoff containing phrases such as “use something similar,” “choose a suitable icon,” “make it look premium,” or “adjust as needed” for an approved visual decision.

---

# GĐ3.0 — ASSET CLASSIFICATION

Classify every visual resource before production packaging.

Preferred output types:

| Visual type | Preferred implementation resource |
|---|---|
| logo/vector mark | SVG |
| custom icon | SVG |
| ornament/line/shape | SVG |
| vector illustration | SVG |
| photographic image | AVIF/WebP/PNG/JPEG as appropriate |
| transparent photographic/composite asset | WebP/PNG as appropriate |
| normal headings/body/copy/CTA text | live HTML text |
| normal button/card/layout | HTML/CSS component |
| special wordmark/decorative lettering | SVG/path allowed |
| complex Photoshop-like effect | preserve source fidelity; rasterize only when justified |

Do not convert an entire UI section/page into one giant SVG merely to obtain screenshot parity. That hides the actual interface structure from implementation and is a hard failure unless the entire object is intentionally a single illustration.

---

# GĐ3.1 — SOURCE-FIRST EXTRACTION

When AI/Figma/SVG/PSD or another structured source exists:

1. inspect it before recreating anything;
2. extract original embedded/vector/alpha/mask resources where possible;
3. never fake extractable assets by cropping screenshots;
4. never redraw an existing vector by eye;
5. never replace approved fonts with “close enough”;
6. inspect source effects before inventing CSS approximations;
7. preserve an untouched source asset where practical.

When no structured source exists, decomposition from approved PNGs is allowed, but uncertainty and reconstruction status must be recorded.

---

# GĐ3.2 — SVG PRODUCTION PIPELINE

For vector assets, preserve two concepts:

```text
SOURCE SVG
↓ normalize carefully
CANONICAL SVG
↓ optional generated framework wrapper
COMPONENT
```

The canonical SVG is the production visual source of truth. A generated React/Vue wrapper must not silently diverge from it.

## Canonical SVG rules

- preserve a correct `viewBox` for scalable assets;
- preserve intentional `preserveAspectRatio` behavior;
- remove editor-only metadata when safe;
- remove scripts/event handlers from untrusted or externally sourced SVG;
- reject or explicitly document unsafe/unexpected external resource references;
- preserve gradients, masks, clip paths, filters, opacity, stroke and blend behavior required for visual fidelity;
- optimize paths conservatively only after fidelity is established;
- do not remove accessibility information blindly;
- do not flatten editable/live UI text into paths unless it is genuinely artwork/wordmark;
- detect embedded raster images and classify such files as hybrid SVG when relevant.

## SVG ID collision rule

Inline SVG IDs must not collide across multiple assets.

IDs for gradients, masks, clip paths, filters and referenced definitions must use deterministic asset-scoped prefixes, for example:

```text
hero-gold-wave__gradient-01
hero-gold-wave__mask-01
hero-gold-wave__filter-01
```

Do not use random runtime UUIDs for build-critical SVG references when deterministic IDs are possible.

## SVG color policy

Each SVG should be classified as one of:

- `THEMEABLE` — may use `currentColor`/approved tokens;
- `FIXED_BRAND` — preserve exact approved colors;
- `TOKENIZED` — explicitly mapped to design tokens.

Do not automatically convert brand marks or multi-color artwork to `currentColor`.

## SVG accessibility policy

Classify each SVG as:

- `DECORATIVE` — hidden from assistive semantics where appropriate;
- `INFORMATIVE` — supply an accessible name/description strategy;
- `INTERACTIVE` — semantic control belongs to the containing UI component and must satisfy keyboard/focus requirements.

---

# GĐ3.3 — UI COMPONENT / PLACEMENT CONTRACT

ChatGPT must specify where every production asset/component belongs.

Required machine-readable maps SHOULD include:

- `route-map.json`;
- `section-map.json`;
- `component-map.json`;
- `asset-manifest.json`;
- `placement-map.json`;
- `typography.json`;
- `tokens.json`;
- `responsive.json`;
- `interactions.json`.

A placement entry should resolve at least:

```json
{
  "asset": "hero-gold-wave",
  "file": "assets/production/svg/hero-gold-wave.svg",
  "route": "/",
  "section": "hero",
  "role": "decorative-background",
  "desktop": {
    "anchor": "bottom-right",
    "width": "48%",
    "zIndex": 2
  },
  "mobile": {
    "anchor": "bottom-center",
    "width": "92%"
  },
  "mustNot": [
    "do not redraw with CSS",
    "do not replace approved colors"
  ]
}
```

Exact schema may evolve, but the executor must not need to guess location, role or visual behavior.

---

# GĐ3.4 — PRODUCTION UI ASSET PACK

Preferred project-repository structure:

```text
PROJECT/
├── .webby/
│   ├── PROJECT_STATE.yaml
│   ├── HANDOFF.json
│   ├── CLAUDE_TASK.md
│   ├── asset-manifest.json
│   ├── component-map.json
│   ├── placement-map.json
│   ├── route-map.json
│   ├── section-map.json
│   ├── typography.json
│   ├── tokens.json
│   ├── responsive.json
│   ├── interactions.json
│   ├── requests/
│   └── qa/
│       ├── visual-contract.json
│       ├── defects.json
│       └── qa-report.json
├── assets/
│   ├── source/
│   │   ├── vectors/
│   │   └── raster/
│   ├── production/
│   │   ├── svg/
│   │   ├── images/
│   │   ├── logos/
│   │   └── ornaments/
│   └── previews/
├── public/
└── src/
```

Adapt paths to the actual project stack when necessary, but preserve the separation between authoritative source resources, production resources and handoff metadata.

## Typography map

For every visible text role record:

- exact copy;
- route/section;
- semantic role;
- font family/style/weight;
- desktop/mobile sizes;
- line height;
- letter spacing;
- color;
- alignment;
- important line breaks;
- whether the text is CMS/data-driven or fixed.

---

# GĐ3.5 — VISUAL RESOURCE QA

Asset export success is not a visual PASS.

For important derived/normalized assets compare:

```text
AUTHORITATIVE SOURCE
vs
CANONICAL PRODUCTION ASSET
vs
BROWSER RENDER when applicable
```

Inspect, where relevant:

- geometry;
- aspect ratio;
- crop/focal point;
- gradients;
- masks;
- clipping;
- filters;
- strokes;
- opacity;
- blend behavior;
- embedded images;
- SVG ID references;
- light/dark background behavior;
- desktop/mobile usage.

Raster/vector optimization occurs only after visual fidelity is verified.

---

# GITHUB HANDOFF PROTOCOL

## GitHub role

The project repository is the shared versioned truth between ChatGPT and Claude.

ChatGPT publishes:

- production assets;
- UI specs/maps;
- project state;
- handoff instructions;
- expected visual behavior;
- QA defects after implementation.

Claude consumes those materials, implements them, and pushes implementation commits back to the project repository.

## Required `HANDOFF.json`

Before Claude begins, ChatGPT must publish a handoff state that identifies at minimum:

```json
{
  "producer": "CHATGPT",
  "executor": "CLAUDE",
  "status": "UI_SETUP_COMPLETE",
  "uiCommit": "<git-commit-sha>",
  "requiredInputs": [
    ".webby/CLAUDE_TASK.md",
    ".webby/asset-manifest.json",
    ".webby/component-map.json",
    ".webby/placement-map.json",
    ".webby/route-map.json",
    ".webby/typography.json",
    ".webby/responsive.json"
  ]
}
```

The exact commit field may be populated after the publishing commit is known. If that requires a follow-up metadata commit, record the consumed UI commit deterministically.

Claude SHOULD record the UI/handoff commit it consumed so both agents can detect stale implementation context.

## `CLAUDE_TASK.md`

ChatGPT must generate an implementation prompt/contract for Claude after UI setup.

It must state clearly:

```text
The visual design is complete and approved.
You are the implementation executor, not the visual designer.
Do not redesign.
Do not substitute approved assets.
Do not replace fonts.
Do not change approved colors/layout/spacing because another option is easier.
Read all .webby maps and production assets before implementation.
Implement static visual parity first.
Then implement UX, motion, frontend behavior, backend/CMS/logic as required.
If an approved visual decision is missing, create an asset/UI request instead of guessing.
```

Project-specific route and feature instructions must follow this contract.

---

# CLAUDE REQUEST LOOP

If Claude cannot implement an approved visual because a required UI decision/resource is missing, Claude must not invent it.

Create a request such as:

```text
.webby/requests/REQUEST-###.json
```

Example:

```json
{
  "type": "ASSET_REQUEST",
  "requestedBy": "CLAUDE",
  "route": "/property-detail",
  "section": "features",
  "missing": "custom swimming-pool icon",
  "reason": "approved design contains a custom icon but production asset is absent"
}
```

Then:

```text
CLAUDE REQUEST
↓
GITHUB
↓
CHATGPT supplies/clarifies UI resource
↓
CHATGPT updates manifests/handoff
↓
GITHUB
↓
CLAUDE pulls and continues
```

`MISSING APPROVED UI != CLAUDE DESIGNS IT`.

---

# UI_SETUP_COMPLETE — HARD HANDOFF GATE

**Claude must not begin implementation handoff until this gate passes.**

At minimum verify all applicable items:

```text
[ ] approved route list is complete
[ ] approved WEB full-page designs exist
[ ] approved MOBILE full-page designs exist
[ ] Admin/CMS visual routes exist when required
[ ] Master matches approved designs
[ ] all required visual components are defined
[ ] applicable component states are defined
[ ] all custom logos/icons/ornaments/vectors are supplied
[ ] all production raster assets are supplied
[ ] asset source authority is known or reconstruction uncertainty recorded
[ ] SVG assets pass canonicalization/fidelity checks
[ ] fonts or explicit legal/acquisition manifests are supplied
[ ] typography map is complete
[ ] design tokens are defined
[ ] desktop/mobile differences are mapped
[ ] responsive intent is mapped
[ ] route map is complete
[ ] section map is complete
[ ] component map is complete
[ ] asset manifest is complete
[ ] placement map is complete
[ ] important layer/z-index/crop rules are documented
[ ] visual interaction states are defined
[ ] CLAUDE_TASK.md exists
[ ] HANDOFF.json exists
[ ] project GitHub repository contains the handoff assets/specs
[ ] GitHub upload/commit is verified
[ ] no known HARD UI BLOCKER remains
```

If any applicable required item fails:

```text
UI_SETUP_COMPLETE = false
```

Do not tell Claude to “figure it out.” Return responsibility to ChatGPT/GĐ2/GĐ3 and finish the UI setup.

State:

```text
MASTER_READY
→ UI_ASSET_PACK_READY
→ UI_SETUP_COMPLETE
```

---

# GĐ4 — STATIC FRONTEND IMPLEMENTATION

## Owner

**Claude by default in the ChatGPT↔GitHub↔Claude workflow. Codex may be selected explicitly.**

## Entry requirement

```text
UI_SETUP_COMPLETE == true
```

No exception for convenience.

## Executor workflow

Before coding, Claude must:

1. pull the project repository;
2. read `.webby/HANDOFF.json`;
3. identify the UI commit/state being consumed;
4. read `.webby/CLAUDE_TASK.md`;
5. read route/section/component/asset/placement/typography/responsive maps;
6. inspect production assets;
7. only then begin implementation.

## Goal

Translate the supplied complete UI into real frontend code with maximum visual parity.

Claude owns implementation quality and component architecture but not visual invention.

Claude may choose clean code abstractions when they preserve the supplied visual contract.

Claude must use the supplied assets/fonts where specified, preserve live semantic text where appropriate, respect routes and treat WEB/MOBILE as potentially independent compositions.

Never self-certify “100% pixel-perfect.” Render every required route at known target viewports and compare before static PASS.

```text
UI_SETUP_COMPLETE → STATIC_UI_PASS
```

---

# GĐ5 — UX / FRONTEND ENHANCEMENT

## Owner

**Selected implementation executor, normally Claude.**

Only after static visual PASS, implement project-required:

- hover/focus/active behavior;
- sticky navigation;
- menus/drawers;
- modal/lightbox;
- sliders/carousels;
- tabs/accordion;
- form behavior;
- scroll behavior;
- motion/animation;
- responsive interaction changes;
- keyboard behavior;
- reduced-motion handling;
- application/client-side state and other frontend logic.

The visual states supplied by ChatGPT are authoritative. Claude implements their behavior.

UX work must not silently redesign the approved composition.

```text
STATIC_UI_PASS → UX_PASS
```

---

# GĐ6 — BACKEND / CMS / LOGIC

## Owner

**Selected implementation executor, normally Claude.**

Add only what the project requires:

- CMS;
- API;
- database;
- forms/submissions;
- email;
- uploads;
- content/product/news/property data;
- search;
- authentication/roles;
- payments;
- integrations;
- dashboards;
- server validation and business logic.

A simple landing page may need little or no backend.

Backend implementation must not alter the approved frontend visual system merely to simplify data integration.

```text
UX_PASS → FUNCTIONAL_PASS
```

---

# GĐ7 — QA / PRODUCTION

## Roles

- **ChatGPT:** visual authority, design QA, defect identification and visual acceptance.
- **Claude/executor:** implementation, functional fixes and code changes.

## GitHub QA loop

After an implementation commit:

```text
CLAUDE IMPLEMENTATION
↓
GITHUB
↓
CHATGPT visual/functional review
↓
.webby/qa/defects.json or equivalent defect contract
↓
GITHUB
↓
CLAUDE fixes
↓
GITHUB
↓
CHATGPT re-QA
```

Visual defects should identify route, viewport, section/component, severity, observed problem and expected approved behavior whenever possible.

## QA dimensions

### Visual
Compare approved routes/Master against browser renders for layout, typography, asset identity/crop, spacing, colors, borders/radii, effects, component states and responsive composition. Prefer screenshot overlay/diff where useful.

### Responsive
Test desktop, tablet where relevant, mobile and narrow-mobile safety.

### Interaction
Verify navigation, keyboard behavior, forms, loading/error/success states, modals, drawers, sliders, focus and reduced motion.

### Accessibility
Check semantic HTML, keyboard support, visible focus, accessible labels/names and automated checks where useful.

### Performance
Check image/font loading, bundle weight, layout shifts, interaction responsiveness and caching.

### Backend/security
Where applicable validate authorization, server validation, input handling, secrets, API errors, database constraints/migrations and abuse/rate considerations.

```text
FUNCTIONAL_PASS → QA_PASS → PRODUCTION_READY
```

Never claim mathematical visual identity where browser/OS/font rasterization can create unavoidable differences.

---

# SOURCE-OF-TRUTH HIERARCHY

For visual decisions:

1. approved structured UI Master / design system;
2. approved ChatGPT component system;
3. approved production visual assets and UI maps;
4. approved full-page WEB/MOBILE renders;
5. original authoritative assets/fonts where applicable;
6. browser implementation;
7. derived/helper implementation assets.

The browser implementation does not become visual truth merely because it exists.

If browser output conflicts with approved UI truth, implementation is corrected unless the user explicitly approves a design change.

Rejected GĐ1 directions are never implementation sources of truth.

---

# HARD OWNERSHIP CONTRACT

## ChatGPT owns

- input/evidence normalization for visual work;
- design research;
- art direction;
- full WEB/MOBILE visual composition;
- visual Admin/CMS screens when required;
- full component visual system;
- component variants/states;
- SVG/vector production resources;
- production raster visual resources;
- logos/icons/ornaments;
- typography/font mapping;
- colors/tokens/spacing/radii/shadows/gradients;
- responsive visual intent;
- route/section/component mapping;
- asset placement/layer/crop mapping;
- visual implementation constraints;
- Claude handoff prompt;
- visual QA and acceptance.

## Claude/executor owns

- frontend code implementation of the supplied visual system;
- component/code architecture;
- responsive code behavior following the supplied contract;
- UX logic and interactions;
- animation implementation from supplied visual/interaction intent;
- data integration;
- forms/application state;
- API/CMS/database/auth/backend;
- code quality;
- accessibility implementation;
- performance optimization that preserves visual fidelity;
- fixes requested by QA.

## GitHub owns no decisions

GitHub is the shared, versioned exchange/state layer. It records what ChatGPT supplied, what Claude consumed and what implementation/QA changed.

---

# ANTI-DEAD-END RULES

## NEVER

- skip input normalization when source authority matters;
- skip GĐ1 design research and render generic output immediately;
- pretend a repository/source was inspected when it was not;
- silently force one visual direction when the direction-count gate applies;
- present trivial recolors as separate directions;
- begin final full-page production before direction selection;
- mix rejected directions into approved work;
- code before visual truth is established;
- hand Claude an incomplete visual system and tell it to finish the design;
- allow Claude to invent missing approved UI;
- hand off before `UI_SETUP_COMPLETE`;
- crop screenshots to fake extractable source assets;
- redraw existing vectors by eye;
- replace approved fonts with “close enough”;
- remove SVG viewBox/accessibility information blindly;
- allow inline SVG ID collisions;
- turn entire normal UI sections into giant SVG screenshots;
- create presentation boards instead of required full-page final renders;
- omit required font documentation;
- upload low-resolution/broken final design images;
- combine multiple website routes into one final board;
- let multiple agents independently change the same visual truth;
- claim pixel-perfect without comparison;
- add backend/framework complexity without requirements;
- publish private client material to the canonical public skill repo.

## ALWAYS

- verify Drive before final Drive packaging;
- classify Landing Page or Website;
- normalize source/evidence inputs;
- research design before rendering previews;
- explicitly know demo-direction count when required;
- obtain user direction selection;
- create sharp continuous WEB/MOBILE final designs;
- include fonts or explicit font manifest;
- lock an approved Master;
- let ChatGPT own the entire visual UI setup;
- decompose all required production assets/components;
- map asset placement and responsive intent;
- normalize/QA SVG production assets;
- publish the full UI handoff to the project GitHub repository;
- verify `UI_SETUP_COMPLETE` before implementation;
- let Claude implement rather than redesign;
- use GitHub requests instead of Claude guessing missing UI;
- compare browser output against approved visual truth;
- retain reusable lessons.

---

# REFERENCE / KNOWLEDGE PACK

Use references, not mandatory dependencies.

## Design / UI

- `superdesigndev/superdesign-skill`
- `alexpate/awesome-design-systems`
- `radix-ui/primitives`
- `shadcn-ui/ui`
- `storybookjs/storybook`
- `fontsource/fontsource`
- `lucide-icons/lucide`
- `w3c/aria-practices`
- `dequelabs/axe-core`

## SVG / visual asset processing

Evaluate maintained tools and standards for:

- SVG source preservation;
- viewBox/aspect-ratio correctness;
- safe deterministic ID prefixing;
- conservative optimization;
- script/external-reference handling;
- vector accessibility;
- framework component generation;
- visual regression comparison.

Common references may include W3C SVG specifications, SVGO and SVGR where relevant.

## Frontend

- `vercel/next.js`
- `tailwindlabs/tailwindcss`
- `TanStack/query`
- `react-hook-form/react-hook-form`
- `colinhacks/zod`

## Backend / CMS / Auth

- `supabase/supabase`
- `prisma/prisma`
- `payloadcms/payload`
- `trpc/trpc`
- `better-auth/better-auth`

## QA

- `microsoft/playwright`
- `mapbox/pixelmatch`
- `GoogleChrome/lighthouse`
- `getsentry/sentry-javascript`

Evaluate stronger maintained alternatives over time.

---

# CONTINUOUS LEARNING & SKILL EVOLUTION POLICY

`webbyLucifer` operates in a continuous-learning state.

At meaningful milestones form `LESSONS_LEARNED` covering successes, failures, root causes, better alternatives, reusable rules, rules to remove, useful tools/repositories, QA additions and proposed skill changes.

Do not deploy generalized skill changes automatically.

Only after explicit user approval may the AI:

1. inspect the canonical repo;
2. make the smallest safe generalized change;
3. verify no private client data is included;
4. commit/push to the same canonical repository;
5. report the resulting commit SHA.

Canonical repository:

```text
th6322750-stack/webbyLucifer
```

Do not create `-v2`, `-new`, `-final`, or similar replacement repositories unless explicitly requested.

---

# SUGGESTED PROJECT STATE

```yaml
project_name: null
project_type: UNDECIDED # LANDING_PAGE | WEBSITE
phase: DESIGN

input:
  normalized: false
  blockers: []
  assumptions: []

drive:
  connected: unknown
  writable: unknown
  project_folder: null
  uploads_verified: false

design:
  research_complete: false
  demo_direction_count: null
  demo_previews_rendered: false
  selected_directions: []
  direction_locked: false
  sitemap: []
  web_approved: false
  mobile_approved: false
  fonts_packaged: false

master:
  mode: UNDECIDED # FIGMA_MASTER | SVG_MASTER | BOTH_BENCHMARK
  ready: false

ui_setup:
  components_complete: false
  states_complete: false
  assets_complete: false
  svg_qa_pass: false
  typography_complete: false
  tokens_complete: false
  placement_complete: false
  responsive_complete: false
  github_published: false
  handoff_ready: false
  ui_setup_complete: false
  ui_commit: null

implementation:
  executor: CLAUDE
  consumed_ui_commit: null
  static_ui_pass: false
  ux_pass: false
  functional_pass: false

qa:
  visual_pass: false
  responsive_pass: false
  accessibility_pass: false
  performance_pass: false
  backend_pass: false

production_ready: false
```

---

# FINAL OPERATING SUMMARY

```text
CLIENT BRIEF
    ↓
GĐ1.P — normalize inputs / evidence / asset authority
    ↓
verify Drive for client-delivery packaging
    ↓
classify LANDING_PAGE / WEBSITE
    ↓
GĐ1.0 — design research
    ↓
GĐ1.1 — meaningful preview directions
    ↓
USER SELECTS DIRECTION
    ↓
ChatGPT renders every required WEB/MOBILE route
    ↓
client/user approves visual direction
    ↓
GĐ2 — ChatGPT locks full UI Master + complete component visual system
    ↓
GĐ3 — ChatGPT creates/extracts all production UI resources
    ↓
SVG/raster/font/token/component/placement/responsive QA
    ↓
ChatGPT publishes project UI package + maps + CLAUDE_TASK.md to GitHub
    ↓
UI_SETUP_COMPLETE
    ↓
Claude pulls exact UI commit
    ↓
GĐ4 — Claude implements static frontend without redesigning
    ↓
STATIC_UI_PASS
    ↓
GĐ5 — Claude implements UX/frontend behavior
    ↓
UX_PASS
    ↓
GĐ6 — Claude implements backend/CMS/logic as required
    ↓
FUNCTIONAL_PASS
    ↓
GĐ7 — ChatGPT QA → GitHub defect contract → Claude fixes
    ↓
PRODUCTION_READY
    ↓
LESSONS_LEARNED
    ↓ explicit user approval
UPDATE THIS SAME CANONICAL SKILL REPOSITORY
```
