# Visual Handoff Protocol — v3.0

## Purpose

v3 separates three authorities that were previously mixed together:

```text
ASSET MANIFEST = WHICH VISUAL RESOURCE IS ALLOWED / WHERE IT BELONGS
SPEC / CONTRACT = IMPLEMENTATION NUMBERS + RESPONSIVE + STATE + MOTION + BEHAVIOR
RASTER REFERENCE = HUMAN VISUAL ACCEPTANCE + PAGE HIERARCHY / ARRANGEMENT
```

This removes the old failure mode:

```text
beautiful raster
→ executor measures pixels
→ magic ratios / arbitrary gaps
→ implementation drifts
→ repeated screenshot/fix loop
```

---

## 1. Two kinds of render

### A. Asset render / asset production

Image generation may be used to create appropriate production assets such as hero photography, lifestyle imagery, editorial imagery, backgrounds and decorative art when fabrication is allowed.

The output is not automatically a final web asset. It must pass productionization, identity classification and quality checks.

### B. Final UI reference render

The final page reference must be composed from:

```text
actual frozen asset pack
+ declared geometry
+ declared typography
+ real/representative content
+ actual project constraints/tokens when they exist
+ declared responsive behavior
```

It must not be a free-form image-generation hallucination of the whole page.

---

## 2. Deterministic composition

A deterministic composition is a UI composition whose important geometry comes from declared values rather than being inferred later from pixels.

Example:

```text
canvas: 1440
container: 1240
columns: 4
gap: 16
cardRatio: 4/3
sectionPaddingY: 64
heading: 32/40/700
```

These values are implementation inputs. The raster is an output of them.

Hard direction:

```text
SPEC → COMPOSITION → RASTER
```

Forbidden direction:

```text
RASTER → MEASURE → SPEC
```

---

## 3. “Look, do not measure” rule

Claude/executor MAY look at an approved raster to understand:

- section order;
- visual hierarchy;
- composition/arrangement;
- relative emphasis;
- which supplied visual is being referred to.

Claude/executor MUST NOT use the raster as a ruler to invent:

- pixel gaps;
- container widths;
- custom aspect ratios;
- font sizes;
- offsets;
- breakpoints;
- crop positions.

If a required numeric value is missing from the implementation authority:

```text
BLOCKED_SPEC: <missing value>
```

Do not create magic geometry such as `199/144` because a screenshot happened to measure that way.

---

## 4. Asset completeness before final approval

For an `APPROVED FINAL` reference:

```text
EVERY VISIBLE PRODUCTION ASSET
→ must exist in the frozen pack
→ must have an explicit mapping/usage
→ or must intentionally be a declared PLACEHOLDER/state
```

Examples:

- render shows 8 unique project cards → pack must map all 8 visible images;
- gallery shows 5 photos → the 5 photos must exist and map to that gallery/item;
- a floorplan shown as factual → the actual data visual must exist;
- a missing-image design may intentionally show a placeholder if that is the approved state.

Claude must never make up missing images merely to make the implementation resemble the raster.

---

## 5. Asset identity vs presentation

Identity and presentation are separate.

Example model:

```text
ITEM: project:sun-galaxy-complex
FILE: project-sun-galaxy-cover.avif

USAGE:
  project-card:
    ratio: 4/3
    objectPosition:
      mobile: 68% 50%
      desktop: 64% 50%

  project-detail-hero:
    ratio: 16/7
    objectPosition:
      mobile: 72% 45%
      desktop: 50% 40%
```

`objectPosition` belongs to `(asset × usage/frame)`, not globally to the image.

Use `ALLOWED_USAGE` to prevent correct-looking but semantically wrong reuse.

---

## 6. Source/master and web delivery

A high-resolution master is not necessarily the file the browser should load.

```text
MASTER SOURCE
= high-quality authority/archive, FHD/4K-class raster or vector where appropriate

WEB DELIVERY
= the implementation-ready file derived from the master
```

The manifest should identify both when applicable.

