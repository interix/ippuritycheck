---
name: python-refactor-safe
description: Perform low-risk Python refactors that improve structure without changing external behavior.
---

# Safe Python Refactor

Use this skill for internal structure changes that should not alter external behavior.

## Goals
- Improve maintainability with minimal behavioral risk.
- Keep changes scoped and reviewable.
- Preserve public interfaces unless explicitly approved.

## Workflow
1. State the refactor target and boundary.
2. Identify affected functions, classes, and modules.
3. Explain why the behavior should remain unchanged.
4. Apply the refactor in the smallest coherent unit.
5. Suggest focused tests or checks.

## Rules
- Do not mix refactor work with feature work unless requested.
- Avoid broad file renames unless clearly justified.
- Do not change defaults, config semantics, or CLI behavior silently.
- Call out any areas not validated.

## Required output
- Refactor target
- Behavior expected to stay unchanged
- Files changed
- Main structural changes
- Validation suggestions
- Residual risks

