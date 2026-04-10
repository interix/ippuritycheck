---
name: python-project-structure
description: Organize Python projects into clear modules, entrypoints, tests, scripts, and configuration boundaries.
---

# Python Project Structure

Use this skill when initializing or reorganizing a Python project.

## Goals
- Create a layout that is easy to navigate and maintain.
- Separate business logic, entrypoints, tests, and scripts.
- Reduce coupling and avoid circular imports.

## Workflow
1. Identify project type: library, service, CLI, research code, or script-heavy project.
2. Propose a minimal structure that fits the project.
3. Define where config, source code, tests, and scripts should live.
4. Explain entrypoints and import boundaries.
5. Note migration steps if restructuring an existing project.

## Rules
- Keep the structure as simple as the project allows.
- Do not introduce unnecessary architecture layers.
- Keep runtime code separate from experiments or one-off scripts when practical.
- Explain why each major directory exists.

## Required output
- Proposed directory structure
- Purpose of each top-level directory
- Entrypoints
- Config location
- Test location
- Migration notes

