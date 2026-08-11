# GĐ0 Intake & Discovery Protocol — v2.2

## Purpose

GĐ0 exists before any design work. Its job is to turn whatever the user has already supplied into a sufficiently complete, personalized and implementation-relevant project brief before GĐ1 begins.

The core rule is:

```text
READ FIRST
UNDERSTAND SECOND
ASK ONLY WHAT IS MISSING
DESIGN ONLY AFTER INTAKE_COMPLETE
```

GĐ0 is not a fixed questionnaire. It is an adaptive discovery loop.

---

## 1. Inputs GĐ0 must inspect first

Before asking the user anything, ChatGPT MUST inspect every currently available input that may answer the project brief, including when provided:

- user messages and explicit requirements;
- business/service/product description;
- existing website URLs;
- repository/project context;
- screenshots and reference designs;
- logo, colors, fonts and brand assets;
- product/service/property images;
- supplied copy/content;
- audience or customer information;
- desired actions/conversion goals;
- required pages/routes/features;
- WordPress/CMS/admin requirements;
- technical stack or deployment constraints;
- desktop/mobile expectations;
- examples the user likes or dislikes;
- cultural/local/industry constraints;
- deadlines or launch constraints when material.

Never ask the user to repeat information that is already sufficiently known from the current project context.

---

## 2. Build the Project Intake Map

Normalize known information into `.webby/PROJECT_INTAKE.json` when the project repository is available.

Recommended categories:

```text
PROJECT IDENTITY
BUSINESS / OFFER
PRIMARY GOAL
CONVERSION GOAL
TARGET AUDIENCE
BRAND
CONTENT
ASSETS
REFERENCES
ROUTES / INFORMATION ARCHITECTURE
FEATURES
RESPONSIVE EXPECTATIONS
INTERACTIONS
CMS / ADMIN / DATA
TECHNICAL CONSTRAINTS
MUST-HAVE
MUST-NOT-HAVE
PERSONALIZATION SIGNALS
ASSUMPTIONS
OPEN QUESTIONS
BLOCKERS
```

Each important field is classified as one of:

```text
KNOWN
ASSUMED
SOFT_GAP
HARD_GAP
NOT_APPLICABLE
```

Definitions:

- `KNOWN` — directly supplied or reliably evidenced.
- `ASSUMED` — safe temporary assumption that does not materially distort the design; record it visibly.
- `SOFT_GAP` — missing detail that can be handled later without blocking useful design progress.
- `HARD_GAP` — missing information that would materially change the design direction, personalization, scope or conversion logic.
- `NOT_APPLICABLE` — irrelevant to this project.

Do not invent fake readiness percentages.

---

## 3. Adaptive question loop

If `HARD_GAP` items remain, ChatGPT MUST ask targeted questions before GĐ1.

Question rules:

1. Ask only questions whose answers can materially improve or constrain the design.
2. Prefer high-information questions first.
3. Group closely related questions when that makes answering easier, but avoid dumping a giant generic questionnaire.
4. Use concrete examples/options when they help the user answer quickly.
5. Ask in the user's language and use simple wording unless technical precision is required.
6. Never ask a question already answered by supplied files, links, screenshots, repository state or prior user messages.
7. If the user's answer exposes a new material ambiguity, ask the next targeted question.
8. Continue until no unresolved `HARD_GAP` remains.

Typical high-value discovery dimensions include:

- What exactly is being sold/provided?
- Who should the page persuade?
- What is the primary action visitors should take?
- Which products/services/categories matter most?
- What trust signals/proof can be used?
- Which visual identity must be preserved?
- Which pages/features are actually required?
- What should the experience feel like to this specific audience?
- Which examples does the user want to emulate or avoid?

These are dimensions, not a mandatory question list. Do not ask them when already known or irrelevant.

---

## 4. Personalization requirement

GĐ0 must collect enough evidence that GĐ1 is designing for this specific project rather than producing a generic industry template.

Before `INTAKE_COMPLETE`, the project should normally have enough information to answer:

```text
WHAT are we designing?
WHO is it for?
WHY should that audience care?
WHAT should they do next?
WHAT makes this project/brand distinct?
WHAT content/assets/evidence are authoritative?
WHAT pages/features are in scope?
WHAT constraints must the design respect?
```

Not every project needs every field. The rule is material completeness, not bureaucratic completeness.

---

## 5. GĐ0 completion gate

Set:

```text
INTAKE_COMPLETE = true
```

only when:

```text
[ ] all supplied inputs have been inspected
[ ] existing answers have been reused instead of re-asked
[ ] project/business/offer is understood sufficiently
[ ] target audience is known or a safe explicit assumption is accepted
[ ] primary goal/conversion goal is known
[ ] project scope/routes/features are known enough to start design
[ ] brand/assets/references status is understood
[ ] key must-have / must-not-have constraints are captured
[ ] personalization signals are sufficient to avoid a generic design direction
[ ] no unresolved HARD_GAP remains
[ ] assumptions and SOFT_GAP items are recorded
```

If a `HARD_GAP` remains:

```text
INTAKE_COMPLETE = false
GĐ1 MUST NOT START
```

---

## 6. GĐ0 output

When complete, ChatGPT should give the user a concise normalized brief before or as it transitions to GĐ1.

Recommended output:

```text
PROJECT BRIEF LOCKED
- business / offer
- audience
- primary goal
- conversion goal
- brand direction / existing identity
- required pages/features
- content/assets available
- important constraints
- working assumptions
- non-blocking gaps

INTAKE_COMPLETE = true
NEXT = GĐ1 DESIGN / FULL-PAGE UI
```

The summary is a confirmation surface, not an invitation to restart discovery from zero.

---

## 7. Relationship to baseline GĐ1.P

`references/WORKFLOW_BASELINE_V1.md` contains the older `GĐ1.P PROJECT INTAKE / EVIDENCE LOCK` concept.

In v2.2, interpret that work as belonging to GĐ0:

```text
OLD: GĐ1.P PROJECT INTAKE / EVIDENCE LOCK
NEW: GĐ0 INTAKE / DISCOVERY / EVIDENCE LOCK
```

Do not run the same intake twice. Once `INTAKE_COMPLETE` is locked, GĐ1 consumes the normalized intake and starts design research/direction work.

If new user information arrives later and materially changes the project, update the intake state and affected downstream revision instead of silently ignoring the change.

---

## 8. Anti-patterns

Do not:

- jump from a vague brief directly into GĐ1;
- ask a generic 20-question form regardless of context;
- ask the user to repeat known information;
- assume a generic target audience without recording it;
- treat logo/color alone as sufficient personalization;
- collect trivia that does not affect design or implementation;
- block on minor `SOFT_GAP` details that can be safely handled later;
- invent business facts, testimonials, statistics or claims as if supplied by the user;
- let Claude fill missing design strategy later.

GĐ0 exists so GĐ1 begins with a project-specific, evidence-backed brief.