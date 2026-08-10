# webbyLucifer Knowledge Pack

This file is a **reference registry and selection guide**, not an installation manifest.

> **REFERENCE != DEPENDENCY**
>
> Study strong sources and current official documentation. Install only what the real project needs. The visual contract belongs to `webbyLucifer`; external libraries must not become an excuse to replace the approved design.

---

# 1. Core operating doctrine

`webbyLucifer` uses a strict responsibility split:

```text
CHATGPT = FULL UI AUTHORITY
CLAUDE  = IMPLEMENTATION AUTHORITY
GITHUB  = VERSIONED EXCHANGE LAYER / SHARED PROJECT STATE
```

The knowledge pack supports that split.

Research/tooling is successful when it helps ChatGPT produce a more complete UI handoff or helps Claude implement the supplied UI more reliably **without moving visual decisions from ChatGPT to Claude**.

Evaluate references against these questions:

1. Does it reduce visual guessing?
2. Does it preserve authoritative source fidelity?
3. Does it produce reusable production resources rather than screenshot hacks?
4. Can the output be described deterministically in GitHub handoff files?
5. Can Claude consume it without redesigning the UI?
6. Does it reduce correction loops?
7. Does it introduce unacceptable licensing, privacy, maintenance or build risk?

---

# 2. GĐ1 — design research and UI direction

Use strong design/component sources for principles, not for blind visual copying.

## superdesigndev/superdesign-skill

Reference for:

- AI-oriented visual exploration;
- structured design direction generation;
- preview/iteration thinking.

Do not treat its output patterns as a universal style.

## alexpate/awesome-design-systems

Reference registry for studying varied design-system approaches and avoiding tunnel vision.

## fontsource/fontsource

Reference/source awareness for:

- web-font families and weights;
- packaging options;
- understanding which exact font resources exist for implementation.

Approved typography still controls the project. Do not replace a selected typeface merely because another one is easier to install.

## lucide-icons/lucide

Reference/source for consistent generic UI icons only when the approved design does not contain custom/source iconography.

Never substitute an approved custom icon with Lucide for convenience.

---

# 3. GĐ2/GĐ3 — UI component architecture and accessibility

## shadcn-ui/ui

Use as reference for:

- composable component structure;
- component source ownership;
- practical design-token translation;
- Tailwind-oriented composition when the selected stack uses it.

Do not inherit the default shadcn visual identity over the approved UI.

## radix-ui/primitives

Use as reference for:

- accessible behavioral primitives;
- Dialog, Popover, Tabs, Dropdown, Tooltip and related state models;
- keyboard/focus behavior;
- separating behavior from visual styling.

This is especially useful because Claude can implement robust interaction behavior while preserving ChatGPT's visual states.

## storybookjs/storybook

Use as reference/tooling when useful for:

- isolated component states;
- responsive/viewport review;
- visual state catalogs;
- component documentation;
- QA of reusable implementation components.

## w3c/aria-practices

Use as the behavior/accessibility reference for:

- keyboard patterns;
- roles/states/properties;
- interaction semantics.

## dequelabs/axe-core

Use when automated accessibility checks are appropriate.

Automated checks do not replace manual keyboard/semantic review.

---

# 4. GĐ3 — SVG/vector production

SVG/vector handoff is a high-risk stage because small export/optimization changes can alter masks, gradients, filters, IDs, scaling or browser behavior.

The detailed canonical workflow lives in:

```text
references/SVG_PRODUCTION_PIPELINE.md
```

## W3C SVG 2

Primary standards reference for:

- SVG viewport/user coordinate systems;
- `viewBox`;
- `preserveAspectRatio`;
- paths and geometry;
- embedded content;
- SVG accessibility behavior.

Core rule for `webbyLucifer`: preserve intentional responsive scaling and do not remove structural information simply to minimize bytes.

## SVGO

Reference/tooling for conservative production SVG optimization.

Important current areas to inspect before real use:

- `preset-default` behavior;
- `cleanupIds`;
- `prefixIds`;
- `removeScripts`;
- editor metadata removal;
- numeric/path precision;
- title/description removal behavior;
- viewBox-related plugins.

Rules:

- keep source SVG separately;
- never trust an optimizer PASS without visual comparison;
- use deterministic/reproducible ID prefixes when inline collisions are possible;
- treat untrusted script/event behavior as unsafe by default;
- verify the exact installed/current SVGO version before copying a configuration.

## SVGR

Optional reference/tooling for converting canonical SVG assets into React components.

Use only when component wrapping helps the chosen stack.

The canonical SVG remains visual truth; generated React components are implementation derivatives.

## Vector production selection rule

Prefer SVG for genuinely vector resources such as:

- logos/wordmarks;
- icons;
- ornaments;
- vector illustrations;
- approved vector masks/shapes.

Prefer live HTML/CSS/components for:

- normal text;
- buttons;
- cards;
- semantic controls;
- layout sections.

Prefer raster formats for photographic imagery and other raster-native content.

Never convert a complete page/section into a giant SVG merely to obtain screenshot similarity.

---

# 5. Image/raster production

When working with photographic/product/property imagery, investigate techniques that preserve source quality while producing web-ready variants.

