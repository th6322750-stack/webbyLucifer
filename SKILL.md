# webbyLucifer — `change_web` v3.1

> **Mission:** make UI work high-fidelity without making every task expensive. Large/new design work uses an asset-complete implementation-ready pipeline; small existing polish and bug fixes use fast paths. Claude implements without redesigning, asset hunting, pixel reverse-engineering or unnecessary audit loops.
>
> **Core authority:** **USER = FINAL ACCEPTANCE AUTHORITY. CHATGPT = DESIGN / UI / ASSET / STATE / MOTION-FEEL AUTHORITY. CLAUDE = IMPLEMENTATION / TECHNICAL-MECHANISM AUTHORITY. GOOGLE DRIVE = HEAVY ASSET STORAGE/DELIVERY WHEN VERIFIED FOR THE CURRENT WORK SESSION. GITHUB = CODE + LIGHTWEIGHT CONTRACT/STATE + WEB DELIVERY WHEN GIT/HYBRID MODE IS USED. VERCEL = OPTIONAL PREVIEW/DEPLOYMENT.**

---

# 0. v3.1 hard principles

```text
ROUTE THE TASK BEFORE RUNNING A PIPELINE
ASK MATERIAL QUESTIONS BEFORE DESIGN
COUNT ASSETS BEFORE CREATING THEM FOR NEW/REDESIGN SCOPE
HIGH-RES MASTER FIRST — FULL HD / 4K CLASS, 4K PREFERRED
NO LOW-RES PATCHWORK OR FAKE UPSCALE AS AUTHORITY
NO CLAUDE IMAGE SEARCH / GENERATION / SUBSTITUTION
ASSET PACK BEFORE FULL-PIPELINE IMPLEMENTATION
SPEC CREATES RENDER — RENDER NEVER CREATES SPEC
RASTER IS FOR HUMAN ACCEPTANCE / ARRANGEMENT, NOT PIXEL MEASUREMENT
MOTION FEEL = CHATGPT; MOTION MECHANISM = CLAUDE
DRIVE ACCESS MUST BE PROVED AGAIN IN EACH WORK SESSION WHEN DRIVE IS USED
DRIVE IS DELIVERY/STORAGE, NOT DEFAULT RUNTIME SERVING ARCHITECTURE
VISIBLE ICONS MUST EXIST IN THE ICON INVENTORY BEFORE FULL-PIPELINE READY
CLAUDE DOES NOT REDESIGN, RESEARCH, AUDIT THE WHOLE REPO, OR PLAN LONG BY DEFAULT
SCREENSHOT LOOPS ARE NOT DEFAULT
CRITICAL DATA-LOSS / SECURITY FINDINGS MUST BE REPORTED IMMEDIATELY
USER PERFORMS FINAL VISUAL ACCEPTANCE
```

User-facing communication rule:

> When an English or specialist term materially matters, explain in plain Vietnamese what it means and what it is used for the first time, unless the user clearly does not need the explanation.

---

# 1. Canonical references and precedence

Read only what the active task needs.

```text
ALWAYS AT START
→ SKILL.md
→ references/V3_1_AMENDMENTS.md

NEW PROJECT / MAJOR REDESIGN
→ references/INTAKE_DISCOVERY_PROTOCOL.md
→ references/ASSET_FIRST_IMPLEMENTATION_READY_PROTOCOL.md
→ references/VISUAL_HANDOFF_PROTOCOL.md
→ references/GITHUB_HANDOFF_PROTOCOL.md
→ references/AGENT_OWNERSHIP_PROTOCOL.md

EXISTING POLISH / BUG FIX
→ references/V3_1_AMENDMENTS.md
→ active short task contract
→ only supporting protocol actually needed

QA / ACCEPTANCE
→ references/QA_PROTOCOL.md
```

Precedence:

```text
SKILL.md v3.1 hard rules
> V3_1_AMENDMENTS.md
> v3.0 phase-specific protocol where not superseded
> v2.x protocol where not superseded
> WORKFLOW_BASELINE_V1.md legacy guidance
> examples/templates
```

---

# 2. TASK ROUTER — mandatory first decision

Before deciding how much process to run, classify the work.

