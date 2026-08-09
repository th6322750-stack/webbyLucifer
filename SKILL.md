# webbyLucifer — `change_web`

> **Mission:** Turn a single client brief into a client-approved WEB/MOBILE design, an AI-readable implementation master, a production UI asset pack, a real frontend/backend implementation, and a verified production-ready website.
>
> **Operating principle:** webbyLucifer is continuously evolving. Learn from every real project, propose reusable improvements, but never persist or deploy those improvements to this canonical public repository without explicit user approval.

---

## 0. Core operating model

`webbyLucifer` is a staged workflow. Each stage has a clear owner and an entry/exit gate so different AIs do not overlap, guess, or rewrite the same work at the same time.

### Stage map

1. **GĐ1 — DEMO DESIGN** — Owner: ChatGPT
2. **GĐ2 — MASTER UI** — Owner: ChatGPT
3. **GĐ3 — UI DECOMPOSITION / UI ASSET PACK** — Owner: ChatGPT
4. **GĐ4 — STATIC FRONTEND BUILD** — Owner: Codex or Claude
5. **GĐ5 — UX / FRONTEND ENHANCEMENT** — Owner: Codex or Claude
6. **GĐ6 — BACKEND / CMS / LOGIC** — Owner: Codex or Claude
7. **GĐ7 — QA / PRODUCTION** — ChatGPT reviews, executor fixes

The default end-to-end input should be **one client brief**. The skill should ask only for information that is truly blocking progress.

---

# GĐ1 — DEMO DESIGN

## Owner

**ChatGPT**

## Goal

From the client's brief, references, logo, images, copy, colors, or even a very rough idea, design and render a complete WEB and MOBILE visual demo for client approval.

## Mandatory Drive connection gate

Before starting GĐ1 production work:

1. Check whether Google Drive is connected and writable.
2. If connected, use it as the project delivery workspace.
3. If not connected, tell the user that Drive must be connected if they want automatic folder creation/upload. Do not pretend the folders were created.
4. Do not require the user to manually create the folder structure when Drive write access is available.

## Project folder structure on Drive

Create:

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
    ├── font1.ttf / .otf / .woff2
    └── ...
