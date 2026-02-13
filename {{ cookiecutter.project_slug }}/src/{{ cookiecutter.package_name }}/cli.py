"""CLI entry point for {{ cookiecutter.project_name }}."""

from __future__ import annotations

import argparse

from {{ cookiecutter.package_name }} import __version__


def build_parser() -> argparse.ArgumentParser:
    """Create the command-line parser."""
    parser = argparse.ArgumentParser(prog="{{ cookiecutter.project_slug }}")
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def main() -> int:
    """Run the CLI."""
    parser = build_parser()
    parser.parse_args()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
