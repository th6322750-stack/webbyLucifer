# webbyLucifer — `change_web`

> **Mission:** Turn a client brief into approved WEB/MOBILE design files, an AI-readable implementation master, a production UI asset pack, a real frontend/backend implementation, and a verified production-ready website.
>
> **Operating principle:** webbyLucifer continuously learns from real projects. It may propose reusable improvements, but it must never deploy learned changes to this canonical public repository without explicit user approval.

---

# 0. CORE OPERATING MODEL

`webbyLucifer` is a gated seven-stage workflow with clear ownership.

1. **GĐ1 — DEMO DESIGN** — ChatGPT
2. **GĐ2 — MASTER UI** — ChatGPT
3. **GĐ3 — UI DECOMPOSITION / UI ASSET PACK** — ChatGPT
4. **GĐ4 — STATIC FRONTEND BUILD** — Codex or Claude
5. **GĐ5 — UX / FRONTEND ENHANCEMENT** — Codex or Claude
6. **GĐ6 — BACKEND / CMS / LOGIC** — Codex or Claude
7. **GĐ7 — QA / PRODUCTION** — ChatGPT reviews; executor fixes

The default input is one client brief. Ask only questions that genuinely block useful progress, except for mandatory gates explicitly defined below.

---

# GĐ1 — DEMO DESIGN

## Owner

**ChatGPT**

## Goal

Understand the client brief, research the right design language, propose one or more meaningful visual directions, render previews for the user to choose from, then produce the final full-page WEB/MOBILE design package for client approval.

GĐ1 MUST NOT jump directly from a brief to one arbitrary final design.

The required order is:

```text
CLIENT BRIEF
↓
DRIVE GATE
↓
PROJECT TYPE GATE
↓
GĐ1.0 DESIGN RESEARCH & KNOWLEDGE GATE
↓
GĐ1.1 DEMO-DIRECTION PREVIEW GATE
↓
USER SELECTS DIRECTION
↓
FULL-PAGE FINAL DEMO PRODUCTION
↓
DRIVE DELIVERY
↓
CLIENT APPROVAL
```

---

## Mandatory Google Drive connection gate

Before GĐ1 production work:

1. Verify that Google Drive is connected with a minimal read.
2. Verify that Drive is writable before promising automatic packaging.
3. When writable, create the required project folders automatically.
4. If Drive is disconnected/read-only, stop final packaging and ask the user to restore access.
5. Never claim a folder or upload exists unless the connector confirms it.

The Drive structure is the **final delivery workspace**. Rough preview experiments do not have to be uploaded there unless the user asks.

---

## Mandatory project-type gate

Classify the project as exactly one of:

- `LANDING_PAGE`
- `WEBSITE`

If the brief clearly determines the type, classify it automatically.

If genuinely ambiguous, ask:

> Thiết kế này là **Landing Page một trang** hay **Website nhiều trang**?

Rules:

- Never treat a multi-page website as one landing page.
- Never invent unnecessary subpages for a landing page.
- For a website, infer a concise sitemap before final full-page production.
- Add Admin/CMS design screens only when the brief requires them.

---

# GĐ1.0 — MANDATORY DESIGN RESEARCH & KNOWLEDGE GATE

## Purpose

Before rendering any visual preview, ChatGPT must research and reason about the correct design language for the specific client, industry, audience, brand, and website type.

The goal is to reduce generic AI output such as the same Hero + three cards + CTA pattern for every project.

**Research comes before visual generation.**

## Mandatory research inputs

Inspect all available inputs first:

- client brief;
- business/industry;
- audience and conversion goal;
- logo and brand assets;
- brand colors;
- supplied copy/content;
- product/service imagery;
- reference websites/screenshots;
- existing website if supplied;
- required routes/features;
- cultural/brand constraints;
- WEB/MOBILE expectations.

Do not assume the client has `.ai`, Figma, PSD, or a complete asset library.

## Design Reference Pack