```text
TASK
|
|----- NEW_REDESIGN
|      |----- new website/page, major redesign, hierarchy/layout architecture change,
|      |      new design system, major responsive redesign, or substantial new asset set
|      |----- run the FULL PIPELINE
|
|----- EXISTING_POLISH
|      |----- existing approved UI; small/local visual adjustment such as spacing,
|      |      typography size, radius, icon size, alignment, card height, or one existing section
|      |----- use FAST PATH; do not rerun full asset/design pipeline unless the change truly needs it
|
|----- BUG_FIX
       |----- a specific incorrect behavior/defect with a known or reproducible target
       |----- use TARGETED FIX path; no redesign/audit expansion
```

If classification is ambiguous and materially changes cost/scope, ask the user once. Do not default a five-line CSS change into the full pipeline.

---

# 3. FULL PIPELINE — NEW_REDESIGN only

```text
GĐ0  Intake + environment/resource readiness
GĐ1  Visual direction/page structure
GĐ2  UI decomposition + Asset Count Plan
GĐ3  Asset classification + high-res production
GĐ4  Productionize + asset QA + transport freeze
GĐ5  Deterministic UI composition + responsive/state/motion feel
GĐ6  User visual approval
GĐ7  IMPLEMENTATION_READY_UI gate
GĐ8  Short implementation contract
GĐ9  Claude implementation
GĐ10 Minimum proportional technical checks
GĐ11 User acceptance of real website
GĐ12 Functional QA → bug IDs → targeted fixes → final handoff
```

Full-pipeline hard flow:

```text
READ EXISTING INPUT
→ ASK ONLY MATERIAL GAPS
→ DECOMPOSE UI
→ COUNT ASSETS
→ REPORT COUNT TO USER
→ CREATE/COLLECT HIGH-RES MASTERS
→ CREATE WEB DELIVERY
→ QA + FREEZE ASSET PACK
→ BUILD FINAL UI FROM DECLARED VALUES + REAL PACK
→ USER APPROVES
→ IMPLEMENTATION_READY_UI
→ SHORT CLAUDE CONTRACT
→ CLAUDE CODES
→ MINIMUM CHECKS
→ USER ACCEPTANCE
→ FUNCTIONAL QA IF NEEDED
```

---

# 4. FAST PATH — EXISTING_POLISH

Existing polish reuses the current approved baseline instead of replaying GĐ0–GĐ7.

```text
CURRENT UI / USER REQUEST
→ ChatGPT identifies exact target + scope
→ Is a new/missing asset required?
   → NO: skip Asset Count/Production/Drive pipeline
   → YES: ChatGPT prepares only the required asset(s), maps them, then hands off
→ short contract
→ Claude reads 1–3 relevant files by default
→ edit
→ proportional technical check
→ user reviews
```

Screenshot rule:

```text
already have enough screenshot/link/description → do not create another screenshot by default
need visual evidence to diagnose current layout/runtime → one targeted screenshot/smoke check may be used
```

Fast path must not silently become a broad redesign. If the requested change alters hierarchy/layout architecture/design system/major responsive behavior, reclassify to `NEW_REDESIGN` and tell the user why.

---

# 5. TARGETED PATH — BUG_FIX

```text
BUG / DEFECT
→ reproduce only when needed
→ identify affected scope
→ fix named defect
→ targeted test
→ short report
```

Bug fixing is not permission to redesign, re-audit the repository, research external inspiration, or clean unrelated code.

---

# 6. Environment + asset transport readiness

For full-pipeline work, establish when applicable:

```text
repository / branch
remote vs Claude local unpushed drift
Claude repository access
ChatGPT remote repository access
Drive connection
Vercel need
CMS / Sheets / API / database source
env/secrets relevant to running
reference authority
layout mode: FULL_WIDTH / FULL_BLEED_WITH_CONTAINER / BOXED / MIXED
device/business priority
```

## Drive proof must be session-scoped

`DRIVE_READY` is never a permanent project fact.

When Drive is used in the current work session:

```text
put/use one real test file
→ Claude downloads it successfully in THIS WORK SESSION
→ record workSessionId + verifiedForSessionId + sessionVerifiedAt
→ DRIVE_SESSION_READY
```

If the session expires or download fails later, readiness becomes false again for that session and the transport must be re-verified before relying on Drive.

Transport modes:

