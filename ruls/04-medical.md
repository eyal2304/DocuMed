# Rule: Medical Domain

## Data Privacy (Phase 4 — Cloud Architecture)
**Updated 2026-03-25. Supabase is the sole approved cloud backend.**

### Approved storage
- Patient data is stored in **Supabase** (PostgreSQL) via the approved JS client.
- localStorage / IndexedDB may serve as a temporary cache only — never as primary storage.

### Prohibited data flows
- Never send PHI/PII to any third-party API, analytics service, or error-reporting service.
- No tracking scripts (Google Analytics, Mixpanel, Sentry, etc.).
- Never log patient data to `console.*` in production builds.

### Row Level Security (RLS) — MANDATORY, NON-NEGOTIABLE
- **Every Supabase table that stores patient data MUST have RLS enabled.**
- Default policy: deny all. Grant only what is explicitly needed.
- Every table must have a policy of the form:
  ```sql
  CREATE POLICY "users can access own data"
  ON <table_name>
  FOR ALL
  USING (auth.uid() = user_id);
  ```
- No table may be readable or writable by users other than the row owner.
- Never use `USING (true)` — open policies are forbidden.
- RLS status must be verified before any new table is used in production.

### GDPR compliance (EU / Israeli PDPA)
- Users must give explicit informed consent before any data is stored in the cloud.
  A mandatory checkbox on the registration form fulfills this requirement.
- Users have the right to export their data (JSON) and request deletion.
  These features must be available before the app reaches production.
- Data minimization: collect only fields necessary for the app's tracking purpose.

### HIPAA alignment (best-effort, non-US deployment)
- Treat all health data as PHI regardless of jurisdiction.
- Supabase encrypts data at rest (AES-256) and in transit (TLS 1.2+) by default — verify this is enabled on the project.
- Access logs are available in the Supabase dashboard — review regularly.
- No PHI in Supabase storage bucket filenames, folder paths, or metadata.

### Authentication
- All data writes require an authenticated Supabase session (`auth.uid()` is non-null).
- Never allow unauthenticated writes to any patient data table.
- Session tokens are managed by the Supabase JS client — do not store them manually.

## Error Messages
- Never show raw technical errors (`TypeError`, stack traces, etc.) to users.
- Always show a calm, friendly Hebrew fallback message instead.
- Tone must be reassuring — patients may be anxious about their health.

## Health Values
- Every health value (dosage, measurement, lab result) must display its unit explicitly.
- Example: "500 מ"ג" not "500" — never leave units implicit.
- Dates must follow the agreed project format (see open questions).

## Medical Accuracy
- Never auto-suggest diagnoses, treatments, or dosages.
- App is a tracking tool, not a clinical decision support system.
- Flag any feature that could be misread as medical advice.