Use strong public repositories and design knowledge as **references**, not mandatory dependencies.

### Primary GĐ1 references

- `superdesigndev/superdesign-skill` — AI-oriented design workflow and visual exploration patterns.
- `alexpate/awesome-design-systems` — broad design-system references to avoid tunnel vision.
- `radix-ui/primitives` — interaction/component anatomy and state thinking.
- `shadcn-ui/ui` — practical component composition and modern UI structure.
- `fontsource/fontsource` — typography/font discovery and web-font awareness.
- `lucide-icons/lucide` — consistent icon-language reference when appropriate.
- `w3c/aria-practices` — interaction/accessibility patterns that should influence UI decisions early.
- `dequelabs/axe-core` — accessibility QA awareness; reference only during design.

These repositories are **knowledge sources**. GĐ1 must not install all of them or copy their visual style blindly.

`REFERENCE != DEPENDENCY`

## Research-selection rule

Do not use the exact same references with the exact same weight for every project.

Choose research according to the project domain and brief.

Examples:

```text
LUXURY / HERITAGE / CULTURAL
→ editorial composition
→ typography quality
→ whitespace and hierarchy
→ premium image treatment
→ restrained ornament / material feel

REAL ESTATE
→ listing hierarchy
→ property search/filter patterns
→ project/detail storytelling
→ map/location presentation
→ trust and conversion CTA

SAAS / TECHNOLOGY
→ product storytelling
→ modular component systems
→ information hierarchy
→ dashboard/app patterns when relevant
→ strong CTA and product proof

E-COMMERCE
→ category architecture
→ product cards
→ product-detail hierarchy
→ trust, price and CTA clarity
→ cart/checkout patterns when required

SERVICE / SPA / HOSPITALITY
→ emotional imagery
→ service hierarchy
→ social proof
→ booking/contact conversion
→ mobile-first conversion flow
```

These are examples, not fixed templates.

## Research behavior

Before preview rendering, ChatGPT must determine:

- desired brand mood;
- visual hierarchy;
- likely layout system;
- typography direction;
- imagery treatment;
- component language;
- spacing rhythm;
- key trust/conversion elements;
- important WEB/MOBILE differences;
- patterns to avoid because they conflict with the brief.

If the user supplied a reference site, study the reference for principles and intent without blindly cloning copyrighted design details.

If current external research tools are available and the project would benefit, inspect relevant maintained sources. If external research is unavailable, do not fabricate having inspected a repository; continue from the built-in knowledge/reference pack and record the limitation internally.

## Anti-generic rule

Before accepting a proposed art direction, test it against these questions:

```text
Could this design be swapped onto an unrelated company with only the logo changed?
Does it look like a generic AI landing-page template?
Are the directions merely color variations of one layout?
Does the typography actually support the brand character?
Does the information hierarchy reflect this client's business?
Does the mobile concept look intentionally designed rather than shrunk desktop?
```

If the answer exposes generic output, revise the direction before showing it to the user.

## Internal research summary

Before rendering previews, form a concise internal `DESIGN_RESEARCH_SUMMARY`:

```yaml
project_domain:
audience:
conversion_goal:
brand_mood:
visual_principles: []
typography_direction:
imagery_direction:
component_language:
mobile_strategy:
references_consulted: []
patterns_to_avoid: []
```

This is working context, not a required client-facing deliverable unless the user asks for it.

## GĐ1.0 exit gate

Do not render demo previews until:

```text
[ ] brief and supplied assets inspected
[ ] project domain/audience understood
[ ] relevant design references selected
[ ] typography direction considered
[ ] visual principles defined
[ ] WEB/MOBILE implications considered
[ ] generic-template risk checked
[ ] DESIGN_RESEARCH_SUMMARY formed
```

State:

```text
DESIGN → DESIGN_RESEARCH_READY
```

---

# GĐ1.1 — MANDATORY DEMO-DIRECTION PREVIEW GATE

## Purpose