```text
DRIVE  = master + delivery transported through Drive
GIT    = delivery/assets transported through Git when appropriate
HYBRID = heavy masters in Drive; web delivery in Git/project paths
```

Recommended practical default when Drive is unstable but source masters are large:

```text
MASTER 4K → Drive
WEB DELIVERY → Git / project destination path
```

Do not dump all 4K masters into Git merely to bypass Drive.

---

# 7. Asset count + asset quality for full pipeline

Before production, decompose each implementation-relevant route/section and count required assets by **ROLE**.

Examples of ROLE:

```text
HERO
PROJECT_COVER
RENTAL_COVER
GALLERY
NEWS_COVER
BACKGROUND
LOGO
ICON
FLOORPLAN
MAP
PROGRESS
PLACEHOLDER
```

Report before production:

```text
total assets
existing assets
ChatGPT create/prepare
user/client must supply
FHD-class
4K-class
vector
route/section distribution
```

Raster master policy:

```text
production-authoritative raster minimum = FHD class
4K class preferred
hero/full-bleed = 4K preferred/expected by project policy
never call a small enlarged image a true authoritative 4K source
never assemble low-res scraps only to satisfy pixel dimensions
```

Asset classification answers WHAT KIND OF AUTHORITY the asset has:

```text
BRAND
AUTHENTIC
DEMO
EDITORIAL
DECORATIVE
PLACEHOLDER
DATA_VISUAL
```

ROLE answers WHAT THE ASSET DOES IN UI. `ICON` is a ROLE, not another classification axis.

---

# 8. ICON INVENTORY gate

Every icon visibly required by the approved full-pipeline UI must be explicitly inventoried and exist before `IMPLEMENTATION_READY_UI`.

```text
ICON INVENTORY
|
|----- heart-outline.svg
|----- heart-filled.svg
|----- play.svg
|----- pause.svg
|----- arrow-left.svg
|----- arrow-right.svg
|----- ...
```

An icon asset can simultaneously be:

```text
classification = BRAND | DECORATIVE | other appropriate class
role = ICON
```

If an approved visible icon is required but no actual asset exists:

```text
IMPLEMENTATION_READY_UI = false
NEED_ASSET
```

Claude must not recreate the missing icon with ad-hoc CSS, Unicode, another library icon or a visually similar file unless the design contract explicitly authorizes that implementation.

---

# 9. Master source vs web delivery + runtime destination

```text
MASTER SOURCE = highest-quality source/archive
WEB DELIVERY = implementation-ready file the website actually uses
```

Core rule:

> **Drive is delivery/storage, not the default runtime serving architecture. `destinationPath` / declared runtime source is authoritative.**

Typical Next.js/project-path flow:

```text
ChatGPT prepares delivery asset
→ Drive or Git transport
→ Claude copies/downloads exact file
→ save to manifest destinationPath
→ e.g. public/assets/projects/a.webp
→ app serves project asset normally
```

If the project intentionally uses a CDN/remote image loader, that architecture must be declared; do not infer Drive itself is the live image origin.

---

# 10. Deterministic UI authority

```text
DECLARED DESIGN VALUES → FINAL COMPOSITION → RASTER
```

Never:

```text
RASTER → CLAUDE MEASURES PIXELS → MAGIC NUMBERS → CODE
```

```text
RASTER = human acceptance + hierarchy/arrangement
SPEC/MANIFEST = implementation numbers, mappings, states and behavior
```

If a material numeric value is missing, use `BLOCKED_SPEC` rather than measuring a screenshot.

---

# 11. Responsive, content and states

Use real project breakpoints/constraints. Do not invent familiar breakpoints when the project already has its own system.

Use real/representative Vietnamese content where wrapping matters. Define content envelopes such as max lines, clamp, no-wrap and representative short/long values when needed.

ChatGPT owns layout-changing visual states when applicable:

```text
NORMAL
LONG_TEXT
SHORT_TEXT
IMAGE_MISSING
PARTIAL_DATA
EMPTY
FEW_ITEMS
LOADING
```

Only draw separate states when the state materially changes layout; otherwise a rule is enough.

---

# 12. Motion ownership — FEEL vs MECHANISM

Motion is intentionally split into two layers.

