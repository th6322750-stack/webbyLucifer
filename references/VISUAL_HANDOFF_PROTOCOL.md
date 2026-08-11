# Visual-First Handoff Protocol — v2.1

## Purpose

webbyLucifer v2.1 keeps ChatGPT as the full visual authority and Claude as the implementation authority, but changes how approved UI is transferred into implementation.

The default principle is:

```text
VISUAL FIRST
CONTRACT SECOND
```

Do not spend tokens describing what an executor can reliably see in an approved full-page render. Use structured contracts for behavior, state, responsive rules, data, navigation, motion, constraints, and any decision that is not safely inferable from the visual truth.

---

## 1. Approved visual truth

After GĐ1/GĐ2 approval, ChatGPT SHOULD publish full-page renders for every implementation-relevant route and required viewport.

Recommended project structure:

```text
.webby/
└── visual-handoff/
    ├── routes.json
    ├── home-desktop.png
    ├── home-mobile.png
    ├── product-desktop.png
    └── product-mobile.png
```

The approved renders are visual truth for visible presentation. They do not replace authoritative original assets, native/vector sources, or explicit interaction/responsive/data contracts.

Recommended authority order when applicable:

```text
1. approved original/source asset
2. approved full-page render
3. approved structured Master/design source
4. explicit visual/behavior contract
5. browser implementation
```

If the browser differs from approved visual truth, the implementation is fixed. Do not rewrite the approved design merely to match an easier implementation.

---

## 2. Visual handoff package

GĐ3 SHOULD publish a `VISUAL_HANDOFF_PACKAGE` containing:

- approved route renders;
- viewport identity for each render;
- route-to-render mapping;
- authoritative asset references;
- only the contracts needed for information not fully visible in renders;
- active handoff/lock/revision metadata.

Example `routes.json`:

```json
{
  "schemaVersion": 1,
  "routes": {
    "/": {
      "desktop": "home-desktop.png",
      "mobile": "home-mobile.png"
    },
    "/product": {
      "desktop": "product-desktop.png",
      "mobile": "product-mobile.png"
    }
  }
}
```

When `routes.json` exists, it SHOULD conform to `schemas/visual-handoff.schema.json`.

---

## 3. Minimal invisible-behavior contract

Do not duplicate clear visible information into large prose/JSON contracts unless deterministic implementation requires it.

Contracts SHOULD focus on:

- responsive composition not fully represented by supplied viewports;
- hover/focus/active behavior;
- motion and transition behavior;
- navigation and route targets;
- dynamic states such as loading, empty, error, authenticated, selected;
- CMS/API/data binding;
- accessibility behavior that is not visually obvious;
- conditional visibility;
- functional constraints and `mustNot` rules;
- exact geometry only when visual fidelity materially depends on it.

Rule:

```text
IMAGE = VISIBLE FORM
CONTRACT = INVISIBLE OR AMBIGUOUS BEHAVIOR
```

A component map or placement map MAY still contain precise information when needed. v2.1 does not remove those contracts; it prevents unnecessary duplication.

---

## 4. Route-scoped context loading

Executors SHOULD consume only the context required for the active route/component.

For example, implementing `/product` normally requires:

```text
product approved renders
+ product assets
+ product responsive rules
+ product interactions/states
+ shared tokens/components actually used
```

Do not load every project contract into model context by default.

Preferred rules:

```text
ROUTE-SCOPED CONTEXT
COMPONENT-SCOPED CONTEXT
ON-DEMAND CONTRACT LOADING
```

This is a token-efficiency rule and must not reduce implementation correctness.

---

## 5. GĐ4 visual reconstruction

Before writing implementation code for an approved route, Claude/executor SHOULD inspect the route's approved render(s) and reconstruct:

- section hierarchy;
- containers and grids;
- typography hierarchy;
- spacing relationships;
- cards and controls;
- imagery treatment;
- borders, radii and shadows;
- alignment and layering;
- visible responsive differences between supplied viewports.

Then combine this visible evidence with the minimal contract.

Hard rule:

```text
VISIBLE APPROVED UI MUST BE DERIVED FROM APPROVED VISUAL TRUTH WHEN AVAILABLE.
```

Claude MUST NOT claim a visible UI decision is undefined merely because it is absent from text when it is clear in an approved render.

If a material UI decision is not clear in the render and is not defined by a contract, the existing request lifecycle applies:

```text
MISSING APPROVED UI != CLAUDE DESIGNS IT
```

---

## 6. Implementation targets

Visual reconstruction is implementation-target agnostic.

### MODE A — CODE

Default for coded projects:

```text
Approved Render
→ visual reconstruction
→ React / Next.js / Vue / HTML/CSS / selected stack
```

### MODE B — ELEMENTOR

Use only when the project explicitly targets WordPress + Elementor:

```text
Approved Render
→ visual reconstruction
→ Elementor-compatible JSON/template
→ WordPress import
```

Elementor is an implementation target, not the default architecture and not a replacement for webbyLucifer's authority, revision, QA, or request rules.

---

## 7. Handoff gate additions

When approved renders are part of the project, `UI_SETUP_COMPLETE` SHOULD additionally verify:

```text
[ ] every required route has its required approved viewport render(s)
[ ] route-to-render mappings resolve to existing files
[ ] active renders belong to the current UI revision/commit
[ ] no stale render is referenced by the active handoff
[ ] non-visible behavior needed for implementation is explicitly contracted
```

If a required render is missing and the route cannot be implemented without visual invention, `UI_SETUP_COMPLETE` remains false for that scope.

---

## 8. Visual QA loop

After implementation:

```text
IMPLEMENTATION
↓
RUN REAL WEBSITE
↓
CAPTURE BROWSER SCREENSHOT AT MATCHING VIEWPORT
↓
COMPARE AGAINST APPROVED RENDER
↓
PUBLISH DEFECTS
↓
EXECUTOR FIXES
↓
RE-CAPTURE / RE-QA
```

ChatGPT owns visual acceptance. The executor does not self-approve visual parity.

The approved render is expected state. The browser screenshot is implementation evidence.

---

## 9. Non-regression rules

v2.1 does NOT remove or weaken:

- GĐ1→GĐ7 phase order;
- user approval gates;
- source-first asset authority;
- canonical SVG rules;
- `HANDOFF.json`;
- `WEBBY_LOCK.json`;
- deterministic UI revision/commit;
- stale-handoff protection;
- ownership boundaries;
- request lifecycle;
- implementation receipts;
- validator usage;
- backend/CMS phase;
- final ChatGPT visual QA.

The change is specifically how visible UI information is handed to implementation: prefer approved visual truth over redundant token-heavy description.
