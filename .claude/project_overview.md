---
name: DocuMed project overview
description: What DocuMed is, its stack, and how it is delivered
type: project
---

**DocuMed** — Hebrew RTL web app for chronic disease management (ניהול מחלות כרוניות).

- Main file: `index.html` (single file, everything inline)
- Stack: vanilla HTML + CSS + JS. No frameworks, no build tools.
- Color system: oklch() tokens via CSS custom properties in `:root`
- Language: Hebrew, RTL (`lang="he" dir="rtl"` on `<html>`)
- Data storage: browser only — localStorage / IndexedDB, no backend
- Target users: Hebrew-speaking patients, ages 40–70
- Delivery: single shareable file, fully offline-capable

**Why:** Lowers barrier for hospital IT adoption — no install, no infra, no network required.

**Rule files live in:** `ruls/`, `frontend/`, `skills/`, `agents/` — each with its own `CLAUDE.md`.
