# SVG Production Pipeline

This reference defines how `webbyLucifer` converts approved visual resources into production SVG assets that Claude can consume without guessing.

> The purpose is not to turn the whole UI into SVG. The purpose is to preserve true vector resources, normalize them safely, map them to components, and verify that the browser render still matches the approved visual truth.

## 1. Ownership

```text
CHATGPT = visual/vector authority
CLAUDE  = implementation executor
GITHUB  = versioned exchange layer
```

ChatGPT owns asset classification, extraction/reconstruction, SVG normalization, color/accessibility intent, placement mapping and visual QA before handoff.

Claude may consume or wrap the supplied production SVG in the chosen frontend stack, but must not silently redraw, recolor, substitute or simplify an approved SVG.

---

## 2. Asset classification comes first

Do not convert every visible object into SVG.

Preferred production representation:

| Visual resource | Preferred output |
| --- | --- |
| Vector logo / wordmark | SVG |
| UI icon | SVG |
| Ornament / line art / decorative vector | SVG |
| Vector illustration | SVG |
| Vector mask / clip / shape | SVG when browser-safe and fidelity is preserved |
| Photographic property/product/person image | AVIF/WebP/PNG/JPEG as appropriate |
| Normal heading/body/CTA text | Live HTML text |
| Button/card/container | HTML/CSS/component |
| Complex Photoshop-like effect | SVG only if fidelity/browser behavior is verified; otherwise raster/CSS according to the authoritative source |
| SVG containing embedded raster | `HYBRID_SVG`, explicitly recorded in the manifest |

Hard rule:

```text
FULL UI SECTION != GIANT SVG SCREENSHOT
```

Semantic UI remains real UI. SVG is for visual resources that are genuinely vector or need vector behavior.

---

## 3. Source authority and preservation

Use this authority order when available:

```text
ORIGINAL VECTOR SOURCE
AI / SVG / FIGMA / EPS / PDF VECTOR
        ↓
ORIGINAL RASTER SOURCE
        ↓
APPROVED STRUCTURED MASTER
        ↓
APPROVED WEB/MOBILE RENDER
        ↓
DERIVED / RECONSTRUCTED RESOURCE
```

Rules:

1. Inspect the authoritative source before recreating anything.
2. Never crop a screenshot to fake an asset that exists in source form.
3. Never redraw an existing vector by eye when it can be extracted.
4. Preserve a read-only/original copy before optimization.
5. Record reconstruction uncertainty when no structured source exists.

Recommended layout:

```text
assets/
├── source/
│   └── vectors/
│       └── hero-gold-wave.source.svg
└── production/
    └── svg/
        └── hero-gold-wave.svg
```

The source file is archival/authoritative input. The production file is the normalized asset used by implementation.

---

## 4. Canonicalization contract

For every production SVG, normalize conservatively and preserve fidelity.

### 4.1 Viewport and scaling

Preserve or intentionally establish a valid `viewBox` when the asset is expected to scale responsively.

`viewBox` together with `preserveAspectRatio` defines how SVG user-space is mapped into the viewport. Do not remove `viewBox` merely to save bytes when the asset needs responsive scaling.

Record important aspect-ratio behavior in the asset/placement manifest when `meet`, `slice`, `none`, clipping or non-default alignment materially affects rendering.

### 4.2 Editor metadata

Production SVG may remove editor-only metadata/namespaces when doing so does not change the visual result.

Keep the original source asset separately so authoring metadata is not permanently destroyed.

### 4.3 IDs, gradients, masks, filters and clip paths

Inline SVGs can conflict when independent files reuse IDs such as:

```text
gradient0
clip0
mask0
filter0
a
b
```

Production assets that may be inlined must use collision-safe IDs.

Prefer deterministic/reproducible prefixes derived from a stable asset identity such as filename/asset slug. Do not rely on random UUIDs or build-order counters for SSR/React/Next.js output.

Example naming intent:

```text
hero-gold-wave__gradient-01
hero-gold-wave__mask-01
hero-gold-wave__filter-01
```

When using SVGO, inspect the current behavior of `cleanupIds` and `prefixIds`. `cleanupIds` may cause collisions across multiple inline SVGs; deterministic `prefixIds` is the preferred mitigation when IDs must survive.

### 4.4 Scripts and unsafe behavior

Unless an approved SVG intentionally requires trusted script behavior, production SVGs must not carry JavaScript execution capability.

For untrusted/external SVG input, strip or reject:

- `<script>` elements;
- event-handler attributes such as `onload`/`onclick`;
- script URLs;
- unexpected interactive links when not required.

Current SVGO tooling provides `removeScripts` for this purpose. Interactive scripted SVG is an explicit exception, not the default.

### 4.5 External references

Inspect references such as:

- `<image href="...">`;
- `<use href="...">`;
- filters/masks/patterns referencing URLs;
- remote fonts/resources;
- external styles.

The production manifest should record whether an SVG contains external references or embedded raster content.

Do not assume an SVG is self-contained simply because the file extension is `.svg`.

### 4.6 Numeric/path optimization

Optimize only after preserving visual truth.

Aggressive path conversion, path merging, transform conversion or numeric rounding may alter delicate geometry, strokes, masks or filter output.

Use conservative precision for brand marks and visually sensitive assets, then compare before/after renders.

### 4.7 Color policy

Every production SVG should have an explicit color policy:

```text
FIXED_BRAND
THEMEABLE
TOKENIZED
```

