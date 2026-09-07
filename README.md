<div align="center">
    <p>
        <img src="https://raw.githubusercontent.com/Haight3/pycountry-convert/c0f0635efd4336a75bdd98e0b1fca9040c271cc6/resources/images/logo.jpg" width="75%" alt="pycountry-convert-ng logo">
    </p>

<h2 align="center">PyCountry Convert Next Generation v2026.9.0</h2>
<h4 align="center">Fast country, ISO code, and continent conversion utilities.</h4>

<p align="center">
  <a href="#introduction">Introduction</a> &bull;
  <a href="#why-this-fork">Why This Fork?</a> &bull;
  <a href="#quick-start">Quick Start</a> &bull;
  <a href="#installation">Installation</a> &bull;
  <a href="#api">API</a> &bull;
  <a href="#development">Development</a>
</p>

<p align="center">
  <a href="https://pypi.org/project/pycountry-convert-ng/">
    <img src="https://img.shields.io/pypi/v/pycountry-convert-ng.svg" alt="PyPI">
  </a>
  <a href="https://github.com/Haight3/pycountry-convert/actions/workflows/ci.yml">
    <img src="https://github.com/Haight3/pycountry-convert/actions/workflows/ci.yml/badge.svg" alt="CI">
  </a>
  <a href="https://github.com/Haight3/pycountry-convert/actions/workflows/validate-release-meta.yml">
    <img src="https://github.com/Haight3/pycountry-convert/actions/workflows/validate-release-meta.yml/badge.svg" alt="Validate Release Metadata">
  </a>
  <a href="https://github.com/Haight3/pycountry-convert/actions/workflows/deploy.yml">
    <img src="https://github.com/Haight3/pycountry-convert/actions/workflows/deploy.yml/badge.svg" alt="Deployment">
  </a>
  <a href="https://github.com/Haight3/pycountry-convert/actions/workflows/version-inc.yml">
    <img src="https://github.com/Haight3/pycountry-convert/actions/workflows/version-inc.yml/badge.svg" alt="Version Increment">
  </a>
</p>
</div>

# Introduction

`pycountry-convert-ng` is a lightweight Python package for converting between country names, ISO 3166-1 alpha-2 and alpha-3 country codes, and continents.

It is a maintained continuation of the original `pycountry-convert` project. The package keeps the familiar Python import name and public conversion API:

```python
import pycountry_convert as pc
```

while the maintained distribution is published as:

```text
pycountry-convert-ng
```

The goal is deliberately small: keep the original package fast and useful, while bringing its packaging, testing, Python support, CI, and release infrastructure up to date.

# Why this fork?

The original `pycountry-convert` package is compact and efficient, and it provides a particularly useful capability that is surprisingly inconvenient to find in many alternatives: mapping ISO country codes to continents without requiring a large geospatial dependency stack.

