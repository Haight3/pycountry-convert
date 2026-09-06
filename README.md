<div align="center">
    <p>
        <img src="https://raw.githubusercontent.com/Haight3/pycountry-convert/master/resources/images/logo.jpg" width="75%" alt="pycountry-convert-ng logo">
    </p>

<h2 align="center">pycountry-convert-ng v2026.9.0</h2>
<h4 align="center">Maintained country, ISO code, and continent conversions based on pycountry-convert 0.7.2.</h4>

<p align="center">
  <a href="#introduction">Introduction</a> &bull;
  <a href="#why-this-fork">Why This Fork?</a> &bull;
  <a href="#quick-start">Quick Start</a> &bull;
  <a href="#installation">Installation</a> &bull;
  <a href="#api">API</a> &bull;
  <a href="#development">Development</a>
</p>

<p align="center">
  <a href="https://pypi.org/project/pycountry-convert-ng/"><img src="https://img.shields.io/pypi/v/pycountry-convert-ng.svg" alt="PyPI"></a>
  <a href="https://github.com/Haight3/pycountry-convert/actions/workflows/ci.yml"><img src="https://github.com/Haight3/pycountry-convert/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <a href="https://github.com/Haight3/pycountry-convert/actions/workflows/deploy.yml"><img src="https://github.com/Haight3/pycountry-convert/actions/workflows/deploy.yml/badge.svg" alt="Deployment"></a>
</p>
</div>

# Introduction

`pycountry-convert-ng` is the maintained next-generation distribution of `pycountry-convert`. It converts between country names, ISO 3166-1 alpha-2 and alpha-3 country codes, and continent codes/names.

The Python import remains:

```python
import pycountry_convert as pc
```

The maintained distribution is installed as `pycountry-convert-ng`.

# Why this fork?

The original project is small and useful, particularly for the country-to-continent mapping that many larger country-code packages do not expose directly. Unfortunately, the repository historically referenced by the `0.7.2` package (`TuneLab/pycountry-convert`) is no longer available at that location, while other mirrors/forks can contain substantially older code.

For that reason this fork uses the published **`pycountry-convert 0.7.2` release implementation** as the compatibility baseline rather than the stale code that was initially present in this GitHub fork.

Haight maintains the surrounding project infrastructure: modern `pyproject.toml` packaging, current Python support, automated tests, CI, versioning, PyPI Trusted Publishing, and GitHub Releases. The upstream `0.7.2` implementation itself is intentionally kept recognizable and minimally modified; its package version is the only source-level metadata adapted to the NG release line.

The `0.7.2` implementation combines:

- `pycountry` for ISO country data
- additional Wikipedia-derived country-name aliases
- country alpha-2 to continent-code mappings
- continent-code to continent-name mappings
- country-name formatting modes (`default`, `lower`, `upper`)
- mapping helper functions for alpha-2, alpha-3, names, and numeric country data

# Installation

```bash
pip install pycountry-convert-ng
```

The import name stays compatible with the original package:

```python
import pycountry_convert as pc
```

# Quick Start

## Country code to continent

```python
import pycountry_convert as pc

continent_code = pc.country_alpha2_to_continent_code("DE")
continent_name = pc.convert_continent_code_to_continent_name(continent_code)

print(continent_code)  # EU
print(continent_name)  # Europe
```

## Alpha-3 code to continent

```python
alpha2 = pc.country_alpha3_to_country_alpha2("DEU")
continent_code = pc.country_alpha2_to_continent_code(alpha2)
continent = pc.convert_continent_code_to_continent_name(continent_code)

print(continent)  # Europe
```

## Country conversions

```python
pc.country_alpha2_to_country_name("DE")
# "Germany"

pc.country_alpha3_to_country_alpha2("DEU")
# "DE"

pc.country_name_to_country_alpha2("Germany")
# "DE"

pc.country_name_to_country_alpha3("Germany")
# "DEU"
```

Aliases from the original Wikipedia mapping are retained, for example:

```python
pc.country_name_to_country_alpha2("Great Britain")
# "GB"

pc.country_name_to_country_alpha2("South Korea")
# "KR"
```

# API

The principal public functions from the `0.7.2` API are:

| Function | Conversion |
| --- | --- |
| `country_alpha2_to_continent_code()` | ISO alpha-2 -> continent code |
| `convert_continent_code_to_continent_name()` | continent code -> continent name |
| `country_alpha2_to_country_name()` | ISO alpha-2 -> country name |
| `country_alpha3_to_country_alpha2()` | ISO alpha-3 -> ISO alpha-2 |
| `country_name_to_country_alpha2()` | country name -> ISO alpha-2 |
| `country_name_to_country_alpha3()` | country name -> ISO alpha-3 |
| `map_countries()` | combined country mapping |
| `map_country_name_to_country_alpha2()` | country-name -> alpha-2 mapping |
| `map_country_name_to_country_alpha3()` | country-name -> alpha-3 mapping |
| `map_country_alpha2_to_country_name()` | alpha-2 -> country-name mapping |
| `map_country_alpha3_to_country_name()` | alpha-3 -> country-name mapping |
| `map_country_alpha3_to_country_alpha2()` | alpha-3 -> alpha-2 mapping |
| `map_country_alpha2_to_country_alpha3()` | alpha-2 -> alpha-3 mapping |

Country names can be formatted with `COUNTRY_NAME_FORMAT_DEFAULT`, `COUNTRY_NAME_FORMAT_LOWER`, and `COUNTRY_NAME_FORMAT_UPPER`.

# Package Naming

```text
PyPI distribution:  pycountry-convert-ng
Python import:       pycountry_convert
```

This keeps existing Python imports familiar while giving the maintained fork an independent PyPI release line.

# Development

```bash
pip install -e ".[dev]"
pytest
ruff check src tests
python -m build
python -m twine check dist/*
```

The upstream implementation under `src/pycountry_convert/` is excluded from automatic Ruff rewriting so maintenance tooling does not silently rewrite the compatibility baseline.

# Release & PyPI

Versions use `YYYY.MM.PATCH`, for example `2026.9.0` and `2026.9.1`.

The release pipeline builds and validates wheel/sdist artifacts, installs the built wheel for a smoke test, publishes through PyPI Trusted Publishing, and only then creates the GitHub tag and Release.

# Attribution

`pycountry-convert-ng` is based on `pycountry-convert 0.7.2`, originally developed by TUNE / TuneLab contributors. Original copyright and license attribution are preserved in the source and `LICENSE` file.

The NG packaging, CI, testing, release automation, and ongoing maintenance are provided by Haight Labs.

# License

MIT. See [LICENSE](LICENSE).
