# webbyLucifer — `change_web` v2.1

> **Mission:** turn a client brief into approved full UI prepared by ChatGPT, publish an implementation-ready UI contract through GitHub, let Claude implement without visual invention or unnecessary design context, then verify the real website against approved visual truth.
>
> **Core architecture:** **ChatGPT = FULL UI AUTHORITY. Webby = ROUTE + COMPRESS + VERIFY. Claude = IMPLEMENTATION AUTHORITY. GitHub = VERSIONED EXCHANGE LAYER / SHARED PROJECT STATE.**

---

# 0. Runtime loading and precedence

webbyLucifer v2.1 preserves the GĐ1→GĐ7 responsibilities from v1, but the full v1 baseline is no longer mandatory runtime context.

Read first:

```text
SKILL.md
→ references/PHASE_ROUTER.md
→ only the current actor/phase-specific references
```

`references/WORKFLOW_BASELINE_V1.md` is compatibility/legacy authority. Read it only when migrating a v1 project, resolving a compatibility conflict, or when an active v2.1 protocol does not contain a required rule.

Precedence:

```text
SKILL.md v2.1 hard rules
> active v2.1 protocol
> phase-specific v2 protocol
> WORKFLOW_BASELINE_V1.md
> examples/templates
```

The seven stages remain:

```text
GĐ1 — DESIGN / FULL-PAGE UI — ChatGPT
GĐ2 — FULL UI MASTER / DESIGN SYSTEM — ChatGPT
GĐ3 — FULL PRODUCTION UI SETUP / GITHUB HANDOFF — ChatGPT
GĐ4 — STATIC FRONTEND IMPLEMENTATION — Claude by default
GĐ5 — UX / FRONTEND ENHANCEMENT — selected implementation executor
GĐ6 — BACKEND / CMS / LOGIC — selected implementation executor
GĐ7 — QA / PRODUCTION — ChatGPT reviews; executor fixes
```

---

# 1. Operating principles

```text
CHATGPT = THINK + DESIGN + VISUAL DECISIONS
WEBBY   = ROUTE + COMPRESS + STATE + VALIDATE
CLAUDE  = IMPLEMENT APPROVED CONTRACT
GITHUB  = VERSIONED SHARED STATE
CHATGPT = VISUAL QA + LEARNING EXTRACTION
```

Hard rules:

1. Claude must never be forced to guess an approved UI decision.
2. ChatGPT must complete applicable UI decisions before implementation handoff.
3. Critical handoff facts must be machine-verifiable when tooling allows it.
4. Design knowledge is not automatically implementation input.
5. Claude receives the smallest deterministic implementation contract that is sufficient for the current scope.

---

# 2. Token-efficient Claude handoff

Read `references/CLAUDE_MINIMAL_HANDOFF.md` for GĐ4–GĐ6.

Before Claude begins, ChatGPT/Webby SHOULD compile:

```text
.webby/claude-pack/
├── TASK.md
├── contract.json
├── components.json
├── assets.json
├── responsive.json
└── lock.json
```

Claude MUST NOT read these by default:

```text
WORKFLOW_BASELINE_V1.md
KNOWLEDGE_PACK.md
SVG design/reconstruction instructions
client ideation history
rejected UI alternatives
long visual rationale
unrelated routes/components/assets
closed QA history
raw project learning history
```

If an implementation-critical fact is missing, Claude creates a request. Missing approved UI is not permission to design.

Prefer deterministic values/IDs over prose. Webby should compress ChatGPT decisions into implementation instructions rather than transfer design reasoning.

---

# 3. GitHub contract layers

Each project SHOULD contain the applicable source contracts:

```text
.webby/
├── PROJECT_STATE.yaml
├── HANDOFF.json
├── WEBBY_LOCK.json
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
├── claude-pack/
├── implementation/
│   └── IMPLEMENTATION_RECEIPT.json
├── qa/
│   ├── defects.json
│   └── qa-report.json
└── learning/
```

The canonical schemas live under `schemas/`.

Source contracts can be richer than the compiled Claude pack. Claude consumes only the current implementation subset.

---

# 4. UI identity and handoff integrity

A handoff SHOULD identify:

```text
handoffId
uiRevision
uiCommit
parentUiCommit
contractDigest when available
createdAt
```

`uiCommit` identifies the UI package state being handed off. A later handoff/lock commit may reference that UI commit; do not require a Git commit to contain its own final SHA.

When tooling permits, `contractDigest` SHOULD identify the normalized active contract content independently of Git commit identity.

`WEBBY_LOCK.json` identifies the exact contract/pack state expected by the executor.

Before continuing implementation after repository changes, compare the previously consumed identity against the active handoff. Material mismatch means:

```text
STALE_HANDOFF
```

Claude must consume the new state or create a request when migration is ambiguous.

---

# 5. UI_SETUP_COMPLETE hard gate

Applicable baseline visual requirements still apply. v2.1 additionally requires:

