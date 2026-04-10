---
name: python-bugfix
description: Fix Python bugs with a smallest-change-first workflow based on traceback, call path, and verification.
---

# Python Bug Fix

Use this skill when debugging Python code.

## Goals
- Understand the failure before editing code.
- Produce the smallest viable fix.
- Avoid unrelated refactors.
- Explain verification clearly.

## Workflow
1. Read the traceback or error message carefully.
2. Identify the failing entrypoint, function, and likely call chain.
3. State the likely root cause and confidence level.
4. Propose a minimal fix plan.
5. Modify only the files required for the fix.
6. Provide verification steps.

## Rules
- Do not expand the task into a refactor unless asked.
- If the bug is ambiguous, list the most likely hypotheses.
- If the fix changes external behavior, call that out explicitly.
- If tests exist, prefer updating or adding the smallest relevant test.

## Required output
- Bug summary
- Likely root cause
- Files to modify
- Minimal fix plan
- Risk points
- Verification steps

