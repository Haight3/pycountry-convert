# Changelog

All notable changes to the Haight-maintained fork are documented here.

## [2026.9.0] - 2026-09-06

### Changed

- Renamed the maintained distribution to `pycountry-convert-ng` while preserving the `pycountry_convert` import package.
- Replaced the stale implementation initially inherited by the GitHub fork with the published `pycountry-convert 0.7.2` package implementation.
- Restored the real `0.7.2` public API, including `country_alpha2_to_continent_code`, `convert_continent_code_to_continent_name`, `country_name_to_country_alpha3`, country mapping helpers, name formatting, and Wikipedia aliases.
- Restored `pycountry` as the runtime source for ISO country data.
- Migrated packaging from legacy `setup.py` to PEP 517/518/621 `pyproject.toml` and a `src/` layout.
- Replaced Travis CI and legacy tooling with GitHub Actions, Ruff, pytest, and pre-commit.
- Added automated calendar versioning, release metadata validation, package builds, installation verification, PyPI Trusted Publishing, and GitHub Releases.
- Relocated data and examples under `resources/` and updated tests/examples for the `0.7.2` API.
- Kept the upstream implementation excluded from automatic Ruff rewriting to preserve the compatibility baseline.

### Added

- Added the maintained project README, contribution guidance, package logo, behavioral tests, and modern release infrastructure.

## [0.7.2] - upstream compatibility baseline

- Published upstream implementation used as the source baseline for the NG fork.

## [0.2.2] - 2017-03-12

- Version declared by the older GitHub source initially inherited by this fork.

## [0.1.9] - 2017-03-12

- Makefile and README.rst.

## [0.1.8] - 2017-03-12

- Country name to Country Alpha-2 code cleanup.

## [0.0.1] - 2016-11-17

- Initial conception.
- Code pulled from TuneLab/tune-mv-integration-python.
