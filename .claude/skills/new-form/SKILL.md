---
name: new-form
description: Add a new form to DocuMed's index.html — Hebrew labels, RTL layout, accessible inputs, LocalStorage save, validation with Hebrew error messages.
---

# New Form — DocuMed

## Step 1 — Gather requirements

Ask the user (all at once):
1. **מטרת הטופס** — לדוגמה: "הוספת תרופה", "עדכון מחלה כרונית", "רישום תסמין"
2. **שדות** — אילו שדות נדרשים? (טקסט, תאריך, מספר, בחירה מרשימה?)
3. **שמירה** — לאן נשמר הטופס? (localStorage? מה שם המפתח?)
4. **אחרי שמירה** — מה קורה? (הודעת הצלחה, איפוס שדות, ניווט?)

## Step 2 — Read the file

Read `index.html` to understand:
- The existing form patterns (if any)
- The `:root` tokens available
- Where to insert the new form

## Step 3 — Generate the form

### HTML rules
- `<form>` element with `novalidate` (we handle validation in JS)
- Each field: `<label>` + `<input>` / `<select>` / `<textarea>` pair
- `label` uses `for="[id]"`, input uses matching `id`
- All labels and placeholders in Hebrew
- Error messages: `<span class="form__error" role="alert" aria-live="polite">` per field
- Submit: `<button type="submit">` with Hebrew label
- Cancel/reset: `<button type="button">` if needed

### CSS rules
- Token-only: `var(--color-*)`, `var(--radius-xl)`, `var(--shadow-sm)`
- RTL: `padding-inline-start/end`, `text-align: start`
- Input focus: `outline: 2px solid var(--color-teal-500)`
- Error state: `border-color: var(--color-red-500)`
- Mobile-first: full-width inputs on 375px

### JS rules
```js
// Validation — check before save
function validateFormName(data) {
  const errors = {};
  if (!data.fieldName) errors.fieldName = 'שדה חובה';
  return errors;
}

// Save to localStorage
function saveFormName(data) {
  try {
    const existing = JSON.parse(localStorage.getItem('key') || '[]');
    existing.push({ ...data, id: Date.now() });
    localStorage.setItem('key', JSON.stringify(existing));
    return true;
  } catch {
    showError('לא ניתן לשמור את הנתונים. נסה שוב.');
    return false;
  }
}

// Handler
function onFormNameSubmit(e) {
  e.preventDefault();
  // read fields, validate, save, give feedback
}
```

## Step 4 — Insert into index.html

Use `Edit` to insert HTML at the correct location.
Use `Edit` to append CSS inside the `<style>` block.
Use `Edit` to append JS inside the `<script>` block.

**Never rewrite the whole file.**

## Step 5 — Verify

- [ ] Every input has a matching `<label>`
- [ ] Error messages use `role="alert"` and are in Hebrew
- [ ] localStorage calls are in try/catch with Hebrew fallback
- [ ] No raw CSS values — only `var(--token)`
- [ ] No `margin-left/right` or `text-align: left/right`
- [ ] Submit button is `<button type="submit">`, not a `<div>`
