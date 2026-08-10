# webbyLucifer — `change_web`

> **Mission:** Turn one client brief into approved WEB/MOBILE design files, an AI-readable implementation master, a production UI asset pack, a real frontend/backend implementation, and a verified production-ready website.
>
> **Operating principle:** webbyLucifer continuously learns from real projects. It may propose reusable improvements, but it must never deploy them to the canonical public repository without explicit user approval.

---

## 0. Core operating model

`webbyLucifer` is a gated seven-stage workflow. Every stage has one clear owner.

1. **GĐ1 — DEMO DESIGN** — ChatGPT
2. **GĐ2 — MASTER UI** — ChatGPT
3. **GĐ3 — UI DECOMPOSITION / UI ASSET PACK** — ChatGPT
4. **GĐ4 — STATIC FRONTEND BUILD** — Codex or Claude
5. **GĐ5 — UX / FRONTEND ENHANCEMENT** — Codex or Claude
6. **GĐ6 — BACKEND / CMS / LOGIC** — Codex or Claude
7. **GĐ7 — QA / PRODUCTION** — ChatGPT reviews; executor fixes

The default input is one client brief. Ask only questions that genuinely block a usable result, except for mandatory gates explicitly defined in this skill.

---

# GĐ1 — DEMO DESIGN

## Owner

**ChatGPT**

## Goal

From the client brief, references, logo, imagery, copy, colors, or even a rough idea, create multiple possible visual directions when requested, let the user choose the best direction(s), then create the complete client-facing WEB/MOBILE design package for approval.

GĐ1 is not allowed to jump directly from brief to one arbitrary final design without first passing the demo-direction gate below.

---

## Mandatory Google Drive connection gate

Before any GĐ1 production work:

1. Verify that Google Drive is connected by performing a minimal read.
2. Verify that Drive is writable before promising automatic packaging.
3. When Drive is connected and writable, create the required folders automatically.
4. If Drive is unavailable, disconnected, or read-only, stop packaging and ask the user to connect or restore Drive access.
5. Never claim that a Drive folder or upload exists unless the connector confirms it.

The Drive folder structure is the **final delivery workspace**, not the place where every rough visual experiment must be stored.

---

## Mandatory project-type gate

Before final rendering, classify the request as exactly one of:

- `LANDING_PAGE`
- `WEBSITE`

If the brief clearly determines the type, classify it automatically.

If genuinely ambiguous, stop and ask exactly:

> Thiết kế này là **Landing Page một trang** hay **Website nhiều trang**?

Do not treat a multi-page website as one landing page. Do not invent unnecessary subpages for a landing page.

---

# GĐ1.1 — MANDATORY DEMO-DIRECTION PREVIEW GATE

## Purpose

Before spending time rendering the full long WEB/MOBILE package, ChatGPT must let the user see and choose the visual direction first.

The user may want one safe direction or several alternative directions to compare internally or show to the client.

## Mandatory question

Unless the user already explicitly supplied the number in the current request, ChatGPT MUST ask:

> **Bạn muốn mình render trước bao nhiêu phương án giao diện demo để chọn? 1, 2, 3 hay số khác?**

Do not silently default to exactly one design.

If the user already said, for example, “cho tôi 3 phương án”, do not ask the same question again; use `demo_direction_count: 3`.

## What counts as a distinct demo direction

Each requested direction must be meaningfully different in art direction, not just a trivial recolor.

Possible differences may include:

- composition and visual hierarchy;
- typography pairing;
- Hero structure;
- image treatment;
- spacing rhythm;
- navigation treatment;
- card/component language;
- ornament/effect style;
- density and content presentation;
- brand mood such as minimal, luxury, editorial, heritage, technology, playful, premium, etc.

Do not pretend that three nearly identical color variants are three design directions.

## Preview rendering contract

For each requested direction, create a **visual preview** before creating final full-page files.

The preview must be large and clear enough for the user to judge the design direction.

For a `LANDING_PAGE`, each direction should normally preview enough of the page to establish the system, such as:

```text
HEADER
↓
HERO
↓
1–2 representative content sections
```

