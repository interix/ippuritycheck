---
name: python-test-writer
description: Add focused tests for Python code using the project's existing test framework and conventions.
---

# Python Test Writer

Use this skill to add or improve tests.

## Goals
- Add the smallest useful test coverage.
- Follow the existing test framework and project conventions.
- Cover the main path first, then key edge cases.

## Workflow
1. Detect the project's test framework and test layout.
2. Identify the smallest unit or workflow to verify.
3. Write targeted tests with clear names.
4. Avoid introducing a new framework unless asked.
5. Explain what the tests cover and what they do not cover.

## Rules
- Prefer deterministic tests.
- Avoid network, filesystem, or timing dependencies unless necessary.
- If mocking is needed, keep it minimal and explain why.
- If the project lacks tests, propose a minimal starting pattern.

## Required output
- Test framework detected
- New or changed test files
- Behaviors covered
- Edge cases covered
- Remaining gaps
- How to run the tests

