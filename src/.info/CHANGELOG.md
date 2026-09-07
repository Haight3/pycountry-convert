# Changelog

All notable changes to the Haight-maintained fork are documented here.

## [2026.9.0] - 2026-09-06

### Changed

- Renamed the maintained distribution to `pycountry-convert-ng` while preserving the `pycountry_convert` import package and public API.
- Migrated packaging from legacy `setup.py` to PEP 517/518/621 `pyproject.toml`.
- Migrated the package to a `src/pycountry_convert` layout.
- Preserved the existing conversion implementation and public API.
- Replaced Travis CI, Pylint, YAPF, and legacy requirements files with GitHub Actions, Ruff, pytest, and pre-commit.
- Added automated versioning, release metadata validation, package builds, installation verification, PyPI Trusted Publishing, and GitHub Releases.
- Declared the runtime package dependency-free because the conversion implementation uses static in-memory mappings.
- Relocated data and example resources under the `resources` directory.
- Restored and standardized `YYYY.MM.PATCH` versioning and corrected the bumpver configuration.
- Updated the README, contributing guidance, package documentation, and release documentation.
- Reformatted country conversion mappings and updated conversion tests.

### Added

- Added the new package logo asset.

## [0.7.2] - 2018-02-16

- Python 2.7 supported.
- Travis CI testing both Python 2.7 and 3.6.

## [0.7.1] - 2018-02-15

- Migrated to GitHub/TuneLab.
- Added Python 2.7 support.
- Added `lru_cache()`.

## [0.6.7] - 2018-02-15

- Added `common_name` from pycountry (vgavro).

## [0.6.6] - 2018-01-25

- Migrated to GitHub/tuneinc.
- Changed the license to MIT.

## [0.6.2] - 2017-12-09

- Added readthedocs.org.

## [0.5.4] - 2017-12-07

- Changed the license to LGPL 3.0.

## [0.5.0] - 2017-11-30

- Added README.rst.
- Added hits and contributors.

## [0.3.0] - 2017-11-27

- Added README.rst.
- Added Travis CI.

## [0.2.2] - 2017-03-12

- Version declared by the legacy package at the point used by this fork.

## [0.1.9] - 2017-03-12

- Makefile and README.rst.

## [0.1.8] - 2016-11-19

- Makefile and README.rst.

## [0.1.0] - 2016-11-17

- Initial code.
- Code pulled from TuneLab/tune-mv-integration-python.
- Country name to Country Alpha-2 code cleanup.

## [0.0.1] - 2016-11-17

- Initial commit.