```

Client-facing GĐ1 delivery is intentionally minimal. Do not expose source code, GitHub, CMS, Figma source, or internal production assets unless explicitly requested.

## Input tolerance

The client may provide any subset of:

- a short description;
- industry/business type;
- a logo;
- brand colors;
- rough copy;
- screenshots;
- reference websites;
- product images;
- existing brand assets;
- no formal design source at all.

Do not assume `.ai`, Figma, PSD, Sketch, XD, or a complete asset library exists.

## GĐ1 responsibilities

ChatGPT must:

1. understand the brief and intended audience;
2. infer the appropriate website type and information hierarchy;
3. choose a coherent visual direction;
4. create a WEB composition;
5. create a MOBILE composition as a real mobile layout, not merely a shrunken desktop;
6. use real/client-approved fonts where available;
7. render final WEB/MOBILE PNGs;
8. self-review the two renders for consistency before delivery;
9. upload the outputs into the Drive folder structure when Drive is available.

## GĐ1 exit gate

Do not enter GĐ2 until the user/client explicitly approves the design direction.

State transition:

```text
DESIGN -> DESIGN_APPROVED
```

---

# GĐ2 — MASTER UI

## Owner

**ChatGPT**

## Goal

Create an AI-readable, structured master source that preserves the approved visual design and gives an implementation agent something better than a screenshot to follow.

## Mandatory choice gate

Before doing any GĐ2 work, determine whether the user has explicitly selected a master strategy.

Allowed modes:

- `FIGMA_MASTER`
- `SVG_MASTER`
- `BOTH_BENCHMARK`

If no mode has been selected, **STOP and ask exactly this decision**:

> Bạn muốn Giai đoạn 2 đi theo hướng nào: **A — Figma Master, B — SVG Master, hay C — Cả hai để benchmark độ ổn định?**

Do not infer or silently choose a direction.

## Strategy A — Figma Master

Use Figma as structured design truth when the environment can create/edit/read the needed Figma source reliably.

Expected structure should clearly separate:

- WEB frame(s);
- MOBILE frame(s);
- reusable components;
- typography;
- colors/tokens;
- images/assets;
- states/variants where appropriate.

The approved PNGs remain the visual acceptance references.

## Strategy B — SVG Master

Use structured SVG as the machine-readable visual master.

Expected output:

```text
MASTER/
├── WEB_TenDuAn.svg
├── MOBILE_TenDuAn.svg
├── assets/
└── design-spec.json     # optional but preferred for complex projects
```

The SVG/master must preserve, where technically appropriate:

- canvas dimensions;
- x/y geometry;
- width/height;
- font family;
- font size;
- line height;
- color;
- opacity;
- gradients;
- clipping/masks;
- image placement;
- z/layer order.

## Strategy C — Both benchmark

Produce both Figma and SVG representations when practical, then compare:

- visual fidelity;
- implementation speed;
- number of corrections required;
- responsive interpretability;
- asset preservation;
- Codex/Claude comprehension;
- long-term stability.

Do not permanently declare one method superior until repeated projects provide evidence.

## GĐ2 consistency rule

The MASTER and the client-approved WEB/MOBILE PNGs must describe the **same design**.

Never create a new interpretation in GĐ2 just because the master format is different.

## GĐ2 exit gate

```text
DESIGN_APPROVED -> MASTER_READY
```

---

# GĐ3 — UI DECOMPOSITION / UI ASSET PACK

## Owner

**ChatGPT — mandatory owner for all UI asset decomposition and visual source analysis.**

This stage exists because an implementation agent may be able to reproduce a static composition from `.ai`, SVG, Figma, or screenshots, but a production website still needs real reusable assets, real text, real fonts, real components, and explicit responsive/UX intent.

## Goal

Understand the approved `WEB.png` + `MOBILE.png` and the GĐ2 master deeply enough to decompose the visual into a production-ready UI system.

## Critical rule learned from failure

The problem is **not** that assets need to be extracted/rendered. The problem is extracting/rendering them **before the authoritative source and composition are understood**.

Therefore:

> **Lock visual truth first. Then decompose production assets from that truth. Never guess production assets before source analysis is complete.**

## GĐ3 responsibilities

ChatGPT must identify and map:

- website sections;
- visual layers;
- background images;
- foreground/product images;
- transparent images;
- vectors;
- logos/wordmarks;
- icons;
- ornaments;
- gradients;
- masks/alpha;
- shadows/glows/effects;
- typography;
- all visible text;
- CTA labels;
- card/section structure;
- desktop/mobile differences;
- reusable components;
- design tokens.

## Source-first asset rule

If a real source exists (AI/Figma/SVG/PSD/etc.):

1. inspect the source before recreating anything;
2. extract the original embedded/vector/alpha/mask asset when possible;
3. do not crop a screenshot to fake an asset when the real source contains it;
4. do not redraw a logo/icon/ornament by eye if the original vector exists;
5. do not substitute a similar font when the approved font exists;
6. do not invent masks/effects until the original effect stack has been inspected.

If no structured source exists, decomposition from the approved PNGs is allowed, but uncertainty must be documented.

## Typography map

Create a definitive mapping for each visible text role:

- exact copy;
- semantic role (heading/body/eyebrow/CTA/label/etc.);
- font family;
- weight/style;
- desktop size;
- mobile size;
- line height;
- letter spacing;
- color;
- alignment;
- wrapping/line breaks when visually significant.

Do not bake normal editable UI text into images unless the artwork itself requires it.

## Preferred UI Asset Pack

```text
UI_ASSET_PACK/
├── images/
│   ├── hero-background.webp
│   ├── hero-product.webp
│   └── ...
├── icons/
│   └── *.svg
├── ornaments/
│   └── *.svg / transparent web assets
├── logos/
│   ├── logo-mark.svg
│   ├── logo-wordmark.svg
│   └── ...
├── fonts/
│   └── approved web-usable font files
├── text/
│   ├── content-map.json
│   └── font-map.json
└── spec/
    ├── section-map.json
    ├── ui-map.json
    ├── desktop-layout.json
    ├── mobile-layout.json
    ├── INTERACTIONS.md
    └── RESPONSIVE.md
