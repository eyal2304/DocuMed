---
name: refactor
description: Refactor a component in DocuMed's index.html — improve structure, reduce repetition, or improve accessibility, without changing behavior.
---

# Refactor — DocuMed

## Step 1 — Understand the goal

Ask the user (if not already provided):
1. **מה לשפר?** — לדוגמה: "להפחית חזרות", "לשפר נגישות", "לנקות CSS", "לאחד event listeners"
2. **איזה קומפוננט?** — שם הסקשן או ה-class הרלוונטי
3. **מה לא לשנות?** — כל התנהגות קיימת נשמרת בדיוק כמו שהיא

## Step 2 — Read the component

Read `index.html` — specifically the target component's HTML, CSS, and JS.

Before suggesting anything, document:
- Current structure (2–3 lines summary)
- What is repeated / problematic
- What is working and must stay identical

## Step 3 — Plan the refactor

List every change you intend to make:
- `[CSS] הסר border-radius: 8px שלוש פעמים → var(--radius-xl) בכלל אחד`
- `[JS] אחד שלושה event listeners → event delegation אחד על ה-parent`
- etc.

**Hard limits:**
- Zero behavior change — same user-visible outcome
- No new features added
- No new external dependencies
- All CSS must still use `var(--token)` only
- All layout must still use RTL-safe properties
- All visible strings must stay in Hebrew

Get confirmation: "אלה השינויים המתוכננים — להמשיך?"

## Step 4 — Apply changes

Use `Edit` for each change. One logical change per `Edit` call.

## Step 5 — Verify

After all edits:
- [ ] No behavior change (interactions work the same)
- [ ] No raw CSS values introduced
- [ ] No RTL violations introduced
- [ ] No Hebrew strings removed or changed to English
- [ ] Code is shorter or cleaner than before

Report: "ריפקטורינג הושלם — [N] שינויים, אפס שינויי התנהגות"
