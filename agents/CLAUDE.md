# Agents — DocuMed

Instructions for how Claude should behave as an agent on this project.

---

## Core Agent Identity

You are working on **DocuMed** — a single-file Hebrew RTL web app for chronic disease management.

- All code lives in one file: `index.html`
- Stack: vanilla HTML + CSS + JS. No frameworks. No build tools.
- Language: Hebrew. RTL layout. oklch color system.
- Users: Hebrew-speaking patients. Tone must be warm, not clinical.

Always load and respect the full rule set before making any change:
- `@ruls/CLAUDE.md` — hard constraints
- `@frontend/CLAUDE.md` — code style
- `@skills/CLAUDE.md` — prompt patterns

---

## Default Behavior

**When asked to add a feature:**
1. Read the relevant section of `index.html` first.
2. Follow token-only styling — never introduce raw values.
3. Return only the changed block, not the full file, unless explicitly asked.
4. All new strings in Hebrew.

**When asked to fix a bug:**
1. Identify the minimal change needed.
2. Do not refactor surrounding code.
3. Explain root cause in one sentence before showing the fix.

**When asked to review code:**
1. Check against the checklist in `@skills/CLAUDE.md` → Code Review section.
2. Report issues only — do not rewrite unless asked.

**When asked to write copy / text:**
1. Hebrew only. Warm tone. No clinical jargon.
2. Cover all states: default, success, error, empty.

---

## What to Always Verify Before Editing

- [ ] Is the edit inside `index.html` only?
- [ ] Do all CSS values use `var(--token)`?
- [ ] Are all new strings in Hebrew?
- [ ] Does layout use RTL-safe properties (`inline-start/end`, `text-align: start`)?
- [ ] Are new interactive elements keyboard accessible with Hebrew aria labels?
- [ ] Will this work offline (no external fetch required)?

---

## What NOT to Do

- Never create separate `.css`, `.js`, or `.html` files.
- Never add `<link>` or `<script src>` tags pointing to external resources.
- Never use a framework (React, Vue, Alpine, HTMX, etc.).
- Never use `npm`, `node`, or any terminal build command.
- Never show English text to the user.
- Never bypass token variables with raw values.
- Never suppress errors silently — always show a Hebrew fallback message to users.

---

## Response Style for This Project

- Be concise. This is a focused single-file project.
- Show only changed code unless a full view is needed.
- Use inline comments in Hebrew for any logic that isn't self-evident.
- Flag any decision that touches patient data privacy or medical accuracy.
