#!/usr/bin/env python3
"""PreToolUse:Bash — block npm/node/build tools"""
import json, sys, re

data = json.load(sys.stdin)
command = data.get("tool_input", {}).get("command", "")

BUILD_TOOLS = r"\b(npm|npx|node|vite|webpack|parcel|rollup|babel|yarn|pnpm|bun|tsc|esbuild)\b"
if re.search(BUILD_TOOLS, command):
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": (
                "Build tools אסורים ב-DocuMed. "
                "הפרויקט הוא single-file HTML — אין npm, אין bundler, אין transpiler. "
                "כל הקוד חייב להיות inline בתוך index.html."
            )
        }
    }))

sys.exit(0)