- `FIXED_BRAND`: preserve approved fills/strokes exactly.
- `THEMEABLE`: component may intentionally use `currentColor` or controlled props.
- `TOKENIZED`: colors are mapped to approved design tokens/CSS variables.

Do not automatically replace logo/artwork colors with `currentColor` just because it is convenient for implementation.

### 4.8 Text policy

Normal UI/content text must remain live HTML when possible.

Text may remain/convert to vector paths only when it is genuinely artwork, a logo/wordmark, decorative lettering, or another approved non-semantic graphic.

Do not convert ordinary headings, descriptions, prices, CTA labels or CMS content into vector paths to chase screenshot parity.

### 4.9 Accessibility intent

Classify each SVG as one of:

```text
DECORATIVE
INFORMATIVE
INTERACTIVE
```

- `DECORATIVE`: implementation should hide it from the accessibility tree when appropriate.
- `INFORMATIVE`: provide an accessible name/description at the SVG or containing component level.
- `INTERACTIVE`: semantic control behavior belongs to the containing UI component and must support keyboard/focus requirements.

Do not depend blindly on SVG `<title>`/`<desc>` surviving optimization. Accessibility intent belongs in the manifest/component contract as well.

---

## 5. SVG manifest

Each important production SVG should be represented in `asset-manifest.json` or a dedicated `svg-manifest.json`.

Example:

```json
{
  "id": "hero-gold-wave",
  "source": "assets/source/vectors/hero-gold-wave.source.svg",
  "production": "assets/production/svg/hero-gold-wave.svg",
  "category": "ORNAMENT",
  "viewBox": "0 0 840 120",
  "colorPolicy": "FIXED_BRAND",
  "accessibility": "DECORATIVE",
  "containsRaster": false,
  "containsExternalRefs": false,
  "containsScripts": false,
  "routes": ["/"],
  "qa": "PASS"
}
```

When a field cannot be known reliably, record uncertainty rather than inventing a value.

---

## 6. Componentization

Canonical production SVG is the visual source of truth.

For React/Next.js projects, a generated component may be derived from the canonical SVG using tooling such as SVGR when appropriate.

```text
CANONICAL SVG
      ↓
GENERATED / WRAPPED COMPONENT
      ↓
FRONTEND IMPLEMENTATION
```

Hard rule:

```text
GENERATED COMPONENT != NEW VISUAL SOURCE OF TRUTH
```

If the vector artwork changes, update the authoritative/canonical SVG and regenerate or update the wrapper in a traceable way.

Claude may create a clean wrapper API (`className`, `aria-*`, controlled color props when allowed) but must preserve the visual contract.

---

## 7. Placement contract

Supplying an SVG file is not enough. ChatGPT must also tell Claude where and how it is used.

Placement mapping should cover, where relevant:

- route;
- section/component;
- role;
- desktop/mobile anchor;
- width/height behavior;
- crop/overflow;
- z-index/layer relationship;
- pointer-events;
- theme/color behavior;
- whether replacement/redrawing is forbidden.

Example:

```json
{
  "asset": "hero-gold-wave",
  "file": "assets/production/svg/hero-gold-wave.svg",
  "route": "/",
  "section": "hero",
  "role": "decorative-background",
  "desktop": { "anchor": "bottom-right", "width": "48%", "zIndex": 2 },
  "mobile": { "anchor": "bottom-center", "width": "92%" },
  "mustNot": ["redraw with CSS", "change approved colors"]
}
```

---

## 8. Visual QA gate

Successful export/optimization is not a PASS.

For important assets compare:

```text
AUTHORITATIVE SOURCE
vs
CANONICAL PRODUCTION SVG
vs
BROWSER RENDER
```

Check where applicable:

- geometry;
- aspect ratio;
- crop/overflow;
- gradient stops/direction;
- masks/clip paths;
- filters;
- strokes;
- opacity/blending;
- embedded raster positioning;
- ID references;
- light/dark background behavior;
- desktop/mobile placement.

When browser support or implementation mode matters, test the same usage mode Claude will use: `<img>`, CSS background, inline SVG, component wrapper, sprite, etc.

A derived production SVG cannot be marked `PASS` until fidelity is verified against the authoritative source.

---

## 9. Hard failures

SVG setup fails when any applicable condition is true:

```text
[ ] asset was recreated despite an extractable authoritative source
[ ] screenshot crop is being used as a fake vector/source asset
[ ] giant section/page SVG replaces semantic UI
[ ] required viewBox/scaling behavior is broken
[ ] inline IDs can collide across assets
[ ] untrusted scripts/event handlers remain
[ ] hidden external/raster dependencies are undocumented
[ ] approved brand colors were altered without authorization
[ ] normal content text was unnecessarily converted to paths
[ ] accessibility intent is unknown for meaningful graphics
[ ] source and production copies are not distinguishable
[ ] asset has not passed visual fidelity comparison
[ ] placement/route/component usage is unspecified
```

Any applicable failure keeps:

```text
UI_SETUP_COMPLETE = false
```

---

## 10. Tooling references

Use these as current technical references, not mandatory dependencies:

- W3C SVG 2 — coordinate systems, `viewBox`, `preserveAspectRatio`, embedded content and accessibility behavior.
- SVGO documentation — production optimization, `cleanupIds`, `prefixIds`, `removeScripts`, editor metadata and plugin behavior.
- SVGR documentation — optional SVG-to-React component generation.

Always verify current tool/version behavior before adopting a configuration into a real project.

`REFERENCE != DEPENDENCY`.
