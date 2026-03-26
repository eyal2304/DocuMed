---
name: DocuMed medical domain rules
description: Patient data privacy, error message tone, health value display, no clinical advice
type: project
---

**Data privacy:**
- Patient data stays in the browser only (localStorage / IndexedDB).
- Never send PII to any external API, analytics service, or server.
- No tracking scripts, no error-reporting services that transmit data.

**Error messages:**
- Never show raw technical errors (`TypeError`, stack traces) to users.
- Always show a calm, friendly Hebrew fallback message.
- Tone must be reassuring — patients may be anxious about their health.

**Health values:**
- Always show units explicitly: "500 מ״ג", "37.2°C", "120/80 מ״מ כספית".
- Never leave units implicit.

**Medical accuracy:**
- App is a tracking tool only — not a clinical decision support system.
- Never auto-suggest diagnoses, treatments, or dosages.
- Flag any feature that could be misread as medical advice.

**Why:** Medical context demands extra care — wrong data display or alarming errors can cause real patient harm.
