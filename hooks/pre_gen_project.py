"""Validate cookiecutter inputs before generation."""

from __future__ import annotations

import re
import sys

PROJECT_SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
PACKAGE_RE = re.compile(r"^[a-z_][a-z0-9_]*$")

project_slug = "{{ cookiecutter.project_slug }}"
package_name = "{{ cookiecutter.package_name }}"

if not PROJECT_SLUG_RE.match(project_slug):
    print(f"ERROR: project_slug '{project_slug}' must be kebab-case.")
    sys.exit(1)

if not PACKAGE_RE.match(package_name):
    print(f"ERROR: package_name '{package_name}' must be a valid Python package name.")
    sys.exit(1)
