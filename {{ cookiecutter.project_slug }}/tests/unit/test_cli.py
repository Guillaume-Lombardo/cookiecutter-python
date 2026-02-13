from __future__ import annotations

import pytest

from {{ cookiecutter.package_name }} import cli
from {{ cookiecutter.package_name }}.settings import Settings


def test_build_parser_supports_version_flag(capsys) -> None:
    parser = cli.build_parser()

    with pytest.raises(SystemExit) as exc_info:
        parser.parse_args(["--version"])
    assert exc_info.value.code == 0

    captured = capsys.readouterr()
    assert "{{ cookiecutter.version }}" in captured.out


def test_main_initializes_logging_and_returns_zero(mocker) -> None:
    dummy_parser = mocker.Mock()
    dummy_parser.parse_args.return_value = None

    mocker.patch("{{ cookiecutter.package_name }}.cli.build_parser", return_value=dummy_parser)
    mocker.patch("{{ cookiecutter.package_name }}.cli.get_settings", return_value=Settings())
    mock_configure = mocker.patch("{{ cookiecutter.package_name }}.cli.configure_logging")
    mock_logger = mocker.Mock()
    mocker.patch("{{ cookiecutter.package_name }}.cli.get_logger", return_value=mock_logger)

    result = cli.main()

    assert result == 0
    mock_configure.assert_called_once()
    mock_logger.info.assert_called_once()
