---
name: python-env-check
description: Inspect the active Python interpreter, virtual environment, dependency files, and execution risk before running Python commands.
---

# Python Environment Check

Use this skill before running any Python-related command.

## Goals
- Identify the exact Python interpreter and pip that will be used.
- Detect the active virtual environment and project dependency files.
- Explain the command, its purpose, and any side effects.
- Avoid unsafe or implicit environment changes.

## Required checks
Report all of the following before execution:
- Python executable path
- Python version
- Pip executable path
- Active virtual environment name or path
- Presence of   -     -     -     -     -   - Whether the command may write files, install dependencies, download data, use network access, or start long-running jobs

## Rules
- Prefer the project's existing environment.
- Do not switch interpreters automatically.
- Do not create or recreate environments without approval.
- Do not install packages without approval.
- Do not mix python/pip from different environments.

## Output template
Python environment check:
- Python path:
- Python version:
- Pip path:
- Active virtual environment:
- Environment files detected:
- Command to run:
- Purpose:
- Side effects:
- Risk points:
- Approval needed:

