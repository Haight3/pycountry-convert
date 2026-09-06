# Contributing

## Development setup

```bash
python -m pip install -e ".[dev]"
pre-commit install
```

Run validation locally with:

```bash
ruff check src tests
python -m pytest
python -m build
python -m twine check dist/*
```

## Source policy

The legacy conversion implementation under `src/pycountry_convert/` is intentionally kept stable. Infrastructure changes should not alter mapping behavior without dedicated tests and an explicit review of backward compatibility.

## Release flow

1. Develop on a feature branch.
2. Merge into `release-candidate` after CI passes.
3. The version workflow increments the package version on `release-candidate`.
4. Update `src/.info/CHANGELOG.md` so the release version has a matching heading.
5. Open a pull request from `release-candidate` to `master`.
6. CI and release metadata validation must pass.
7. Merging to `master` builds and verifies the distribution.
8. The verified wheel and source distribution are published to PyPI as `pycountry-convert-ng` through the `pypi` environment using Trusted Publishing.
9. The Git tag and GitHub Release are created only after the PyPI publication succeeds.

No PyPI API token is stored in GitHub. The deployment uses OpenID Connect with the PyPI Trusted Publisher configured for `Haight3/pycountry-convert`, workflow `deploy.yml`, environment `pypi`.