```text
MOTION FEEL — CHATGPT
|----- trigger
|----- duration
|----- easing
|----- distance
|----- stagger
|----- orchestration/order
|----- never-animate
|----- reduced-motion intent

MOTION MECHANISM — CLAUDE
|----- CSS vs JS
|----- observer/scroll implementation
|----- requestAnimationFrame/interpolation
|----- wheel/touch handling
|----- cleanup/listeners
|----- technical fallbacks
|----- avoiding permanently hidden states
```

Claude may change the mechanism without asking Design Authority when all are true:

```text
visual feel does not change
observable behavior does not change
no material new global behavior surface is introduced
```

A **global behavior surface** includes, for example:

```text
global wheel/touch/key interception
preventing/replacing default browser scroll behavior across routes
app-wide event capture
cross-route navigation/focus behavior changes
global provider/state/scroll engine affecting the whole site
```

Even with zero new npm dependencies, introducing such a global behavior surface is architecturally material. Claude must report it before applying broadly. Use `TECHNICAL_CONSTRAINT` when the approved feel cannot be met safely without that expansion.

---

# 13. Approval states + readiness

```text
VISUAL_DIRECTION_APPROVED
= user likes the design direction

IMPLEMENTATION_READY_UI
= full-pipeline UI also has enough assets/mapping/geometry/responsive/state/delivery information to implement without invention
```

For `NEW_REDESIGN`, `IMPLEMENTATION_READY_UI` requires all applicable full-pipeline checks.

For `EXISTING_POLISH` and `BUG_FIX`, do not force Asset Count/4K/Drive gates when no new asset/design pipeline is involved. Use the fast-path readiness flags in the handoff/task instead.

---

# 14. Claude execution model

Ordinary scoped task:

```text
receive short contract
→ DRIFT / SCOPE / TOKEN pre-flight
→ read 1–3 relevant implementation files by default
→ code
→ exact assets only when needed
→ proportional checks
→ 3–5 line report
```

Claude MUST NOT by default:

```text
write a long plan/todo
re-audit the entire repository
research external design inspiration
redesign approved UI
search/generate/substitute assets
map identity-bearing assets by array index
invent missing icons/states/visual feel
measure raster pixels for geometry
run screenshot matrices
run full test suites for trivial visual-only changes
write long narrative reports
```

Blockers:

```text
NEED_ASSET
BLOCKED_SPEC
TECHNICAL_CONSTRAINT
```

Continue unaffected work when safe; never invent a visual replacement.

---

# 15. CRITICAL FINDING exception to anti-scope-creep

Anti-scope-creep remains active, but serious data-loss/security findings must never be hidden merely because they are outside the current UI task.

Critical examples:

```text
silent overwrite / data loss
auth bypass
secret/credential exposure
serious authorization failure
unexpected destructive action
serious security vulnerability
```

Two branches:

```text
A. CURRENT ACTION IS CAUSING / ABOUT TO CAUSE HARM
   → stop only the harmful/affected action
   → report CRITICAL_FINDING with evidence + affected scope + immediate risk
   → do not continue the dangerous step without direction

B. EXISTING UNRELATED CRITICAL BUG IS DISCOVERED
   → report CRITICAL_FINDING immediately
   → continue the current task if the current task is safe and independent
   → do not silently expand into a full security/backend audit
```

A critical finding is an escalation signal, not permission to refactor or audit the whole system.

---

# 16. Technical checks + screenshots

Run checks proportional to task risk:

```text
static small UI change → typecheck/lint/build only as relevant
new responsive layout → one quick browser smoke check when useful
complex interaction/motion mechanism → targeted runtime test
backend/data/security → targeted tests
```

Screenshot comparison is not the default implementation loop. Use it only when it adds evidence: user-requested preview, diagnosis of a visual/runtime issue, or a genuinely layout-sensitive smoke check.

---

# 17. Version

Current canonical protocol:

```text
3.1.0
```

v3.1 keeps v3.0's asset-first deterministic model but adds:

```text
TASK ROUTER + EXISTING_POLISH/BUG_FIX fast paths
MOTION FEEL vs MECHANISM split
session-scoped Drive proof + DRIVE/GIT/HYBRID transport
ICON as ROLE + icon inventory gate
Drive delivery vs runtime destination clarification
CRITICAL_FINDING two-branch exception
```

Generalized skill changes still require explicit user approval before canonical repository changes.