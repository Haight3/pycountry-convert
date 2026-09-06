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
4. Update `CHANGELOG.md` so the release version has a matching heading.
5. Open a pull request from `release-candidate` to `master`.
6. CI and release metadata validation must pass.
7. Merging to `master` builds and validates the distributions.
8. The built wheel is installed and smoke-tested.
9. The verified distributions are published to PyPI as `pycountry-convert-ng` through Trusted Publishing.
10. Only after PyPI succeeds is the Git tag and GitHub Release created.

The PyPI publisher is bound to the GitHub environment `pypi`; no PyPI API token is stored in GitHub.
