---
name: python-cli-tool
description: Create or improve Python CLI tools with argparse, clear help text, error handling, and predictable behavior.
---

# Python CLI Tool

Use this skill when building or modifying a Python command-line tool.

## Goals
- Create a usable CLI with predictable inputs and outputs.
- Provide clear help text and basic error handling.
- Avoid hidden side effects.

## Workflow
1. Define command purpose, inputs, outputs, and exit behavior.
2. Prefer argparse unless the project already standardizes on another library.
3. Add help text and examples where useful.
4. Handle invalid input gracefully.
5. Clarify whether the tool writes files, modifies data, or supports dry-run.

## Rules
- Do not hardcode environment-specific paths.
- Prefer explicit arguments over hidden global state.
- Keep the entrypoint and business logic separated when practical.
- If the command is destructive, require explicit confirmation flags.

## Required output
- CLI purpose
- Entry command
- Arguments and flags
- Side effects
- Error handling summary
- Example usage

