from __future__ import annotations

import json
import shutil
import subprocess
from pathlib import Path

import pytest


def _run(cmd: list[str], cwd: Path) -> subprocess.CompletedProcess[str]:
    """Run a command and fail with full output for easier debugging."""
    return subprocess.run(
        cmd,
        cwd=cwd,
        check=True,
        capture_output=True,
        text=True,
        timeout=1800,
    )


def _run_maybe_fail(cmd: list[str], cwd: Path) -> subprocess.CompletedProcess[str]:
    """Run a command and return output without enforcing exit code."""
    return subprocess.run(
        cmd,
        cwd=cwd,
        check=False,
        capture_output=True,
        text=True,
        timeout=1800,
    )


def _assert_no_repo_artifacts(repo_root: Path) -> None:
    """Ensure test execution left no build/test artifacts in template repository root."""
    forbidden = [
        ".coverage",
        "coverage.json",
        ".pytest_cache",
        ".ruff_cache",
        "htmlcov",
        "dist",
        "build",
        ".venv",
    ]
    leftovers = [name for name in forbidden if (repo_root / name).exists()]
    assert leftovers == []
    assert not (repo_root / "tests" / "end2end" / "__pycache__").exists()


def _cleanup_repo_artifacts(repo_root: Path) -> None:
    """Remove temporary artifacts that may be created during test execution."""
    shutil.rmtree(repo_root / ".pytest_cache", ignore_errors=True)
    shutil.rmtree(repo_root / ".ruff_cache", ignore_errors=True)
    shutil.rmtree(repo_root / "htmlcov", ignore_errors=True)
    shutil.rmtree(repo_root / "dist", ignore_errors=True)
    shutil.rmtree(repo_root / "build", ignore_errors=True)
    shutil.rmtree(repo_root / ".venv", ignore_errors=True)
    for file_name in [".coverage", "coverage.json"]:
        (repo_root / file_name).unlink(missing_ok=True)
    shutil.rmtree(repo_root / "tests" / "end2end" / "__pycache__", ignore_errors=True)


@pytest.mark.end2end
def test_cookiecutter_generates_precommit_clean_package_with_high_coverage(tmp_path: Path) -> None:
    """Generate a package from template, run quality gates, and cleanup artifacts."""
    repo_root = Path(__file__).resolve().parents[2]
    generated_root = tmp_path / "generated"
    generated_root.mkdir(parents=True, exist_ok=True)

    project_dir = generated_root / "my-awesome-package"

    try:
        _run(
            [
                "uvx",
                "--from",
                "cookiecutter",
                "cookiecutter",
                str(repo_root),
                "--no-input",
                "--output-dir",
                str(generated_root),
            ],
            cwd=repo_root,
        )

        assert project_dir.exists()
        assert (project_dir / "pyproject.toml").exists()

        _run(["git", "init"], cwd=project_dir)
        _run(["git", "checkout", "-b", "e2e"], cwd=project_dir)
        _run(["git", "add", "."], cwd=project_dir)

        _run(["uv", "sync", "--group", "dev"], cwd=project_dir)
        # Pre-commit may return non-zero with strict profiles, but must run and apply fixes.
        precommit_result = _run_maybe_fail(
            ["uv", "run", "pre-commit", "run", "--all-files"],
            cwd=project_dir,
        )
        assert precommit_result.returncode in {0, 1}
        if precommit_result.returncode == 1:
            status = _run(["git", "status", "--porcelain"], cwd=project_dir).stdout.strip()
            assert status != ""

        _run(["uv", "run", "pytest", "-m", "unit or integration or end2end"], cwd=project_dir)
        _run(["uv", "run", "coverage", "json", "-o", "coverage.json"], cwd=project_dir)

        coverage_data = json.loads((project_dir / "coverage.json").read_text(encoding="utf-8"))
        percent = float(coverage_data["totals"]["percent_covered"])
        assert percent > 80.0
    finally:
        if project_dir.exists():
            shutil.rmtree(project_dir)
        _cleanup_repo_artifacts(repo_root)

    assert not project_dir.exists()
    _assert_no_repo_artifacts(repo_root)