Let the user see and choose the visual direction **before** spending time on complete long WEB/MOBILE renders.

## Mandatory question

Unless the user already supplied the number in the current request, ask:

> **Bạn muốn mình render trước bao nhiêu phương án giao diện demo để chọn? 1, 2, 3 hay số khác?**

Do not silently default to one design.

If the user already requested a number, do not ask again.

## Distinct-direction rule

Each direction must be meaningfully different, not a trivial recolor.

Differences may include:

- composition and hierarchy;
- typography pairing;
- Hero concept;
- image treatment;
- navigation style;
- spacing rhythm;
- card/component language;
- ornament/effect language;
- density/content presentation;
- overall brand mood.

Three almost-identical layouts with different colors are **not** three valid directions.

## Preview rendering contract

For each direction, render a clear preview large enough to judge the design language.

For `LANDING_PAGE`, normally show enough to establish the system:

```text
HEADER
↓
HERO
↓
1–2 REPRESENTATIVE SECTIONS
```

For `WEBSITE`, normally preview the homepage/primary route plus enough shared elements to understand how the whole site will look.

Where mobile materially changes the concept, include a mobile preview.

Preview images are **selection artifacts**, not final GĐ1 delivery assets. They do not replace the required long full-page final PNGs.

## Presentation contract

Label clearly:

```text
PHƯƠNG ÁN 01 — <direction name>
PHƯƠNG ÁN 02 — <direction name>
PHƯƠNG ÁN 03 — <direction name>
...
```

Give only a short rationale/tradeoff for each. Let the visuals do the work.

The user may:

- select one direction;
- select several directions for further development;
- request another exploration round;
- request a hybrid such as `layout PA01 + font PA02 + Hero PA03`.

## Selection lock

Do NOT begin complete full-page production until at least one direction is selected/approved.

```text
DESIGN_RESEARCH_READY
↓
DEMO_DIRECTIONS_REQUESTED
↓
DEMO_PREVIEWS_RENDERED
↓
USER_DIRECTION_SELECTED
↓
FULL_DEMO_PRODUCTION
```

If another exploration round is requested, render another preview round rather than treating the old direction as approved.

## Multiple complete client directions

If the user wants multiple selected directions developed completely for the client, preserve the canonical Drive folders and distinguish variants by filename.

Example:

```text
TEN-DU-AN/
├── bản WEB/
│   ├── PA01_WEB_TenDuAn.png
│   └── PA02_WEB_TenDuAn.png
├── bản MOBILE/
│   ├── PA01_MOBILE_TenDuAn.png
│   └── PA02_MOBILE_TenDuAn.png
└── Document fonts/
    └── ...
```

If one direction is selected, use canonical filenames without `PAxx_` prefix.

Rejected directions must not silently leak into GĐ2/GĐ3/implementation.

---

# GĐ1-A — LANDING_PAGE OUTPUT CONTRACT

A landing page is one continuous route from Header to Footer.

For one selected direction, the final client-facing Drive structure is exactly:

```text
TEN-DU-AN/
│
├── bản WEB/
│   └── WEB_TenDuAn.png
│
├── bản MOBILE/
│   └── MOBILE_TenDuAn.png
│
└── Document fonts/
    ├── FontHeading.ttf / .otf / .woff2
    ├── FontBody.ttf / .otf / .woff2
    └── ...
```

`WEB_TenDuAn.png` must be one continuous full-page image:

```text
HEADER
↓
HERO
↓
ALL CONTENT SECTIONS
↓
CTA / FORM WHEN PRESENT
↓
FOOTER
```

`MOBILE_TenDuAn.png` must also run continuously from Header to Footer using a genuine mobile composition.

### Forbidden final landing outputs

Never use as final GĐ1 output:

- presentation board;
- collage;
- mini screenshots on one canvas;
- desktop/mobile mockup sheet;
- section-summary poster;
- first viewport only;
- cropped Hero only;
- disconnected fragments;
- short/compressed “vón cục” representation of a long page.

