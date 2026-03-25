# Skills / Prompt Library — DocuMed

Ready-to-use prompts for common tasks on this project. Copy, fill in `[brackets]`, paste.

---

## Feature Development

### Add a new section

```
Add a [feature name] section to this single-file Hebrew RTL medical app.

Requirements:
- Match existing oklch color tokens and radius/shadow scale from :root
- RTL layout (direction: rtl, inline-* properties)
- No external dependencies
- Mobile-first starting at 375px
- Semantic HTML with Hebrew aria labels
- Section background: var(--bg-[color]-soft)

Insert the new HTML block after [existing section name].
Return only the new HTML + CSS additions. No full-file rewrite.
```

### Refactor a component

```
Refactor the [component name] in this single-file HTML app.
Goal: [what to improve — e.g., "reduce repetition", "improve accessibility", "extract to reusable pattern"].
Constraints: stay single-file, keep all existing token variables, no behavior change.
Show only the changed lines with brief before/after diff comments.
```

---

## Styling & Design

### Build a new UI component

```
Design a [component type — e.g., card, modal, form, badge] for a Hebrew RTL medical app.
Style using only these CSS tokens: [paste relevant :root variables].
States needed: default, hover, focus, disabled, [any other].
Mobile size: 375px. Return HTML + CSS only.
```

### Debug a visual issue

```
This Hebrew RTL single-file app has a visual bug: [describe what looks wrong].
Likely cause: RTL direction, oklch color value, or flexbox/grid layout.
Relevant code: [paste section].
Diagnose root cause. Provide minimal CSS fix. No refactoring.
```

---

## Content & Copy

### Write Hebrew UI microcopy

```
Write Hebrew UI microcopy for a chronic disease management app.
Tone: warm, clear, reassuring — not clinical or alarming.
Target users: Hebrew-speaking patients aged 40–70.
Feature: [feature name].
Provide for each state:
- Button / action labels
- Empty state message
- Success message
- Error message (calm, no jargon)
- Tooltip / helper text
Output: Hebrew only. No transliteration.
```

### Translate English UI text to Hebrew

```
Translate these UI strings to Hebrew for a medical app.
Tone: professional but warm. Not overly formal.
Strings: [list them].
For each: provide the translation + a note if there's a better idiomatic alternative.
```

---

## Accessibility

### Full accessibility audit

```
Audit this Hebrew RTL HTML for accessibility issues:
1. aria labels — present and in Hebrew?
2. Keyboard navigation order — correct for RTL?
3. Color contrast — oklch values at AA (4.5:1) minimum?
4. Focus styles — visible on all interactive elements?
5. aria-live regions — dynamic content announced?
6. Touch targets — ≥ 44px on mobile?

Code: [paste].
List issues by severity (critical / major / minor).
For each: exact location + exact code fix.
```

---

## Debugging

### JS bug in single-file app

```
Single-file Hebrew RTL web app. JS bug: [describe behavior].
No frameworks, vanilla JS only.
Relevant code: [paste].
Root cause diagnosis + minimal fix. No restructuring.
```

### Storage bug

```
This app uses [localStorage / IndexedDB] for patient data.
Bug: [describe — e.g., "data not persisting", "reading stale values"].
Relevant storage code: [paste].
Diagnose and fix. Ensure try/catch around all storage calls.
```

---

## Code Review

### Quick review prompt

```
Review this addition to a single-file Hebrew RTL medical app:
[paste code]

Check for:
1. Token usage — any raw colors/radius/shadows bypassing :root?
2. RTL correctness — any hardcoded left/right that should be inline-start/end?
3. Hebrew strings — any English visible to users?
4. Accessibility — missing aria labels or focus styles?
5. Performance — any layout-thrashing animations?

Return: list of issues only. No rewritten code unless asked.
```
