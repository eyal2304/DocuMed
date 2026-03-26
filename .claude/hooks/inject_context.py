#!/usr/bin/env python3
"""UserPromptSubmit — inject DocuMed project context into every conversation turn"""
import json, sys

print(json.dumps({
    "additionalContext": (
        "PROJECT: DocuMed — single-file Hebrew RTL medical app (index.html only).\n"
        "HARD RULES:\n"
        "- All code inline in index.html. No separate files. No build tools. No CDN.\n"
        "- CSS: use var(--token) only — no raw colors/radius/shadows outside :root.\n"
        "- Layout: RTL. Use margin/padding-inline-start/end, text-align: start/end.\n"
        "- All user-visible text in Hebrew. No English placeholders.\n"
        "- Mobile-first: design at 375px.\n"
        "- Medical: patient data stays in browser only. Calm Hebrew error messages.\n"
        "OPEN DECISIONS (ask before writing related code):\n"
        "- Storage: localStorage vs IndexedDB?\n"
        "- Date format: DD/MM/YYYY or relative?\n"
        "- Data model: what fields per chronic condition?\n"
        "Full rules: .claude/rules_*.md"
    )
}))

sys.exit(0)
