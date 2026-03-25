# DocuMed — Claude Project Root

**DocuMed** — אפליקציית ניהול מחלות כרוניות בעברית.
Single-file HTML · RTL · oklch design tokens · Vanilla JS · No build tools.

---

## Sub-files (always load these)

- **Rules & constraints:** @ruls/CLAUDE.md
- **Frontend & code style:** @frontend/CLAUDE.md
- **Prompt library / skills:** @skills/CLAUDE.md
- **Agent behavior:** @agents/CLAUDE.md

---

## Project Snapshot

| Item | Value |
|---|---|
| Main file | `index.html` |
| Language | Hebrew (עברית), RTL |
| Color system | oklch() tokens via CSS custom properties |
| Data storage | localStorage / IndexedDB (browser only, no backend) |
| Target users | Hebrew-speaking patients, ages 40–70 |
| Delivery | Single file — shareable, offline-capable |

---

## ROI Highlights (Feb 23 – Mar 23 2026)

| Win | Why it mattered |
|---|---|
| RTL + oklch token system | Zero LTR/RTL conflicts; dark-mode-safe without extra work |
| Single-file architecture | No infra needed; works in any hospital environment |
| CSS design token system | One `:root` change updates the whole UI |

---

*Last updated: 2026-03-23*
