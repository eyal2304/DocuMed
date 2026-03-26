---
name: add-section
description: Add a new section to DocuMed's index.html following all project rules — Hebrew RTL, token-only CSS, mobile-first, semantic HTML, no external dependencies.
---

# Add Section — DocuMed

When this skill is invoked, add a new section to `index.html`.

## Step 1 — Gather requirements

Ask the user (in one message, all at once):

1. **שם הסקשן** — מה הסקשן עושה? (לדוגמה: "רשימת תרופות", "יומן תסמינים")
2. **רקע** — איזה background token? בחר מהרשימה:
   - `--bg-blue-soft` / `--bg-green-soft` / `--bg-purple-soft`
   - `--bg-pink-soft` / `--bg-orange-soft` / `--bg-teal-soft`
3. **אחרי מה?** — אחרי איזה סקשן קיים להכניס את החדש?
4. **תוכן** — מה יהיה בפנים? (כרטיסיות, טופס, רשימה, כפתורות?)

## Step 2 — Read the file first

Before writing anything:
- Read `index.html` to understand the existing structure and token values in `:root`.
- Identify the insertion point the user specified.

## Step 3 — Generate the section

Write the new section following ALL these rules:

### HTML rules
- Use `<section>` with `aria-labelledby` pointing to its heading `id`.
- Hebrew heading in `<h2>` or `<h3>`.
- Semantic child elements: `<article>` for cards, `<ul>/<li>` for lists, `<form>` for forms, `<button>` for actions.
- Every interactive element has an `aria-label` in Hebrew.
- No English visible to users — all strings in Hebrew.

### CSS rules
- Add new styles inside the existing `<style>` block — never create a new `<style>` tag.
- Use **only** `var(--token)` for colors, radius, shadows. Zero raw values.
- Use RTL-safe layout properties:
  - `margin-inline-start` / `margin-inline-end` (never margin-left/right)
  - `padding-inline-start` / `padding-inline-end`
  - `text-align: start` (never left/right)
- Mobile-first: base styles for 375px, then `@media (min-width: 640px)` for larger screens.
- Class naming: `.section-[name]`, `.section-[name]__[element]`, `.section-[name]--[modifier]`

### Structure template
```html
<!-- ── [SECTION NAME] ── -->
<section class="section-[name]" aria-labelledby="heading-[name]">
  <h2 id="heading-[name]" class="section-[name]__title">[Hebrew title]</h2>
  <!-- content here -->
</section>
```

```css
/* ── [SECTION NAME] ── */
.section-[name] {
  background: var(--bg-[color]-soft);
  border-radius: var(--radius-2xl);
  box-shadow: var(--shadow-sm);
  padding: 1.5rem;
}
.section-[name]__title {
  color: var(--color-neutral-800);
  font-size: 1.125rem;
  font-weight: 600;
  margin-block-end: 1rem;
}
```

## Step 4 — Insert into index.html

Use the `Edit` tool to insert the new HTML at the exact insertion point.
Use the `Edit` tool again to append the new CSS inside the existing `<style>` block.

**Never rewrite the whole file.**

## Step 5 — Verify

After inserting, confirm:
- [ ] New section is inside `<main>` (or the correct parent)
- [ ] No raw color/radius/shadow values in the new CSS
- [ ] No `margin-left`, `margin-right`, `text-align: left/right`
- [ ] All visible text is in Hebrew
- [ ] No new `<style>` or `<script>` tags were created
