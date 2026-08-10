# webbyLucifer — `change_web` v2

> **Mission:** turn a client brief into approved full UI prepared by ChatGPT, publish an implementation-ready UI contract through GitHub, let Claude implement without visual invention, then verify the real website against approved visual truth.
>
> **Core architecture:** **ChatGPT = FULL UI AUTHORITY. Claude = IMPLEMENTATION AUTHORITY. GitHub = VERSIONED EXCHANGE LAYER / SHARED PROJECT STATE.**

## 0. Compatibility and load order

webbyLucifer v2 keeps the complete GĐ1→GĐ7 workflow from v1. The previous canonical rules are preserved unchanged in:

```text
references/WORKFLOW_BASELINE_V1.md
```

An agent using this skill MUST read this file first, then read the v1 baseline, then only the phase-specific references needed for the current task.

Precedence when rules conflict:

```text
SKILL.md v2 hard rules
> phase-specific v2 protocol
> WORKFLOW_BASELINE_V1.md
> examples/templates
```

The seven stages remain unchanged:

```text
GĐ1 — DESIGN / FULL-PAGE UI — ChatGPT
GĐ2 — FULL UI MASTER / DESIGN SYSTEM — ChatGPT
GĐ3 — FULL PRODUCTION UI SETUP / GITHUB HANDOFF — ChatGPT
GĐ4 — STATIC FRONTEND IMPLEMENTATION — Claude by default
GĐ5 — UX / FRONTEND ENHANCEMENT — selected implementation executor
GĐ6 — BACKEND / CMS / LOGIC — selected implementation executor
GĐ7 — QA / PRODUCTION — ChatGPT reviews; executor fixes
```

All design, source-first asset, Drive, Master, SVG, responsive, production packaging, request-loop and QA rules in the v1 baseline continue to apply unless this file explicitly strengthens them.

---

# 1. V2 operating principle

v1 relied primarily on agents reading and obeying written rules. v2 turns the handoff into a machine-verifiable protocol.

```text
RULES
+ SCHEMAS
+ STATE
+ LOCK
+ OWNERSHIP
+ VALIDATION
+ RECEIPTS
+ QA CONTRACT
```

The highest-priority rule remains:

> **Claude must never be forced to guess an approved UI decision. ChatGPT must completely prepare the UI before implementation handoff.**

But v2 adds a second hard rule:

> **A declaration is not enough. Critical handoff facts must be machine-verifiable whenever the project environment allows it.**

---

# 2. GitHub contract layers

Each project repository SHOULD contain:

```text
.webby/
├── PROJECT_STATE.yaml
├── HANDOFF.json
├── WEBBY_LOCK.json
├── CLAUDE_TASK.md
├── visual-contract.json
├── asset-manifest.json
├── component-map.json
├── placement-map.json
├── route-map.json
├── section-map.json
├── typography.json
├── tokens.json
├── responsive.json
├── interactions.json
├── requests/
├── implementation/
│   └── IMPLEMENTATION_RECEIPT.json
└── qa/
    ├── defects.json
    └── qa-report.json
```

Production resources remain separated from authoritative/source files exactly as defined by the baseline workflow.

## Machine contract

The canonical v2 schemas live under:

```text
schemas/
```

When a schema exists for a project file, agents SHOULD conform to that schema and validators SHOULD reject structurally invalid handoffs.

---

# 3. UI_SETUP_COMPLETE v2 hard gate

The baseline checklist still applies. v2 additionally requires, when applicable:

```text
[ ] HANDOFF.json identifies a deterministic UI revision/commit
[ ] WEBBY_LOCK.json exists
[ ] required handoff files referenced by HANDOFF exist
[ ] lock entries resolve to existing files
[ ] production assets referenced by manifests exist
[ ] no unresolved HARD UI BLOCKER remains
[ ] no OPEN blocking request makes the handoff incomplete
[ ] agent ownership boundaries are declared
[ ] handoff is not stale
[ ] validation passes or an explicit validator-unavailable reason is recorded
```

Only then:

```text
UI_SETUP_COMPLETE = true
```

If validation is available and fails, `UI_SETUP_COMPLETE` MUST remain false.

---

# 4. Deterministic UI revision and stale-handoff prevention

A v2 handoff SHOULD identify:

```text
handoffId
uiRevision
uiCommit
parentUiCommit
createdAt
```

`WEBBY_LOCK.json` SHOULD identify the exact contract state Claude is expected to consume.

Claude records the consumed UI commit/revision before implementation.

Before continuing implementation after pulling new repository state, compare:

```text
consumed UI revision/commit
vs
current active UI revision/commit
```

If the active UI package changed materially:

```text
STALE_HANDOFF
```

Claude MUST NOT silently continue against an obsolete UI package. Pull and consume the new handoff or create a request when migration is ambiguous.

---

# 5. Agent ownership / write boundaries

Read `references/AGENT_OWNERSHIP_PROTOCOL.md`.

Default model:

```text
CHATGPT OWNS VISUAL TRUTH
CLAUDE OWNS IMPLEMENTATION TRUTH
```