```text
[ ] deterministic UI revision/commit exists
[ ] WEBBY_LOCK exists
[ ] required handoff inputs exist
[ ] production assets referenced by manifests exist
[ ] no unresolved HARD UI BLOCKER exists
[ ] no OPEN blocking request conflicts with readiness
[ ] ownership boundaries are declared
[ ] handoff is not stale
[ ] validation passes, or validator-unavailable reason is explicit
[ ] Claude pack can be compiled for the requested implementation scope
```

Only then:

```text
UI_SETUP_COMPLETE = true
```

If available validation fails, readiness stays false.

---

# 6. Ownership boundaries

Read `references/AGENT_OWNERSHIP_PROTOCOL.md`.

Default:

```text
CHATGPT OWNS VISUAL TRUTH
CLAUDE OWNS IMPLEMENTATION TRUTH
```

Typical ChatGPT/Webby-owned content:

```text
.webby visual specs/maps
HANDOFF / LOCK / claude-pack
visual source/production assets
design/master outputs
visual QA acceptance/defects
learning extraction
```

Typical Claude-owned content:

```text
src/**
app/**
components/**
server/backend implementation
implementation configuration
.webby/requests/**
.webby/implementation/**
```

Claude treats approved visual contracts/assets as read-only unless authority is explicitly changed. ChatGPT performing QA should publish defects rather than casually rewriting implementation code.

---

# 7. Asset, component and placement integrity

Important production assets SHOULD use stable IDs and, when tooling permits:

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

Component and placement contracts SHOULD use stable IDs and enough information to implement without visual invention.

Validators SHOULD check cross-references such as:

```text
route → section
section → component
component → parent component
component → required asset
placement → component/asset
interaction → component
```

Exact geometry is required only where material to approved visual fidelity.

---

# 8. Request and implementation lifecycle

Request lifecycle:

```text
OPEN
→ ACKNOWLEDGED
→ RESOLVED
→ CONSUMED
→ CLOSED
```

Hard rule:

```text
MISSING APPROVED UI != CLAUDE DESIGNS IT
```

After a meaningful implementation milestone, Claude SHOULD publish:

```text
.webby/implementation/IMPLEMENTATION_RECEIPT.json
```

At minimum it records:

```text
consumed handoff/ui identity
implementation commit
implemented routes/components
build/test status when available
open requests/blockers
preview/deployment reference when available
```

---

# 9. QA contract

Read `references/QA_PROTOCOL.md`.

Machine-readable defects SHOULD use stable IDs and identify:

```text
defectId
implementationCommit
route
viewport
section/componentId
severity
observed
expected
authoritative evidence/reference
status
acceptance criteria when useful
```

Claude fixes against defect IDs. ChatGPT re-tests and closes defects only after acceptance.

Browser implementation remains lower visual authority than approved Master/assets/specs/renders.

---

# 10. Validation

The repository provides:

```text
scripts/webby-validate.py
```

Validation should progressively cover:

```text
syntax
→ schema
→ file existence/integrity
→ contract cross-references
→ state/readiness consistency
→ request blockers
→ receipt/QA consistency
```

A validator cannot prove artistic quality or pixel parity. It verifies the handoff contract; visual acceptance remains ChatGPT's responsibility.

---

# 11. Learning loop

Read `references/LEARNING_LOOP.md`.

After implementation/QA, ChatGPT/Webby MAY extract concise evidence-backed lessons into:

```text
.webby/learning/
├── PROJECT_LESSONS.json
├── UI_PATTERNS.json
└── FAILURE_PATTERNS.json
```

The learning store is not dumped into Claude context.

```text
requests + QA defects + outcomes
→ extract reusable lesson
→ retrieve only relevant lessons on a future task
→ ChatGPT applies lesson during design/packaging
→ Webby compiles changed implementation facts
→ Claude receives minimal pack
```

This loop should reduce repeated defects and implementation-token consumption over time.

---

# 12. Versioned evolution

Current protocol version:

```text
2.1.0
```

Generalized skill changes require explicit user approval before being merged into the canonical repository.

Do not create random replacement repositories such as `webbyLucifer-v2`, `final`, or `new`. Version this canonical repository.

---

# 13. Final model

```text
CLIENT BRIEF
↓
CHATGPT GĐ1 DESIGN
↓
CHATGPT GĐ2 MASTER / DESIGN SYSTEM
↓
CHATGPT GĐ3 PRODUCTION UI CONTRACT
↓
WEBBY VALIDATES + LOCKS + COMPILES MINIMAL CLAUDE PACK
↓
UI_SETUP_COMPLETE
↓
CLAUDE CONSUMES ONLY IMPLEMENTATION-RELEVANT STATE
↓
GĐ4 / GĐ5 / GĐ6 IMPLEMENTATION
↓
IMPLEMENTATION RECEIPT
↓
CHATGPT GĐ7 VISUAL QA
↓
STRUCTURED DEFECTS
↓
CLAUDE FIX
↓
CHATGPT ACCEPTANCE
↓
LEARNING EXTRACTION
↓
PRODUCTION_READY
```
