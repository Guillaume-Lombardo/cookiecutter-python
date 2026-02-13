---
name: tooling
description: Maintain developer tooling and quality gates (uv, ruff, ty, pre-commit).
---

# Tooling

## Setup
- `uv sync --group dev`
- `uv run pre-commit install`

## Validation pipeline
1. `uv run ruff format .`
2. `uv run ruff check .`
3. `uv run ty check src tests`
4. `uv run pytest -m unit`
5. `uv run pytest -m integration`
6. `uv run pytest -m end2end`
7. `uv run pre-commit run --all-files`
8. Keep `settings.py` + `logging.py` aligned so logger behavior follows env config.
