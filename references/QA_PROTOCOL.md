# QA Protocol

## Roles

- ChatGPT owns visual acceptance against approved truth.
- Claude/executor owns implementation fixes.

## Visual-first QA — v2.1

When an approved full-page render exists for the tested route/viewport, use the normal evidence loop:

```text
APPROVED RENDER = EXPECTED VISUAL STATE
BROWSER SCREENSHOT = IMPLEMENTATION EVIDENCE
```

Recommended loop:

```text
run real website
↓
capture browser screenshot at matching viewport
↓
compare against approved render
↓
publish actionable defects
↓
executor fixes
↓
re-capture / re-QA
```

Comparison SHOULD cover applicable visible differences including:

- section order and presence;
- layout and container geometry;
- spacing and alignment;
- typography hierarchy and wrapping;
- image size/crop/position;
- controls, cards, borders, radii and shadows;
- color treatment;
- overflow or clipping;
- responsive composition;
- missing or unexpectedly visible components.

A screenshot comparison may be automated or visually inspected, but ChatGPT remains the final visual acceptance authority.

## Defect lifecycle

Recommended:

```text
OPEN → FIXED_PENDING_QA → CLOSED
          ↘ REOPENED ↗
```

## Defect identity

Every actionable defect SHOULD use a stable `defectId` and record:

- implementation commit;
- route;
- exact viewport;
- section/component ID;
- severity;
- observed result;
- expected approved behavior/appearance;
- authoritative source/spec/render reference;
- evidence when available;
- acceptance criteria when useful.

For visual parity defects, prefer referencing the exact approved render and matching browser screenshot/evidence.

## Severity

Suggested values:

```text
BLOCKER
HIGH
MEDIUM
LOW
```

## Acceptance

Claude must not self-close visual defects solely because code changed. ChatGPT re-renders/reviews the affected state and closes or reopens the defect.

Browser implementation is evidence, never visual authority. If the implementation differs from approved visual truth, fix the implementation unless the user explicitly approves a design revision.

Automated screenshot diff, accessibility checks and performance checks are evidence, not replacements for approved visual authority.