Typical ChatGPT-owned paths/content:

```text
.webby visual specs/maps
.webby HANDOFF/LOCK state
assets/source visual authority
assets/production visual resources
design/master outputs
.webby/qa visual acceptance/defects
```

Typical Claude-owned paths/content:

```text
src/**
app/**
components/**
server/backend implementation
implementation configuration
.webby/requests/**
.webby/implementation/**
```

Claude must treat ChatGPT-owned approved visual contract files as read-only unless the user explicitly changes authority.

ChatGPT must not casually rewrite implementation code merely because it is performing visual QA; it should publish defects for the implementation executor.

---

# 6. Asset integrity

Every important production asset SHOULD have a stable asset ID and, when tooling permits, integrity metadata such as:

```text
sha256
mime
byteSize
width/height or SVG viewBox
source authority
reconstruction status
license/redistribution status when relevant
usedBy
```

If an approved production asset changes unexpectedly, validation SHOULD flag the change before implementation or QA consumes it.

The source-first and canonical-SVG rules from the baseline remain mandatory.

---

# 7. High-precision component and placement contracts

Component maps SHOULD use stable IDs rather than relying only on human-readable names.

Recommended fields include:

```text
componentId
implementationTarget when known
parentComponentId
slots/children
states
variants
dataContract when applicable
requiredAssets
interactionIds
responsive composition
mustNot
```

Placement maps SHOULD describe enough geometry for the executor to implement without visual invention. Recommended fields include:

```text
placementId
assetId/componentId
containerId
referenceViewport
coordinateSpace
anchor/offset
width/maxWidth/minWidth
aspectRatio
objectFit/objectPosition/focalPoint
zIndex/layer relationship
breakpoint behavior
mustNot
```

Exact geometry is required only where material to approved visual fidelity; do not manufacture meaningless precision.

---

# 8. Claude request lifecycle

The baseline request loop remains. v2 standardizes lifecycle where practical:

```text
OPEN
→ ACKNOWLEDGED
→ RESOLVED
→ CONSUMED
→ CLOSED
```

A resolved request SHOULD record the resolution commit/revision and affected files. Claude consumes the resolved UI state before closing the request.

Hard rule remains:

```text
MISSING APPROVED UI != CLAUDE DESIGNS IT
```

---

# 9. Implementation receipt

After an implementation milestone, Claude SHOULD publish:

```text
.webby/implementation/IMPLEMENTATION_RECEIPT.json
```

The receipt identifies at minimum:

```text
consumedUiCommit / consumedUiRevision
implementationCommit
implemented routes/components
build/test status when available
open requests/blockers
preview/deployment reference when available
```

This receipt is the executor-to-ChatGPT delivery contract. It does not replace Git history; it makes the consumed UI state and implementation scope explicit.

---

# 10. QA contract

Read `references/QA_PROTOCOL.md`.

Machine-readable QA defects SHOULD use stable defect IDs and identify:

```text
defectId
implementationCommit
route
viewport
section/componentId
severity
observed
expected
authoritative reference/evidence
status
acceptance criteria when useful
```

Claude fixes defects against those IDs. ChatGPT re-tests and closes defects only after acceptance.

Browser implementation remains lower visual authority than approved Master/assets/specs/renders.

---

# 11. Validation

The canonical repository provides:

```text
scripts/webby-validate.py
```

The validator is intentionally dependency-light. It performs structural and cross-reference checks that can be run without external packages. JSON Schemas remain the canonical structural contracts for fuller schema-aware tooling.

Recommended project use:

```bash
python scripts/webby-validate.py /path/to/project
```

A validator cannot prove artistic quality or full pixel parity. It verifies the handoff contract; visual acceptance remains ChatGPT's responsibility.

---

# 12. Versioned evolution

Current protocol version:

```text
2.0.0
```

Generalized skill changes still require explicit user approval before being committed to the canonical repository.

Do not create random replacement repositories such as `webbyLucifer-v2`, `final`, or `new`. Version this same canonical repository.

---

# 13. Final v2 model

```text
CLIENT BRIEF
↓
GĐ1 DESIGN / FULL-PAGE UI
↓
GĐ2 MASTER / DESIGN SYSTEM
↓
GĐ3 PRODUCTION UI SETUP
↓
SCHEMAS + LOCK + VALIDATION + OWNERSHIP
↓
UI_SETUP_COMPLETE
↓
CLAUDE VERIFIES ACTIVE UI STATE
↓
GĐ4 STATIC IMPLEMENTATION
↓
IMPLEMENTATION RECEIPT
↓
GĐ5 UX
↓
GĐ6 BACKEND/CMS/LOGIC
↓
GĐ7 CHATGPT QA
↓
DEFECT CONTRACT
↓
CLAUDE FIX
↓
PRODUCTION_READY
```

For all detailed GĐ1–GĐ7 visual and implementation rules not repeated here, `references/WORKFLOW_BASELINE_V1.md` remains incorporated into this skill by reference.