Claude normally uses the delivery file. Do not point the implementation directly at a huge 4K PNG merely because it is the source master.

Runtime optimizers such as framework image optimization do not replace art direction, safe areas, identity mapping or mobile crop decisions.

---

## 7. Responsive reference strategy

Do not choose reference widths only because they are common device sizes. Use the actual project layout breakpoints.

Recommended strategy:

```text
1. mobile representative width (commonly ~390, project-dependent)
2. exact breakpoint where desktop/tablet composition first changes
3. exact wide/container behavior breakpoint
4. 1920 only when full-width/full-bleed behavior needs large-screen review
```

Rule:

> Inspect the boundary where the layout becomes hardest, not only a comfortable width well above the breakpoint.

If the project uses a 900px desktop transition, 900 is more informative than 1024 for catching the tightest desktop state.

---

## 8. Existing-polish vs redesign mode

### EXISTING POLISH

When the user wants to preserve the current structure and fix visual details:

```text
current browser screenshot = CURRENT evidence
ChatGPT annotation/spec = TARGET
Claude implements the explicit deltas
```

A new full-page target render is not required for every small polish task.

### NEW / REDESIGN

When the page/section is being materially redesigned:

```text
asset plan
→ frozen asset pack
→ deterministic composition
→ final user-approved reference
→ implementation contract
```

Do not treat the old browser screenshot as target authority in a redesign.

---

## 9. Content authority

When real content exists, use real content in the final reference, especially Vietnamese text whose wrapping/diacritics affect layout.

When content can change later, define a content envelope such as:

```text
title: maxLines 2; clamp; tested short/long Vietnamese values
location: maxLines 1; ellipsis
price: noWrap; tested with representative longest formatted value
```

Do not use artificially short copy merely to make the approved render look cleaner.

---

## 10. State authority

ChatGPT owns the visual treatment of runtime states that materially change layout.

Common states when applicable:

```text
NORMAL
LONG_TEXT
SHORT_TEXT
IMAGE_MISSING
PARTIAL_DATA
EMPTY
FEW_ITEMS
LOADING
ERROR
```

Do not create a separate full-page render for every state. Prefer a compact component state sheet only for states whose layout actually differs.

If a real runtime state exists but no visual rule exists and it cannot safely reuse the normal style:

```text
BLOCKED_SPEC: missing visual state
```

Claude must not silently invent the state.

---

## 11. Motion authority

Motion belongs to Design Authority, not to implementation improvisation.

When needed, specify:

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

If a clear motion spec cannot be achieved with the current implementation architecture/performance budget, Claude reports:

```text
TECHNICAL_CONSTRAINT
```

with concise evidence rather than silently changing the feel.

---

## 12. Final visual package

A v3 visual handoff can contain:

```text
USER-APPROVED RASTER REFERENCES
+ DETERMINISTIC GEOMETRY / TYPE / RESPONSIVE RULES
+ ASSET MANIFEST + DRIVE REFERENCES
+ REQUIRED STATE RULES/SHEET
+ MOTION RULES WHEN APPLICABLE
+ SHORT IMPLEMENTATION CONTRACT
```

The raster does not need to duplicate every implementation number in visible annotations; the structured spec carries those numbers.

---

## 13. Approval distinction

```text
VISUAL_DIRECTION_APPROVED
= user approves how it looks

IMPLEMENTATION_READY_UI
= user-approved UI + complete assets + delivery + mappings + semantic geometry + responsive + states + motion-or-N/A
```

Only `IMPLEMENTATION_READY_UI` is the normal handoff state for Claude.

---

## 14. Screenshots after implementation

Browser screenshots are evidence, not an automatic loop.

Do not require a screenshot matrix after every task. Use screenshots when:

- the user asks to see the result;
- diagnosing a visual/runtime issue;
- a responsive/new-layout smoke check genuinely benefits from visual evidence;
- a QA phase explicitly requires evidence.

The user is final visual acceptance authority. Claude does not self-approve visual parity.
