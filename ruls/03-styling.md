# Rule: Styling

## Token-Only
- Raw color, radius, and shadow values are **forbidden** anywhere except `:root`.
- Always reference via `var(--token-name)`.
- Adding a new value? Add it to `:root` first, then reference the token.

## Mobile-First
- Design and test at 375px width first.
- Scale up to larger screens with `min-width` media queries only.
- Touch targets must be at least 44×44px.
- No desktop-only assumptions in base styles.

## Semantic HTML
- Use correct elements — never `<div>` when a semantic element exists:
  - `<nav>` for navigation
  - `<main>` for primary content (one per page)
  - `<section>` for named regions (add `aria-labelledby`)
  - `<article>` for repeating self-contained units (cards, list items)
  - `<button>` for actions (never `<div onclick>`)
  - `<a>` for navigation (never `<div onclick>`)
