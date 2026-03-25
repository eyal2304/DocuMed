# Rule: Architecture

## Single-File Constraint
- All code lives in `index.html` — HTML, CSS, and JS together.
- Never create separate `.css`, `.js`, or template files.
- Never add `<link rel="stylesheet">` or `<script src>` pointing to local files.

## No Build Tools
- No npm, no package.json, no node_modules.
- No webpack, Vite, Rollup, Parcel, or any bundler.
- No Babel, TypeScript, or any transpiler.
- The file must open by double-clicking in any browser — zero setup.

## No External Dependencies
- No CDN links (`unpkg`, `jsdelivr`, `cdnjs`, etc.).
- No Google Fonts or any external font load.
- No third-party scripts or stylesheets.
- App must work fully offline, with no network connection.

## Phase 4 Exception — Supabase (Cloud-First Architecture)
**Effective Phase 4 (2026-03-25). This is the sole CDN exception.**

- The Supabase JS client **may** be loaded via the official Supabase CDN:
  `https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2/dist/umd/supabase.min.js`
- No other CDN, external script, or stylesheet may be added.
- The app now requires a network connection for data persistence (Supabase).
  Local localStorage/IndexedDB may be used as a read-only cache or fallback only.
- The Supabase Project URL and publishable API key may be embedded in `index.html`.
  Never embed service-role keys, JWT secrets, or any privileged credentials.
- All Supabase table access must go through the JS client with the publishable key only.
  Direct REST calls bypassing the client are forbidden.
