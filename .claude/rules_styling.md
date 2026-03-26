---
name: DocuMed styling rules
description: Token-only CSS values, mobile-first breakpoints, semantic HTML elements
type: project
---

**Token-only styling — raw values forbidden outside `:root`.**

Always use `var(--token)`. Never write raw colors, radius, or shadow values in component CSS.

Key tokens:
- Brand: `--color-teal-400`, `--color-teal-500`
- Text/bg scale: `--color-neutral-50` → `--color-neutral-900`
- Danger: `--color-red-500`
- Section backgrounds: `--bg-blue-soft`, `--bg-green-soft`, `--bg-purple-soft`, `--bg-pink-soft`, `--bg-orange-soft`, `--bg-teal-soft`
- Radius: `--radius-xl` (cards/inputs), `--radius-2xl` (modals)
- Shadows: `--shadow-sm` (cards), `--shadow-md` (modals), `--shadow-lg` (overlays)

**Mobile-first:**
- Base styles target 375px. Scale up with `min-width` media queries.
- Touch targets ≥ 44×44px.

**Semantic HTML — never `<div>` when a semantic element fits:**
- `<nav>`, `<main>` (one per page), `<section>` (+ `aria-labelledby`), `<article>`, `<button>`, `<a>`

**Why:** Token system lets one `:root` change update the entire UI — critical for client customization in medical software.