For a `WEBSITE`, each direction should normally preview the primary/home page art direction and enough shared components to judge how the rest of the site will look.

Where mobile treatment materially affects the concept, include a mobile preview as well.

Preview images are **selection artifacts**, not final GĐ1 delivery assets. Therefore they do not replace the required long full-page files and should not be mistaken for the final Drive package.

## Mandatory presentation to the user

Label previews clearly:

```text
PHƯƠNG ÁN 01 — <short direction name>
PHƯƠNG ÁN 02 — <short direction name>
PHƯƠNG ÁN 03 — <short direction name>
...
```

For each direction, provide only a short explanation of the design logic and major tradeoff. Let the image do the main work.

Then ask the user to choose:

- one direction to develop;
- multiple directions to develop further;
- or request a hybrid of specific aspects from several directions.

Example:

> Chọn PA01, PA02, PA03; hoặc nói “lấy bố cục PA01 + font PA02 + Hero PA03”.

## Selection lock

Do NOT begin the expensive final full-page rendering step until the user has selected or approved at least one direction.

Allowed states:

```text
DEMO_DIRECTIONS_REQUESTED
↓
DEMO_PREVIEWS_RENDERED
↓
USER_DIRECTION_SELECTED
↓
FULL_DEMO_PRODUCTION
```

If the user requests another exploration round, create a new preview round instead of pretending the old direction was approved.

## Multiple directions for client presentation

If the user wants several selected directions developed into complete demos for the client, this is allowed.

Do not change the required root Drive folder names. Keep the canonical folders and distinguish variants by filename.

Example for a landing page with two complete client demo directions:

```text
TEN-DU-AN/
│
├── bản WEB/
│   ├── PA01_WEB_TenDuAn.png
│   └── PA02_WEB_TenDuAn.png
│
├── bản MOBILE/
│   ├── PA01_MOBILE_TenDuAn.png
│   └── PA02_MOBILE_TenDuAn.png
│
└── Document fonts/
    └── ...
```

If only one direction is selected, use the normal canonical names without a `PAxx_` prefix.

After the client chooses the winning direction, that selected direction becomes the visual acceptance candidate and subsequent phases must not silently mix assets/styles from rejected directions.

---

## GĐ1-A — LANDING_PAGE output contract

A landing page is one long route from Header to Footer.

For one selected direction, create exactly this client-facing Drive structure:

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

### Mandatory landing render format

`WEB_TenDuAn.png` must be one continuous vertical full-page image:

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

`MOBILE_TenDuAn.png` must also be one continuous vertical full-page image from Header to Footer using the real mobile composition.

### Forbidden landing outputs

Never use any of the following as the final GĐ1 output:

- a presentation board;
- a collage;
- multiple mini screenshots placed on one canvas;
- a desktop/mobile mockup board;
- a poster summarizing sections;
- only the first viewport;
- a cropped Hero instead of the full page;
- several disconnected screen fragments;
- a short, compressed, “vón cục” image that does not represent the entire page length.

The final reference behavior is a naturally long website screenshot, not a portfolio presentation sheet.

---

## GĐ1-B — WEBSITE output contract

A website contains multiple routes/pages.

Before final full-page rendering:

1. Infer a concise sitemap/page map from the client brief.
2. Identify all required primary user-facing pages.
3. Include detail pages when the product requires them, such as product detail, property detail, article detail, project detail, checkout, or contact.
4. Add Admin/CMS screens only when the brief explicitly requires them.
5. Keep one coherent visual system across all pages.
6. Apply the direction approved in GĐ1.1 consistently across the whole sitemap.

Create this client-facing Drive structure:

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

### Mandatory website render format

Every route must be exported as its own separate continuous full-page PNG.

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

Every page image must run from that page’s Header/navigation area through all page content to its Footer or natural page ending.

### Forbidden website outputs

Never combine all final website pages into one promotional board such as:

```text
[Homepage desktop] [Detail desktop] [Listing desktop]
[Mobile screen 1]  [Mobile screen 2] [Admin dashboard]
```

That style may be useful as an optional portfolio presentation, but it is not the GĐ1 production output.

Never replace per-route files with one image named `TatCaGiaoDien.png`.