Final output must look like a naturally long website design/screenshot.

---

# GĐ1-B — WEBSITE OUTPUT CONTRACT

A website contains multiple routes/pages.

Before final rendering:

1. Infer the sitemap from the brief.
2. Identify required user-facing routes.
3. Include required detail routes such as property/product/project/article detail.
4. Include checkout/account/contact routes only when required.
5. Add Admin/CMS screens only when explicitly required.
6. Apply the selected art direction consistently across the sitemap.

Final Drive structure:

```text
TEN-DU-AN/
│
├── bản WEB/
│   ├── 01_TrangChu_WEB.png
│   ├── 02_TenTrang_WEB.png
│   ├── 03_TenTrang_WEB.png
│   └── ...
│
├── bản MOBILE/
│   ├── 01_TrangChu_MOBILE.png
│   ├── 02_TenTrang_MOBILE.png
│   ├── 03_TenTrang_MOBILE.png
│   └── ...
│
├── bản ADMIN/                    # only when explicitly required
│   ├── 01_TongQuan_ADMIN.png
│   ├── 02_TenManHinh_ADMIN.png
│   └── ...
│
└── Document fonts/
    ├── FontHeading.ttf / .otf / .woff2
    ├── FontBody.ttf / .otf / .woff2
    └── ...
```

Every route must be its **own separate continuous full-page PNG**.

Example:

```text
01_TrangChu_WEB.png
02_DanhSachBDS_WEB.png
03_ChiTietBDS_WEB.png
04_DuAn_WEB.png
05_ChiTietDuAn_WEB.png
06_TinTuc_WEB.png
07_ChiTietTinTuc_WEB.png
08_LienHe_WEB.png
```

Mobile must contain corresponding separate full-page route renders.

Never combine all final website routes into one promotional board or one `TatCaGiaoDien.png` file.

---

# GĐ1 FINAL RESOLUTION CONTRACT

All final GĐ1 PNGs uploaded to Drive must be:

- full-page vertical renders;
- high-resolution;
- readable at 100% zoom;
- free of visible blur/pixelation;
- free of broken text and compression damage;
- exported from the final composition, never enlarged from a low-resolution preview.

## WEB

Minimum:

```text
width: 1920 px
height: natural full-page height
```

The natural page height may be 6000, 8500, 12000px or more. Never squash the page into a short canvas.

## MOBILE

Minimum:

```text
width: 1080 px
height: natural full-page height
```

Mobile must be an intentional mobile composition, not desktop merely resized to 1080px.

## Hard failures

GĐ1 fails when a final image is:

- preview-sized;
- blurry/pixelated;
- upscaled from a smaller preview;
- aggressively compressed;
- cropped before page end;
- first-screen-only;
- a collage/presentation board;
- unreadable in Drive.

In this skill, “Full HD” means at least **1920px-wide WEB** and **1080px-wide MOBILE**, preserving natural page height.

---

# GĐ1 DOCUMENT FONTS CONTRACT

`Document fonts/` is mandatory for every final GĐ1 package.

It must never be silently omitted.

Include actual font files used by the selected design when:

- files are available;
- redistribution is permitted;
- the environment can upload them.

Typical supported formats:

- `.ttf`
- `.otf`
- `.woff`
- `.woff2`

Rules:

- Do not add random unused fonts.
- Do not replace an approved font with “close enough”.
- Do not redistribute proprietary/system fonts without permission.
- If a required font binary cannot legally/technically be uploaded, retain `Document fonts/` and add a manifest containing exact family, style/weight, source/acquisition requirement, affected roles, and reason binary is absent.
- An unexplained empty fonts folder is incomplete.
- If multiple PA directions use different fonts, map each font to the correct PA direction.

---

# GĐ1 RESPONSIBILITIES

ChatGPT must:

