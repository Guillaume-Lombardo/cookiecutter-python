---
name: architecture
description: Design and maintain package architecture, module boundaries, and public interfaces.
---

# Architecture

## Rules
1. Keep runtime code in `src/{{ cookiecutter.package_name }}/`.
2. Keep CLI parsing in `cli.py` and business logic in dedicated modules.
3. Keep public interfaces typed and explicit.
4. Keep `pyproject.toml` metadata consistent with package runtime version.

## Validation
- `uv run pytest -m unit`
- `uv run {{ cookiecutter.project_slug }} --help`
