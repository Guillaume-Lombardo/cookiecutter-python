# AGENTS

## Mission
Build and maintain a production-ready Python package with clear architecture, strong quality gates, and release automation.

## Working Rules
- Keep runtime code under `src/{{ cookiecutter.package_name }}/`.
- Keep tests deterministic and isolated from external network calls.
- Use typed interfaces and explicit error handling.
- Prefer small, cohesive modules.

## Quality Gates
Run before push/PR:
- `uv run ruff format .`
- `uv run ruff check .`
- `uv run ty check src tests`
- `uv run pytest -m unit`
- `uv run pytest -m integration`
- `uv run pytest -m end2end`
- `uv run pre-commit run --all-files`

## Skills
- `skills/architecture/SKILL.md`
- `skills/tooling/SKILL.md`
- `skills/testing/SKILL.md`
- `skills/release/SKILL.md`
