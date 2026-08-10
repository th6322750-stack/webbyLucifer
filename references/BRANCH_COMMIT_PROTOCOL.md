# Branch and Commit Protocol

This protocol improves traceability without requiring one mandatory branching model for every project.

## Recommended commit prefixes

```text
webby(ui):      ChatGPT visual/UI package
webby(lock):    handoff/lock metadata
webby(request): missing UI/resource request lifecycle
webby(impl):    Claude implementation
webby(qa):      ChatGPT QA defects/acceptance
webby(fix):     executor fixes from QA
```

## Recommended branches when branch separation is useful

```text
webby/ui-<revision>
webby/impl-<scope>
webby/qa-<scope>
```

Small projects may use one branch if ownership boundaries and commit traceability remain clear.

## UI commit rule

An active handoff must identify the exact UI commit/revision Claude consumes. If metadata cannot reference the same commit that creates it, use a deterministic preceding UI package commit or a small follow-up lock metadata commit.

## Material UI change

A material approved UI change creates a new `uiRevision` and active handoff state. Claude must compare its `consumedUiCommit`/revision before continuing.

## Never

- force-push shared history without explicit project agreement;
- mix unrelated client UI, implementation and skill-repository changes in one opaque commit;
- use vague commit messages such as `update`, `final`, `fix stuff` when the commit is part of the agent exchange contract.
