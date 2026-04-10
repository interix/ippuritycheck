---
name: python-performance-check
description: Analyze Python performance issues by identifying bottlenecks before proposing optimizations.
---

# Python Performance Check

Use this skill when performance is a concern.

## Goals
- Locate likely bottlenecks before changing code.
- Distinguish CPU, I/O, memory, and startup costs.
- Suggest low-risk optimizations first.

## Workflow
1. Define the slow behavior and the measurement context.
2. Identify whether the issue is CPU-bound, I/O-bound, memory-bound, or mixed.
3. Suggest the smallest measurement or profiling step needed.
4. Propose optimization options with tradeoffs.
5. Explain how to validate improvement.

## Rules
- Do not optimize blindly.
- Do not sacrifice clarity without a clear reason.
- Prefer algorithmic or data-flow improvements over micro-optimizations when appropriate.
- Call out when claims are only hypotheses and not yet measured.

## Required output
- Symptom summary
- Likely bottleneck type
- Measurement plan
- Optimization options
- Tradeoffs
- Validation method

