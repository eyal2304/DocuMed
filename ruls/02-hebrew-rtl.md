# Rule: Hebrew & RTL

## HTML
- `lang="he" dir="rtl"` must be on `<html>` — not only `<body>`.
- Every user-visible string must be in Hebrew. No English placeholders, ever.

## CSS
- `direction: rtl` in body CSS — both attribute and CSS are required.
- Text alignment defaults to `text-align: start` (RTL-safe).
- Never hardcode `left` / `right` — use logical properties instead:
  - `margin-inline-start` / `margin-inline-end`
  - `padding-inline-start` / `padding-inline-end`
  - `inset-inline-start` / `inset-inline-end`
  - `text-align: start` / `end`
- Never add `direction: ltr` without an inline comment explaining why.

## Typography
- Font stack: `ui-sans-serif, system-ui, sans-serif`
- Renders natively for Hebrew on all platforms — no web font needed.

## Icons & Directional Visuals
- Arrows and chevrons that indicate direction must be mirrored for RTL.
- Use CSS `transform: scale(-1, 1)` or provide separate RTL assets.
