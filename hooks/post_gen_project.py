"""Apply post-generation cleanup."""

from __future__ import annotations

import shutil
from pathlib import Path

if "{{ cookiecutter.create_github_actions }}" == "no":
    github_dir = Path('.github')
    if github_dir.exists():
        shutil.rmtree(github_dir)
