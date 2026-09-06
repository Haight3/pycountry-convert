# pycountry-convert-ng

`pycountry-convert-ng` is the maintained next-generation distribution of `pycountry-convert`. It provides fast in-memory conversion between country names, ISO 3166-1 alpha-2 / alpha-3 codes, and continent names.

The Python import package remains `pycountry_convert`, preserving the existing public API.

## Installation

From PyPI:

```bash
python -m pip install pycountry-convert-ng
```

From the repository:

```bash
python -m pip install "git+https://github.com/Haight3/pycountry-convert.git"
```

For development:

```bash
python -m pip install -e ".[dev]"
pre-commit install
```

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
build + installation verification
        ↓
PyPI Trusted Publishing
        ↓
GitHub tag + GitHub Release
```

The package is published to PyPI as `pycountry-convert-ng` through Trusted Publishing. The import name remains `pycountry_convert`.

## License

MIT. See [LICENSE](LICENSE).
