#!/usr/bin/env python3
"""PostToolUse:Edit|Write — validate index.html after every change"""
import json, sys, re, pathlib

data = json.load(sys.stdin)
file_path = data.get("tool_input", {}).get("file_path", "")

if "index.html" not in str(file_path):
    sys.exit(0)

try:
    content = pathlib.Path(file_path).read_text(encoding="utf-8")
except Exception:
    sys.exit(0)

warnings = []

# ── 1. External dependencies ──────────────────────────────────────────────────
# Phase 4 approved exception: Supabase JS client only (see ruls/01-architecture.md)
APPROVED_EXTERNAL = [
    r'cdn\.jsdelivr\.net/npm/@supabase/supabase-js@2/',
]

def _is_approved(url_line: str) -> bool:
    return any(re.search(p, url_line, re.IGNORECASE) for p in APPROVED_EXTERNAL)

EXT_PATTERNS = [
    r'<script\s+src=["\']https?://[^"\']+["\']',
    r'<link[^>]+href=["\']https?://[^"\']+["\']',
    r"@import\s+['\"]https?://",
    r'src=["\']https?://(?!.*localhost)[^"\']+["\']',
]
for pat in EXT_PATTERNS:
    matches = re.findall(pat, content, re.IGNORECASE)
    unapproved = [m for m in matches if not _is_approved(m)]
    if unapproved:
        warnings.append("🔴 EXTERNAL DEPENDENCY — האפליקציה לא תעבוד offline! הסר CDN/remote links.")
        break

# ── 2. RTL violations in CSS ───────────────────────────────────────────────────
css_match = re.search(r"<style[^>]*>(.*?)</style>", content, re.DOTALL | re.IGNORECASE)
if css_match:
    css = css_match.group(1)
    # Remove :root so we don't flag tokens defined there
    css_no_root = re.sub(r":root\s*\{[^}]*\}", "", css, flags=re.DOTALL)

    rtl_hits = re.findall(r"(?:margin|padding)-(left|right)\s*:", css_no_root)
    if rtl_hits:
        warnings.append(
            f"🟡 RTL VIOLATION — {len(rtl_hits)}x margin/padding-left/right. "
            f"השתמש ב-inline-start / inline-end."
        )

    if re.search(r"text-align\s*:\s*(left|right)\b", css_no_root):
        warnings.append("🟡 RTL VIOLATION — text-align: left/right. השתמש ב-start / end.")

# ── 3. Raw color values outside :root ─────────────────────────────────────────
if css_match:
    css = css_match.group(1)
    css_no_root = re.sub(r":root\s*\{[^}]*\}", "", css, flags=re.DOTALL)
    raw = re.findall(
        r"(?:color|background(?:-color)?|border(?:-color)?|box-shadow)\s*:[^;]*?"
        r"(?:#[0-9a-fA-F]{3,8}|rgb[a]?\(|hsl[a]?\(|oklch\()",
        css_no_root,
    )
    # Filter out lines that are actually var(--...)
    raw = [r for r in raw if "var(--" not in r]
    if raw:
        warnings.append(
            f"🟡 TOKEN VIOLATION — {len(raw)} ערך צבע גולמי מחוץ ל-:root. "
            f"השתמש ב-var(--token) בלבד."
        )

# ── Output ─────────────────────────────────────────────────────────────────────
if warnings:
    print("\n".join(warnings), file=sys.stderr)
    # Exit 2 = send as feedback to Claude so it can fix
    sys.exit(2)

sys.exit(0)
