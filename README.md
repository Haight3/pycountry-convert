# pycountry-convert

`pycountry-convert` provides fast in-memory conversion between country names, ISO 3166-1 alpha-2 / alpha-3 codes, and continent names.

This repository is a maintained fork of the original TuneLab project. The conversion tables and public conversion API are intentionally preserved; the surrounding packaging, testing, CI, and release infrastructure has been modernized.

## Installation

From the repository:

```bash
python -m pip install "git+https://github.com/Haight3/pycountry-convert.git"
```

For development:

```bash
python -m pip install -e ".[dev]"
pre-commit install
```

Release wheels and source distributions are attached to GitHub Releases. This fork does not automatically publish to the public PyPI project owned by the upstream package.

## Usage

```python
import pycountry_convert as pc

continent = pc.convert_country_alpha2_to_continent("DE")
country = pc.convert_country_alpha2_to_country_name("DE")
alpha2 = pc.convert_country_alpha3_to_country_alpha2("DEU")
alpha2_from_name = pc.convert_country_name_to_country_alpha2("Germany")

continent_from_alpha3 = pc.convert_country_alpha2_to_continent(
    pc.convert_country_alpha3_to_country_alpha2("DEU")
)
```

The public functions are:

- `convert_country_alpha2_to_continent()`
- `convert_country_alpha2_to_country_name()`
- `convert_country_alpha3_to_country_alpha2()`
- `convert_country_name_to_country_alpha2()`

Unknown keys retain the legacy behavior and raise `KeyError` where applicable.

## Repository layout

```text
.
├── .github/
│   └── workflows/
├── data/
├── examples/
├── src/
│   └── pycountry_convert/
├── tests/
├── pyproject.toml
└── README.md
```

## Release flow

The repository follows the same release model used by other Haight Python projects:

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
build + installation verification + GitHub Release
```

The package version is managed with `bumpver`. Git tags are created only after the release artifacts have been built and verified successfully.

## License

MIT. See [LICENSE](LICENSE).
