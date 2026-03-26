---
name: debug-visual
description: Debug a visual or layout bug in DocuMed — misaligned RTL elements, broken spacing, wrong colors, overlapping content, or animation glitches.
---

# Debug Visual — DocuMed

## Step 1 — Describe the problem

Ask the user (if not provided):
1. **מה נראה?** — תאר מה נראה לא נכון (לדוגמה: "הכפתור יושב בצד שמאל", "הצל חסר", "הטקסט חורג מהגבול")
2. **איפה?** — איזה סקשן / קומפוננט / מסך?
3. **מתי?** — רק במובייל? רק ב-hover? תמיד?
4. **ציפייה** — מה היית מצפה לראות?

## Step 2 — Diagnose category

Based on the description, identify the likely category:

### A — RTL Layout Bug
Symptoms: element appears on wrong side, arrow points wrong direction, text starts from wrong edge.
Check: `margin-left/right` instead of `inline-start/end`, missing `direction: rtl`, `text-align: left` instead of `start`, flexbox `row` vs `row-reverse` in RTL.

### B — Token / Color Bug
Symptoms: wrong color, color doesn't match surrounding elements, missing border or shadow.
Check: raw hex/rgb instead of `var(--token)`, token name typo, token not defined in `:root`, dark-mode conflict.

### C — Spacing / Sizing Bug
Symptoms: too much/little space, element too small/large, text overflows.
Check: hardcoded `px` values, missing `box-sizing: border-box`, `min-width` conflicts, `overflow: hidden` cutting content.

### D — Z-index / Overlap Bug
Symptoms: element hidden behind another, modal not on top, dropdown cut off.
Check: missing `position: relative` on parent, `overflow: hidden` on ancestor, z-index value.

### E — Animation / Transition Bug
Symptoms: jerky motion, element jumps, transition doesn't fire.
Check: animating `width/height/top/left` instead of `transform/opacity`, missing `transition` property, `prefers-reduced-motion` blocking animation.

## Step 3 — Read the relevant code

Read `index.html` — specifically the CSS and HTML for the affected component.

## Step 4 — Diagnose

State clearly:
- **Root cause:** [one sentence — what is wrong in the code]
- **Category:** [A/B/C/D/E from above]
- **Line(s):** [exact line numbers]

## Step 5 — Fix

Apply the minimal fix using `Edit`.

Rules:
- Fix only the visual issue — do not refactor
- Keep all `var(--token)` usage
- Keep all RTL-safe properties
- If the fix changes a value: explain why the new value is correct

## Step 6 — Verify

Re-read the changed lines and confirm:
- [ ] Root cause addressed
- [ ] No new raw values introduced
- [ ] No new RTL violations
- [ ] Nothing else visually affected

Report: "תוקן: [מה תוקן] — [קטגוריה] bug בשורה X"
