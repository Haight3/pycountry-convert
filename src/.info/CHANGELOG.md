# Changelog

All notable changes to the Haight-maintained fork are documented here.

## [2026.9.1] - 2026-09-07

### Added

- Added conversion from continent codes to continent names.
- Added conversion from country names and ISO alpha-3 codes to ISO alpha-3 and alpha-2 codes.
- Added cached mapping APIs for country names, official names, ISO alpha-2, ISO alpha-3, and numeric identifiers.
- Added configurable default, uppercase, and lowercase country-name formatting.
- Added support for country aliases sourced from the published `pycountry-convert` 0.7.2 implementation.
- Added a notebook tutorial covering the public conversion API.

### Changed

- Rebased the conversion implementation on the source distributed with `pycountry-convert` 0.7.2.
- Changed country and ISO mappings to use `pycountry>=24.6.1` as the authoritative runtime data source.
- Split country-to-continent conversion into `country_alpha2_to_continent_code()` and `convert_continent_code_to_continent_name()`.
- Changed country-name conversion to accept country names, ISO alpha-2 codes, and ISO alpha-3 codes through the same public entrypoints.
- Separated non-ISO territories such as Abkhazia, Kosovo, and South Ossetia from the ISO-backed country-name mappings.
- Expanded conversion tests to cover all continents, country aliases, name formatting, mapping APIs, chained conversions, and invalid inputs.
- Replaced the standalone Python example with a comprehensive Jupyter notebook tutorial.
- Updated the README to document the published 0.7.2 baseline, revised public API, installation instructions, supported Python versions, and release workflows.
- Converted the package logo from JFIF to JPEG and changed the README to use a commit-pinned logo URL.

### Deprecated

### Removed

- Removed the legacy `convert_country_alpha2_to_continent()`, `convert_country_alpha2_to_country_name()`, `convert_country_alpha3_to_country_alpha2()`, and `convert_country_name_to_country_alpha2()` public names.
- Removed the legacy modules that contained the static country-name and ISO conversion tables.
- Removed the obsolete JFIF logo and standalone `example_country_convert.py` example.

### Fixed

- Corrected the East Timor alias to use the current ISO alpha-2 code `TL` instead of the withdrawn `TP` code.
- Standardized invalid country, continent, and ISO-code inputs to raise descriptive `KeyError` exceptions.
- Corrected alpha-2 and alpha-3 passthrough validation in the country-name conversion functions.
- Corrected country mapping construction to resolve Wikipedia aliases through validated `pycountry` records.

### Security

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
