# GĐ0 Intake + Environment / Resource Readiness Protocol — v3.0

## Purpose

GĐ0 prevents the project from entering UI production while basic project, environment, layout, data or asset authority is still unknown.

Core rule:

```text
READ EXISTING EVIDENCE FIRST
ASK ONLY MATERIAL GAPS
CONFIRM ENVIRONMENT / RESOURCE ACCESS
DO NOT SILENTLY ASSUME A MAJOR LAYOUT MODE
START DESIGN ONLY WHEN THE REMAINING GAPS ARE SAFE
```

User-facing rule: if an English or specialist term is used, explain in plain Vietnamese what it means and what it is used for when the term first matters.

---

## 1. Inspect before asking

Before asking the user anything, ChatGPT MUST inspect all available inputs that may already answer the brief, including when supplied:

- current conversation and earlier accepted decisions;
- screenshots, PDFs, Figma, video, website references;
- current website and implementation context;
- brand/logo/font/color assets;
- product/property/project/news content;
- real photos, floorplans, maps, progress images and data visuals;
- repository URL, branch, project structure and current stack;
- CMS/Sheets/API/database information;
- deployment/preview information;
- audience, conversion goal and business priorities;
- desired desktop/mobile/wide-screen behavior;
- user likes/dislikes and fidelity target.

Never ask the user to repeat information already sufficiently known.

---

## 2. Project brief map

When a project repository is available, normalize useful state into:

```text
.webby/PROJECT_INTAKE.json
```

Recommended categories:

```text
PROJECT IDENTITY
BUSINESS / OFFER
PRIMARY GOAL
CONVERSION GOAL
TARGET AUDIENCE
BUSINESS PRIORITY
BRAND
CONTENT / DATA
SOURCE ASSETS
REFERENCES / VISUAL AUTHORITY
ROUTES / FEATURES
LAYOUT MODE
RESPONSIVE EXPECTATIONS
MOTION EXPECTATIONS
CMS / ADMIN / DATA
REPOSITORY / BRANCH
REMOTE / LOCAL DRIFT STATUS
GOOGLE DRIVE ACCESS
VERCEL / PREVIEW NEED
ENV / SECRETS READINESS
MUST-HAVE
MUST-NOT-HAVE
ASSUMPTIONS
OPEN QUESTIONS
BLOCKERS
```

Field status:

```text
KNOWN
ASSUMED
SOFT_GAP
HARD_GAP
NOT_APPLICABLE
```

Definitions:

- `KNOWN`: directly supplied or reliably evidenced.
- `ASSUMED`: safe temporary assumption that does not materially distort UI/implementation; record visibly.
- `SOFT_GAP`: can be resolved later without forcing redesign/rework.
- `HARD_GAP`: can materially change UI direction, asset count, implementation, business hierarchy or layout.
- `NOT_APPLICABLE`: irrelevant to this project.

---

## 3. Mandatory environment/resource readiness questions when not already known

Ask only the missing applicable items:

```text
Which GitHub repo is authoritative?
Which branch will Claude work on?
Can ChatGPT read the remote repo?
Can Claude read/write the repo?
Does Claude have local unpushed work that differs from remote?
Is Google Drive connected and can Claude download the asset folder?
Is Vercel preview needed for user review, or is local review sufficient?
What CMS / Sheets / API / database source is authoritative?
Are any env/secrets required before the affected feature can run?
```

Definitions for user-facing explanations when needed:

- **Repo / repository**: kho chứa source code của dự án. Tác dụng: mọi người cùng làm trên đúng code.
- **Branch**: nhánh code riêng. Tác dụng: sửa mà chưa ảnh hưởng bản chính.
- **Remote**: trạng thái code đã đẩy lên GitHub. Tác dụng: ChatGPT có thể đọc được trạng thái chung này.
- **Local**: code trên máy Claude/chủ dự án. Tác dụng: có thể chứa thay đổi chưa push mà ChatGPT chưa thấy.
- **Vercel**: nền tảng deploy website. Tác dụng: tạo link online để chạy/preview; không bắt buộc chỉ để bắt đầu code.
- **Deploy**: đưa website lên môi trường có thể truy cập/chạy thật.
- **CMS**: hệ quản trị nội dung. Tác dụng: người quản trị nhập/sửa dữ liệu mà không sửa code.
- **Environment variable / env**: cấu hình bí mật hoặc theo môi trường. Tác dụng: kết nối API/database/service mà không hardcode thông tin nhạy cảm.

---

## 4. Mandatory major layout decision

The intake must know the applicable layout mode before final design when it materially affects composition:

```text
FULL_WIDTH
FULL_BLEED_WITH_CONTAINER
BOXED
MIXED
```

Definitions:

- `FULL_WIDTH`: content/layout intentionally uses the available screen width.
- `FULL_BLEED_WITH_CONTAINER`: background/media can reach the viewport edges while readable content remains constrained.
- `BOXED`: most page content is constrained inside a centered maximum-width container.
- `MIXED`: route/section-specific combination.

If the reference does not establish this and the choice can materially change the UI, ChatGPT MUST ask the user. Do not silently inherit a generic 1200/1240px container.

---

## 5. Asset/data authority discovery

Before GĐ2 asset counting, identify:

```text
which assets already exist
which are real/authentic
which can be demo/generated
which must never be fabricated
which source is authoritative
whether source resolution is adequate
whether logo/icon has native/vector source
```

Typical no-fabrication categories:

```text
floorplans
maps that claim factual location/data
construction progress for a named real project
specific property photos claimed as authentic
brand marks when an original exists
regulated/factual diagrams
```

Do not let the executor solve these gaps later.

---

## 6. Adaptive question loop

If material gaps remain:

```text
INSPECT
↓
NORMALIZE KNOWN FACTS
↓
IDENTIFY MATERIAL GAP
↓
ASK THE SMALLEST USEFUL QUESTION SET
↓
MERGE ANSWER
↓
RE-EVALUATE
```

Question rules:

1. Ask only questions that can change UI, asset requirements, scope, content hierarchy or implementation readiness.
2. Do not dump a generic 20-question form.
3. Prefer concrete choices when useful, e.g. `full-width / full background + container / boxed`.
4. Ask in the user's language.
5. Explain necessary specialist terms simply.
6. Never ask a question already answered by supplied evidence.
7. Do not block on a harmless `SOFT_GAP`.
8. Never silently invent a `HARD_GAP` answer.

---

## 7. GĐ0 completion gate

Set:

```text
INTAKE_COMPLETE = true
```

only when the applicable items are sufficiently known:

```text
[ ] all available inputs were inspected
[ ] project/business/offer is understood
[ ] audience and primary/conversion goal are sufficiently known
[ ] business/content priority is sufficiently known
[ ] routes/features scope is known enough for decomposition
[ ] reference/visual authority is known
[ ] layout mode is known or safely not material yet
[ ] asset/data authority status is known enough to count assets
[ ] repo/branch/access state is known when implementation will use an existing repo
[ ] remote/local drift risk is recorded when applicable
[ ] Drive availability/access is known when heavy asset handoff is expected
[ ] preview/deployment requirement is known when material
[ ] no unresolved HARD_GAP would force likely redesign/rework
```

If a material `HARD_GAP` remains:

```text
INTAKE_COMPLETE = false
DO NOT ENTER FINAL UI/ASSET PRODUCTION
```

---

## 8. Output

Keep the user-facing summary concise:

```text
PROJECT BRIEF LOCKED
- goal / priority
- routes/scope
- reference authority
- layout mode
- asset/data authority status
- repo/branch/Drive/preview status
- remaining safe assumptions

INTAKE_COMPLETE = true
NEXT = UI DECOMPOSITION + ASSET COUNT
```

Do not restart discovery from zero after this point. Update only the affected fields when new information arrives.
