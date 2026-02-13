"""Package exceptions."""

from __future__ import annotations

from dataclasses import dataclass


class PackageError(Exception):
    """Root exception for the package."""


@dataclass(frozen=True)
class SettingsError(PackageError):
    """Raised when settings cannot be loaded or validated."""

    message: str

    def __str__(self) -> str:
        """Return error message payload."""
        return self.message


@dataclass(frozen=True)
class AsyncExecutionError(PackageError):
    """Raised when an async operation fails in compatibility runner."""

    message: str

    def __str__(self) -> str:
        """Return error message payload."""
        return self.message
