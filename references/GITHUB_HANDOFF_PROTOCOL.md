# GitHub + Drive Handoff Protocol — webbyLucifer v3.1

## Core model

```text
USER    = FINAL ACCEPTANCE AUTHORITY
CHATGPT = DESIGN/UI/ASSET/MOTION-FEEL AUTHORITY
CLAUDE  = IMPLEMENTATION/TECHNICAL-MECHANISM AUTHORITY
GITHUB  = CODE + LIGHTWEIGHT CONTRACT/STATE + WEB DELIVERY WHEN GIT/HYBRID IS USED
DRIVE   = HEAVY ASSET STORAGE/DELIVERY WHEN VERIFIED FOR CURRENT WORK SESSION
VERCEL  = OPTIONAL PREVIEW/DEPLOYMENT
```

---

## 1. Task-mode aware handoff

Handoff must declare:

```text
taskMode = NEW_REDESIGN | EXISTING_POLISH | BUG_FIX
```

- `NEW_REDESIGN` uses the full asset-first readiness package.
- `EXISTING_POLISH` uses a small scoped contract and only the assets actually needed.
- `BUG_FIX` uses a targeted defect contract.

Do not force full Asset Count/Drive/4K readiness onto fast-path tasks that do not create a new asset/design package.

---

## 2. GitHub is not the default 4K master dump

GitHub primarily stores:

```text
source code
project configuration
machine-readable handoff/lock state
asset manifest / asset count plan
short implementation contract
implementation receipts
bug/QA records
web delivery assets when GIT/HYBRID mode says they live in the project
```

Heavy 4K masters can remain in Drive. Do not push them all to Git merely because Drive is temporarily unavailable.

---

## 3. Transport modes

```text
DRIVE
= masters and delivery transported through Drive

GIT
= delivery/assets transported through Git/project paths; Drive proof not required

HYBRID
= heavy masters in Drive; web delivery in Git/project destination paths
```

`HYBRID` is often the practical default for a coded web app when large master archives should stay out of Git but local/static delivery files are needed by the framework.

---

## 4. Drive proof is session-scoped

Never store Drive readiness as a permanent project truth.

When `DRIVE` or `HYBRID` is used:

```text
HANDOFF.workSessionId
→ Claude successfully downloads one real file in THIS work session
→ manifest.assetStore.verifiedForSessionId = workSessionId
→ record sessionVerifiedAt
→ accessProofStatus = VERIFIED_THIS_SESSION
```

If auth/session later expires or a real download fails:

```text
DRIVE_SESSION_READY = false
→ re-auth/re-verify before relying on Drive again
```

A proof from a previous session is stale.

---

## 5. Drive is not runtime serving architecture

Hard rule:

> **Drive is storage/delivery transport. `destinationPath` or an explicitly declared runtime source is authoritative for implementation/runtime.**

Typical Next.js/local-static flow:

```text
Drive/Git delivery
→ Claude obtains exact file
→ save at manifest destinationPath
→ e.g. public/assets/projects/a.webp
→ application serves from project path
```

If the project uses a CDN/remote loader, declare it. Never infer Google Drive as the live image origin.

---

## 6. Recommended `.webby/`

```text
.webby/
├── PROJECT_INTAKE.json
├── ASSET_COUNT_PLAN.json
├── HANDOFF.json
├── WEBBY_LOCK.json
├── CLAUDE_TASK.md
├── asset-manifest.json
├── visual-handoff/
├── requests/
├── implementation/
└── qa/
```

Fast-path tasks may use a smaller applicable subset. Do not require the executor to load every optional contract.

---

## 7. Handoff states

```text
NOT_READY
VISUAL_DIRECTION_APPROVED
IMPLEMENTATION_READY_UI
SUPERSEDED
```

For `NEW_REDESIGN`, `IMPLEMENTATION_READY_UI` means the full asset/spec/mapping/transport/state package is ready.

For `EXISTING_POLISH` / `BUG_FIX`, readiness means the current baseline, exact target and any required new assets/spec are sufficiently known for the scoped task; do not manufacture full-pipeline paperwork.

---

## 8. Full-pipeline asset handoff

Before `NEW_REDESIGN` implementation:

```text
asset count reported
high-res masters pass policy
web delivery exists
ITEM/ALLOWED_USAGE mapping complete
required icon inventory complete
transport mode declared
current-session Drive proof valid if DRIVE/HYBRID
runtime destination/source declared
```

An image visible only in chat is not a delivered asset.

---

## 9. Claude consume protocol

```text
read taskMode + short task contract
→ DRIFT CHECK
→ SCOPE CHECK
→ TOKEN CHECK
→ if Drive used, verify proof matches current workSessionId
→ read only required manifest/spec
→ read 1–3 relevant implementation files by default
→ code
→ proportional technical checks
→ short report
```

Do not use a giant prompt or repo-wide audit as a substitute for a complete contract.

---

## 10. Missing asset/spec

```text
NEED_ASSET
BLOCKED_SPEC
TECHNICAL_CONSTRAINT
```

Never search/generate/substitute a visual asset merely to unblock implementation.

---

## 11. Motion mechanism boundary

Technical motion mechanism belongs to Claude, but a mechanism that creates a new **global behavior surface** must be reported before broad application.

Examples:

```text
global wheel/touch/key interception
preventDefault browser scrolling across routes
app-wide event capture
site-wide scroll engine/provider
cross-route focus/navigation interception
```

This is material even when no npm dependency is added.

---

## 12. Critical Finding exception

A serious data-loss/security finding must be reported immediately even when outside the current UI scope.

```text
current action is harmful → stop only that action + report
existing unrelated critical bug → report + continue safe independent task
```

Do not turn the finding into an unauthorized broad audit/refactor.

---

## 13. Vercel

Vercel is optional unless the task specifically needs online preview/deployment behavior. Lack of Vercel does not block ordinary design/asset planning/local implementation.

---

## 14. Forbidden shortcuts

```text
small polish forced through full pipeline without need
Drive readiness reused from a stale session
Claude substitutes/searches/generates missing visual assets
Claude fakes missing approved icons
Claude measures raster to invent geometry
Claude silently introduces site-wide scroll/event interception
Drive treated as live runtime image source by assumption
heavy 4K masters dumped into Git by default
critical data-loss/security evidence hidden because it is “out of scope”
```
