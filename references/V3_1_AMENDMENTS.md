# webbyLucifer v3.1 Amendments

This file contains the canonical v3.1 amendments that override conflicting v3.0 rules.

## A1 — Task Router

Classify every task before selecting process cost:

```text
NEW_REDESIGN
= new site/page, major redesign, hierarchy/layout/design-system/major responsive or major asset-set change
→ full v3 pipeline

EXISTING_POLISH
= small/local visual change on an existing approved UI
→ fast path; reuse current authority; no full intake/asset pipeline unless actually needed

BUG_FIX
= specific incorrect behavior/defect
→ targeted fix path; no redesign/re-audit
```

A screenshot is not mandatory for EXISTING_POLISH. Use an existing screenshot/link/description when sufficient. Capture one only when it materially helps diagnose the current state.

## A2 — Motion FEEL vs MECHANISM

```text
CHATGPT owns MOTION FEEL:
trigger, duration, easing, distance, stagger, orchestration, never-animate, reduced-motion intent.

CLAUDE owns MOTION MECHANISM:
CSS/JS choice, observer strategy, scroll/wheel implementation, requestAnimationFrame/interpolation, cleanup/listeners, fallbacks and technical safety.
```

Claude may change mechanism without approval only when visible feel and observable behavior remain unchanged and no material global behavior surface is introduced.

A material global behavior surface includes global wheel/touch/key interception, preventing or replacing browser default scroll behavior across routes, app-wide event capture, cross-route focus/navigation changes, or a site-wide scroll/provider engine. This is architecturally material even with zero new dependencies and must be reported before broad application.

## A3 — Session-scoped asset transport proof

Drive readiness expires with the work session. Never treat `DRIVE_READY=true` as permanent.

When DRIVE or HYBRID transport is used:

```text
current workSessionId
→ download one real file successfully in the current session
→ record verifiedForSessionId + sessionVerifiedAt
→ only then rely on Drive for that session
```

If auth/session expires later, readiness is false again until re-verified.

Transport modes:

```text
DRIVE  = heavy/delivery transport through Drive
GIT    = delivery/assets through Git when appropriate
HYBRID = heavy masters in Drive; web delivery in Git/project destination paths
```

Do not move all heavy 4K masters to Git merely because Drive temporarily fails.

## A4 — ICON is a ROLE, plus inventory gate

Do not add ICON as a peer classification to AUTHENTIC/DEMO/etc.

```text
classification = authority/nature of the asset
role           = UI job performed by the asset
```

Example:

```text
classification = BRAND
role = ICON
```

Every icon visible in an approved full-pipeline UI must appear in the icon inventory and have an actual mapped asset before `IMPLEMENTATION_READY_UI`.

Missing `heart-filled.svg`, `play.svg`, `pause.svg`, or any other visible icon blocks readiness with `NEED_ASSET`; Claude must not fake the icon with ad-hoc CSS/Unicode/similar library assets unless explicitly authorized.

## A5 — Drive delivery is not runtime architecture

Hard rule:

> **Google Drive is storage/delivery transport, not the default live image origin. `destinationPath` or the explicitly declared runtime source is authoritative.**

Typical project path flow:

```text
Drive/Git delivery
→ Claude obtains exact file
→ save at manifest destinationPath
→ e.g. public/assets/... for a typical Next.js project
→ runtime serves from the project as configured
```

If a project intentionally uses a CDN/remote loader, declare that architecture; never infer Drive as runtime source.

## A6 — Critical Finding exception

Critical findings include credible evidence of data loss/silent overwrite, auth bypass, secret exposure, severe authorization error, unintended destructive operation, or serious security vulnerability.

```text
CURRENT ACTION CAUSING/ABOUT TO CAUSE HARM
→ stop only that harmful action
→ report CRITICAL_FINDING immediately
→ wait before repeating the dangerous step

EXISTING UNRELATED CRITICAL BUG DISCOVERED
→ report CRITICAL_FINDING immediately
→ continue current task if safe and independent
→ do not silently expand into a broad audit/refactor
```

A Critical Finding is an escalation exception to anti-scope-creep, not permission for scope expansion.

## Implementation principle

v3.1 is intentionally asymmetric:

```text
large/new work → expensive preparation, cheap implementation
small polish    → cheap scoped path
bug fix         → targeted path
```

The point is to eliminate both failure modes:

```text
UNDER-SPECIFIED LARGE WORK → Claude guesses and loops
OVER-PROCESSED SMALL WORK  → workflow itself wastes time
```
