---
name: DocuMed open questions
description: Unresolved design decisions — must be answered before writing related code
type: project
---

Do not write code that depends on these until they are resolved. Ask the user first.

- **Data model** — what fields per chronic condition? (name, diagnosis date, medications, dosage, notes, severity?)
- **Storage engine** — localStorage vs. IndexedDB? Decide before any persistence code.
- **Date format** — DD/MM/YYYY or relative ("לפני 3 ימים") or both? Must be consistent app-wide.
- **Offline indicator** — badge, banner, or silent when no network?
- **Export / backup** — can a patient export their data? What format — JSON, PDF?
- **Accessibility review** — NVDA + Chrome with Hebrew screen reader before first release.

**How to apply:** If a task touches storage, dates, or data model — check this list first and surface the relevant question to the user before proceeding.