---

## Mandatory full-page and resolution contract

All **final GĐ1 PNGs uploaded to Drive** must be:

- full-page vertical renders;
- high-resolution;
- readable at 100% zoom;
- free of blur, broken text, pixelation, compression artifacts, and accidental scaling damage;
- exported from the final structured composition, not enlarged from a low-resolution preview.

### WEB resolution

Every final WEB design PNG must be at least:

```text
width: 1920 px
height: natural full-page height
```

Examples:

```text
1920 × 6000
1920 × 8500
1920 × 12000
```

The height must follow the actual page. Never squash a long page to fit a short canvas.

### MOBILE resolution

Every final MOBILE design PNG must be at least:

```text
width: 1080 px
height: natural full-page height
```

Examples:

```text
1080 × 8000
1080 × 12000
1080 × 16000
```

The mobile image must be a true mobile composition, not a desktop image resized to 1080px.

### Resolution hard failures

GĐ1 fails if any final delivered image is:

- preview-sized;
- blurry;
- visibly pixelated;
- stretched from a smaller source;
- aggressively compressed;
- cropped before the page ends;
- a first-screen-only screenshot;
- a collage/presentation board;
- unreadable when opened normally in Drive.

“Full HD” in this skill means at least **1920px-wide WEB** and **1080px-wide MOBILE**, while preserving the entire natural page height.

Important distinction:

- GĐ1.1 preview renders exist only to choose art direction.
- Final Drive renders must always satisfy this full-page high-resolution contract.

---

## Mandatory `Document fonts/` contract

`Document fonts/` must always exist in every final GĐ1 package.

It must not be silently omitted.

Place the actual font files used by the selected design into this folder when:

- the files are available;
- redistribution is permitted;
- the environment can upload them.

Supported examples include:

- `.ttf`
- `.otf`
- `.woff`
- `.woff2`

Do not add random unused fonts.

Do not substitute a different font after design approval.

Do not redistribute proprietary/system fonts without permission.

When an approved font cannot legally or technically be uploaded, keep `Document fonts/` and add a clear manifest/note containing:

- exact font family;
- exact style/weight;
- source or acquisition requirement;
- affected design roles;
- reason the binary was not included.

A missing folder is never acceptable. An empty unexplained folder is not considered complete.

If multiple complete demo directions use different font families, the font manifest must map each font to the relevant `PAxx` direction so rejected fonts are not accidentally carried into production later.

---

## GĐ1 design responsibilities

ChatGPT must:

1. understand the brief and audience;
2. classify `LANDING_PAGE` or `WEBSITE`;
3. ask how many demo directions the user wants unless already specified;
4. render the requested preview directions;
5. present the preview directions clearly for selection;
6. wait for the user to choose/approve direction(s);
7. infer the correct information architecture;
8. define and lock the selected art direction;
9. create all required final WEB compositions;
10. create all corresponding final MOBILE compositions;
11. use the final approved font choices consistently;
12. preserve Vietnamese text and accents correctly;
13. render continuous full-page PNGs;
14. visually inspect every final output before upload;
15. create the exact Drive folders;
16. upload every final file to the correct folder;
17. verify the uploads by listing the resulting Drive folders.

---

## GĐ1 quality inspection

Before final upload, inspect for:

- the user was never given a demo-direction choice;
- requested preview count was not produced;
- “different” previews are merely trivial recolors;
- a rejected direction leaked into the selected final design;
- garbled or misspelled text;
- broken Vietnamese accents;
- incorrect fonts;
- clipped sections;
- duplicated imagery;
- unfinished placeholders;
- weak contrast;
- inconsistent desktop/mobile content;
- missing pages from the sitemap;
- missing font files or font manifest;
- image width below the required minimum;
- accidental collage or presentation-board composition.

---

## GĐ1 exit gate

Do not enter GĐ2 until all applicable checks pass:

```text
[ ] Drive connection verified
[ ] Project classified as LANDING_PAGE or WEBSITE
[ ] Demo-direction count explicitly known
[ ] Requested demo previews rendered
[ ] User selected/approved at least one direction
[ ] Selected direction locked for final production
[ ] Exact final Drive folder structure created
[ ] All required WEB page PNGs exist
[ ] All required MOBILE page PNGs exist
[ ] Every final PNG is full-page and vertically continuous
[ ] Every final WEB PNG is at least 1920px wide
[ ] Every final MOBILE PNG is at least 1080px wide
[ ] Every final image is sharp and readable
[ ] No collage/presentation-board used as final output
[ ] Document fonts/ exists
[ ] Correct font files or an explicit font manifest exist
[ ] Drive upload verified by listing folders
[ ] User/client approved the design direction
```

State transition:

```text
DESIGN
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

Create an AI-readable structured master that preserves the approved design and gives the implementation agent more reliable information than screenshots alone.

## Mandatory choice gate

If the user has not selected a strategy, stop and ask:

> Bạn muốn Giai đoạn 2 đi theo hướng nào: **A — Figma Master, B — SVG Master, hay C — Cả hai để benchmark độ ổn định?**

Allowed modes:

- `FIGMA_MASTER`
- `SVG_MASTER`
- `BOTH_BENCHMARK`

Do not silently choose.

## Strategy A — Figma Master

Use Figma only when the environment can reliably create, edit, and read the source.

Organize:

- all WEB route frames;
- all MOBILE route frames;
- reusable components;
- variants/states;
- typography;
- colors/tokens;
- images and vectors;
- Auto Layout/constraints where meaningful.

## Strategy B — SVG Master

Create structured masters for all approved routes:

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

For a landing page, WEB and MOBILE may each contain one master file.

Preserve canvas size, geometry, typography, colors, opacity, gradients, masks, image placement, grouping, and layer order.

## Strategy C — Both benchmark

Create both representations from the same approved design and compare:

- visual fidelity;
- implementation speed;
- correction loops;
- responsive interpretation;
- asset/font preservation;
- Codex/Claude comprehension;
- long-term stability.

Do not declare a permanent winner after one project.

## GĐ2 consistency gate

The Master and the approved full-page PNGs must describe the same routes and visual design.

Render the Master back to canonical WEB/MOBILE sizes and compare before handoff.

```text
DESIGN_APPROVED → MASTER_READY
```

---

# GĐ3 — UI DECOMPOSITION / UI ASSET PACK

## Owner

**ChatGPT — mandatory owner for UI analysis, asset decomposition, typography mapping, and production visual resources.**

## Goal

Understand every approved WEB/MOBILE page and the GĐ2 Master deeply enough to create a production-ready UI system.

> Lock visual truth first. Then decompose production assets from that truth. Never guess assets before source analysis is complete.

## Responsibilities

Identify and map:

- all routes and sections;
- visual layers;
- backgrounds;
- foreground/product images;
- transparent assets;
- vectors;
- logos and wordmarks;
- icons and ornaments;
- gradients, masks, alpha, shadows, glows, and effects;
- every visible text string;
- CTA labels;
- exact font roles;
- reusable components;
- desktop/mobile differences;
- design tokens;
- responsive behavior;
- interaction intent.

## Source-first rules

When AI/Figma/SVG/PSD or another source exists:

1. inspect it before recreating anything;
2. extract original embedded/vector/alpha/mask resources when possible;
3. do not fake extractable assets by cropping screenshots;
4. do not redraw existing vectors by eye;
5. do not replace approved fonts with similar fonts;
6. inspect the source effect stack before inventing CSS approximations.

When no structured source exists, decomposition from approved PNGs is permitted, but uncertainty must be recorded.

## Required typography map

For every visible text role record:

- exact copy;
- route and section;
- semantic role;
- font family;
- style/weight;
- desktop size;
- mobile size;
- line height;
- letter spacing;
- color;
- alignment;
- significant line breaks.

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

Prefer SVG for vectors, WebP/AVIF for raster imagery after visual QA, alpha-capable formats for transparency, and legal web font formats where licensing permits.

## GĐ3 exit gate

The implementation agent must not need to guess primary asset identity, visible copy, font roles, routes, or desktop/mobile composition.

```text
MASTER_READY → UI_ASSET_PACK_READY
```

---

# GĐ4 — STATIC FRONTEND BUILD

## Owner

**Codex or Claude**

## Mandatory executor gate

If no executor is selected, stop and ask:

> Giai đoạn build giao cho **Codex hay Claude**?

Allowed values:

- `CODEX`
- `CLAUDE`

## Inputs

- approved full-page WEB/MOBILE PNGs;
- GĐ2 Master;
- GĐ3 UI Asset Pack;
- route and section maps;
- typography/content maps;
- responsive contract;
- repository constraints.

## Goal

Build the static frontend with maximum visual parity before complex UX or backend work.

The executor must use supplied assets and approved fonts, preserve live text where appropriate, respect route structure, and treat WEB/MOBILE as potentially independent compositions.

Never hide visual errors behind arbitrary CSS filters or blends unless they are source-derived.

Never self-certify “100% pixel-perfect”.

## Static gate

Render every required route at its approved reference viewport and compare against the approved PNG.

Do not enter GĐ5 while material visual mismatch remains.

```text
UI_ASSET_PACK_READY → STATIC_UI_PASS
```

---

# GĐ5 — UX / FRONTEND ENHANCEMENT

## Owner

**The selected Codex or Claude executor unless the user changes it.**

Add only required:

- hover/focus/active states;
- sticky navigation;
- menu/drawer;
- modal/lightbox;
- slider/carousel;
- tabs/accordion;
- form states;
- scroll behavior;
- animation/motion;
- responsive interaction changes;
- keyboard support;
- reduced-motion handling.

Interaction work must not break approved visual composition. Re-run route-level visual QA after meaningful UX changes.

```text
STATIC_UI_PASS → UX_PASS
```

---

# GĐ6 — BACKEND / CMS / LOGIC

## Owner

**Codex or Claude**

Add only capabilities required by the project:

- CMS;
- API;
- database;
- forms and submissions;
- email;
- uploads;
- content/news/product data;
- search;
- authentication and roles;
- payments;
- integrations;
- dashboards.

A landing page may require little or no backend.

`REFERENCE != DEPENDENCY`

Do not install systems merely because the skill knows them.

```text
UX_PASS → FUNCTIONAL_PASS
```

---

# GĐ7 — QA / PRODUCTION

## Roles

- **ChatGPT:** design authority, review, comparison, defect identification, acceptance.
- **Codex/Claude:** implementation and fixes.

## QA dimensions

### Visual

Compare every approved route for layout, typography, image identity/crop, spacing, colors, borders/radii, effects, and key states. Prefer screenshot overlays and visual diff over subjective statements.

### Responsive

Test desktop, tablet when relevant, mobile, and narrow-mobile safety.

### Interaction

Verify navigation, keyboard behavior, forms, loading/error/success states, modals, drawers, sliders, focus behavior, and reduced motion.

### Accessibility

Use semantic HTML, keyboard support, visible focus, accessible labels/names, and automated checks where useful.

### Performance

Check image/font loading, bundle weight, layout shifts, interaction responsiveness, caching, and project-appropriate performance indicators.

### Backend/security

When applicable, validate authorization, server validation, input handling, secrets, API errors, database constraints/migrations, and abuse/rate considerations.

```text
FUNCTIONAL_PASS → QA_PASS → PRODUCTION_READY
```

Do not claim mathematical identity where browser/OS/font rasterization can cause unavoidable differences.

---

# Source-of-truth hierarchy

1. approved structured Master/source;
2. approved full-page WEB/MOBILE PNGs;
3. original assets and fonts;
4. browser implementation;
5. derived/helper assets.

Rejected GĐ1 demo directions are not implementation sources of truth.

An original AI/Figma/SVG source may outrank screenshots until approval locks a new Master.

Never treat the current browser implementation as truth merely because it already exists.

---

# Anti-dead-end rules

## NEVER

- skip the GĐ1 demo-direction choice and silently force one arbitrary visual direction;
- present trivial recolors as meaningfully different demo directions;
- start final full-page production before at least one preview direction is selected;
- mix rejected visual directions into an approved direction without explicit instruction;
- code before identifying visual truth;
- decompose assets before understanding the source composition;
- guess an existing source asset;
- crop screenshots to fake extractable assets;
- redraw existing vectors by eye;
- replace an approved font with “close enough”;
- create presentation boards instead of required final full-page renders;
- omit `Document fonts/`;
- upload low-resolution or broken final images;
- combine multiple routes into one final board;
- let multiple agents independently fix the same area;
- claim pixel-perfect without comparison;
- add backend/framework complexity without requirements;
- publish private client material to this public repository.

## ALWAYS

- verify Drive;
- classify Landing Page or Website;
- explicitly know the desired demo-direction count;
- render previews before expensive final full-page production;
- get user selection/approval of the design direction;
- create the exact final Drive structure;
- render final full-page continuous images;
- meet minimum resolution;
- include fonts or an explicit font manifest;
- verify uploads;
- define source of truth;
- preserve desktop/mobile intent;
- obtain client design approval;
- lock a Master;
- let ChatGPT own UI decomposition;
- let Codex/Claude own implementation;
- compare at known viewports before PASS;
- retain reusable lessons.

---

# Reference / knowledge pack

Use as references, not mandatory dependencies.

## UI / accessibility / component architecture

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

## Backend / CMS / auth

- `supabase/supabase`
- `prisma/prisma`
- `payloadcms/payload`
- `trpc/trpc`
- `better-auth/better-auth`

## Browser / visual / production QA

- `microsoft/playwright`
- `mapbox/pixelmatch`
- `GoogleChrome/lighthouse`
- `getsentry/sentry-javascript`

Evaluate stronger maintained alternatives over time.

---

# Continuous Learning & Skill Evolution Policy

`webbyLucifer` always operates in a continuous-learning state.

Every project and conversation may reveal evidence-based improvements.

Observe:

- what worked;
- what caused unnecessary iteration;
- where intent was misunderstood;
- where handoff failed;
- which demo-direction process helped the user/client decide faster;
- which Master format worked better;
- which extraction/rendering methods were reliable;
- which font/mask/effect methods failed;
- which prompts improved implementation;
- which QA checks found real defects;
- which connectors removed manual work.

At meaningful milestones, form a `LESSONS_LEARNED` summary containing successes, failures, root causes, better alternatives, reusable rules, rules to remove, tools worth evaluating, QA additions, and proposed skill changes.

## Public-repository privacy

Never publish:

- private URLs;
- credentials or secrets;
- personal information;
- proprietary client assets;
- private source code;
- unreleased designs;
- confidential business information;
- font/assets without redistribution rights.

Generalize the lesson instead of leaking project data.

## Improvement deployment gate

When a reusable improvement is found, explain briefly:

- what was learned;
- what section should change;
- expected benefit;
- possible regression.

Do not deploy automatically.

Only after explicit user approval may the AI:

1. inspect the canonical repo;
2. make the smallest appropriate generalized change;
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

# Suggested project state

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

# Final operating summary

```text
CLIENT BRIEF
    ↓
GĐ1 — verify Drive
    ↓
classify LANDING_PAGE or WEBSITE
    ↓
ASK: user wants how many demo directions?
    ↓
ChatGPT renders visual preview directions
    ↓
user selects one / several / hybrid direction
    ↓
lock selected direction
    ↓
render every required final route as separate full-page WEB/MOBILE PNG
    ↓
1920px WEB + 1080px MOBILE minimum, sharp and continuous
    ↓
create exact Drive structure + mandatory Document fonts/
    ↓ client approves
GĐ2 — user chooses Figma / SVG / Both
    ↓ Master locked
GĐ3 — ChatGPT decomposes UI assets, text, fonts, routes, and specs
    ↓ UI Asset Pack ready
GĐ4 — user chooses Codex / Claude → static frontend
    ↓ visual parity pass
GĐ5 — UX/frontend enhancement
    ↓ UX pass
GĐ6 — backend/CMS/logic only as required
    ↓ functional pass
GĐ7 — ChatGPT QA + executor fixes
    ↓
PRODUCTION READY
    ↓
LESSONS LEARNED
    ↓ explicit user approval
UPDATE THIS SAME PUBLIC REPOSITORY
```
