---
name: python-dependency-change
description: Handle Python dependency additions or updates carefully, with approval, version awareness, and environment clarity.
---

# Python Dependency Change

Use this skill when changing Python dependencies.

## Goals
- Make dependency changes explicit and reviewable.
- Respect the project's existing dependency management approach.
- Avoid accidental global installs or untracked dependency drift.

## Workflow
1. Explain why the dependency is needed.
2. Identify the package name, version strategy, and target environment.
3. Identify which dependency files would change.
4. Note compatibility risks.
5. Request approval before installing or editing dependency files.

## Rules
- Do not install packages without approval.
- Do not default to the newest version without a reason.
- Prefer the project's existing dependency manager.
- If adding a dependency for one small task, explain why standard library or existing packages are insufficient.

## Required output
- Package name
- Why it is needed
- Target environment
- Files that would change
- Version strategy
- Compatibility risks
- Approval needed

