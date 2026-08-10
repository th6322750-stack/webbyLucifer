# Phase Router — webbyLucifer v2.1

## Goal

Load the minimum rules needed for the current actor and phase. Do not make every agent read the full historical workflow.

## Hard rule

`references/WORKFLOW_BASELINE_V1.md` is legacy authority, not default runtime context.

Read it only when:

- a required rule is not represented in the active v2.1 protocol;
- migrating a v1 project;
- resolving a direct compatibility conflict.

## Actor-aware loading

### ChatGPT — GĐ1/GĐ2/GĐ3

ChatGPT owns all visual decisions and may load the design, asset, SVG, handoff and knowledge references needed for the current UI task.

Do not load implementation-only material unless required to make the UI contract executable.

### Claude — GĐ4/GĐ5/GĐ6

Claude MUST NOT read the full baseline, knowledge pack, SVG production pipeline, design rationale, rejected design history or unrelated QA history by default.

Claude reads only:

1. `.webby/claude-pack/TASK.md`
2. `.webby/claude-pack/contract.json`
3. `.webby/claude-pack/components.json`
4. `.webby/claude-pack/assets.json`
5. `.webby/claude-pack/responsive.json`
6. `.webby/claude-pack/lock.json`
7. explicitly referenced implementation files from the current repository

If a required implementation fact is absent, Claude creates a request. Missing UI information is not permission to design.

### ChatGPT — GĐ7 QA

Load the active UI truth, implementation receipt, evidence and open defects. Historical design material is optional unless needed to resolve a visual dispute.

## Token-efficiency rule

Prefer normalized IDs, values and constraints over prose.

Good:

```json
{"componentId":"hero-main","height":760,"assetId":"hero-01","mobileLayout":"stack"}
```

Avoid sending implementation agents long visual rationale when the same requirement can be represented deterministically.

## Result

```text
CHATGPT = THINK + DESIGN
WEBBY = ROUTE + COMPRESS + VERIFY
CLAUDE = IMPLEMENT
GITHUB = STATE
CHATGPT = QA
```