This repository was initially forked from [`jefftune/pycountry-convert`](https://github.com/jefftune/pycountry-convert), but that repository contains older code and does not match the `pycountry-convert` package published on [PyPI](https://pypi.org/project/pycountry-convert/). PyPI identifies `TuneLab/pycountry-convert` as the repository for its `0.7.2` source code, but that repository is no longer available and currently returns a 404.

To recover the actual published code, the `0.7.2` source distribution was downloaded from PyPI and used to update this package. That published source now serves as the baseline for this maintained fork, with modern packaging, testing, Python support, CI, and release infrastructure added around it.

`pycountry-convert-ng` therefore focuses on:

- **continued maintenance** for current Python versions
- **modern packaging** through `pyproject.toml` and a `src/` layout
- **automated testing** on Python 3.11, 3.12, 3.13, and 3.14
- **automated releases** through GitHub Actions and PyPI Trusted Publishing
- **minimal runtime overhead** with static in-memory conversion tables
- **backward-compatible imports** through `pycountry_convert`
- **preserving the original conversion behavior** unless a change is explicitly reviewed and tested

The distribution name was changed to `pycountry-convert-ng` so that the maintained fork can be released independently without taking over or conflicting with the original PyPI project.

# Quick Start

```python
import pycountry_convert as pc

# ISO alpha-2 -> continent code
continent_code = pc.country_alpha2_to_continent_code("DE")
# "EU"

# Continent code -> continent name
pc.convert_continent_code_to_continent_name(continent_code)
# "Europe"

# ISO alpha-2 -> country name
pc.country_alpha2_to_country_name("DE")
# "Germany"

# ISO alpha-3 -> ISO alpha-2
pc.country_alpha3_to_country_alpha2("DEU")
# "DE"

# Country name -> ISO alpha-2 and alpha-3
pc.country_name_to_country_alpha2("Germany")
# "DE"

pc.country_name_to_country_alpha3("Germany")
# "DEU"
```

For an alpha-3 code, continent lookup can be composed directly from the public API:

```python
alpha2 = pc.country_alpha3_to_country_alpha2("DEU")
continent_code = pc.country_alpha2_to_continent_code(alpha2)
continent = pc.convert_continent_code_to_continent_name(continent_code)

print(continent)
# Europe
```

# Installation

Install the maintained package from PyPI:

```cmd
> pip install pycountry-convert-ng
```

The import remains unchanged:

```python
import pycountry_convert
```

You can also install directly from GitHub:

```cmd
> pip install https://github.com/Haight3/pycountry-convert/archive/master.zip
```

To install an in-development branch, replace `master` with the desired branch name.

# API

The public conversion functions are:


| Function                                     | Conversion                  |
| ---------------------------------------------- | ----------------------------- |
| `convert_country_alpha2_to_continent()`      | ISO alpha-2 -> continent    |
| `convert_country_alpha2_to_country_name()`   | ISO alpha-2 -> country name |
| `convert_country_alpha3_to_country_alpha2()` | ISO alpha-3 -> ISO alpha-2  |
| `convert_country_name_to_country_alpha2()`   | country name -> ISO alpha-2 |

Unknown values retain the legacy behavior of the original implementation and may raise `KeyError` where applicable.

## Package naming

The PyPI distribution and Python import intentionally have different names:

```text
PyPI distribution:  pycountry-convert-ng
Python import:       pycountry_convert
```

This allows existing code to continue using the original import API while installing the maintained fork.

# Project Structure

```text
.
├── .github/
│   └── workflows/
├── resources/
│   ├── data/
│   ├── examples/
│   └── images/
├── src/
│   ├── .info/
│   └── pycountry_convert/
├── tests/
├── pyproject.toml
└── README.md
```

The conversion package itself lives under `src/pycountry_convert/`. Historical/supporting data and examples are kept under `resources/`.

# Development

Install the project in editable mode with the development dependencies:

```cmd
> pip install -e .[dev]
```

Run the test suite:

```cmd
> pytest
```

Run the tests with coverage:

```cmd
> pytest --cov=pycountry_convert --cov-report=term-missing
```

Run Ruff:

```cmd
> ruff check src tests
```

Build and validate the distributions locally:

```cmd
> python -m build
> python -m twine check dist/*
```

Pre-commit hooks can be installed with:

```cmd
> pre-commit install
```

# Release & PyPI

The project follows the same automated release model used by other Haight Python projects:

```text
feature / development
        ↓
release-candidate
        ↓
automatic version increment + CI
        ↓
pull request to master
        ↓
release metadata validation + CI
        ↓
master
        ↓
build wheel + source distribution
        ↓
installation verification
        ↓
PyPI Trusted Publishing
        ↓
GitHub tag + GitHub Release
```

Versions use the calendar-based pattern:

```text
YYYY.MM.PATCH
```

For example:

```text
2026.9.0
2026.9.1
2026.9.2
```

Publishing to PyPI uses OpenID Connect through PyPI Trusted Publishing. No long-lived PyPI API token is stored in the repository.

# Attribution

This repository is a fork of [`jefftune/pycountry-convert`](https://github.com/jefftune/pycountry-convert), originally developed by TUNE / TuneLab contributors.

The original copyright and attribution are preserved. The modernized fork is maintained by Haight Labs.

# License

MIT. See [LICENSE](LICENSE) for the complete license and original attribution.
