# Open Questions — DocuMed

Decisions not yet made. Resolve before writing related code.

---

- [ ] **Data model** — what fields per chronic condition?
  (name, diagnosis date, medications, dosage, notes, severity?)

- [ ] **Storage engine** — localStorage vs. IndexedDB?
  Decide before any persistence code is written.

- [ ] **Date format** — DD/MM/YYYY or relative ("לפני 3 ימים") or both?
  Must be consistent across the entire app.

- [ ] **Accessibility review** — test with Hebrew screen reader (NVDA + Chrome) before first release.

- [ ] **Offline indicator** — how does the app signal it's working offline?
  Badge, banner, or silent?

- [ ] **Export / backup** — can a patient export their data? What format (JSON, PDF)?
