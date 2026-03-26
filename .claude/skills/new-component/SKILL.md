---
name: new-component
description: Design and build a reusable UI component for DocuMed — card, badge, modal, drawer, toast, or tag — using only project tokens.
---

# New Component — DocuMed

## Step 1 — Define the component

Ask the user (if not already provided):
1. **סוג** — card / badge / modal / drawer / toast / tag / אחר?
2. **שימוש** — איפה ישמש? (לדוגמה: "כרטיסיית תרופה", "תג חומרת מחלה", "חלון אישור מחיקה")
3. **מצבים** — אילו מצבים צריך? (default, hover, active, disabled, loading, error)
4. **תוכן** — מה יהיה בפנים? (טקסט, אייקון, כפתור, badge?)

## Step 2 — Read the file

Read `index.html` to understand existing patterns and available tokens in `:root`.

## Step 3 — Design the component

### Anatomy

Define the HTML structure:
```
[component-name]            ← root element
├── [component]__header     ← (if needed)
├── [component]__body       ← main content
└── [component]__actions    ← (if needed, buttons/links)
```

BEM naming: `.component-[name]`, `.component-[name]__[element]`, `.component-[name]--[modifier]`

### Token mapping

Map every visual property to a token:
- Background → `var(--bg-*-soft)` or `var(--color-neutral-*)`
- Text → `var(--color-neutral-*)`
- Border → `var(--color-neutral-200)`
- Radius → `var(--radius-xl)` or `var(--radius-2xl)`
- Shadow → `var(--shadow-sm)` or `var(--shadow-md)`
- Focus ring → `var(--color-teal-500)`

**No raw values. Ever.**

### States

For each required state, define CSS using modifiers or pseudo-classes:
- `:hover` → lighten background via token
- `:focus-visible` → `outline: 2px solid var(--color-teal-500); outline-offset: 2px`
- `.is-disabled` → `opacity: 0.5; pointer-events: none`
- `.is-loading` → add spinner using `border` + `animation: spin`

### RTL

- All padding/margin: `inline-start/end` only
- Text: `text-align: start`
- Directional icons: note which ones need `transform: scaleX(-1)` in RTL

### Mobile-first

- Base styles: 375px
- Touch targets for interactive variants: min 44×44px
- Scale up with `@media (min-width: 640px)` only

## Step 4 — Write and insert

Output both HTML (usage example) and CSS (component definition).

Use `Edit` to append the component CSS inside the existing `<style>` block.
If the component needs JS (modal open/close, toast dismiss), append to `<script>`.

**Never rewrite the whole file.**

## Step 5 — Verify

- [ ] All CSS uses `var(--token)` — zero raw values
- [ ] `:focus-visible` style is present for interactive variants
- [ ] RTL-safe properties throughout
- [ ] All visible text in Hebrew
- [ ] Touch target ≥ 44px where clickable
- [ ] Reduced-motion safe (no mandatory animation without `prefers-reduced-motion` check)