1. understand brief, audience and conversion goal;
2. classify `LANDING_PAGE` or `WEBSITE`;
3. complete GĐ1.0 design research;
4. select relevant references instead of blindly reusing one style;
5. ask how many demo directions are wanted unless already specified;
6. render that number of meaningful previews;
7. present previews clearly;
8. wait for direction selection/approval;
9. infer sitemap/information architecture when applicable;
10. lock the selected art direction;
11. create all required final WEB compositions;
12. create corresponding MOBILE compositions;
13. use approved typography consistently;
14. preserve Vietnamese text/accents correctly;
15. render continuous full-page final PNGs;
16. inspect final outputs before upload;
17. create the exact Drive folders;
18. upload files to the correct folders;
19. verify final uploads by listing Drive folders.

---

# GĐ1 QUALITY / EXIT GATE

Do not enter GĐ2 until applicable checks pass:

```text
[ ] Drive connection verified
[ ] LANDING_PAGE or WEBSITE determined
[ ] GĐ1.0 research completed
[ ] Relevant references selected
[ ] Generic-template risk checked
[ ] Demo-direction count explicitly known
[ ] Requested previews rendered
[ ] Directions are meaningfully different
[ ] User selected/approved direction(s)
[ ] Selected direction locked
[ ] Exact final Drive structure created
[ ] Required WEB final PNGs exist
[ ] Required MOBILE final PNGs exist
[ ] Every final PNG is continuous full-page
[ ] Every WEB PNG is >= 1920px wide
[ ] Every MOBILE PNG is >= 1080px wide
[ ] Final images are sharp/readable
[ ] No collage/presentation board used as final output
[ ] Document fonts/ exists
[ ] Correct font files or explicit font manifest exist
[ ] Drive upload verified
[ ] User/client approved final design direction
```

State transition:

```text
DESIGN
→ DESIGN_RESEARCH_READY
→ DEMO_PREVIEWS_RENDERED
→ DESIGN_DIRECTION_SELECTED
→ FULL_DEMO_READY
→ DESIGN_APPROVED
```

---

# GĐ2 — MASTER UI

## Owner

**ChatGPT**

## Goal

Create an AI-readable structured Master representing the approved design more reliably than screenshots alone.

## Mandatory choice gate

If the user has not selected a strategy, ask:

> Giai đoạn 2 muốn theo hướng nào: **A — Figma Master, B — SVG Master, hay C — cả hai để benchmark?**

Allowed modes:

- `FIGMA_MASTER`
- `SVG_MASTER`
- `BOTH_BENCHMARK`

Do not silently choose.

## Figma Master

Use only when the environment can reliably create/edit/read the required native source. Preserve route frames, typography, geometry, colors/tokens, image placement, components, variants and responsive constraints where meaningful.

## SVG Master

Example:

```text
MASTER/
├── WEB/
│   ├── 01_TrangChu.svg
│   └── ...
├── MOBILE/
│   ├── 01_TrangChu.svg
│   └── ...
├── assets/
└── design-spec.json
```

Preserve canvas size, geometry, typography, colors, opacity, gradients, masks, image placement, grouping and layer order.

## Both benchmark

Create both from the same approved visual and compare fidelity, implementation speed, correction loops, responsive interpretation, asset/font preservation and Codex/Claude comprehension.

Do not declare a permanent winner from one project.

## GĐ2 gate

Master and approved PNGs must describe the same routes/design.

```text
DESIGN_APPROVED → MASTER_READY
```

---

# GĐ3 — UI DECOMPOSITION / UI ASSET PACK

## Owner

**ChatGPT — mandatory owner of visual analysis, production assets, text mapping, font mapping and UI decomposition.**

## Goal

Understand every approved WEB/MOBILE page and Master deeply enough that the implementation agent does not have to guess the visual system.

> Lock visual truth first. Decompose production assets from that truth second.

## Responsibilities

Identify/map:

