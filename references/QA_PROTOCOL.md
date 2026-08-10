# QA Protocol

## Roles

- ChatGPT owns visual acceptance against approved truth.
- Claude/executor owns implementation fixes.

## Defect lifecycle

Recommended:

```text
OPEN → FIXED_PENDING_QA → CLOSED
          ↘ REOPENED ↗
```

## Defect identity

Every actionable defect SHOULD use a stable `defectId` and record:

- implementation commit;
- route;
- exact viewport;
- section/component ID;
- severity;
- observed result;
- expected approved behavior;
- authoritative source/spec/render reference;
- evidence when available;
- acceptance criteria when useful.

## Severity

Suggested values:

```text
BLOCKER
HIGH
MEDIUM
LOW
```

## Acceptance

Claude must not self-close visual defects solely because code changed. ChatGPT re-renders/reviews the affected state and closes or reopens the defect.

Automated screenshot diff, accessibility checks and performance checks are evidence, not replacements for approved visual authority.
