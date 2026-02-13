---
name: testing
description: Maintain test strategy across unit, integration, and end-to-end scopes.
---

# Testing

## Topology
- `tests/unit`: default fast checks
- `tests/integration`: component boundaries
- `tests/end2end`: CLI/user journeys

## Rules
1. Keep tests deterministic and local.
2. Add at least one end-to-end test for each CLI-visible feature.
3. Write a failing test before bug fixes whenever possible.

## Commands
- `uv run pytest`
- `uv run pytest -m integration`
- `uv run pytest -m end2end`