- routes and sections;
- backgrounds;
- foreground/product images;
- transparent assets;
- vectors;
- logos/wordmarks;
- icons/ornaments;
- masks/alpha/gradients/shadows/glows;
- every visible text string;
- CTA labels;
- exact typography roles;
- reusable UI components;
- desktop/mobile differences;
- design tokens;
- responsive intent;
- interaction intent.

## Source-first rules

When AI/Figma/SVG/PSD or another source exists:

1. inspect it before recreating anything;
2. extract original embedded/vector/alpha/mask resources where possible;
3. do not fake extractable assets by cropping screenshots;
4. do not redraw existing vectors by eye;
5. do not replace approved fonts;
6. inspect source effects before inventing CSS approximations.

When no structured source exists, decomposition from approved PNGs is allowed, but uncertainty must be recorded.

## Typography map

For each visible text role record:

- exact copy;
- route/section;
- semantic role;
- font family/style/weight;
- desktop/mobile sizes;
- line height;
- letter spacing;
- color;
- alignment;
- important line breaks.

## Preferred UI Asset Pack

```text
UI_ASSET_PACK/
├── images/
├── icons/
├── ornaments/
├── logos/
├── fonts/
├── text/
│   ├── content-map.json
│   └── font-map.json
└── spec/
    ├── route-map.json
    ├── section-map.json
    ├── ui-map.json
    ├── desktop-layout.json
    ├── mobile-layout.json
    ├── INTERACTIONS.md
    └── RESPONSIVE.md
```

Prefer SVG for vectors and legal web-font formats where licensing permits. Raster optimization happens only after fidelity is verified.

```text
MASTER_READY → UI_ASSET_PACK_READY
```

---

# GĐ4 — STATIC FRONTEND BUILD

## Owner

**Codex or Claude**

## Mandatory executor gate

If executor is undecided, ask:

> Giai đoạn build giao cho **Codex hay Claude**?

Allowed:

- `CODEX`
- `CLAUDE`

## Inputs

- approved full-page WEB/MOBILE PNGs;
- GĐ2 Master;
- GĐ3 UI Asset Pack;
- route/section maps;
- typography/content maps;
- responsive contract;
- repository constraints.

## Goal

Build the static frontend with maximum visual parity before complex UX/backend work.

The executor must use supplied assets/fonts, preserve live text where appropriate, respect routes, and treat WEB/MOBILE as potentially independent compositions.

Never self-certify “100% pixel-perfect”.

Render every required route at the approved target viewport and compare before PASS.

```text
UI_ASSET_PACK_READY → STATIC_UI_PASS
```

---

# GĐ5 — UX / FRONTEND ENHANCEMENT

## Owner

**Selected Codex or Claude executor unless the user changes it.**

Only after static visual PASS, add project-required:

- hover/focus/active states;
- sticky navigation;
- menu/drawer;
- modal/lightbox;
- slider/carousel;
- tabs/accordion;
- form states;
- scroll behavior;
- motion/animation;
- responsive interaction changes;
- keyboard support;
- reduced-motion handling.

Interaction work must not break the approved visual composition. Re-run visual QA after meaningful UX changes.

```text
STATIC_UI_PASS → UX_PASS
```

---

# GĐ6 — BACKEND / CMS / LOGIC

## Owner

**Codex or Claude**

Add only what the project actually requires:

- CMS;
- API;
- database;
- forms/submissions;
- email;
- uploads;
- content/product/news data;
- search;
- authentication/roles;
- payments;
- integrations;
- dashboards.

A simple landing page may need little or no backend.

`REFERENCE != DEPENDENCY`

```text
UX_PASS → FUNCTIONAL_PASS
```

---

# GĐ7 — QA / PRODUCTION

## Roles

- **ChatGPT:** design authority, visual review, defect identification and acceptance.
- **Codex/Claude:** implementation and fixes.

## QA dimensions

### Visual
Compare approved routes for layout, typography, image identity/crop, spacing, colors, borders/radii, effects and key states. Prefer screenshot overlay/diff over subjective judgment.

### Responsive
Test desktop, tablet where relevant, mobile and narrow-mobile safety.

