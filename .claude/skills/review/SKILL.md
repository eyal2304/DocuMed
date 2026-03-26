---
name: review
description: Review DocuMed's index.html against all project rules — architecture, RTL, CSS tokens, Hebrew strings, accessibility, medical domain, and performance. Reports issues by severity.
---

# Code Review Agent — DocuMed

Run a full review of `index.html` against every DocuMed rule.

## Behavior

Read `index.html` in full, then run all checks below in order.
Report every finding — do not stop at first issue.
Do not fix anything unless the user explicitly asks after the review.

---

## Check 1 — Architecture

- [ ] All code is inside `index.html` — no `<link rel="stylesheet">` to local files, no `<script src>` to local files
- [ ] No external URLs in `<script src>`, `<link href>`, `@import`, `fetch()`, `XMLHttpRequest`
- [ ] No `<script type="module">` (implies build tooling mindset)
- [ ] File opens in browser without any server or install

---

## Check 2 — CSS Tokens

Read the `:root {}` block and extract all defined tokens.
Then scan all CSS outside `:root` for:

- [ ] Raw hex colors (`#xxx`, `#xxxxxx`) → should be `var(--color-*)`
- [ ] Raw `rgb()`, `rgba()`, `hsl()`, `hsla()`, `oklch()` → should be token
- [ ] Raw `border-radius` values (e.g. `8px`, `1rem`) → should be `var(--radius-*)`
- [ ] Raw `box-shadow` values → should be `var(--shadow-*)`

Report: how many violations, which lines, what token should replace them.

---

## Check 3 — RTL & Hebrew

CSS:
- [ ] Any `margin-left` / `margin-right` → should be `margin-inline-start/end`
- [ ] Any `padding-left` / `padding-right` → should be `padding-inline-start/end`
- [ ] Any `left:` / `right:` on positioned elements → should be `inset-inline-start/end`
- [ ] Any `text-align: left` / `text-align: right` → should be `start` / `end`
- [ ] Any `direction: ltr` without an inline comment explaining why

HTML:
- [ ] `<html>` has both `lang="he"` and `dir="rtl"`
- [ ] All user-visible text is in Hebrew — flag any English strings visible in UI
- [ ] Directional icons/arrows — are they mirrored for RTL?

---

## Check 4 — Accessibility

- [ ] Every `<img>` has `alt` attribute (in Hebrew, or `alt=""` if decorative)
- [ ] Every icon-only `<button>` has `aria-label` in Hebrew
- [ ] Every `<section>` has `aria-labelledby` pointing to a heading
- [ ] Every `<form>` input has an associated `<label>`
- [ ] No `outline: none` or `outline: 0` without a custom `:focus-visible` style replacing it
- [ ] `<main>` exists and appears once
- [ ] Heading hierarchy is logical (h1 → h2 → h3, no skips)
- [ ] Dynamic content regions have `aria-live="polite"` if they update without page reload
- [ ] Touch targets: are buttons/links likely to be ≥ 44px? (flag anything with explicit small sizes)

---

## Check 5 — Medical Domain

- [ ] No `fetch()`, `XMLHttpRequest`, or any network call that could send patient data
- [ ] No third-party analytics, error tracking, or telemetry scripts
- [ ] Any displayed health values (dosage, measurements) — do they show units?
- [ ] Any raw JS errors shown directly to the user? Should be caught and shown as calm Hebrew messages
- [ ] Any content that could be misread as medical advice or diagnosis?

---

## Check 6 — JavaScript Quality

- [ ] No `var` — only `const` / `let`
- [ ] No `document.getElementById` / `getElementsBy*` — use `querySelector`
- [ ] No `console.log` left in code
- [ ] `localStorage` / `IndexedDB` calls wrapped in `try/catch`
- [ ] Event listeners use delegation where N similar elements exist
- [ ] No inline `onclick=` attributes — use `addEventListener`

---

## Check 7 — Performance

- [ ] No CSS animations on `width`, `height`, `top`, `left`, `margin` — only `transform` and `opacity`
- [ ] No `*` selector except the top-level box-sizing reset
- [ ] `transition` durations ≤ 400ms
- [ ] No base64-encoded images > 50KB inline

---

## Output Format

Report results in this structure:

```
## Review Results — DocuMed index.html

### 🔴 Critical (fix before shipping)
- [Check category] [exact issue] → [suggested fix]

### 🟡 Warning (should fix)
- [Check category] [exact issue] → [suggested fix]

### 🟢 Passed
- [List checks that passed cleanly]

### Summary
X critical · Y warnings · Z passed
```

If everything passes: "✅ כל הבדיקות עברו — הקוד תואם את כללי DocuMed."

---

## After the report

Ask the user: "רוצה שאתקן את הבעיות הקריטיות?"
Wait for confirmation before touching any code.
