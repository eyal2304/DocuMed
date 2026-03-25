# Frontend & Code Style — DocuMed

Guidelines for writing HTML, CSS, and JS inside `index.html`.

---

## HTML Style

- **Indentation:** 2 spaces. No tabs.
- **Attribute order:** `id` → `class` → `type` → `aria-*` → `data-*` → event handlers.
- **Boolean attributes:** no value needed — write `disabled` not `disabled="true"`.
- **Self-closing:** void elements (`<input>`, `<img>`, `<br>`) do not get a slash.
- **Quotes:** always double quotes for attribute values.
- **Semantic structure:**
  ```html
  <header> → site header / nav
  <main>   → one per page, primary content
  <section> → named content regions (add aria-labelledby)
  <article> → self-contained repeating units (cards, list items)
  <aside>  → secondary info, tooltips, side panels
  <footer> → page footer
  ```
- Every `<img>` needs `alt` in Hebrew. Decorative images get `alt=""`.
- Every interactive element needs an accessible label in Hebrew (visible label or `aria-label`).

---

## CSS Style

### Token System (never bypass these)

```css
/* Colors */
var(--color-teal-400)      /* brand light */
var(--color-teal-500)      /* brand default */
var(--color-neutral-50)    /* bg lightest */
var(--color-neutral-100)   /* page bg */
var(--color-neutral-200)   /* borders */
var(--color-neutral-300)   /* dividers */
var(--color-neutral-400)   /* placeholder text */
var(--color-neutral-500)   /* secondary text */
var(--color-neutral-600)   /* body text */
var(--color-neutral-700)   /* strong text */
var(--color-neutral-800)   /* headings */
var(--color-neutral-900)   /* max contrast */
var(--color-red-500)       /* errors / danger */

/* Section backgrounds */
var(--bg-blue-soft)
var(--bg-green-soft)
var(--bg-purple-soft)
var(--bg-pink-soft)
var(--bg-orange-soft)
var(--bg-teal-soft)

/* Radius */
var(--radius-xl)    /* cards, inputs */
var(--radius-2xl)   /* modals, large panels */

/* Shadows */
var(--shadow-sm)    /* cards */
var(--shadow-md)    /* modals, dropdowns */
var(--shadow-lg)    /* overlays, drawers */
```

### CSS Naming

- BEM-lite: `.component`, `.component__element`, `.component--modifier`
- No generic names like `.box`, `.wrapper`, `.container` — use purpose names: `.card-condition`, `.header-main`.
- State classes: `.is-active`, `.is-disabled`, `.is-loading` (always `is-` prefix).
- JS hooks: `.js-toggle`, `.js-submit` — never style these, only use in JS.

### CSS Property Order (within each rule)

1. `display`, `visibility`, `content`
2. `position`, `top/right/bottom/left`, `z-index`
3. `width`, `height`, `min-*`, `max-*`
4. `margin`, `padding`
5. `flex`/`grid` properties
6. `font-*`, `text-*`, `line-height`, `color`
7. `background`, `border`, `border-radius`, `box-shadow`
8. `transition`, `animation`
9. `cursor`, `pointer-events`, `user-select`

### RTL CSS Rules

- Use `margin-inline-start` / `margin-inline-end` instead of `margin-left` / `margin-right`.
- Use `padding-inline-start` / `padding-inline-end` for directional padding.
- Use `inset-inline-start` / `inset-inline-end` for positioned elements.
- Use `text-align: start` / `end` instead of `left` / `right`.

---

## JavaScript Style

- **No frameworks.** Vanilla JS only.
- **No `var`** — use `const` by default, `let` only when reassignment is needed.
- **Arrow functions** for callbacks; named `function` declarations for top-level functions.
- **`querySelector` / `querySelectorAll`** — never use `getElementById` or `getElementsBy*`.
- **Event delegation** — attach one listener to a parent, not N listeners to N children.
- **DOM updates** — batch reads before writes to avoid layout thrash.
- **Data storage** — use `localStorage` for simple key-value; use IndexedDB (via a thin wrapper) for structured data.
- **Error handling** — every `localStorage` or IndexedDB call wrapped in try/catch; show Hebrew fallback on failure.
- **No `console.log` in production code** — remove before committing.

### Function naming

```js
// Actions: verb + noun
function saveCondition(data) {}
function loadConditions() {}
function deleteCondition(id) {}
function renderConditionCard(condition) {}

// Predicates: is / has / can
function isValidDate(str) {}
function hasUnsavedChanges() {}

// Event handlers: on + element + event
function onSaveButtonClick(e) {}
function onFormSubmit(e) {}
```

### JS Structure inside `<script>`

Organize code in this order:
```js
// 1. Constants & config
// 2. State (module-level variables)
// 3. Data layer (storage read/write)
// 4. Render functions (DOM output)
// 5. Event handlers
// 6. Init (runs on DOMContentLoaded)
```

---

## Accessibility Checklist

Before any new feature ships:

- [ ] All interactive elements reachable by keyboard (Tab order makes sense in RTL)
- [ ] Focus visible — never `outline: none` without a custom focus style
- [ ] `aria-label` in Hebrew on icon-only buttons
- [ ] Dynamic content changes announced via `aria-live="polite"`
- [ ] Color contrast: text on background ≥ 4.5:1 (AA)
- [ ] Touch targets ≥ 44×44px on mobile

---

## Performance Rules

- No images larger than 50 KB inline (use SVG or CSS shapes instead).
- Animations use `transform` and `opacity` only — never animate `width`, `height`, `top`, `left`.
- `transition` max 250ms for UI feedback; 400ms for entrance animations.
- Avoid `*` selector in CSS except for box-sizing reset at top.
