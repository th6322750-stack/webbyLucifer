# GitHub + Drive Handoff Protocol — webbyLucifer v3.0

## Core model

```text
USER    = FINAL ACCEPTANCE AUTHORITY
CHATGPT = DESIGN/UI/ASSET AUTHORITY
CLAUDE  = IMPLEMENTATION AUTHORITY
GITHUB  = CODE + LIGHTWEIGHT VERSIONED CONTRACT/STATE
DRIVE   = HEAVY ASSET PACK DELIVERY
VERCEL  = OPTIONAL PREVIEW/DEPLOYMENT
```

---

## 1. GitHub is not the default heavy-asset dump

GitHub should primarily contain:

```text
source code
small project configuration
machine-readable handoff/lock state
asset manifest / asset count plan
short implementation contract
implementation receipts
bug/QA records when useful
```

Large 4K masters and bulk asset packs default to one Google Drive project folder after asset production begins.

Web delivery files may ultimately be copied into the implementation repository when the framework/deployment needs local static files; the canonical master/archive can remain in Drive.

---

## 2. GĐ0 access check

Before implementation handoff, establish:

```text
GitHub repository
branch
ChatGPT remote access
Claude repo access
Claude local unpushed drift status
Google Drive folder access
whether Vercel preview is required
```

Do not assume `remote == Claude local`.

---

## 3. Recommended project `.webby/`

Keep the implementation exchange small:

```text
.webby/
├── PROJECT_INTAKE.json
├── ASSET_COUNT_PLAN.json
├── HANDOFF.json
├── WEBBY_LOCK.json
├── CLAUDE_TASK.md
├── asset-manifest.json
├── visual-handoff/
│   └── routes.json / light references when used
├── requests/
├── implementation/
│   └── IMPLEMENTATION_RECEIPT.json
└── qa/
    └── defects.json
```

Do not require the executor to load every optional map/token file if the active contract does not need it.

---

## 4. Drive package

Recommended:

```text
PROJECT_NAME/
├── 01_MASTER_ASSETS/
├── 02_WEB_DELIVERY/
├── 03_BRAND/
├── 04_PROJECTS/
├── 05_RENTALS/
├── 06_EDITORIAL/
├── 07_DATA_VISUAL/
├── 08_PLACEHOLDERS/
├── 09_MANIFEST/
└── 10_FINAL_UI_REFERENCE/
```

Before `IMPLEMENTATION_READY_UI`, confirm:

```text
Drive folder exists
Claude can access/download
manifest points to exact files/IDs/paths
all required visible assets exist
```

An image only visible in chat is not considered delivered.

---

## 5. Handoff status

Recommended v3 states:

```text
NOT_READY
VISUAL_DIRECTION_APPROVED
IMPLEMENTATION_READY_UI
SUPERSEDED
```

`VISUAL_DIRECTION_APPROVED` means the user likes the visible design.

`IMPLEMENTATION_READY_UI` means the package also has sufficient assets/mapping/spec/responsive/state/motion information for implementation without invention.

Claude starts ordinary UI implementation only from `IMPLEMENTATION_READY_UI`.

---

## 6. Active UI identity and lock

The handoff should identify:

```text
handoffId
uiRevision
uiCommit
parentUiCommit
createdAt
status
```

`WEBBY_LOCK.json` may lock lightweight contract/manifest files in Git.

Do not force massive Drive binaries into Git merely for lock purposes. Record Drive IDs/paths/checksums in the manifest when available.

---

## 7. Claude consume protocol

```text
confirm branch/local state
↓
DRIFT CHECK
↓
read short CLAUDE_TASK
↓
read only required manifest/spec inputs
↓
confirm exact Drive assets are accessible
↓
SCOPE CHECK
↓
TOKEN CHECK
↓
read 1–3 relevant implementation files by default
↓
code
↓
minimum proportional checks
↓
short report / receipt
```

Do not use a 500-line implementation prompt as a substitute for a complete UI package.

---

## 8. Drift handling

`DRIFT` means Claude local code differs from the remote/current state that ChatGPT used when preparing the contract.

If `CURRENT` no longer matches materially:

```text
BLOCKED_SPEC: remote/local drift invalidates CURRENT assumption
```

or report the exact technical scope conflict.

Do not knowingly code from a stale assumption.

---

## 9. Missing asset/spec handling

Use:

```text
NEED_ASSET
BLOCKED_SPEC
TECHNICAL_CONSTRAINT
```

Never search for a replacement image merely to unblock yourself.

When ChatGPT resolves a missing asset:

```text
create/fix high-res master as applicable
→ create delivery
→ upload Drive
→ update manifest
→ notify executor of exact item/file/usage
```

---

## 10. Implementation receipt

Keep it concise. At a meaningful milestone, record when useful:

```text
consumedUiRevision / commit
implementationCommit
changed files/routes/components
technical checks
asset mapping status
open blockers
preview URL if available
```

Long narrative implementation reports are not required for ordinary UI tasks.

---

## 11. Vercel

Vercel is optional.

Use it when the user wants an online preview, production deployment or browser-based acceptance environment.

Do not block asset planning, design or ordinary local implementation merely because Vercel is not connected, unless the task specifically depends on deployment behavior.

---

## 12. Forbidden shortcuts

```text
Claude substitutes missing assets
Claude searches/generates visual resources independently
Claude measures raster to invent geometry
Claude audits the whole repo for a small scoped UI task
Claude assumes remote == local without checking when drift is plausible
ChatGPT marks implementation-ready while Drive/manifest/asset mapping is incomplete
heavy master assets are pushed into Git by default without need
screenshot loops are used as a replacement for a complete spec
```
