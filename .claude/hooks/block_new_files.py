#!/usr/bin/env python3
"""PreToolUse:Write — block creating new .html/.css/.js files outside index.html"""
import json, sys, pathlib

data = json.load(sys.stdin)
file_path = data.get("tool_input", {}).get("file_path", "")
p = pathlib.Path(file_path)

# Allow index.html and all project config/docs folders
ALLOWED_PARTS = {"index.html", ".claude", "ruls", "frontend", "agents", "skills", "hooks", "memory", "CLAUDE.md", "MEMORY.md"}
if any(part in ALLOWED_PARTS for part in p.parts):
    sys.exit(0)
if p.name in ALLOWED_PARTS:
    sys.exit(0)

# Block new web source files only
BLOCKED_EXTENSIONS = {".js", ".css", ".html", ".ts", ".jsx", ".tsx", ".mjs"}
if p.suffix in BLOCKED_EXTENSIONS:
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": (
                f"DocuMed הוא single-file app. "
                f"אסור ליצור קובץ {p.suffix} חדש ({p.name}). "
                f"כל הקוד חייב להיות בתוך index.html."
            )
        }
    }))

sys.exit(0)
