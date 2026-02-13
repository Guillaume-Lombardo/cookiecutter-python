# cookiecutter-python-package

Cookiecutter template to bootstrap Python packages with:

- `uv` dependency management
- `ruff` lint + format
- `ty` type checking
- `pytest` (unit/integration/end2end markers)
- `pre-commit`
- GitHub Actions CI + PyPI/TestPyPI release workflow
- AI collaboration helpers (`AGENTS.md` + local `skills/`)

## Usage

```bash
uvx --from cookiecutter cookiecutter gh:Guillaume-Lombardo/cookiecutter-python
```

Local path usage also works:

```bash
uvx --from cookiecutter cookiecutter /absolute/path/to/cookiecutter-python
```

Then in the generated project:

```bash
uv sync --group dev
uv run pre-commit install
uv run pre-commit run --all-files
uv run pytest

git add .
git commit -m "initial commit"
git push -u origin main
```

## Notes

- Release workflow uses trusted publishing (`pypa/gh-action-pypi-publish`).
- Configure GitHub environments `testpypi` and `pypi` before first release.
