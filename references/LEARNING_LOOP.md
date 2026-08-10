# Learning Loop — webbyLucifer v2.1

## Purpose

Capture reusable lessons from implementation and QA without forcing future implementation agents to read project history.

## Project-local learning

Projects MAY maintain:

```text
.webby/learning/
├── PROJECT_LESSONS.json
├── UI_PATTERNS.json
└── FAILURE_PATTERNS.json
```

## Ownership

ChatGPT/Webby owns learning extraction and retrieval.

Claude does not read the learning store by default. A lesson is passed to Claude only when it materially changes the current implementation instruction, and then it SHOULD be compiled into the minimal handoff instead of copied as historical prose.

## What to learn

High-value lessons include:

- repeated QA defects;
- responsive compositions that repeatedly drift;
- asset formats or reconstruction choices that cause implementation problems;
- component patterns that consistently produce reliable parity;
- ambiguous instructions that caused requests or rework;
- instructions that consumed significant implementation context without changing code;
- browser/implementation constraints that should affect future UI packaging.

Do not store secrets, private client content, credentials, personal data or proprietary source material in a public canonical learning store.

## Lesson quality gate

A lesson SHOULD be stored only when it is:

1. evidence-backed;
2. reusable beyond one transient mistake, or explicitly marked project-local;
3. actionable;
4. concise;
5. scoped by tags/affected phase/component when useful.

## Suggested record

```json
{
  "lessonId": "WB-LRN-0042",
  "scope": "PROJECT",
  "category": "RESPONSIVE",
  "summary": "Hero focal point must be explicit at mobile breakpoint",
  "evidence": ["WB-QA-0017", "WB-QA-0021"],
  "action": "Require mobile objectPosition/focalPoint in compiled asset placement when hero imagery is art-directed",
  "appliesTo": ["GĐ3", "GĐ7"],
  "status": "ACTIVE"
}
```

## Retrieval rule

Do not dump the learning store into an agent prompt.

```text
project/task context
→ retrieve matching lessons
→ apply them during ChatGPT design/packaging
→ compile only changed implementation facts
→ Claude receives minimal contract
```

## Feedback loop

```text
IMPLEMENTATION
→ QA DEFECTS / REQUESTS
→ LESSON EXTRACTION
→ CHATGPT FUTURE DESIGN/PACKAGING
→ SMALLER, CLEARER CLAUDE PACK
→ FEWER DEFECTS / LOWER TOKEN USE
```