### Interaction
Verify navigation, keyboard behavior, forms, loading/error/success states, modals, drawers, sliders, focus and reduced motion.

### Accessibility
Check semantic HTML, keyboard support, visible focus, accessible labels/names and automated checks where useful.

### Performance
Check image/font loading, bundle weight, layout shifts, interaction responsiveness and caching.

### Backend/security
Where applicable, validate authorization, server validation, input handling, secrets, API errors, database constraints/migrations and abuse/rate considerations.

```text
FUNCTIONAL_PASS → QA_PASS → PRODUCTION_READY
```

Never claim mathematical visual identity where browser/OS/font rasterization can create unavoidable differences.

---

# SOURCE-OF-TRUTH HIERARCHY

1. approved structured Master/source;
2. approved full-page WEB/MOBILE PNGs;
3. original assets/fonts;
4. browser implementation;
5. derived/helper assets.

Rejected GĐ1 demo directions are not implementation sources of truth.

An original AI/Figma/SVG source may outrank screenshots until approval locks a new Master.

Never treat current browser implementation as truth simply because it already exists.

---

# ANTI-DEAD-END RULES

## NEVER

- skip GĐ1.0 research and render a generic design immediately;
- pretend a repository was inspected when it was not;
- copy one design system blindly across unrelated industries;
- skip the GĐ1 demo-direction choice and silently force one visual direction;
- present trivial recolors as different directions;
- start final full-page production before selection;
- mix rejected directions into approved work without instruction;
- code before identifying visual truth;
- decompose assets before understanding source composition;
- guess an existing source asset;
- crop screenshots to fake extractable assets;
- redraw existing vectors by eye;
- replace approved fonts with “close enough”;
- create presentation boards instead of required final full-page renders;
- omit `Document fonts/`;
- upload low-resolution/broken final images;
- combine multiple routes into one final board;
- let multiple agents independently fix the same area;
- claim pixel-perfect without comparison;
- add backend/framework complexity without requirements;
- publish private client material to this public repository.

## ALWAYS

- verify Drive;
- classify Landing Page or Website;
- research design direction before rendering previews;
- choose references according to domain/brief;
- explicitly know demo-direction count;
- render previews before full-page production;
- get user selection/approval;
- create exact final Drive structure;
- render continuous full-page final images;
- meet resolution minimums;
- include fonts or explicit font manifest;
- verify uploads;
- preserve desktop/mobile intent;
- obtain client design approval;
- lock a Master;
- let ChatGPT own UI decomposition;
- let Codex/Claude own implementation;
- compare at known viewports before PASS;
- retain reusable lessons.

---

# REFERENCE / KNOWLEDGE PACK

Use references, not mandatory dependencies.

## GĐ1 Design Research

- `superdesigndev/superdesign-skill`
- `alexpate/awesome-design-systems`
- `radix-ui/primitives`
- `shadcn-ui/ui`
- `fontsource/fontsource`
- `lucide-icons/lucide`
- `w3c/aria-practices`
- `dequelabs/axe-core`

## UI / Accessibility / Component Architecture

- `shadcn-ui/ui`
- `radix-ui/primitives`
- `storybookjs/storybook`
- `w3c/aria-practices`
- `dequelabs/axe-core`

## Frontend

- `vercel/next.js`
- `tailwindlabs/tailwindcss`
- `TanStack/query`
- `react-hook-form/react-hook-form`
- `colinhacks/zod`
- `lucide-icons/lucide`

## Backend / CMS / Auth

- `supabase/supabase`
- `prisma/prisma`
- `payloadcms/payload`
- `trpc/trpc`
- `better-auth/better-auth`

## Browser / Visual / Production QA

- `microsoft/playwright`
- `mapbox/pixelmatch`
- `GoogleChrome/lighthouse`
- `getsentry/sentry-javascript`

Evaluate stronger maintained alternatives over time.

---

# CONTINUOUS LEARNING & SKILL EVOLUTION POLICY

