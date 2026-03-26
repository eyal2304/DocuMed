---
name: tokens
description: Audit and extend DocuMed's design token system in :root — add missing tokens, find raw values that should be tokenized, keep the system consistent.
---

# Design Tokens — DocuMed

Two modes: **audit** (find problems) or **extend** (add new tokens).
Ask the user which they need, or infer from context.

---

## Mode A — Audit

Read `index.html` in full.

### Step 1 — Extract all tokens

List everything currently in `:root {}` — colors, radii, shadows, backgrounds.

### Step 2 — Scan for raw values outside `:root`

Find every CSS rule that uses:
- `#xxxxxx`, `rgb(`, `rgba(`, `hsl(`, `oklch(` — raw colors
- `border-radius: [0-9]` — raw radii
- `box-shadow: [0-9]` — raw shadows

Report format:
```
⚠️  Raw values found (should be tokens):
- Line 142: border-radius: 8px → closest token: var(--radius-xl)
- Line 207: color: #374151 → closest token: var(--color-neutral-700)
```

### Step 3 — Flag missing token categories

Is any design property NOT covered by a token? Common gaps:
- Spacing scale (are margins/paddings hardcoded numbers?)
- Typography scale (are font-sizes hardcoded?)
- Animation durations
- Z-index scale

Report these as suggestions, not violations.

### Step 4 — Consistency check

Are similar values tokenized consistently?
- Same visual gray used in two tokens with slightly different `oklch` values?
- Soft background colors — are they all using the same lightness formula?

---

## Mode B — Extend (add new tokens)

Ask the user:
1. **מה להוסיף?** — לדוגמה: "צבע כתום לאזהרות", "רדיוס קטן לתגיות", "מרווח סטנדרטי"
2. **שם** — מה שם הטוקן? (לדוגמה: `--color-orange-500`, `--radius-sm`, `--space-md`)
3. **ערך** — `oklch()` לצבעים, `px`/`rem` לשאר

### oklch color formula used in this project

Match the existing lightness/chroma pattern:
- `neutral` tones: high lightness (0.95–0.99) for backgrounds, low (0.2–0.4) for text
- Brand `teal`: around `oklch(0.55 0.15 195)`
- Soft backgrounds (`--bg-*-soft`): high lightness `≈ 0.95`, low chroma `≈ 0.03–0.06`

### Adding a token

1. Identify the correct position in `:root` (group colors with colors, radii with radii)
2. Use `Edit` to insert the new token inside `:root`
3. Show: `/* הוסף */ --token-name: value;`

### After adding

- Verify the token is inside `:root {}` — not outside it
- Show where in the file it was added
- Remind the user to use `var(--token-name)` wherever the value is needed
