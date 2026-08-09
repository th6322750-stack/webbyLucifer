# webbyLucifer Knowledge Pack

This file is a **reference registry**, not an installation manifest.

> **REFERENCE != DEPENDENCY**
>
> Study patterns from strong projects. Install only what the current project actually needs.

## UI / component architecture / accessibility

### shadcn-ui/ui
Use as reference for:
- composable component structure;
- accessible UI composition;
- ownership of component source;
- practical Tailwind-based design systems.

### radix-ui/primitives
Use as reference for:
- accessible interaction primitives;
- Dialog, Popover, Tabs, Dropdown, Tooltip and related behavior;
- keyboard/focus behavior.

### storybookjs/storybook
Use as reference for:
- isolated component states;
- visual state catalogs;
- responsive/viewport review;
- component documentation and testing.

### w3c/aria-practices
Use as reference for:
- accessible interaction patterns;
- keyboard behavior;
- roles/states/properties.

### dequelabs/axe-core
Use as reference/tooling when automated accessibility checks are appropriate.

---

## Frontend

### vercel/next.js
Reference for:
- React full-stack architecture;
- routing/rendering;
- server/client boundaries;
- production web application patterns.

### tailwindlabs/tailwindcss
Reference for:
- utility-first responsive systems;
- design token translation;
- consistency in spacing/type/layout.

Not mandatory. CSS Modules, vanilla CSS, styled systems, or other approaches may be more appropriate for a project.

### TanStack/query
Reference for:
- asynchronous server state;
- caching;
- invalidation;
- mutations;
- pagination/infinite data.

Use only when the project truly has client-side server-state needs.

### react-hook-form/react-hook-form
Reference for:
- form state;
- validation integration;
- efficient complex forms.

### colinhacks/zod
Reference for:
- schemas;
- runtime validation;
- shared input contracts.

### lucide-icons/lucide
Reference/source for consistent general-purpose interface icons when the design does not provide custom iconography.

Do not replace client/source icons with Lucide simply because it is convenient.

---

## Backend / CMS / auth

### supabase/supabase
Reference for projects needing combinations of:
- Postgres;
- authentication;
- storage;
- realtime;
- generated APIs.

### prisma/prisma
Reference for:
- typed data access;
- schema/migrations;
- database modeling in TypeScript projects.

### payloadcms/payload
Reference for:
- CMS/admin interfaces;
- content modeling;
- Next.js-oriented full-stack CMS projects.

### trpc/trpc
Reference for end-to-end typed APIs in TypeScript-only systems where that tradeoff is appropriate.

### better-auth/better-auth
Reference for modern authentication architecture when user accounts/auth flows are actually required.

---

## QA / browser automation / visual regression

### microsoft/playwright
Primary reference for:
- browser automation;
- Chromium/Firefox/WebKit testing;
- screenshot capture;
- viewport testing;
- interaction/E2E checks.

### mapbox/pixelmatch
Reference for:
- pixel-level image comparison;
- generating visual difference images;
- objective visual regression checks.

Use together with perceptual/structural review; pixel differences may include legitimate font/OS rasterization variance.

### GoogleChrome/lighthouse
Reference for:
- performance;
- accessibility signals;
- SEO/basic best-practice audits.

### getsentry/sentry-javascript
Reference for production runtime error/trace monitoring where the project needs it.

---

# GĐ3-specific research focus

GĐ3 is the highest-risk handoff stage because the visual must be converted into real production resources.

When working on GĐ3, actively look for stronger current techniques related to:

- source image extraction;
- SVG/vector preservation;
- alpha/mask extraction;
- font identification and web-font preparation;
- color/design-token extraction;
- image optimization without visual damage;
- responsive component decomposition;
- visual layer mapping;
- design-to-code structured formats;
- browser screenshot comparison;
- AI-readable UI specifications.

Do **not** adopt a new tool solely because it is popular. Evaluate it against real project evidence:

1. Does it reduce guessing?
2. Does it preserve source fidelity?
3. Does it reduce rework?
4. Can Codex/Claude consume the result reliably?
5. Does it create unacceptable licensing/privacy/maintenance risk?

If a better method is found during a project, propose it through the Continuous Learning gate in `SKILL.md` before changing the canonical workflow.