Relevant concerns:

- original source identity;
- crop/focal-point preservation;
- transparent alpha preservation;
- color profile/visual shifts;
- responsive sizing;
- AVIF/WebP/JPEG/PNG suitability;
- optimization after visual verification;
- avoiding duplicated low-quality derivatives.

The authoritative source should remain distinguishable from production derivatives.

Raster optimization must not occur before the crop/fidelity contract is known.

---

# 6. Typography/font production

GĐ3 must make the approved typography executable rather than leaving Claude to infer it.

Research/prepare:

- exact family;
- exact style/weight;
- available web-font formats;
- licensing/redistribution constraints;
- fallback behavior;
- Vietnamese glyph support when required;
- font loading strategy;
- mapping of every semantic/visual role.

If binaries cannot legally/technically be committed, create an explicit manifest with acquisition/source requirements instead of silently substituting another font.

---

# 7. Frontend implementation references

These sources help Claude implement the already-defined UI. They do not own the visual system.

## vercel/next.js

Reference for:

- React full-stack architecture;
- routing/rendering;
- server/client boundaries;
- production application patterns.

## tailwindlabs/tailwindcss

Reference for:

- responsive utility systems;
- translating approved tokens/spacing/layout into implementation;
- consistent component styling.

Not mandatory. CSS Modules, vanilla CSS, CSS-in-JS or other approaches may be more appropriate.

## TanStack/query

Reference for:

- asynchronous server state;
- caching/invalidation;
- mutations;
- pagination/infinite data.

Use only when real client-side server-state complexity justifies it.

## react-hook-form/react-hook-form

Reference for efficient form state/validation integration.

## colinhacks/zod

Reference for runtime schemas and shared input contracts.

---

# 8. Backend / CMS / auth references

Use only when the actual project requires them.

## supabase/supabase

Reference for combinations of:

- Postgres;
- authentication;
- storage;
- realtime;
- generated APIs.

## prisma/prisma

Reference for:

- typed data access;
- schema/migrations;
- database modeling in TypeScript projects.

## payloadcms/payload

Reference for:

- CMS/admin systems;
- content modeling;
- Next.js-oriented full-stack CMS workflows.

## trpc/trpc

Reference for end-to-end typed TypeScript APIs when that tradeoff is appropriate.

## better-auth/better-auth

Reference for modern auth architecture when user accounts/auth flows are genuinely required.

Do not add backend frameworks, auth, databases or CMS simply because they appear in this pack.

---

# 9. GitHub handoff / agent collaboration

The detailed project exchange rules live in:

```text
references/GITHUB_HANDOFF_PROTOCOL.md
```

GitHub is used as:

```text
VERSIONED COMMUNICATION BUS
+ ASSET REGISTRY
+ UI IMPLEMENTATION CONTRACT
+ PROJECT STATE
+ QA EXCHANGE
```

Useful handoff artifacts include:

- `PROJECT_STATE.yaml`;
- `HANDOFF.json`;
- `CLAUDE_TASK.md`;
- asset/component/placement/route/section maps;
- typography/tokens/responsive/interaction specs;
- missing-UI requests;
- QA defect reports.

Commit identity matters because ChatGPT and Claude must know which UI state is being produced, consumed and reviewed.

---

# 10. Browser / visual / production QA

## microsoft/playwright

Primary reference/tool for:

- Chromium/Firefox/WebKit automation;
- screenshot capture;
- viewport testing;
- interaction/E2E checks.

## mapbox/pixelmatch

Reference for:

- pixel-level comparison;
- visual difference images;
- objective regression signals.

Use together with structural/perceptual review. Font rasterization/browser/OS differences can produce legitimate pixel differences.

## GoogleChrome/lighthouse

Reference/tool for:

- performance;
- accessibility signals;
- SEO/basic best-practice audits.

## getsentry/sentry-javascript

Reference for production runtime error/trace monitoring when the project needs it.

---

# 11. GĐ3 active research focus

GĐ3 is the highest-risk handoff stage because the approved visual system becomes executable production resources.

During real projects, actively evaluate stronger current techniques for:

- authoritative source extraction;
- SVG/vector preservation and canonicalization;
- deterministic SVG IDs;
- alpha/mask extraction;
- font identification and legal web-font preparation;
- design-token extraction;
- image optimization without visual damage;
- responsive component decomposition;
- visual layer/z-index mapping;
- asset placement contracts;
- design-to-code structured formats;
- AI-readable UI specifications;
- browser screenshot comparison;
- Git-based agent handoff/state synchronization.

Do **not** adopt a tool solely because it is popular.

A candidate method is valuable only when evidence shows it improves the `webbyLucifer` contract.

---

# 12. Continuous-learning rule

When a better method is discovered:

1. validate it on real evidence;
2. identify which workflow rule it improves;
3. record expected benefit and possible regression;
4. generalize the lesson without client/private data;
5. request explicit user approval before changing the canonical public skill repository.

The canonical repo remains:

```text
th6322750-stack/webbyLucifer
```

Do not create random replacement `v2`, `new`, `final` or `final-final` repositories unless explicitly requested.
