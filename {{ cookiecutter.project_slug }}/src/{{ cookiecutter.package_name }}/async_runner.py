"""Helpers to run async operations from sync or async contexts."""

from __future__ import annotations

import asyncio
import threading
from collections.abc import Coroutine
from queue import Queue
from typing import Any

from {{ cookiecutter.package_name }}.exceptions import AsyncExecutionError


def _run_in_background_thread[T](coro: Coroutine[Any, Any, T]) -> T:
    """Run a coroutine in a dedicated thread with its own event loop."""
    output: Queue[T | BaseException] = Queue(maxsize=1)

    def _runner() -> None:
        try:
            output.put(asyncio.run(coro))
        except BaseException as exc:  # noqa: BLE001
            output.put(exc)

    thread = threading.Thread(target=_runner, daemon=True)
    thread.start()
    thread.join()

    result = output.get()
    if isinstance(result, BaseException):
        raise AsyncExecutionError(f"Async task failed: {result}") from result
    return result


def run_async[T](coro: Coroutine[Any, Any, T]) -> T:
    """Run an async coroutine from both sync and async contexts."""
    try:
        asyncio.get_running_loop()
    except RuntimeError:
        return asyncio.run(coro)

    return _run_in_background_thread(coro)
