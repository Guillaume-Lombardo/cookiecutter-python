from {{ cookiecutter.package_name }} import __version__


def test_version_is_set() -> None:
    assert __version__ == "{{ cookiecutter.version }}"
