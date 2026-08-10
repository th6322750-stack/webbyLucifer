# Agent Ownership Protocol

## Purpose

Prevent ChatGPT and Claude from silently editing the same source of truth.

```text
CHATGPT = VISUAL TRUTH OWNER
CLAUDE = IMPLEMENTATION TRUTH OWNER
```

## Default ownership

### ChatGPT-owned / Claude read-only unless explicitly reassigned

- approved visual Masters/renders;
- `.webby/HANDOFF.json` and `.webby/WEBBY_LOCK.json` active UI declarations;
- route/section/component/placement/typography/token/responsive/interactions visual contracts;
- `assets/source/**` visual source authority;
- `assets/production/**` approved visual resources;
- `.webby/qa/**` acceptance and visual defect records.

### Claude-owned / ChatGPT review-only by default

- frontend implementation source;
- backend/server implementation;
- implementation architecture and configuration;
- tests owned by implementation;
- `.webby/implementation/**`;
- `.webby/requests/**` request creation/consumption state, except ChatGPT may resolve supplied UI resources.

## Rules

1. Ownership is about decision authority, not Git permissions.
2. Claude must not modify an approved visual contract to make implementation easier.
3. ChatGPT performing QA should publish a defect rather than silently redesigning implementation code.
4. User instructions can explicitly reassign ownership for a project.
5. Generated framework wrappers may be Claude-owned while canonical SVG/assets remain ChatGPT-owned.
6. If a required visual resource is missing, use the request loop.
7. If an implementation change requires a design change, obtain explicit visual approval and publish a new UI revision.

## Conflict state

If both agents modified the same authoritative visual contract without explicit reassignment:

```text
OWNERSHIP_CONFLICT
```

Do not resolve by choosing the newest file automatically. Return to the authoritative owner and user-approved intent.
