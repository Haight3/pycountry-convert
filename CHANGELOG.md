# Changelog

All notable changes to the Haight-maintained fork are documented here.

## [2026.9.0.0] - 2026-09-06

### Changed

- Renamed the maintained distribution to `pycountry-convert-ng` while preserving the `pycountry_convert` import package and public API.
- Migrated packaging from legacy `setup.py` to PEP 517/518/621 `pyproject.toml`.
- Migrated the package to a `src/pycountry_convert` layout.
- Preserved the existing conversion implementation and public API.
- Replaced Travis CI, Pylint, YAPF, and legacy requirements files with GitHub Actions, Ruff, pytest, and pre-commit.
- Added automated versioning, release metadata validation, package builds, installation verification, PyPI Trusted Publishing, and GitHub Releases.
- Declared the runtime package dependency-free because the conversion implementation uses static in-memory mappings.

## [0.2.2] - 2017-03-12

- Version declared by the legacy package at the point used by this fork.

## [0.1.9] - 2017-03-12

- Makefile and README.rst.

## [0.1.8] - 2017-03-12

- Country name to Country Alpha-2 code cleanup.

## [0.0.1] - 2016-11-17

- Initial conception.
- Code pulled from TuneLab/tune-mv-integration-python.
