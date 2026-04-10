---
name: python-package-quality
description: Review Python code quality with focused checks for naming, exceptions, function size, typing, dead code, and maintainability.
---

# Python Package Quality

Use this skill to review Python code quality without automatically performing broad rewrites.

## Goals
- Surface maintainability issues clearly.
- Prioritize actionable problems over style trivia.
- Keep review output structured and specific.

## Review areas
- Function and class naming clarity
- Excessive function length or complexity
- Exception handling quality
- Type hints and interface clarity
- Dead code or unreachable paths
- Module responsibility and cohesion
- Comments and docstrings where needed

## Rules
- Do not auto-rewrite the whole module unless asked.
- Focus on the most important issues first.
- Use concrete file names, symbols, and examples.
- Distinguish between required fixes and optional improvements.

## Required output
- Highest-priority issues
- Why each issue matters
- Suggested fixes
- Optional improvements
- Files or symbols reviewed

