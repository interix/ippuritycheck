---
name: python-data-script
description: Write Python data-processing scripts that make inputs, outputs, side effects, and summary statistics explicit.
---

# Python Data Script

Use this skill when creating or modifying data-processing scripts.

## Goals
- Make input and output paths explicit.
- Avoid accidental overwrite of source data.
- Handle large files safely when possible.
- Produce a useful processing summary.

## Workflow
1. Define input format, output format, and overwrite policy.
2. State whether the script streams or loads data fully into memory.
3. Make output paths explicit.
4. Add summary reporting for rows, files, or records processed.
5. Clarify failure behavior and partial-output behavior.

## Rules
- Do not overwrite source data by default.
- Prefer streaming or chunking for large files.
- Explain assumptions about schema, encoding, and delimiters.
- Call out side effects before execution.

## Required output
- Input path or pattern
- Output path or pattern
- Overwrite policy
- Processing summary fields
- Memory considerations
- Validation checks

