---
name: fix
description: Fix a specific bug in DocuMed's index.html — diagnose root cause, apply minimal fix, verify nothing broke.
---

# Bug Fix — DocuMed

## Step 1 — Understand the bug

Ask the user (if not already provided):
1. **מה הבעיה?** — תאר מה קורה לעומת מה שאמור לקרות.
2. **איפה?** — באיזה חלק של האפליקציה? (שם הסקשן / פעולה שמפעילה את הבאג)
3. **מתי?** — בעת לחיצה? טעינה? שמירה? גלילה?

## Step 2 — Read before touching

Read the relevant section of `index.html`.
- Find the exact lines responsible for the behavior.
- Identify root cause — one sentence.

## Step 3 — Plan the minimal fix

Before writing code:
- Write one sentence: **Root cause:** [what is wrong]
- Write one sentence: **Fix:** [what will change]
- Confirm: does this fix require changing JS, CSS, or HTML (or a combination)?

Do **not** refactor surrounding code. Do **not** rename things. Do **not** add new features.

## Step 4 — Apply the fix

Use `Edit` with the smallest possible change.

Rules:
- One `Edit` call per logical change
- Preserve indentation and quote style
- If fix is in CSS: use only `var(--token)` — no raw values
- If fix is in JS: wrap any new storage calls in try/catch with Hebrew fallback
- If fix adds visible text: Hebrew only

## Step 5 — Verify

After the fix, re-read the changed lines and confirm:
- [ ] Root cause is addressed
- [ ] No raw color/radius/shadow values introduced
- [ ] No `margin-left/right` or `text-align: left/right` introduced
- [ ] No English strings visible to the user
- [ ] No surrounding code was changed accidentally

Report: "תוקן: [מה תוקן] — שורה X"
