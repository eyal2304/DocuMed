---
name: DocuMed Hebrew and RTL rules
description: Hebrew-first strings, RTL layout properties, font stack, directional icons
type: project
---

**Every user-visible string must be in Hebrew. No English placeholders ever.**

**HTML:**
- `lang="he" dir="rtl"` on `<html>` — not only `<body>`.

**CSS:**
- `direction: rtl` in body CSS (attribute + CSS both required).
- `text-align: start` as default (never hardcode `left`/`right`).
- Use logical properties everywhere:
  - `margin-inline-start` / `margin-inline-end`
  - `padding-inline-start` / `padding-inline-end`
  - `inset-inline-start` / `inset-inline-end`
- Never add `direction: ltr` without an inline comment explaining why.

**Typography:**
- Font stack: `ui-sans-serif, system-ui, sans-serif` — no web font load needed, renders Hebrew natively.

**Icons:**
- Directional arrows/chevrons must be mirrored for RTL via `transform: scale(-1, 1)`.

**Why:** Retrofitting RTL is expensive. Hebrew-first from day one prevents a whole class of layout bugs.
