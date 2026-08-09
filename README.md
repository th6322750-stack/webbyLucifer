# webbyLucifer

`webbyLucifer` is a public, continuously evolving workflow/skill for taking a client web brief from **visual concept -> approved WEB/MOBILE demo -> AI-readable master -> production UI asset pack -> frontend/backend implementation -> verified production website**.

The core skill lives in [`SKILL.md`](./SKILL.md).

## Workflow

```text
GĐ1 — DEMO DESIGN
ChatGPT
Brief -> WEB.png + MOBILE.png + fonts -> client approval

GĐ2 — MASTER UI
ChatGPT
User MUST choose:
A. Figma Master
B. SVG Master
C. Both benchmark

GĐ3 — UI DECOMPOSITION / UI ASSET PACK
ChatGPT
Images + vectors + logos + ornaments + masks + fonts + text map + layout map + UX/responsive spec

GĐ4 — STATIC FRONTEND BUILD
User MUST choose Codex or Claude
Master + UI Asset Pack -> static frontend -> visual parity gate

GĐ5 — UX / FRONTEND ENHANCEMENT
Selected executor
Interactions + motion + responsive behavior + accessibility

GĐ6 — BACKEND / CMS / LOGIC
Selected executor
Only what the project actually requires

GĐ7 — QA / PRODUCTION
ChatGPT reviews; executor fixes
Visual + responsive + UX + accessibility + performance + backend QA
```

## Key principles

- **Source first.** Never guess production assets before understanding the authoritative visual source.
- **ChatGPT owns UI decomposition.** Static design/master is not enough for production; ChatGPT maps every important image, vector, text, font, mask, effect, component and responsive difference into a reusable UI Asset Pack.
- **Implementation agents do not improvise the visual identity.** Codex/Claude consume the approved master and asset/spec pack.
- **Static parity before UX, UX before backend.** Keep gates separate so one layer cannot hide errors in another.
- **Reference != dependency.** Strong public repositories are learning references, not packages that must be installed in every project.
- **Continuous learning with permission.** Every real project may improve the methodology, but changes are pushed to this public repository only after explicit user approval and only after client/private data has been removed.

## GĐ1 Drive behavior

When the environment has Google Drive access, GĐ1 must check that Drive is connected/writable and automatically create the delivery structure:

```text
TEN-DU-AN/
├── bản WEB/
│   └── WEB_TenDuAn.png
├── bản MOBILE/
│   └── MOBILE_TenDuAn.png
└── Document fonts/
```

The client-facing demo package stays intentionally minimal.

## Canonical repository

This repository is the canonical public source of truth for the skill. Improvements should evolve through normal commits/tags/releases rather than creating random `v2`, `final`, or `final-final` repositories.

## Privacy / public-repo rule

Do **not** commit client secrets, private URLs, proprietary source code, unreleased designs, personal data, credentials, API keys, or non-redistributable font/assets. Project lessons must be generalized before they become part of the skill.
