---
name: DocuMed architecture rules
description: Single-file constraint, no build tools, no external dependencies
type: project
---

**Rule: everything stays in `index.html`.**

- Never create separate `.css`, `.js`, or template files.
- Never add `<link rel="stylesheet">` or `<script src>` pointing to local files.
- No npm, no package.json, no node_modules.
- No webpack, Vite, Rollup, Parcel, Babel, TypeScript — no transpiler of any kind.
- No CDN links, no Google Fonts, no third-party scripts.
- App must open by double-clicking in any browser with zero setup.
- App must work fully offline with no network connection.

**Why:** Hospital IT environments often block installs and external network access. Single-file = zero friction adoption.

**How to apply:** Before any edit, verify you are only touching `index.html`. If a feature "needs" a second file — find a way to do it inline instead.