`webbyLucifer` always operates in a continuous-learning state.

Every project/conversation may reveal evidence-based improvements.

Observe:

- what worked;
- what caused unnecessary iteration;
- where intent was misunderstood;
- where design research improved/worsened the result;
- which reference sources were useful;
- which demo-direction process helped decisions;
- which Master format worked better;
- which extraction/rendering methods were reliable;
- which font/mask/effect methods failed;
- which prompts improved implementation;
- which QA checks found real defects;
- which connectors reduced manual work.

At meaningful milestones form a `LESSONS_LEARNED` summary with successes, failures, root causes, better alternatives, reusable rules, rules to remove, tools/repositories worth evaluating, QA additions and proposed skill changes.

## Public-repository privacy

Never publish:

- private URLs;
- credentials/secrets;
- personal information;
- proprietary client assets;
- private source code;
- unreleased designs;
- confidential business information;
- fonts/assets without redistribution rights.

Generalize lessons instead of leaking project data.

## Improvement deployment gate

When a reusable improvement is found, explain briefly:

- what was learned;
- which section should change;
- expected benefit;
- possible regression.

Do not deploy automatically.

Only after explicit user approval may the AI:

1. inspect the canonical repo;
2. make the smallest generalized change;
3. verify no private client data is included;
4. commit it;
5. push it to the same canonical repository;
6. report the commit SHA.

Canonical repository:

```text
th6322750-stack/webbyLucifer
```

Do not create `-v2`, `-new`, or `-final-final` repositories unless explicitly requested.

---

# SUGGESTED PROJECT STATE

```yaml
project_name: null
project_type: UNDECIDED # LANDING_PAGE | WEBSITE
phase: DESIGN

drive:
  connected: unknown
  writable: unknown
  project_folder: null
  uploads_verified: false

design:
  research_complete: false
  research_summary: null
  references_consulted: []
  demo_direction_count: null
  demo_preview_round: 0
  demo_previews_rendered: false
  selected_directions: []
  direction_locked: false
  sitemap: []
  required_web_pages: []
  required_mobile_pages: []
  admin_required: false
  web_approved: false
  mobile_approved: false
  full_page_verified: false
  resolution_verified: false
  fonts_packaged: false

master:
  mode: UNDECIDED # FIGMA_MASTER | SVG_MASTER | BOTH_BENCHMARK
  ready: false

ui_asset_pack:
  ready: false

implementation:
  executor: UNDECIDED # CODEX | CLAUDE
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
GĐ1 — verify Google Drive
    ↓
classify LANDING_PAGE / WEBSITE
    ↓
GĐ1.0 — research domain, brand, typography, UI patterns and relevant repos
    ↓
form DESIGN_RESEARCH_SUMMARY
    ↓
ask how many demo directions the user wants
    ↓
GĐ1.1 — render meaningful visual previews
    ↓
user selects one / several / hybrid direction
    ↓
lock selected direction
    ↓
render every required final route as separate long full-page WEB/MOBILE PNG
    ↓
WEB >= 1920px wide / MOBILE >= 1080px wide / sharp / natural page height
    ↓
create exact Drive structure + mandatory Document fonts/
    ↓
client approves
    ↓
GĐ2 — user chooses Figma / SVG / Both
    ↓
Master locked
    ↓
GĐ3 — ChatGPT decomposes UI assets, text, fonts, routes and specs
    ↓
UI Asset Pack ready
    ↓
GĐ4 — user chooses Codex / Claude → static frontend
    ↓
visual parity pass
    ↓
GĐ5 — UX/frontend enhancement
    ↓
UX pass
    ↓
GĐ6 — backend/CMS/logic only as required
    ↓
functional pass
    ↓
GĐ7 — ChatGPT QA + executor fixes
    ↓
PRODUCTION READY
    ↓
LESSONS LEARNED
    ↓ explicit user approval
UPDATE THIS SAME PUBLIC REPOSITORY
```
