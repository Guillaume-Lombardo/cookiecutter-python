from {{ cookiecutter.package_name }} import cli


def test_cli_module_exposes_main() -> None:
    assert callable(cli.main)