```

Exact file names may vary by project; the conceptual separation should remain.

## Asset format guidance

Prefer, when appropriate:

- logos/icons/line art -> SVG;
- photographic/raster images -> WebP/AVIF with quality chosen by visual QA;
- transparency -> SVG, PNG, or alpha-capable WebP depending on source and quality needs;
- fonts -> web-appropriate legal formats, commonly WOFF2 where licensing permits;
- motion/video -> MP4/WebM/Lottie only when the approved design/UX requires it.

## GĐ3 UX contract

Static design does not fully specify behavior. ChatGPT must produce explicit behavior contracts for anything not obvious from the static image.

Examples:

```text
HEADER
- sticky behavior
- menu open/close behavior
- desktop/mobile differences

GALLERY
- click -> lightbox
- mobile swipe
- keyboard behavior

FORM
- validation
- loading
- success
- error
```

## GĐ3 responsive contract

Document:

- major layout breakpoints or behavior ranges;
- components that reflow vs. components that use independent mobile composition;
- card/grid changes;
- type scaling behavior;
- media crop/position behavior;
- hidden/shown elements;
- navigation transformation.

## GĐ3 exit gate

GĐ3 only passes when the implementation agent can build without guessing the identity of primary assets, visible text, font roles, or the intended desktop/mobile composition.

```text
MASTER_READY -> UI_ASSET_PACK_READY
```

---

# GĐ4 — STATIC FRONTEND BUILD

## Owner

**Codex or Claude**

## Mandatory executor choice gate

Before implementation, if the user has not selected the executor, **STOP and ask**:

> Giai đoạn build giao cho **Codex hay Claude**?

Allowed values:

- `CODEX`
- `CLAUDE`

Never silently select an implementation agent.

## Inputs

Executor receives:

- approved WEB/MOBILE PNGs;
- GĐ2 MASTER;
- GĐ3 UI_ASSET_PACK;
- typography/content maps;
- responsive contract;
- any existing repository/project constraints.

## Goal

Build the static frontend with maximum visual parity **before adding complex UX or backend behavior**.

## Implementation rules

The executor must:

- use provided production assets instead of inventing replacements;
- use approved fonts;
- preserve live text where appropriate;
- respect source geometry and composition;
- treat WEB and MOBILE as potentially independent compositions;
- not hide visual mismatches behind arbitrary CSS filters/blends unless they are source-derived;
- not self-certify “100% pixel-perfect”.

## Static visual gate

Render browser screenshots at the approved reference viewports and compare them against the approved design.

Do not move to GĐ5 while material visual mismatch remains.

```text
UI_ASSET_PACK_READY -> STATIC_UI_PASS
```

---

# GĐ5 — UX / FRONTEND ENHANCEMENT

## Owner

**Same selected executor unless the user explicitly changes it.**

## Goal

Turn the visually correct static frontend into a complete interactive frontend using the GĐ3 UX/responsive contracts.

Potential work includes only what the project requires:

- hover/focus/active states;
- sticky behavior;
- menu/drawer;
- modal/lightbox;
- slider/carousel;
- tabs/accordion;
- forms and UI states;
- scroll behavior;
- animation/motion;
- responsive interaction changes;
- keyboard accessibility;
- reduced-motion handling.

## Rule

Do not let animation or interaction changes break approved visual composition. Re-run visual QA after significant UX changes.

```text
STATIC_UI_PASS -> UX_PASS
```

---

# GĐ6 — BACKEND / CMS / LOGIC

## Owner

**Codex or Claude**

## Goal

Add only the backend capabilities required by the project.

Possible systems:

- CMS;
- API;
- database;
- forms/submissions;
- email;
- uploads;
- blog/news;
- product data;
- search;
- authentication;
- roles/permissions;
- payments;
- integrations;
- dashboards.

A simple landing page may have little or no backend. Do not add backend complexity just because the skill knows how.

## Rule

`REFERENCE != DEPENDENCY`

Knowledge of a library/repository does not mean it must be installed.

```text
UX_PASS -> FUNCTIONAL_PASS
```

---

# GĐ7 — QA / PRODUCTION

## Roles

- **ChatGPT:** design authority, comparison, review, defect identification, acceptance decision.
- **Codex/Claude:** implementation/fixes.

Do not allow both roles to modify the same problem concurrently without a clear owner.

## QA dimensions

### Visual QA

Compare approved design vs. implementation:

- layout;
- typography;
- image identity/crop;
- spacing;
- colors;
- borders/radii;
- responsive behavior;
- visual effects;
- key interaction states.

Use screenshot/overlay/diff methods where possible rather than subjective “looks close”.

### Responsive QA

Test representative widths for:

- desktop;
- tablet where relevant;
- mobile;
- narrow mobile safety.

### Interaction QA

Verify:

- navigation;
- keyboard operation;
- forms;
- loading/error/success states;
- modals/drawers;
- sliders/lightboxes;
- focus behavior;
- reduced motion when relevant.

### Accessibility QA

Use semantic HTML, keyboard support, visible focus, accessible names/labels, and automated accessibility checks where useful.

### Performance QA

Check image/font loading, bundle weight, layout shifts, interaction responsiveness, caching, and core performance indicators appropriate to the project.

### Backend/security QA

When a backend exists, validate:

- authentication/authorization boundaries;
- server-side validation;
- input sanitization/normalization as appropriate;
- secrets handling;
- API errors;
- database constraints/migrations;
- rate/abuse considerations where relevant.

## Final exit

```text
FUNCTIONAL_PASS -> QA_PASS -> PRODUCTION_READY
```

Do not claim mathematical 100% identity when browser/OS/font rendering can cause unavoidable rasterization differences. The acceptance target is source-locked composition plus verified visual parity within renderer constraints.

---

# Source-of-truth hierarchy

At any point, explicitly identify the authoritative source.

General hierarchy when applicable:

1. approved structured master/source;
2. approved WEB/MOBILE reference PNGs;
3. original source assets/fonts;
4. current browser implementation;
5. derived/helper assets.

When the project starts from an existing structured source (AI/Figma/SVG/etc.), that source may outrank screenshots until client approval locks a new master.

Never use the current browser implementation as the visual truth merely because it already exists.

---

# Anti-dead-end rules

## NEVER

- code before identifying the authoritative visual source;
- decompose production assets before understanding the source composition;
- guess an asset when the source already contains it;
- crop a screenshot to fake an extractable source asset;
- redraw existing source vectors by eye;
- replace an available font with a “close enough” font;
- write long implementation directives before auditing the source;
- let multiple agents independently “fix” the same visual area without ownership;
- call something pixel-perfect before comparison;
- add backend/framework complexity without a requirement;
- publish client/private material to the public skill repository.

## ALWAYS

- audit inputs first;
- define source of truth;
- preserve desktop/mobile intent;
- client-approve design before implementation;
- lock a master;
- let ChatGPT own UI decomposition/assets;
- let executor own implementation;
- screenshot implementation at known viewports;
- compare before PASS;
- record reusable lessons from failures and successes.

---

# Reference / knowledge pack

Use these repositories and standards as **knowledge references**, not mandatory dependencies.

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

Evaluate better-maintained or more suitable alternatives over time. Do not treat this list as permanent truth.

---

# Continuous Learning & Skill Evolution Policy

`webbyLucifer` must always operate in a continuous-learning state.

Every project and conversation is a potential source of reusable improvements when the lesson is supported by real evidence.

## Learn from each project

Observe:

- what worked;
- what caused unnecessary iteration;
- where intent was misunderstood;
- where design-to-code handoff failed;
- which master format was easier for Codex/Claude;
- which extraction/rendering method was reliable;
- which fonts/masks/effects caused problems;
- which prompts produced better execution;
- which QA methods found real defects;
- which tools/connectors eliminated manual steps;
- what can be automated safely next time.

Do not repeat a failed workflow merely because it exists in this document.

## Project retrospective

At meaningful milestones, form a `LESSONS_LEARNED` summary:

- Successes
- Failures
- Root causes
- Better alternatives
- Reusable rules
- Rules to remove/change
- Repositories/tools worth evaluating
- QA checks worth adding
- Proposed changes to webbyLucifer

Lessons must be evidence-based, not speculative.

## Generalize, do not leak client data

Never commit to this public repository:

- client names when unnecessary;
- private URLs;
- credentials;
- API keys;
- personal information;
- proprietary client assets;
- private source code;
- unreleased designs;
- confidential business information;
- font files/assets without redistribution rights.

Convert project experience into generalized methodology.

Bad lesson:

> “Client X hero uses file abc.png at x=987.”

Good lesson:

> “When a source contains embedded transparency, extract and verify the original alpha/mask before browser-side reconstruction.”

## Improvement proposal gate

When a conversation reveals a meaningful reusable improvement, tell the user briefly that a reusable improvement was found and summarize:

- what was learned;
- why the current skill should change;
- which section would change;
- expected benefit;
- possible regression/risk.

Do not deploy the change automatically.

## Explicit permission before Git deployment

Before modifying this canonical public repository, obtain explicit user approval.

Only after approval may the AI:

1. inspect the current canonical repository;
2. prepare the smallest appropriate change;
3. verify no client/private information is included;
4. update docs/rules/tests as appropriate;
5. commit the improvement;
6. push to the **same canonical `webbyLucifer` repository**;
7. report exactly what changed and the commit SHA.

## Canonical repository rule

Approved reusable improvements belong here:

```text
th6322750-stack/webbyLucifer
```

Do not create random successor repositories (`-v2`, `-new`, `-final-final`) unless the user explicitly requests a fork or major rewrite.

Use normal Git history/tags/releases to evolve the skill.

## Public repository mindset

Every committed rule should be understandable and useful to another person or AI agent that knows nothing about the client project that produced the lesson.

Prefer rules that are:

- generalized;
- reproducible;
- testable where possible;
- explicit about failure modes;
- explicit about fallback paths;
- tool-agnostic when possible.

## Failure memory matters

Preserve generalized failure lessons, not only successes.

Example failed pattern:

```text
screenshot
-> guessed assets
-> guessed masks
-> code
-> visual mismatch
-> recreate assets
-> code again
```

Generalized lesson:

> Do not decompose production assets before identifying and locking the authoritative visual source.

The purpose of learning is to make the same failure less likely on the next project.

---

# Suggested project state model

```yaml
project_name: null
website_type: null
phase: DESIGN

drive:
  connected: unknown
  project_folder: null

design:
  web_approved: false
  mobile_approved: false

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
GĐ1 — ChatGPT designs WEB + MOBILE
    ↓ client approves
GĐ2 — user chooses Figma / SVG / Both
    ↓ master locked
GĐ3 — ChatGPT decomposes all UI assets/text/fonts/specs
    ↓ production UI pack ready
GĐ4 — user chooses Codex / Claude -> static frontend
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
    ↓ user explicitly approves reusable improvement
UPDATE THIS SAME PUBLIC REPOSITORY
```
